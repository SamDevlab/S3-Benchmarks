"""Audit Stage05 planning without activating or promoting its gate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from tools.generate_bootstrap_fuzz_corpus import cases


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def audit(stage_map: dict[str, Any], plan: dict[str, Any], matrix: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    corpus_ids = {case.case_id for case in cases()}
    prepared = set(str(key) for key in plan.get("prepared_cases", {}).keys())
    negative = set(str(key) for key in plan.get("negative_cases_to_pin_on_activation", {}).keys())
    known = corpus_ids | prepared | negative

    if plan.get("activation_status") != "PREPARED_NOT_ACTIVE":
        errors.append("fixture plan activation_status must remain PREPARED_NOT_ACTIVE")
    if matrix.get("activation_status") != "PREPARED_NOT_ACTIVE":
        errors.append("capability matrix activation_status must remain PREPARED_NOT_ACTIVE")

    stage05 = stage_map.get("stages", {}).get("05_CALLS_ARRAYS_S3", {})
    active_required = set(str(value) for value in stage05.get("required_cases", []))
    leaked = sorted((prepared | negative) & active_required)
    if leaked:
        errors.append(f"prepared Stage05 cases leaked into active stage map: {leaked}")

    unknown_refs: list[str] = []
    capabilities = matrix.get("capabilities", {})
    if not isinstance(capabilities, dict):
        errors.append("capabilities must be an object")
        capabilities = {}
    for name, raw in capabilities.items():
        if not isinstance(raw, dict):
            errors.append(f"capability {name} must be an object")
            continue
        fixtures = raw.get("fixtures", [])
        if not isinstance(fixtures, list):
            errors.append(f"capability {name}.fixtures must be a list")
            continue
        for fixture in fixtures:
            if str(fixture) not in known:
                unknown_refs.append(f"{name}:{fixture}")
    if unknown_refs:
        errors.append(f"unknown Stage05 fixture references: {sorted(unknown_refs)}")

    policy = matrix.get("capacity_policy", {})
    if not isinstance(policy, dict):
        errors.append("capacity_policy must be an object")
        policy = {}
    if policy.get("historical_call_pool_is_provenance_only") is not True:
        errors.append("historical call-pool evidence must remain provenance only")
    if policy.get("blind_reuse_of_736_746_for_new_source") is not False:
        errors.append("blind reuse of historical 736/746 capacity must remain false")

    return {
        "schema": "s3-benchmarks.bootstrap.stage05-preparedness-audit.v1",
        "stage_id": "05_CALLS_ARRAYS_S3",
        "status": "PASS_PREPARED_NOT_ACTIVE" if not errors else "FAIL",
        "existing_corpus_case_count": len(corpus_ids),
        "prepared_case_count": len(prepared),
        "negative_case_count": len(negative),
        "active_stage05_case_count": len(active_required),
        "prepared_cases_leaked_into_active_map": leaked,
        "errors": errors,
        "activation_authorized": False,
        "promotion_effect": "NONE_PLANNING_AUDIT_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage-map", type=Path, required=True)
    parser.add_argument("--fixture-plan", type=Path, required=True)
    parser.add_argument("--capability-matrix", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = audit(_load(args.stage_map), _load(args.fixture_plan), _load(args.capability_matrix))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE05_PREPAREDNESS_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE05_PREPAREDNESS={report['status']}")
    return 0 if report["status"] == "PASS_PREPARED_NOT_ACTIVE" else 3


if __name__ == "__main__":
    raise SystemExit(main())
