"""Controlled native PROCESS_E2E measurement for the 2.1 baseline.

This driver deliberately keeps the candidate-activation adapter as the source
of workload truth and the existing protocol/artifact/statistics modules as the
measurement substrate.  Correctness and measurement executables are built and
run in separate phases.  The timed executable performs one useful workload
and emits one post-work canary; therefore this first campaign reports
PROCESS_E2E only and never presents it as kernel time.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import time
from typing import Any

try:
    import resource
except ModuleNotFoundError:  # pragma: no cover - Linux measurement host provides it.
    resource = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmarks.candidate_activation.adapters import native_canary_source, run_hosted  # noqa: E402
from benchmarks.candidate_activation.workloads import WorkloadCase, performance_cases  # noqa: E402
from protocol.measurement import MeasurementProtocol, interleave  # noqa: E402
from protocol.provenance import require_commit, sha256_file  # noqa: E402
from protocol.result import BenchmarkResult  # noqa: E402
from protocol.workload import canonical_json  # noqa: E402
from tools.artifacts import RunIdentity, file_record, require_provenance  # noqa: E402
from tools.assembly_analyzer import analyze_assembly_text  # noqa: E402


EXPECTED_S3_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"
DEFAULT_WARMUPS = 5
DEFAULT_REPETITIONS = 30
NATIVE_MAX_INSTRUCTIONS = 1 << 62
CANARY_OUTPUT = re.compile(r"program returned:\s*(-?\d+)")


@dataclass(frozen=True, slots=True)
class BuiltVariant:
    variant: str
    optimization: str
    source_path: Path
    assembly_path: Path
    executable_path: Path
    assembly: str
    metrics: dict[str, Any]


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


def _read_first(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8").strip()
    except OSError:
        return "UNAVAILABLE"


def _lscpu() -> dict[str, str]:
    output = _run_text(["lscpu"]) or ""
    result: dict[str, str] = {}
    for line in output.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def collect_environment(s3_repo: Path, benchmark_sha: str) -> dict[str, Any]:
    cpu = _lscpu()
    logical = os.cpu_count() or 1
    affinity = sorted(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None
    meminfo = _read_first("/proc/meminfo")
    ram = next((line.split(":", 1)[1].strip() for line in meminfo.splitlines() if line.startswith("MemTotal:")), "UNAVAILABLE")
    governor = sorted(Path("/sys/devices/system/cpu").glob("cpu*/cpufreq/scaling_governor"))
    governor_values = sorted({_read_first(str(path)) for path in governor}) or ["UNAVAILABLE"]
    turbo = _read_first("/sys/devices/system/cpu/intel_pstate/no_turbo")
    if turbo == "0":
        turbo_state = "ENABLED_OR_UNCONTROLLED"
    elif turbo == "1":
        turbo_state = "DISABLED"
    else:
        turbo_state = "UNAVAILABLE"
    smt = _read_first("/sys/devices/system/cpu/smt/active")
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
        "distribution": _read_first("/etc/os-release"),
        "cache_l1d": cpu.get("L1d cache", "UNAVAILABLE"),
        "cache_l1i": cpu.get("L1i cache", "UNAVAILABLE"),
        "cache_l2": cpu.get("L2 cache", "UNAVAILABLE"),
        "cache_l3": cpu.get("L3 cache", "UNAVAILABLE"),
        "numa": cpu.get("NUMA node(s)", "UNAVAILABLE"),
    }
    fingerprint = hashlib.sha256(canonical_json(stable).encode("utf-8")).hexdigest()
    load = os.getloadavg() if hasattr(os, "getloadavg") else None
    noisy = bool(load and load[0] > logical)
    environment = {
        **stable,
        "machine_fingerprint_sha256": fingerprint,
        "hostname": platform.node(),
        "os": platform.system(),
        "os_release": platform.release(),
        "python_version": platform.python_version(),
        "benchmark_repo_sha": benchmark_sha,
        "s3_sha": require_commit(s3_repo, EXPECTED_S3_SHA, label="S3 candidate"),
        "gcc_version": _tool_version("gcc"),
        "clang_version": _tool_version("clang"),
        "as_version": _tool_version("as"),
        "ld_version": _tool_version("ld"),
        "perf_version": _tool_version("perf"),
        "hyperfine_version": _tool_version("hyperfine"),
        "cpu_affinity": affinity,
        "smt_status": smt if smt != "UNAVAILABLE" else "UNAVAILABLE",
        "cpu_governor": governor_values,
        "turbo_state": turbo_state,
        "load_average_before": load,
        "environment_noisy": noisy,
    }
    return environment


def _parse_canary(stdout: str) -> int:
    match = CANARY_OUTPUT.search(stdout)
    if match is None:
        raise RuntimeError(f"native executable did not emit a canary: {stdout!r}")
    return int(match.group(1))


def _build_variant(case: WorkloadCase, optimization: str, variant: str, root: Path, toolchain: Any) -> BuiltVariant:
    from bootstrap.s3.backends.x86_64 import X8664Backend
    from bootstrap.s3.pipeline import compile_source

    fixture_id = f"{case.workload_id}__{case.size}".replace("/", "_")
    variant_root = root / "fixtures" / fixture_id / variant.lower()
    variant_root.mkdir(parents=True, exist_ok=False)
    source = native_canary_source(case)
    source_path = variant_root / "measurement.s3"
    assembly_path = variant_root / "program.s"
    executable_path = variant_root / "program"
    source_path.write_text(source, encoding="utf-8", newline="\n")
    compile_start = time.perf_counter_ns()
    assembly_program = compile_source(source, optimization=optimization).assembly
    assembly = X8664Backend(
        register_allocation=True,
        max_instructions=NATIVE_MAX_INSTRUCTIONS,
    ).generate(assembly_program)
    toolchain.build(assembly, executable_path, keep_assembly=assembly_path)
    compile_wall_ns = time.perf_counter_ns() - compile_start
    metrics = analyze_assembly_text(assembly, variant, executable_path).__dict__
    metrics.update({
        "compile_wall_ns": compile_wall_ns,
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "source_bytes": len(source.encode("utf-8")),
        "assembly_sha256": hashlib.sha256(assembly.encode("utf-8")).hexdigest(),
        "executable_sha256": sha256_file(executable_path),
    })
    return BuiltVariant(variant, optimization, source_path, assembly_path, executable_path, assembly, metrics)


def _run_once(executable: Path) -> tuple[int, int, dict[str, int]]:
    before = resource.getrusage(resource.RUSAGE_CHILDREN) if resource is not None else None
    start = time.perf_counter_ns()
    completed = subprocess.run([os.fspath(executable)], check=False, capture_output=True, text=True, timeout=30.0)
    elapsed = time.perf_counter_ns() - start
    after = resource.getrusage(resource.RUSAGE_CHILDREN) if resource is not None else None
    if completed.returncode != 0:
        raise RuntimeError(f"native execution failed ({completed.returncode}): {completed.stderr.strip()}")
    if _parse_canary(completed.stdout) != 1:
        raise RuntimeError(f"native correctness canary failed: {completed.stdout!r}")
    if before is None or after is None:
        return elapsed, completed.returncode, {
            "user_cpu_ns": 0,
            "system_cpu_ns": 0,
            "peak_rss_bytes": 0,
            "minor_faults": 0,
            "major_faults": 0,
        }
    return elapsed, completed.returncode, {
        "user_cpu_ns": int(max(0.0, after.ru_utime - before.ru_utime) * 1_000_000_000),
        "system_cpu_ns": int(max(0.0, after.ru_stime - before.ru_stime) * 1_000_000_000),
        "peak_rss_bytes": int(after.ru_maxrss) * 1024,
        "minor_faults": int(max(0, after.ru_minflt - before.ru_minflt)),
        "major_faults": int(max(0, after.ru_majflt - before.ru_majflt)),
    }


def _correctness_gate(case: WorkloadCase, toolchain: Any, s3_root: Path) -> dict[str, Any]:
    observed_o0 = run_hosted(case, optimization="O0")
    observed_o1 = run_hosted(case, optimization="O1")
    if abs(float(observed_o0) - float(case.expected)) > 1e-12 or abs(float(observed_o1) - float(case.expected)) > 1e-12:
        raise RuntimeError(f"hosted oracle mismatch: expected={case.expected} O0={observed_o0} O1={observed_o1}")
    temp = s3_root / ".correctness" / f"{case.workload_id.replace('.', '_')}__{case.size}"
    temp.mkdir(parents=True, exist_ok=False)
    values: dict[str, int] = {}
    for optimization in ("O0", "O1"):
        built = _build_variant(case, optimization, f"correctness-{optimization}", temp, toolchain)
        _elapsed, _returncode, _resources = _run_once(built.executable_path)
        values[optimization] = 1
    return {"status": "PASS", "hosted_o0": observed_o0, "hosted_o1": observed_o1, "native_canary": values}


def _work_units(case: WorkloadCase) -> int:
    if case.workload_id == "scientific.rmsd.single":
        return 31 if case.size == "medium" else 7
    if case.workload_id == "scientific.rmsd.batch":
        pairs = 16 if case.size == "medium" else 3
        return pairs * 3
    if case.workload_id == "scientific.rmsd.matrix":
        dimension = 4 if case.size == "medium" else 3
        return dimension * dimension * 3
    if case.workload_id in {"hpc.prk.nstream", *{f"memory.babelstream.{name}" for name in ("copy", "scale", "add", "triad", "dot")}}:
        return 31 if case.size == "medium" else 7
    if case.workload_id == "hpc.prk.transpose":
        return 12 * 16 if case.size == "medium" else 3 * 4
    if case.workload_id == "numerical.polybench.jacobi_1d":
        return 18 if case.size == "medium" else 5
    if case.workload_id in {"numerical.polybench.gemm", "language.plb2.matmul"}:
        rows, cols, inner = (12, 16, 8) if case.size == "medium" else (3, 4, 2)
        return rows * cols * inner
    if case.workload_id == "numerical.polybench.2mm":
        rows, cols, inner = (12, 16, 8) if case.size == "medium" else (3, 4, 2)
        return 2 * rows * cols * inner
    if case.workload_id in {"numerical.polybench.atax", "numerical.polybench.mvt"}:
        rows, cols = (12, 16) if case.size == "medium" else (3, 4)
        return rows * cols
    raise ValueError(f"no work-unit contract for {case.workload_id}")


def _measure_variant(built: BuiltVariant, protocol: MeasurementProtocol) -> dict[str, Any]:
    for _ in range(protocol.warmups):
        _run_once(built.executable_path)
    samples: list[int] = []
    resources: list[dict[str, int]] = []
    for _variant in interleave((built.variant,), protocol.repetitions):
        elapsed, _returncode, resource_metrics = _run_once(built.executable_path)
        samples.append(elapsed)
        resources.append(resource_metrics)
    return {
        "samples": samples,
        "resource_samples": resources,
        "maximum_peak_rss_bytes": max((item["peak_rss_bytes"] for item in resources), default=0),
    }


def _perf_probe() -> dict[str, str]:
    perf = shutil.which("perf")
    if perf is None:
        return {"available": "NO", "permission": "NOT_INSTALLED"}
    completed = subprocess.run([perf, "stat", "-e", "cycles", "true"], check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        return {"available": "NO", "permission": "DENIED_OR_UNAVAILABLE"}
    return {"available": "YES", "permission": "AVAILABLE_BUT_NOT_COLLECTED_PER_SAMPLE"}


def _serialize_measurement(case: WorkloadCase, built: BuiltVariant, correctness: dict[str, Any], timed: dict[str, Any], environment: dict[str, Any], benchmark_sha: str, s3_sha: str) -> dict[str, Any]:
    protocol = MeasurementProtocol(
        warmups=DEFAULT_WARMUPS,
        repetitions=DEFAULT_REPETITIONS,
        target_sample_duration_ns=None,
        timing_scope="PROCESS_E2E",
        interleaved=True,
    )
    result = BenchmarkResult(
        run_id=f"native-v1-{case.workload_id}-{case.size}-{built.variant}",
        benchmark_repo_sha=benchmark_sha,
        s3_sha=s3_sha,
        upstream_shas={},
        environment=environment,
        workload={
            "id": case.workload_id,
            "size_class": case.size,
            "logical_shape": case.logical_shape,
            "physical_layout": case.physical_layout,
            "index_mapping": case.index_mapping,
            "work_unit": "adapter-defined useful operation",
            "work_units_per_sample": _work_units(case),
            "source_sha256": built.metrics["source_sha256"],
        },
        variant={"id": built.variant, "role": "NATIVE_MEASUREMENT", "optimization": built.optimization},
        correctness=correctness,
        build={"mode": "S3_NATIVE_X86_64", "assembly_path": str(built.assembly_path), "executable_path": str(built.executable_path)},
        measurement_protocol=protocol,
        samples=tuple(float(value) for value in timed["samples"]),
        work_units=_work_units(case),
        artifact_metrics={
            **built.metrics,
            "helper_calls": "NOT_AVAILABLE_SEPARATELY",
            "bounds_checks": "NOT_AVAILABLE",
            "frame_loads": "NOT_AVAILABLE",
            "frame_stores": "NOT_AVAILABLE",
        },
        hardware_metrics={
            "user_cpu_ns_samples": [item["user_cpu_ns"] for item in timed["resource_samples"]],
            "system_cpu_ns_samples": [item["system_cpu_ns"] for item in timed["resource_samples"]],
            "peak_rss_bytes_samples": [item["peak_rss_bytes"] for item in timed["resource_samples"]],
            "minor_faults_samples": [item["minor_faults"] for item in timed["resource_samples"]],
            "major_faults_samples": [item["major_faults"] for item in timed["resource_samples"]],
            "perf_counters": "NOT_AVAILABLE_PER_POLICY_OR_PERMISSION",
        },
    )
    return result.to_dict()


def run_measurement(args: argparse.Namespace) -> Path:
    benchmark_sha = require_commit(ROOT, args.benchmark_sha, label="benchmark repository")
    s3_repo = args.s3_repo.resolve()
    provenance = require_provenance(
        s3_repo=s3_repo,
        requested_s3_sha=args.s3_sha,
        benchmark_repo=ROOT,
        requested_benchmark_sha=benchmark_sha,
    )
    os.environ["S3_REPO"] = str(s3_repo)
    os.environ["S3_COMMIT"] = provenance["s3_commit"]
    if str(s3_repo) not in sys.path:
        sys.path.insert(0, str(s3_repo))
    environment = collect_environment(s3_repo, benchmark_sha)
    environment["perf"] = _perf_probe()
    from bootstrap.s3.backends.x86_64 import NativeToolchain
    toolchain = NativeToolchain.detect()
    cases = performance_cases()
    run = RunIdentity.create(args.output_root, args.run_id)
    measurements: list[dict[str, Any]] = []
    gates: list[dict[str, Any]] = []
    skipped_runtime: list[dict[str, str]] = []
    for index, case in enumerate(cases, start=1):
        print(f"CORRECTNESS {index}/{len(cases)} {case.workload_id} {case.size}", flush=True)
        try:
            correctness = _correctness_gate(case, toolchain, run.run_root)
        except Exception as error:
            skipped_runtime.append({
                "id": case.workload_id,
                "size": case.size,
                "status": "NATIVE_NOT_QUALIFIED",
                "reason": f"{type(error).__name__}: {error}",
            })
            print(f"SKIP {index}/{len(cases)} {case.workload_id} {case.size}: {error}", flush=True)
            continue
        gates.append({"workload_id": case.workload_id, "size": case.size, **correctness})
        built_variants = [
            _build_variant(case, "O0", "s3-o0", run.run_root, toolchain),
            _build_variant(case, "O1", "s3-o1", run.run_root, toolchain),
        ]
        for built in built_variants:
            print(f"MEASURE {index}/{len(cases)} {case.workload_id} {case.size} {built.variant}", flush=True)
            timed = _measure_variant(built, MeasurementProtocol(warmups=DEFAULT_WARMUPS, repetitions=DEFAULT_REPETITIONS, timing_scope="PROCESS_E2E", interleaved=True))
            measurements.append(_serialize_measurement(case, built, correctness, timed, environment, benchmark_sha, provenance["s3_commit"]))
    environment["load_average_after"] = os.getloadavg() if hasattr(os, "getloadavg") else None
    environment["environment_noisy"] = bool(environment["load_average_after"] and environment["load_average_after"][0] > (os.cpu_count() or 1))
    payload = {
        "schema": "s3.benchmark.native-measurement.v1",
        "campaign": "S3_BENCHMARKS_2_1_NATIVE_MEASUREMENT",
        "provenance": provenance,
        "environment": environment,
        "corpus": {
            "source": "benchmarks.candidate_activation.workloads.performance_cases",
            "sizes_declared_before_measurement": ["small", "medium"],
            "case_count": len(cases),
            "workloads": [
                {
                    "id": case.workload_id,
                    "size": case.size,
                    "logical_shape": case.logical_shape,
                    "physical_layout": case.physical_layout,
                    "index_mapping": case.index_mapping,
                    "work_units": _work_units(case),
                    "source_sha256": hashlib.sha256(case.source.encode("utf-8")).hexdigest(),
                    "source_bytes": len(case.source.encode("utf-8")),
                }
                for case in cases
            ],
            "skipped": {
                "scientific.rmsd.single": "MEASURED_BY_ADAPTER_GENERATOR",
                "realworld.jsmn": "legacy_harness_not_joined_to_protocol_v2",
                "compiler.tsvc.initial-subset": "capability_shape_evidence_only",
                "hpc.prk.stencil": "not_activated_in_2.0.1",
                "hpc.prk.dgemm": "not_activated_in_2.0.1",
                "runtime": skipped_runtime,
            },
        },
        "correctness_gates": gates,
        "measurement_policy": {
            "mode": "SEPARATE_NATIVE_MEASUREMENT_EXECUTABLE",
            "timing_scope": "PROCESS_E2E",
            "setup_scope": "PER_PROCESS_BEFORE_WORKLOAD",
            "iterations_per_sample": 1,
            "kernel_time": "NOT_AVAILABLE",
            "anti_dce": "ONE_INTEGER_CANARY_AFTER_WORKLOAD",
            "warmups": DEFAULT_WARMUPS,
            "repetitions": DEFAULT_REPETITIONS,
            "interleaved": True,
            "target_sample_duration": "NOT_REACHED_FOR_PROCESS_E2E_MICROWORKLOADS",
            "fast_math": False,
        },
        "measurements": measurements,
        "raw_samples": "PRESERVED_IN_MEASUREMENTS",
        "perf": environment["perf"],
    }
    path = run.write_json_once("measurement-results.json", payload)
    run.write_json_once("artifact-manifest.json", {
        "schema": "s3.benchmark.artifact-manifest.v2",
        "run_id": run.run_id,
        "provenance": provenance,
        "measurement_results": file_record(run, path),
        "artifact_count": sum(1 for _ in run.run_root.rglob("*") if _.is_file()),
    })
    print(f"RUN_ID={run.run_id}")
    print(f"MEASUREMENT_RESULTS={path}")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--s3-sha", default=EXPECTED_S3_SHA)
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--output-root", type=Path, default=ROOT / "baselines" / "native-v1")
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    run_measurement(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
