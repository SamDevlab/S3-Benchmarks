from __future__ import annotations

from tools.normalize_codex_stage04_report import normalize


def test_normalizer_maps_revision5_checkpoint_without_prose_inference() -> None:
    text = """
CONTROL_REVISION=5
CANDIDATE_GIT_SHA=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
CANDIDATE_SOURCE_SHA256=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
CANDIDATE_BINARY_SHA256=cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
STAGE03_EVIDENCE_BACKFILL=PASS
EXPR_PARSER_SYNTAX=PASS
UNARY_NEGATE=PASS
UNARY_INVERT=BLOCKED
SUPPORTED_BINARY_OPERATORS=PASS
UNSUPPORTED_MULTIPLY_DIVIDE_REMAINDER=NOT_APPLICABLE
S1_TYPED_VALUES=BLOCKED
S2_DEF_USE=BLOCKED
Z_MASK=3
CANONICAL_SOURCE_MUTATED=NO
FIRST_REAL_BLOCKER=UNARY_INVERT
NEXT_STAGE=
This prose says PASS but must not count.
"""
    report = normalize(text)
    assert report["normalization_status"] == "PASS"
    assert report["control_revision"] == 5
    assert report["gates"]["expr_parser_syntax"] == "PASS"
    assert report["gates"]["unary_invert"] == "BLOCKED"
    assert report["gates"]["unsupported_multiply_divide_remainder"] == "NOT_APPLICABLE"
    assert report["invariants"]["z_mask"] == 3
    assert report["invariants"]["canonical_source_mutated"] is False
    assert report["first_real_blocker"] == "UNARY_INVERT"


def test_normalizer_does_not_infer_missing_gate_pass() -> None:
    report = normalize("CONTROL_REVISION=5\nEXPR_PARSER_SYNTAX=PASS\n")
    assert report["gates"] == {"expr_parser_syntax": "PASS"}
    assert "s1_typed_values" not in report["gates"]
    assert report["invariants"]["z_mask"] is None


def test_normalizer_rejects_bound_instead_of_observed_zmask() -> None:
    report = normalize("CONTROL_REVISION=5\nZ_MASK=<31\n")
    assert report["normalization_status"] == "BLOCKED"
    assert any("observed integer" in error for error in report["normalization_errors"])


def test_normalizer_rejects_duplicate_key() -> None:
    report = normalize("CONTROL_REVISION=5\nEXPR_PARSER_SYNTAX=PASS\nEXPR_PARSER_SYNTAX=BLOCKED\n")
    assert report["normalization_status"] == "BLOCKED"
    assert report["duplicate_keys"] == ["EXPR_PARSER_SYNTAX"]
    assert report["gates"]["expr_parser_syntax"] == "BLOCKED"


def test_normalizer_accepts_head_after_as_git_sha_alias() -> None:
    report = normalize(
        "CONTROL_REVISION=5\n"
        "HEAD_AFTER=0123456789abcdef0123456789abcdef01234567\n"
        "CANDIDATE_SOURCE_SHA256=" + "a" * 64 + "\n"
    )
    assert report["normalization_status"] == "PASS"
    assert report["candidate_git_sha"] == "0123456789abcdef0123456789abcdef01234567"
