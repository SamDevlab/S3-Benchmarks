from __future__ import annotations

from tools.check_stage11_action_authorization import check


CONTRACT = {
    "actions": {
        "SELF_EMIT": {
            "authorization_field": "self_emit_authorized",
            "required_prior_pass": ["s1", "s2", "s3", "s4", "s5", "general_emitter", "canonical_stage1_emission"],
        },
        "STAGE2": {
            "authorization_field": "stage2_authorized",
            "required_prior_pass": ["self_emit"],
        },
        "STAGE3": {
            "authorization_field": "stage3_authorized",
            "required_prior_pass": ["stage2"],
        },
        "T4": {
            "authorization_field": "t4_authorized",
            "required_prior_pass": ["self_emit", "stage2", "stage3", "stage2_stage3_equivalence"],
        },
    }
}


def _control(**overrides: bool | str | int) -> dict:
    value = {
        "control_revision": 11,
        "active_stage": "11_SELF_EMIT_BOOTSTRAP",
        "self_emit_authorized": False,
        "stage2_authorized": False,
        "stage3_authorized": False,
        "t4_authorized": False,
    }
    value.update(overrides)
    return value


def test_self_emit_requires_own_authorization_and_prior_closure() -> None:
    gates = {field: "PASS" for field in CONTRACT["actions"]["SELF_EMIT"]["required_prior_pass"]}
    report = check(CONTRACT, _control(self_emit_authorized=True), {"gates": gates}, "SELF_EMIT")
    assert report["status"] == "AUTHORIZED_HANDOFF"
    assert report["action_performed_by_this_tool"] is False


def test_self_emit_does_not_infer_authorization_from_prior_pass() -> None:
    gates = {field: "PASS" for field in CONTRACT["actions"]["SELF_EMIT"]["required_prior_pass"]}
    report = check(CONTRACT, _control(), {"gates": gates}, "SELF_EMIT")
    assert report["status"] == "NOT_AUTHORIZED"


def test_stage2_requires_real_self_emit_pass() -> None:
    report = check(CONTRACT, _control(stage2_authorized=True), {"gates": {"self_emit": "BLOCKED"}}, "STAGE2")
    assert report["status"] == "NOT_AUTHORIZED"
    assert report["missing_prior_pass"] == ["self_emit"]


def test_stage3_requires_stage2_pass() -> None:
    report = check(CONTRACT, _control(stage3_authorized=True), {"gates": {"stage2": "PASS"}}, "STAGE3")
    assert report["status"] == "AUTHORIZED_HANDOFF"


def test_t4_requires_equivalence_and_all_bootstrap_artifacts() -> None:
    gates = {"self_emit": "PASS", "stage2": "PASS", "stage3": "PASS", "stage2_stage3_equivalence": "BLOCKED"}
    report = check(CONTRACT, _control(t4_authorized=True), {"gates": gates}, "T4")
    assert report["status"] == "NOT_AUTHORIZED"
    assert report["missing_prior_pass"] == ["stage2_stage3_equivalence"]


def test_action_blocks_outside_stage11_even_if_bit_true() -> None:
    control = _control(self_emit_authorized=True)
    control["active_stage"] = "10_GENERAL_EMITTER"
    gates = {field: "PASS" for field in CONTRACT["actions"]["SELF_EMIT"]["required_prior_pass"]}
    report = check(CONTRACT, control, {"gates": gates}, "SELF_EMIT")
    assert report["status"] == "NOT_AUTHORIZED"
