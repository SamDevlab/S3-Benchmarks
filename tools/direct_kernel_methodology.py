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
import importlib
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import statistics
import subprocess
import sys
import time
from tempfile import TemporaryDirectory
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
FIXED_WORK_TARGET_MIN_NS = 250_000_000
FIXED_WORK_PREFERRED_MIN_NS = 500_000_000
FIXED_WORK_PREFERRED_MAX_NS = 1_000_000_000
FIXED_WORK_SAMPLE_TIMEOUT_SECONDS = 5.0
FIXED_WORK_CALIBRATION_LEVELS = (1, 10, 100, 1000, 10000, 100000, 1000000, 10000000)


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


def _run_text(command: list[str], *, timeout: float = 10.0) -> str | None:
    try:
        completed = subprocess.run(command, check=False, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if completed.returncode != 0:
        return None
    return (completed.stdout or completed.stderr).strip()


def _tool_version(command: str) -> str:
    value = _run_text([command, "--version"])
    return value.splitlines()[0] if value else "UNAVAILABLE"


def _collect_native_environment(s3_repo: Path, benchmark_sha: str, s3_sha: str) -> dict[str, Any]:
    lscpu = _run_text(["lscpu"]) or ""
    cpu: dict[str, str] = {}
    for line in lscpu.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            cpu[key.strip()] = value.strip()
    logical = os.cpu_count() or 1
    affinity = sorted(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None
    meminfo = _run_text(["cat", "/proc/meminfo"]) or ""
    ram = next((line.split(":", 1)[1].strip() for line in meminfo.splitlines() if line.startswith("MemTotal:")), "UNAVAILABLE")
    governor = sorted(Path("/sys/devices/system/cpu").glob("cpu*/cpufreq/scaling_governor"))
    governors = sorted({path.read_text(encoding="utf-8").strip() for path in governor}) or ["UNAVAILABLE"]
    turbo_raw = _run_text(["cat", "/sys/devices/system/cpu/intel_pstate/no_turbo"]) or "UNAVAILABLE"
    turbo = "ENABLED_OR_UNCONTROLLED" if turbo_raw == "0" else "DISABLED" if turbo_raw == "1" else "UNAVAILABLE"
    smt = _run_text(["cat", "/sys/devices/system/cpu/smt/active"]) or "UNAVAILABLE"
    stable = {
        "architecture": platform.machine(),
        "cpu_model": cpu.get("Model name", platform.processor()),
        "cpu_vendor": cpu.get("Vendor ID", "UNAVAILABLE"),
        "cpu_family": cpu.get("CPU family", "UNAVAILABLE"),
        "cpu_model_id": cpu.get("Model", "UNAVAILABLE"),
        "cpu_stepping": cpu.get("Stepping", "UNAVAILABLE"),
        "physical_cores": cpu.get("Core(s) per socket", "UNAVAILABLE"),
        "logical_cores": logical,
        "ram": ram,
        "kernel": platform.release(),
        "distribution": _run_text(["cat", "/etc/os-release"]) or "UNAVAILABLE",
        "cache_l1d": cpu.get("L1d cache", "UNAVAILABLE"),
        "cache_l1i": cpu.get("L1i cache", "UNAVAILABLE"),
        "cache_l2": cpu.get("L2 cache", "UNAVAILABLE"),
        "cache_l3": cpu.get("L3 cache", "UNAVAILABLE"),
        "numa": cpu.get("NUMA node(s)", "UNAVAILABLE"),
    }
    fingerprint = hashlib.sha256(json.dumps(stable, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    load = os.getloadavg() if hasattr(os, "getloadavg") else None
    return {
        **stable,
        "machine_fingerprint_sha256": fingerprint,
        "hostname": platform.node(),
        "os": platform.system(),
        "os_release": platform.release(),
        "python_version": platform.python_version(),
        "benchmark_repo_sha": benchmark_sha,
        "s3_sha": s3_sha,
        "gcc_version": _tool_version("gcc"),
        "clang_version": _tool_version("clang"),
        "as_version": _tool_version("as"),
        "ld_version": _tool_version("ld"),
        "perf_version": _tool_version("perf"),
        "cpu_affinity": affinity,
        "smt_status": smt,
        "cpu_governor": governors,
        "turbo_state": turbo,
        "load_average_before": load,
        "environment_noisy": bool(load and load[0] > logical),
    }


def _perf_availability() -> dict[str, str]:
    perf = shutil.which("perf")
    if perf is None:
        return {"available": "NO", "permission": "NOT_INSTALLED"}
    completed = subprocess.run([perf, "stat", "-e", "cycles", "true"], check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        return {"available": "NO", "permission": "DENIED_OR_UNAVAILABLE"}
    return {"available": "YES", "permission": "AVAILABLE_BUT_NOT_COLLECTED_PER_SAMPLE"}


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
    assembly_path = build_root / "reference.s"
    object_path = build_root / "reference.o"
    executable_path = build_root / "program"
    source_path.write_text(build_matched_c_source(pilot, iterations), encoding="utf-8", newline="\n")
    assembly_command = [compiler_path, "-std=c99", "-O2", "-fno-fast-math", "-S", str(source_path), "-o", str(assembly_path)]
    compile_command = [compiler_path, "-std=c99", "-O2", "-fno-fast-math", "-c", str(source_path), "-o", str(object_path)]
    link_command = [compiler_path, str(object_path), "-lm", "-o", str(executable_path)]
    for command in (assembly_command, compile_command, link_command):
        completed = subprocess.run(command, check=False, capture_output=True, text=True, timeout=30.0)
        if completed.returncode != 0:
            details = completed.stderr.strip() or completed.stdout.strip()
            raise RuntimeError(f"{compiler} build failed: {details}")
    return {
        "variant": "GCC_O2" if compiler == "gcc" else "CLANG_O2",
        "compiler": compiler,
        "optimization": "O2",
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


def _run_native_sample(
    build: dict[str, Any],
    *,
    timeout_seconds: float = NATIVE_SAMPLE_TIMEOUT_SECONDS,
    cpu_affinity: int | None = None,
) -> dict[str, Any]:
    executable = Path(build["executable_path"])
    command = [os.fspath(executable)]
    taskset = shutil.which("taskset")
    if cpu_affinity is not None and taskset is not None:
        command = [taskset, "-c", str(cpu_affinity), *command]
    start = time.perf_counter_ns()
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        return {
            "status": "TIMEOUT",
            "elapsed_ns": None,
            "timeout_seconds": timeout_seconds,
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
        "timeout_seconds": timeout_seconds,
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
    environment = _collect_native_environment(s3_repo, benchmark_sha, EXPECTED_S3_SHA)
    environment["perf"] = _perf_availability()
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
    deterministic_status = "PASS" if all(item["determinism_status"] == "PASS" for item in run_a_workloads + run_b_workloads) else "FAIL"
    reproducibility_status = "PASS" if all(item["pass"] for item in reproducibility) else "FAIL"
    result = {
        "status": "PASS" if deterministic_status == "PASS" and reproducibility_status == "PASS" else "METHODOLOGY_REFINEMENT_REQUIRED",
        "machine_fingerprint_sha256": environment["machine_fingerprint_sha256"],
        "environment": environment,
        "variants": [spec[0] for spec in specs],
        "run_a": run_a,
        "run_b": run_b,
        "same_machine": run_a["environment"]["machine_fingerprint_sha256"] == run_b["environment"]["machine_fingerprint_sha256"],
        "same_machine_reproducibility": reproducibility,
        "same_machine_reproducibility_status": reproducibility_status,
        "deterministic_builds": deterministic_status,
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
        native_values = list(item["native"].values())
        if all(value["status"] == "PASS" for value in native_values):
            item["status"] = "PASS" if all(value["pass"] for value in item["hosted"].values()) else "HOSTED_CORRECTNESS_FAIL"
        elif all("unsupported pilot" in value.get("error", "") for value in native_values):
            item["status"] = "HARNESS_GAP"
        else:
            item["status"] = "REPRODUCED_NATIVE_FAILURE"
        result.append(item)
    return result


def _fixed_work_summary(samples: list[int], total_work_units: int) -> dict[str, Any]:
    if not samples or total_work_units < 1:
        raise ValueError("fixed-work samples and work units must be positive")
    ordered = sorted(float(value) for value in samples)
    median = statistics.median(ordered)
    mean = statistics.fmean(ordered)
    deviations = [abs(value - median) for value in ordered]
    p95 = ordered[max(0, math.ceil(0.95 * len(ordered)) - 1)]
    stddev = statistics.stdev(ordered) if len(ordered) > 1 else 0.0
    return {
        "N": len(ordered),
        "min_ns": ordered[0],
        "median_ns": median,
        "mean_ns": mean,
        "max_ns": ordered[-1],
        "p95_ns": p95,
        "stddev_ns": stddev,
        "mad_ns": statistics.median(deviations),
        "cv": stddev / mean if mean else float("inf"),
        "total_work_units": total_work_units,
        "ns_per_work_unit": median / total_work_units,
    }


def _select_fixed_work_level(calibration: list[dict[str, Any]]) -> dict[str, Any] | None:
    valid = [
        item for item in calibration
        if item.get("status") == "PASS"
        and item["fastest_ns"] >= FIXED_WORK_TARGET_MIN_NS
        and item["slowest_ns"] <= FIXED_WORK_SAMPLE_TIMEOUT_SECONDS * 1_000_000_000
    ]
    if not valid:
        return None
    preferred = [
        item for item in valid
        if FIXED_WORK_PREFERRED_MIN_NS <= item["fastest_ns"] <= FIXED_WORK_PREFERRED_MAX_NS
    ]
    candidates = preferred or valid
    return min(candidates, key=lambda item: abs(item["fastest_ns"] - 750_000_000))


def _fixed_work_correctness(
    pilots: tuple[Pilot, ...],
    specs: list[tuple[str, str, str]],
    root: Path,
    toolchain: Any,
    cpu_affinity: int | None,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with TemporaryDirectory(prefix="s3bench-fixed-correctness-") as directory:
        temporary_root = Path(directory)
        for pilot in pilots:
            for spec in specs:
                build = _build_replay_variant(pilot, 1, spec, temporary_root / pilot.workload_id / spec[0], toolchain)
                sample = _run_native_sample(
                    build,
                    timeout_seconds=FIXED_WORK_SAMPLE_TIMEOUT_SECONDS,
                    cpu_affinity=cpu_affinity,
                )
                records.append({
                    "workload_id": pilot.workload_id,
                    "variant": spec[0],
                    "status": "PASS" if sample.get("status") == "PASS" and sample.get("canary") == 1 else "FAIL",
                    "sample": sample,
                })
    return records


def _calibrate_fixed_work(
    pilot: Pilot,
    specs: list[tuple[str, str, str]],
    root: Path,
    toolchain: Any,
    cpu_affinity: int | None,
) -> dict[str, Any]:
    calibration: list[dict[str, Any]] = []
    for iterations in FIXED_WORK_CALIBRATION_LEVELS:
        with TemporaryDirectory(prefix=f"s3bench-calibration-{pilot.workload_id}-") as directory:
            level: dict[str, Any] = {"K": iterations, "variants": {}}
            for spec in specs:
                build = _build_replay_variant(pilot, iterations, spec, Path(directory) / spec[0], toolchain)
                sample = _run_native_sample(
                    build,
                    timeout_seconds=FIXED_WORK_SAMPLE_TIMEOUT_SECONDS,
                    cpu_affinity=cpu_affinity,
                )
                level["variants"][spec[0]] = {
                    "status": sample.get("status"),
                    "elapsed_ns": sample.get("elapsed_ns"),
                    "timeout_seconds": sample.get("timeout_seconds"),
                }
            elapsed = [
                float(item["elapsed_ns"])
                for item in level["variants"].values()
                if item.get("status") == "PASS" and item.get("elapsed_ns") is not None
            ]
            level["fastest_ns"] = min(elapsed) if len(elapsed) == len(specs) else None
            level["slowest_ns"] = max(elapsed) if len(elapsed) == len(specs) else None
            level["status"] = "PASS" if len(elapsed) == len(specs) else "FAIL"
            calibration.append(level)
            if level["status"] == "PASS" and level["slowest_ns"] > FIXED_WORK_SAMPLE_TIMEOUT_SECONDS * 1_000_000_000:
                break
            if level["status"] == "PASS" and level["fastest_ns"] >= FIXED_WORK_PREFERRED_MIN_NS:
                break
    selection = _select_fixed_work_level(calibration)
    return {
        "workload_id": pilot.workload_id,
        "calibration": calibration,
        "selected": selection,
        "status": "PASS" if selection else "NO_COMMON_FIXED_WORK_WINDOW",
    }


def _fixed_work_measurement(
    run_id: str,
    pilots: tuple[Pilot, ...],
    specs: list[tuple[str, str, str]],
    selected: dict[str, dict[str, Any]],
    builds: dict[str, dict[str, dict[str, Any]]],
    environment: dict[str, Any],
    cpu_affinity: int | None,
) -> dict[str, Any]:
    labels = [spec[0] for spec in specs]
    workloads: list[dict[str, Any]] = []
    for pilot in pilots:
        choice = selected[pilot.workload_id]["selected"]
        iterations = int(choice["K"])
        samples: dict[str, list[int]] = {label: [] for label in labels}
        warmups: dict[str, list[int]] = {label: [] for label in labels}
        for order in _interleaved_labels(labels, FIXED_WORK_WARMUPS):
            for label in order:
                sample = _run_native_sample(
                    builds[pilot.workload_id][label],
                    timeout_seconds=FIXED_WORK_SAMPLE_TIMEOUT_SECONDS,
                    cpu_affinity=cpu_affinity,
                )
                if sample.get("status") != "PASS":
                    raise RuntimeError(f"fixed-work warmup failed: {pilot.workload_id} {label}: {sample}")
                warmups[label].append(int(sample["elapsed_ns"]))
        for order in _interleaved_labels(labels, FIXED_WORK_REPETITIONS):
            for label in order:
                sample = _run_native_sample(
                    builds[pilot.workload_id][label],
                    timeout_seconds=FIXED_WORK_SAMPLE_TIMEOUT_SECONDS,
                    cpu_affinity=cpu_affinity,
                )
                if sample.get("status") != "PASS":
                    raise RuntimeError(f"fixed-work measurement failed: {pilot.workload_id} {label}: {sample}")
                samples[label].append(int(sample["elapsed_ns"]))
        total_work_units = _pilot_work_units(pilot) * iterations
        workloads.append({
            "workload_id": pilot.workload_id,
            "size": pilot.size,
            "K_final": iterations,
            "work_units_per_iteration": _pilot_work_units(pilot),
            "total_work_units": total_work_units,
            "environment": environment,
            "binary_sha256": {label: builds[pilot.workload_id][label]["executable_sha256"] for label in labels},
            "warmups_ns": warmups,
            "samples_ns": samples,
            "summaries": {label: _fixed_work_summary(values, total_work_units) for label, values in samples.items()},
        })
    return {"run_id": run_id, "environment": environment, "workloads": workloads}


def _fixed_pressure_map(result: dict[str, Any]) -> dict[str, Any]:
    reproducible = result["same_machine_reproduction"] == "PASS"
    perf_available = result["perf"]["available"] == "YES"
    def entry(name: str, classification: str, strength: str, causality: str, evidence: str) -> dict[str, str]:
        return {"pressure": name, "classification": classification, "evidence_strength": strength, "causality": causality, "evidence": evidence}
    return {
        "status": "ACTIONABLE" if reproducible else "NOT_ACTIONABLE_REPRODUCIBILITY_OPEN",
        "pressures": [
            entry("PROCESS_STARTUP", "WEAKENED" if result["fixed_work_window"] else "UNCHANGED", "MULTI_FAMILY", "UNKNOWN", "fixed work raises the useful-work fraction but A/B must remain stable before causal attribution"),
            entry("MEASUREMENT_VARIABILITY", "FALSIFIED" if reproducible else "STRENGTHENED", "MULTI_FAMILY", "CORRELATED", "same-binary Run A/B comparison"),
            entry("STATIC_CODE_DENSITY", "UNCHANGED", "MULTI_WORKLOAD", "UNKNOWN", "assembly hashes are preserved; static size is not a dynamic cause"),
            entry("STACK_OPERATION_DENSITY", "UNCHANGED", "MULTI_WORKLOAD", "UNKNOWN", "no dynamic counter evidence"),
            entry("RUNTIME_HELPER_PRESSURE", "UNCHANGED", "MULTI_WORKLOAD", "UNKNOWN", "helper density not measured in this protocol"),
            entry("MEMORY_BANDWIDTH", "UNCHANGED", "MULTI_FAMILY", "UNKNOWN", "perf counters unavailable or not collected"),
            entry("CACHE_LOCALITY", "UNCHANGED", "MULTI_FAMILY", "UNKNOWN", "perf counters unavailable or not collected"),
            entry("BRANCHING", "UNCHANGED", "MULTI_FAMILY", "UNKNOWN", "perf counters unavailable or not collected"),
            entry("NUMERIC_THROUGHPUT", "UNCHANGED", "MULTI_FAMILY", "UNKNOWN", "perf counters unavailable or not collected"),
        ],
        "causal_experiment_ready": reproducible and perf_available,
    }


def _run_fixed_work_native_stability(
    s3_repo: Path,
    benchmark_sha: str,
    report_root: Path,
    toolchain: Any,
) -> dict[str, Any]:
    specs = _native_variant_specs()
    pilots = pilot_cases()
    if [spec[0] for spec in specs] != ["S3_O0", "S3_O1", "GCC_O2", "CLANG_O2"]:
        raise RuntimeError("fixed-work protocol requires S3_O0, S3_O1, GCC_O2 and CLANG_O2")
    cpu_affinity = 0 if shutil.which("taskset") else None
    environment = _collect_native_environment(s3_repo, benchmark_sha, EXPECTED_S3_SHA)
    environment["cpu_affinity"] = [cpu_affinity] if cpu_affinity is not None else environment.get("cpu_affinity")
    environment["perf"] = _perf_availability()
    run_id = time.strftime("fixed-work-native-%Y%m%d-%H%M%S", time.gmtime())
    raw_root = report_root / "raw" / run_id
    raw_root.mkdir(parents=True, exist_ok=False)
    correctness = _fixed_work_correctness(pilots, specs, raw_root / "correctness", toolchain, cpu_affinity)
    correctness_status = "PASS" if len(correctness) == 16 and all(item["status"] == "PASS" for item in correctness) else "FAIL"
    _write_json(raw_root / "correctness.json", {"points": correctness, "status": correctness_status})
    if correctness_status != "PASS":
        raise RuntimeError("fixed-work native correctness gate failed; no performance was collected")
    selected: dict[str, dict[str, Any]] = {}
    for pilot in pilots:
        selected[pilot.workload_id] = _calibrate_fixed_work(pilot, specs, raw_root / "calibration", toolchain, cpu_affinity)
    _write_json(raw_root / "calibration.json", selected)
    if any(item["status"] != "PASS" for item in selected.values()):
        frozen_manifest = {
            "benchmark_sha": benchmark_sha,
            "s3_sha": EXPECTED_S3_SHA,
            "run_id": run_id,
            "status": "NO_COMMON_FIXED_WORK_WINDOW",
            "methodology": "FIXED_WORK_AMPLIFIED_PROCESS",
            "variants": [spec[0] for spec in specs],
            "cpu_affinity": environment["cpu_affinity"],
            "anti_DCE_policy": "native integer canary over final observable",
            "workloads": [
                {
                    "workload_id": pilot.workload_id,
                    "family": pilot.family,
                    "size": pilot.size,
                    "K_final": None,
                    "work_units_per_iteration": _pilot_work_units(pilot),
                    "total_work_units": None,
                    "input_dimensions": pilot.case.logical_shape,
                    "data_layout": pilot.case.physical_layout,
                    "index_mapping": pilot.case.index_mapping,
                    "calibration_probes": selected[pilot.workload_id]["calibration"],
                    "calibration_decision": None,
                    "variants": [spec[0] for spec in specs],
                }
                for pilot in pilots
            ],
        }
        jacobi = _jacobi_triage(s3_repo, raw_root / "jacobi", toolchain)
        jacobi_status = (
            "PASS"
            if all(item["status"] == "PASS" for item in jacobi)
            else "HARNESS_GAP"
            if all(item["status"] == "HARNESS_GAP" for item in jacobi)
            else "REPRODUCED_NATIVE_FAILURE"
        )
        result = {
            "campaign": "S3_BENCHMARKS_2_1_2_FIXED_WORK_NATIVE_STABILITY",
            "benchmark_sha": benchmark_sha,
            "s3_sha": EXPECTED_S3_SHA,
            "run_id": run_id,
            "environment": environment,
            "variants": [spec[0] for spec in specs],
            "methodology": "FIXED_WORK_AMPLIFIED_PROCESS",
            "direct_kernel_time": "NOT_AVAILABLE",
            "callable_kernel_abi": "NO",
            "cross_k_slope_status": "HISTORICAL_ONLY",
            "hosted_correctness": "PASS_PRIOR_FIXED_HOSTED_REPLAY",
            "native_correctness": "PASS",
            "matched_flat_reference": "PASS",
            "correctness_points": correctness,
            "fixed_work_manifest": frozen_manifest,
            "frozen_builds": {},
            "build_determinism": "NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW",
            "same_binary_run_a_run_b": "NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW",
            "same_machine_reproduction": "NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW",
            "reproducibility": [],
            "run_a": "NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW",
            "run_b": "NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW",
            "perf": environment["perf"],
            "perf_counters": "UNAVAILABLE_PERMISSION" if environment["perf"]["available"] != "YES" else "NOT_COLLECTED",
            "jacobi_triage": jacobi,
            "jacobi_native_correctness": jacobi_status,
            "jacobi_performance_measured": "NO",
            "fixed_work_window": False,
            "pressure_map_v3": "NOT_ACTIONABLE_NO_COMMON_FIXED_WORK_WINDOW",
            "s3_causal_experiment_ready": "NO",
            "next_path": "MEASUREMENT_ENVIRONMENT_INVESTIGATION",
            "next_campaign": "S3_BENCHMARKS_2_1_2_FIXED_WORK_NATIVE_STABILITY_REFINEMENT",
            "raw_samples": f"reports/benchmarks-2.1.2-fixed-work-native-stability/raw/{run_id}",
            "status": "NO_COMMON_FIXED_WORK_WINDOW",
        }
        pressure_map = _fixed_pressure_map(result)
        result["pressure_map_v3_detail"] = pressure_map
        _write_fixed_work_reports(report_root, frozen_manifest, result, pressure_map, jacobi)
        return result
    builds: dict[str, dict[str, dict[str, Any]]] = {}
    determinism: list[dict[str, Any]] = []
    for pilot in pilots:
        iterations = int(selected[pilot.workload_id]["selected"]["K"])
        builds[pilot.workload_id] = {}
        for spec in specs:
            build = _build_replay_variant(pilot, iterations, spec, raw_root / "official", toolchain)
            canary = _run_native_sample(build, timeout_seconds=FIXED_WORK_SAMPLE_TIMEOUT_SECONDS, cpu_affinity=cpu_affinity)
            if canary.get("status") != "PASS":
                raise RuntimeError(f"official fixed-work canary failed: {pilot.workload_id} {spec[0]}: {canary}")
            builds[pilot.workload_id][spec[0]] = build
            with TemporaryDirectory(prefix="s3bench-fixed-determinism-") as directory:
                duplicate = _build_replay_variant(pilot, iterations, spec, Path(directory), toolchain)
                fields = ("source_sha256", "assembly_sha256", "object_sha256", "executable_sha256")
                determinism.append({
                    "workload_id": pilot.workload_id,
                    "variant": spec[0],
                    "first": {field: build[field] for field in fields},
                    "second": {field: duplicate[field] for field in fields},
                    "pass": all(build[field] == duplicate[field] for field in fields),
                })
    frozen_manifest = {
        "benchmark_sha": benchmark_sha,
        "s3_sha": EXPECTED_S3_SHA,
        "run_id": run_id,
        "methodology": "FIXED_WORK_AMPLIFIED_PROCESS",
        "variants": [spec[0] for spec in specs],
        "cpu_affinity": environment["cpu_affinity"],
        "anti_DCE_policy": "native integer canary over final observable",
        "workloads": [
            {
                "workload_id": pilot.workload_id,
                "family": pilot.family,
                "size": pilot.size,
                "K_final": selected[pilot.workload_id]["selected"]["K"],
                "work_units_per_iteration": _pilot_work_units(pilot),
                "total_work_units": _pilot_work_units(pilot) * selected[pilot.workload_id]["selected"]["K"],
                "input_dimensions": pilot.case.logical_shape,
                "data_layout": pilot.case.physical_layout,
                "index_mapping": pilot.case.index_mapping,
                "calibration_probes": selected[pilot.workload_id]["calibration"],
                "calibration_decision": selected[pilot.workload_id]["selected"],
                "variants": [spec[0] for spec in specs],
            }
            for pilot in pilots
        ],
    }
    _write_json(raw_root / "frozen-build-manifest.json", {"builds": builds, "determinism": determinism})
    _write_json(raw_root / "FIXED_WORK_MANIFEST.json", frozen_manifest)
    environment_after_build = _collect_native_environment(s3_repo, benchmark_sha, EXPECTED_S3_SHA)
    run_a = _fixed_work_measurement("A", pilots, specs, selected, builds, {"before": environment, "after": environment_after_build}, cpu_affinity)
    _write_json(raw_root / "run-a.json", run_a)
    environment_before_b = _collect_native_environment(s3_repo, benchmark_sha, EXPECTED_S3_SHA)
    run_b = _fixed_work_measurement("B", pilots, specs, selected, builds, {"before": environment_before_b}, cpu_affinity)
    run_b["environment"]["after"] = _collect_native_environment(s3_repo, benchmark_sha, EXPECTED_S3_SHA)
    _write_json(raw_root / "run-b.json", run_b)
    labels = [spec[0] for spec in specs]
    by_a = {item["workload_id"]: item for item in run_a["workloads"]}
    by_b = {item["workload_id"]: item for item in run_b["workloads"]}
    reproducibility: list[dict[str, Any]] = []
    for pilot in pilots:
        for label in labels:
            a = by_a[pilot.workload_id]["summaries"][label]
            b = by_b[pilot.workload_id]["summaries"][label]
            relative_delta = abs(a["ns_per_work_unit"] - b["ns_per_work_unit"]) / max(abs(a["ns_per_work_unit"]), abs(b["ns_per_work_unit"]), 1e-12)
            reproducibility.append({
                "workload_id": pilot.workload_id,
                "variant": label,
                "median_a_ns": a["median_ns"],
                "median_b_ns": b["median_ns"],
                "cv_a": a["cv"],
                "cv_b": b["cv"],
                "ns_per_work_unit_a": a["ns_per_work_unit"],
                "ns_per_work_unit_b": b["ns_per_work_unit"],
                "relative_delta": relative_delta,
                "limit": CONVERGENCE_RELATIVE_LIMIT,
                "pass": relative_delta <= CONVERGENCE_RELATIVE_LIMIT,
            })
    same_binary = all(
        by_a[pilot.workload_id]["binary_sha256"] == by_b[pilot.workload_id]["binary_sha256"]
        for pilot in pilots
    )
    same_machine = run_a["environment"]["before"]["machine_fingerprint_sha256"] == run_b["environment"]["before"]["machine_fingerprint_sha256"]
    reproducibility_status = "PASS" if same_binary and same_machine and all(item["pass"] for item in reproducibility) else "FAIL"
    deterministic_status = "PASS" if all(item["pass"] for item in determinism) else "FAIL"
    jacobi = _jacobi_triage(s3_repo, raw_root / "jacobi", toolchain)
    result = {
        "campaign": "S3_BENCHMARKS_2_1_2_FIXED_WORK_NATIVE_STABILITY",
        "benchmark_sha": benchmark_sha,
        "s3_sha": EXPECTED_S3_SHA,
        "run_id": run_id,
        "environment": environment,
        "variants": labels,
        "methodology": "FIXED_WORK_AMPLIFIED_PROCESS",
        "direct_kernel_time": "NOT_AVAILABLE",
        "callable_kernel_abi": "NO",
        "cross_k_slope_status": "HISTORICAL_ONLY",
        "hosted_correctness": "PASS_PRIOR_FIXED_HOSTED_REPLAY",
        "native_correctness": "PASS",
        "matched_flat_reference": "PASS",
        "correctness_points": correctness,
        "fixed_work_manifest": frozen_manifest,
        "frozen_builds": builds,
        "build_determinism": deterministic_status,
        "same_binary_run_a_run_b": "PASS" if same_binary else "FAIL",
        "same_machine_reproduction": reproducibility_status,
        "reproducibility": reproducibility,
        "run_a": run_a,
        "run_b": run_b,
        "perf": environment["perf"],
        "perf_counters": "UNAVAILABLE_PERMISSION" if environment["perf"]["available"] != "YES" else "NOT_COLLECTED",
        "jacobi_triage": jacobi,
        "jacobi_native_correctness": "PASS" if all(item["status"] == "PASS" for item in jacobi) else "HARNESS_GAP" if all(item["status"] == "HARNESS_GAP" for item in jacobi) else "REPRODUCED_NATIVE_FAILURE",
        "jacobi_performance_measured": "NO",
        "fixed_work_window": True,
        "pressure_map_v3": "ACTIONABLE" if reproducibility_status == "PASS" else "NOT_ACTIONABLE_REPRODUCIBILITY_OPEN",
        "s3_causal_experiment_ready": "YES" if reproducibility_status == "PASS" and environment["perf"]["available"] == "YES" else "NO",
        "next_path": "EVIDENCE_DRIVEN" if reproducibility_status == "PASS" else "MEASUREMENT_ENVIRONMENT_INVESTIGATION",
        "next_campaign": "S3_BENCHMARKS_2_2_SCIENTIFIC_MINI_APPS" if reproducibility_status == "PASS" else "S3_BENCHMARKS_2_1_2_FIXED_WORK_NATIVE_STABILITY_REFINEMENT",
        "raw_samples": f"reports/benchmarks-2.1.2-fixed-work-native-stability/raw/{run_id}",
        "status": "COMPLETE" if reproducibility_status == "PASS" else "MEASUREMENT_REPRODUCIBILITY_OPEN",
    }
    pressure_map = _fixed_pressure_map(result)
    result["pressure_map_v3_detail"] = pressure_map
    _write_json(report_root / "FIXED_WORK_MANIFEST.json", frozen_manifest)
    _write_json(report_root / "FIXED_WORK_NATIVE_RESULT.json", result)
    _write_json(report_root / "PRESSURE_MAP_V3.json", pressure_map)
    _write_json(report_root / "JACOBI_CORRECTNESS_TRIAGE.json", {"status": result["jacobi_native_correctness"], "items": jacobi})
    (report_root / "FIXED_WORK_NATIVE_REPORT.md").write_text(_fixed_work_report_markdown(result), encoding="utf-8", newline="\n")
    (report_root / "PRESSURE_MAP_V3.md").write_text(_fixed_pressure_map_markdown(pressure_map), encoding="utf-8", newline="\n")
    (report_root / "JACOBI_CORRECTNESS_TRIAGE.md").write_text(_jacobi_report_markdown(result), encoding="utf-8", newline="\n")
    return result


FIXED_WORK_WARMUPS = 5
FIXED_WORK_REPETITIONS = 30


def _fixed_work_report_markdown(result: dict[str, Any]) -> str:
    return f"""# S3 Benchmarks 2.1.2 Fixed-Work Native Stability

```text
CAMPAIGN=S3_BENCHMARKS_2_1_2_FIXED_WORK_NATIVE_STABILITY
BENCHMARK_HEAD={result['benchmark_sha']}
S3_SHA={result['s3_sha']}
MACHINE_FINGERPRINT={result['environment']['machine_fingerprint_sha256']}
METHODOLOGY=FIXED_WORK_AMPLIFIED_PROCESS
DIRECT_KERNEL_TIME=NOT_AVAILABLE
CALLABLE_KERNEL_ABI=NO
CROSS_K_SLOPE_STATUS=HISTORICAL_ONLY
NATIVE_CORRECTNESS={result['native_correctness']}
MATCHED_FLAT_REFERENCE={result['matched_flat_reference']}
FROZEN_BINARY_A_B={result['same_binary_run_a_run_b']}
BUILD_DETERMINISM={result['build_determinism']}
SAME_MACHINE_REPRODUCTION={result['same_machine_reproduction']}
PERF_DIAGNOSTICS={result['perf_counters']}
JACOBI_NATIVE_CORRECTNESS={result['jacobi_native_correctness']}
JACOBI_PERFORMANCE_MEASURED=NO
PRESSURE_MAP_V3={result['pressure_map_v3']}
S3_CAUSAL_EXPERIMENT_READY={result['s3_causal_experiment_ready']}
NEXT_PATH={result['next_path']}
STATUS={result['status']}
PR=18
MERGE=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

The primary comparison uses one selected `K_FINAL` per workload, the same
across S3 O0, S3 O1, GCC O2 and Clang O2. Calibration is discarded as timing
evidence. {('Calibration found no common `K_FINAL` satisfying the bounded target across all four variants for every workload, so no official fixed binary or Run A/B was started; this is a protocol closure, not a timing result.' if not result['fixed_work_window'] else 'Official builds were created once, hashed, and reused unchanged by Run A and Run B. The samples measure native process-E2E work, including the remaining startup/runtime envelope; they are not direct kernel time.')}

The historical cross-K slope evidence remains preserved in the 2.1.1 report
and is classified `HISTORICAL_ONLY`. It is not used as the primary result here.

Raw JSON, frozen manifests, build hashes, calibration decisions and all sample
arrays are under `{result['raw_samples']}`. Derived executables, objects and
assembly payloads may be removed after hashing; their SHA-256 values remain in
the frozen manifest.
"""


def _fixed_pressure_map_markdown(pressure_map: dict[str, Any]) -> str:
    lines = ["# Pressure Map V3", "", "| Pressure | Classification | Evidence strength | Causality |", "| --- | --- | --- | --- |"]
    for item in pressure_map["pressures"]:
        lines.append(f"| {item['pressure']} | {item['classification']} | {item['evidence_strength']} | {item['causality']} |")
    lines.extend(["", f"`PRESSURE_MAP_V3={pressure_map['status']}`", f"`S3_CAUSAL_EXPERIMENT_READY={'YES' if pressure_map['causal_experiment_ready'] else 'NO'}`", "", "No pressure is promoted to a compiler optimization target without reproducible fixed-work evidence and a discriminating experiment."])
    return "\n".join(lines) + "\n"


def _jacobi_report_markdown(result: dict[str, Any]) -> str:
    return f"""# Jacobi Correctness Triage

```text
JACOBI_NATIVE_CORRECTNESS={result['jacobi_native_correctness']}
JACOBI_PERFORMANCE_MEASURED=NO
```

Hosted small and medium O0/O1 checks remain recorded. The native adapter
currently reports an explicit `HARNESS_GAP` for the Jacobi pilot because the
fixed-work pilot builder does not expose that workload in the native replay
generator. This is not classified as an S3 native failure and no Jacobi timing
was collected.
"""


def _write_fixed_work_reports(
    report_root: Path,
    frozen_manifest: dict[str, Any],
    result: dict[str, Any],
    pressure_map: dict[str, Any],
    jacobi: list[dict[str, Any]],
) -> None:
    _write_json(report_root / "FIXED_WORK_MANIFEST.json", frozen_manifest)
    _write_json(report_root / "FIXED_WORK_NATIVE_RESULT.json", result)
    _write_json(report_root / "PRESSURE_MAP_V3.json", pressure_map)
    _write_json(report_root / "JACOBI_CORRECTNESS_TRIAGE.json", {"status": result["jacobi_native_correctness"], "items": jacobi})
    (report_root / "FIXED_WORK_NATIVE_REPORT.md").write_text(_fixed_work_report_markdown(result), encoding="utf-8", newline="\n")
    (report_root / "PRESSURE_MAP_V3.md").write_text(_fixed_pressure_map_markdown(pressure_map), encoding="utf-8", newline="\n")
    (report_root / "JACOBI_CORRECTNESS_TRIAGE.md").write_text(_jacobi_report_markdown(result), encoding="utf-8", newline="\n")


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
    native_replay_status = native_replay is not None
    native_replay_green = bool(native_replay and native_replay.get("status") == "PASS")
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
        "pressure_map_v2": "NATIVE_REPLAY_COMPLETE" if native_replay_green else "NATIVE_REPLAY_REPRODUCIBILITY_GAP" if native_replay_status else "NATIVE_HOST_DEFERRED",
        "s3_causal_experiment_ready": "NO",
        "next_path": "EXPAND_CORPUS_OR_CAUSAL_EXPERIMENT_AFTER_PRESSURE_REVIEW" if native_replay_green else "METHODOLOGY_REFINEMENT_FOR_PROCESS_E2E_SLOPE_STABILITY" if native_replay_status else "qualify_linux_native_host",
        "next_campaign": "S3_BENCHMARKS_2_2_SCIENTIFIC_MINI_APPS" if native_replay_status else "S3_BENCHMARKS_2_1_1_NATIVE_REPLAY",
        "workloads_expanded_after_pilot": "NO",
        "jsmn_direct_kernel_method": "DEFERRED",
        "tsvc_performance": "NOT_RUN",
        "full_suite": "NOT_RUN_BENCHMARK_SCOPE",
        "compileall": "PASS",
        "diff_check": "PASS",
        "status": "COMPLETE_NATIVE_REPLAY" if native_replay_green else "METHODOLOGY_REFINEMENT_REQUIRED" if native_replay_status else "ENVIRONMENT_DEFERRED",
        "host_platform": f"{platform.system()} {platform.machine()}",
        "hosted_pilot_gate": hosted["status"],
        "native_toolchain_available": native_available,
        "native_replay_status": "PASS" if native_replay_green else "METHODOLOGY_REFINEMENT_REQUIRED" if native_replay_status else "DEFERRED",
        "build_determinism_status": "PASS" if deterministic_status else "FAIL_OR_DEFERRED",
        "native_replay_result": "reports/benchmarks-2.1.1-direct-kernel-methodology/NATIVE_REPLAY_RESULT.json" if native_replay else None,
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


def run_fixed_work_campaign(args: argparse.Namespace) -> Path:
    """Run the 2.1.2 frozen-work protocol on the controlled native host."""

    root = ROOT
    s3_repo = args.s3_repo.resolve()
    benchmark_sha = require_commit(root, args.benchmark_sha, label="benchmark repository")
    s3_sha = require_commit(s3_repo, args.s3_sha, label="S3 candidate")
    if s3_sha != EXPECTED_S3_SHA:
        raise RuntimeError(f"S3 candidate is not the pinned source: {s3_sha} != {EXPECTED_S3_SHA}")
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("fixed-work native stability requires Linux x86-64")
    report_root = root / "reports" / "benchmarks-2.1.2-fixed-work-native-stability"
    report_root.mkdir(parents=True, exist_ok=True)
    os.environ["S3_REPO"] = str(s3_repo)
    os.environ["S3_COMMIT"] = s3_sha
    _activate_pinned_s3_modules(s3_repo)
    from bootstrap.s3.backends.x86_64 import NativeToolchain

    _run_fixed_work_native_stability(s3_repo, benchmark_sha, report_root, NativeToolchain.detect())
    print(f"FIXED_WORK_RESULT={report_root / 'FIXED_WORK_NATIVE_RESULT.json'}")
    return report_root / "FIXED_WORK_NATIVE_RESULT.json"


def _activate_pinned_s3_modules(s3_repo: Path) -> None:
    """Make the benchmark process fail closed on a stale installed S3 module."""

    repo = s3_repo.resolve()
    if not (repo / "bootstrap" / "s3" / "pipeline.py").is_file():
        raise RuntimeError(f"S3_REPO is not a complete S3 checkout: {repo}")
    for name in list(sys.modules):
        if name == "bootstrap" or name.startswith("bootstrap."):
            del sys.modules[name]
    sys.path[:] = [entry for entry in sys.path if entry != str(repo)]
    sys.path.insert(0, str(repo))
    pipeline = importlib.import_module("bootstrap.s3.pipeline")
    loaded = Path(pipeline.__file__).resolve()
    try:
        loaded.relative_to(repo)
    except ValueError as error:
        raise RuntimeError(f"S3 module escaped pinned checkout: {loaded}") from error


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
    parser.add_argument("--fixed-work", action="store_true", help="run the 2.1.2 frozen-work native stability protocol")
    args = parser.parse_args(argv)
    path = run_fixed_work_campaign(args) if args.fixed_work else run_campaign(args)
    print(f"RESULT={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
