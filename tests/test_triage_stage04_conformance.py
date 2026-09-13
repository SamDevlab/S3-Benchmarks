from __future__ import annotations

from tools.triage_stage04_conformance import triage


def test_pass_report_has_no_blocker() -> None:
    result = triage({"status": "PASS", "errors": []})
    assert result["status"] == "NO_MISMATCH"
    assert result["first_blocker"] is None
    assert result["promotion_effect"] == "NONE_TRIAGE_ONLY"


def test_instruction_shape_maps_to_s2() -> None:
    result = triage(
        {
            "status": "FAIL",
            "errors": ["instruction 3 semantic shape mismatch"],
        }
    )
    assert result["first_blocker"] == "INSTRUCTION_SHAPE"
    assert result["likely_lane"] == "S2"
    assert result["stage04_actionable"] is True


def test_missing_local_binding_maps_to_s1() -> None:
    result = triage(
        {
            "status": "FAIL",
            "errors": ["missing local binding 'value' in function 0"],
        }
    )
    assert result["first_blocker"] == "LOCAL_BINDING"
    assert result["likely_lane"] == "S1"
    assert "local-binding V row" in result["repair_action"]


def test_result_edge_mismatch_maps_to_s2() -> None:
    result = triage(
        {
            "status": "FAIL",
            "errors": ["result edge count mismatch for instruction 4"],
        }
    )
    assert result["first_blocker"] == "RESULT_EDGE_COUNT"
    assert result["likely_lane"] == "S2"


def test_operand_edge_mismatch_maps_to_s2() -> None:
    result = triage(
        {
            "status": "FAIL",
            "errors": ["missing mapped operand edge for expected [4, 0, 7]"],
        }
    )
    assert result["first_blocker"] == "OPERAND_EDGE"
    assert result["likely_lane"] == "S2"


def test_general_call_mismatch_is_not_stage04_actionable() -> None:
    result = triage(
        {
            "status": "FAIL",
            "errors": ["missing call record for expected instruction 3"],
        }
    )
    assert result["first_blocker"] == "CALL_RECORD"
    assert result["likely_lane"] == "S3"
    assert result["stage04_actionable"] is False


def test_unknown_error_stays_fail_closed() -> None:
    result = triage(
        {
            "status": "FAIL",
            "errors": ["some new verifier invariant failed"],
        }
    )
    assert result["first_blocker"] == "UNKNOWN_STRICT_MISMATCH"
    assert result["stage04_actionable"] is False


def test_fail_without_errors_requires_verifier_detail() -> None:
    result = triage({"status": "FAIL", "errors": []})
    assert result["status"] == "BLOCKED_NO_ERROR_DETAIL"
    assert result["first_blocker"] == "MISSING_VERIFIER_DETAIL"
