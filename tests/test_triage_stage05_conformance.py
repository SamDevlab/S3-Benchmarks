from tools.triage_stage05_conformance import triage


def test_missing_call_record_maps_to_c_attachment() -> None:
    result = triage({"status": "FAIL", "errors": ["missing call record for expected instruction 3"]})
    assert result["first_blocker"] == "C_RECORD_ATTACHMENT"
    assert result["continue_broadening"] is False


def test_call_metadata_mismatch_maps_to_c_metadata() -> None:
    result = triage({"status": "FAIL", "errors": ["call semantic metadata mismatch for instruction 3"]})
    assert result["first_blocker"] == "C_METADATA"


def test_call_source_span_maps_to_c_source_span() -> None:
    result = triage({"status": "FAIL", "errors": ["call source identity mismatch for 'helper'"]})
    assert result["first_blocker"] == "C_SOURCE_SPAN"


def test_unmapped_call_argument_does_not_patch_a_first() -> None:
    result = triage({"status": "FAIL", "errors": ["cannot map call argument edge [3, 0, 9]"]})
    assert result["first_blocker"] == "VALUE_MAPPING_BEFORE_A"


def test_missing_mapped_call_argument_maps_to_a_edge() -> None:
    result = triage({"status": "FAIL", "errors": ["missing mapped call argument for expected [3, 0, 9]"]})
    assert result["first_blocker"] == "A_ARGUMENT_EDGE"


def test_pass_does_not_promote_by_itself() -> None:
    result = triage({"status": "PASS", "errors": []})
    assert result["status"] == "NO_MISMATCH"
    assert result["promotion_effect"] == "NONE_TRIAGE_ONLY"
