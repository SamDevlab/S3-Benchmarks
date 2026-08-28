"""Evaluate a normalized Codex Stage04 checkpoint against the laboratory gate."""

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
    status_field_failures: list[dict[str, Any]] = []
    evidence_debt: list[dict[str, Any]] = []

    if checkpoint.get("stage_id") != contract.get("stage_id"):
        errors.append("stage_id mismatch")

    revision = checkpoint.get("control_revision")
    minimum = int(contract.get("control_revision_minimum", 0))
    if not isinstance(revision, int) or revision < minimum:
        errors.append(f"control_revision must be >= {minimum}")

    candidate_git_sha = checkpoint.get("candidate_git_sha")
    if not isinstance(candidate_git_sha, str) or HEX40.fullmatch(candidate_git_sha) is None:
        errors.append("candidate_git_sha must be 40 lowercase hex characters")

    candidate_source_sha = checkpoint.get("candidate_source_sha256")
    if not isinstance(candidate_source_sha, str) or HEX64.fullmatch(candidate_source_sha) is None:
        errors.append("candidate_source_sha256 must be 64 lowercase hex characters")

    candidate_binary_sha = checkpoint.get("candidate_binary_sha256")
    if candidate_binary_sha is not None:
        if not isinstance(candidate_binary_sha, str) or HEX64.fullmatch(candidate_binary_sha) is None:
            errors.append("candidate_binary_sha256 must be null or 64 lowercase hex characters")

    gates = checkpoint.get("gates")
    if not isinstance(gates, dict):
        errors.append("checkpoint.gates must be an object")
        gates = {}

    for field in contract.get("required_pass_fields", []):
        status = gates.get(field, "MISSING")
        if status != "PASS":
            blocked_fields.append(str(field))

    required_status_fields = contract.get("required_status_fields", {})
    if not isinstance(required_status_fields, dict):
        errors.append("contract.required_status_fields must be an object")
        required_status_fields = {}
    debt_fields = {
        str(field) for field in contract.get("nonblocking_debt_fields", [])
    }
    for field, allowed in required_status_fields.items():
        if not isinstance(allowed, list) or not allowed:
            errors.append(f"contract required status field {field} has no allowed values")
            continue
        observed = gates.get(field, "MISSING")
        if observed not in allowed:
            status_field_failures.append({
                "field": str(field),
                "observed": observed,
                "allowed": list(allowed),
            })
        elif str(field) in debt_fields and observed != "PASS":
            evidence_debt.append({
                "field": str(field),
                "observed": observed,
                "blocking": False,
            })

    invariants = checkpoint.get("invariants")
    if not isinstance(invariants, dict):
        errors.append("checkpoint.invariants must be an object")
        invariants = {}

    if invariants.get("canonical_source_mutated") is not False:
        errors.append("canonical_source_mutated must be false")
    if invariants.get("self_emit_authorized") is not False:
        errors.append("self_emit_authorized must be false during Stage04")
    if invariants.get("stage2_authorized") is not False:
        errors.append("stage2_authorized must be false during Stage04")

    z_mask = invariants.get("z_mask")
    if not isinstance(z_mask, int):
        errors.append("z_mask must be an integer")
    elif z_mask >= int(contract.get("required_invariants", {}).get("z_mask_must_be_less_than", 31)):
        errors.append("z_mask must remain below 31 during Stage04")

    status = (
        "PASS"
        if not errors and not blocked_fields and not status_field_failures
        else "BLOCKED"
    )
    return {
        "schema": "s3-benchmarks.bootstrap.stage04-expression-evaluation.v3",
        "stage_id": contract.get("stage_id"),
        "status": status,
        "control_revision": revision,
        "candidate_git_sha": candidate_git_sha,
        "candidate_source_sha256": candidate_source_sha,
        "candidate_binary_sha256": candidate_binary_sha,
        "blocked_fields": blocked_fields,
        "status_field_failures": status_field_failures,
        "nonblocking_evidence_debt": evidence_debt,
        "errors": errors,
        "next_stage_candidate": "05_CALLS_ARRAYS_S3" if status == "PASS" else None,
        "promotion_effect": "NONE_LABORATORY_GATE_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = evaluate(_load(args.contract), _load(args.checkpoint))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE04_GATE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE04_GATE={report['status']}")
    print(f"BLOCKED_FIELDS={len(report['blocked_fields'])}")
    print(f"STATUS_FIELD_FAILURES={len(report['status_field_failures'])}")
    print(f"NONBLOCKING_EVIDENCE_DEBT={len(report['nonblocking_evidence_debt'])}")
    return 0 if report["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
