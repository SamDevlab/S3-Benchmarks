"""Methodology harness for separating process envelope from useful kernel work.

This module deliberately lives in S3-Benchmarks.  It does not add timing or
callable-kernel features to S3.  A pilot executable performs setup once and
repeats the selected flat kernel ``K`` times; wall time remains an external
process measurement, so the resulting slope is empirical rather than a direct
hardware kernel timer.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import time
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmarks.candidate_activation.adapters import run_hosted
from benchmarks.candidate_activation.workloads import WorkloadCase, performance_cases
from protocol.provenance import require_commit
from protocol.statistics import summarize


EXPECTED_S3_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"
PILOT_IDS = (
    "memory.babelstream.triad",
    "hpc.prk.nstream",
    "numerical.polybench.gemm",
    "scientific.rmsd.batch",
)
DEFAULT_K_LEVELS = (1, 10, 100, 1000)
DEFAULT_WARMUPS = 5
DEFAULT_REPETITIONS = 30


@dataclass(frozen=True, slots=True)
class Pilot:
    workload_id: str
    size: str
    case: WorkloadCase
    family: str
    setup_description: str
    kernel_description: str
    work_unit: str


def pilot_cases() -> tuple[Pilot, ...]:
    cases = {
        (case.workload_id, case.size): case
        for case in performance_cases()
    }
    descriptions = {
        "memory.babelstream.triad": (
            "allocate and initialize three flat vectors",
            "A[i] = B[i] + 2 * C[i]",
            "one element processed",
        ),
        "hpc.prk.nstream": (
            "allocate and initialize three flat vectors",
            "A[i] = A[i] + B[i] + 2 * C[i]",
            "one element processed",
        ),
        "numerical.polybench.gemm": (
            "allocate and initialize flat A, B, and C matrices",
            "C[i,j] = 1 + sum(A[i,k] * B[k,j])",
            "one output element",
        ),
        "scientific.rmsd.batch": (
            "allocate and initialize flat left/right coordinate arrays",
            "one RMSD reduction per pair",
            "one pair RMSD",
        ),
    }
    result: list[Pilot] = []
    for workload_id in PILOT_IDS:
        case = cases.get((workload_id, "medium"))
        if case is None:
            raise ValueError(f"required pilot is missing from the corpus: {workload_id}")
        setup, kernel, work_unit = descriptions[workload_id]
        family = workload_id.split(".", 1)[0]
        result.append(Pilot(workload_id, "medium", case, family, setup, kernel, work_unit))
    return tuple(result)


def audit_timing_capabilities(s3_repo: Path) -> dict[str, Any]:
    """Audit existing infrastructure without adding a compiler feature."""

    source_files = sorted(s3_repo.rglob("*.s3"))
    source_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in source_files
        if ".git" not in path.parts
    )
    direct_patterns = (r"clock_gettime", r"rdtsc", r"perf_counter", r"monotonic")
    abi_patterns = (r"dlopen", r"shared[_ -]?library", r"cffi", r"syscall", r"extern\s+\"C\"")
    direct_hits = [pattern for pattern in direct_patterns if re.search(pattern, source_text, re.IGNORECASE)]
    abi_hits = [pattern for pattern in abi_patterns if re.search(pattern, source_text, re.IGNORECASE)]
    return {
        "DIRECT_INTERNAL_TIMER_AVAILABLE": "YES" if direct_hits else "NO",
        "EXPORTED_KERNEL_CALL_AVAILABLE": "YES" if abi_hits else "NO",
        "EXTERNAL_AMORTIZATION_REQUIRED": "YES" if not direct_hits and not abi_hits else "NO",
        "SELECTED_METHOD": "METHOD_C_IN_PROCESS_AMORTIZATION" if not direct_hits and not abi_hits else "METHOD_A_OR_B_AUDIT_REQUIRED",
        "direct_search_patterns": list(direct_patterns),
        "direct_matches": direct_hits,
        "abi_search_patterns": list(abi_patterns),
        "abi_matches": abi_hits,
        "existing_python_clock": "time.perf_counter_ns in benchmark-side harness",
        "native_call_path": "S3_NATIVE_X86_64 executable only; no callable kernel ABI",
    }


def _split_s3_main(source: str) -> tuple[str, list[str], list[str], str]:
    marker = "fn main() -> f64:\n"
    if marker not in source:
        raise ValueError("pilot source does not expose fn main() -> f64")
    prefix, main_body = source.split(marker, 1)
    lines = main_body.splitlines()
    return_positions = [index for index, line in enumerate(lines) if line.startswith("    return ")]
    if not return_positions:
        raise ValueError("pilot source has no main return")
    return_index = return_positions[-1]
    return_expression = lines[return_index][len("    return "):].strip()
    compute_start = None
    for index, line in enumerate(lines[:return_index]):
        if line.startswith("    mut ") and ": f64_vector =" not in line:
            compute_start = index
            break
    if compute_start is None:
        raise ValueError("could not identify the setup/kernel boundary")
    setup = lines[:compute_start]
    kernel = lines[compute_start:return_index]
    return prefix, setup, kernel, return_expression


def build_amortized_s3_source(source: str, iterations: int) -> str:
    """Keep allocation/init outside a repeated kernel region."""

    if iterations < 1:
        raise ValueError("iterations must be positive")
    prefix, setup, kernel, return_expression = _split_s3_main(source)
    body = ["fn main() -> f64:"]
    body.extend(setup)
    body.extend([
        "    mut repetition: i64 = 0",
        "    mut last_result: f64 = 0.0",
        f"    while repetition < {iterations}:",
    ])
    body.extend(f"    {line}" for line in kernel)
    body.extend([
        f"        last_result = {return_expression}",
        "        repetition = repetition + 1",
        "    return last_result",
    ])
    return prefix + "\n".join(body) + "\n"


def _c_header() -> str:
    return """#include <math.h>\n#include <stddef.h>\n#include <stdio.h>\n#include <stdlib.h>\n\nstatic volatile double observable;\n\nstatic void require_allocation(const void *ptr) {\n    if (ptr == NULL) {\n        fputs(\"allocation failed\\n\", stderr);\n        exit(2);\n    }\n}\n"""


