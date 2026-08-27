from __future__ import annotations

from tools.check_prepared_stage_activation import check


def _control(active: str) -> dict:
    return {
        "control_revision": 5,
        "active_stage": active,
        "emergency_stop": False,
        "canonical_stage1_mutation_authorized": False,
        "self_emit_authorized": False,
        "stage2_authorized": False,
        "stage3_authorized": False,
        "t4_authorized": False,
    }


def _plan(stage: str) -> dict:
    return {"stage_id": stage, "activation_status": "PREPARED_NOT_ACTIVE"}


def test_stage06_plan_remains_inactive_during_stage04() -> None:
    report = check(_control("04_EXPRESSIONS_S1_S2"), _plan("06_CONTROL_FLOW_S4"))
    assert report["status"] == "NOT_ACTIVE"
    assert report["activation_authorized_by_this_tool"] is False


def test_stage07_becomes_ready_only_when_control_selects_it() -> None:
    report = check(_control("07_SERIALIZATION_S5"), _plan("07_SERIALIZATION_S5"))
    assert report["status"] == "READY_TO_VALIDATE_PREPARED_STAGE"
    assert report["next_action"] == "VALIDATE_PREPARED_STAGE_INPUTS"


def test_guard_rejects_unexpected_self_emit_authorization() -> None:
    control = _control("06_CONTROL_FLOW_S4")
    control["self_emit_authorized"] = True
    report = check(control, _plan("06_CONTROL_FLOW_S4"))
    assert report["status"] == "INVALID_CONTROL_SNAPSHOT"
    assert "self_emit_authorized" in report["unexpected_authorizations"]


def test_guard_rejects_non_prepared_plan() -> None:
    plan = _plan("05_CALLS_ARRAYS_S3")
    plan["activation_status"] = "ACTIVE"
    report = check(_control("05_CALLS_ARRAYS_S3"), plan)
    assert report["status"] == "INVALID_CONTROL_SNAPSHOT"


def test_guard_rejects_unknown_stage() -> None:
    report = check(_control("04_EXPRESSIONS_S1_S2"), _plan("99_UNKNOWN"))
    assert report["status"] == "INVALID_CONTROL_SNAPSHOT"
    assert any("unsupported prepared stage" in error for error in report["errors"])
