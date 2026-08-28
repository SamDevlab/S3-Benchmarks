from __future__ import annotations

import json
from pathlib import Path

from tools.check_bootstrap_laboratory import validate

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "laboratory" / "bootstrap-v1" / "contract.json"
CURRENT_CHECKPOINT = (
    ROOT
    / "laboratory"
    / "bootstrap-v1"
    / "checkpoints"
    / "s3-0789ad2.json"
)


def _contract() -> dict:
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def _snapshot() -> dict:
    return {
        "provenance": {
            "s3_commit": "0789ad2df5f200c6b35b67d591d10e016c1a557a",
            "benchmark_commit": "0000000000000000000000000000000000000000",
            "source_lock_valid": True,
            "benchmark_lock_valid": True,
        },
        "bootstrap": {
            "stage0_reference": "PASS",
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
        "determinism": {
            "stage1_stage2_stage3_equivalence": "NOT_AUTHORIZED"
        },
        "resources": {
            "peak_rss_bytes": None,
            "compile_wall_seconds": None,
            "artifact_bytes": None,
            "assembly_bytes": 0,
            "semantic_value_count": None,
            "instruction_count": None,
            "block_count": None,
            "call_count": None,
        },
        "performance_eligibility": {
            "correctness_pass": False,
            "equivalent_workload": False,
            "stable_environment": False,
            "performance_valid": False,
        },
    }


def test_current_blocked_bootstrap_state_is_valid_evidence() -> None:
    result = validate(_snapshot(), _contract())
    assert result["status"] == "PASS"
    assert result["derived"]["all_semantic_surfaces_pass"] is False
    assert result["derived"]["stage2_created"] is False
    assert result["derived"]["performance_valid_expected"] is False


def test_pinned_current_checkpoint_is_valid_and_fail_closed() -> None:
    snapshot = json.loads(CURRENT_CHECKPOINT.read_text(encoding="utf-8"))
    result = validate(snapshot, _contract())
    assert result["status"] == "PASS"
    assert snapshot["provenance"]["s3_commit"].startswith("0789ad2")
    assert snapshot["bootstrap"]["stage1_self_emit"] == "NOT_AUTHORIZED"
    assert snapshot["bootstrap"]["stage2"] == "NOT_CREATED"
    assert snapshot["bootstrap"]["full_self_hosting"] is False
    assert snapshot["performance_eligibility"]["performance_valid"] is False


def test_stage2_cannot_exist_before_self_emit_and_semantic_closure() -> None:
    snapshot = _snapshot()
    snapshot["bootstrap"]["stage2"] = "PASS"
    result = validate(snapshot, _contract())
    assert result["status"] == "FAIL"
    assert any("Stage2 exists" in item for item in result["violations"])


def test_full_self_hosting_cannot_be_claimed_without_equivalence() -> None:
    snapshot = _snapshot()
    snapshot["bootstrap"].update(
        {
            "stage1": "PASS",
            "stage1_self_emit": "PASS",
            "stage2": "PASS",
            "stage3": "PASS",
            "full_self_hosting": True,
        }
    )
    for key in snapshot["semantic_ir"]:
        snapshot["semantic_ir"][key] = "PASS"
    snapshot["determinism"]["stage1_stage2_stage3_equivalence"] = "BLOCKED"
    result = validate(snapshot, _contract())
    assert result["status"] == "FAIL"
    assert any("full_self_hosting" in item for item in result["violations"])


def test_performance_gate_is_derived_not_declared() -> None:
    snapshot = _snapshot()
    snapshot["performance_eligibility"].update(
        {
            "correctness_pass": False,
            "equivalent_workload": True,
            "stable_environment": True,
            "performance_valid": True,
        }
    )
    result = validate(snapshot, _contract())
    assert result["status"] == "FAIL"
    assert result["derived"]["performance_valid_expected"] is False


def test_resource_metrics_are_characterization_and_must_be_non_negative() -> None:
    snapshot = _snapshot()
    snapshot["resources"]["peak_rss_bytes"] = -1
    result = validate(snapshot, _contract())
    assert result["status"] == "FAIL"
    assert any("peak_rss_bytes" in item for item in result["violations"])
