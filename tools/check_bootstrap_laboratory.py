"""Validate S3 Bootstrap Laboratory v1 snapshots.

This tool is intentionally evidence-only. It does not build S3, mutate the S3
repository, create Stage2/Stage3 artifacts, or run performance measurements.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "laboratory" / "bootstrap-v1" / "contract.json"


class BootstrapLabError(ValueError):
    pass


def _require_dict(value: object, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise BootstrapLabError(f"{label} must be an object")
    return value


def _require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        raise BootstrapLabError(f"{label} must be boolean")
    return value


def _state(value: object, allowed: set[str], label: str) -> str:
    if not isinstance(value, str) or value not in allowed:
        raise BootstrapLabError(f"{label} has invalid state: {value!r}")
    return value


def validate(snapshot: dict[str, Any], contract: dict[str, Any]) -> dict[str, Any]:
    allowed = set(contract["allowed_states"])
    missing_sections = [
        section for section in contract["required_sections"] if section not in snapshot
    ]
    if missing_sections:
        raise BootstrapLabError(
            "missing required sections: " + ", ".join(missing_sections)
        )

    provenance = _require_dict(snapshot["provenance"], "provenance")
    bootstrap = _require_dict(snapshot["bootstrap"], "bootstrap")
    semantic_ir = _require_dict(snapshot["semantic_ir"], "semantic_ir")
    determinism = _require_dict(snapshot["determinism"], "determinism")
    resources = _require_dict(snapshot["resources"], "resources")
    performance = _require_dict(
        snapshot["performance_eligibility"], "performance_eligibility"
    )

    if not isinstance(provenance.get("s3_commit"), str) or len(provenance["s3_commit"]) < 7:
        raise BootstrapLabError("provenance.s3_commit must identify an exact S3 commit")
    if not isinstance(provenance.get("benchmark_commit"), str) or len(provenance["benchmark_commit"]) < 7:
        raise BootstrapLabError(
            "provenance.benchmark_commit must identify an exact benchmark commit"
        )
    source_lock_valid = _require_bool(
        provenance.get("source_lock_valid"), "provenance.source_lock_valid"
    )
    benchmark_lock_valid = _require_bool(
        provenance.get("benchmark_lock_valid"), "provenance.benchmark_lock_valid"
    )

    stage0 = _state(bootstrap.get("stage0_reference"), allowed, "bootstrap.stage0_reference")
    stage1 = _state(bootstrap.get("stage1"), allowed, "bootstrap.stage1")
    self_emit = _state(bootstrap.get("stage1_self_emit"), allowed, "bootstrap.stage1_self_emit")
    stage2 = _state(bootstrap.get("stage2"), allowed, "bootstrap.stage2")
    stage3 = _state(bootstrap.get("stage3"), allowed, "bootstrap.stage3")
    full_self_hosting = _require_bool(
        bootstrap.get("full_self_hosting"), "bootstrap.full_self_hosting"
    )

    surface_states: dict[str, str] = {}
    for name in contract["semantic_surfaces"]:
        surface_states[name] = _state(
            semantic_ir.get(name), allowed, f"semantic_ir.{name}"
        )

    equivalence = _state(
        determinism.get("stage1_stage2_stage3_equivalence"),
        allowed,
        "determinism.stage1_stage2_stage3_equivalence",
    )

    stable_environment = _require_bool(
        performance.get("stable_environment"),
        "performance_eligibility.stable_environment",
    )
    equivalent_workload = _require_bool(
        performance.get("equivalent_workload"),
        "performance_eligibility.equivalent_workload",
    )
    correctness_pass = _require_bool(
        performance.get("correctness_pass"),
        "performance_eligibility.correctness_pass",
    )
    performance_valid = _require_bool(
        performance.get("performance_valid"),
        "performance_eligibility.performance_valid",
    )

    all_surfaces_pass = all(state == "PASS" for state in surface_states.values())
    stage2_created = stage2 not in {"NOT_CREATED", "NOT_STARTED", "BLOCKED", "NOT_AUTHORIZED"}
    stage2_correct = stage2 == "PASS"
    stage3_correct = stage3 == "PASS"

    violations: list[str] = []
    if stage2_created and not (self_emit == "PASS" and all_surfaces_pass):
        violations.append("Stage2 exists before Stage1 self-emit and semantic IR closure")
    if stage3 not in {"NOT_CREATED", "NOT_STARTED", "BLOCKED", "NOT_AUTHORIZED"} and not stage2_correct:
        violations.append("Stage3 exists before Stage2 correctness PASS")
    if full_self_hosting and not (
        self_emit == "PASS"
        and stage2_correct
        and stage3_correct
        and equivalence == "PASS"
    ):
        violations.append("full_self_hosting claimed before required bootstrap proofs")

    expected_performance_valid = all(
        [
            correctness_pass,
            equivalent_workload,
            stable_environment,
            source_lock_valid,
            benchmark_lock_valid,
        ]
    )
    if performance_valid != expected_performance_valid:
        violations.append(
            "performance_valid disagrees with correctness/equivalence/environment/provenance gates"
        )

    for metric in contract["resource_metrics"]:
        value = resources.get(metric)
        if value is not None and (
            not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0
        ):
            violations.append(f"resource metric {metric} must be null or non-negative numeric")

    status = "PASS" if not violations else "FAIL"
    return {
        "schema": "s3.bootstrap-laboratory-validation.v1",
        "status": status,
        "violations": violations,
        "derived": {
            "all_semantic_surfaces_pass": all_surfaces_pass,
            "stage2_created": stage2_created,
            "performance_valid_expected": expected_performance_valid,
            "full_self_hosting": full_self_hosting,
        },
        "observed": {
            "stage0_reference": stage0,
            "stage1": stage1,
            "stage1_self_emit": self_emit,
            "stage2": stage2,
            "stage3": stage3,
            "equivalence": equivalence,
            "semantic_surfaces": surface_states,
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    args = parser.parse_args(argv)

    snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    result = validate(
        _require_dict(snapshot, "snapshot"), _require_dict(contract, "contract")
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
