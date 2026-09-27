from __future__ import annotations

from pathlib import Path

from tools.s3_110_cross_version_index import build_index


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/s3-1.10-memory-intelligence-lab"


def test_historical_cross_version_matrix_is_hash_checked_and_conservative() -> None:
    index = build_index(
        REPORT / "evidence/historical-replay-v1/multi-sha-result-v1.json",
        REPORT / "evidence/historical-replay-v1",
    )

    assert index["experiment_id"] == "EXP-S3-110-HIST-001"
    assert index["status"] == "PASS"
    assert index["measurement_class"] == "CHARACTERIZATION_ONLY"
    assert index["native_speedup_claim"] is False
    assert index["direct_cross_version_timing_delta_supported"] is False
    assert index["static_object_metric_comparability"] == "SAME_SCHEMA_AND_EXTRACTION_PROTOCOL"
    versions = index["versions"]
    assert [row["s3_line"] for row in versions] == ["1.5", "1.6", "1.7", "1.8", "1.9"]
    assert all(row["replay_status"] == "REPLAYED" for row in versions)
    assert all(row["correctness"] == "PASS_ALL_BUILDS" for row in versions)


def test_complete_matrix_records_separate_s3_110_replay_without_causal_claim() -> None:
    historical = REPORT / "evidence/historical-replay-v1"
    current = REPORT / "evidence/replay-1.10-candidate-v1"
    index = build_index(
        historical / "multi-sha-result-v1.json",
        historical,
        supplemental_matrix_path=current / "multi-sha-result-v1.json",
        supplemental_evidence_dir=current,
    )

    assert index["coverage"] == "COMPLETE_1_5_TO_1_10"
    assert index["report_kind"] == "S3_CROSS_VERSION_REPLAY_COMPATIBILITY_INDEX"
    assert index["measurement_class"] == "CHARACTERIZATION_ONLY"
    assert index["native_speedup_claim"] is False
    assert index["direct_cross_version_timing_delta_supported"] is False
    assert index["matrix_execution_order"] == "serial_groups_not_interleaved"
    assert len(index["matrix_groups"]) == 2
    assert [row["s3_line"] for row in index["versions"]] == [
        "1.5", "1.6", "1.7", "1.8", "1.9", "1.10"
    ]
    candidate = index["versions"][-1]
    assert candidate["s3_commit"] == "856bf0cd60c3da6ba701adec73c7858d063739a7"
    assert candidate["replay_group"] == "CURRENT_1_10_SEPARATE_RUN"
    assert candidate["correctness"] == "PASS_ALL_BUILDS"
    assert candidate["raw_result_sha256"]
    assert "separate single-SHA group" in index["timing_comparability_note"]
