"""Check one Stage11 bootstrap action against live control and prior evidence. Never executes the action."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def check(contract: dict[str, Any], control: dict[str, Any], evidence: dict[str, Any], action: str) -> dict[str, Any]:
    errors: list[str] = []
    actions = contract.get("actions")
    if not isinstance(actions, dict) or action not in actions:
        errors.append(f"unsupported action: {action}")
        spec: dict[str, Any] = {}
    else:
        raw = actions[action]
        spec = raw if isinstance(raw, dict) else {}
        if not spec:
            errors.append(f"invalid contract action specification: {action}")

    if control.get("active_stage") != "11_SELF_EMIT_BOOTSTRAP":
        errors.append("active_stage is not 11_SELF_EMIT_BOOTSTRAP")

    authorization_field = spec.get("authorization_field")
    if not isinstance(authorization_field, str) or control.get(authorization_field) is not True:
        errors.append(f"{authorization_field or 'authorization_field'} is not true")

    required_prior = spec.get("required_prior_pass", [])
    gates = evidence.get("gates")
    if not isinstance(gates, dict):
        gates = {}
        errors.append("evidence.gates must be an object")
    missing_prior: list[str] = []
    for field in required_prior:
        if gates.get(field) != "PASS":
            missing_prior.append(str(field))
    if missing_prior:
        errors.append("required prior PASS missing: " + ", ".join(missing_prior))

    # A later action must not be treated as authorized merely because a later control bit is true.
    # The exact selected action and its own prior evidence are evaluated independently.
    status = "AUTHORIZED_HANDOFF" if not errors else "NOT_AUTHORIZED"
    return {
        "schema": "s3-benchmarks.bootstrap.stage11-action-authorization-evaluation.v1",
        "status": status,
        "action": action,
        "control_revision": control.get("control_revision"),
        "authorization_field": authorization_field,
        "missing_prior_pass": missing_prior,
        "errors": errors,
        "action_performed_by_this_tool": False,
        "authorized_action": action if status == "AUTHORIZED_HANDOFF" else None,
        "promotion_effect": "NONE_AUTHORIZATION_FIREWALL_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--control", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--action", required=True, choices=["SELF_EMIT", "STAGE2", "STAGE3", "T4"])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = check(_load(args.contract), _load(args.control), _load(args.evidence), args.action)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE11_AUTHORIZATION_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE11_{args.action}_AUTHORIZATION={result['status']}")
    return 0 if result["status"] in {"AUTHORIZED_HANDOFF", "NOT_AUTHORIZED"} else 3


if __name__ == "__main__":
    raise SystemExit(main())