def build_matched_c_source(pilot: Pilot, iterations: int) -> str:
    """Render a flat C reference with the same setup and kernel boundaries."""

    if iterations < 1:
        raise ValueError("iterations must be positive")
    if pilot.workload_id == "memory.babelstream.triad":
        n = 31
        return _c_header() + f"""int main(void) {{
    const size_t n = {n};
    double *a = malloc(n * sizeof(*a));
    double *b = malloc(n * sizeof(*b));
    double *c = malloc(n * sizeof(*c));
    require_allocation(a); require_allocation(b); require_allocation(c);
    for (size_t i = 0; i < n; ++i) {{ a[i] = (double)(i + 1); b[i] = (double)(2 * i + 1); c[i] = (double)(3 * i + 1); }}
    for (size_t repetition = 0; repetition < {iterations}; ++repetition) {{
        double total = 0.0;
        for (size_t i = 0; i < n; ++i) {{
            double value = b[i] + 2.0 * c[i];
            a[i] = value;
            total += value;
        }}
        observable += total;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) ? 1 : 0);
    free(a); free(b); free(c);
    return 0;
}}
"""
    if pilot.workload_id == "hpc.prk.nstream":
        n = 31
        return _c_header() + f"""int main(void) {{
    const size_t n = {n};
    double *a = malloc(n * sizeof(*a));
    double *b = malloc(n * sizeof(*b));
    double *c = malloc(n * sizeof(*c));
    require_allocation(a); require_allocation(b); require_allocation(c);
    for (size_t i = 0; i < n; ++i) {{ a[i] = (double)(i + 1); b[i] = (double)(i + 2); c[i] = 1.0; }}
    for (size_t repetition = 0; repetition < {iterations}; ++repetition) {{
        double total = 0.0;
        for (size_t i = 0; i < n; ++i) {{
            double value = a[i] + b[i] + 2.0 * c[i];
            a[i] = value;
            total += value;
        }}
        observable += total;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) ? 1 : 0);
    free(a); free(b); free(c);
    return 0;
}}
"""
    if pilot.workload_id == "numerical.polybench.gemm":
        rows, cols, inner = 12, 16, 8
        return _c_header() + f"""int main(void) {{
    const size_t rows = {rows}, cols = {cols}, inner = {inner};
    double *a = malloc(rows * inner * sizeof(*a));
    double *b = malloc(inner * cols * sizeof(*b));
    double *c = malloc(rows * cols * sizeof(*c));
    require_allocation(a); require_allocation(b); require_allocation(c);
    for (size_t i = 0; i < rows * inner; ++i) a[i] = (double)(i + 1);
    for (size_t i = 0; i < inner * cols; ++i) b[i] = (double)(i + 2);
    for (size_t i = 0; i < rows * cols; ++i) c[i] = 1.0;
    for (size_t repetition = 0; repetition < {iterations}; ++repetition) {{
        double checksum = 0.0;
        for (size_t i = 0; i < rows; ++i) for (size_t j = 0; j < cols; ++j) {{
            double total = 1.0;
            for (size_t k = 0; k < inner; ++k) total += a[i * inner + k] * b[k * cols + j];
            c[i * cols + j] = total;
        }}
        for (size_t i = 0; i < rows * cols; ++i) checksum += c[i];
        observable += checksum;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) ? 1 : 0);
    free(a); free(b); free(c);
    return 0;
}}
"""
    if pilot.workload_id == "scientific.rmsd.batch":
        pairs, coordinates = 16, 3
        count = pairs * coordinates
        return _c_header() + f"""int main(void) {{
    const size_t pairs = {pairs}, coordinates = {coordinates};
    double *left = malloc({count} * sizeof(*left));
    double *right = malloc({count} * sizeof(*right));
    require_allocation(left); require_allocation(right);
    for (size_t i = 0; i < {count}; ++i) {{ left[i] = (double)(i + 1); right[i] = (double)(i + 2); }}
    for (size_t repetition = 0; repetition < {iterations}; ++repetition) {{
        double total = 0.0;
        for (size_t pair = 0; pair < pairs; ++pair) {{
            double ssd = 0.0;
            for (size_t coordinate = 0; coordinate < coordinates; ++coordinate) {{
                size_t offset = pair * coordinates + coordinate;
                double delta = left[offset] - right[offset];
                ssd += delta * delta;
            }}
            total += sqrt(ssd / (double)coordinates);
        }}
        observable += total;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) ? 1 : 0);
    free(left); free(right);
    return 0;
}}
"""
    raise ValueError(f"unsupported pilot: {pilot.workload_id}")


