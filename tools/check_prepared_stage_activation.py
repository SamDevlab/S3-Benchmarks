"""Guard prepared Stage05/06/07 laboratory plans against the live S3 control-plane snapshot."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

SUPPORTED_STAGES = {
    "05_CALLS_ARRAYS_S3",
    "06_CONTROL_FLOW_S4",
    "07_SERIALIZATION_S5",
}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def check(control: dict[str, Any], plan: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    desired = plan.get("stage_id")
    active = control.get("active_stage")
    revision = control.get("control_revision")

    if desired not in SUPPORTED_STAGES:
        errors.append(f"unsupported prepared stage: {desired}")
    if not isinstance(revision, int) or revision < 1:
        errors.append("control_revision must be a positive integer")
    if plan.get("activation_status") != "PREPARED_NOT_ACTIVE":
        errors.append("prepared plan must have activation_status=PREPARED_NOT_ACTIVE")

    if control.get("emergency_stop") is True:
        errors.append("control plane has emergency_stop=true")

    later_authorizations = {
        "canonical_stage1_mutation_authorized": control.get("canonical_stage1_mutation_authorized"),
        "self_emit_authorized": control.get("self_emit_authorized"),
        "stage2_authorized": control.get("stage2_authorized"),
        "stage3_authorized": control.get("stage3_authorized"),
        "t4_authorized": control.get("t4_authorized"),
    }
    unexpected = sorted(name for name, value in later_authorizations.items() if value is not False)
    if unexpected:
        errors.append("unexpected later/canonical authorization while qualifying prepared stage: " + ", ".join(unexpected))

    if errors:
        status = "INVALID_CONTROL_SNAPSHOT"
    elif active == desired:
        status = "READY_TO_VALIDATE_PREPARED_STAGE"
    else:
        status = "NOT_ACTIVE"

    return {
        "schema": "s3-benchmarks.bootstrap.prepared-stage-activation-guard.v1",
        "status": status,
        "control_revision": revision,
        "active_stage": active,
        "prepared_stage": desired,
        "unexpected_authorizations": unexpected,
        "errors": errors,
        "activation_authorized_by_this_tool": False,
        "next_action": "VALIDATE_PREPARED_STAGE_INPUTS" if status == "READY_TO_VALIDATE_PREPARED_STAGE" else None,
        "promotion_effect": "NONE_CONTROL_GUARD_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = check(_load(args.control), _load(args.plan))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"PREPARED_STAGE_ACTIVATION_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"PREPARED_STAGE_ACTIVATION={report['status']}")
    return 0 if report["status"] in {"NOT_ACTIVE", "READY_TO_VALIDATE_PREPARED_STAGE"} else 3


if __name__ == "__main__":
    raise SystemExit(main())
