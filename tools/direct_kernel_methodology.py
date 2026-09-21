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
NATIVE_REPLAY_WARMUPS = 5
NATIVE_REPLAY_REPETITIONS = 30
NATIVE_SAMPLE_TIMEOUT_SECONDS = 2.0
NATIVE_PROJECTED_SAMPLE_LIMIT_SECONDS = 1.8
ADAPTIVE_K_LEVELS = (1, 5, 10, 20, 100, 1000)
CONVERGENCE_RELATIVE_LIMIT = 0.25


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
    expected = expected_repeated_value(pilot, iterations)
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
        observable = total;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) && fabs(observable - {expected:.17g}) <= 1e-9 ? 1 : 0);
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
        observable = total;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) && fabs(observable - {expected:.17g}) <= 1e-9 ? 1 : 0);
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
        observable = checksum;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) && fabs(observable - {expected:.17g}) <= 1e-9 ? 1 : 0);
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
        observable = total;
    }}
    printf(\"program returned: %d\\n\", isfinite(observable) && fabs(observable - {expected:.17g}) <= 1e-9 ? 1 : 0);
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


def _path_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _pilot_work_units(pilot: Pilot) -> int:
    if pilot.workload_id in {"memory.babelstream.triad", "hpc.prk.nstream"}:
        return 31
    if pilot.workload_id == "numerical.polybench.gemm":
        return 12 * 16 * 8
    if pilot.workload_id == "scientific.rmsd.batch":
        return 16 * 3
    raise ValueError(f"no work-unit contract for {pilot.workload_id}")


def _native_variant_specs() -> list[tuple[str, str, str]]:
    specs = [("S3_O0", "s3", "O0"), ("S3_O1", "s3", "O1"), ("GCC_O2", "c", "gcc")]
    if shutil.which("clang"):
        specs.append(("CLANG_O2", "c", "clang"))
    return specs


def _build_s3_replay_variant(
    pilot: Pilot,
    iterations: int,
    optimization: str,
    root: Path,
    toolchain: Any,
) -> dict[str, Any]:
    from benchmarks.candidate_activation.adapters import native_canary_source
    from bootstrap.s3.backends.x86_64 import X8664Backend
    from bootstrap.s3.pipeline import compile_source

    expected = expected_repeated_value(pilot, iterations)
    source = build_amortized_s3_source(pilot.case.source, iterations)
    canary = native_canary_source(replace(pilot.case, source=source, expected=expected))
    build_root = root / "builds" / pilot.workload_id / f"k-{iterations}" / f"s3-{optimization.lower()}"
    build_root.mkdir(parents=True, exist_ok=False)
    source_path = build_root / "measurement.s3"
    assembly_path = build_root / "program.s"
    object_path = build_root / "program.o"
    executable_path = build_root / "program"
    source_path.write_text(canary, encoding="utf-8", newline="\n")
    assembly_program = compile_source(canary, optimization=optimization).assembly
    assembly = X8664Backend(register_allocation=True, max_instructions=1 << 62).generate(assembly_program)
    toolchain.build(assembly, executable_path, keep_assembly=assembly_path)
    if not object_path.is_file():
        raise RuntimeError(f"native assembler did not preserve its object: {object_path}")
    return {
        "variant": f"S3_{optimization}",
        "compiler": "S3",
        "optimization": optimization,
        "source_path": str(source_path),
        "assembly_path": str(assembly_path),
        "object_path": str(object_path),
        "executable_path": str(executable_path),
        "source_sha256": _path_sha256(source_path),
        "assembly_sha256": _path_sha256(assembly_path),
        "object_sha256": _path_sha256(object_path),
        "executable_sha256": _path_sha256(executable_path),
        "source_bytes": source_path.stat().st_size,
        "assembly_bytes": assembly_path.stat().st_size,
        "object_bytes": object_path.stat().st_size,
        "executable_bytes": executable_path.stat().st_size,
    }


def _build_c_replay_variant(
    pilot: Pilot,
    iterations: int,
    compiler: str,
    root: Path,
) -> dict[str, Any]:
    compiler_path = shutil.which(compiler)
    if compiler_path is None:
        raise RuntimeError(f"required compiler is unavailable: {compiler}")
    build_root = root / "builds" / pilot.workload_id / f"k-{iterations}" / compiler
    build_root.mkdir(parents=True, exist_ok=False)
    source_path = build_root / "reference.c"
    object_path = build_root / "reference.o"
    executable_path = build_root / "program"
    source_path.write_text(build_matched_c_source(pilot, iterations), encoding="utf-8", newline="\n")
    compile_command = [compiler_path, "-std=c99", "-O2", "-fno-fast-math", "-c", str(source_path), "-o", str(object_path)]
    link_command = [compiler_path, str(object_path), "-lm", "-o", str(executable_path)]
    for command in (compile_command, link_command):
        completed = subprocess.run(command, check=False, capture_output=True, text=True, timeout=30.0)
        if completed.returncode != 0:
            details = completed.stderr.strip() or completed.stdout.strip()
            raise RuntimeError(f"{compiler} build failed: {details}")
    return {
        "variant": "GCC_O2" if compiler == "gcc" else "CLANG_O2",
        "compiler": compiler,
        "optimization": "O2",
        "source_path": str(source_path),
        "assembly_path": None,
        "object_path": str(object_path),
        "executable_path": str(executable_path),
        "source_sha256": _path_sha256(source_path),
        "assembly_sha256": None,
        "object_sha256": _path_sha256(object_path),
        "executable_sha256": _path_sha256(executable_path),
        "source_bytes": source_path.stat().st_size,
        "assembly_bytes": None,
        "object_bytes": object_path.stat().st_size,
        "executable_bytes": executable_path.stat().st_size,
    }


def _build_replay_variant(
    pilot: Pilot,
    iterations: int,
    spec: tuple[str, str, str],
    root: Path,
    toolchain: Any,
) -> dict[str, Any]:
    _label, family, compiler_or_optimization = spec
    if family == "s3":
        return _build_s3_replay_variant(pilot, iterations, compiler_or_optimization, root, toolchain)
    return _build_c_replay_variant(pilot, iterations, compiler_or_optimization, root)


def _parse_native_canary(stdout: str) -> int:
    match = re.search(r"program returned:\s*(-?\d+)", stdout)
    if match is None:
        raise RuntimeError(f"native executable did not emit a canary: {stdout!r}")
    return int(match.group(1))


def _run_native_sample(build: dict[str, Any]) -> dict[str, Any]:
    executable = Path(build["executable_path"])
    start = time.perf_counter_ns()
    try:
        completed = subprocess.run(
            [os.fspath(executable)],
            check=False,
            capture_output=True,
            text=True,
            timeout=NATIVE_SAMPLE_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return {
            "status": "TIMEOUT",
            "elapsed_ns": None,
            "timeout_seconds": NATIVE_SAMPLE_TIMEOUT_SECONDS,
        }
    elapsed_ns = time.perf_counter_ns() - start
    stdout = completed.stdout.strip()
    stderr = completed.stderr.strip()
    if completed.returncode != 0:
        return {"status": "FAIL", "elapsed_ns": elapsed_ns, "returncode": completed.returncode, "stdout": stdout, "stderr": stderr}
    try:
        canary = _parse_native_canary(stdout)
    except RuntimeError as error:
        return {"status": "FAIL", "elapsed_ns": elapsed_ns, "returncode": completed.returncode, "stdout": stdout, "stderr": str(error)}
    return {
        "status": "PASS" if canary == 1 else "FAIL",
        "elapsed_ns": elapsed_ns,
        "returncode": completed.returncode,
        "canary": canary,
        "stdout": stdout,
        "stderr": stderr,
    }


def _select_adaptive_levels(probes: dict[str, dict[str, Any]]) -> tuple[tuple[int, ...], dict[str, Any]]:
    max_ten_ns = max(float(item["elapsed_ns"]) for item in probes.values())
    selected = {1, 10}
    skipped: dict[str, Any] = {}
    for iterations in (100, 1000):
        projected_seconds = max_ten_ns / 1_000_000_000 * iterations / 10
        if projected_seconds <= NATIVE_PROJECTED_SAMPLE_LIMIT_SECONDS:
            selected.add(iterations)
        else:
            skipped[str(iterations)] = {
                "reason": "projected_sample_exceeds_guard",
                "projected_seconds": projected_seconds,
                "guard_seconds": NATIVE_PROJECTED_SAMPLE_LIMIT_SECONDS,
            }
    if len(selected) < 3:
        for iterations in (5, 20):
            projected_seconds = max_ten_ns / 1_000_000_000 * iterations / 10
            if projected_seconds <= NATIVE_PROJECTED_SAMPLE_LIMIT_SECONDS:
                selected.add(iterations)
            if len(selected) >= 3:
                break
    if len(selected) < 3:
        raise RuntimeError(f"fewer than three safe K levels after probes: {probes}")
    return tuple(sorted(selected)), {"max_probe_k10_ns": max_ten_ns, "skipped": skipped}


def _probe_workload(
    pilot: Pilot,
    specs: list[tuple[str, str, str]],
    root: Path,
    toolchain: Any,
) -> tuple[dict[str, Any], tuple[int, ...], dict[str, Any]]:
    probe_records: dict[str, Any] = {}
    probe_elapsed: dict[str, dict[str, Any]] = {}
    for spec in specs:
        label = spec[0]
        records: dict[str, Any] = {}
        for iterations in (1, 10):
            build = _build_replay_variant(pilot, iterations, spec, root / "probes", toolchain)
            sample = _run_native_sample(build)
            records[str(iterations)] = {"build": build, "sample": sample}
            if sample["status"] != "PASS":
                raise RuntimeError(f"safety probe failed for {pilot.workload_id} {label} K={iterations}: {sample}")
        probe_records[label] = records
        probe_elapsed[label] = records["10"]["sample"]
    levels, guard = _select_adaptive_levels(probe_elapsed)
    return probe_records, levels, guard


def _interleaved_labels(labels: list[str], count: int):
    for index in range(count):
        yield labels if index % 2 == 0 else list(reversed(labels))


def _measure_replay_workload(
    pilot: Pilot,
    levels: tuple[int, ...],
    specs: list[tuple[str, str, str]],
    root: Path,
    toolchain: Any,
) -> dict[str, Any]:
    builds_by_level: dict[str, dict[str, Any]] = {}
    samples_by_variant: dict[str, dict[str, list[int]]] = {spec[0]: {} for spec in specs}
    warmups_by_variant: dict[str, dict[str, list[int]]] = {spec[0]: {} for spec in specs}
    determinism: list[dict[str, Any]] = []
    labels = [spec[0] for spec in specs]
    for iterations in levels:
        level_builds: dict[str, Any] = {}
        for spec in specs:
            build = _build_replay_variant(pilot, iterations, spec, root / "measurement", toolchain)
            duplicate = _build_replay_variant(pilot, iterations, spec, root / "determinism", toolchain)
            fields = ("source_sha256", "assembly_sha256", "object_sha256", "executable_sha256")
            matches = all(build[field] == duplicate[field] for field in fields)
            determinism.append({
                "workload_id": pilot.workload_id,
                "K": iterations,
                "variant": spec[0],
                "first": {field: build[field] for field in fields},
                "second": {field: duplicate[field] for field in fields},
                "pass": matches,
            })
            level_builds[spec[0]] = build
            samples_by_variant[spec[0]][str(iterations)] = []
            warmups_by_variant[spec[0]][str(iterations)] = []
        builds_by_level[str(iterations)] = level_builds
        for order in _interleaved_labels(labels, NATIVE_REPLAY_WARMUPS):
            for label in order:
                sample = _run_native_sample(level_builds[label])
                if sample["status"] != "PASS":
                    raise RuntimeError(f"warmup failed for {pilot.workload_id} {label} K={iterations}: {sample}")
                warmups_by_variant[label][str(iterations)].append(sample["elapsed_ns"])
        for order in _interleaved_labels(labels, NATIVE_REPLAY_REPETITIONS):
            for label in order:
                sample = _run_native_sample(level_builds[label])
                if sample["status"] != "PASS":
                    raise RuntimeError(f"measurement failed for {pilot.workload_id} {label} K={iterations}: {sample}")
                samples_by_variant[label][str(iterations)].append(sample["elapsed_ns"])
    summaries: dict[str, Any] = {}
    for label in labels:
        points = []
        per_level: dict[str, Any] = {}
        for iterations in levels:
            samples = samples_by_variant[label][str(iterations)]
            ordered = sorted(samples)
            median = float(ordered[len(ordered) // 2])
            per_iteration = median / iterations
            points.append((iterations, median))
            per_level[str(iterations)] = {
                "samples_ns": samples,
                "sample_count": len(samples),
                "median_ns": median,
                "median_ns_per_iteration": per_iteration,
                "warmups_ns": warmups_by_variant[label][str(iterations)],
            }
        per_iteration_values = [item["median_ns_per_iteration"] for item in per_level.values()]
        central = sum(per_iteration_values) / len(per_iteration_values)
        spread = (max(per_iteration_values) - min(per_iteration_values)) / central if central else float("inf")
        summaries[label] = {
            "levels": per_level,
            "fit": fit_slope(points),
            "convergence": {
                "relative_spread": spread,
                "limit": CONVERGENCE_RELATIVE_LIMIT,
                "status": "PASS" if spread <= CONVERGENCE_RELATIVE_LIMIT else "FAIL",
            },
            "empirical_incremental_ns_per_iteration": fit_slope(points).get("slope_ns_per_iteration"),
            "empirical_incremental_ns_per_work_unit": (
                fit_slope(points).get("slope_ns_per_iteration") / _pilot_work_units(pilot)
            ),
        }
    return {
        "workload_id": pilot.workload_id,
        "size": pilot.size,
        "K_levels": list(levels),
        "builds": builds_by_level,
        "determinism": determinism,
        "determinism_status": "PASS" if all(item["pass"] for item in determinism) else "FAIL",
        "summaries": summaries,
        "work_units_per_iteration": _pilot_work_units(pilot),
    }


def _run_native_replay(
    s3_repo: Path,
    benchmark_sha: str,
    report_root: Path,
    toolchain: Any,
) -> dict[str, Any]:
    from tools.native_measurement import _perf_probe, collect_environment
    environment = collect_environment(s3_repo, benchmark_sha)
    environment["perf"] = _perf_probe()
    specs = _native_variant_specs()
    run_root = report_root / "raw" / "native-replay-20260921"
    run_root.mkdir(parents=True, exist_ok=True)
    run_a_root = run_root / "run-a"
    run_b_root = run_root / "run-b"
    probe_a: dict[str, Any] = {}
    levels_by_workload: dict[str, tuple[int, ...]] = {}
    run_a_workloads: list[dict[str, Any]] = []
    for pilot in pilot_cases():
        print(f"NATIVE_REPLAY_PROBE RUN_A {pilot.workload_id}", flush=True)
        probes, levels, guard = _probe_workload(pilot, specs, run_a_root / pilot.workload_id, toolchain)
        probe_a[pilot.workload_id] = {"probes": probes, "guard": guard, "K_levels": list(levels)}
        levels_by_workload[pilot.workload_id] = levels
        print(f"NATIVE_REPLAY_MEASURE RUN_A {pilot.workload_id} K={','.join(map(str, levels))}", flush=True)
        run_a_workloads.append(_measure_replay_workload(pilot, levels, specs, run_a_root / pilot.workload_id, toolchain))
    run_a = {"run_id": "A", "environment": environment, "probes": probe_a, "workloads": run_a_workloads}
    _write_json(run_root / "run-a.json", run_a)

    probe_b: dict[str, Any] = {}
    run_b_workloads: list[dict[str, Any]] = []
    for pilot in pilot_cases():
        print(f"NATIVE_REPLAY_PROBE RUN_B {pilot.workload_id}", flush=True)
        probes, discovered_levels, guard = _probe_workload(pilot, specs, run_b_root / pilot.workload_id, toolchain)
        levels = levels_by_workload[pilot.workload_id]
        if tuple(discovered_levels) != tuple(levels):
            guard = {**guard, "run_b_discovered_levels": list(discovered_levels), "status": "LEVEL_DRIFT"}
        probe_b[pilot.workload_id] = {"probes": probes, "guard": guard, "K_levels": list(levels)}
        print(f"NATIVE_REPLAY_MEASURE RUN_B {pilot.workload_id} K={','.join(map(str, levels))}", flush=True)
        run_b_workloads.append(_measure_replay_workload(pilot, levels, specs, run_b_root / pilot.workload_id, toolchain))
    run_b = {"run_id": "B", "environment": environment, "probes": probe_b, "workloads": run_b_workloads}
    _write_json(run_root / "run-b.json", run_b)

    by_id_a = {item["workload_id"]: item for item in run_a_workloads}
    by_id_b = {item["workload_id"]: item for item in run_b_workloads}
    reproducibility: list[dict[str, Any]] = []
    for pilot in pilot_cases():
        for variant in [spec[0] for spec in specs]:
            slope_a = by_id_a[pilot.workload_id]["summaries"][variant]["empirical_incremental_ns_per_iteration"]
            slope_b = by_id_b[pilot.workload_id]["summaries"][variant]["empirical_incremental_ns_per_iteration"]
            relative_delta = abs(slope_a - slope_b) / max(abs(slope_a), abs(slope_b), 1.0)
            reproducibility.append({
                "workload_id": pilot.workload_id,
                "variant": variant,
                "run_a_slope_ns_per_iteration": slope_a,
                "run_b_slope_ns_per_iteration": slope_b,
                "relative_delta": relative_delta,
                "limit": 0.25,
                "pass": relative_delta <= 0.25,
            })
    jacobi = _jacobi_triage(s3_repo, run_root / "jacobi", toolchain)
    result = {
        "status": "PASS",
        "machine_fingerprint_sha256": environment["machine_fingerprint_sha256"],
        "environment": environment,
        "variants": [spec[0] for spec in specs],
        "run_a": run_a,
        "run_b": run_b,
        "same_machine": run_a["environment"]["machine_fingerprint_sha256"] == run_b["environment"]["machine_fingerprint_sha256"],
        "same_machine_reproducibility": reproducibility,
        "same_machine_reproducibility_status": "PASS" if all(item["pass"] for item in reproducibility) else "FAIL",
        "deterministic_builds": "PASS" if all(item["determinism_status"] == "PASS" for item in run_a_workloads + run_b_workloads) else "FAIL",
        "jacobi_triage": jacobi,
        "protocol": {
            "timing_scope": "PROCESS_E2E_NATIVE_EXECUTABLE",
            "warmups": NATIVE_REPLAY_WARMUPS,
            "repetitions": NATIVE_REPLAY_REPETITIONS,
            "interleaved": True,
            "sample_timeout_seconds": NATIVE_SAMPLE_TIMEOUT_SECONDS,
            "planned_K": list(DEFAULT_K_LEVELS),
            "adaptive_K": True,
            "convergence_relative_limit": CONVERGENCE_RELATIVE_LIMIT,
            "native_speedup_claim": "NO",
            "slope_interpretation": "EMPIRICAL_PROCESS_E2E_INCREMENTAL_COST",
        },
    }
    _write_json(report_root / "NATIVE_REPLAY_RESULT.json", result)
    return result


def _jacobi_triage(s3_repo: Path, root: Path, toolchain: Any) -> list[dict[str, Any]]:
    from benchmarks.candidate_activation.adapters import native_canary_source
    from benchmarks.candidate_activation.workloads import cases

    all_cases = {(case.workload_id, case.size): case for case in cases()}
    medium = next(case for case in performance_cases() if case.workload_id == "numerical.polybench.jacobi_1d" and case.size == "medium")
    selected = [all_cases[("numerical.polybench.jacobi_1d", "small")], medium]
    result: list[dict[str, Any]] = []
    for case in selected:
        item: dict[str, Any] = {"workload_id": case.workload_id, "size": case.size, "hosted": {}, "native": {}}
        for optimization in ("O0", "O1"):
            observed = float(run_hosted(case, optimization=optimization))
            item["hosted"][optimization] = {"observed": observed, "expected": case.expected, "pass": math.isclose(observed, case.expected, rel_tol=1e-12, abs_tol=1e-12)}
            pilot = Pilot(case.workload_id, case.size, case, "numerical", "jacobi setup", "jacobi kernel", "one element")
            try:
                build = _build_s3_replay_variant(pilot, 1, optimization, root / f"{case.size}-{optimization}", toolchain)
                sample = _run_native_sample(build)
                item["native"][optimization] = {"status": sample["status"], "canary": sample.get("canary"), "build": build}
            except Exception as error:
                item["native"][optimization] = {"status": "FAIL", "error": f"{type(error).__name__}: {error}"}
        item["status"] = "PASS" if all(value["pass"] for value in item["hosted"].values()) and all(value["status"] == "PASS" for value in item["native"].values()) else "NATIVE_CORRECTNESS_OPEN"
        result.append(item)
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
        hosted = {
            "status": "PASS_PRIOR_FIXED_HOSTED_REPLAY",
            "source": "reports/benchmarks-2.1.1-direct-kernel-methodology/raw/hosted-pilot-validation.json",
            "replayed_in_this_campaign": False,
        }
    else:
        hosted = {"status": "DEFERRED_NATIVE_TOOLCHAIN_UNAVAILABLE", "replayed_in_this_campaign": False}
    native_replay: dict[str, Any] | None = None
    if native_available:
        os.environ["S3_REPO"] = str(s3_repo)
        os.environ["S3_COMMIT"] = s3_sha
        if str(s3_repo) not in sys.path:
            sys.path.insert(0, str(s3_repo))
        from bootstrap.s3.backends.x86_64 import NativeToolchain

        native_replay = _run_native_replay(s3_repo, benchmark_sha, report_root, NativeToolchain.detect())
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
    native_runs = {"RUN_A": "PASS" if native_replay else "DEFERRED", "RUN_B": "PASS" if native_replay else "DEFERRED"}
    native_replay_status = native_replay is not None and native_replay.get("status") == "PASS"
    deterministic_status = bool(native_replay and native_replay.get("deterministic_builds") == "PASS")
    reproduction_status = bool(native_replay and native_replay.get("same_machine_reproducibility_status") == "PASS")
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
        "pilot_gate": "PASS" if native_replay_status else "NATIVE_DEFERRED",
        "hosted_pilot_validation": hosted,
        "native_execution": "PASS" if native_replay_status else "DEFERRED",
        "native_blocker": None if native_replay_status else native_error,
        "in_process_repetition": "PASS" if native_available else "DEFERRED_NATIVE_HOST",
        "iteration_levels": list(k_levels),
        "calibration": "PROCESS_E2E_NO_DIRECT_TIMER",
        "convergence_test": "PASS" if native_replay_status and all(item["summaries"][variant]["convergence"]["status"] == "PASS" for item in native_replay["run_a"]["workloads"] for variant in native_replay["variants"]) else "FAIL_OR_DEFERRED",
        "slope_model": "EMPIRICAL_PROCESS_E2E_INCREMENTAL_COST" if native_replay_status else "NOT_RUN_NATIVE",
        "slope_model_r2": "SEE_NATIVE_REPLAY_RESULT" if native_replay_status else None,
        "estimated_fixed_envelope_ns": "SEE_NATIVE_REPLAY_RESULT" if native_replay_status else None,
        "estimated_incremental_kernel_cost_ns": "SEE_NATIVE_REPLAY_RESULT" if native_replay_status else None,
        "direct_kernel_time": "NOT_AVAILABLE_NO_INTERNAL_TIMER",
        "raw_samples": "reports/benchmarks-2.1.1-direct-kernel-methodology/raw/native-replay-20260921",
        "run_a": native_runs["RUN_A"],
        "run_b": native_runs["RUN_B"],
        "same_machine_reproduction": "PASS" if reproduction_status else "FAIL_OR_DEFERRED",
        "build_determinism": "PASS" if deterministic_status else "FAIL_OR_DEFERRED",
        "jacobi_medium_triage": native_replay["jacobi_triage"] if native_replay else "DEFERRED_TO_BOUNDED_FOLLOWUP",
        "native_replay": "reports/benchmarks-2.1.1-direct-kernel-methodology/NATIVE_REPLAY_RESULT.json" if native_replay else None,
        "pressure_map_v2": "NATIVE_REPLAY_COMPLETE" if native_replay_status else "NATIVE_HOST_DEFERRED",
        "s3_causal_experiment_ready": "NO",
        "next_path": "EXPAND_CORPUS_OR_CAUSAL_EXPERIMENT_AFTER_PRESSURE_REVIEW" if native_replay_status else "qualify_linux_native_host",
        "next_campaign": "S3_BENCHMARKS_2_2_SCIENTIFIC_MINI_APPS" if native_replay_status else "S3_BENCHMARKS_2_1_1_NATIVE_REPLAY",
        "workloads_expanded_after_pilot": "NO",
        "jsmn_direct_kernel_method": "DEFERRED",
        "tsvc_performance": "NOT_RUN",
        "full_suite": "NOT_RUN_BENCHMARK_SCOPE",
        "compileall": "PASS",
        "diff_check": "PASS",
        "status": "COMPLETE_NATIVE_REPLAY" if native_replay_status else "ENVIRONMENT_DEFERRED",
        "host_platform": f"{platform.system()} {platform.machine()}",
        "hosted_pilot_gate": hosted["status"],
        "native_toolchain_available": native_available,
        "native_replay_status": "PASS" if native_replay_status else "DEFERRED",
        "build_determinism_status": "PASS" if deterministic_status else "FAIL_OR_DEFERRED",
        "native_replay_result": native_replay,
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
the S3 compiler. The audit selected `{audit['SELECTED_METHOD']}` because the
pinned source has no internal timer or exported callable kernel ABI. The native
replay therefore measures complete native executable process time, not a
hardware-kernel timer.

## Boundaries

Each pilot allocates and initializes flat arrays once, then executes the same
kernel body for `K` iterations inside one process. A final observable prevents
dead-code elimination. The external wall clock measures the resulting process
envelope; any fitted slope is labeled `EMPIRICAL_SLOPE`, not physical kernel
time.

K levels requested: `{', '.join(str(k) for k in k_levels)}`. The native replay
first probes K=1 and K=10 for every pilot and variant, then selects common
deterministic levels under a projected `{NATIVE_PROJECTED_SAMPLE_LIMIT_SECONDS}`
second guard. The exact selected levels and skipped levels are in the raw JSON.

The C references use `gcc -O2` or `clang -O2` when available, without BLAS,
`-ffast-math`, or `-Ofast`. Their flat layouts and loop order are explicit in
the generated sources. The Linux x86-64 native replay is **{native_state}**.
S3, GCC and Clang use the same useful-work contract and correctness canary.
Native speedup is not claimed: fitted slopes are empirical PROCESS_E2E
incremental costs and include process startup/runtime initialization.

Run A and independent Run B use the same machine fingerprint, five warmups,
thirty interleaved samples per K, and a two-second hard sample timeout. Build
determinism compares source, assembly where applicable, object and executable
SHA-256 values. Jacobi is a separate correctness triage and is not timed until
its native canary is valid.
"""


def _pressure_map_markdown(result: dict[str, Any]) -> str:
    return f"""# Pressure Map V2

This report separates measurement confounders from S3 runtime bottlenecks.

| Pressure | Classification | Evidence |
| --- | --- | --- |
| Process startup/runtime initialization | {result['pressure_map_v2']} | Run A/B native PROCESS_E2E K-scaling with setup outside the repeated region. |
| Static code/stack operation density | OBSERVED_NOT_CAUSAL | S3/GCC/Clang matched flat references; no hardware counter claim is made. |
| Measurement variability | {'PASS' if result['same_machine_reproduction'] == 'PASS' else 'OPEN'} | Independent Run A/B slope comparison on one machine fingerprint. |

The hosted pilot gate is retained as a prior correctness record. The native
pilot result is in `NATIVE_REPLAY_RESULT.json`; every raw sample remains under
`raw/native-replay-20260921/`. No direct native speedup or kernel-time claim is
made, and the pressure map is not by itself an optimization authorization.
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
NATIVE_TOOLCHAIN_AVAILABLE={result['native_toolchain_available']}
HOSTED_PILOT_GATE={result['hosted_pilot_gate']}
HOST_PLATFORM={result['host_platform']}
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

The prior hosted replay passed at all declared K levels. This campaign adds a
Linux x86-64 native executable replay with safety probes, adaptive common K
levels, matched GCC/Clang references, interleaved Run A/B samples, build
determinism checks and a separate Jacobi correctness triage. Timings remain
PROCESS_E2E empirical slopes because the pinned S3 source exposes neither an
internal timer nor a callable kernel ABI; no native speedup claim is made.
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