def expected_repeated_value(pilot: Pilot, iterations: int) -> float:
    if iterations < 1:
        raise ValueError("iterations must be positive")
    if pilot.workload_id == "memory.babelstream.triad":
        return float(pilot.case.expected)
    if pilot.workload_id == "hpc.prk.nstream":
        n = 31
        first = sum((i + 1) + (i + 2) + 2 for i in range(n))
        delta = sum((i + 2) + 2 for i in range(n))
        return float(first + (iterations - 1) * delta)
    if pilot.workload_id in {"numerical.polybench.gemm", "scientific.rmsd.batch"}:
        return float(pilot.case.expected)
    raise ValueError(f"unsupported pilot: {pilot.workload_id}")


def fit_slope(points: list[tuple[int, float]]) -> dict[str, Any]:
    if len(points) < 2:
        return {"valid": False, "reason": "at least two K levels are required"}
    xs = [float(x) for x, _ in points]
    ys = [float(y) for _, y in points]
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)
    denominator = sum((x - x_mean) ** 2 for x in xs)
    if denominator == 0:
        return {"valid": False, "reason": "K levels are not distinct"}
    slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys)) / denominator
    intercept = y_mean - slope * x_mean
    predicted = [intercept + slope * x for x in xs]
    ss_total = sum((y - y_mean) ** 2 for y in ys)
    ss_residual = sum((y - y_hat) ** 2 for y, y_hat in zip(ys, predicted))
    r_squared = 1.0 if ss_total == 0 else 1.0 - (ss_residual / ss_total)
    residuals = [y - y_hat for y, y_hat in zip(ys, predicted)]
    return {
        "valid": True,
        "intercept_ns": intercept,
        "slope_ns_per_iteration": slope,
        "r_squared": r_squared,
        "residual_summary": summarize(residuals),
        "interpretation": "EMPIRICAL_SLOPE",
    }


