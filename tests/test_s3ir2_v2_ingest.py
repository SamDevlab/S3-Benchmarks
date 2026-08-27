from __future__ import annotations

from tools.ingest_s3ir2_v2 import ingest


VALID = """\
S3IR2 2
F 0 1 0 4 0 1
B 0 0 0 2 1
V 0 0 3 3 10 1 0 -1
V 1 0 4 3 20 1 0 -1
I 0 0 0 0 1 1 0 -1 7
R 0 0 0
I 1 0 0 1 23 0 1 -1 -1
O 1 0 0
T 1 1 -1 -1 -1 -1 0
Z 31
"""


def test_complete_stream_is_structurally_ready_but_not_semantic_pass() -> None:
    report = ingest(VALID, source_sha256="a" * 64)
    assert report["structural_status"] == "PASS"
    assert report["declared_complete"] is True
    assert report["completeness_mask"] == 31
    assert report["bootstrap_gate"] == "CANDIDATE_STREAM_READY_FOR_STRICT_CONFORMANCE"
    assert report["semantic_conformance_status"] == "NOT_EVALUATED_USE_S3_CONFORMANCE_GATE"
    assert report["promotion_effect"] == "NONE_CONSUMER_ONLY"
    assert all(value == "PASS_DECLARED" for value in report["lanes"].values())


def test_incomplete_mask_stays_blocked_without_becoming_structural_failure() -> None:
    report = ingest(VALID.replace("Z 31", "Z 3"))
    assert report["structural_status"] == "PASS"
    assert report["declared_complete"] is False
    assert report["bootstrap_gate"] == "BLOCKED"
    assert report["lanes"]["S1_typed_values_and_bindings"] == "PASS_DECLARED"
    assert report["lanes"]["S2_instruction_def_use"] == "PASS_DECLARED"
    assert report["lanes"]["S3_call_dataflow"] == "BLOCKED"


def test_unknown_value_reference_is_structural_failure() -> None:
    broken = VALID.replace("O 1 0 0", "O 1 0 99")
    report = ingest(broken)
    assert report["structural_status"] == "FAIL"
    assert report["bootstrap_gate"] == "BLOCKED"
    assert any("unknown value 99" in error for error in report["errors"])
