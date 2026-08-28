"""Compare a live Codex STAGE_SEQUENCE.json snapshot with the laboratory's expected route contract."""

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


def validate(contract: dict[str, Any], live: dict[str, Any]) -> dict[str, Any]:
    expected = contract.get("sequence")
    observed = live.get("sequence")
    errors: list[str] = []
    changes: list[dict[str, Any]] = []

    if not isinstance(expected, list) or not isinstance(observed, list):
        errors.append("both contract.sequence and live.sequence must be arrays")
        expected = expected if isinstance(expected, list) else []
        observed = observed if isinstance(observed, list) else []

    max_len = max(len(expected), len(observed))
    for index in range(max_len):
        exp = expected[index] if index < len(expected) else None
        obs = observed[index] if index < len(observed) else None
        if exp != obs:
            changes.append({"index": index, "expected": exp, "observed": obs})

    if live.get("authorization_rule") and "Never infer authorization" not in str(live.get("authorization_rule")):
        errors.append("live authorization_rule no longer contains never-infer-authorization semantics")
    if live.get("failure_rule") and "remain in that stage" not in str(live.get("failure_rule")):
        errors.append("live failure_rule no longer clearly requires remaining in the failed stage")

    status = "MATCH" if not errors and not changes else "DRIFT_DETECTED"
    return {
        "schema": "s3-benchmarks.bootstrap.control-route-drift.v1",
        "status": status,
        "expected_stage_count": len(expected),
        "observed_stage_count": len(observed),
        "changes": changes,
        "errors": errors,
        "requires_control_contract_review": status == "DRIFT_DETECTED",
        "promotion_effect": "NONE_DRIFT_DETECTION_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--live-sequence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = validate(_load(args.contract), _load(args.live_sequence))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"CONTROL_ROUTE_DRIFT_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"CONTROL_ROUTE={result['status']}")
    return 0 if result["status"] == "MATCH" else 3


if __name__ == "__main__":
    raise SystemExit(main())
