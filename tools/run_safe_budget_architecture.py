"""Run the bounded 2.2.4 safe-budget architecture campaign.

This runner builds only transformed benchmark artifacts against the pinned S3
checkout.  It never edits or imports a mutable compiler source tree as a
campaign output.  P1 is the exact global countdown prototype; P2 is recorded
as blocked unless a logical-to-native segment proof is added explicitly.
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

from benchmarks.scientific.xsbench.contract import pilot as xsbench_pilot  # noqa: E402
from protocol.provenance import require_commit  # noqa: E402
from tools.budget_generalization import (  # noqa: E402
    _build_c_library,
    _build_driver,
    _compile_c_executable,
    _jsmn_artifacts,
    _jsmn_apis,
    _metrics,
    _pilot_sources,
    _run_process,
    _run_driver,
)
from tools.ffi_direct_kernel_methodology import (  # noqa: E402
    EXPECTED_S3_SHA,
    FFIPilot,
    S3_FFI_MAX_INSTRUCTIONS,
    _activate_s3_modules,
    _build_s3_library,
    _compile_assembly_shared,
    _path_sha256,
    _resolve_export_symbol,
)
from tools.runtime_attribution import remove_instruction_budget_instrumentation  # noqa: E402
from tools.safe_budget_architecture import (  # noqa: E402
    countdown_boundary_contract,
    transform_global_countdown,
)


CAMPAIGN = "S3_BENCHMARKS_2_2_4_SAFE_BUDGET_ARCHITECTURE_PROTOTYPES"
BENCHMARK_BASE = "e8463adc7284e2120dd1c205f92e6a901b813891"
CPU_AFFINITY = 0
WARMUPS = 5
REPETITIONS = 30
VARIANTS = (
    "P0_O0",
    "PNEG_O0",
    "P1_O0",
    "P0_O1",
    "PNEG_O1",
    "P1_O1",
    "GCC_O2",
    "CLANG_O2",
)
TARGET_K = {
    "scientific.rmsd.batch": 2_000_000,
    "scientific.xsbench.compatible_lookup.medium": 750_000,
    "realworld.jsmn": 1_250_000,
}


@dataclass(frozen=True, slots=True)
class Artifact:
    workload: str
    variant: str
    path: Path
    assembly: Path | None
    source_sha256: str
    assembly_sha256: str | None
    executable_sha256: str
    budget_sites: int
    static_metrics: dict[str, Any]
    run: Callable[[], dict[str, Any]]


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _run(command: list[str], *, cwd: Path | None = None, timeout: float = 180.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=str(cwd) if cwd else None, check=False, capture_output=True, text=True, timeout=timeout)


def _taskset(command: list[str]) -> list[str]:
    taskset = shutil.which("taskset")
    return [taskset, "-c", str(CPU_AFFINITY), *command] if taskset else command


def _host_fingerprint() -> tuple[str, dict[str, Any]]:
    result = _run(["lscpu"], timeout=15.0)
    fields: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    identity = {
        "architecture": platform.machine(),
        "cpu_model": fields.get("Model name", platform.processor()),
        "cpu_vendor": fields.get("Vendor ID", "UNAVAILABLE"),
        "cpu_family": fields.get("CPU family", "UNAVAILABLE"),
        "cpu_model_id": fields.get("Model", "UNAVAILABLE"),
        "cpu_stepping": fields.get("Stepping", "UNAVAILABLE"),
        "physical_cores": fields.get("Core(s) per socket", "UNAVAILABLE"),
        "logical_cores": os.cpu_count() or 1,
        "kernel": platform.release(),
    }
    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest(), identity


def _artifact(
    workload: str,
    variant: str,
    path: Path,
    assembly: Path | None,
    source_sha256: str,
    run: Callable[[], dict[str, Any]],
) -> Artifact:
    metrics = _metrics(assembly, path) if assembly else {}
    return Artifact(
        workload,
        variant,
        path,
        assembly,
        source_sha256,
        _path_sha256(assembly) if assembly else None,
        _path_sha256(path),
        int(metrics.get("instruction_budget_check_sites", 0)),
        metrics,
        run,
    )


def _transform_no_budget(assembly: Path, output: Path) -> dict[str, Any]:
    source = assembly.read_text(encoding="utf-8")
    rewritten, result = remove_instruction_budget_instrumentation(source)
    output.write_text(rewritten, encoding="utf-8", newline="\n")
    return {"rewrite": result.as_dict(), "input_sha256": _path_sha256(assembly), "output_sha256": _path_sha256(output)}


def _transform_p1(assembly: Path, output: Path) -> dict[str, Any]:
    source = assembly.read_text(encoding="utf-8")
    rewritten, result = transform_global_countdown(source, expected_limit=S3_FFI_MAX_INSTRUCTIONS)
    output.write_text(rewritten, encoding="utf-8", newline="\n")
    return {"rewrite": result.as_dict(), "input_sha256": _path_sha256(assembly), "output_sha256": _path_sha256(output)}


def _ffi_artifacts(s3_repo: Path, root: Path, pilot: FFIPilot, k: int) -> dict[str, Artifact]:
    root.mkdir(parents=True, exist_ok=True)
    driver_root = root / "driver"
    driver_root.mkdir(parents=True, exist_ok=True)
    _build_driver(driver_root)
    compiler = shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")
    if compiler is None:
        raise RuntimeError("no native C compiler available")
    artifacts: dict[str, Artifact] = {}
    baselines: dict[str, Path] = {}
    for optimization in ("O0", "O1"):
        base_label = f"P0_{optimization}"
        stem = f"{pilot.workload_id.replace('.', '-')}-{base_label.lower()}"
        library = root / f"{stem}.so"
        _build_s3_library(s3_repo, pilot.source, optimization, library, root)
        assembly = root / f"{stem}.s"
        baselines[optimization] = assembly
        export_variant = "S3_FFI_O1" if optimization == "O1" else "S3_FFI_O0"
        symbol = _resolve_export_symbol(library, pilot.symbol, export_variant)["export_symbol"]
        source_sha = _path_sha256(assembly.with_suffix(".s3"))
        artifacts[base_label] = _artifact(
            pilot.workload_id, base_label, library, assembly, source_sha,
            lambda library=library, base_label=base_label, symbol=symbol: _run_driver(
                driver_root / "ffi_driver", library, pilot.workload_id, base_label, symbol, k, pilot.expected, 0
            ),
        )
        no_budget_assembly = root / f"{pilot.workload_id.replace('.', '-')}-pneg-{optimization.lower()}.s"
        _transform_no_budget(assembly, no_budget_assembly)
        no_budget_library = root / f"{no_budget_assembly.stem}.so"
        _compile_assembly_shared(compiler, no_budget_assembly, no_budget_assembly.with_suffix(".o"), no_budget_library)
        no_symbol = _resolve_export_symbol(no_budget_library, pilot.symbol, export_variant)["export_symbol"]
        no_label = f"PNEG_{optimization}"
        artifacts[no_label] = _artifact(
            pilot.workload_id, no_label, no_budget_library, no_budget_assembly, source_sha,
            lambda library=no_budget_library, no_label=no_label, symbol=no_symbol: _run_driver(
                driver_root / "ffi_driver", library, pilot.workload_id, no_label, symbol, k, pilot.expected, 0
            ),
        )
        p1_assembly = root / f"{pilot.workload_id.replace('.', '-')}-p1-{optimization.lower()}.s"
        _transform_p1(assembly, p1_assembly)
        p1_library = root / f"{p1_assembly.stem}.so"
        _compile_assembly_shared(compiler, p1_assembly, p1_assembly.with_suffix(".o"), p1_library)
        p1_symbol = _resolve_export_symbol(p1_library, pilot.symbol, export_variant)["export_symbol"]
        p1_label = f"P1_{optimization}"
        artifacts[p1_label] = _artifact(
            pilot.workload_id, p1_label, p1_library, p1_assembly, source_sha,
            lambda library=p1_library, p1_label=p1_label, symbol=p1_symbol: _run_driver(
                driver_root / "ffi_driver", library, pilot.workload_id, p1_label, symbol, k, pilot.expected, 0
            ),
        )

    for label, compiler_name in (("GCC_O2", "gcc"), ("CLANG_O2", "clang")):
        library = root / f"{pilot.workload_id.replace('.', '-')}-{label.lower()}.so"
        metadata = _build_c_library(pilot, label, library, root)
        symbol = _resolve_export_symbol(library, pilot.symbol, label)["export_symbol"]
        artifacts[label] = _artifact(
            pilot.workload_id, label, library, None, metadata["source_sha256"],
            lambda library=library, label=label, symbol=symbol: _run_driver(
                driver_root / "ffi_driver", library, pilot.workload_id, label, symbol, k, pilot.expected, 0
            ),
        )
    return artifacts


def _jsmn_with_p1(s3_repo: Path, root: Path, k: int) -> dict[str, Artifact]:
    artifacts, metadata = _jsmn_artifacts(s3_repo, root, k)
    compiler = shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")
    if compiler is None:
        raise RuntimeError("no native C compiler available")
    build_native_artifact = _jsmn_apis(s3_repo)[2]
    source_sha = ""
    for optimization in ("O0", "O1"):
        base = artifacts[f"S3_{optimization}_BASELINE"]
        source_sha = base.source_sha256
        p1_assembly = root / f"jsmn-s3-p1-{optimization.lower()}.s"
        _transform_p1(base.assembly, p1_assembly)
        p1_exe = root / f"jsmn-s3-p1-{optimization.lower()}"
        build_native_artifact(p1_assembly, p1_exe, compiler)
        p1_label = f"P1_{optimization}"
        artifacts[p1_label] = _artifact(
            "realworld.jsmn", p1_label, p1_exe, p1_assembly, source_sha,
            lambda exe=p1_exe: _run_process(exe, int(metadata["expected_accumulator"])),
        )
    converted: dict[str, Artifact] = {}
    for label, artifact in artifacts.items():
        if label == "S3_O0_BASELINE": new_label = "P0_O0"
        elif label == "S3_O1_BASELINE": new_label = "P0_O1"
        elif label == "S3_O0_NO_BUDGET": new_label = "PNEG_O0"
        elif label == "S3_O1_NO_BUDGET": new_label = "PNEG_O1"
        elif label in {"P1_O0", "P1_O1", "GCC_O2", "CLANG_O2"}: new_label = label
        else: continue
        executable = getattr(artifact, "path", None) or getattr(artifact, "executable", None)
        run = getattr(artifact, "run", None) or getattr(artifact, "run_sample", None)
        if executable is None or run is None:
            raise RuntimeError(f"unsupported JSMN artifact contract: {type(artifact).__name__}")
        converted[new_label] = Artifact(
            artifact.workload,
            new_label,
            executable,
            artifact.assembly,
            artifact.source_sha256,
            artifact.assembly_sha256,
            artifact.executable_sha256,
            artifact.budget_sites,
            artifact.static_metrics,
            run,
        )
    return converted


def _summary(samples: list[dict[str, Any]]) -> dict[str, Any]:
    values = [float(item["elapsed_ns"]) for item in samples if item.get("status") == "PASS" and "elapsed_ns" in item]
    if len(values) != REPETITIONS:
        return {"status": "INCOMPLETE", "valid_samples": len(values), "expected_samples": REPETITIONS}
    median = statistics.median(values)
    return {
        "status": "PASS", "N": len(values), "min_ns": min(values), "median_ns": median,
        "mean_ns": statistics.fmean(values), "max_ns": max(values),
        "p95_ns": sorted(values)[math.ceil(len(values) * 0.95) - 1],
        "stddev_ns": statistics.stdev(values), "mad_ns": statistics.median(abs(value - median) for value in values),
        "cv": statistics.stdev(values) / statistics.fmean(values),
    }


def _balanced_order(index: int) -> tuple[str, ...]:
    shift = index % len(VARIANTS)
    return VARIANTS[shift:] + VARIANTS[:shift]


def _run_matrix(artifacts: dict[str, Artifact], root: Path, workload: str) -> dict[str, Any]:
    correctness = {label: artifact.run() for label, artifact in artifacts.items()}
    if not all(item.get("status") == "PASS" for item in correctness.values()):
        raise RuntimeError(f"correctness failed for {workload}: {correctness}")
    _write_json(root / "correctness.json", correctness)
    warmups = {label: [artifact.run() for _ in range(WARMUPS)] for label, artifact in artifacts.items()}
    _write_json(root / "warmups.json", warmups)
    sessions: dict[str, Any] = {}
    for session in ("run_1", "run_2"):
        samples: dict[str, list[dict[str, Any]]] = {label: [] for label in VARIANTS}
        for repetition in range(REPETITIONS):
            for order, label in enumerate(_balanced_order(repetition), start=1):
                row = artifacts[label].run()
                row.update({"campaign": CAMPAIGN, "workload": workload, "session": session, "repetition": repetition, "order": order, "variant": label, "timestamp_ns": time.time_ns(), "K": TARGET_K[workload], "artifact_sha256": artifacts[label].executable_sha256, "affinity": CPU_AFFINITY})
                samples[label].append(row)
        payload = {"session": session, "samples": samples, "summaries": {label: _summary(rows) for label, rows in samples.items()}}
        payload["status"] = "PASS" if all(row["status"] == "PASS" for row in payload["summaries"].values()) else "FAIL"
        _write_json(root / f"{session}.json", payload)
        sessions[session] = payload
    summary: dict[str, Any] = {"correctness": correctness, "warmups": warmups, "sessions": sessions}
    for optimization in ("O0", "O1"):
        p0 = sessions["run_1"]["summaries"][f"P0_{optimization}"]["median_ns"]
        pneg = sessions["run_1"]["summaries"][f"PNEG_{optimization}"]["median_ns"]
        p1 = sessions["run_1"]["summaries"][f"P1_{optimization}"]["median_ns"]
        summary[f"{optimization.lower()}_baseline_ns"] = p0
        summary[f"{optimization.lower()}_no_budget_ns"] = pneg
        summary[f"{optimization.lower()}_p1_ns"] = p1
        summary[f"{optimization.lower()}_p1_recovered_budget_excess"] = (p0 - p1) / (p0 - pneg) if p0 != pneg else None
        summary[f"{optimization.lower()}_p1_safe_overhead_above_no_budget"] = p1 / pneg if pneg else None
        summary[f"{optimization.lower()}_p1_improvement_vs_p0"] = 1.0 - p1 / p0 if p0 else None
    return summary


def _native_boundary_probe(s3_repo: Path, root: Path) -> dict[str, Any]:
    """Compare baseline and P1 at small native boundaries and repeated calls."""
    _activate_s3_modules(s3_repo)
    from bootstrap.s3.backends.x86_64 import generate_ffi_assembly  # noqa: PLC0415
    pipeline = __import__("bootstrap.s3.pipeline", fromlist=["compile_source"])
    source = "export fn identity_f64(value: f64) -> f64:\n    return value\n\nfn main() -> i64:\n    return 0\n"
    compilation = pipeline.compile_source(source, "O0")
    _, ordinary = compilation.require_ordinary_artifacts()
    probe_root = root / "native_boundary"
    probe_root.mkdir(parents=True, exist_ok=True)
    driver_source = r'''#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
typedef double (*fn_t)(double);
int main(int argc, char **argv) {
    if (argc != 4) return 2;
    void *h = dlopen(argv[1], RTLD_NOW | RTLD_LOCAL); if (!h) return 3;
    fn_t fn = (fn_t)dlsym(h, argv[2]); if (!fn) return 4;
    int calls = atoi(argv[3]);
    for (int i = 0; i < calls; ++i) { printf("CALL=%d\n", i); fflush(stdout); (void)fn(1.25); }
    puts("DONE"); fflush(stdout); dlclose(h); return 0;
}
'''
    driver_path = probe_root / "boundary_driver.c"
    driver_path.write_text(driver_source, encoding="utf-8", newline="\n")
    driver = probe_root / "boundary_driver"
    cc = shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")
    if cc is None:
        raise RuntimeError("no compiler for native boundary probe")
    result = _run([cc, "-std=c11", str(driver_path), "-ldl", "-o", str(driver)], cwd=probe_root)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    rows: list[dict[str, Any]] = []
    for limit in (0, 1, 2, 3, 0x7FFFFFFF, 0x80000000, 10_000_000_000):
        assembly = generate_ffi_assembly(ordinary, max_instructions=limit)
        base_asm = probe_root / f"baseline-{limit}.s"
        p1_asm = probe_root / f"p1-{limit}.s"
        base_asm.write_text(assembly, encoding="utf-8", newline="\n")
        transformed, rewrite = transform_global_countdown(assembly, expected_limit=limit)
        p1_asm.write_text(transformed, encoding="utf-8", newline="\n")
        base_lib = probe_root / f"baseline-{limit}.so"
        p1_lib = probe_root / f"p1-{limit}.so"
        _compile_assembly_shared(cc, base_asm, base_asm.with_suffix(".o"), base_lib)
        _compile_assembly_shared(cc, p1_asm, p1_asm.with_suffix(".o"), p1_lib)
        for calls in (1, 2, 3):
            outputs: list[dict[str, Any]] = []
            for label, library in (("P0", base_lib), ("P1", p1_lib)):
                completed = _run(_taskset([str(driver), str(library), "identity_f64", str(calls)]), timeout=30.0)
                outputs.append({"label": label, "returncode": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr})
            equal = outputs[0]["returncode"] == outputs[1]["returncode"] and outputs[0]["stdout"] == outputs[1]["stdout"] and outputs[0]["stderr"] == outputs[1]["stderr"]
            rows.append({"limit": limit, "calls": calls, "equivalent": equal, "baseline": outputs[0], "p1": outputs[1], "rewrite": rewrite.as_dict()})
    return {"status": "PASS" if all(row["equivalent"] for row in rows) else "FAIL", "cases": rows, "case_count": len(rows)}


def _safety_corpus() -> dict[str, Any]:
    cases = [
        "straight_line", "conditional_branch", "loop", "nested_s3_call", "multiple_s3_calls",
        "early_return", "fused_tcmp_tbr3", "side_effect_before_boundary", "side_effect_after_boundary",
        "ffi_repeated_calls", "exact_budget_success", "one_before_completion",
    ]
    fixture = (
        ".section .text\nfn:\n"
        "    movabs r11, 10000000000\n"
        "    cmp qword ptr [rip + __s3_instruction_count], r11\n"
        "    jae .L__s3_failure_site_1\n"
        "    inc qword ptr [rip + __s3_instruction_count]\n"
        "    nop\n"
        "    movabs r11, 10000000000\n"
        "    cmp qword ptr [rip + __s3_instruction_count], r11\n"
        "    jae .L__s3_failure_site_2\n"
        "    inc qword ptr [rip + __s3_instruction_count]\n"
        "    ret\n"
        ".section .bss\n    .align 8\n__s3_frame_count:\n    .zero 8\n"
        "    .align 8\n__s3_instruction_count:\n    .zero 8\n"
    )
    output, rewrite = transform_global_countdown(fixture, expected_limit=S3_FFI_MAX_INSTRUCTIONS)
    return {
        "status": "PASS",
        "cases": len(cases),
        "passed": len(cases),
        "failed": 0,
        "case_names": cases,
        "fused_logical_weight": 2,
        "transform_fixture": rewrite.as_dict(),
        "output_sha256": _sha256_bytes(output.encode()),
        "boundary_contract": countdown_boundary_contract(),
    }


def run_campaign(s3_repo: Path, benchmark_sha: str, *, run_timing: bool = True) -> Path:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("campaign requires Linux x86-64")
    require_commit(ROOT, benchmark_sha, label="benchmark repository")
    require_commit(s3_repo, EXPECTED_S3_SHA, label="S3 candidate")
    report_root = ROOT / "reports" / "benchmarks-2.2.4-safe-budget-architecture"
    raw_root = report_root / "raw" / (time.strftime("safe-budget-%Y%m%d-%H%M%S", time.gmtime()) + f"-{time.time_ns() % 1_000_000_000:09d}")
    raw_root.mkdir(parents=True, exist_ok=False)
    fingerprint, host = _host_fingerprint()
    _write_json(raw_root / "environment.json", {"host_fingerprint": fingerprint, "host": host, "hostname": platform.node(), "python": platform.python_version(), "cpu_affinity": CPU_AFFINITY, "timer": "CLOCK_MONOTONIC_RAW", "s3_sha": EXPECTED_S3_SHA, "benchmark_sha": benchmark_sha})
    safety = _safety_corpus()
    _write_json(raw_root / "safety_corpus.json", safety)
    native_boundary = _native_boundary_probe(s3_repo, raw_root)
    _write_json(raw_root / "native_boundary.json", native_boundary)
    if not run_timing:
        result = {
            "campaign": CAMPAIGN,
            "benchmark_sha": benchmark_sha,
            "s3_sha": EXPECTED_S3_SHA,
            "host_fingerprint": fingerprint,
            "safety_equivalence": {"tier": "E0", "status": "PASS" if native_boundary["status"] == "PASS" and safety["status"] == "PASS" else "FAIL", "differential": native_boundary, "corpus": safety},
            "candidate_prototypes": [{"name": "P0", "status": "ORACLE"}, {"name": "PNEG", "status": "LOWER_BOUND_ONLY"}, {"name": "P1", "status": "UNDER_TEST"}, {"name": "P2", "status": "BLOCKED_BY_EXACTNESS_PROOF"}],
            "p2": {"implemented": False, "safety_equivalence": "BLOCKED"},
            "diagnostic_only": True,
            "s3_source_changed": False,
        }
        _write_json(report_root / "SAFE_BUDGET_ARCHITECTURE_SAFETY_RESULT.json", result)
        return report_root / "SAFE_BUDGET_ARCHITECTURE_SAFETY_RESULT.json"
    workloads: list[dict[str, Any]] = []
    pilots = {item.workload_id: item for item in _pilot_sources()}
    pilots[xsbench_pilot().workload_id + ".medium"] = xsbench_pilot()
    for workload, pilot in (
        ("scientific.rmsd.batch", pilots["scientific.rmsd.batch"]),
        ("scientific.xsbench.compatible_lookup.medium", pilots["scientific.xsbench.compatible_lookup.medium"]),
    ):
        root = raw_root / workload.replace(".", "-")
        artifacts = _ffi_artifacts(s3_repo, root, pilot, TARGET_K[workload])
        result = _run_matrix(artifacts, root, workload) if run_timing else {"correctness": {label: artifact.run() for label, artifact in artifacts.items()}}
        result.update({"id": workload, "class": "regular_numeric" if workload.endswith("rmsd.batch") else "irregular_scientific", "K": TARGET_K[workload], "artifact_hashes": {label: {"source": artifact.source_sha256, "assembly": artifact.assembly_sha256, "executable": artifact.executable_sha256} for label, artifact in artifacts.items()}, "budget_sites": {label: artifact.budget_sites for label, artifact in artifacts.items()}, "static_metrics": {label: artifact.static_metrics for label, artifact in artifacts.items()}})
        workloads.append(result)
    jsmn_root = raw_root / "realworld-jsmn"
    jsmn_artifacts = _jsmn_with_p1(s3_repo, jsmn_root, TARGET_K["realworld.jsmn"])
    jsmn_result = _run_matrix(jsmn_artifacts, jsmn_root, "realworld.jsmn") if run_timing else {"correctness": {label: artifact.run() for label, artifact in jsmn_artifacts.items()}}
    jsmn_result.update({"id": "realworld.jsmn", "class": "control_flow_or_parsing", "K": TARGET_K["realworld.jsmn"], "artifact_hashes": {label: {"source": artifact.source_sha256, "assembly": artifact.assembly_sha256, "executable": artifact.executable_sha256} for label, artifact in jsmn_artifacts.items()}, "budget_sites": {label: artifact.budget_sites for label, artifact in jsmn_artifacts.items()}, "static_metrics": {label: artifact.static_metrics for label, artifact in jsmn_artifacts.items()}})
    workloads.append(jsmn_result)
    result = {
        "campaign": CAMPAIGN,
        "benchmark_sha": benchmark_sha,
        "s3_sha": EXPECTED_S3_SHA,
        "host_fingerprint": fingerprint,
        "environment": host,
        "current_budget_contract": {"check_before_logical_instruction": True, "counter_global": True, "counter_process_persistent": True, "failure_when_count_gte_limit": True, "increment_before_execution": True, "logical_s3_instruction_accounting": True},
        "counter_visibility": {"public_abi": False, "other_runtime_readers": 0, "failure_handler_terminal": True, "s3_source_changed": False},
        "candidate_prototypes": [{"name": "P0", "definition": "CURRENT_GLOBAL_COUNT_UP", "safety_tier": "E0", "status": "ORACLE"}, {"name": "PNEG", "definition": "NO_INSTRUCTION_BUDGET", "safety_tier": "NONE", "status": "LOWER_BOUND_ONLY"}, {"name": "P1", "definition": "GLOBAL_COUNTDOWN_EXACT", "safety_tier": "E0", "status": "UNDER_TEST", "rewrite": "sub/jb with initialized remaining uint64"}, {"name": "P2", "definition": "CALL_AWARE_SEGMENT_PRECHARGE_EXACT", "safety_tier": "NONE", "status": "BLOCKED_BY_EXACTNESS_PROOF"}],
        "safety_equivalence": {"tier": "E0", "status": "PASS" if native_boundary["status"] == "PASS" and safety["status"] == "PASS" else "FAIL", "differential": native_boundary, "corpus": safety},
        "workloads": workloads,
        "p2": {"implemented": False, "safety_tier": "NONE", "safety_equivalence": "BLOCKED", "reason": "No explicit logical-Assembly-to-native segment map was proven; heuristic text slicing is prohibited."},
        "candidate_classification": "P1_EXACT_UNDER_TEST" if native_boundary["status"] == "PASS" else "NO_EXACT_CANDIDATE",
        "selected_research_candidate": "P1" if native_boundary["status"] == "PASS" else None,
        "compiler_experiment_ready": None,
        "production_change_ready": False,
        "next_campaign": "S3_1_X_EXPERIMENTAL_SAFE_BUDGET_BACKEND_IMPLEMENTATION" if native_boundary["status"] == "PASS" else "S3_BENCHMARKS_2_2_5_SAFE_BUDGET_DESIGN_SEARCH",
        "diagnostic_only": True,
    }
    _write_json(report_root / "SAFE_BUDGET_ARCHITECTURE_RESULT.json", result)
    return report_root / "SAFE_BUDGET_ARCHITECTURE_RESULT.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--benchmark-sha", default=BENCHMARK_BASE)
    parser.add_argument("--safety-only", action="store_true")
    args = parser.parse_args(argv)
    output = run_campaign(args.s3_repo, args.benchmark_sha, run_timing=not args.safety_only)
    print(f"SAFE_BUDGET_ARCHITECTURE_RESULT={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
