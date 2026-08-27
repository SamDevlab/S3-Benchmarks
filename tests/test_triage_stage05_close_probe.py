from tools.triage_stage05_close_probe import triage


def test_classifies_special_open_legacy_dispatch_first_setter() -> None:
    result = triage({
        "SPECIAL_OPEN_ACTIVE": "-1",
        "BEFORE_SPECIAL_OPEN_PARSE_OK": "-1",
        "AFTER_SPECIAL_OPEN_PARSE_OK": "0",
        "ARGUMENT_PARSE_STARTED": "0",
        "Z_MASK": "0",
    })
    assert result["classification"] == "SYNTHETIC_CALL_OPEN_KIND_FALLS_THROUGH_LEGACY_OPERAND_DISPATCH"
    assert result["next_owner"] == "LEGACY_OPERAND_DISPATCH_SPECIAL_OPEN_GUARD"
    assert result["continue_broadening"] is False


def test_classifies_argument_stop_before_close() -> None:
    result = triage({
        "BEFORE_CLOSE_PARSE_OK": "0",
        "AFTER_CLOSE_PARSE_OK": "0",
        "Z_MASK": "0",
    })
    assert result["classification"] == "ARGUMENT_STOP_OR_TOKEN_BEFORE_RIGHT_PAREN"
    assert result["next_owner"] == "ARGUMENT_STOP_OR_TOKEN_BEFORE_RIGHT_PAREN"
    assert result["continue_broadening"] is False


def test_classifies_flip_inside_close() -> None:
    result = triage({
        "BEFORE_CLOSE_PARSE_OK": "-1",
        "AFTER_CLOSE_PARSE_OK": "0",
        "Z_MASK": "0",
    })
    assert result["classification"] == "RIGHT_PAREN_CALL_CLOSE"
    assert result["next_owner"] == "CURRENT_CODE_EQ_2_CALL_CLOSE"
    assert result["continue_broadening"] is False


def test_classifies_post_parse_when_close_valid_but_z0() -> None:
    result = triage({
        "BEFORE_CLOSE_PARSE_OK": "-1",
        "AFTER_CLOSE_PARSE_OK": "-1",
        "Z_MASK": "0",
    })
    assert result["classification"] == "POST_PARSE_FINALIZATION_OR_COMPLETENESS"
    assert result["next_owner"] == "STRICT_STAGE05_CONFORMANCE_FIRST_MISMATCH"


def test_z7_still_requires_strict_conformance() -> None:
    result = triage({
        "BEFORE_CLOSE_PARSE_OK": "-1",
        "AFTER_CLOSE_PARSE_OK": "-1",
        "Z_MASK": "7",
    })
    assert result["classification"] == "PARSER_CLOSE_VALID_STAGE05_MASK_READY"
    assert result["next_owner"] == "STRICT_STAGE05_CONFORMANCE"
    assert result["promotion_effect"] == "NONE_TRIAGE_ONLY"


def test_incomplete_evidence_blocks_repair_selection() -> None:
    result = triage({"BEFORE_CLOSE_PARSE_OK": "-1"})
    assert result["classification"] == "INSUFFICIENT_PARSER_PROBE"
    assert result["continue_broadening"] is False
