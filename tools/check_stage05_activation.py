"""Guard Stage05 fixture activation using an explicit S3 control-plane snapshot."""

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


def check(control: dict[str, Any], plan: dict[str, Any], matrix: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    active_stage = control.get("active_stage")
    revision = control.get("control_revision")

    if not isinstance(revision, int) or revision < 1:
        errors.append("control_revision must be a positive integer")
    if plan.get("activation_status") != "PREPARED_NOT_ACTIVE":
        errors.append("fixture plan must still be PREPARED_NOT_ACTIVE before activation")
    if matrix.get("activation_status") != "PREPARED_NOT_ACTIVE":
        errors.append("capability matrix must still be PREPARED_NOT_ACTIVE before activation")

    dangerous = {
        "canonical_stage1_mutation_authorized": control.get("canonical_stage1_mutation_authorized"),
        "self_emit_authorized": control.get("self_emit_authorized"),
        "stage2_authorized": control.get("stage2_authorized"),
        "stage3_authorized": control.get("stage3_authorized"),
        "t4_authorized": control.get("t4_authorized"),
    }
    unexpected_authorizations = sorted(
        key for key, value in dangerous.items() if value is not False
    )
    if unexpected_authorizations:
        errors.append(
            "Stage05 planning snapshot unexpectedly authorizes later/canonical gates: "
            + ", ".join(unexpected_authorizations)
        )

    if errors:
        status = "INVALID_CONTROL_SNAPSHOT"
    elif active_stage != "05_CALLS_ARRAYS_S3":
        status = "NOT_ACTIVE"
    else:
        status = "READY_TO_VALIDATE_AND_PIN_FIXTURES"

    return {
        "schema": "s3-benchmarks.bootstrap.stage05-activation-guard.v1",
        "status": status,
        "control_revision": revision,
        "active_stage": active_stage,
        "unexpected_authorizations": unexpected_authorizations,
        "errors": errors,
        "activation_authorized_by_this_tool": False,
        "next_action": (
            "VALIDATE_PREPARED_FIXTURES_WITH_S3_REFERENCE"
            if status == "READY_TO_VALIDATE_AND_PIN_FIXTURES"
            else None
        ),
        "promotion_effect": "NONE_CONTROL_GUARD_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control", type=Path, required=True)
    parser.add_argument("--fixture-plan", type=Path, required=True)
    parser.add_argument("--capability-matrix", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = check(_load(args.control), _load(args.fixture_plan), _load(args.capability_matrix))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE05_ACTIVATION_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE05_ACTIVATION_GUARD={report['status']}")
    return 0 if report["status"] in {"NOT_ACTIVE", "READY_TO_VALIDATE_AND_PIN_FIXTURES"} else 3


if __name__ == "__main__":
    raise SystemExit(main())
