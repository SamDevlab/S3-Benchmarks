"""Audit whether every Stage04 semantic capability has a pinned focused fixture."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def audit(matrix: dict[str, Any]) -> dict[str, Any]:
    capabilities = matrix.get("capabilities")
    if not isinstance(capabilities, dict):
        raise ValueError("capabilities must be an object")

    pinned: list[str] = []
    partial: list[str] = []
    missing: list[str] = []
    invalid: list[str] = []
    rows: list[dict[str, Any]] = []

    for name, raw in sorted(capabilities.items()):
        if not isinstance(raw, dict):
            invalid.append(str(name))
            continue
        status = str(raw.get("fixture_status", "UNKNOWN"))
        fixtures = raw.get("fixtures")
        if not isinstance(fixtures, list):
            fixtures = []
            invalid.append(str(name))
        if status == "PINNED":
            if fixtures:
                pinned.append(str(name))
            else:
                invalid.append(str(name))
        elif status == "PARTIAL_PINNED":
            partial.append(str(name))
        elif status == "FIXTURE_NOT_YET_PINNED":
            missing.append(str(name))
        else:
            invalid.append(str(name))
        rows.append({
            "capability": str(name),
            "fixture_status": status,
            "fixtures": list(fixtures),
        })

    complete = not partial and not missing and not invalid and bool(rows)
    return {
        "schema": "s3-benchmarks.bootstrap.stage04-fixture-audit.v1",
        "stage_id": matrix.get("stage_id"),
        "status": "PASS" if complete else "INCOMPLETE_FIXTURE_COVERAGE",
        "capability_count": len(rows),
        "pinned_count": len(pinned),
        "partial_count": len(partial),
        "missing_count": len(missing),
        "invalid_count": len(invalid),
        "pinned_capabilities": pinned,
        "partial_capabilities": partial,
        "missing_capabilities": missing,
        "invalid_capabilities": invalid,
        "capabilities": rows,
        "promotion_effect": "NONE_FIXTURE_PLANNING_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        value = json.loads(args.matrix.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("matrix must be JSON object")
        report = audit(value)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE04_FIXTURE_AUDIT_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE04_FIXTURE_COVERAGE={report['status']}")
    print(f"PINNED={report['pinned_count']}")
    print(f"PARTIAL={report['partial_count']}")
    print(f"MISSING={report['missing_count']}")
    return 0 if report["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
