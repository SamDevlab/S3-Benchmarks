from __future__ import annotations

from tools.analyze_stage04_parser_recovery import analyze


def _attempt(attempt_id: str, source: str, status: str, fingerprint: str | None) -> dict:
    value = {
        "attempt_id": attempt_id,
        "candidate_source_sha256": source,
        "parser_status": status,
    }
    if fingerprint is not None:
        value["diagnostic_fingerprint"] = fingerprint
    return value


def test_changed_blocker_after_source_change_is_progress() -> None:
    report = analyze([
        _attempt("a1", "a" * 64, "BLOCKED_SYNTAX", "indent:100"),
        _attempt("a2", "b" * 64, "BLOCKED_STRUCTURAL", "duplicate-match:220"),
    ])
    assert report["status"] == "RECOVERY_PROGRESS"
    assert report["attempts"][1]["classification"] == "FORWARD_RECOVERY_PROGRESS"
    assert report["s1_projection"] == "NOT_EVALUATED_BY_PARSER_RECOVERY"
    assert report["s2_projection"] == "NOT_EVALUATED_BY_PARSER_RECOVERY"


def test_same_source_same_blocker_is_reobservation_only() -> None:
    report = analyze([
        _attempt("a1", "a" * 64, "BLOCKED_SYNTAX", "indent:100"),
        _attempt("a2", "a" * 64, "BLOCKED_SYNTAX", "indent:100"),
    ])
    assert report["status"] == "PARSER_BLOCKED"
    assert report["attempts"][1]["classification"] == "REOBSERVATION_ONLY"


def test_three_changed_sources_with_same_blocker_detect_stall() -> None:
    report = analyze([
        _attempt("a1", "a" * 64, "BLOCKED_SYNTAX", "duplicate-match:220"),
        _attempt("a2", "b" * 64, "BLOCKED_SYNTAX", "duplicate-match:220"),
        _attempt("a3", "c" * 64, "BLOCKED_SYNTAX", "duplicate-match:220"),
    ])
    assert report["status"] == "STALLED_REPAIR"
    assert report["stalled_repair_detected"] is True
    assert report["attempts"][2]["classification"] == "STALLED_REPAIR"


def test_parser_pass_does_not_promote_semantic_lanes() -> None:
    report = analyze([
        _attempt("a1", "a" * 64, "BLOCKED_SYNTAX", "indent:100"),
        _attempt("a2", "b" * 64, "PASS", None),
    ])
    assert report["status"] == "PARSER_RECOVERED"
    assert report["expr_parser_syntax_projection"] == "PASS"
    assert report["s1_projection"] == "NOT_EVALUATED_BY_PARSER_RECOVERY"
    assert report["s2_projection"] == "NOT_EVALUATED_BY_PARSER_RECOVERY"


def test_blocked_without_diagnostic_is_not_fabricated_as_progress() -> None:
    report = analyze([
        _attempt("a1", "a" * 64, "BLOCKED_SYNTAX", None),
    ])
    assert report["status"] == "PARSER_BLOCKED"
    assert report["attempts"][0]["classification"] == "BLOCKED_UNCLASSIFIED"