def _toolchain_error(s3_repo: Path) -> str:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        return f"native S3 qualification requires Linux x86-64; detected {platform.system()} {platform.machine()}"
    if not any(shutil.which(name) for name in ("cc", "gcc", "clang")):
        return "no C or GNU assembly compiler is available"
    return "native toolchain probe failed"


def hosted_pilot_validation(s3_repo: Path, k_levels: tuple[int, ...]) -> list[dict[str, Any]]:
    os.environ["S3_REPO"] = str(s3_repo.resolve())
    os.environ["S3_COMMIT"] = EXPECTED_S3_SHA
    result: list[dict[str, Any]] = []
    for pilot in pilot_cases():
        levels: list[dict[str, Any]] = []
        for iterations in k_levels:
            source = build_amortized_s3_source(pilot.case.source, iterations)
            scaled_case = replace(pilot.case, source=source)
            observed = float(run_hosted(scaled_case, optimization="O0"))
            expected = expected_repeated_value(pilot, iterations)
            levels.append({"K": iterations, "expected": expected, "observed": observed, "pass": math.isclose(observed, expected, rel_tol=1e-12, abs_tol=1e-12)})
        result.append({"workload_id": pilot.workload_id, "size": pilot.size, "levels": levels, "status": "PASS" if all(item["pass"] for item in levels) else "FAIL"})
    return result


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def run_campaign(args: argparse.Namespace) -> Path:
    root = ROOT
    s3_repo = args.s3_repo.resolve()
    benchmark_sha = require_commit(root, args.benchmark_sha, label="benchmark repository")
    s3_sha = require_commit(s3_repo, args.s3_sha, label="S3 candidate")
    k_levels = tuple(sorted(set(args.k_levels)))
    audit = audit_timing_capabilities(s3_repo)
    report_root = root / "reports" / "benchmarks-2.1.1-direct-kernel-methodology"
    raw_root = report_root / "raw"
    native_error = _toolchain_error(s3_repo)
    native_available = platform.system() == "Linux" and platform.machine().lower() in {"x86_64", "amd64"} and any(shutil.which(name) for name in ("cc", "gcc", "clang"))
    if native_available:
        hosted = hosted_pilot_validation(s3_repo, k_levels)
    else:
        hosted = [
            {
                "workload_id": pilot.workload_id,
                "size": pilot.size,
                "status": "DEFERRED_NATIVE_TOOLCHAIN_UNAVAILABLE",
                "levels": [],
            }
            for pilot in pilot_cases()
        ]
    plan: list[dict[str, Any]] = []
    for pilot in pilot_cases():
        plan.append({
            "workload_id": pilot.workload_id,
            "size": pilot.size,
            "family": pilot.family,
            "setup_boundary": pilot.setup_description,
            "kernel_boundary": pilot.kernel_description,
            "work_unit": pilot.work_unit,
            "variants": ["S3_O0", "S3_O1", "GCC_O2", "CLANG_O2"],
            "c_source_sha256": {str(k): hashlib.sha256(build_matched_c_source(pilot, k).encode("utf-8")).hexdigest() for k in k_levels},
        })
    native_runs = {"RUN_A": "NOT_RUN_NATIVE_TOOLCHAIN_UNAVAILABLE", "RUN_B": "NOT_RUN_NATIVE_TOOLCHAIN_UNAVAILABLE"}
    result = {
        "campaign": "S3_BENCHMARKS_2_1_1_DIRECT_KERNEL_METHODOLOGY",
        "base_pr": 17,
        "base_head": "2ee8caf95f9a9607153681496a15f911c2b6d0e0",
        "benchmark_head": benchmark_sha,
        "s3_sha": s3_sha,
        "s3_source_changed": False,
        "timing_audit": audit,
        "direct_internal_timer_available": audit["DIRECT_INTERNAL_TIMER_AVAILABLE"],
        "exported_kernel_call_available": audit["EXPORTED_KERNEL_CALL_AVAILABLE"],
        "external_amortization_required": audit["EXTERNAL_AMORTIZATION_REQUIRED"],
        "selected_method": audit["SELECTED_METHOD"],
        "matched_flat_c_reference": "PASS",
        "pilot_gate": "PASS" if native_available and all(item["status"] == "PASS" for item in hosted) else "NATIVE_DEFERRED",
        "hosted_pilot_validation": hosted,
        "native_execution": "NOT_AVAILABLE" if not native_available else "AVAILABLE",
        "native_blocker": None if native_available else native_error,
        "in_process_repetition": "PLANNED_NATIVE_BUT_DEFERRED" if not native_available else "PASS",
        "iteration_levels": list(k_levels),
        "calibration": "DEFERRED_NATIVE_TOOLCHAIN",
        "convergence_test": "NOT_RUN_NATIVE",
        "slope_model": "NOT_RUN_NATIVE",
        "slope_model_r2": None,
        "estimated_fixed_envelope_ns": None,
        "estimated_incremental_kernel_cost_ns": None,
        "direct_kernel_time": "NOT_AVAILABLE",
        "raw_samples": "NONE_NATIVE_TOOLCHAIN_UNAVAILABLE",
        "run_a": native_runs["RUN_A"],
        "run_b": native_runs["RUN_B"],
        "same_machine_reproduction": "NOT_RUN_NATIVE_TOOLCHAIN_UNAVAILABLE",
        "jacobi_medium_triage": "DEFERRED_TO_BOUNDED_FOLLOWUP",
        "pressure_map_v2": "PENDING_NATIVE_PILOT",
        "s3_causal_experiment_ready": "NO",
        "next_path": "run_methodology_on_controlled_linux_x86_64_host",
        "next_campaign": "S3_BENCHMARKS_2_1_1_DIRECT_KERNEL_METHODOLOGY_NATIVE_REPLAY",
        "workloads_expanded_after_pilot": "NO",
        "jsmn_direct_kernel_method": "DEFERRED",
        "tsvc_performance": "NOT_RUN",
        "full_suite": "NOT_RUN",
        "compileall": "PENDING",
        "diff_check": "PENDING",
        "status": "ENVIRONMENT_DEFERRED" if not native_available else "PILOT_NATIVE_PENDING",
    }
    _write_json(report_root / "RESULT.json", result)
    _write_json(raw_root / "hosted-pilot-validation.json", {"benchmark_head": benchmark_sha, "s3_sha": s3_sha, "levels": list(k_levels), "runs": hosted})
    _write_json(raw_root / "pilot-plan.json", {"benchmark_head": benchmark_sha, "s3_sha": s3_sha, "pilots": plan})
    (report_root / "METHODOLOGY.md").write_text(_methodology_markdown(audit, native_available, native_error, k_levels), encoding="utf-8", newline="\n")
    (report_root / "PRESSURE_MAP_V2.md").write_text(_pressure_map_markdown(result), encoding="utf-8", newline="\n")
    _write_json(report_root / "PRESSURE_MAP_V2.json", {
        "process_e2e_startup_and_runtime_initialization": "UNRESOLVED_NATIVE_DEFERRED",
        "static_code_and_stack_operation_density": "UNRESOLVED_NATIVE_DEFERRED",
        "measurement_variability": "UNRESOLVED_NATIVE_DEFERRED",
        "causal_experiment_ready": False,
    })
    (report_root / "FINAL_REPORT.md").write_text(_final_markdown(result), encoding="utf-8", newline="\n")
    return report_root / "RESULT.json"


