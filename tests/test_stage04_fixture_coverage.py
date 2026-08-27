from __future__ import annotations

from tools.audit_stage04_fixture_coverage import audit


def test_stage04_fixture_audit_reports_missing_and_partial() -> None:
    report = audit({
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "capabilities": {
            "literal": {"fixture_status": "PINNED", "fixtures": ["wide_literal_positive"]},
            "precedence": {"fixture_status": "FIXTURE_NOT_YET_PINNED", "fixtures": []},
            "comparison": {"fixture_status": "PARTIAL_PINNED", "fixtures": ["while_counter"]},
        },
    })
    assert report["status"] == "INCOMPLETE_FIXTURE_COVERAGE"
    assert report["pinned_count"] == 1
    assert report["missing_capabilities"] == ["precedence"]
    assert report["partial_capabilities"] == ["comparison"]


def test_stage04_fixture_audit_passes_only_all_pinned() -> None:
    report = audit({
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "capabilities": {
            "literal": {"fixture_status": "PINNED", "fixtures": ["a"]},
            "precedence": {"fixture_status": "PINNED", "fixtures": ["b"]},
        },
    })
    assert report["status"] == "PASS"
    assert report["missing_count"] == 0
    assert report["partial_count"] == 0
