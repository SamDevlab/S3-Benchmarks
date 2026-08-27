from tools.triage_stage05_call_gate import triage


def test_z3_routes_to_strict_before_arrays() -> None:
    result = triage({
        "ZERO_ARG_Z_MASK": "3",
        "ONE_ARG_Z_MASK": "3",
        "TWO_ARG_Z_MASK": "3",
    })
    assert result["classification"] == "RUN_STRICT_CONFORMANCE_BEFORE_ARRAYS"
    assert result["arrays_unlocked"] is False


def test_strict_fail_uses_first_error_only() -> None:
    result = triage({
        "ONE_ARG_Z_MASK": "3",
        "STRICT_CONFORMANCE_STATUS": "FAIL",
        "STRICT_FIRST_ERROR": "missing mapped call argument for expected [1, 0, 3]",
    })
    assert result["classification"] == "STRICT_CALL_CONFORMANCE_MISMATCH"
    assert result["next_owner"] == "STRICT_ERRORS_0"


def test_strict_pass_with_z3_routes_to_completeness_predicate() -> None:
    result = triage({
        "ONE_ARG_Z_MASK": "3",
        "STRICT_CONFORMANCE_STATUS": "PASS",
    })
    assert result["classification"] == "CALL_SEMANTICS_PASS_S3_MASK_NOT_CLAIMED"
    assert result["next_owner"] == "STAGE05_S3_COMPLETENESS_PREDICATE"


def test_all_z7_plus_strict_pass_continues_internal_matrix_only() -> None:
    result = triage({
        "ZERO_ARG_Z_MASK": "7",
        "ONE_ARG_Z_MASK": "7",
        "TWO_ARG_Z_MASK": "7",
        "STRICT_CONFORMANCE_STATUS": "PASS",
    })
    assert result["classification"] == "INTERNAL_CALL_GATE_READY"
    assert result["arrays_unlocked"] is False


def test_any_z0_stops_broadening() -> None:
    result = triage({
        "ZERO_ARG_Z_MASK": "3",
        "ONE_ARG_Z_MASK": "0",
    })
    assert result["classification"] == "VALID_CALL_REGRESSION_OR_FAIL_CLOSED"
    assert result["next_owner"] == "FIRST_Z0_FIXTURE"
