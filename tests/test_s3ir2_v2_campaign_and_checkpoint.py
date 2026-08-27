from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.aggregate_s3ir2_v2_campaign import aggregate
from tools.record_s3ir2_v2_checkpoint import record


STAGE_MAP = {
    "stages": {
        "03_PASS1_BINDINGS": {
            "required_cases": ["a", "b"],
            "gate_focus": ["bindings"],
        },
        "07_SERIALIZATION_S5": {
            "required_cases": ["a", "b"],
            "gate_focus": ["determinism"],
        },
    }
}

CANDIDATE_SHA = "a" * 40
SOURCE_SHA = "b" * 64
BINARY_SHA = "c" * 64


def _manifest(
    *,
    native: str = "PASS",
    semantic: str = "PASS",
    deterministic: str = "PASS",
) -> dict[str, object]:
    qualification = (
        "PASS"
        if native == "PASS" and semantic == "PASS" and deterministic == "PASS"
        else "BLOCKED"
    )
    return {
        "candidate_git_sha": CANDIDATE_SHA,
        "candidate_source_sha256": SOURCE_SHA,
        "candidate_binary_sha256": BINARY_SHA,
        "control_revision": 3,
        "structural_status": "PASS",
        "native_provenance_status": native,
        "semantic_conformance_status": semantic,
        "determinism_status": deterministic,
        "qualification_gate": qualification,
    }


def test_campaign_requires_every_mapped_case() -> None:
    report = aggregate(STAGE_MAP, {"a": _manifest()})
    assert report["stages"]["03_PASS1_BINDINGS"]["status"] == "INCOMPLETE_EVIDENCE"
    assert report["stages"]["03_PASS1_BINDINGS"]["missing_cases"] == ["b"]
    assert report["full_v2_fixture_campaign"] == "BLOCKED"


def test_campaign_requires_native_provenance() -> None:
    report = aggregate(STAGE_MAP, {"a": _manifest(), "b": _manifest(native="NOT_EVALUATED")})
    assert report["stages"]["03_PASS1_BINDINGS"]["status"] == "NATIVE_PROVENANCE_BLOCKED"
    assert report["stages"]["03_PASS1_BINDINGS"]["native_provenance_fail_cases"] == ["b"]
    assert report["full_v2_fixture_campaign"] == "BLOCKED"


def test_stage07_requires_determinism() -> None:
    report = aggregate(
        STAGE_MAP,
        {
            "a": _manifest(),
            "b": _manifest(deterministic="NOT_EVALUATED"),
        },
    )
    assert report["stages"]["03_PASS1_BINDINGS"]["status"] == "PASS_EVIDENCE_SET"
    assert report["stages"]["07_SERIALIZATION_S5"]["status"] == "DETERMINISM_BLOCKED"


def test_full_campaign_passes_only_with_all_proofs() -> None:
    report = aggregate(STAGE_MAP, {"a": _manifest(), "b": _manifest()})
    assert report["stages"]["03_PASS1_BINDINGS"]["status"] == "PASS_EVIDENCE_SET"
    assert report["stages"]["07_SERIALIZATION_S5"]["status"] == "PASS_EVIDENCE_SET"
    assert report["full_v2_fixture_campaign"] == "PASS"


def test_checkpoint_is_immutable_and_hash_bound(tmp_path: Path) -> None:
    evidence = tmp_path / "evidence-manifest.json"
    evidence.write_text(json.dumps(_manifest()) + "\n", encoding="utf-8")
    output = tmp_path / "candidate" / "case.json"
    checkpoint = record(
        candidate_sha=CANDIDATE_SHA,
        candidate_source_sha256=SOURCE_SHA,
        case_id="local_identity",
        stage_id="03_PASS1_BINDINGS",
        evidence_manifest=evidence,
        output=output,
    )
    assert checkpoint["candidate_git_sha"] == CANDIDATE_SHA
    assert checkpoint["candidate_source_sha256"] == SOURCE_SHA
    assert checkpoint["candidate_binary_sha256"] == BINARY_SHA
    assert checkpoint["immutable"] is True
    assert output.exists()
    with pytest.raises(FileExistsError):
        record(
            candidate_sha=CANDIDATE_SHA,
            candidate_source_sha256=SOURCE_SHA,
            case_id="local_identity",
            stage_id="03_PASS1_BINDINGS",
            evidence_manifest=evidence,
            output=output,
        )


def test_checkpoint_rejects_identity_relabeling(tmp_path: Path) -> None:
    evidence = tmp_path / "evidence-manifest.json"
    evidence.write_text(json.dumps(_manifest()) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="candidate_sha does not match"):
        record(
            candidate_sha="d" * 40,
            candidate_source_sha256=SOURCE_SHA,
            case_id="local_identity",
            stage_id="03_PASS1_BINDINGS",
            evidence_manifest=evidence,
            output=tmp_path / "wrong.json",
        )


def test_checkpoint_rejects_malformed_hashes(tmp_path: Path) -> None:
    evidence = tmp_path / "evidence-manifest.json"
    evidence.write_text(json.dumps(_manifest()) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="candidate_sha"):
        record(
            candidate_sha="abc123",
            candidate_source_sha256=SOURCE_SHA,
            case_id="local_identity",
            stage_id="03_PASS1_BINDINGS",
            evidence_manifest=evidence,
            output=tmp_path / "bad.json",
        )
