from __future__ import annotations

from tools.audit_stage04_fixture_coverage import audit


def test_stage04_fixture_audit_reports_missing_and_partial() -> None:
    report = audit({
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "capabilities": {
            "literal": {"fixture_status": "PINNED", "fixtures": ["wide_literal_positive"]},
            "precedence": {"fixture_status": "FIXTURE_NOT_YET_PINNED", "fixtures": []},
            "comparison": {"fixture_status": "PARTIAL_PINNED", "fixtures": ["while_counter"]},
            "unsupported_multiply": {"fixture_status": "NOT_APPLICABLE_BY_LANGUAGE_CONTRACT", "fixtures": []},
        },
    })
    assert report["status"] == "INCOMPLETE_FIXTURE_COVERAGE"
    assert report["pinned_count"] == 1
    assert report["missing_capabilities"] == ["precedence"]
    assert report["partial_capabilities"] == ["comparison"]
    assert report["not_applicable_capabilities"] == ["unsupported_multiply"]
    assert report["invalid_count"] == 0


def test_stage04_fixture_audit_passes_with_all_applicable_pinned() -> None:
    report = audit({
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "capabilities": {
            "literal": {"fixture_status": "PINNED", "fixtures": ["a"]},
            "precedence": {"fixture_status": "PINNED", "fixtures": ["b"]},
            "unsupported_multiply": {"fixture_status": "NOT_APPLICABLE_BY_LANGUAGE_CONTRACT", "fixtures": []},
        },
    })
    assert report["status"] == "PASS"
    assert report["missing_count"] == 0
    assert report["partial_count"] == 0
    assert report["not_applicable_count"] == 1
    assert report["invalid_count"] == 0


def test_stage04_fixture_audit_rejects_not_applicable_with_fixture() -> None:
    report = audit({
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "capabilities": {
            "unsupported_multiply": {
                "fixture_status": "NOT_APPLICABLE_BY_LANGUAGE_CONTRACT",
                "fixtures": ["invented_multiply_case"],
            },
        },
    })
    assert report["status"] == "INCOMPLETE_FIXTURE_COVERAGE"
    assert report["invalid_capabilities"] == ["unsupported_multiply"]
