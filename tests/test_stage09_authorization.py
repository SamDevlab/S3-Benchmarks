from __future__ import annotations

from tools.check_stage09_authorization import check


def _control() -> dict:
    return {
        "control_revision": 9,
        "active_stage": "09_CANONICAL_INTEGRATION",
        "canonical_stage1_mutation_authorized": True,
        "self_emit_authorized": False,
        "stage2_authorized": False,
        "stage3_authorized": False,
        "t4_authorized": False,
    }


def _stage08() -> dict:
    return {
        "stage_id": "08_CANONICAL_SOURCE_INPUT",
        "status": "PASS",
        "canonical_mutation_authorized_by_this_tool": False,
    }


def test_stage09_authorizes_handoff_only_with_explicit_control_and_stage08_pass() -> None:
    report = check(_control(), _stage08())
    assert report["status"] == "AUTHORIZED_HANDOFF"
    assert report["canonical_mutation_performed_by_this_tool"] is False
    assert report["self_emit_authorized_by_this_tool"] is False


def test_stage09_blocks_when_control_authorization_false() -> None:
    control = _control()
    control["canonical_stage1_mutation_authorized"] = False
    report = check(control, _stage08())
    assert report["status"] == "NOT_AUTHORIZED"
    assert any("canonical_stage1_mutation_authorized" in error for error in report["errors"])


def test_stage09_blocks_before_live_stage09() -> None:
    control = _control()
    control["active_stage"] = "08_CANONICAL_SOURCE_INPUT"
    report = check(control, _stage08())
    assert report["status"] == "NOT_AUTHORIZED"


def test_stage09_blocks_without_stage08_pass() -> None:
    stage08 = _stage08()
    stage08["status"] = "BLOCKED"
    report = check(_control(), stage08)
    assert report["status"] == "NOT_AUTHORIZED"
    assert any("Stage08 evidence status" in error for error in report["errors"])


def test_stage09_blocks_if_self_emit_is_already_authorized() -> None:
    control = _control()
    control["self_emit_authorized"] = True
    report = check(control, _stage08())
    assert report["status"] == "NOT_AUTHORIZED"
    assert any("self_emit_authorized" in error for error in report["errors"])
