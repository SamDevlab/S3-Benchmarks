from tools.render_bootstrap_scorecard import build_scorecard, render_markdown


def _snapshot():
    return {
        "bootstrap": {
            "stage1": "BLOCKED",
            "stage1_self_emit": "NOT_AUTHORIZED",
            "stage2": "NOT_CREATED",
            "stage3": "NOT_STARTED",
            "full_self_hosting": False,
        },
        "semantic_ir": {
            "typed_values": "BLOCKED",
            "instruction_def_use": "BLOCKED",
            "call_dataflow": "BLOCKED",
            "complete_terminators": "BLOCKED",
            "canonical_serialization": "BLOCKED",
        },
        "provenance": {
            "source_lock_valid": True,
            "benchmark_lock_valid": True,
        },
        "evidence_notes": {
            "host_oracle_used_as_stage1_evidence": False,
            "supplemental_evidence": [
                {"source_applicability": "HISTORICAL_SOURCE_MISMATCH"}
            ],
        },
        "performance_eligibility": {
            "correctness_pass": False,
            "equivalent_workload": False,
            "stable_environment": False,
            "performance_valid": False,
        },
    }


def test_scorecard_has_no_single_numeric_score() -> None:
    scorecard = build_scorecard(_snapshot())
    assert scorecard["single_numeric_score"] is None
    assert scorecard["dimensions"]["bootstrap"]["stage1"] == "BLOCKED"
    assert scorecard["dimensions"]["behavioral_coverage"]["status"] == "NOT_RUN"
    assert scorecard["promotion"]["performed"] is False


def test_behavioral_pass_does_not_change_ir_state() -> None:
    coverage = {
        "case_count": 10,
        "case_parity_pass": 10,
        "case_parity_ratio": 1.0,
        "stage1_blocked_cases": 0,
        "semantic_mismatches": 0,
    }
    scorecard = build_scorecard(_snapshot(), coverage=coverage)
    assert scorecard["dimensions"]["behavioral_coverage"]["case_parity_pass"] == 10
    assert scorecard["dimensions"]["semantic_ir"]["typed_values"] == "BLOCKED"
    assert scorecard["dimensions"]["bootstrap"]["full_self_hosting"] is False


def test_historical_source_mismatch_is_visible_in_confidence() -> None:
    scorecard = build_scorecard(_snapshot())
    provenance = scorecard["dimensions"]["provenance_confidence"]
    assert provenance["source_lock_valid"] is True
    assert provenance["historical_source_mismatch_count"] == 1
    assert provenance["host_oracle_used_as_stage1_evidence"] is False


def test_markdown_preserves_separate_dimensions() -> None:
    markdown = render_markdown(build_scorecard(_snapshot()))
    assert "No aggregate numeric score" in markdown
    assert "Stage1: `BLOCKED`" in markdown
    assert "Historical source mismatches: `1`" in markdown
    assert "Performance valid: `False`" in markdown
