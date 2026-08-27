"""Check whether live control + Stage08 evidence authorize a Stage09 handoff. Never mutates S3."""

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


def check(control: dict[str, Any], stage08: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []

    if control.get("active_stage") != "09_CANONICAL_INTEGRATION":
        errors.append("active_stage is not 09_CANONICAL_INTEGRATION")
    if control.get("canonical_stage1_mutation_authorized") is not True:
        errors.append("canonical_stage1_mutation_authorized is not true")

    for field in ("self_emit_authorized", "stage2_authorized", "stage3_authorized", "t4_authorized"):
        if control.get(field) is not False:
            errors.append(f"{field} must remain false at Stage09 authorization")

    if stage08.get("stage_id") != "08_CANONICAL_SOURCE_INPUT":
        errors.append("prior evidence is not Stage08 canonical-input evidence")
    if stage08.get("status") != "PASS":
        errors.append("Stage08 evidence status is not PASS")
    if stage08.get("canonical_mutation_authorized_by_this_tool") is not False:
        errors.append("Stage08 evidence must not itself authorize canonical mutation")

    status = "AUTHORIZED_HANDOFF" if not errors else "NOT_AUTHORIZED"
    return {
        "schema": "s3-benchmarks.bootstrap.stage09-authorization-evaluation.v1",
        "status": status,
        "control_revision": control.get("control_revision"),
        "active_stage": control.get("active_stage"),
        "stage08_status": stage08.get("status"),
        "errors": errors,
        "canonical_mutation_performed_by_this_tool": False,
        "authorized_action": (
            "HANDOFF_TO_S3_FOR_SMALLEST_REVIEWABLE_CANONICAL_INTEGRATION_PATCH"
            if status == "AUTHORIZED_HANDOFF"
            else None
        ),
        "self_emit_authorized_by_this_tool": False,
        "stage2_authorized_by_this_tool": False,
        "promotion_effect": "NONE_AUTHORIZATION_FIREWALL_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control", type=Path, required=True)
    parser.add_argument("--stage08-evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = check(_load(args.control), _load(args.stage08_evidence))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE09_AUTHORIZATION_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE09_AUTHORIZATION={result['status']}")
    return 0 if result["status"] in {"AUTHORIZED_HANDOFF", "NOT_AUTHORIZED"} else 3


if __name__ == "__main__":
    raise SystemExit(main())
