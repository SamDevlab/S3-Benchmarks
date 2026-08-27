from tools.import_s3_bootstrap_evidence import snapshot_from_semantic_requirements


def _semantic(relationships: dict[str, object]) -> dict[str, object]:
    return {
        "schema": "s3.selfhost.stage1-semantic-ir-requirements.v1",
        "status": "BLOCKED_GENERAL_EMITTER_CAPABILITY_GAP",
        "stage1_self_emit": "BLOCKED_UNTIL_MISSING_LANES_EXIST_AND_VERIFY",
        "stage2": "NOT_STARTED",
        "stage3": "NOT_STARTED",
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
