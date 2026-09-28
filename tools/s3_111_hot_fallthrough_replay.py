"""Independently replay and inspect a pinned S3 hot-fallthrough pair."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib.util
import json
import platform
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

EXPECTED_S3_COMMIT = "832b1cc04fe1f6174e482eb3a245e08af3d53211"
EXPECTED_S3_TREE = "dc1138890655169088f9371ce32a9050cfc3af8d"
EXPECTED_BENCH_COMMIT = "b3ecb9b2269b583cba0706fd7ed13956a9641512"
EXPECTED_BENCH_TREE = "06316635dfc1830d3ec3955803acb0d168b77a7e"
EXPECTED_EXPERIMENT_ID = "EXP-S3-111-HOT-FALLTHROUGH-001"
WORKLOAD_SYMBOLS = {
    "engineering.point-cloud-summary.v1": "point_cloud_summary",
    "geospatial.raster-window-statistics.v1": "raster_window_statistics",
    "energy.pv-timeseries-aggregation.v1": "energy_series_aggregation",
}


def _git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True
    ).stdout.strip()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_pinned_benchmark(source_root: Path):
    script = source_root / "tools/s3_15_native_workload_benchmark.py"
    if not script.is_file():
        raise FileNotFoundError(f"pinned S3 workload helper is missing: {script}")
    sys.path.insert(0, str(source_root))
    spec = importlib.util.spec_from_file_location("s3_111_pinned_workload", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load pinned S3 workload helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_artifact(path: Path, descriptor: object) -> dict[str, Any]:
    if not isinstance(descriptor, dict):
        raise ValueError("artifact descriptor must be an object")
    name, size, digest = descriptor.get("file_name"), descriptor.get("bytes"), descriptor.get("sha256")
    if not isinstance(name, str) or Path(name).name != name or path.name != name:
        raise ValueError("artifact filename does not match its descriptor")
    if not isinstance(size, int) or isinstance(size, bool) or size <= 0:
        raise ValueError("artifact byte length is invalid")
    if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
        raise ValueError("artifact SHA-256 is invalid")
    if path.is_symlink() or not path.is_file():
        raise ValueError("artifact must be a regular file")
    payload = path.read_bytes()
    if len(payload) != size or _sha256(payload) != digest:
        raise ValueError("artifact bytes differ from the pinned descriptor")
    return {"file_name": name, "bytes": size, "sha256": digest}


def parse_disassembly(text: str) -> dict[str, int]:
    instructions: list[tuple[str, str]] = []
    for line in text.splitlines():
        if ":\t" not in line:
            continue
        columns = line.split("\t")
        if len(columns) < 3:
            continue
        fields = columns[2].strip().split(None, 1)
        if fields:
            instructions.append((fields[0].lower(), fields[1] if len(fields) > 1 else ""))
    return {
        "static_machine_instructions": len(instructions),
        "static_branches": sum(mnemonic.startswith("j") for mnemonic, _ in instructions),
        "static_memory_references": sum("(" in operands for _, operands in instructions),
    }


def inspect_binary(path: Path, symbol: str) -> dict[str, int]:
    size_output = subprocess.run(
        ["size", "-A", str(path)], check=True, capture_output=True, text=True
    ).stdout
    text_bytes = 0
    for line in size_output.splitlines():
        columns = line.split()
        if columns and columns[0] == ".text":
            text_bytes = int(columns[1])
            break
    nm_output = subprocess.run(
        ["nm", "-S", "--defined-only", str(path)], check=True, capture_output=True, text=True
    ).stdout
    symbol_bytes = 0
    for line in nm_output.splitlines():
        columns = line.split()
        if len(columns) >= 4 and columns[-1] == symbol:
            symbol_bytes = int(columns[1], 16)
            break
    if text_bytes <= 0 or symbol_bytes <= 0:
        raise ValueError("independent ELF inspection could not find .text or the exported symbol")
    disassembly = subprocess.run(
        ["objdump", "-d", f"--disassemble={symbol}", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return {
        **parse_disassembly(disassembly),
        "text_section_bytes": text_bytes,
        "exported_function_bytes": symbol_bytes,
    }


def _assert_metrics_match_independently(
    recorded: dict[str, Any], baseline: dict[str, int], candidate: dict[str, int]
) -> dict[str, int]:
    recorded_baseline = recorded.get("baseline")
    recorded_candidate = recorded.get("candidate")
    recorded_delta = recorded.get("candidate_minus_baseline")
    if not all(isinstance(row, dict) for row in (recorded_baseline, recorded_candidate, recorded_delta)):
        raise ValueError("recorded native structure is malformed")
    checked = (
        "static_machine_instructions",
        "static_branches",
        "static_memory_references",
        "text_section_bytes",
        "exported_function_bytes",
    )
    deltas: dict[str, int] = {}
    for metric in checked:
        if baseline[metric] != recorded_baseline.get(metric):
            raise ValueError(f"independent baseline {metric} differs from S3 record")
        if candidate[metric] != recorded_candidate.get(metric):
            raise ValueError(f"independent candidate {metric} differs from S3 record")
        delta = candidate[metric] - baseline[metric]
        if delta != recorded_delta.get(metric):
            raise ValueError(f"independent {metric} delta differs from S3 record")
        deltas[metric] = delta
    return deltas


def replay(
    *, source_root: Path, lab_root: Path, experiment_path: Path, binary_root: Path
) -> dict[str, Any]:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("independent native replay requires Linux x86-64")
    source_root, lab_root = source_root.resolve(), lab_root.resolve()
    source_commit = _git(source_root, "rev-parse", "HEAD")
    source_tree = _git(source_root, "rev-parse", "HEAD^{tree}")
    if (source_commit, source_tree) != (EXPECTED_S3_COMMIT, EXPECTED_S3_TREE):
        raise ValueError("S3 checkout does not match the pinned control")
    if _git(source_root, "status", "--porcelain", "--", "bootstrap/s3"):
        raise ValueError("tracked S3 compiler sources are modified")
    bench_commit = _git(lab_root, "rev-parse", "HEAD")
    bench_tree = _git(lab_root, "rev-parse", "HEAD^{tree}")
    if (bench_commit, bench_tree) != (EXPECTED_BENCH_COMMIT, EXPECTED_BENCH_TREE):
        raise ValueError("S3-Benchmarks checkout does not match the pinned 1.11 lab base")
    if _git(lab_root, "status", "--porcelain", "--untracked-files=no"):
        raise ValueError("tracked S3-Benchmarks files differ from the pinned lab base")

    experiment_bytes = experiment_path.read_bytes()
    experiment = json.loads(experiment_bytes)
    if experiment.get("experiment_id") != EXPECTED_EXPERIMENT_ID:
        raise ValueError("unsupported hot-fallthrough experiment identity")
    control = experiment.get("control")
    workload = experiment.get("workload")
    artifacts = experiment.get("artifacts")
    structure = experiment.get("native_structure")
    if not all(isinstance(item, dict) for item in (control, workload, artifacts, structure)):
        raise ValueError("experiment evidence is incomplete")
    if (control.get("s3_commit"), control.get("s3_tree")) != (source_commit, source_tree):
        raise ValueError("experiment source identity differs from the clean S3 control")
    if workload.get("reference_correctness") != "PASS_BASELINE_AND_CANDIDATE":
        raise ValueError("S3 candidate did not record reference correctness")

    baseline_path = binary_root / str(artifacts.get("baseline", {}).get("file_name"))
    candidate_path = binary_root / str(artifacts.get("candidate", {}).get("file_name"))
    baseline_artifact = verify_artifact(baseline_path, artifacts.get("baseline"))
    candidate_artifact = verify_artifact(candidate_path, artifacts.get("candidate"))

    benchmark = _load_pinned_benchmark(source_root)
    manifest, references = benchmark._load_inputs()
    workload_id = workload.get("workload_id")
    manifest_row = next(
        row for row in manifest["workloads"] if row["workload_id"] == workload_id
    )
    source_bytes = (source_root / "benchmarks" / manifest_row["s3_source"]).read_bytes()
    canonical_source = source_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if _sha256(canonical_source) != workload.get("source_sha256_canonical_lf"):
        raise ValueError("benchmark workload source does not match candidate evidence")
    reference = next(row for row in references["workloads"] if row["workload_id"] == workload_id)
    outputs: dict[str, list[float]] = {}
    output_digests: dict[str, str] = {}
    for label, path, expected_digest in (
        ("baseline", baseline_path, workload.get("baseline_output_sha256")),
        ("candidate", candidate_path, workload.get("candidate_output_sha256")),
    ):
        library = ctypes.CDLL(str(path))
        output = (ctypes.c_double * len(benchmark.OUTPUT_KEYS[workload_id]))()
        status = benchmark._make_call(library, reference, output)()
        values = list(output)
        if status != 0:
            raise RuntimeError(f"{label} native artifact returned status {status}")
        benchmark._check_output(values, reference["expected_output"], workload_id)
        digest = _sha256(benchmark._json_bytes([round(value, 10) for value in values]))
        if digest != expected_digest:
            raise ValueError(f"{label} output does not match the S3 experiment record")
        outputs[label] = values
        output_digests[label] = digest
    if outputs["baseline"] != outputs["candidate"]:
        raise ValueError("baseline/candidate exact result mismatch")

    try:
        symbol = WORKLOAD_SYMBOLS[workload_id]
    except KeyError as exc:
        raise ValueError(f"unsupported workload symbol: {workload_id}") from exc
    independent_baseline = inspect_binary(baseline_path, symbol)
    independent_candidate = inspect_binary(candidate_path, symbol)
    independent_deltas = _assert_metrics_match_independently(
        structure, independent_baseline, independent_candidate
    )
    return {
        "schema_version": "1.0.0",
        "report_kind": "S3_BENCHMARKS_INDEPENDENT_HOT_FALLTHROUGH_REPLAY",
        "experiment_id": EXPECTED_EXPERIMENT_ID,
        "status": "PASS",
        "classification": "INDEPENDENT_CORRECTNESS_AND_STRUCTURE_REPLAY_NO_TIMING",
        "provenance": {
            "bench_commit": bench_commit,
            "bench_tree": bench_tree,
            "bench_tracked_tree_clean": True,
            "bench_tool_sha256": _sha256(Path(__file__).read_bytes()),
            "s3_commit": source_commit,
            "s3_tree": source_tree,
            "s3_tracked_compiler_clean": True,
            "experiment_sha256": _sha256(experiment_bytes),
            "pinned_workload_helper_sha256": _sha256(
                (source_root / "tools/s3_15_native_workload_benchmark.py").read_bytes()
            ),
            "target": "Linux x86-64",
        },
        "workload_id": workload_id,
        "artifacts": {"baseline": baseline_artifact, "candidate": candidate_artifact},
        "correctness": {
            "baseline_reference": "PASS",
            "candidate_reference": "PASS",
            "outputs_exactly_equal": True,
            "baseline_output_sha256": output_digests["baseline"],
            "candidate_output_sha256": output_digests["candidate"],
        },
        "independent_native_structure": {
            "baseline": independent_baseline,
            "candidate": independent_candidate,
            "candidate_minus_baseline": independent_deltas,
            "matches_s3_experiment_metrics": True,
        },
        "timing_class": "NOT_MEASURED_IN_LAB_REPLAY",
        "native_speedup_claim": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-source", type=Path, required=True)
    parser.add_argument("--lab-root", type=Path, required=True)
    parser.add_argument("--experiment", type=Path, required=True)
    parser.add_argument("--binary-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = replay(
        source_root=args.s3_source,
        lab_root=args.lab_root,
        experiment_path=args.experiment,
        binary_root=args.binary_root,
    )
    encoded = (json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(f"OUTPUT={args.output}")
    print(f"OUTPUT_SHA256={_sha256(encoded)}")
    print("INDEPENDENT_REPLAY=PASS correctness=yes native_metrics=match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
