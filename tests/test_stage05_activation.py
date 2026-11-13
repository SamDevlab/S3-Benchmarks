from __future__ import annotations

from tools.check_stage05_activation import check


def _plan() -> dict:
    return {"activation_status": "PREPARED_NOT_ACTIVE"}


def _matrix() -> dict:
    return {"activation_status": "PREPARED_NOT_ACTIVE"}


def _control(stage: str) -> dict:
    return {
        "control_revision": 5,
        "active_stage": stage,
        "canonical_stage1_mutation_authorized": False,
        "self_emit_authorized": False,
        "stage2_authorized": False,
        "stage3_authorized": False,
        "t4_authorized": False,
    }


def test_stage05_guard_stays_inactive_during_stage04() -> None:
    report = check(_control("04_EXPRESSIONS_S1_S2"), _plan(), _matrix())
    assert report["status"] == "NOT_ACTIVE"
    assert report["next_action"] is None
    assert report["activation_authorized_by_this_tool"] is False


def test_stage05_guard_allows_fixture_validation_only_when_stage05_active() -> None:
    report = check(_control("05_CALLS_ARRAYS_S3"), _plan(), _matrix())
    assert report["status"] == "READY_TO_VALIDATE_AND_PIN_FIXTURES"
    assert report["next_action"] == "VALIDATE_PREPARED_FIXTURES_WITH_S3_REFERENCE"
    assert report["activation_authorized_by_this_tool"] is False


def test_stage05_guard_rejects_premature_self_emit_authorization() -> None:
    control = _control("05_CALLS_ARRAYS_S3")
    control["self_emit_authorized"] = True
    report = check(control, _plan(), _matrix())
    assert report["status"] == "INVALID_CONTROL_SNAPSHOT"
    assert "self_emit_authorized" in report["unexpected_authorizations"]


def test_stage05_guard_rejects_mutated_plan_state() -> None:
    plan = _plan()
    plan["activation_status"] = "ACTIVE"
    report = check(_control("05_CALLS_ARRAYS_S3"), plan, _matrix())
    assert report["status"] == "INVALID_CONTROL_SNAPSHOT"
