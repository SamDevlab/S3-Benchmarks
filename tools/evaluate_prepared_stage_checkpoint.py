"""Evaluate a prepared Stage06/Stage07 checkpoint against a machine-readable laboratory gate."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def evaluate(contract: dict[str, Any], checkpoint: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    blocked_fields: list[str] = []

    if checkpoint.get("stage_id") != contract.get("stage_id"):
        errors.append("stage_id mismatch")

    git_sha = checkpoint.get("candidate_git_sha")
    source_sha = checkpoint.get("candidate_source_sha256")
    binary_sha = checkpoint.get("candidate_binary_sha256")
    if not isinstance(git_sha, str) or HEX40.fullmatch(git_sha) is None:
        errors.append("candidate_git_sha must be 40 lowercase hex characters")
    if not isinstance(source_sha, str) or HEX64.fullmatch(source_sha) is None:
        errors.append("candidate_source_sha256 must be 64 lowercase hex characters")
    if binary_sha is not None and (not isinstance(binary_sha, str) or HEX64.fullmatch(binary_sha) is None):
        errors.append("candidate_binary_sha256 must be null or 64 lowercase hex characters")

    gates = checkpoint.get("gates")
    if not isinstance(gates, dict):
        gates = {}
        errors.append("checkpoint.gates must be an object")
    for field in contract.get("required_pass_fields", []):
        if gates.get(field) != "PASS":
            blocked_fields.append(str(field))

    invariants = checkpoint.get("invariants")
    if not isinstance(invariants, dict):
        invariants = {}
        errors.append("checkpoint.invariants must be an object")
    required = contract.get("required_invariants", {})
    for boolean_field in ("canonical_source_mutated", "self_emit_authorized", "stage2_authorized"):
        if boolean_field in required and invariants.get(boolean_field) is not required[boolean_field]:
            errors.append(f"{boolean_field} must be {str(required[boolean_field]).lower()}")

    relation = required.get("z_mask_relation")
    expected = required.get("z_mask_value")
    observed = invariants.get("z_mask")
    if not isinstance(observed, int):
        errors.append("z_mask must be an integer")
    elif relation == "LT" and not observed < int(expected):
        errors.append(f"z_mask must be < {expected}")
    elif relation == "EQ" and observed != int(expected):
        errors.append(f"z_mask must equal {expected}")
    elif relation not in {"LT", "EQ"}:
        errors.append(f"unsupported z_mask_relation: {relation}")

    status = "PASS" if not errors and not blocked_fields else "BLOCKED"
    return {
        "schema": "s3-benchmarks.bootstrap.prepared-stage-evaluation.v1",
        "stage_id": contract.get("stage_id"),
        "status": status,
        "candidate_git_sha": git_sha,
        "candidate_source_sha256": source_sha,
        "candidate_binary_sha256": binary_sha,
        "blocked_fields": blocked_fields,
        "errors": errors,
        "next_stage_candidate": contract.get("next_stage_candidate") if status == "PASS" else None,
        "promotion_effect": "NONE_LABORATORY_GATE_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = evaluate(_load(args.contract), _load(args.checkpoint))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"PREPARED_STAGE_GATE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"PREPARED_STAGE_GATE={result['status']}")
    return 0 if result["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
