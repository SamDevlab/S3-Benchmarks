from __future__ import annotations

from tools.summarize_s3ir2_v2_checkpoint_history import summarize


STAGE_MAP = {
    "stages": {
        "03_PASS1_BINDINGS": {"required_cases": ["a", "b"]},
        "04_EXPRESSIONS_S1_S2": {"required_cases": ["c"]},
    }
}


def _checkpoint(
    candidate: str,
    source: str,
    binary: str,
    stage: str,
    case: str,
    gate: str,
    control_revision: int = 3,
) -> dict:
    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-checkpoint.v1",
        "candidate_git_sha": candidate,
        "candidate_source_sha256": source,
        "candidate_binary_sha256": binary,
        "control_revision": control_revision,
        "stage_id": stage,
        "case_id": case,
        "evidence_manifest": {
            "structural_status": "PASS",
            "native_provenance_status": "PASS",
            "semantic_conformance_status": "PASS" if gate == "PASS" else "FAIL",
            "determinism_status": "PASS",
            "qualification_gate": gate,
        },
    }


def test_history_uses_explicit_checkpoint_order() -> None:
    c1 = "a" * 40
    c2 = "0" * 40
    report = summarize(
        STAGE_MAP,
        [
            _checkpoint(c1, "b" * 64, "c" * 64, "03_PASS1_BINDINGS", "a", "PASS"),
            _checkpoint(c1, "b" * 64, "c" * 64, "03_PASS1_BINDINGS", "b", "FAIL"),
            _checkpoint(c2, "d" * 64, "e" * 64, "03_PASS1_BINDINGS", "a", "PASS"),
            _checkpoint(c2, "d" * 64, "e" * 64, "03_PASS1_BINDINGS", "b", "PASS"),
        ],
    )
    assert report["status"] == "PASS"
    assert [row["candidate_git_sha"] for row in report["timeline"]] == [c1, c2]
    assert report["timeline"][0]["stage_status"]["03_PASS1_BINDINGS"]["status"] == "BLOCKED"
    assert report["timeline"][1]["stage_status"]["03_PASS1_BINDINGS"]["status"] == "PASS_EVIDENCE_SET"
    assert "03_PASS1_BINDINGS:b" in report["timeline"][1]["newly_passing_cases"]


def test_history_reports_lost_passing_case_only_when_reobserved() -> None:
    c1 = "a" * 40
    c2 = "b" * 40
    report = summarize(
        STAGE_MAP,
        [
            _checkpoint(c1, "c" * 64, "d" * 64, "03_PASS1_BINDINGS", "a", "PASS"),
            _checkpoint(c2, "e" * 64, "f" * 64, "03_PASS1_BINDINGS", "a", "FAIL"),
        ],
    )
    assert report["timeline"][1]["lost_passing_cases"] == ["03_PASS1_BINDINGS:a"]
    assert report["timeline"][1]["not_reobserved_previous_pass_cases"] == []


def test_history_marks_missing_rerun_as_not_reobserved() -> None:
    c1 = "a" * 40
    c2 = "b" * 40
    report = summarize(
        STAGE_MAP,
        [
            _checkpoint(c1, "c" * 64, "d" * 64, "03_PASS1_BINDINGS", "a", "PASS"),
            _checkpoint(c2, "e" * 64, "f" * 64, "04_EXPRESSIONS_S1_S2", "c", "PASS"),
        ],
    )
    second = report["timeline"][1]
    assert second["lost_passing_cases"] == []
    assert second["not_reobserved_previous_pass_cases"] == ["03_PASS1_BINDINGS:a"]
    assert second["newly_passing_cases"] == ["04_EXPRESSIONS_S1_S2:c"]


def test_history_rejects_identity_drift_within_same_candidate() -> None:
    candidate = "a" * 40
    report = summarize(
        STAGE_MAP,
        [
            _checkpoint(candidate, "b" * 64, "c" * 64, "03_PASS1_BINDINGS", "a", "PASS"),
            _checkpoint(candidate, "d" * 64, "c" * 64, "03_PASS1_BINDINGS", "b", "PASS"),
        ],
    )
    assert report["status"] == "FAIL"
    assert any("changes candidate_source_sha256" in error for error in report["errors"])
