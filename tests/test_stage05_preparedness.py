from __future__ import annotations

from tools.audit_stage05_preparedness import audit


def _stage_map() -> dict:
    return {
        "stages": {
            "05_CALLS_ARRAYS_S3": {
                "required_cases": ["parameter_ordinal_0", "nested_calls"]
            }
        }
    }


def _plan() -> dict:
    return {
        "activation_status": "PREPARED_NOT_ACTIVE",
        "prepared_cases": {
            "zero_arg_call": {"source": "fn main() -> i64:\n    return 0\n"}
        },
        "negative_cases_to_pin_on_activation": {
            "unresolved_callee_fail_closed": {"source_shape": "missing()"}
        },
    }


def _matrix() -> dict:
    return {
        "activation_status": "PREPARED_NOT_ACTIVE",
        "capabilities": {
            "existing": {
                "fixture_status": "PINNED_EXISTING_CORPUS",
                "fixtures": ["nested_calls"],
            },
            "prepared": {
                "fixture_status": "PREPARED_NOT_PINNED",
                "fixtures": ["zero_arg_call"],
            },
            "negative": {
                "fixture_status": "NEGATIVE_CASE_NOT_YET_PINNED",
                "fixtures": ["unresolved_callee_fail_closed"],
            },
        },
        "capacity_policy": {
            "historical_call_pool_is_provenance_only": True,
            "blind_reuse_of_736_746_for_new_source": False,
        },
    }


def test_stage05_preparedness_passes_without_activation() -> None:
    report = audit(_stage_map(), _plan(), _matrix())
    assert report["status"] == "PASS_PREPARED_NOT_ACTIVE"
    assert report["activation_authorized"] is False
    assert report["prepared_cases_leaked_into_active_map"] == []


def test_stage05_preparedness_rejects_prepared_fixture_leak() -> None:
    stage_map = _stage_map()
    stage_map["stages"]["05_CALLS_ARRAYS_S3"]["required_cases"].append("zero_arg_call")
    report = audit(stage_map, _plan(), _matrix())
    assert report["status"] == "FAIL"
    assert report["prepared_cases_leaked_into_active_map"] == ["zero_arg_call"]


def test_stage05_preparedness_rejects_historical_capacity_promotion() -> None:
    matrix = _matrix()
    matrix["capacity_policy"]["blind_reuse_of_736_746_for_new_source"] = True
    report = audit(_stage_map(), _plan(), matrix)
    assert report["status"] == "FAIL"
    assert any("736/746" in error for error in report["errors"])


def test_stage05_preparedness_rejects_unknown_fixture_reference() -> None:
    matrix = _matrix()
    matrix["capabilities"]["bad"] = {
        "fixture_status": "PREPARED_NOT_PINNED",
        "fixtures": ["does_not_exist"],
    }
    report = audit(_stage_map(), _plan(), matrix)
    assert report["status"] == "FAIL"
    assert any("unknown Stage05 fixture" in error for error in report["errors"])
