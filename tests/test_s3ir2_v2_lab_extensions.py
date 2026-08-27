from __future__ import annotations

import json
from pathlib import Path

from tools.capture_s3ir2_v2_failure_bundle import capture
from tools.check_s3ir2_v2_determinism import check
from tools.classify_s3ir2_v2_failure import classify
from tools.ingest_s3ir2_v2 import ingest
from tools.render_s3ir2_v2_scorecard import build_scorecard


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


def test_scorecard_requires_semantics_and_determinism() -> None:
    report = ingest(STREAM)
    blocked = build_scorecard(report, conformance={"status": "PASS"})
    assert blocked["all_five_lanes_proven"] is True
    assert blocked["qualification_gate"] == "BLOCKED"
    passed = build_scorecard(
        report,
        conformance={"status": "PASS"},
        determinism={"status": "PASS"},
    )
    assert passed["qualification_gate"] == "PASS"


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


def test_failure_bundle_preserves_hashes(tmp_path: Path) -> None:
    source = tmp_path / "case.s3"
    stream = tmp_path / "case.s3ir2"
    conformance = tmp_path / "case.json"
    output = tmp_path / "bundle"
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    stream.write_text(STREAM, encoding="utf-8")
    conformance.write_text(json.dumps({"status": "FAIL", "errors": ["mismatch"]}), encoding="utf-8")
    manifest = capture(source, stream, conformance, output)
    assert manifest["conformance_status"] == "FAIL"
    assert manifest["minimization_status"] == "NOT_RUN"
    assert (output / "manifest.json").exists()
    assert (output / "ingest.json").exists()


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
