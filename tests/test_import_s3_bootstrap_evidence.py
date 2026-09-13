import json

from tools.import_s3_bootstrap_evidence import (
    snapshot_from_semantic_requirements,
    summarize_supplemental_json,
)


def _semantic(relationships: dict[str, object]) -> dict[str, object]:
    return {
        "schema": "s3.selfhost.stage1-semantic-ir-requirements.v1",
        "status": "BLOCKED_GENERAL_EMITTER_CAPABILITY_GAP",
        "stage1_self_emit": "BLOCKED_UNTIL_MISSING_LANES_EXIST_AND_VERIFY",
        "stage2": "NOT_STARTED",
        "stage3": "NOT_STARTED",
        "source": {"sha256": "c" * 64},
        "missing_lossless_typed_lanes": ["typed_constant_interning_and_definition_ids"],
        "storage_evidence": {"semantic_relationships": relationships},
        "reference_typed_ir": {
            "status": "MEASURED_HOST_IR_ORACLE_NOT_STAGE1_EVIDENCE",
            "instructions": 49128,
        },
    }


def _snapshot(relationships: dict[str, object]):
    return snapshot_from_semantic_requirements(
        _semantic(relationships),
        s3_commit="a" * 40,
        benchmark_commit="b" * 40,
        source_lock_valid=True,
        benchmark_lock_valid=True,
    )


def test_current_false_relationships_remain_blocked() -> None:
    snapshot = _snapshot(
        {
            "typed_value_definitions": False,
            "instruction_operand_value_ids": False,
            "instruction_result_value_ids": False,
            "call_argument_value_ids": False,
            "call_result_value_ids": False,
            "complete_terminator_values": False,
            "canonical_serialized_ir": False,
        }
    )
    assert set(snapshot["semantic_ir"].values()) == {"BLOCKED"}
    assert snapshot["bootstrap"]["stage1"] == "BLOCKED"
    assert snapshot["bootstrap"]["stage2"] == "NOT_STARTED"
    assert snapshot["evidence_notes"]["host_oracle_used_as_stage1_evidence"] is False


def test_surface_requires_every_relationship_in_group() -> None:
    snapshot = _snapshot(
        {
            "typed_value_definitions": True,
            "instruction_operand_value_ids": True,
            "instruction_result_value_ids": False,
            "call_argument_value_ids": True,
            "call_result_value_ids": True,
            "complete_terminator_values": True,
            "canonical_serialized_ir": True,
        }
    )
    assert snapshot["semantic_ir"]["typed_values"] == "PASS"
    assert snapshot["semantic_ir"]["instruction_def_use"] == "BLOCKED"
    assert snapshot["semantic_ir"]["call_dataflow"] == "PASS"
    assert snapshot["semantic_ir"]["complete_terminators"] == "PASS"
    assert snapshot["semantic_ir"]["canonical_serialization"] == "PASS"


def test_missing_relationship_is_never_promoted() -> None:
    snapshot = _snapshot({"typed_value_definitions": True})
    assert snapshot["semantic_ir"]["typed_values"] == "PASS"
    assert snapshot["semantic_ir"]["instruction_def_use"] == "BLOCKED"
    assert snapshot["semantic_ir"]["call_dataflow"] == "BLOCKED"


def test_host_oracle_counts_do_not_fill_stage1_resource_metrics() -> None:
    snapshot = _snapshot({})
    assert snapshot["resources"]["instruction_count"] is None
    assert snapshot["resources"]["semantic_value_count"] is None


def _write_call_pool_fixture(path, measured_sha: str) -> None:
    path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "status": "POOL_CLOSED_EMITTER_BLOCKED",
                "pool": {
                    "required_capacity": 736,
                    "selected_capacity": 746,
                    "headroom": 10,
                    "bank_sizes": [365, 365, 16],
                },
                "runtime_measurement": {
                    "total_calls": 656,
                    "total_call_arguments": 736,
                    "max_call_arity": 4,
                    "pool_used": 736,
                    "pool_gate": "PASS",
                },
                "clean_source_gate": {"source_sha256": measured_sha},
                "remaining_blocker": {
                    "id": "GENERAL_EMITTER_CAPABILITY_GAP",
                    "stage": "general emitter",
                    "stage1_to_stage2": "BLOCKED_NOT_STARTED",
                    "stage3": "NOT_STARTED",
                },
            }
        ),
        encoding="utf-8",
    )


def test_call_pool_closure_matching_source_is_still_provenance_only(tmp_path) -> None:
    evidence = tmp_path / "call-argument-pool-closure.json"
    current_sha = "d" * 64
    _write_call_pool_fixture(evidence, current_sha)
    row = summarize_supplemental_json(
        evidence,
        current_semantic_source_sha256=current_sha,
    )
    assert row["status"] == "POOL_CLOSED_EMITTER_BLOCKED"
    assert row["pool"]["required_capacity"] == 736
    assert row["pool"]["selected_capacity"] == 746
    assert row["pool"]["headroom"] == 10
    assert row["runtime_measurement"]["pool_gate"] == "PASS"
    assert row["remaining_blocker"]["id"] == "GENERAL_EMITTER_CAPABILITY_GAP"
    assert row["source_applicability"] == "MATCH"
    assert row["promotion_effect"] == "NONE_PROVENANCE_ONLY"


def test_historical_call_pool_source_mismatch_is_explicit(tmp_path) -> None:
    evidence = tmp_path / "call-argument-pool-closure.json"
    _write_call_pool_fixture(evidence, "1" * 64)
    row = summarize_supplemental_json(
        evidence,
        current_semantic_source_sha256="2" * 64,
    )
    assert row["source_applicability"] == "HISTORICAL_SOURCE_MISMATCH"
    assert row["measured_source_sha256"] == "1" * 64
    assert row["current_semantic_source_sha256"] == "2" * 64
    assert row["promotion_effect"] == "NONE_PROVENANCE_ONLY"
