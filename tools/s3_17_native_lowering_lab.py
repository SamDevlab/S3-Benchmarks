from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import math
import platform
import random
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "benchmarks/s3-1.7-native-lowering/manifest.json"
FIXTURE_PATH = ROOT / "benchmarks/s3-1.7-native-lowering/fixtures/s3-1.5-reference-results-v1.json"
DATASET_PATH = ROOT / "benchmarks/s3-1.7-native-lowering/fixtures/datasets-v1.json"
CONTROL_ADAPTER_PATH = ROOT / "benchmarks/s3-1.7-native-lowering/control-ffi-budget-cli.patch"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _version_line(command: str) -> str:
    executable = shutil.which(command)
    if executable is None:
        raise RuntimeError(f"required tool is unavailable: {command}")
    completed = subprocess.run([executable, "--version"], capture_output=True, text=True, check=True)
    return (completed.stdout or completed.stderr).splitlines()[0]


def _cpu_model() -> str:
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.is_file():
        for line in cpuinfo.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.lower().startswith(("model name", "hardware")) and ":" in line:
                return line.split(":", 1)[1].strip()
    return platform.processor() or "unreported"


def load_contract(
    manifest_path: Path = MANIFEST_PATH,
    fixture_path: Path = FIXTURE_PATH,
    dataset_path: Path = DATASET_PATH,
    *,
    require_candidate_sha: bool = True,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    fixture_bytes = fixture_path.read_bytes()
    if _sha256(fixture_bytes) != manifest["reference_fixture"]["sha256"]:
        raise ValueError("reference fixture SHA-256 does not match the manifest")
    dataset_bytes = dataset_path.read_bytes()
    if _sha256(dataset_bytes) != manifest["dataset_manifest"]["sha256"]:
        raise ValueError("dataset manifest SHA-256 does not match the manifest")
    adapter = manifest["control_build_adapter"]
    adapter_bytes = (ROOT / adapter["path"]).read_bytes()
    if _sha256(adapter_bytes) != adapter["sha256"]:
        raise ValueError("control build adapter SHA-256 does not match the manifest")
    max_instructions = manifest["protocol"]["max_instructions"]
    if isinstance(max_instructions, bool) or not isinstance(max_instructions, int) or max_instructions < 1:
        raise ValueError("protocol.max_instructions must be a positive integer")
    if max_instructions != manifest["budget_provenance"]["value"]:
        raise ValueError("protocol max_instructions disagrees with pinned budget provenance")
    protocol = manifest["protocol"]
    if protocol.get("optimization") not in {"O0", "O1"}:
        raise ValueError("protocol.optimization must be O0 or O1")
    if protocol.get("source_syntax") not in {"0.5", "0.6"}:
        raise ValueError("protocol.source_syntax must be 0.5 or 0.6")
    candidate_sha = manifest.get("s3_candidate_sha")
    if require_candidate_sha and (not isinstance(candidate_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", candidate_sha)):
        raise ValueError("manifest must pin an exact S3 candidate commit SHA")
    fixture = json.loads(fixture_bytes)
    dataset = json.loads(dataset_bytes)
    return manifest, fixture, dataset


def _git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def verify_checkout(repo: Path, expected_sha: str, label: str) -> None:
    if not repo.is_dir():
        raise ValueError(f"{label} checkout does not exist: {repo}")
    actual = _git(repo, "rev-parse", "HEAD")
    if actual != expected_sha:
        raise ValueError(f"{label} HEAD mismatch: expected {expected_sha}, got {actual}")
    if _git(repo, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError(f"{label} checkout is not clean: {repo}")


def _prepare_control_build_overlay(
    control_repo: Path,
    artifact_dir: Path,
    manifest: dict[str, Any],
) -> tuple[Path, dict[str, Any]]:
    adapter = manifest["control_build_adapter"]
    overlay_root = Path(tempfile.mkdtemp(prefix="s3-17-control-cli-", dir=artifact_dir))
    shutil.copytree(control_repo / "bootstrap", overlay_root / "bootstrap")
    applied = subprocess.run(
        ["git", "apply", str(CONTROL_ADAPTER_PATH)],
        cwd=overlay_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if applied.returncode != 0:
        raise RuntimeError(f"control CLI compatibility patch failed: {applied.stderr.strip()}")
    file_hashes = {
        relative_path: _sha256((overlay_root / relative_path).read_bytes())
        for relative_path in adapter["files"]
    }
    return overlay_root, {
        "status": "APPLIED_TO_TEMPORARY_BOOTSTRAP_COPY",
        "reason": adapter["reason"],
        "patch_path": adapter["path"],
        "patch_sha256": adapter["sha256"],
        "files": file_hashes,
        "overlay_path": str(overlay_root),
        "backend_sources_modified": False,
    }


def _build_command(
    repo: Path,
    source: Path,
    library: Path,
    assembly: Path,
    *,
    optimization: str,
    source_syntax: str,
    max_instructions: int,
) -> list[str]:
    return [
        sys.executable,
        "-m",
        "bootstrap.s3.cli",
        "ffi-build",
        str(source),
        "-O",
        optimization.removeprefix("O"),
        "--source-syntax",
        source_syntax,
        "--max-instructions",
        str(max_instructions),
        "--native-policy",
        "baseline",
        "-o",
        str(library),
        "--keep-assembly",
        str(assembly),
    ]


def _build(
    repo: Path,
    source: Path,
    library: Path,
    assembly: Path,
    *,
    optimization: str,
    source_syntax: str,
    max_instructions: int,
) -> dict[str, Any]:
    command = _build_command(
        repo,
        source,
        library,
        assembly,
        optimization=optimization,
        source_syntax=source_syntax,
        max_instructions=max_instructions,
    )
    completed = subprocess.run(
        command,
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    record = {
        "command": command,
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }
    if completed.returncode != 0:
        raise RuntimeError(f"S3 public CLI build failed: {completed.stderr.strip()}")
    if not library.is_file() or not assembly.is_file():
        raise RuntimeError("S3 CLI reported success without both requested artifacts")
    record["library_sha256"] = _sha256(library.read_bytes())
    record["assembly_sha256"] = _sha256(assembly.read_bytes())
    return record


def _double_array(values: list[float]) -> Any:
    return (ctypes.c_double * len(values))(*values)


def _int64_array(values: list[int]) -> Any:
    return (ctypes.c_int64 * len(values))(*values)


def _bind(
    library: Any,
    workload_id: str,
    data: dict[str, Any],
    capacity_w: float,
) -> tuple[Any, Any, dict[str, Any]]:
    if workload_id == "engineering.point-cloud-summary.v1":
        function = library.point_cloud_summary
        coordinates = _double_array(data["coordinates"])
        output = (ctypes.c_double * 10)()
        function.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int64, ctypes.c_int64,
                             ctypes.POINTER(ctypes.c_double), ctypes.c_int64]
        function.restype = ctypes.c_int64
        args = (coordinates, len(coordinates), int(data["point_count"]), output, 10)
    elif workload_id == "geospatial.raster-window-statistics.v1":
        function = library.raster_window_statistics
        values = _double_array(data["values"])
        mask = _int64_array(data["valid_mask"])
        output = (ctypes.c_double * 6)()
        function.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
                             ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64,
                             ctypes.c_int64, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int64]
        function.restype = ctypes.c_int64
        args = (values, len(values), mask, len(mask), int(data["width"]), int(data["height"]),
                float(data["threshold"]), output, 6)
    elif workload_id == "energy.pv-timeseries-aggregation.v1":
        function = library.energy_series_aggregation
        ac_power = _double_array(data["ac_power_w"])
        load = _double_array(data["load_w"])
        output = (ctypes.c_double * 5)()
        function.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
                             ctypes.POINTER(ctypes.c_double), ctypes.c_int64, ctypes.c_double,
                             ctypes.POINTER(ctypes.c_double), ctypes.c_int64]
        function.restype = ctypes.c_int64
        args = (ac_power, len(ac_power), load, len(load), capacity_w, output, 5)
    else:
        raise ValueError(f"unsupported workload contract: {workload_id}")
    return function, output, {"args": args}


def _invoke(bound: tuple[Any, Any, dict[str, Any]]) -> list[float]:
    function, output, prepared = bound
    status = int(function(*prepared["args"]))
    if status != 0:
        raise RuntimeError(f"native workload returned status {status}")
    return [float(value) for value in output]


def _check_reference(record: dict[str, Any], output: list[float], fields: list[str]) -> dict[str, Any]:
    expected = record["expected_output"]
    tolerances = record["numerical_tolerance"]
    actual_by_field = dict(zip(fields, output, strict=True))
    comparisons: list[dict[str, Any]] = []
    for field in fields:
        actual = actual_by_field[field]
        target = float(expected[field])
        allowed = max(float(tolerances["absolute"]), float(tolerances["relative"]) * abs(target))
        error = abs(actual - target)
        if not math.isfinite(actual) or error > allowed:
            raise AssertionError(f"{record['workload_id']} {field}: got {actual}, expected {target} ± {allowed}")
        comparisons.append({"field": field, "actual": actual, "expected": target, "absolute_error": error,
                            "allowed_error": allowed})
    return {"status": "PASS", "comparisons": comparisons}


def _disassembly_metrics(library_path: Path, symbol: str) -> dict[str, Any]:
    objdump = shutil.which("objdump")
    if objdump is None:
        raise RuntimeError("objdump is required for independent static code metrics")
    completed = subprocess.run(
        [objdump, "-d", f"--disassemble={symbol}", str(library_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    instruction_re = re.compile(r"^\s*[0-9a-fA-F]+:\s+(?:[0-9a-fA-F]{2}\s+)+([A-Za-z][A-Za-z0-9.]*)\s*(.*)$")
    instructions: list[tuple[str, str]] = []
    for line in completed.stdout.splitlines():
        match = instruction_re.match(line)
        if match:
            instructions.append((match.group(1).lower(), match.group(2)))
    if not instructions:
        raise RuntimeError(f"objdump did not find machine instructions for {symbol}")
    return {
        "symbol": symbol,
        "static_machine_instructions": len(instructions),
        "static_memory_operand_instructions": sum("(" in operands or "[" in operands for _, operands in instructions),
        "static_branches": sum(mnemonic.startswith(("j", "loop")) for mnemonic, _ in instructions),
        "disassembly_sha256": _sha256(completed.stdout.encode()),
    }


def _sample(bound: tuple[Any, Any, dict[str, Any]], iterations: int) -> float:
    function, _, prepared = bound
    start = time.perf_counter_ns()
    for _ in range(iterations):
        status = function(*prepared["args"])
        if status != 0:
            raise RuntimeError(f"timed native workload returned status {status}")
    return (time.perf_counter_ns() - start) / iterations


def _bootstrap_interval(values: list[float], seed: int, count: int) -> list[float]:
    rng = random.Random(seed)
    medians = [statistics.median(rng.choices(values, k=len(values))) for _ in range(count)]
    medians.sort()
    return [medians[int(count * 0.025)], medians[min(count - 1, int(count * 0.975))]]


def _paired_summary(control: list[float], candidate: list[float], seed: int, count: int) -> dict[str, Any]:
    ratios = [base / changed for base, changed in zip(control, candidate, strict=True)]
    median_ratio = statistics.median(ratios)
    interval = _bootstrap_interval(ratios, seed, count)
    threshold = 1.05
    if interval[0] > threshold:
        classification = "MATERIAL_IMPROVEMENT"
    elif interval[1] < 1.0 / threshold:
        classification = "MATERIAL_SLOWDOWN"
    elif interval[0] >= 1.0 / threshold and interval[1] <= threshold:
        classification = "NO_MATERIAL_CHANGE_WITHIN_5_PERCENT"
    else:
        classification = "INCONCLUSIVE"
    return {
        "control_over_candidate_median_ratio": median_ratio,
        "paired_bootstrap_95_percentile_interval": interval,
        "classification": classification,
        "material_change_threshold": 0.05,
        "bootstrap_resamples": count,
        "bootstrap_seed": seed,
    }


def run_lab(control_repo: Path, candidate_repo: Path, artifact_dir: Path) -> dict[str, Any]:
    manifest, fixture, dataset = load_contract()
    control_sha = manifest["s3_control_sha"]
    candidate_sha = manifest["s3_candidate_sha"]
    verify_checkout(control_repo, control_sha, "control")
    verify_checkout(candidate_repo, candidate_sha, "candidate")
    artifact_dir.mkdir(parents=True, exist_ok=True)
    control_build_repo, control_build_adapter = _prepare_control_build_overlay(
        control_repo,
        artifact_dir,
        manifest,
    )
    expected_records = {item["workload_id"]: item for item in fixture["workloads"]}
    protocol = manifest["protocol"]
    workload_results: dict[str, Any] = {}
    prepared_workloads: dict[str, dict[str, Any]] = {}
    for workload in manifest["workloads"]:
        workload_id = workload["workload_id"]
        record = expected_records[workload_id]
        fixture_output = json.dumps(record["expected_output"], sort_keys=True, indent=2, allow_nan=False).encode() + b"\n"
        if _sha256(fixture_output) != record["output_sha256"]:
            raise ValueError(f"external output fixture hash mismatch for {workload_id}")
        builds: dict[str, Any] = {}
        libraries: dict[str, Any] = {}
        static: dict[str, Any] = {}
        with tempfile.TemporaryDirectory(prefix="s3-17-", dir=artifact_dir) as temporary:
            temp = Path(temporary)
            for label, repo in (("control", control_repo), ("candidate", candidate_repo)):
                source = repo / workload["source_path"]
                if _sha256(source.read_bytes()) != workload["source_sha256"]:
                    raise ValueError(f"S3 source file SHA mismatch for {workload_id} in {label}")
                library_path = temp / f"{label}-{workload_id}.so"
                assembly_path = temp / f"{label}-{workload_id}.s"
                build_repo = control_build_repo if label == "control" else repo
                builds[label] = _build(
                    build_repo,
                    source,
                    library_path,
                    assembly_path,
                    optimization=protocol["optimization"],
                    source_syntax=protocol["source_syntax"],
                    max_instructions=protocol["max_instructions"],
                )
                libraries[label] = ctypes.CDLL(str(library_path))
                static[label] = _disassembly_metrics(library_path, workload["native_symbol"])

            bound = {
                label: _bind(
                    libraries[label],
                    workload_id,
                    record["input"],
                    float(dataset["energy"]["dc_capacity_w"]),
                )
                for label in ("control", "candidate")
            }
            correctness: dict[str, Any] = {}
            outputs: dict[str, list[float]] = {}
            for label in ("control", "candidate"):
                outputs[label] = _invoke(bound[label])
                correctness[label] = _check_reference(record, outputs[label], workload["output_fields"])
            if outputs["control"] != outputs["candidate"]:
                raise AssertionError(f"control/candidate outputs differ for {workload_id}")

            workload_results[workload_id] = {
                "reference_engine": record["reference_engine"],
                "reference_engine_version": record["reference_engine_version"],
                "reference_output_sha256": record["output_sha256"],
                "input_fixture_sha256": _sha256(json.dumps(record["input"], sort_keys=True, allow_nan=False).encode()),
                "correctness": correctness,
                "control_candidate_output_equal": True,
                "static_metrics": static,
                "builds": builds,
            }
            prepared_workloads[workload_id] = bound

    for workload in manifest["workloads"]:
        workload_id = workload["workload_id"]
        bound = prepared_workloads[workload_id]
        for _ in range(protocol["warmups"]):
            _sample(bound["control"], protocol["iterations_per_sample"])
            _sample(bound["candidate"], protocol["iterations_per_sample"])

        rng = random.Random(protocol["paired_order_seed"])
        control_samples: list[float] = []
        candidate_samples: list[float] = []
        order: list[list[str]] = []
        for _ in range(protocol["samples"]):
            labels = ["control", "candidate"]
            rng.shuffle(labels)
            order.append(labels)
            durations: dict[str, float] = {}
            for label in labels:
                durations[label] = _sample(bound[label], protocol["iterations_per_sample"])
            control_samples.append(durations["control"])
            candidate_samples.append(durations["candidate"])

        workload_results[workload_id]["timing"] = {
            "control_ns_per_call": control_samples,
            "candidate_ns_per_call": candidate_samples,
            "control_median_ns_per_call": statistics.median(control_samples),
            "candidate_median_ns_per_call": statistics.median(candidate_samples),
            "control_coefficient_of_variation": statistics.pstdev(control_samples) / statistics.mean(control_samples),
            "candidate_coefficient_of_variation": statistics.pstdev(candidate_samples) / statistics.mean(candidate_samples),
            "paired_order": order,
            "paired_comparison": _paired_summary(
                control_samples,
                candidate_samples,
                protocol["paired_order_seed"],
                protocol["bootstrap_resamples"],
            ),
        }

    return {
        "schema_version": "1.0.0",
        "experiment_id": manifest["experiment_id"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "s3_control_sha": control_sha,
        "s3_candidate_sha": candidate_sha,
        "s3_control_repo": str(control_repo),
        "s3_candidate_repo": str(candidate_repo),
        "s3_checkouts_clean_and_exact": True,
        "s3_control_build_adapter": control_build_adapter,
        "benchmark_lab_source_sha": _sha256(Path(__file__).read_bytes()),
        "manifest_sha256": _sha256(MANIFEST_PATH.read_bytes()),
        "reference_fixture_sha256": manifest["reference_fixture"]["sha256"],
        "dataset_manifest_sha256": manifest["dataset_manifest"]["sha256"],
        "budget_provenance": manifest["budget_provenance"],
        "host": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": _cpu_model(),
            "python": platform.python_version(),
        },
        "toolchain": {
            "cc": _version_line("cc"),
            "linker": _version_line("ld"),
            "objdump": _version_line("objdump"),
        },
        "protocol": protocol,
        "correctness_before_timing": True,
        "performance_claim_scope": "paired native execution characterization; no claim against C or other compilers",
        "workloads": workload_results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Independent S3 1.7 native lowering evidence runner")
    parser.add_argument("--s3-control", type=Path, required=True)
    parser.add_argument("--s3-candidate", type=Path, required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_lab(args.s3_control.resolve(), args.s3_candidate.resolve(), args.artifact_dir.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"EXPERIMENT={result['experiment_id']}")
    print(f"S3_CONTROL_SHA={result['s3_control_sha']}")
    print(f"S3_CANDIDATE_SHA={result['s3_candidate_sha']}")
    print(f"RESULT={args.output}")
    print("CORRECTNESS_BEFORE_TIMING=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
