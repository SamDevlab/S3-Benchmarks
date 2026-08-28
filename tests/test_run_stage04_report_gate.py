from __future__ import annotations

import json
from pathlib import Path

from tools.run_stage04_report_gate import run


CONTRACT = {
    "stage_id": "04_EXPRESSIONS_S1_S2",
    "control_revision_minimum": 5,
    "required_pass_fields": ["expr_parser_syntax", "s1_typed_values", "s2_def_use"],
    "required_status_fields": {
        "unsupported_multiply_divide_remainder": ["FAIL_CLOSED", "NOT_APPLICABLE"]
    },
    "required_invariants": {"z_mask_must_be_less_than": 31},
}


def _base() -> str:
    return (
        "CONTROL_REVISION=5\n"
        "CANDIDATE_GIT_SHA=" + "a" * 40 + "\n"
        "CANDIDATE_SOURCE_SHA256=" + "b" * 64 + "\n"
        "EXPR_PARSER_SYNTAX=PASS\n"
        "S1_TYPED_VALUES=PASS\n"
        "S2_DEF_USE=PASS\n"
        "UNSUPPORTED_MULTIPLY_DIVIDE_REMAINDER=NOT_APPLICABLE\n"
        "Z_MASK=3\n"
        "CANONICAL_SOURCE_MUTATED=NO\n"
    )


def test_report_gate_passes_complete_normalized_subset(tmp_path: Path) -> None:
    result = run(_base(), CONTRACT, tmp_path)
    assert result["status"] == "PASS"
    assert result["stage04_gate"] == "PASS"
    assert (tmp_path / "normalized-stage04-checkpoint.json").exists()
    assert (tmp_path / "stage04-gate.json").exists()


def test_report_gate_blocks_missing_required_gate(tmp_path: Path) -> None:
    text = _base().replace("S2_DEF_USE=PASS\n", "")
    result = run(text, CONTRACT, tmp_path)
    assert result["status"] == "BLOCKED_STAGE04"
    assert "s2_def_use" in result["blocked_fields"]


def test_report_gate_stops_on_normalization_failure(tmp_path: Path) -> None:
    text = _base() + "CONTROL_REVISION=5\n"
    result = run(text, CONTRACT, tmp_path)
    assert result["status"] == "BLOCKED_NORMALIZATION"
    assert result["stage04_gate"] == "NOT_EVALUATED"
    normalized = json.loads((tmp_path / "normalized-stage04-checkpoint.json").read_text())
    assert normalized["duplicate_keys"] == ["CONTROL_REVISION"]