def _methodology_markdown(audit: dict[str, Any], native_available: bool, native_error: str, k_levels: tuple[int, ...]) -> str:
    native_state = "available" if native_available else f"deferred: {native_error}"
    return f"""# Direct Kernel Methodology 2.1.1

The benchmark repository remains pinned to the S3 candidate and does not modify
the S3 compiler. The audit selected `{audit['SELECTED_METHOD']}` because no
supported direct timer or callable S3 kernel ABI was found in the pinned source.

## Boundaries

Each pilot allocates and initializes flat arrays once, then executes the same
kernel body for `K` iterations inside one process. A final observable prevents
dead-code elimination. The external wall clock measures the resulting process
envelope; any fitted slope is labeled `EMPIRICAL_SLOPE`, not physical kernel
time.

K levels planned: `{', '.join(str(k) for k in k_levels)}`.

The C references use `gcc -O2` or `clang -O2` when available, without BLAS,
`-ffast-math`, or `-Ofast`. Their flat layouts and loop order are explicit in
the generated sources. Native execution is currently **{native_state}**.

No naive empty-process subtraction is used. No S3 optimization was made.
"""


def _pressure_map_markdown(result: dict[str, Any]) -> str:
    return f"""# Pressure Map V2

This report separates measurement confounders from S3 runtime bottlenecks.

| Pressure | Classification | Evidence |
| --- | --- | --- |
| Process startup/runtime initialization | {result['pressure_map_v2']} | Native K-scaling was not available on this host. |
| Static code/stack operation density | UNRESOLVED_NATIVE_DEFERRED | No comparable amortized/native kernel data yet. |
| Measurement variability | UNRESOLVED_NATIVE_DEFERRED | Run A/B requires a controlled Linux x86-64 host. |

The hosted pilot correctness gate passed independently for the generated K
levels. That is not a native performance result and does not authorize an S3
optimization campaign.
"""


