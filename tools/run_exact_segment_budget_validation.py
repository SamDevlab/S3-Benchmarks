"""Validate the experimental S3 exact-segment budget mode on fixed workloads.

This benchmark-side runner pins both S3 repositories, proves default-mode
assembly identity before timing, and records every correctness, warmup, and
timed process result under a unique immutable raw directory.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import importlib
import inspect
import json
import math
import os
from pathlib import Path
import platform
import shutil
import statistics
import subprocess
import sys
import time
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from protocol.provenance import require_commit, sha256_file  # noqa: E402
from tools.ffi_direct_kernel_methodology import (  # noqa: E402
    S3_FFI_MAX_INSTRUCTIONS,
    _activate_s3_modules,
    _build_driver,
    _compile_assembly_shared,
    _path_sha256,
    _pilot_sources,
    _resolve_export_symbol,
    _run_driver,
)
from tools.runtime_attribution import (  # noqa: E402
    audit_assembly,
    _instruction_lines,
    remove_instruction_budget_instrumentation,
)


CAMPAIGN = "S3_BENCHMARKS_EXPERIMENTAL_SEGMENT_BUDGET_VALIDATION"
BENCHMARK_BASE = "8fc0aba50ca48d3f7171bdf49395df3cd880626a"
BENCHMARK_BRANCH = "research/benchmarks-2.2.5-s3-segment-budget-validation"
S3_CONTROL_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"
S3_EXPERIMENT_SHA = "1a76e341098b54a639fec22eecea362cc243c46f"
S3_HARDENING_SHA = "6f320242e3c1ebbb0d2ac5d6d85272ab375e5333"
EXTERNAL_WARMUPS = 5
INLINE_WARMUPS = 0
REPETITIONS = 30
SESSIONS = ("run_1", "run_2")
CPU_AFFINITY = 0
MAX_RELATIVE_SESSION_MEDIAN_DELTA = 0.25
MINIMUM_USEFUL_RECOVERY = 0.25
STRONG_RECOVERY = 0.50
MAX_HARDENING_RUNTIME_REGRESSION = 0.05
MINIMUM_RETAINED_BUDGET_RECOVERY = 0.50
MINIMUM_HOT_LAYOUT_RECOVERY = 0.25
TARGET_K = {
    "scientific.rmsd.batch": 2_000_000,
    "scientific.xsbench.compatible_lookup.medium": 750_000,
    "realworld.jsmn": 1_250_000,
}
VARIANTS = (
    "P0_O0",
    "P2_O0",
    "P2H_O0",
    "PNEG_O0",
    "P0_O1",
    "P2_O1",
    "P2H_O1",
    "PNEG_O1",
)


@dataclass(frozen=True, slots=True)
class Artifact:
    workload: str
    variant: str
    optimization: str
    s3_source_sha: str
    executable: Path
    assembly: Path
    source_sha256: str
    assembly_sha256: str
    executable_sha256: str
    static_metrics: dict[str, Any]
    budget_sites: int
    run: Callable[[], dict[str, Any]]


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _write_raw_manifest(raw_root: Path) -> dict[str, Any]:
    manifest_path = raw_root / "raw-evidence-manifest.json"
    if manifest_path.exists():
        raise RuntimeError(f"refusing to replace immutable raw manifest: {manifest_path}")
    files = sorted(
        path
        for path in raw_root.rglob("*")
        if path.is_file() and path != manifest_path
    )
    entries = [
        {
            "path": path.relative_to(raw_root).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in files
    ]
    payload = {"schema": "s3.segment-budget.raw-manifest.v1", "files": entries}
    manifest_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    for entry in entries:
        path = raw_root / Path(entry["path"])
        if path.stat().st_size != entry["bytes"] or sha256_file(path) != entry["sha256"]:
            raise RuntimeError(f"raw evidence changed during manifest verification: {entry['path']}")
    return {"path": manifest_path.name, "entry_count": len(entries)}


def _run(command: list[str], *, timeout: float = 30.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def _git_output(repo: Path, *args: str) -> str:
    result = _run(["git", "-C", str(repo), *args])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git command failed: {args}")
    return result.stdout.strip()


def _require_repo_identity(repo: Path, expected_sha: str, label: str, *, clean: bool = True) -> str:
    actual = _git_output(repo, "rev-parse", "HEAD")
    if actual != expected_sha:
        raise RuntimeError(f"{label} HEAD mismatch: expected={expected_sha} actual={actual}")
    if clean and _git_output(repo, "status", "--porcelain"):
        raise RuntimeError(f"{label} worktree is not clean: {repo}")
    return actual


def _require_ancestor(repo: Path, ancestor_sha: str, descendant_sha: str, label: str) -> None:
    resolved = _git_output(repo, "rev-parse", "--verify", f"{ancestor_sha}^{{commit}}")
    if resolved != ancestor_sha:
        raise RuntimeError(f"{label} is not a full commit identity: {ancestor_sha}")
    result = subprocess.run(
        ["git", "-C", str(repo), "merge-base", "--is-ancestor", ancestor_sha, descendant_sha],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"{label} is not an ancestor of the candidate source")


def _assert_same_program_instance(p0_program: Any, p2_program: Any, workload: str) -> bool:
    if p0_program is not p2_program:
        raise RuntimeError(f"{workload} P0/P2 did not use the same AssemblyProgram instance")
    return True


def _relative_delta(first: float, second: float) -> float:
    denominator = max(abs(first), abs(second))
    return abs(first - second) / denominator if denominator else 0.0


def _balanced_order(repetition: int, session_index: int = 0) -> tuple[str, ...]:
    shift = (repetition + session_index * 3) % len(VARIANTS)
    return VARIANTS[shift:] + VARIANTS[:shift]


def _sample_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    values = [
        float(row["elapsed_ns"])
        for row in rows
        if row.get("status") == "PASS" and "elapsed_ns" in row
    ]
    if len(values) != REPETITIONS:
        return {
            "status": "INCOMPLETE",
            "valid_samples": len(values),
            "expected_samples": REPETITIONS,
        }
    ordered = sorted(values)
    median = statistics.median(values)
    mean = statistics.fmean(values)
    return {
        "status": "PASS",
        "N": len(values),
        "min_ns": min(values),
        "median_ns": median,
        "mean_ns": mean,
        "max_ns": max(values),
        "p95_ns": ordered[math.ceil(len(ordered) * 0.95) - 1],
        "stddev_ns": statistics.stdev(values),
        "mad_ns": statistics.median(abs(value - median) for value in values),
        "cv": statistics.stdev(values) / mean if mean else 0.0,
    }


def _recovery_metrics(times: dict[str, float]) -> dict[str, float | None]:
    p0 = times["P0"]
    p2 = times["P2"]
    p2h = times["P2H"]
    pneg = times["PNEG"]
    excess = p0 - pneg
    if excess == 0:
        return {
            "p2_recovered_budget_excess": None,
            "p2h_recovered_budget_excess": None,
            "p2h_vs_p2": p2h / p2 if p2 else None,
            "p2_over_pneg": None,
        }
    return {
        "p2_recovered_budget_excess": (p0 - p2) / excess,
        "p2h_recovered_budget_excess": (p0 - p2h) / excess,
        "p2h_vs_p2": p2h / p2 if p2 else None,
        "p2_over_pneg": p2 / pneg if pneg else None,
    }


def _added_text_recovery(
    p0_text: int,
    p2_text: int,
    p2h_text: int,
) -> float | None:
    p2_added = p2_text - p0_text
    if p2_added == 0:
        return None
    return (p2_added - (p2h_text - p0_text)) / p2_added


def _hardening_result(cells: list[dict[str, Any]]) -> str:
    if len(cells) != 6:
        return "INCOMPLETE"
    if not all(cell.get("correctness_pass") and cell.get("reproducibility_pass") for cell in cells):
        return "BLOCKED"
    if any(
        cell.get("p2h_vs_p2") is None
        or cell["p2h_vs_p2"] > 1.0 + MAX_HARDENING_RUNTIME_REGRESSION
        for cell in cells
    ):
        return "REJECTED_PERFORMANCE_REGRESSION"
    if any(
        cell.get("p2h_recovered_budget_excess") is None
        or cell["p2h_recovered_budget_excess"] < MINIMUM_RETAINED_BUDGET_RECOVERY
        for cell in cells
    ):
        return "CURRENT_P2_RETAINED"
    text_recovery = [cell.get("added_text_recovery") for cell in cells]
    if all(value is not None and value >= STRONG_RECOVERY for value in text_recovery):
        return "STRONG_QUALIFIED"
    if all(value is not None and value >= MINIMUM_USEFUL_RECOVERY for value in text_recovery):
        return "QUALIFIED"
    hot_recovery = [cell.get("hot_text_recovery") for cell in cells]
    if all(
        value is not None and value >= MINIMUM_HOT_LAYOUT_RECOVERY
        for value in hot_recovery
    ):
        if all(value is not None and value >= 0 for value in text_recovery):
            return "HOT_LAYOUT_QUALIFIED"
    return "CURRENT_P2_RETAINED"


def _cross_workload_result(recoveries: list[float]) -> str:
    if len(recoveries) != 6:
        return "INCOMPLETE"
    if all(value >= STRONG_RECOVERY for value in recoveries):
        return "STRONG_MATERIAL_RECOVERY"
    if all(value >= MINIMUM_USEFUL_RECOVERY for value in recoveries):
        return "USEFUL_MATERIAL_RECOVERY"
    if any(value >= MINIMUM_USEFUL_RECOVERY for value in recoveries):
        return "WORKLOAD_SENSITIVE"
    return "SAFE_NOT_MATERIAL"


def _host_fingerprint(benchmark_base_sha: str, benchmark_source_sha: str) -> dict[str, Any]:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("campaign requires Linux x86-64")
    if not hasattr(time, "CLOCK_MONOTONIC_RAW"):
        raise RuntimeError("CLOCK_MONOTONIC_RAW is unavailable")
    if CPU_AFFINITY not in os.sched_getaffinity(0):
        raise RuntimeError("CPU 0 is outside the guest's allowed affinity set")
    taskset = shutil.which("taskset")
    if taskset is None or _run([taskset, "-c", str(CPU_AFFINITY), "true"]).returncode != 0:
        raise RuntimeError("taskset CPU 0 validation failed")
    lscpu = _run(["lscpu"]).stdout
    cpu = {
        key.strip(): value.strip()
        for line in lscpu.splitlines()
        if ":" in line
        for key, value in [line.split(":", 1)]
    }
    stable = {
        "architecture": platform.machine(),
        "cpu_model": cpu.get("Model name", platform.processor()),
        "cpu_vendor": cpu.get("Vendor ID", "UNAVAILABLE"),
        "cpu_family": cpu.get("CPU family", "UNAVAILABLE"),
        "cpu_model_id": cpu.get("Model", "UNAVAILABLE"),
        "cpu_stepping": cpu.get("Stepping", "UNAVAILABLE"),
        "physical_cores": cpu.get("Core(s) per socket", "UNAVAILABLE"),
        "logical_cores": os.cpu_count() or 1,
        "kernel": platform.release(),
        "distribution": Path("/etc/os-release").read_text(encoding="utf-8"),
    }
    fingerprint = hashlib.sha256(
        json.dumps(stable, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return {
        "host_fingerprint": fingerprint,
        "host": stable,
        "hostname": platform.node(),
        "python": platform.python_version(),
        "benchmark_base_sha": benchmark_base_sha,
        "benchmark_source_sha": benchmark_source_sha,
        "s3_control_sha": S3_CONTROL_SHA,
        "s3_experiment_sha": S3_EXPERIMENT_SHA,
        "s3_hardening_sha": S3_HARDENING_SHA,
        "cpu_affinity": sorted(os.sched_getaffinity(0)),
        "timed_affinity": CPU_AFFINITY,
        "external_warmups": EXTERNAL_WARMUPS,
        "inline_warmups": INLINE_WARMUPS,
        "repetitions_per_session": REPETITIONS,
        "independent_sessions": list(SESSIONS),
        "fresh_process_per_sample": True,
        "balanced_interleaving": True,
        "clock": "CLOCK_MONOTONIC_RAW",
        "load_average_before": os.getloadavg(),
    }


def _load_budget_plan_diagnostics(*, required: bool) -> Any | None:
    module_name = "bootstrap.s3.backends.x86_64.instruction_budget"
    try:
        budget_module = importlib.import_module(module_name)
    except ModuleNotFoundError as error:
        if not required and error.name == module_name:
            return None
        raise
    return budget_module.budget_plan_diagnostics


def _activate_backend(
    s3_repo: Path,
    *,
    require_budget_diagnostics: bool = True,
) -> tuple[Any, Any, Any | None]:
    pipeline = _activate_s3_modules(s3_repo)
    backend_module = importlib.import_module("bootstrap.s3.backends.x86_64.backend")
    diagnostics = _load_budget_plan_diagnostics(required=require_budget_diagnostics)
    return pipeline, backend_module.X8664Backend, diagnostics


def _compile_program(
    s3_repo: Path,
    source: str,
    optimization: str,
    *,
    require_budget_diagnostics: bool = True,
) -> tuple[Any, Any, Any | None]:
    pipeline, backend_type, diagnostics = _activate_backend(
        s3_repo,
        require_budget_diagnostics=require_budget_diagnostics,
    )
    compilation = pipeline.compile_source(source, optimization)
    _, program = compilation.require_ordinary_artifacts()
    return program, backend_type, diagnostics


def _emit_program(
    program: Any,
    backend_type: Any,
    diagnostics: Any,
    mode: str,
    *,
    ffi: bool,
) -> tuple[str, str, dict[str, Any]]:
    backend = _create_backend(backend_type, mode)
    assembly = backend._generate_ffi(program) if ffi else backend.generate(program)
    functions = (
        [
            diagnostics(function, max_instructions=S3_FFI_MAX_INSTRUCTIONS)
            for function in program.functions
        ]
        if diagnostics is not None
        else []
    )
    program_fingerprint = _sha256_text(repr(program))
    return assembly, program_fingerprint, _aggregate_segment_diagnostics(functions)


def _create_backend(backend_type: Any, mode: str) -> Any:
    parameters = inspect.signature(backend_type).parameters
    kwargs: dict[str, Any] = {"max_instructions": S3_FFI_MAX_INSTRUCTIONS}
    if "instruction_budget_mode" in parameters:
        kwargs["instruction_budget_mode"] = mode
    elif mode != "per-instruction":
        raise RuntimeError(
            "backend does not support the requested experimental instruction budget mode"
        )
    return backend_type(**kwargs)


def _emit(
    s3_repo: Path,
    source: str,
    optimization: str,
    mode: str,
    *,
    ffi: bool,
    require_budget_diagnostics: bool = True,
) -> tuple[str, Any, str, dict[str, Any]]:
    program, backend_type, diagnostics = _compile_program(
        s3_repo,
        source,
        optimization,
        require_budget_diagnostics=require_budget_diagnostics,
    )
    assembly, fingerprint, segments = _emit_program(
        program,
        backend_type,
        diagnostics,
        mode,
        ffi=ffi,
    )
    return assembly, program, fingerprint, segments


def _aggregate_segment_diagnostics(functions: list[dict[str, Any]]) -> dict[str, Any]:
    segments = [segment for function in functions for segment in function["segments"]]
    weights = [int(segment["logical_weight"]) for segment in segments]
    histogram: Counter[int] = Counter(weights)
    return {
        "logical_instructions": sum(int(item["logical_instruction_count"]) for item in functions),
        "segment_count": len(segments),
        "fast_segments": sum(int(item["fast_segment_count"]) for item in functions),
        "scalar_sites": sum(int(item["scalar_sites"]) for item in functions),
        "mean_segment_weight": statistics.fmean(weights) if weights else 0.0,
        "median_segment_weight": statistics.median(weights) if weights else 0,
        "max_segment_weight": max(weights, default=0),
        "segment_weight_histogram": [
            {"weight": weight, "segments": histogram[weight]}
            for weight in sorted(histogram)
        ],
        "call_barriers": sum(int(item["call_barriers"]) for item in functions),
        "control_barriers": sum(
            int(item["branch_barriers"]) + int(item["return_barriers"])
            for item in functions
        ),
        "functions": functions,
    }


def _control_assembly(
    control_repo: Path,
    source: str,
    optimization: str,
    *,
    ffi: bool,
) -> str:
    assembly, _program, _fingerprint, _segments = _emit(
        control_repo,
        source,
        optimization,
        "per-instruction",
        ffi=ffi,
        require_budget_diagnostics=False,
    )
    return assembly


def _text_section_bytes(executable: Path) -> int:
    return int(_executable_text_metrics(executable)["hot_text_bytes"])


def _executable_text_metrics(executable: Path) -> dict[str, int]:
    readelf = shutil.which("readelf")
    if readelf is None:
        raise RuntimeError("readelf is required for executable text section sizes")
    result = _run([readelf, "-W", "-S", str(executable)])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "readelf section query failed")
    section_sizes: dict[str, int] = {}
    executable_text_bytes = 0
    for line in result.stdout.splitlines():
        fields = line.split()
        index = next(
            (position for position, field in enumerate(fields) if field.startswith(".")),
            None,
        )
        if index is None or len(fields) <= index + 6:
            continue
        name = fields[index]
        size = int(fields[index + 4], 16)
        flags = fields[index + 6]
        if "A" in flags and "X" in flags:
            executable_text_bytes += size
        if name.startswith(".text"):
            section_sizes[name] = size
    if ".text" not in section_sizes:
        raise RuntimeError(f".text section was not found in {executable}")
    return {
        "hot_text_bytes": section_sizes[".text"],
        "cold_text_bytes": section_sizes.get(".text.unlikely", 0),
        "total_executable_text_bytes": executable_text_bytes,
    }


def _slow_path_instruction_count(assembly: str) -> int:
    in_slow_path = False
    in_cold_section = False
    count = 0
    for line in assembly.splitlines():
        stripped = line.strip()
        if stripped.startswith('.section .text.unlikely,'):
            in_cold_section = True
            continue
        if stripped == ".section .text":
            in_cold_section = False
            in_slow_path = False
            continue
        if in_cold_section:
            if _instruction_lines([line]):
                count += 1
            continue
        if stripped.endswith(":"):
            if stripped.startswith(".L__s3_budget_") and stripped.endswith("_slow:"):
                in_slow_path = True
            elif in_slow_path and (
                stripped.startswith(".L_s3_f")
                or stripped.startswith(".L__s3_budget_")
            ):
                in_slow_path = False
            continue
        if in_slow_path and stripped.startswith(".size "):
            in_slow_path = False
            continue
        if in_slow_path and _instruction_lines([line]):
            count += 1
    return count


def _slow_block_count(assembly: str) -> int:
    return sum(
        1
        for line in assembly.splitlines()
        if line.strip().startswith(".L__s3_budget_")
        and line.strip().endswith("_slow:")
    )


def _segment_plan_sha256(segments: dict[str, Any]) -> str:
    encoded = json.dumps(
        segments,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _native_metrics(assembly: str, executable: Path) -> dict[str, Any]:
    metrics = audit_assembly(assembly, binary=executable)
    text_metrics = _executable_text_metrics(executable)
    slow_instructions = _slow_path_instruction_count(assembly)
    metrics["elf_bytes"] = executable.stat().st_size
    metrics.update(text_metrics)
    metrics["text_bytes"] = text_metrics["total_executable_text_bytes"]
    metrics["static_native_instructions"] = int(metrics["total_instructions"])
    metrics["slow_path_native_instructions"] = slow_instructions
    metrics["slow_block_count"] = _slow_block_count(assembly)
    metrics["fast_path_native_instructions"] = (
        int(metrics["total_instructions"]) - slow_instructions
    )
    return metrics


def _write_assembly(path: Path, assembly: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(assembly, encoding="utf-8", newline="\n")


def _build_ffi_executable(
    assembly: str,
    root: Path,
    driver: Path,
    pilot: Any,
    workload: str,
    optimization: str,
    variant: str,
    k: int,
    s3_source_sha: str,
) -> Artifact:
    assembly_path = root / f"{variant.lower()}.s"
    executable = root / f"{variant.lower()}.so"
    object_path = root / f"{variant.lower()}.o"
    _write_assembly(assembly_path, assembly)
    compiler = shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")
    if compiler is None:
        raise RuntimeError("no native C compiler available")
    _compile_assembly_shared(compiler, assembly_path, object_path, executable)
    export_variant = "S3_FFI_O1" if optimization == "O1" else "S3_FFI_O0"
    symbol = _resolve_export_symbol(executable, pilot.symbol, export_variant)["export_symbol"]
    metrics = _native_metrics(assembly, executable)
    run = lambda executable=executable, workload=workload, variant=variant, symbol=symbol: _run_driver(
        driver, executable, workload, variant, symbol, k, pilot.expected, INLINE_WARMUPS
    )
    return Artifact(
        workload,
        variant,
        optimization,
        s3_source_sha,
        executable,
        assembly_path,
        _sha256_text(pilot.source),
        _path_sha256(assembly_path),
        sha256_file(executable),
        metrics,
        int(metrics["instruction_budget_check_sites"]),
        run,
    )


def _transform_variants(p0_assembly: str) -> dict[str, tuple[str, dict[str, Any]]]:
    pneg, pneg_report = remove_instruction_budget_instrumentation(p0_assembly)
    return {
        "PNEG": (pneg, pneg_report.as_dict()),
    }


def _make_jsmn_assembly_artifact(
    assembly: str,
    root: Path,
    workload: str,
    optimization: str,
    variant: str,
    source: str,
    expected: int,
    build_native_artifact: Callable[..., Any],
    s3_source_sha: str,
) -> Artifact:
    assembly_path = root / f"{variant.lower()}.s"
    executable = root / variant.lower()
    _write_assembly(assembly_path, assembly)
    compiler = shutil.which("cc") or shutil.which("gcc")
    if compiler is None:
        raise RuntimeError("a C compiler is required for JSMN native artifacts")
    build_native_artifact(assembly_path, executable, compiler)
    metrics = _native_metrics(assembly, executable)
    from tools.budget_generalization import _run_process  # noqa: PLC0415

    run = lambda executable=executable, expected=expected: _run_process(executable, expected)
    return Artifact(
        workload,
        variant,
        optimization,
        s3_source_sha,
        executable,
        assembly_path,
        _sha256_text(source),
        _path_sha256(assembly_path),
        sha256_file(executable),
        metrics,
        int(metrics["instruction_budget_check_sites"]),
        run,
    )


def _build_ffi_cell(
    *,
    workload: str,
    pilot: Any,
    optimization: str,
    k: int,
    raw_root: Path,
    control_repo: Path,
    experiment_repo: Path,
    hardening_repo: Path,
    driver: Path,
) -> tuple[dict[str, Artifact], dict[str, Any], dict[str, Any]]:
    cell_root = raw_root / workload.replace(".", "-") / optimization.lower()
    cell_root.mkdir(parents=True, exist_ok=False)
    control_assembly = _control_assembly(control_repo, pilot.source, optimization, ffi=True)
    isolation_root = raw_root / "experiment-isolation"
    control_path = isolation_root / f"{workload.replace('.', '-')}-{optimization.lower()}-control.s"
    _write_assembly(control_path, control_assembly)
    program, backend_type, diagnostics = _compile_program(
        experiment_repo,
        pilot.source,
        optimization,
    )
    p0_program = program
    p2_program = program
    p0_assembly, program_fingerprint, segments = _emit_program(
        p2_program,
        backend_type,
        diagnostics,
        "per-instruction",
        ffi=True,
    )
    p2_assembly, p2_fingerprint, _ = _emit_program(
        p2_program,
        backend_type,
        diagnostics,
        "exact-segment",
        ffi=True,
    )
    if p2_fingerprint != program_fingerprint:
        raise RuntimeError("P0/P2 did not use the same compiled AssemblyProgram")
    same_program_instance = _assert_same_program_instance(p0_program, p2_program, workload)

    p2h_program, p2h_backend_type, p2h_diagnostics = _compile_program(
        hardening_repo,
        pilot.source,
        optimization,
    )
    p2h_default_assembly, p2h_default_fingerprint, p2h_segments = _emit_program(
        p2h_program,
        p2h_backend_type,
        p2h_diagnostics,
        "per-instruction",
        ffi=True,
    )
    p2h_assembly, p2h_exact_fingerprint, p2h_exact_segments = _emit_program(
        p2h_program,
        p2h_backend_type,
        p2h_diagnostics,
        "exact-segment",
        ffi=True,
    )
    if p2h_default_fingerprint != program_fingerprint:
        raise RuntimeError("P2/P2H compiled AssemblyProgram fingerprints differ")
    if p2h_exact_fingerprint != p2h_default_fingerprint:
        raise RuntimeError("P2H default/exact emissions used different programs")
    if p2h_default_assembly != p0_assembly:
        raise RuntimeError("P2H PER_INSTRUCTION output changed from P0 byte identity")
    p2_plan_sha = _segment_plan_sha256(segments)
    p2h_plan_sha = _segment_plan_sha256(p2h_exact_segments)
    if p2h_exact_segments != segments or p2h_plan_sha != p2_plan_sha:
        raise RuntimeError("P2/P2H deterministic segment plans differ")
    if p2h_segments != p2h_exact_segments:
        raise RuntimeError("P2H diagnostics changed between default and exact emission")

    p0_sha = _sha256_text(p0_assembly)
    control_sha = _sha256_text(control_assembly)
    p2h_default_sha = _sha256_text(p2h_default_assembly)
    candidate_path = isolation_root / f"{workload.replace('.', '-')}-{optimization.lower()}-candidate-p0.s"
    _write_assembly(candidate_path, p0_assembly)
    isolation = {
        "workload": workload,
        "optimization": optimization,
        "control_sha": S3_CONTROL_SHA,
        "p2_source_sha": S3_EXPERIMENT_SHA,
        "p2h_source_sha": S3_HARDENING_SHA,
        "control_p0_assembly_sha256": control_sha,
        "candidate_p0_assembly_sha256": p0_sha,
        "p2h_default_assembly_sha256": p2h_default_sha,
        "assembly_equal": control_sha == p0_sha == p2h_default_sha,
        "candidate_source_sha256": _sha256_text(pilot.source),
        "p2_program_fingerprint": program_fingerprint,
        "p2h_program_fingerprint": p2h_default_fingerprint,
        "p2_p2h_same_assembly_program": p2h_default_fingerprint == program_fingerprint,
        "p0_and_p2_same_program_instance": same_program_instance,
        "p2_segment_plan_sha256": p2_plan_sha,
        "p2h_segment_plan_sha256": p2h_plan_sha,
        "p2_p2h_segment_plan_equal": p2_plan_sha == p2h_plan_sha,
        "backend_configuration_diff": "instruction_budget_mode only",
    }
    if not isolation["assembly_equal"]:
        raise RuntimeError(f"default-mode isolation failed for {workload}/{optimization}")
    _write_assembly(cell_root / "input.s3", pilot.source)
    derived = _transform_variants(p0_assembly)
    assemblies = {
        "P0": (p0_assembly, {}),
        "P2": (p2_assembly, {}),
        "P2H": (p2h_assembly, {}),
        "PNEG": derived["PNEG"],
    }
    artifacts: dict[str, Artifact] = {}
    transformations: dict[str, Any] = {}
    for variant, (assembly, report) in assemblies.items():
        label = f"{variant}_{optimization}"
        artifact_root = cell_root / variant.lower()
        artifact_root.mkdir(parents=True, exist_ok=False)
        artifacts[label] = _build_ffi_executable(
            assembly,
            artifact_root,
            driver,
            pilot,
            workload,
            optimization,
            label,
            k,
            S3_HARDENING_SHA if variant == "P2H" else S3_EXPERIMENT_SHA,
        )
        artifacts[label].static_metrics["fast_segment_count"] = (
            int(p2h_exact_segments["fast_segments"])
            if variant == "P2H"
            else int(segments["fast_segments"])
            if variant == "P2"
            else None
        )
        artifacts[label].static_metrics["segment_count"] = (
            int(p2h_exact_segments["segment_count"])
            if variant == "P2H"
            else int(segments["segment_count"])
            if variant == "P2"
            else None
        )
        transformations[label] = report
    segment_record = {
        "workload": workload,
        "optimization": optimization,
        "p2": segments,
        "p2h": p2h_exact_segments,
        "p2_sha256": p2_plan_sha,
        "p2h_sha256": p2h_plan_sha,
        "equal": p2_plan_sha == p2h_plan_sha,
    }
    return artifacts, isolation, {"transformations": transformations, "segments": segment_record}


def _build_jsmn_cells(
    *,
    k: int,
    raw_root: Path,
    control_repo: Path,
    experiment_repo: Path,
    hardening_repo: Path,
) -> tuple[dict[str, Artifact], list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    from tools.budget_generalization import _jsmn_apis  # noqa: PLC0415

    reference_oracle, run_hosted, build_native_artifact, _render_c, render_s3 = _jsmn_apis(experiment_repo)
    template_path = ROOT / "benchmarks/jsmn/s3/jsmn_demo.s3"
    fixture_path = ROOT / "benchmarks/jsmn/corpus/small/small_01_flat.json"
    template = template_path.read_text(encoding="utf-8")
    input_text = fixture_path.read_text(encoding="utf-8")
    reference_status, reference_tokens = reference_oracle(input_text.encode("ascii"))
    hosted = {}
    for optimization in ("O0", "O1"):
        actual = run_hosted(template, input_text, optimization)
        hosted[optimization] = {
            "status": actual.status,
            "tokens_equal": actual.tokens == reference_tokens,
            "reference_status": reference_status,
        }
        if actual.status != reference_status or actual.tokens != reference_tokens:
            raise RuntimeError(f"hosted JSMN oracle mismatch at {optimization}")
    expected = (abs(reference_status) * k) % 200
    all_artifacts: dict[str, Artifact] = {}
    isolation_rows: list[dict[str, Any]] = []
    transform_rows: dict[str, Any] = {}
    segments_by_opt: dict[str, Any] = {}
    for optimization in ("O0", "O1"):
        source = render_s3(template, input_text, k)
        control_assembly = _control_assembly(control_repo, source, optimization, ffi=False)
        program, backend_type, diagnostics = _compile_program(
            experiment_repo,
            source,
            optimization,
        )
        p0_program = program
        p2_program = program
        p0_assembly, fingerprint, segments = _emit_program(
            p2_program,
            backend_type,
            diagnostics,
            "per-instruction",
            ffi=False,
        )
        p2_assembly, p2_fingerprint, _ = _emit_program(
            p2_program,
            backend_type,
            diagnostics,
            "exact-segment",
            ffi=False,
        )
        if p2_fingerprint != fingerprint:
            raise RuntimeError("JSMN P0/P2 did not use the same compiled AssemblyProgram")
        same_program_instance = _assert_same_program_instance(
            p0_program,
            p2_program,
            "realworld.jsmn",
        )
        p2h_program, p2h_backend_type, p2h_diagnostics = _compile_program(
            hardening_repo,
            source,
            optimization,
        )
        p2h_default_assembly, p2h_default_fingerprint, p2h_default_segments = _emit_program(
            p2h_program,
            p2h_backend_type,
            p2h_diagnostics,
            "per-instruction",
            ffi=False,
        )
        p2h_assembly, p2h_fingerprint, p2h_segments = _emit_program(
            p2h_program,
            p2h_backend_type,
            p2h_diagnostics,
            "exact-segment",
            ffi=False,
        )
        if p2h_default_fingerprint != fingerprint or p2h_fingerprint != fingerprint:
            raise RuntimeError("JSMN P2/P2H compiled AssemblyProgram fingerprints differ")
        if p2h_default_assembly != p0_assembly:
            raise RuntimeError("JSMN P2H PER_INSTRUCTION output changed from P0 byte identity")
        p2_plan_sha = _segment_plan_sha256(segments)
        p2h_plan_sha = _segment_plan_sha256(p2h_segments)
        if p2h_segments != segments or p2h_plan_sha != p2_plan_sha:
            raise RuntimeError("JSMN P2/P2H deterministic segment plans differ")
        if p2h_default_segments != p2h_segments:
            raise RuntimeError("JSMN P2H diagnostics changed between default and exact emission")
        control_sha = _sha256_text(control_assembly)
        p0_sha = _sha256_text(p0_assembly)
        p2h_default_sha = _sha256_text(p2h_default_assembly)
        isolation = {
            "workload": "realworld.jsmn",
            "optimization": optimization,
            "control_sha": S3_CONTROL_SHA,
            "p2_source_sha": S3_EXPERIMENT_SHA,
            "p2h_source_sha": S3_HARDENING_SHA,
            "control_p0_assembly_sha256": control_sha,
            "candidate_p0_assembly_sha256": p0_sha,
            "p2h_default_assembly_sha256": p2h_default_sha,
            "assembly_equal": control_sha == p0_sha == p2h_default_sha,
            "candidate_source_sha256": _sha256_text(source),
            "p2_program_fingerprint": fingerprint,
            "p2h_program_fingerprint": p2h_default_fingerprint,
            "p2_p2h_same_assembly_program": p2h_default_fingerprint == fingerprint,
            "p0_and_p2_same_program_instance": same_program_instance,
            "p2_segment_plan_sha256": p2_plan_sha,
            "p2h_segment_plan_sha256": p2h_plan_sha,
            "p2_p2h_segment_plan_equal": p2_plan_sha == p2h_plan_sha,
            "backend_configuration_diff": "instruction_budget_mode only",
        }
        if not isolation["assembly_equal"]:
            raise RuntimeError(f"default-mode isolation failed for JSMN/{optimization}")
        isolation_rows.append(isolation)
        iso_root = raw_root / "experiment-isolation"
        _write_assembly(iso_root / f"realworld-jsmn-{optimization.lower()}-control.s", control_assembly)
        _write_assembly(iso_root / f"realworld-jsmn-{optimization.lower()}-candidate-p0.s", p0_assembly)
        cell_root = raw_root / "realworld-jsmn" / optimization.lower()
        cell_root.mkdir(parents=True, exist_ok=False)
        _write_assembly(cell_root / "input.s3", source)
        derived = _transform_variants(p0_assembly)
        variants = {
            "P0": (p0_assembly, S3_EXPERIMENT_SHA),
            "P2": (p2_assembly, S3_EXPERIMENT_SHA),
            "P2H": (p2h_assembly, S3_HARDENING_SHA),
            "PNEG": (derived["PNEG"][0], S3_EXPERIMENT_SHA),
        }
        for variant, (assembly, s3_source_sha) in variants.items():
            label = f"{variant}_{optimization}"
            artifact_root = cell_root / variant.lower()
            artifact_root.mkdir(parents=True, exist_ok=False)
            all_artifacts[label] = _make_jsmn_assembly_artifact(
                assembly,
                artifact_root,
                "realworld.jsmn",
                optimization,
                label,
                source,
                expected,
                build_native_artifact,
                s3_source_sha,
            )
            all_artifacts[label].static_metrics["fast_segment_count"] = (
                int(p2h_segments["fast_segments"])
                if variant == "P2H"
                else int(segments["fast_segments"])
                if variant == "P2"
                else None
            )
            all_artifacts[label].static_metrics["segment_count"] = (
                int(p2h_segments["segment_count"])
                if variant == "P2H"
                else int(segments["segment_count"])
                if variant == "P2"
                else None
            )
            if variant in derived:
                transform_rows[label] = derived[variant][1]
        segments_by_opt[optimization] = {
            "workload": "realworld.jsmn",
            "optimization": optimization,
            "p2": segments,
            "p2h": p2h_segments,
            "p2_sha256": p2_plan_sha,
            "p2h_sha256": p2h_plan_sha,
            "equal": p2_plan_sha == p2h_plan_sha,
        }
    correctness_meta = {
        "fixture_sha256": sha256_file(fixture_path),
        "template_sha256": sha256_file(template_path),
        "reference_status": reference_status,
        "reference_tokens": len(reference_tokens),
        "expected_native_accumulator": expected,
        "hosted_differential": hosted,
    }
    return all_artifacts, isolation_rows, transform_rows, {
        "correctness": correctness_meta,
        "segments": segments_by_opt,
    }


def _correctness_gate(artifacts: dict[str, Artifact], root: Path) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for label in VARIANTS:
        artifact = artifacts[label]
        row = artifact.run()
        rows[label] = row
    passed = all(row.get("status") == "PASS" for row in rows.values())
    payload = {"status": "PASS" if passed else "FAIL", "variants": rows}
    _write_json(root / "correctness.json", payload)
    if not passed:
        raise RuntimeError(f"native correctness failed: {rows}")
    return payload


def _warmups(artifacts: dict[str, Artifact], root: Path) -> dict[str, Any]:
    rows: dict[str, list[dict[str, Any]]] = {label: [] for label in VARIANTS}
    for repetition in range(EXTERNAL_WARMUPS):
        for label in _balanced_order(repetition):
            row = artifacts[label].run()
            row.update({"warmup": True, "repetition": repetition, "variant": label})
            rows[label].append(row)
            if row.get("status") != "PASS":
                _write_json(root / "warmups.json", rows)
                raise RuntimeError(f"warmup failed for {label}: {row}")
    _write_json(root / "warmups.json", rows)
    return rows


def _run_sessions(
    artifacts: dict[str, Artifact],
    root: Path,
    *,
    workload: str,
    optimization_by_variant: dict[str, str],
    k: int,
    host_fingerprint: str,
) -> dict[str, Any]:
    sessions: dict[str, Any] = {}
    for session_index, session in enumerate(SESSIONS):
        samples: dict[str, list[dict[str, Any]]] = {label: [] for label in VARIANTS}
        jsonl = (root / f"{session}.jsonl").open("w", encoding="utf-8", newline="\n")
        with jsonl:
            for repetition in range(REPETITIONS):
                for order, label in enumerate(_balanced_order(repetition, session_index), start=1):
                    row = artifacts[label].run()
                    row.update({
                        "campaign": CAMPAIGN,
                        "workload": workload,
                        "optimization": optimization_by_variant[label],
                        "session": session,
                        "repetition": repetition,
                        "order": order,
                        "variant": label,
                        "timestamp_ns": time.time_ns(),
                        "K": k,
                        "artifact_sha256": artifacts[label].executable_sha256,
                        "assembly_sha256": artifacts[label].assembly_sha256,
                        "s3_source_sha": artifacts[label].s3_source_sha,
                        "host_fingerprint": host_fingerprint,
                        "affinity": CPU_AFFINITY,
                        "inline_warmups": INLINE_WARMUPS,
                    })
                    samples[label].append(row)
                    jsonl.write(json.dumps(row, sort_keys=True, allow_nan=False) + "\n")
                    jsonl.flush()
                    if row.get("status") != "PASS":
                        _write_json(root / f"{session}.partial.json", {"session": session, "samples": samples})
                        raise RuntimeError(f"timed sample failed: {row}")
                print(f"{workload} {session} repetition {repetition + 1}/{REPETITIONS}", flush=True)
        payload = {
            "session": session,
            "samples": samples,
            "summaries": {label: _sample_summary(rows) for label, rows in samples.items()},
            "status": "PASS" if all(_sample_summary(rows)["status"] == "PASS" for rows in samples.values()) else "FAIL",
        }
        _write_json(root / f"{session}.json", payload)
        sessions[session] = payload
    return sessions


def _cell_metrics(
    sessions: dict[str, Any],
    artifacts: dict[str, Artifact],
    workload: str,
    optimization: str,
) -> dict[str, Any]:
    labels = {
        variant: f"{variant}_{optimization}"
        for variant in ("P0", "P2", "P2H", "PNEG")
    }
    medians = {
        variant: {
            session: float(sessions[session]["summaries"][label]["median_ns"])
            for session in SESSIONS
        }
        for variant, label in labels.items()
    }
    reproducibility = {
        variant: _relative_delta(values[SESSIONS[0]], values[SESSIONS[1]])
        for variant, values in medians.items()
    }
    times = {
        variant: statistics.fmean(values.values())
        for variant, values in medians.items()
    }
    p0 = artifacts[labels["P0"]].static_metrics
    p2 = artifacts[labels["P2"]].static_metrics
    p2h = artifacts[labels["P2H"]].static_metrics
    p2_added_text = p2["total_executable_text_bytes"] - p0["total_executable_text_bytes"]
    p2h_added_text = p2h["total_executable_text_bytes"] - p0["total_executable_text_bytes"]
    p2_added_hot = p2["hot_text_bytes"] - p0["hot_text_bytes"]
    p2h_added_hot = p2h["hot_text_bytes"] - p0["hot_text_bytes"]
    code_size = {
        variant: {
            "elf_bytes": artifacts[label].static_metrics["elf_bytes"],
            "total_executable_text_bytes": artifacts[label].static_metrics[
                "total_executable_text_bytes"
            ],
            "hot_text_bytes": artifacts[label].static_metrics["hot_text_bytes"],
            "cold_text_bytes": artifacts[label].static_metrics["cold_text_bytes"],
            "static_native_instructions": artifacts[label].static_metrics[
                "static_native_instructions"
            ],
            "fast_path_native_instructions": artifacts[label].static_metrics[
                "fast_path_native_instructions"
            ],
            "slow_path_native_instructions": artifacts[label].static_metrics[
                "slow_path_native_instructions"
            ],
            "fast_segment_count": artifacts[label].static_metrics["fast_segment_count"],
            "segment_count": artifacts[label].static_metrics["segment_count"],
            "slow_block_count": artifacts[label].static_metrics["slow_block_count"],
            "s3_source_sha": artifacts[label].s3_source_sha,
            "assembly_sha256": artifacts[label].assembly_sha256,
            "elf_sha256": artifacts[label].executable_sha256,
        }
        for variant, label in labels.items()
    }
    return {
        "workload": workload,
        "optimization": optimization,
        "K": TARGET_K[workload],
        "session_medians_ns": medians,
        "T_ns_mean_of_session_medians": times,
        "relative_session_median_delta": reproducibility,
        "reproducibility_pass": all(
            value <= MAX_RELATIVE_SESSION_MEDIAN_DELTA
            for value in reproducibility.values()
        ),
        **_recovery_metrics(times),
        "added_text_recovery": (
            (p2_added_text - p2h_added_text) / p2_added_text
            if p2_added_text != 0
            else None
        ),
        "hot_text_recovery": (
            (p2_added_hot - p2h_added_hot) / p2_added_hot
            if p2_added_hot != 0
            else None
        ),
        "code_size": {
            "variants": code_size,
            "P2_added_total_executable_text_bytes": p2_added_text,
            "P2H_added_total_executable_text_bytes": p2h_added_text,
            "P2_added_hot_text_bytes": p2_added_hot,
            "P2H_added_hot_text_bytes": p2h_added_hot,
        },
    }


def _build_ffi_workload(
    workload: str,
    pilot: Any,
    raw_root: Path,
    control_repo: Path,
    experiment_repo: Path,
    hardening_repo: Path,
    driver_root: Path,
) -> tuple[dict[str, Artifact], dict[str, Any], dict[str, Any]]:
    driver_root.mkdir(parents=True, exist_ok=True)
    driver_metadata = _build_driver(driver_root)
    driver = driver_root / "ffi_driver"
    artifacts: dict[str, Artifact] = {}
    isolations: dict[str, Any] = {}
    transformation_rows: dict[str, Any] = {}
    segments: dict[str, Any] = {}
    for optimization in ("O0", "O1"):
        cell_artifacts, isolation, metadata = _build_ffi_cell(
            workload=workload,
            pilot=pilot,
            optimization=optimization,
            k=TARGET_K[workload],
            raw_root=raw_root,
            control_repo=control_repo,
            experiment_repo=experiment_repo,
            hardening_repo=hardening_repo,
            driver=driver,
        )
        artifacts.update(cell_artifacts)
        isolations[optimization] = isolation
        transformation_rows.update(metadata["transformations"])
        segments[optimization] = metadata["segments"]
    return artifacts, {
        "driver": driver_metadata,
        "isolation": isolations,
        "transformations": transformation_rows,
        "segments": segments,
    }, {}


def run_campaign(
    control_repo: Path,
    experiment_repo: Path,
    hardening_repo: Path,
    benchmark_source_sha: str,
    benchmark_base_sha: str = BENCHMARK_BASE,
) -> Path:
    benchmark_source_sha = _require_repo_identity(
        ROOT,
        benchmark_source_sha,
        "benchmark source",
    )
    _require_ancestor(ROOT, benchmark_base_sha, benchmark_source_sha, "benchmark base")
    branch = _git_output(ROOT, "branch", "--show-current")
    if branch != BENCHMARK_BRANCH:
        raise RuntimeError(f"benchmark branch mismatch: expected={BENCHMARK_BRANCH} actual={branch}")
    if _git_output(ROOT, "merge-base", "--is-ancestor", benchmark_base_sha, benchmark_source_sha) == "":
        # --is-ancestor emits no stdout on success; its return code was checked above.
        pass
    require_commit(control_repo, S3_CONTROL_SHA, label="S3 control")
    require_commit(experiment_repo, S3_EXPERIMENT_SHA, label="S3 experiment")
    require_commit(hardening_repo, S3_HARDENING_SHA, label="S3 hardening")
    _require_repo_identity(control_repo, S3_CONTROL_SHA, "S3 control")
    _require_repo_identity(experiment_repo, S3_EXPERIMENT_SHA, "S3 experiment")
    _require_repo_identity(hardening_repo, S3_HARDENING_SHA, "S3 hardening")
    _require_ancestor(
        experiment_repo,
        S3_EXPERIMENT_SHA,
        S3_HARDENING_SHA,
        "P2 baseline in P2H lineage",
    )
    environment = _host_fingerprint(benchmark_base_sha, benchmark_source_sha)
    run_id = time.strftime("segment-budget-%Y%m%d-%H%M%S", time.gmtime()) + f"-{time.time_ns() % 1_000_000_000:09d}"
    report_root = ROOT / "reports" / "s3-experimental-segment-budget"
    raw_root = report_root / "raw" / run_id
    raw_root.mkdir(parents=True, exist_ok=False)
    _write_json(raw_root / "environment.json", environment)

    from benchmarks.scientific.xsbench.contract import pilot as xsbench_pilot  # noqa: PLC0415

    pilots = {pilot.workload_id: pilot for pilot in _pilot_sources()}
    xs_pilot = xsbench_pilot()
    pilots["scientific.xsbench.compatible_lookup.medium"] = xs_pilot
    all_workloads: dict[str, Any] = {}
    all_segments: dict[str, Any] = {}
    all_isolation: dict[str, Any] = {}
    all_transformations: dict[str, Any] = {}
    artifact_by_workload: dict[str, dict[str, Artifact]] = {}
    correctness_by_workload: dict[str, Any] = {}

    for workload in (
        "scientific.rmsd.batch",
        "scientific.xsbench.compatible_lookup.medium",
    ):
        pilot = pilots[workload]
        artifacts, metadata, _ = _build_ffi_workload(
            workload,
            pilot,
            raw_root,
            control_repo,
            experiment_repo,
            hardening_repo,
            raw_root / workload.replace(".", "-") / "driver",
        )
        artifact_by_workload[workload] = artifacts
        all_isolation[workload] = metadata["isolation"]
        all_segments[workload] = metadata["segments"]
        all_transformations[workload] = metadata["transformations"]

    jsmn_artifacts, jsmn_isolation, jsmn_transforms, jsmn_meta = _build_jsmn_cells(
        k=TARGET_K["realworld.jsmn"],
        raw_root=raw_root,
        control_repo=control_repo,
        experiment_repo=experiment_repo,
        hardening_repo=hardening_repo,
    )
    artifact_by_workload["realworld.jsmn"] = jsmn_artifacts
    all_isolation["realworld.jsmn"] = {row["optimization"]: row for row in jsmn_isolation}
    all_segments["realworld.jsmn"] = jsmn_meta["segments"]
    all_transformations["realworld.jsmn"] = jsmn_transforms
    all_workloads["realworld.jsmn"] = {"metadata": jsmn_meta["correctness"]}

    if not all(
        row["assembly_equal"]
        for workload_rows in all_isolation.values()
        for row in workload_rows.values()
    ):
        raise RuntimeError("P0 isolation did not match the pinned control in all six cells")
    _write_json(raw_root / "experiment-isolation.json", all_isolation)
    _write_json(raw_root / "segment-plans.json", all_segments)
    _write_json(raw_root / "transformations.json", all_transformations)

    for workload, artifacts in artifact_by_workload.items():
        _write_json(
            raw_root / workload.replace(".", "-") / "artifact-manifest.json",
            {
                "benchmark_source_sha": benchmark_source_sha,
                "artifacts": {
                    label: {
                        "workload": artifact.workload,
                        "variant": label.rsplit("_", 1)[0],
                        "optimization": artifact.optimization,
                        "s3_source_sha": artifact.s3_source_sha,
                        "source_sha256": artifact.source_sha256,
                        "assembly_sha256": artifact.assembly_sha256,
                        "elf_sha256": artifact.executable_sha256,
                        "elf_bytes": artifact.static_metrics["elf_bytes"],
                        "hot_text_bytes": artifact.static_metrics["hot_text_bytes"],
                        "cold_text_bytes": artifact.static_metrics["cold_text_bytes"],
                        "total_executable_text_bytes": artifact.static_metrics[
                            "total_executable_text_bytes"
                        ],
                    }
                    for label, artifact in sorted(artifacts.items())
                },
            },
        )
        correctness = _correctness_gate(artifacts, raw_root / workload.replace(".", "-"))
        correctness_by_workload[workload] = correctness
        all_workloads.setdefault(workload, {})["correctness"] = correctness
    _write_json(raw_root / "correctness.json", correctness_by_workload)

    optimization_by_variant = {
        label: "O0" if label.endswith("_O0") else "O1"
        for label in VARIANTS
    }
    timing_workloads: dict[str, Any] = {}
    for workload, artifacts in artifact_by_workload.items():
        workload_root = raw_root / workload.replace(".", "-")
        _warmups(artifacts, workload_root)
        sessions = _run_sessions(
            artifacts,
            workload_root,
            workload=workload,
            optimization_by_variant=optimization_by_variant,
            k=TARGET_K[workload],
            host_fingerprint=environment["host_fingerprint"],
        )
        cells = [
            _cell_metrics(sessions, artifacts, workload, optimization)
            for optimization in ("O0", "O1")
        ]
        for cell in cells:
            cell["correctness_pass"] = correctness_by_workload[workload]["status"] == "PASS"
        timing_workloads[workload] = {
            "K": TARGET_K[workload],
            "cells": cells,
            "sessions": {name: sessions[name]["summaries"] for name in SESSIONS},
            "all_variants_reproducible": all(cell["reproducibility_pass"] for cell in cells),
            "all_samples_pass": all(
                sessions[name]["status"] == "PASS" for name in SESSIONS
            ),
        }
        _write_json(workload_root / "workload-summary.json", timing_workloads[workload])

    recovery_values = [
        float(cell["p2_recovered_budget_excess"])
        for workload in timing_workloads.values()
        for cell in workload["cells"]
        if cell["p2_recovered_budget_excess"] is not None
    ]
    all_reproducible = all(
        workload["all_variants_reproducible"]
        for workload in timing_workloads.values()
    )
    all_samples_pass = all(item["all_samples_pass"] for item in timing_workloads.values())
    all_correctness_pass = all(
        item["status"] == "PASS" for item in correctness_by_workload.values()
    )
    cross_workload = _cross_workload_result(recovery_values)
    hardening_cells = [
        cell
        for workload in timing_workloads.values()
        for cell in workload["cells"]
    ]
    hardening_result = _hardening_result(hardening_cells)
    h12 = {
        "status": {
            "STRONG_QUALIFIED": "CONFIRMED_STRUCTURAL_AND_SAFE",
            "QUALIFIED": "CONFIRMED_STRUCTURAL_AND_SAFE",
            "HOT_LAYOUT_QUALIFIED": "CONFIRMED_HOT_LAYOUT_ONLY",
            "CURRENT_P2_RETAINED": "SAFE_NOT_STRUCTURALLY_MATERIAL",
            "REJECTED_PERFORMANCE_REGRESSION": "REJECTED_PERFORMANCE",
            "REJECTED_SEMANTICS": "REJECTED_SEMANTICS",
            "REJECTED_COMPLEXITY": "REJECTED_COMPLEXITY",
        }.get(hardening_result, "BLOCKED"),
        "h12a_status": (
            "CONFIRMED_HOT_LAYOUT_ONLY"
            if hardening_result == "HOT_LAYOUT_QUALIFIED"
            else "UNDER_TEST"
            if hardening_result in {"INCOMPLETE", "BLOCKED"}
            else "NOT_CONFIRMED"
        ),
    }
    result = {
        "campaign": CAMPAIGN,
        "benchmark_base_sha": benchmark_base_sha,
        "benchmark_source_head": benchmark_source_sha,
        "s3_control_sha": S3_CONTROL_SHA,
        "s3_experiment_sha": S3_EXPERIMENT_SHA,
        "s3_hardening_sha": S3_HARDENING_SHA,
        "experiment_isolation": "PASS",
        "default_mode": "per-instruction",
        "experiment_mode": "exact-segment",
        "p0_p2_same_source_and_program": True,
        "p0_p2_only_configuration_difference": "instruction_budget_mode",
        "workloads": timing_workloads,
        "correctness": correctness_by_workload,
        "segment_plans": all_segments,
        "transformations": all_transformations,
        "timing_protocol": {
            "external_warmups": EXTERNAL_WARMUPS,
            "inline_warmups": INLINE_WARMUPS,
            "repetitions_per_session": REPETITIONS,
            "independent_sessions": list(SESSIONS),
            "fresh_process_per_sample": True,
            "balanced_interleaving": True,
            "cpu_affinity": CPU_AFFINITY,
            "clock": "CLOCK_MONOTONIC_RAW",
            "T_definition": "arithmetic mean of the two independent session medians",
            "reproducibility_threshold": MAX_RELATIVE_SESSION_MEDIAN_DELTA,
        },
        "reproducibility": "PASS" if all_reproducible else "FAIL",
        "all_timed_samples_pass": all_samples_pass,
        "minimum_useful_recovery": MINIMUM_USEFUL_RECOVERY,
        "strong_recovery": STRONG_RECOVERY,
        "p2_cross_workload_result": cross_workload,
        "hardening_thresholds": {
            "max_runtime_regression": MAX_HARDENING_RUNTIME_REGRESSION,
            "minimum_useful_added_text_recovery": MINIMUM_USEFUL_RECOVERY,
            "strong_added_text_recovery": STRONG_RECOVERY,
            "minimum_retained_budget_recovery": MINIMUM_RETAINED_BUDGET_RECOVERY,
            "minimum_hot_layout_recovery": MINIMUM_HOT_LAYOUT_RECOVERY,
        },
        "hardening_result": hardening_result,
        "h12": h12,
        "budget_line_continues": (
            "HARDENING_ONLY"
            if cross_workload in {"STRONG_MATERIAL_RECOVERY", "USEFUL_MATERIAL_RECOVERY"}
            else "NO"
        ),
        "no_further_budget_architectures": True,
        "s3_production_change_ready": False,
        "dynamic_accounting_events": "NOT_MEASURED",
        "raw_evidence": str(raw_root.relative_to(ROOT)),
        "raw_evidence_manifest": "raw-evidence-manifest.json",
        "p0_byte_identity": all(
            row["assembly_equal"]
            for workload_rows in all_isolation.values()
            for row in workload_rows.values()
        ),
        "p2_segment_plan_identity": all(
            row["equal"]
            for workload_rows in all_segments.values()
            for row in workload_rows.values()
        ),
        "e0_status": "PASS" if all_correctness_pass else "FAIL",
        "p2h_correctness": "PASS" if all_correctness_pass else "FAIL",
        "production_ready": False,
        "next_campaign": "S3_EXACT_SEGMENT_BUDGET_PRODUCTION_READINESS_REVIEW",
        "status": (
            "PASS"
            if all_correctness_pass
            and all_samples_pass
            and all_reproducible
            and hardening_result not in {"BLOCKED", "INCOMPLETE"}
            else "INCONCLUSIVE"
        ),
    }
    _write_json(raw_root / "campaign-result.json", result)
    manifest_result = _write_raw_manifest(raw_root)
    _write_json(report_root / "EXPERIMENTAL_SEGMENT_BUDGET_RESULT.json", result)
    print(f"EXPERIMENTAL_SEGMENT_BUDGET_RESULT={report_root / 'EXPERIMENTAL_SEGMENT_BUDGET_RESULT.json'}", flush=True)
    print(f"RAW_EVIDENCE={raw_root}", flush=True)
    print(f"RAW_EVIDENCE_MANIFEST={manifest_result['path']} ENTRIES={manifest_result['entry_count']}", flush=True)
    return report_root / "EXPERIMENTAL_SEGMENT_BUDGET_RESULT.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-control", type=Path, required=True)
    parser.add_argument("--s3-experiment", type=Path, required=True)
    parser.add_argument("--s3-hardening", type=Path, required=True)
    parser.add_argument("--benchmark-source-sha", required=True)
    parser.add_argument("--benchmark-base-sha", default=BENCHMARK_BASE)
    args = parser.parse_args(argv)
    result = run_campaign(
        args.s3_control,
        args.s3_experiment,
        args.s3_hardening,
        args.benchmark_source_sha,
        args.benchmark_base_sha,
    )
    print(f"RESULT={result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
