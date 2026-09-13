from __future__ import annotations

from tools.evaluate_prepared_stage_checkpoint import evaluate


STAGE06 = {
    "stage_id": "06_CONTROL_FLOW_S4",
    "required_pass_fields": ["s1_typed_values", "s2_def_use", "s3_call_dataflow", "s4_complete_terminators"],
    "required_invariants": {
        "canonical_source_mutated": False,
        "self_emit_authorized": False,
        "stage2_authorized": False,
        "z_mask_relation": "LT",
        "z_mask_value": 31,
    },
    "next_stage_candidate": "07_SERIALIZATION_S5",
}

STAGE07 = {
    "stage_id": "07_SERIALIZATION_S5",
    "required_pass_fields": [
        "s1_typed_values",
        "s2_def_use",
        "s3_call_dataflow",
        "s4_complete_terminators",
        "s5_canonical_serialization",
        "focused_v2_conformance",
        "deterministic_repeat",
    ],
    "required_invariants": {
        "canonical_source_mutated": False,
        "self_emit_authorized": False,
        "stage2_authorized": False,
        "z_mask_relation": "EQ",
        "z_mask_value": 31,
    },
    "next_stage_candidate": "08_CANONICAL_STAGE1_INPUT",
}


def _checkpoint(stage: str, required: list[str], z_mask: int) -> dict:
    return {
        "stage_id": stage,
        "candidate_git_sha": "a" * 40,
        "candidate_source_sha256": "b" * 64,
        "candidate_binary_sha256": "c" * 64,
        "gates": {field: "PASS" for field in required},
        "invariants": {
            "canonical_source_mutated": False,
            "self_emit_authorized": False,
            "stage2_authorized": False,
            "z_mask": z_mask,
        },
    }


def test_stage06_passes_only_below_z31() -> None:
    checkpoint = _checkpoint(STAGE06["stage_id"], STAGE06["required_pass_fields"], 15)
    report = evaluate(STAGE06, checkpoint)
    assert report["status"] == "PASS"
    assert report["next_stage_candidate"] == "07_SERIALIZATION_S5"


def test_stage06_rejects_premature_z31() -> None:
    checkpoint = _checkpoint(STAGE06["stage_id"], STAGE06["required_pass_fields"], 31)
    report = evaluate(STAGE06, checkpoint)
    assert report["status"] == "BLOCKED"
    assert any("z_mask" in error for error in report["errors"])


def test_stage07_requires_exact_z31() -> None:
    checkpoint = _checkpoint(STAGE07["stage_id"], STAGE07["required_pass_fields"], 31)
    report = evaluate(STAGE07, checkpoint)
    assert report["status"] == "PASS"
    assert report["next_stage_candidate"] == "08_CANONICAL_STAGE1_INPUT"


def test_stage07_blocks_missing_determinism() -> None:
    checkpoint = _checkpoint(STAGE07["stage_id"], STAGE07["required_pass_fields"], 31)
    checkpoint["gates"]["deterministic_repeat"] = "BLOCKED"
    report = evaluate(STAGE07, checkpoint)
    assert report["status"] == "BLOCKED"
    assert "deterministic_repeat" in report["blocked_fields"]


def test_prepared_gate_rejects_canonical_mutation() -> None:
    checkpoint = _checkpoint(STAGE07["stage_id"], STAGE07["required_pass_fields"], 31)
    checkpoint["invariants"]["canonical_source_mutated"] = True
    report = evaluate(STAGE07, checkpoint)
    assert report["status"] == "BLOCKED"
    assert any("canonical_source_mutated" in error for error in report["errors"])
