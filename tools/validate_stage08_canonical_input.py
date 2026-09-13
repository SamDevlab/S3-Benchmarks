"""Validate Stage08 evidence against the exact canonical Stage1 source supplied with the evidence package."""

from __future__ import annotations

import argparse
import hashlib
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


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate(contract: dict[str, Any], checkpoint: dict[str, Any], canonical_source: bytes) -> dict[str, Any]:
    errors: list[str] = []
    blocked_fields: list[str] = []

    if checkpoint.get("stage_id") != contract.get("stage_id"):
        errors.append("stage_id mismatch")

    for field in ("candidate_git_sha",):
        value = checkpoint.get(field)
        if not isinstance(value, str) or HEX40.fullmatch(value) is None:
            errors.append(f"{field} must be 40 lowercase hex characters")
    for field in ("candidate_source_sha256", "candidate_binary_sha256", "canonical_source_sha256", "stream_sha256"):
        value = checkpoint.get(field)
        if not isinstance(value, str) or HEX64.fullmatch(value) is None:
            errors.append(f"{field} must be 64 lowercase hex characters")

    observed_source_sha = _sha256(canonical_source)
    observed_source_bytes = len(canonical_source)
    if checkpoint.get("canonical_source_sha256") != observed_source_sha:
        errors.append("canonical_source_sha256 does not match supplied canonical source")
    if checkpoint.get("canonical_source_bytes") != observed_source_bytes:
        errors.append("canonical_source_bytes does not match supplied canonical source")

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
    if invariants.get("canonical_source_mutated") is not False:
        errors.append("canonical_source_mutated must be false")
    if invariants.get("z_mask") != 31:
        errors.append("z_mask must equal 31 for Stage08")

    status = "PASS" if not errors and not blocked_fields else "BLOCKED"
    return {
        "schema": "s3-benchmarks.bootstrap.stage08-canonical-input-evaluation.v1",
        "stage_id": contract.get("stage_id"),
        "status": status,
        "candidate_git_sha": checkpoint.get("candidate_git_sha"),
        "candidate_source_sha256": checkpoint.get("candidate_source_sha256"),
        "candidate_binary_sha256": checkpoint.get("candidate_binary_sha256"),
        "canonical_source_sha256": observed_source_sha,
        "canonical_source_bytes": observed_source_bytes,
        "stream_sha256": checkpoint.get("stream_sha256"),
        "blocked_fields": blocked_fields,
        "errors": errors,
        "next_stage_candidate": contract.get("next_stage_candidate") if status == "PASS" else None,
        "authorization_after_pass": contract.get("authorization_after_pass") if status == "PASS" else None,
        "canonical_mutation_authorized_by_this_tool": False,
        "promotion_effect": "NONE_LABORATORY_GATE_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--canonical-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = validate(_load(args.contract), _load(args.checkpoint), args.canonical_source.read_bytes())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE08_CANONICAL_INPUT_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE08_CANONICAL_INPUT={result['status']}")
    return 0 if result["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
