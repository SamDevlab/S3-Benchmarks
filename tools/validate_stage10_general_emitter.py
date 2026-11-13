"""Validate Stage10 General Emitter evidence without authorizing SELF_EMIT."""

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


def validate(contract: dict[str, Any], checkpoint: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    blocked_fields: list[str] = []

    if checkpoint.get("stage_id") != contract.get("stage_id"):
        errors.append("stage_id mismatch")

    git_sha = checkpoint.get("candidate_git_sha")
    if not isinstance(git_sha, str) or HEX40.fullmatch(git_sha) is None:
        errors.append("candidate_git_sha must be 40 lowercase hex characters")
    for field in ("canonical_source_sha256", "emitter_source_sha256", "emitted_artifact_sha256"):
        value = checkpoint.get(field)
        if not isinstance(value, str) or HEX64.fullmatch(value) is None:
            errors.append(f"{field} must be 64 lowercase hex characters")

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
    for field, required in contract.get("required_invariants", {}).items():
        if invariants.get(field) is not required:
            errors.append(f"{field} must be {str(required).lower()}")

    principles = checkpoint.get("principles")
    if not isinstance(principles, dict):
        principles = {}
        errors.append("checkpoint.principles must be an object")
    for principle in contract.get("required_principles", []):
        if principles.get(principle) != "PASS":
            blocked_fields.append(f"principle:{principle}")

    status = "PASS" if not errors and not blocked_fields else "BLOCKED"
    return {
        "schema": "s3-benchmarks.bootstrap.stage10-general-emitter-evaluation.v1",
        "stage_id": contract.get("stage_id"),
        "status": status,
        "candidate_git_sha": git_sha,
        "blocked_fields": blocked_fields,
        "errors": errors,
        "next_stage_candidate": contract.get("next_stage_candidate") if status == "PASS" else None,
        "self_emit_authorized_by_this_tool": False,
        "stage2_authorized_by_this_tool": False,
        "promotion_effect": "NONE_LABORATORY_GATE_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = validate(_load(args.contract), _load(args.checkpoint))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE10_GENERAL_EMITTER_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE10_GENERAL_EMITTER={result['status']}")
    return 0 if result["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
