from __future__ import annotations

import hashlib

import pytest

from tools.s3_18_lab import (
    ROOT,
    _safe_repo_path,
    _sha,
    _validate_result_shape,
    build_snapshot,
    validate_snapshot,
)


def test_text_artifact_hash_is_line_ending_independent() -> None:
    assert _sha(b"first\r\nsecond\r\n") == _sha(b"first\nsecond\n")


def test_snapshot_is_deterministic_and_artifacts_are_hash_pinned() -> None:
    first = build_snapshot()
    second = build_snapshot()
    assert first == second

    manifest, results, cross_version = first
    assert len(manifest["evidence_artifacts"]) == 9
    candidate_head = manifest["repositories"]["s3"]["candidate_head"]
    assert results["provenance"]["s3_candidate_head"] == candidate_head
    assert all(item["s3_head"] == candidate_head for item in manifest["evidence_artifacts"])
    assert {item["id"] for item in results["research_questions"]} == {
        f"RQ{index}" for index in range(1, 11)
    }
    assert len(results["hypotheses"]) == 10
    experiment_ids = {item["experiment_id"] for item in results["experiments"]}
    assert all(
        experiment_id in experiment_ids
        for item in results["hypotheses"]
        for experiment_id in item["experiment_ids"]
    )
    assert all(item["experiment_id"] in experiment_ids for item in results["negative_results"])
    for item in manifest["evidence_artifacts"]:
        artifact = ROOT / item["path"]
        assert hashlib.sha256(artifact.read_bytes()).hexdigest() == item["sha256"]
    assert cross_version["direct_delta_supported"] is False
    assert results["default_policy"] == {"instruction_budget": "PER_INSTRUCTION", "changed": False}
    assert results["strict_fp_preserved"] is True
    assert results["runtime_performance_claims"] is False


def test_checked_in_snapshot_matches_current_inputs() -> None:
    summary = validate_snapshot()
    assert summary == {
        "artifact_count": 9,
        "experiment_count": 6,
        "research_question_count": 10,
        "cross_version_delta_supported": False,
    }


def test_artifact_path_rejects_traversal_and_windows_separators() -> None:
    with pytest.raises(ValueError, match="repository-relative"):
        _safe_repo_path("../outside.json")
    with pytest.raises(ValueError, match="repository-relative"):
        _safe_repo_path(r"evidence\outside.json")


def test_result_shape_rejects_default_policy_promotion() -> None:
    _, results, _ = build_snapshot()
    results["default_policy"]["instruction_budget"] = "EXACT"
    with pytest.raises(ValueError, match="PER_INSTRUCTION default"):
        _validate_result_shape(results)


def test_result_shape_rejects_unlinked_negative_evidence() -> None:
    _, results, _ = build_snapshot()
    results["negative_results"][0]["experiment_id"] = "EXP-S3-18-MISSING-001"
    with pytest.raises(ValueError, match="unknown experiment"):
        _validate_result_shape(results)


def test_result_shape_rejects_unqualified_hypothesis_status() -> None:
    _, results, _ = build_snapshot()
    results["hypotheses"][0]["status"] = "QUALIFIED"
    with pytest.raises(ValueError, match="invalid ID, RQ, status, or statement"):
        _validate_result_shape(results)
