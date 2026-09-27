"""Validate and summarize the pinned S3 1.5-1.10 replay evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.s3_19_executor import WORKLOADS  # noqa: E402


EXPERIMENT_ID = "EXP-S3-110-HIST-001"
HISTORICAL_VERSION_SHAS = {
    "1.5": "c924148c6d95948778351c7dd1362259caff670c",
    "1.6": "cb88a8036af1bcdc026db193590cb961bee4737d",
    "1.7": "39dfbb5d19ecefc7df78da7dc8d3ea8e31d81df4",
    "1.8": "b8f446a5ea2b24b948a263cb955f426c5d0f48ce",
    "1.9": "211b1aecec756be42516322429720018f54001e7",
}
CURRENT_VERSION_SHA = "856bf0cd60c3da6ba701adec73c7858d063739a7"
VERSION_SHAS = {**HISTORICAL_VERSION_SHAS, "1.10": CURRENT_VERSION_SHA}


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_json(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value, raw


def _positive_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be positive numeric data")
    if not math.isfinite(float(value)) or value <= 0:
        raise ValueError(f"{label} must be positive numeric data")
    return float(value)


def build_index(
    matrix_path: Path,
    evidence_dir: Path,
    *,
    supplemental_matrix_path: Path | None = None,
    supplemental_evidence_dir: Path | None = None,
) -> dict[str, object]:
    matrix, matrix_bytes = _read_json(matrix_path)
    expected_shas = set(HISTORICAL_VERSION_SHAS.values())
    if matrix.get("report_kind") != "S3_BENCHMARKS_MULTI_SHA_EXECUTION_MATRIX":
        raise ValueError("unexpected multi-SHA report kind")
    if matrix.get("status") != "PASS" or matrix.get("execution_order") != "serial_ascending_sha":
        raise ValueError("multi-SHA replay matrix did not pass its serial protocol")
    if set(matrix.get("revision_order", [])) != expected_shas:
        raise ValueError("matrix revision set does not exactly match S3 1.5-1.9 pins")

    rows = matrix.get("runs")
    if not isinstance(rows, list) or len(rows) != len(HISTORICAL_VERSION_SHAS):
        raise ValueError("multi-SHA run rows are incomplete")
    rows_by_sha: dict[str, tuple[dict[str, Any], Path, str]] = {}
    for row in rows:
        if not isinstance(row, dict) or row.get("status") != "PASS":
            raise ValueError("every pinned historical replay must pass")
        sha = row.get("source_revision")
        if not isinstance(sha, str) or sha in rows_by_sha:
            raise ValueError("run rows have invalid or duplicate source revisions")
        result = row.get("result")
        if not isinstance(result, dict):
            raise ValueError(f"validated executor report missing for {sha}")
        rows_by_sha[sha] = (result, evidence_dir, "HISTORICAL_1_5_TO_1_9")

    if set(rows_by_sha) != expected_shas:
        raise ValueError("run rows do not exactly match pinned historical SHAs")

    matrix_groups: list[dict[str, object]] = [
        {
            "group": "HISTORICAL_1_5_TO_1_9",
            "matrix_path": matrix_path.resolve().relative_to(ROOT).as_posix(),
            "matrix_sha256": _sha256(matrix_bytes),
            "matrix_bytes": len(matrix_bytes),
            "revision_order": matrix["revision_order"],
            "execution_order": matrix["execution_order"],
        }
    ]
    include_current = supplemental_matrix_path is not None or supplemental_evidence_dir is not None
    if include_current:
        if supplemental_matrix_path is None or supplemental_evidence_dir is None:
            raise ValueError("supplemental matrix and evidence directory must be supplied together")
        supplemental, supplemental_bytes = _read_json(supplemental_matrix_path)
        if (
            supplemental.get("report_kind") != "S3_BENCHMARKS_MULTI_SHA_EXECUTION_MATRIX"
            or supplemental.get("status") != "PASS"
            or supplemental.get("execution_order") != "serial_ascending_sha"
            or supplemental.get("revision_order") != [CURRENT_VERSION_SHA]
        ):
            raise ValueError("supplemental replay must be the passing isolated S3 1.10 SHA matrix")
        supplemental_rows = supplemental.get("runs")
        if not isinstance(supplemental_rows, list) or len(supplemental_rows) != 1:
            raise ValueError("supplemental S3 1.10 run row is incomplete")
        row = supplemental_rows[0]
        if not isinstance(row, dict) or row.get("source_revision") != CURRENT_VERSION_SHA or row.get("status") != "PASS":
            raise ValueError("supplemental run does not prove the pinned S3 1.10 candidate")
        result = row.get("result")
        if not isinstance(result, dict):
            raise ValueError("supplemental validated executor report is missing")
        rows_by_sha[CURRENT_VERSION_SHA] = (
            result,
            supplemental_evidence_dir,
            "CURRENT_1_10_SEPARATE_RUN",
        )
        matrix_groups.append(
            {
                "group": "CURRENT_1_10_SEPARATE_RUN",
                "matrix_path": supplemental_matrix_path.resolve().relative_to(ROOT).as_posix(),
                "matrix_sha256": _sha256(supplemental_bytes),
                "matrix_bytes": len(supplemental_bytes),
                "revision_order": supplemental["revision_order"],
                "execution_order": supplemental["execution_order"],
            }
        )

    expected_complete = set(VERSION_SHAS.values()) if include_current else expected_shas
    if set(rows_by_sha) != expected_complete:
        raise ValueError("replay groups do not exactly match their pinned S3 version SHAs")

    common_protocol: dict[str, Any] | None = None
    common_host: dict[str, Any] | None = None
    common_tools: dict[str, Any] | None = None
    common_dataset_hashes: dict[str, str] | None = None
    common_output_hashes: dict[str, str] | None = None
    entries: list[dict[str, object]] = []

    version_shas = VERSION_SHAS if include_current else HISTORICAL_VERSION_SHAS
    for version, sha in version_shas.items():
        executor_result, version_evidence_dir, replay_group = rows_by_sha[sha]
        provenance = executor_result.get("provenance")
        execution = executor_result.get("execution")
        if not isinstance(provenance, dict) or not isinstance(execution, dict):
            raise ValueError(f"executor provenance/execution missing for {version}")
        if provenance.get("s3_commit") != sha or provenance.get("s3_worktree_clean") is not True:
            raise ValueError(f"executor did not verify the pinned clean S3 checkout for {version}")

        raw_path = version_evidence_dir / f"{sha}.json"
        if not raw_path.is_file():
            nested_raw_path = version_evidence_dir / sha / "native-workload-benchmark-v1.json"
            if nested_raw_path.is_file():
                raw_path = nested_raw_path
        if not raw_path.is_file():
            raise ValueError(f"raw result evidence is missing for {version}: {raw_path}")
        raw_result, raw_bytes = _read_json(raw_path)
        raw_hash = _sha256(raw_bytes)
        if raw_hash != provenance.get("raw_result_sha256"):
            raise ValueError(f"raw result SHA-256 mismatch for {version}")
        source = raw_result.get("source_revision")
        if not isinstance(source, dict) or (
            source.get("git_commit") != sha
            or source.get("git_tree") != provenance.get("s3_tree")
            or source.get("worktree_clean") is not True
        ):
            raise ValueError(f"raw result provenance mismatch for {version}")

        protocol = raw_result.get("protocol")
        host = raw_result.get("host")
        tools = raw_result.get("tools")
        if not isinstance(protocol, dict) or not isinstance(host, dict) or not isinstance(tools, dict):
            raise ValueError(f"protocol, host, or toolchain evidence missing for {version}")
        if common_protocol is None:
            common_protocol, common_host, common_tools = protocol, host, tools
        elif protocol != common_protocol or host != common_host or tools != common_tools:
            raise ValueError(f"cross-version host/protocol/toolchain mismatch at {version}")

        workloads = raw_result.get("workloads")
        if not isinstance(workloads, dict) or set(workloads) != set(WORKLOADS):
            raise ValueError(f"workload set mismatch for {version}")
        dataset_hashes: dict[str, str] = {}
        output_hashes: dict[str, str] = {}
        workload_summaries: dict[str, object] = {}
        for workload_id in WORKLOADS:
            workload = workloads[workload_id]
            if not isinstance(workload, dict) or workload.get("correctness") != "PASS_ALL_BUILDS":
                raise ValueError(f"correctness failed or missing: {version}/{workload_id}")
            dataset_hash = workload.get("dataset_sha256")
            hashes = workload.get("native_candidate_output_sha256")
            timing_protocol = workload.get("timing_protocol")
            timings = workload.get("timings")
            binaries = workload.get("binary_metrics")
            if not isinstance(dataset_hash, str) or not isinstance(hashes, dict):
                raise ValueError(f"dataset/output identity missing: {version}/{workload_id}")
            if not isinstance(timing_protocol, dict) or not isinstance(timings, dict) or not isinstance(binaries, dict):
                raise ValueError(f"timing/object data missing: {version}/{workload_id}")
            timing = timings.get("S3_O1_BASELINE")
            metrics = binaries.get("S3_O1_BASELINE")
            if not isinstance(timing, dict) or not isinstance(metrics, dict):
                raise ValueError(f"baseline O1 timing/object data missing: {version}/{workload_id}")
            if timing.get("sample_count") != timing_protocol.get("samples"):
                raise ValueError(f"sample count mismatch: {version}/{workload_id}")
            output_hash = hashes.get("S3_O1_BASELINE")
            if not isinstance(output_hash, str) or len(output_hash) != 64 or any(c not in "0123456789abcdef" for c in output_hash):
                raise ValueError(f"baseline output hash missing: {version}/{workload_id}")
            dataset_hashes[workload_id] = dataset_hash
            output_hashes[workload_id] = output_hash
            workload_summaries[workload_id] = {
                "correctness": "PASS_ALL_BUILDS",
                "dataset_sha256": dataset_hash,
                "baseline_o1_output_sha256": output_hash,
                "baseline_o1_sample_count": timing["sample_count"],
                "baseline_o1_median_ns_per_call": _positive_number(
                    timing.get("median_ns_per_call"), f"{version}/{workload_id} median"
                ),
                "baseline_o1_text_section_bytes": _positive_number(
                    metrics.get("text_section_bytes"), f"{version}/{workload_id} text"
                ),
                "baseline_o1_static_machine_instructions": _positive_number(
                    metrics.get("static_machine_instructions"), f"{version}/{workload_id} instruction count"
                ),
                "timing_protocol": timing_protocol,
            }

        if common_dataset_hashes is None:
            common_dataset_hashes = dataset_hashes
            common_output_hashes = output_hashes
        elif dataset_hashes != common_dataset_hashes or output_hashes != common_output_hashes:
            raise ValueError(f"cross-version dataset or observable output mismatch at {version}")

        artifacts = provenance.get("native_artifacts")
        if not isinstance(artifacts, list) or len(artifacts) != 31:
            raise ValueError(f"native artifact inventory incomplete for {version}")
        entries.append(
            {
                "s3_line": version,
                "s3_commit": sha,
                "s3_tree": provenance["s3_tree"],
                "replay_status": "REPLAYED",
                "replay_group": replay_group,
                "correctness": "PASS_ALL_BUILDS",
                "raw_result_path": raw_path.resolve().relative_to(ROOT).as_posix(),
                "raw_result_sha256": raw_hash,
                "raw_result_bytes": len(raw_bytes),
                "compiler_source_sha256": raw_result.get("compiler_source_sha256"),
                "native_artifact_count": len(artifacts),
                "native_artifacts": artifacts,
                "workloads": workload_summaries,
            }
        )

    if common_protocol is None or common_host is None or common_tools is None:
        raise ValueError("no validated replay rows")
    first_sha = next(iter(HISTORICAL_VERSION_SHAS.values()))
    timing_note = (
        "Host, workload inputs, build variants, and per-version timing protocol match, "
        "but versions ran in serial ascending-SHA groups without cross-version "
        "interleaving; report per-version medians descriptively, not as a causal delta."
    )
    if include_current:
        timing_note = (
            "S3 1.5-1.9 ran as the historical serial ascending-SHA group; S3 1.10 "
            "was replayed later as a separate single-SHA group. Host, workload inputs, "
            "build variants, and per-version timing protocol match, but groups were not "
            "cross-version interleaved; medians are descriptive only, not causal deltas."
        )
    lab_heads = sorted({result[0]["provenance"]["lab_head"] for result in rows_by_sha.values()})
    executor_hashes = sorted({result[0]["provenance"]["executor_sha256"] for result in rows_by_sha.values()})
    return {
        "schema_version": "1.0.0",
        "experiment_id": EXPERIMENT_ID,
        "report_kind": (
            "S3_CROSS_VERSION_REPLAY_COMPATIBILITY_INDEX"
            if include_current
            else "S3_HISTORICAL_CROSS_VERSION_REPLAY_INDEX"
        ),
        "status": "PASS",
        "coverage": "COMPLETE_1_5_TO_1_10" if include_current else "HISTORICAL_1_5_TO_1_9",
        "measurement_class": "CHARACTERIZATION_ONLY",
        "native_speedup_claim": False,
        "direct_cross_version_timing_delta_supported": False,
        "timing_comparability_note": timing_note,
        "static_object_metric_comparability": "SAME_SCHEMA_AND_EXTRACTION_PROTOCOL",
        "matrix_path": matrix_path.name,
        "matrix_sha256": _sha256(matrix_bytes),
        "matrix_bytes": len(matrix_bytes),
        "matrix_execution_order": "serial_groups_not_interleaved" if include_current else matrix.get("execution_order"),
        "matrix_groups": matrix_groups,
        "protocol_sha256": _sha256(json.dumps(common_protocol, sort_keys=True, separators=(",", ":")).encode()),
        "host": common_host,
        "toolchain": common_tools,
        "lab_head": rows_by_sha[first_sha][0]["provenance"]["lab_head"],
        "lab_heads": lab_heads,
        "executor_sha256": rows_by_sha[first_sha][0]["provenance"]["executor_sha256"],
        "executor_sha256_values": executor_hashes,
        "versions": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--evidence-dir", type=Path, required=True)
    parser.add_argument("--supplemental-matrix", type=Path)
    parser.add_argument("--supplemental-evidence-dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = build_index(
        args.matrix,
        args.evidence_dir,
        supplemental_matrix_path=args.supplemental_matrix,
        supplemental_evidence_dir=args.supplemental_evidence_dir,
    )
    encoded = (json.dumps(report, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    print(f"EXPERIMENT={EXPERIMENT_ID} STATUS={report['status']} VERSIONS={len(report['versions'])}")
    print(f"OUTPUT={args.output} SHA256={_sha256(encoded)} BYTES={len(encoded)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