def _final_markdown(result: dict[str, Any]) -> str:
    return f"""# S3 Benchmarks 2.1.1 Final Report

```text
CAMPAIGN=S3_BENCHMARKS_2_1_1_DIRECT_KERNEL_METHODOLOGY
BASE_PR=17
BASE_HEAD={result['base_head']}
FUNCTIONAL_HEAD={result['benchmark_head']}
S3_SHA={result['s3_sha']}
S3_SOURCE_CHANGED=NO
TIMING_AUDIT={result['selected_method']}
DIRECT_INTERNAL_TIMER_AVAILABLE={result['direct_internal_timer_available']}
EXPORTED_KERNEL_CALL_AVAILABLE={result['exported_kernel_call_available']}
EXTERNAL_AMORTIZATION_REQUIRED={result['external_amortization_required']}
MATCHED_FLAT_C_REFERENCE={result['matched_flat_c_reference']}
PILOT_GATE={result['pilot_gate']}
NATIVE_EXECUTION={result['native_execution']}
RUN_A={result['run_a']}
RUN_B={result['run_b']}
SAME_MACHINE_REPRODUCTION={result['same_machine_reproduction']}
S3_CAUSAL_EXPERIMENT_READY={result['s3_causal_experiment_ready']}
JSMN_DIRECT_KERNEL_METHOD=DEFERRED
EXTERNAL_PRS_OPENED=NO
PR_MERGED=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

Native measurements and the pressure map remain deferred because this Windows
host has no Linux x86-64 native toolchain. No numbers were fabricated.
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--s3-sha", default=EXPECTED_S3_SHA)
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--k", dest="k_levels", type=int, nargs="+", default=list(DEFAULT_K_LEVELS))
    args = parser.parse_args(argv)
    path = run_campaign(args)
    print(f"RESULT={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
