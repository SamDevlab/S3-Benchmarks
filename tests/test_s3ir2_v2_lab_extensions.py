from __future__ import annotations

import json
from pathlib import Path

from tools.capture_s3ir2_v2_failure_bundle import capture
from tools.check_s3ir2_v2_determinism import check
from tools.classify_s3ir2_v2_failure import classify
from tools.ingest_s3ir2_v2 import ingest
from tools.render_s3ir2_v2_native_metadata import render
from tools.render_s3ir2_v2_scorecard import build_scorecard
from tools.validate_s3ir2_v2_native_provenance import validate


STREAM = """\
S3IR2 2
F 0 1 0 4 0 1
B 0 0 0 1 0
V 0 0 3 3 0 1 0 -1
I 0 0 0 0 23 0 1 -1 -1
O 0 0 0
T 0 1 -1 -1 -1 -1 0
Z 31
"""


def test_scorecard_does_not_promote_declared_bits_without_conformance() -> None:
    report = ingest(STREAM)
    card = build_scorecard(report)
    assert card["qualification_gate"] == "BLOCKED"
    assert card["dimensions"]["S1_typed_values_and_bindings"]["declared"] == "PASS_DECLARED"
    assert card["dimensions"]["S1_typed_values_and_bindings"]["proven"] == "BLOCKED"
    assert card["single_numeric_score"] is None


def test_scorecard_requires_semantics_determinism_and_native_provenance() -> None:
    report = ingest(STREAM)
    semantic_only = build_scorecard(report, conformance={"status": "PASS"})
    assert semantic_only["all_five_lanes_proven"] is True
    assert semantic_only["qualification_gate"] == "BLOCKED"

    no_native = build_scorecard(
        report,
        conformance={"status": "PASS"},
        determinism={"status": "PASS"},
    )
    assert no_native["qualification_gate"] == "BLOCKED"
    assert no_native["native_provenance_status"] == "NOT_EVALUATED"

    passed = build_scorecard(
        report,
        conformance={"status": "PASS"},
        determinism={"status": "PASS"},
        native_provenance={"status": "PASS"},
    )
    assert passed["qualification_gate"] == "PASS"
    assert passed["native_candidate_provenance_proven"] is True


def test_exact_stream_determinism(tmp_path: Path) -> None:
    first = tmp_path / "a.s3ir2"
    second = tmp_path / "b.s3ir2"
    first.write_text(STREAM, encoding="utf-8")
    second.write_text(STREAM, encoding="utf-8")
    report = check([first, second])
    assert report["status"] == "PASS"
    second.write_text(STREAM.replace("Z 31", "Z 15"), encoding="utf-8")
    report = check([first, second])
    assert report["status"] == "FAIL"


def _native_report(
    output: Path,
    *,
    candidate_source: Path,
    candidate_binary: Path,
    fixture: Path,
    stream: Path,
) -> Path:
    metadata = render(
        candidate_git_sha="a" * 40,
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=fixture,
        stream=stream,
        control_revision=3,
        python_version="3.14.4",
        cc_path="/usr/bin/cc",
        build_exit_code=0,
        run_status="PASS",
        run_exit_code=0,
    )
    report = validate(
        metadata,
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=fixture,
        stream=stream,
    )
    assert report["status"] == "PASS"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output


def test_failure_bundle_preserves_hashes_without_native_context(tmp_path: Path) -> None:
    source = tmp_path / "case.s3"
    stream = tmp_path / "case.s3ir2"
    conformance = tmp_path / "case.json"
    output = tmp_path / "bundle"
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    stream.write_text(STREAM, encoding="utf-8")
    conformance.write_text(json.dumps({"status": "FAIL", "errors": ["mismatch"]}), encoding="utf-8")
    manifest = capture(source, stream, conformance, output)
    assert manifest["conformance_status"] == "FAIL"
    assert manifest["candidate_identity_status"] == "NOT_SUPPLIED"
    assert manifest["minimization_status"] == "NOT_RUN"
    assert (output / "manifest.json").exists()
    assert (output / "ingest.json").exists()


def test_failure_bundle_binds_matching_native_candidate(tmp_path: Path) -> None:
    candidate_source = tmp_path / "candidate-source.s3"
    candidate_binary = tmp_path / "candidate.bin"
    source = tmp_path / "case.s3"
    stream = tmp_path / "case.s3ir2"
    conformance = tmp_path / "conformance.json"
    candidate_source.write_text("fn compiler() -> i64:\n    return 0\n", encoding="utf-8")
    candidate_binary.write_bytes(b"native-stage1")
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    stream.write_text(STREAM, encoding="utf-8")
    conformance.write_text(json.dumps({"status": "FAIL", "errors": ["mismatch"]}), encoding="utf-8")
    native = _native_report(
        tmp_path / "native.json",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture=source,
        stream=stream,
    )
    manifest = capture(
        source,
        stream,
        conformance,
        tmp_path / "bundle",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        native_provenance=native,
    )
    assert manifest["candidate_identity_status"] == "PASS"
    assert manifest["candidate_identity_errors"] == []
    assert manifest["candidate_identity"]["candidate_git_sha"] == "a" * 40


def test_failure_bundle_detects_binary_identity_mismatch(tmp_path: Path) -> None:
    candidate_source = tmp_path / "candidate-source.s3"
    proven_binary = tmp_path / "proven.bin"
    wrong_binary = tmp_path / "wrong.bin"
    source = tmp_path / "case.s3"
    stream = tmp_path / "case.s3ir2"
    conformance = tmp_path / "conformance.json"
    candidate_source.write_text("fn compiler() -> i64:\n    return 0\n", encoding="utf-8")
    proven_binary.write_bytes(b"native-stage1-A")
    wrong_binary.write_bytes(b"native-stage1-B")
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    stream.write_text(STREAM, encoding="utf-8")
    conformance.write_text(json.dumps({"status": "FAIL", "errors": ["mismatch"]}), encoding="utf-8")
    native = _native_report(
        tmp_path / "native.json",
        candidate_source=candidate_source,
        candidate_binary=proven_binary,
        fixture=source,
        stream=stream,
    )
    manifest = capture(
        source,
        stream,
        conformance,
        tmp_path / "bundle",
        candidate_source=candidate_source,
        candidate_binary=wrong_binary,
        native_provenance=native,
    )
    assert manifest["candidate_identity_status"] == "FAIL"
    assert any("binary SHA differs" in error for error in manifest["candidate_identity_errors"])


def test_failure_triage_points_to_call_lane() -> None:
    report = classify({
        "status": "FAIL",
        "errors": [
            "call 7 argument count mismatch",
            "callee function identity mismatch",
        ],
    })
    assert report["primary_lane"] == "S3_call_dataflow"
    assert report["scores"]["S3_call_dataflow"] >= 2
