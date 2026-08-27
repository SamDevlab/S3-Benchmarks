from __future__ import annotations

from tools.evaluate_stage04_expression_checkpoint import evaluate


CONTRACT = {
    "stage_id": "04_EXPRESSIONS_S1_S2",
    "control_revision_minimum": 5,
    "required_pass_fields": [
        "expr_parser_syntax",
        "integer_literal_lowering",
        "negative_wide_literal_lowering",
        "identifier_lookup",
        "lexical_shadowing",
        "unary_negate",
        "unary_invert",
        "supported_binary_operators",
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
    "required_status_fields": {
        "stage03_evidence_backfill": ["PASS", "PARTIAL", "NOT_RECORDED", "NOT_REOBSERVED"],
        "unsupported_multiply_divide_remainder": ["FAIL_CLOSED", "NOT_APPLICABLE"],
    },
    "nonblocking_debt_fields": ["stage03_evidence_backfill"],
    "required_invariants": {"z_mask_must_be_less_than": 31},
}


def _checkpoint() -> dict:
    gates = {field: "PASS" for field in CONTRACT["required_pass_fields"]}
    gates["stage03_evidence_backfill"] = "PASS"
    gates["unsupported_multiply_divide_remainder"] = "NOT_APPLICABLE"
    return {
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "control_revision": 5,
        "candidate_git_sha": "a" * 40,
        "candidate_source_sha256": "b" * 64,
        "candidate_binary_sha256": "c" * 64,
        "gates": gates,
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
    assert report["nonblocking_evidence_debt"] == []


def test_stage03_backfill_debt_is_reported_but_nonblocking() -> None:
    checkpoint = _checkpoint()
    checkpoint["gates"]["stage03_evidence_backfill"] = "NOT_RECORDED"
    report = evaluate(CONTRACT, checkpoint)
    assert report["status"] == "PASS"
    assert report["blocked_fields"] == []
    assert report["nonblocking_evidence_debt"] == [
        {
            "field": "stage03_evidence_backfill",
            "observed": "NOT_RECORDED",
            "blocking": False,
        }
    ]


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


def test_stage04_gate_rejects_speculative_multiply_support() -> None:
    checkpoint = _checkpoint()
    checkpoint["gates"]["unsupported_multiply_divide_remainder"] = "PASS"
    report = evaluate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert report["status_field_failures"] == [
        {
            "field": "unsupported_multiply_divide_remainder",
            "observed": "PASS",
            "allowed": ["FAIL_CLOSED", "NOT_APPLICABLE"],
        }
    ]


def test_stage04_gate_requires_revision_5_or_newer() -> None:
    checkpoint = _checkpoint()
    checkpoint["control_revision"] = 4
    report = evaluate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert any("control_revision" in error for error in report["errors"])
