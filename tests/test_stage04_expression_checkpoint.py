from __future__ import annotations

from tools.evaluate_stage04_expression_checkpoint import evaluate


CONTRACT = {
    "stage_id": "04_EXPRESSIONS_S1_S2",
    "control_revision_minimum": 4,
    "required_pass_fields": [
        "stage03_evidence_backfill",
        "expr_parser_syntax",
        "integer_literal_lowering",
        "negative_wide_literal_lowering",
        "identifier_lookup",
        "lexical_shadowing",
        "unary_lowering",
        "binary_precedence",
        "comparison_lowering",
        "local_initialization",
        "assignment_reassignment",
        "instruction_result_ids",
        "ordered_operand_edges",
        "single_result_definition",
        "candidate_stage0_check",
        "focused_native_v2_conformance",
        "s1_typed_values",
        "s2_def_use",
    ],
    "required_invariants": {"z_mask_must_be_less_than": 31},
}


def _checkpoint() -> dict:
    return {
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "control_revision": 4,
        "candidate_git_sha": "a" * 40,
        "candidate_source_sha256": "b" * 64,
        "candidate_binary_sha256": "c" * 64,
        "gates": {field: "PASS" for field in CONTRACT["required_pass_fields"]},
        "invariants": {
            "canonical_source_mutated": False,
            "self_emit_authorized": False,
            "stage2_authorized": False,
            "z_mask": 3,
        },
    }


def test_stage04_gate_passes_only_complete_checkpoint() -> None:
    report = evaluate(CONTRACT, _checkpoint())
    assert report["status"] == "PASS"
    assert report["next_stage_candidate"] == "05_CALLS_ARRAYS_S3"


def test_stage04_gate_blocks_missing_stage03_backfill() -> None:
    checkpoint = _checkpoint()
    checkpoint["gates"]["stage03_evidence_backfill"] = "NOT_RECORDED"
    report = evaluate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert "stage03_evidence_backfill" in report["blocked_fields"]


def test_stage04_gate_blocks_parser_incomplete() -> None:
    checkpoint = _checkpoint()
    checkpoint["gates"]["expr_parser_syntax"] = "BLOCKED"
    report = evaluate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert "expr_parser_syntax" in report["blocked_fields"]


def test_stage04_gate_rejects_premature_z31() -> None:
    checkpoint = _checkpoint()
    checkpoint["invariants"]["z_mask"] = 31
    report = evaluate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert any("z_mask" in error for error in report["errors"])


def test_stage04_gate_rejects_canonical_mutation() -> None:
    checkpoint = _checkpoint()
    checkpoint["invariants"]["canonical_source_mutated"] = True
    report = evaluate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert any("canonical_source_mutated" in error for error in report["errors"])
