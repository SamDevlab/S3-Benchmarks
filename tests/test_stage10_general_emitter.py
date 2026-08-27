from __future__ import annotations

from tools.validate_stage10_general_emitter import validate


CONTRACT = {
    "stage_id": "10_GENERAL_EMITTER",
    "required_pass_fields": [
        "canonical_semantic_integration",
        "s1_typed_values",
        "s2_def_use",
        "s3_call_dataflow",
        "s4_complete_terminators",
        "s5_canonical_serialization",
        "focused_codegen_native_fixtures",
        "general_emitter",
        "canonical_stage1_emission",
    ],
    "required_principles": [
        "consume semantic records rather than lexical shortcuts",
        "no self-source-specific special cases",
        "preserve ABI/signature semantics",
        "unsupported semantic opcode fails closed",
    ],
    "required_invariants": {
        "self_emit_authorized": False,
        "stage2_authorized": False,
        "stage3_authorized": False,
        "t4_authorized": False,
    },
    "next_stage_candidate": "11_SELF_EMIT_BOOTSTRAP",
}


def _checkpoint() -> dict:
    return {
        "stage_id": "10_GENERAL_EMITTER",
        "candidate_git_sha": "a" * 40,
        "canonical_source_sha256": "b" * 64,
        "emitter_source_sha256": "c" * 64,
        "emitted_artifact_sha256": "d" * 64,
        "gates": {field: "PASS" for field in CONTRACT["required_pass_fields"]},
        "principles": {field: "PASS" for field in CONTRACT["required_principles"]},
        "invariants": {
            "self_emit_authorized": False,
            "stage2_authorized": False,
            "stage3_authorized": False,
            "t4_authorized": False,
        },
    }


def test_stage10_pass_does_not_authorize_self_emit() -> None:
    report = validate(CONTRACT, _checkpoint())
    assert report["status"] == "PASS"
    assert report["next_stage_candidate"] == "11_SELF_EMIT_BOOTSTRAP"
    assert report["self_emit_authorized_by_this_tool"] is False


def test_stage10_blocks_lexical_shortcut_principle_failure() -> None:
    checkpoint = _checkpoint()
    checkpoint["principles"]["consume semantic records rather than lexical shortcuts"] = "BLOCKED"
    report = validate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert any("lexical shortcuts" in field for field in report["blocked_fields"])


def test_stage10_blocks_premature_self_emit_authorization() -> None:
    checkpoint = _checkpoint()
    checkpoint["invariants"]["self_emit_authorized"] = True
    report = validate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert any("self_emit_authorized" in error for error in report["errors"])


def test_stage10_blocks_missing_canonical_emission() -> None:
    checkpoint = _checkpoint()
    checkpoint["gates"]["canonical_stage1_emission"] = "BLOCKED"
    report = validate(CONTRACT, checkpoint)
    assert report["status"] == "BLOCKED"
    assert "canonical_stage1_emission" in report["blocked_fields"]
