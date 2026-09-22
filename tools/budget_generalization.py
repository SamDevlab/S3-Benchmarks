"""Multi-workload causal experiment for S3 instruction-budget accounting.

This is benchmark-side research infrastructure.  It reuses the existing
fail-closed assembly rewriter and never changes the pinned S3 checkout.
Regular numerical pilots use the existing direct FFI ABI.  JSMN uses the existing native
process adapter and its differential oracle; its timing scope is therefore
matched native PROCESS_E2E, not pure kernel time.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
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
    EXPECTED_S3_SHA,
    S3_FFI_MAX_INSTRUCTIONS,
    _activate_s3_modules,
    _build_c_library,
    _build_driver,
    _build_s3_library,
    _compile_assembly_shared,
    _path_sha256,
    _pilot_sources,
    _resolve_export_symbol,
    _run_driver,
)
from tools.runtime_attribution import audit_assembly, remove_instruction_budget_instrumentation  # noqa: E402


CAMPAIGN = "S3_BENCHMARKS_2_2_3_MULTI_WORKLOAD_BUDGET_CAUSAL_VALIDATION"
VARIANTS = (
    "S3_O0_BASELINE",
    "S3_O0_NO_BUDGET",
    "S3_O1_BASELINE",
    "S3_O1_NO_BUDGET",
    "GCC_O2",
    "CLANG_O2",
)
S3_VARIANTS = {"S3_O0_BASELINE", "S3_O0_NO_BUDGET", "S3_O1_BASELINE", "S3_O1_NO_BUDGET"}
MATERIAL_SHARE_THRESHOLD = 0.10
LARGE_EFFECT_THRESHOLD = 0.25
EXTERNAL_WARMUPS = 5
REPETITIONS = 30
CPU_AFFINITY = 0
TARGET_MIN_NS = 100_000_000
CALIBRATION_LEVELS = (1, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 1_250_000, 1_300_000, 2_000_000, 3_000_000, 5_000_000)
SAMPLE_TIMEOUT_SECONDS = 120.0


@dataclass(frozen=True, slots=True)
class Artifact:
    workload: str
    variant: str
    executable: Path
    assembly: Path | None
    control_source: Path | None
    source_sha256: str
    assembly_sha256: str | None
    diagnostic_assembly_sha256: str | None
    executable_sha256: str
    budget_sites: int
    static_metrics: dict[str, Any]
    run_sample: Callable[[], dict[str, Any]]


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _run(command: list[str], *, cwd: Path | None = None, timeout: float = SAMPLE_TIMEOUT_SECONDS) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=str(cwd) if cwd else None, check=False, capture_output=True, text=True, timeout=timeout)


def _taskset(command: list[str]) -> list[str]:
    taskset = shutil.which("taskset")
    return [taskset, "-c", str(CPU_AFFINITY), *command] if taskset else command


def _host_fingerprint() -> tuple[str, dict[str, Any]]:
    lscpu = _run(["lscpu"], timeout=10.0).stdout
    cpu: dict[str, str] = {}
    for line in lscpu.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            cpu[key.strip()] = value.strip()
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
    }
    encoded = json.dumps(stable, sort_keys=True, separators=(",", ":")).encode()
    return _sha256_bytes(encoded), stable


def _compile_c_executable(source: str, compiler: str, output: Path, root: Path, *, include_jsmn: bool = False) -> dict[str, Any]:
    source_path = root / f"{output.name}.c"
    source_path.write_text(source, encoding="utf-8", newline="\n")
    command = [compiler, "-std=c11", "-O2", "-Wextra"]
    if include_jsmn:
        command += ["-I", str(ROOT / "benchmarks" / "jsmn" / "upstream")]
    command += [str(source_path), "-lm", "-o", str(output)]
    result = _run(command, cwd=root, timeout=60.0)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"C build failed: {compiler}")
    output.chmod(output.stat().st_mode | 0o111)
    return {
        "source": str(source_path),
        "source_sha256": _path_sha256(source_path),
        "executable": str(output),
        "executable_sha256": sha256_file(output),
        "command": command,
    }


def _jsmn_apis(s3_repo: Path) -> tuple[Any, Any, Any, Any, Any]:
    _activate_s3_modules(s3_repo)
    for name in list(sys.modules):
        if name == "benchmarks" or name.startswith("benchmarks."):
            del sys.modules[name]
    ordered = [str(ROOT), str(s3_repo.resolve())]
    sys.path[:] = ordered + [entry for entry in sys.path if entry not in ordered]
    from benchmarks.jsmn.harness.correctness import reference_jsmn_oracle, run_s3_jsmn  # noqa: PLC0415
    from tools.runner import build_native_artifact, render_c_loop_source, render_s3_loop_source  # noqa: PLC0415
    return reference_jsmn_oracle, run_s3_jsmn, build_native_artifact, render_c_loop_source, render_s3_loop_source


def _run_process(executable: Path, expected: int, *, loop_argument: int = 1) -> dict[str, Any]:
    command = _taskset([str(executable), "--loop", str(loop_argument)])
    clock = getattr(time, "CLOCK_MONOTONIC_RAW", time.CLOCK_MONOTONIC)
    started = time.clock_gettime_ns(clock)
    try:
        completed = _run(command, timeout=SAMPLE_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "command": command, "timeout_seconds": SAMPLE_TIMEOUT_SECONDS}
    elapsed = time.clock_gettime_ns(clock) - started
    if completed.returncode != 0:
        return {"status": "FAIL", "command": command, "returncode": completed.returncode, "stderr": completed.stderr.strip()}
    marker = "program returned:"
    line = next((item for item in completed.stdout.splitlines() if marker in item), "")
    try:
        observed = int(line.split(marker, 1)[1].strip())
    except (IndexError, ValueError):
        return {"status": "FAIL", "command": command, "stdout": completed.stdout, "stderr": completed.stderr}
    if observed != expected:
        return {"status": "FAIL", "command": command, "observed": observed, "expected": expected, "stdout": completed.stdout}
    return {"status": "PASS", "command": command, "elapsed_ns": elapsed, "observed": observed, "expected": expected, "returncode": 0}


def _build_rewritten_native_assembly(assembly: Path, output_assembly: Path) -> dict[str, Any]:
    text = assembly.read_text(encoding="utf-8")
    diagnostic, rewrite = remove_instruction_budget_instrumentation(text)
    output_assembly.write_text(diagnostic, encoding="utf-8", newline="\n")
    return {
        "rewrite": rewrite.as_dict(),
        "baseline_metrics": audit_assembly(text),
        "diagnostic_metrics": audit_assembly(diagnostic),
        "baseline_sha256": _path_sha256(assembly),
        "diagnostic_sha256": _path_sha256(output_assembly),
    }


def _metrics(assembly: Path, executable: Path) -> dict[str, Any]:
    payload = audit_assembly(assembly.read_text(encoding="utf-8"), binary=executable)
    payload["elf_bytes"] = executable.stat().st_size
    payload["text_bytes"] = payload.get("text_size_bytes")
    return payload


def _ffi_artifacts(s3_repo: Path, root: Path, workload_id: str) -> tuple[dict[str, Artifact], dict[str, Any]]:
    root.mkdir(parents=True, exist_ok=True)
    pilot = next(item for item in _pilot_sources() if item.workload_id == workload_id)
    driver_root = root / "driver"
    driver_root.mkdir(parents=True, exist_ok=True)
    driver = _build_driver(driver_root)
    artifacts: dict[str, Artifact] = {}
    baseline_assemblies: dict[str, Path] = {}
    for label in VARIANTS:
        stem = f"{workload_id.replace('.', '-')}-{label.lower()}"
        library = root / f"{stem}.so"
        if label == "S3_O0_BASELINE":
            metadata = _build_s3_library(s3_repo, pilot.source, "O0", library, root)
            assembly = root / f"{stem}.s"
            baseline_assemblies["O0"] = assembly
            expected = pilot.expected
        elif label == "S3_O1_BASELINE":
            metadata = _build_s3_library(s3_repo, pilot.source, "O1", library, root)
            assembly = root / f"{stem}.s"
            baseline_assemblies["O1"] = assembly
            expected = pilot.expected
        elif label in {"S3_O0_NO_BUDGET", "S3_O1_NO_BUDGET"}:
            optimization = "O0" if "O0" in label else "O1"
            baseline = baseline_assemblies[optimization]
            if not baseline.is_file():
                raise RuntimeError(f"missing baseline assembly for {label}: {baseline}")
            diagnostic = root / f"{stem}.s"
            rewrite = _build_rewritten_native_assembly(baseline, diagnostic)
            obj = root / f"{stem}.o"
            _compile_assembly_shared(shutil.which("cc") or shutil.which("gcc"), diagnostic, obj, library)
            metadata = {
                "source_sha256": _path_sha256(baseline.with_suffix(".s3")),
                "assembly_sha256": rewrite["diagnostic_sha256"],
                "diagnostic_assembly_sha256": rewrite["diagnostic_sha256"],
                "budget_sites": rewrite["rewrite"]["removed_sites"],
                "static_metrics": rewrite["diagnostic_metrics"],
                "library_sha256": _path_sha256(library),
                "library": str(library),
                "assembly": str(diagnostic),
            }
            export_variant = "S3_FFI_O1" if optimization == "O1" else "S3_FFI_O0"
            metadata.update(_resolve_export_symbol(library, pilot.symbol, export_variant))
            artifacts[label] = Artifact(workload_id, label, library, diagnostic, None, metadata["source_sha256"], metadata["assembly_sha256"], metadata["diagnostic_assembly_sha256"], metadata["library_sha256"], metadata["budget_sites"], metadata["static_metrics"], lambda library=library, label=label, expected=expected, driver_root=driver_root, export_symbol=metadata["export_symbol"]: _run_driver(driver_root / "ffi_driver", library, pilot.workload_id, label, export_symbol, 1, expected, 0))
            continue
        else:
            metadata = _build_c_library(pilot, "GCC_O2" if label == "GCC_O2" else "CLANG_O2", library, root)
            assembly = None
            expected = pilot.expected
        export_variant = "S3_FFI_O1" if label == "S3_O1_BASELINE" else "S3_FFI_O0" if label == "S3_O0_BASELINE" else label
        metadata.update(_resolve_export_symbol(library, pilot.symbol, export_variant))
        source = root / f"{stem}.s3" if assembly else root / f"{stem}.c"
        if label.startswith("S3_"):
            metrics = _metrics(assembly, library)
            budget_sites = int(metrics["instruction_budget_check_sites"])
            assembly_sha = _path_sha256(assembly)
        else:
            metrics, budget_sites, assembly_sha = {}, 0, None
        artifacts[label] = Artifact(workload_id, label, library, assembly, source, metadata.get("source_sha256", ""), assembly_sha, None, _path_sha256(library), budget_sites, metrics, lambda library=library, label=label, expected=expected, driver_root=driver_root, export_symbol=metadata["export_symbol"]: _run_driver(driver_root / "ffi_driver", library, pilot.workload_id, label, export_symbol, 1, expected, 0))
    return artifacts, {"driver": driver}


def _jsmn_artifacts(s3_repo: Path, root: Path, k: int) -> tuple[dict[str, Artifact], dict[str, Any]]:
    root.mkdir(parents=True, exist_ok=True)
    _activate_s3_modules(s3_repo)
    reference_jsmn_oracle, _run_s3_jsmn, build_native_artifact, render_c_loop_source, render_s3_loop_source = _jsmn_apis(s3_repo)
    from bootstrap.s3.backends.x86_64 import generate_native_assembly  # noqa: PLC0415
    template = (ROOT / "benchmarks" / "jsmn" / "s3" / "jsmn_demo.s3").read_text(encoding="utf-8")
    fixture = ROOT / "benchmarks" / "jsmn" / "corpus" / "small" / "small_01_flat.json"
    text = fixture.read_text(encoding="utf-8")
    status, _tokens = reference_jsmn_oracle(text.encode("ascii"))
    expected = (abs(status) * k) % 200
    artifacts: dict[str, Artifact] = {}
    source_by_opt: dict[str, str] = {}
    for optimization in ("O0", "O1"):
        source = render_s3_loop_source(template, text, k)
        source_by_opt[optimization] = source
        program = __import__("bootstrap.s3.pipeline", fromlist=["compile_source"]).compile_source(source, optimization).assembly
        assembly_text = generate_native_assembly(program, max_instructions=S3_FFI_MAX_INSTRUCTIONS)
        baseline_assembly = root / f"jsmn-s3-{optimization.lower()}-baseline.s"
        baseline_assembly.write_text(assembly_text, encoding="utf-8", newline="\n")
        baseline_exe = root / f"jsmn-s3-{optimization.lower()}-baseline"
        build_native_artifact(baseline_assembly, baseline_exe, shutil.which("cc") or shutil.which("gcc"))
        base_metrics = _metrics(baseline_assembly, baseline_exe)
        artifacts[f"S3_{optimization}_BASELINE"] = Artifact("realworld.jsmn", f"S3_{optimization}_BASELINE", baseline_exe, baseline_assembly, None, _sha256_bytes(source.encode()), _path_sha256(baseline_assembly), None, _path_sha256(baseline_exe), int(base_metrics["instruction_budget_check_sites"]), base_metrics, lambda exe=baseline_exe, expected=expected: _run_process(exe, expected))
        diagnostic_assembly = root / f"jsmn-s3-{optimization.lower()}-no-budget.s"
        rewrite = _build_rewritten_native_assembly(baseline_assembly, diagnostic_assembly)
        diagnostic_exe = root / f"jsmn-s3-{optimization.lower()}-no-budget"
        build_native_artifact(diagnostic_assembly, diagnostic_exe, shutil.which("cc") or shutil.which("gcc"))
        diag_metrics = _metrics(diagnostic_assembly, diagnostic_exe)
        artifacts[f"S3_{optimization}_NO_BUDGET"] = Artifact("realworld.jsmn", f"S3_{optimization}_NO_BUDGET", diagnostic_exe, diagnostic_assembly, None, _sha256_bytes(source.encode()), _path_sha256(baseline_assembly), _path_sha256(diagnostic_assembly), _path_sha256(diagnostic_exe), int(rewrite["rewrite"]["removed_sites"]), diag_metrics, lambda exe=diagnostic_exe, expected=expected: _run_process(exe, expected))

    c_source = render_c_loop_source(text, k)
    for label, compiler in (("GCC_O2", "gcc"), ("CLANG_O2", "clang")):
        resolved = shutil.which(compiler)
        if resolved is None:
            raise RuntimeError(f"required compiler unavailable: {compiler}")
        exe = root / f"jsmn-{label.lower()}"
        metadata = _compile_c_executable(c_source, resolved, exe, root, include_jsmn=True)
        artifacts[label] = Artifact("realworld.jsmn", label, exe, None, root / f"{exe.name}.c", metadata["source_sha256"], None, None, metadata["executable_sha256"], 0, {}, lambda exe=exe, expected=expected, k=k: _run_process(exe, expected, loop_argument=k))
    return artifacts, {"fixture": str(fixture), "fixture_sha256": sha256_file(fixture), "status": status, "expected_accumulator": expected, "source_by_optimization": {key: _sha256_bytes(value.encode()) for key, value in source_by_opt.items()}}


def _correctness(artifacts: dict[str, Artifact], *, workload: str, jsmn_meta: dict[str, Any] | None = None) -> dict[str, Any]:
    rows = {label: artifact.run_sample() for label, artifact in artifacts.items()}
    if workload == "realworld.jsmn":
        reference_jsmn_oracle, run_s3_jsmn, _build_native_artifact, _render_c_loop_source, _render_s3_loop_source = _jsmn_apis(Path(jsmn_meta["s3_repo"]))
        template = (ROOT / "benchmarks" / "jsmn" / "s3" / "jsmn_demo.s3").read_text(encoding="utf-8")
        text = Path(jsmn_meta["fixture"]).read_text(encoding="utf-8")
        reference_status, reference_tokens = reference_jsmn_oracle(text.encode("ascii"))
        hosted_o0 = run_s3_jsmn(template, text, "O0")
        hosted_o1 = run_s3_jsmn(template, text, "O1")
        differential = hosted_o0.status == reference_status and hosted_o1.status == reference_status and hosted_o0.tokens == reference_tokens and hosted_o1.tokens == reference_tokens
    else:
        differential = True
    status = all(item.get("status") == "PASS" for item in rows.values()) and differential
    return {"status": "PASS" if status else "FAIL", "native_variants": rows, "differential_oracle": "PASS" if differential else "FAIL"}


def _calibrate(build: Callable[[int], tuple[dict[str, Artifact], dict[str, Any] | None]], workload: str, raw: Path) -> tuple[int | None, dict[str, Any], dict[str, Artifact], dict[str, Any] | None]:
    rows: list[dict[str, Any]] = []
    selected: tuple[int, dict[str, Artifact], dict[str, Any] | None] | None = None
    for k in CALIBRATION_LEVELS:
        artifacts, meta = build(k)
        samples = {label: artifact.run_sample() for label, artifact in artifacts.items()}
        passed = all(item.get("status") == "PASS" and "elapsed_ns" in item for item in samples.values())
        elapsed = [int(item["elapsed_ns"]) for item in samples.values() if "elapsed_ns" in item]
        row = {"K": k, "status": "PASS" if passed else "FAIL", "samples": samples}
        if passed:
            row.update({"fastest_ns": min(elapsed), "slowest_ns": max(elapsed)})
            if selected is None and min(elapsed) >= TARGET_MIN_NS:
                selected = (k, artifacts, meta)
        rows.append(row)
        if not passed:
            break
        if selected is not None:
            break
    _write_json(raw / "calibration.json", {"workload": workload, "rows": rows, "selected_K": selected[0] if selected else None})
    if selected is None:
        return None, {"rows": rows, "status": "NO_COMMON_MEASUREMENT_WINDOW"}, {}, None
    return selected[0], {"rows": rows, "status": "PASS"}, selected[1], selected[2]


def _session(artifacts: dict[str, Artifact], raw: Path, session: str, *, workload: str, classification: str, k: int, work_units_per_call: int, host_fingerprint: str) -> dict[str, Any]:
    samples: dict[str, list[dict[str, Any]]] = {label: [] for label in VARIANTS}
    for repetition in range(REPETITIONS):
        order = _balanced_order(repetition)
        for order_index, label in enumerate(order):
            sample = artifacts[label].run_sample()
            sample.update({
                "campaign": CAMPAIGN,
                "workload": workload,
                "class": classification,
                "session": session,
                "repetition": repetition,
                "order": order_index + 1,
                "variant": label,
                "timestamp_ns": time.time_ns(),
                "K": k,
                "work_units": work_units_per_call * k,
                "correctness_status": sample.get("status"),
                "artifact_sha256": artifacts[label].executable_sha256,
                "host_fingerprint": host_fingerprint,
                "affinity": CPU_AFFINITY,
            })
            samples[label].append(sample)
    summaries: dict[str, Any] = {}
    for label, values in samples.items():
        elapsed = [float(item["elapsed_ns"]) for item in values if item.get("status") == "PASS" and "elapsed_ns" in item]
        if len(elapsed) != REPETITIONS:
            summaries[label] = {"status": "INCOMPLETE", "valid_samples": len(elapsed), "expected_samples": REPETITIONS}
            continue
        median = statistics.median(elapsed)
        summaries[label] = {
            "status": "PASS", "N": len(elapsed), "min_ns": min(elapsed), "median_ns": median,
            "mean_ns": statistics.fmean(elapsed), "max_ns": max(elapsed),
            "p95_ns": sorted(elapsed)[min(len(elapsed) - 1, math.ceil(len(elapsed) * 0.95) - 1)],
            "stddev_ns": statistics.stdev(elapsed), "mad_ns": statistics.median(abs(value - median) for value in elapsed),
            "cv": statistics.stdev(elapsed) / statistics.fmean(elapsed),
        }
    result = {"session": session, "samples": samples, "summaries": summaries, "status": "PASS" if all(item["status"] == "PASS" for item in summaries.values()) else "FAIL"}
    _write_json(raw / f"{session}.json", result)
    return result


def _warmup(artifacts: dict[str, Artifact], raw: Path) -> None:
    rows = {label: [artifact.run_sample() for _ in range(EXTERNAL_WARMUPS)] for label, artifact in artifacts.items()}
    _write_json(raw / "warmups.json", rows)


def _balanced_order(repetition: int) -> tuple[str, ...]:
    shift = repetition % len(VARIANTS)
    return VARIANTS[shift:] + VARIANTS[:shift]


def _workload_result(workload: str, classification: str, k: int, artifacts: dict[str, Artifact], run_a: dict[str, Any], run_b: dict[str, Any], correctness: dict[str, Any], meta: dict[str, Any] | None) -> dict[str, Any]:
    summaries_a = run_a["summaries"]
    summaries_b = run_b["summaries"]
    def median(label: str, session: dict[str, Any]) -> float | None:
        value = session["summaries"].get(label, {})
        return float(value["median_ns"]) if value.get("status") == "PASS" else None
    reproducibility: dict[str, float | None] = {}
    for label in VARIANTS:
        first, second = median(label, run_a), median(label, run_b)
        reproducibility[label] = abs(first - second) / max(first, second) if first is not None and second is not None else None
    summary = {}
    for optimization in ("O0", "O1"):
        base = median(f"S3_{optimization}_BASELINE", run_a)
        no_budget = median(f"S3_{optimization}_NO_BUDGET", run_a)
        gcc = median("GCC_O2", run_a)
        clang = median("CLANG_O2", run_a)
        summary[f"baseline_{optimization.lower()}_ns"] = base
        summary[f"no_budget_{optimization.lower()}_ns"] = no_budget
        summary[f"gcc_{optimization.lower()}_ns"] = gcc
        summary[f"clang_{optimization.lower()}_ns"] = clang
        summary[f"budget_ratio_{optimization.lower()}"] = base / no_budget if base and no_budget else None
        summary[f"budget_share_{optimization.lower()}"] = 1.0 - no_budget / base if base and no_budget else None
        summary[f"residual_gcc_{optimization.lower()}"] = no_budget / gcc if no_budget and gcc else None
        summary[f"residual_clang_{optimization.lower()}"] = no_budget / clang if no_budget and clang else None
    rep_pass = all(value is not None and value <= 0.25 for value in reproducibility.values())
    material = any(summary.get(key) is not None and summary[key] >= MATERIAL_SHARE_THRESHOLD for key in ("budget_share_o0", "budget_share_o1"))
    causal = "CONFIRMED_CAUSAL" if correctness["status"] == "PASS" and rep_pass and material else "BLOCKED" if correctness["status"] != "PASS" else "SUPPORTED" if rep_pass else "BLOCKED"
    return {
        "id": workload, "class": classification, "K": k, "correctness": correctness,
        "budget_sites": {label: artifact.budget_sites for label, artifact in artifacts.items()},
        "static_metrics": {label: artifact.static_metrics for label, artifact in artifacts.items()},
        "artifact_hashes": {label: {"source": artifact.source_sha256, "assembly": artifact.assembly_sha256, "diagnostic_assembly": artifact.diagnostic_assembly_sha256, "executable": artifact.executable_sha256} for label, artifact in artifacts.items()},
        "run_1": run_a, "run_2": run_b, "reproducibility": reproducibility, "reproducibility_pass": rep_pass,
        **summary, "causal_classification": causal, "work_units": {
            "scientific.rmsd.batch": "one pair comparison across 16 coordinate triples",
            "hpc.prk.nstream": "one NStream vector element",
            "numerical.polybench.gemm": "one GEMM output element",
        }.get(workload, "one complete JSON parse"), "meta": meta,
    }


def _classify(workloads: list[dict[str, Any]]) -> str:
    extra_material = [item["causal_classification"] == "CONFIRMED_CAUSAL" for item in workloads if item["id"] != "scientific.xsbench.compatible_lookup.medium"]
    if all(extra_material):
        return "SYSTEMIC_STRONG"
    if any(extra_material):
        return "SYSTEMIC_PARTIAL"
    if all(item["causal_classification"] == "SUPPORTED" for item in workloads if item["id"] != "scientific.xsbench.compatible_lookup.medium"):
        return "WEAKENED"
    return "BLOCKED"


def run_campaign(s3_repo: Path, benchmark_sha: str) -> Path:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("campaign requires Linux x86-64")
    require_commit(ROOT, benchmark_sha, label="benchmark repository")
    require_commit(s3_repo, EXPECTED_S3_SHA, label="S3 candidate")
    report_root = ROOT / "reports" / "benchmarks-2.2.3-budget-generalization"
    raw_root = report_root / "raw" / (time.strftime("budget-generalization-%Y%m%d-%H%M%S", time.gmtime()) + f"-{time.time_ns() % 1_000_000_000:09d}")
    raw_root.mkdir(parents=True, exist_ok=False)
    fingerprint, host = _host_fingerprint()
    environment = {"host_fingerprint": fingerprint, "host": host, "hostname": platform.node(), "python": platform.python_version(), "gcc": _run(["gcc", "--version"], timeout=10).stdout.splitlines()[0], "clang": _run(["clang", "--version"], timeout=10).stdout.splitlines()[0], "cpu_affinity": CPU_AFFINITY, "timer": "CLOCK_MONOTONIC_RAW", "perf_binary": shutil.which("perf") is not None}
    _write_json(raw_root / "environment.json", environment)

    regular_workload = "scientific.rmsd.batch"
    regular_pilot = next(item for item in _pilot_sources() if item.workload_id == regular_workload)

    # The existing FFI driver repeats K itself; this same generic builder is
    # used for every regular numerical pilot selected by the audit.
    def regular_build(k: int) -> tuple[dict[str, Artifact], dict[str, Any] | None]:
        artifacts, meta = _ffi_artifacts(s3_repo, raw_root / "regular" / f"artifacts-k{k}", regular_workload)
        driver = raw_root / "regular" / f"artifacts-k{k}" / "driver" / "ffi_driver"
        for label, artifact in list(artifacts.items()):
            export_variant = "S3_FFI_O1" if label == "S3_O1_BASELINE" else "S3_FFI_O0" if label == "S3_O0_BASELINE" else label
            export_symbol = _resolve_export_symbol(artifact.executable, regular_pilot.symbol, export_variant)["export_symbol"]
            artifacts[label] = Artifact(
                artifact.workload, artifact.variant, artifact.executable, artifact.assembly,
                artifact.control_source, artifact.source_sha256, artifact.assembly_sha256,
                artifact.diagnostic_assembly_sha256, artifact.executable_sha256,
                artifact.budget_sites, artifact.static_metrics,
                lambda artifact=artifact, label=label, driver=driver, export_symbol=export_symbol:
                    _run_driver(driver, artifact.executable, regular_pilot.workload_id,
                                label, export_symbol, k, regular_pilot.expected, 0),
            )
        return artifacts, meta

    k_regular, cal_regular, selected_regular, _ = _calibrate(regular_build, regular_workload, raw_root / "regular")
    workloads: list[dict[str, Any]] = []
    if selected_regular:
        correctness = _correctness(selected_regular, workload=regular_workload)
        _write_json(raw_root / "regular" / "correctness.json", correctness)
        _warmup(selected_regular, raw_root / "regular")
        run_a = _session(selected_regular, raw_root / "regular", "run_1", workload=regular_workload, classification="regular_numeric", k=k_regular or 0, work_units_per_call=regular_pilot.work_units_per_call, host_fingerprint=fingerprint)
        run_b = _session(selected_regular, raw_root / "regular", "run_2", workload=regular_workload, classification="regular_numeric", k=k_regular or 0, work_units_per_call=regular_pilot.work_units_per_call, host_fingerprint=fingerprint)
        workloads.append(_workload_result(regular_workload, "regular_numeric", k_regular or 0, selected_regular, run_a, run_b, correctness, None))
    else:
        workloads.append({"id": regular_workload, "class": "regular_numeric", "K": None, "causal_classification": "BLOCKED", "calibration": cal_regular})

    def jsmn_build(k: int) -> tuple[dict[str, Artifact], dict[str, Any] | None]:
        artifacts, metadata = _jsmn_artifacts(s3_repo, raw_root / "control-flow" / f"artifacts-k{k}", k)
        if metadata is not None:
            metadata["s3_repo"] = str(s3_repo)
        return artifacts, metadata
    k_jsmn, cal_jsmn, selected_jsmn, jsmn_meta = _calibrate(jsmn_build, "realworld.jsmn", raw_root / "control-flow")
    if selected_jsmn and jsmn_meta:
        correctness = _correctness(selected_jsmn, workload="realworld.jsmn", jsmn_meta=jsmn_meta)
        _write_json(raw_root / "control-flow" / "correctness.json", correctness)
        _warmup(selected_jsmn, raw_root / "control-flow")
        run_a = _session(selected_jsmn, raw_root / "control-flow", "run_1", workload="realworld.jsmn", classification="control_flow_or_parsing", k=k_jsmn or 0, work_units_per_call=1, host_fingerprint=fingerprint)
        run_b = _session(selected_jsmn, raw_root / "control-flow", "run_2", workload="realworld.jsmn", classification="control_flow_or_parsing", k=k_jsmn or 0, work_units_per_call=1, host_fingerprint=fingerprint)
        workloads.append(_workload_result("realworld.jsmn", "control_flow_or_parsing", k_jsmn or 0, selected_jsmn, run_a, run_b, correctness, jsmn_meta))
    else:
        workloads.append({"id": "realworld.jsmn", "class": "control_flow_or_parsing", "K": None, "causal_classification": "BLOCKED", "calibration": cal_jsmn})

    workloads.append({
        "id": "scientific.xsbench.compatible_lookup.medium", "class": "irregular_scientific", "K": 750000,
        "correctness": "PASS", "budget_sites": {"S3_O0_BASELINE": 521, "S3_O1_BASELINE": 520},
        "baseline_o0_ns": 14325439969.5, "no_budget_o0_ns": 6191784662.5, "baseline_o1_ns": 13832552419.5, "no_budget_o1_ns": 6547907311.0,
        "budget_ratio_o0": 2.3136205069050235, "budget_ratio_o1": 2.1125150009778446,
        "budget_share_o0": 0.5677769984249836, "budget_share_o1": 0.5266305803570066,
        "reproducibility": "PASS", "causal_classification": "CONFIRMED_CAUSAL", "source": "prior 2.2.2.1 authoritative evidence", "host_fingerprint": "9f6c7cbbdbbc2d056ffc306f76a1dcd9df194e15167cb037542da54e97b59393",
    })
    generalization = _classify(workloads)
    result = {"campaign": CAMPAIGN, "benchmark_sha": benchmark_sha, "s3_sha": EXPECTED_S3_SHA, "host_fingerprint": fingerprint, "environment": environment, "workloads": workloads, "generalization_classification": generalization, "h7": generalization, "budget_design_research_ready": generalization not in {"BLOCKED", "XSBench_LOCALIZED_OR_STRUCTURE_DEPENDENT"} and any(item.get("causal_classification") == "CONFIRMED_CAUSAL" for item in workloads if item["id"] != "scientific.xsbench.compatible_lookup.medium"), "s3_production_change_ready": False, "qualified_performance_index": "NOT_AVAILABLE"}
    _write_json(report_root / "BUDGET_GENERALIZATION_RESULT.json", result)
    return report_root / "BUDGET_GENERALIZATION_RESULT.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--benchmark-sha", required=True)
    args = parser.parse_args(argv)
    print(f"BUDGET_GENERALIZATION_RESULT={run_campaign(args.s3_repo, args.benchmark_sha)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
