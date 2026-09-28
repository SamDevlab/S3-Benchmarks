"""Independently rerun and verify S3 1.11 experimental native candidates."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib.util
import json
import math
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any


EXPERIMENT_LABELS = {
    "EXP-S3-111-VALUE-COST-001": "ssa_substitution",
    "EXP-S3-111-VALUE-COST-002": "store_to_load",
}
EXPECTED_S3_COMMIT = "832b1cc04fe1f6174e482eb3a245e08af3d53211"
EXPECTED_S3_TREE = "dc1138890655169088f9371ce32a9050cfc3af8d"
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


def _verify_artifact(path: Path, descriptor: object) -> dict[str, object]:
    if not isinstance(descriptor, dict):
        raise ValueError("native artifact descriptor must be an object")
    name, size, digest = (
        descriptor.get("file_name"), descriptor.get("bytes"), descriptor.get("sha256")
    )
    if not isinstance(name, str) or name != path.name or Path(name).name != name:
        raise ValueError("native artifact filename does not match the supplied binary")
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("native artifact size is invalid")
    if not isinstance(digest, str) or len(digest) != 64:
        raise ValueError("native artifact SHA-256 is invalid")
    if path.is_symlink() or not path.is_file():
        raise ValueError("native candidate must be a regular file")
    data = path.read_bytes()
    if len(data) != size or _sha256(data) != digest:
        raise ValueError("native candidate bytes do not match the pinned descriptor")
    return {"file_name": name, "bytes": size, "sha256": digest}


def _load_pinned_benchmark(source_root: Path):
    script = source_root / "tools/s3_15_native_workload_benchmark.py"
    if not script.is_file():
        raise FileNotFoundError(f"pinned S3 benchmark script is missing: {script}")
    sys.path.insert(0, str(source_root))
    spec = importlib.util.spec_from_file_location("s3_111_pinned_benchmark", script)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load pinned S3 workload definitions")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replay(
    *, source_root: Path, experiment_path: Path, binary_root: Path
) -> dict[str, Any]:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("candidate replay requires Linux x86-64")
    source_root = source_root.resolve()
    experiment = json.loads(experiment_path.read_text(encoding="utf-8"))
    if not isinstance(experiment, dict):
        raise ValueError("experiment evidence must be an object")
    experiment_id = experiment.get("experiment_id")
    candidate_label = EXPERIMENT_LABELS.get(experiment_id)
    if candidate_label is None:
        raise ValueError("unsupported or unpinned experiment identity")
    control = experiment.get("control")
    if not isinstance(control, dict):
        raise ValueError("experiment control provenance is missing")

    source_commit = _git(source_root, "rev-parse", "HEAD")
    source_tree = _git(source_root, "rev-parse", "HEAD^{tree}")
    if source_commit != EXPECTED_S3_COMMIT or source_tree != EXPECTED_S3_TREE:
        raise ValueError("S3 source checkout is not the pinned campaign control")
    if _git(source_root, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("S3 source checkout must be clean for candidate replay")
    if control.get("s3_commit") != source_commit or control.get("s3_tree") != source_tree:
        raise ValueError("experiment source identity differs from the clean pinned checkout")
    if control.get("compiler_source_dirty") is not False:
        raise ValueError("experiment reports compiler source changes")

    benchmark = _load_pinned_benchmark(source_root)
    manifest, references = benchmark._load_inputs()
    reference_by_id = {row["workload_id"]: row for row in references["workloads"]}
    workloads = experiment.get("workloads")
    if not isinstance(workloads, list) or len(workloads) != len(WORKLOAD_SYMBOLS):
        raise ValueError("experiment workload set is incomplete")
    manifest_by_id = {row["workload_id"]: row for row in manifest["workloads"]}
    results: list[dict[str, object]] = []

    for row in workloads:
        if not isinstance(row, dict):
            raise ValueError("experiment workload row is malformed")
        workload_id = row.get("workload_id")
        if workload_id not in WORKLOAD_SYMBOLS or workload_id not in reference_by_id:
            raise ValueError(f"unknown workload: {workload_id}")
        reference = reference_by_id[workload_id]
        expected_source = manifest_by_id[workload_id]["s3_source"]
        source_bytes = (source_root / "benchmarks" / expected_source).read_bytes()
        source_sha = _sha256(source_bytes.replace(b"\r\n", b"\n"))
        if row.get("source_sha256") != source_sha:
            raise ValueError(f"{workload_id}: source digest differs from pinned input")

        artifacts = row.get("native_artifacts")
        if not isinstance(artifacts, dict):
            raise ValueError(f"{workload_id}: binary artifact descriptors are missing")
        artifact = _verify_artifact(
            binary_root / f"{workload_id}-{candidate_label}.so",
            artifacts.get(candidate_label),
        )
        library = ctypes.CDLL(str(binary_root / str(artifact["file_name"])))
        output = (ctypes.c_double * len(benchmark.OUTPUT_KEYS[workload_id]))()
        call = benchmark._make_call(library, reference, output)
        status = call()
        if status != 0:
            raise RuntimeError(f"{workload_id}: native candidate returned status {status}")
        values = list(output)
        benchmark._check_output(values, reference["expected_output"], workload_id)

        recorded = row.get("native_output")
        if not isinstance(recorded, dict):
            raise ValueError(f"{workload_id}: recorded output is missing")
        recorded_candidate = recorded.get(candidate_label)
        recorded_baseline = recorded.get("baseline")
        if not isinstance(recorded_candidate, dict) or not isinstance(recorded_baseline, dict):
            raise ValueError(f"{workload_id}: baseline/candidate output evidence is malformed")
        if values != recorded_candidate.get("values"):
            raise ValueError(f"{workload_id}: replayed output differs from candidate run")
        output_digest = _sha256(
            benchmark._json_bytes([round(value, 10) for value in values])
        )
        if output_digest != recorded_candidate.get("output_sha256"):
            raise ValueError(f"{workload_id}: replayed output digest differs from candidate record")
        if output_digest != recorded_baseline.get("output_sha256"):
            raise ValueError(f"{workload_id}: replayed output differs from baseline output")

        results.append(
            {
                "workload_id": workload_id,
                "source_sha256": source_sha,
                "candidate_artifact": artifact,
                "native_status": status,
                "reference_correctness": "PASS",
                "candidate_recorded_values_equal": True,
                "baseline_output_digest_equal": True,
                "output_sha256": output_digest,
            }
        )

    if {row["workload_id"] for row in results} != set(WORKLOAD_SYMBOLS):
        raise ValueError("experiment workloads do not match the complete pinned set")
    return {
        "schema_version": "1.0.0",
        "report_kind": "S3_BENCHMARKS_INDEPENDENT_NATIVE_CANDIDATE_REPLAY",
        "experiment_id": experiment_id,
        "candidate_label": candidate_label,
        "status": "PASS",
        "classification": "INDEPENDENT_CORRECTNESS_REPLAY_NO_TIMING_CLAIM",
        "provenance": {
            "bench_commit": _git(Path(__file__).resolve().parents[1], "rev-parse", "HEAD"),
            "bench_tree": _git(Path(__file__).resolve().parents[1], "rev-parse", "HEAD^{tree}"),
            "bench_worktree_dirty": bool(
                _git(Path(__file__).resolve().parents[1], "status", "--porcelain")
            ),
            "s3_commit": source_commit,
            "s3_tree": source_tree,
            "s3_worktree_clean": True,
            "experiment_json_sha256": hashlib.sha256(experiment_path.read_bytes()).hexdigest(),
            "replay_tool_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "target": "Linux x86-64",
        },
        "workloads": results,
        "native_speedup_claim": False,
        "timing_class": "NOT_MEASURED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-source", type=Path, required=True)
    parser.add_argument("--experiment", type=Path, required=True)
    parser.add_argument("--binary-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = replay(
        source_root=args.s3_source,
        experiment_path=args.experiment,
        binary_root=args.binary_root,
    )
    encoded = (json.dumps(report, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(f"OUTPUT={args.output}")
    print(f"OUTPUT_SHA256={_sha256(encoded)}")
    print(f"CANDIDATE_REPLAY={report['status']} workloads={len(report['workloads'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
