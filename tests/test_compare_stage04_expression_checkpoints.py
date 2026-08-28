from __future__ import annotations

from tools.compare_stage04_expression_checkpoints import compare


def _checkpoint(**gates: str) -> dict:
    return {
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "candidate_git_sha": "a" * 40,
        "candidate_source_sha256": "b" * 64,
        "candidate_binary_sha256": None,
        "gates": gates,
    }


def test_stage04_compare_reports_improvement() -> None:
    report = compare(
        _checkpoint(expr_parser_syntax="BLOCKED", identifier_lookup="BLOCKED"),
        _checkpoint(expr_parser_syntax="PASS", identifier_lookup="BLOCKED"),
    )
    assert report["regression_gate"] == "PASS"
    assert report["improvement_count"] == 1
    assert report["improvements"][0]["gate"] == "expr_parser_syntax"


def test_stage04_compare_reports_real_regression() -> None:
    report = compare(
        _checkpoint(expr_parser_syntax="PASS", identifier_lookup="PASS"),
        _checkpoint(expr_parser_syntax="PASS", identifier_lookup="BLOCKED"),
    )
    assert report["regression_gate"] == "FAIL"
    assert report["regression_count"] == 1
    assert report["regressions"][0]["gate"] == "identifier_lookup"


def test_stage04_compare_separates_not_reobserved() -> None:
    report = compare(
        _checkpoint(expr_parser_syntax="PASS"),
        _checkpoint(expr_parser_syntax="NOT_REOBSERVED"),
    )
    assert report["regression_gate"] == "PASS"
    assert report["not_reobserved_count"] == 1
    assert report["regression_count"] == 0
