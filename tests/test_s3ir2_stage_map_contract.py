from __future__ import annotations

from tools.check_s3ir2_stage_map_contract import check


def test_stage_map_rejects_unknown_case() -> None:
    report = check({
        "stages": {
            "04_EXPRESSIONS_S1_S2": {
                "required_cases": ["does_not_exist"]
            }
        }
    })
    assert report["status"] == "FAIL"
    assert any("unknown corpus case" in error for error in report["errors"])


def test_stage04_current_mapping_has_no_forbidden_arithmetic_tokens() -> None:
    report = check({
        "stages": {
            "04_EXPRESSIONS_S1_S2": {
                "required_cases": [
                    "unary_negate_tryte",
                    "unary_invert_tryte",
                    "subtraction_lowering",
                    "tritwise_and",
                    "tritwise_or",
                    "relational_equal",
                    "relational_precedence_v06",
                    "mixed_expression_precedence",
                    "mutable_reassignment_example",
                ]
            }
        }
    })
    assert report["status"] == "PASS"


def test_stage_map_rejects_duplicate_required_case() -> None:
    report = check({
        "stages": {
            "03_PASS1_BINDINGS": {
                "required_cases": ["local_identity", "local_identity"]
            }
        }
    })
    assert report["status"] == "FAIL"
    assert any("duplicate required case" in error for error in report["errors"])
