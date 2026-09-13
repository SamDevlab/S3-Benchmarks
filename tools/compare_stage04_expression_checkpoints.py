"""Compare two normalized Stage04 checkpoints without requiring total stage PASS."""

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


def compare(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    if before.get("stage_id") != "04_EXPRESSIONS_S1_S2":
        raise ValueError("baseline is not a Stage04 checkpoint")
    if after.get("stage_id") != "04_EXPRESSIONS_S1_S2":
        raise ValueError("candidate is not a Stage04 checkpoint")

    old_gates = before.get("gates") if isinstance(before.get("gates"), dict) else {}
    new_gates = after.get("gates") if isinstance(after.get("gates"), dict) else {}
    gate_names = sorted(set(old_gates) | set(new_gates))

    improvements: list[dict[str, str]] = []
    regressions: list[dict[str, str]] = []
    unchanged: list[dict[str, str]] = []
    not_reobserved: list[dict[str, str]] = []

    for gate in gate_names:
        old = str(old_gates.get(gate, "MISSING"))
        new = str(new_gates.get(gate, "MISSING"))
        row = {"gate": gate, "before": old, "after": new}
        if new in {"MISSING", "NOT_RECORDED", "NOT_REOBSERVED"} and old == "PASS":
            not_reobserved.append(row)
        elif old == "PASS" and new != "PASS":
            regressions.append(row)
        elif old != "PASS" and new == "PASS":
            improvements.append(row)
        else:
            unchanged.append(row)

    old_identity = {
        "candidate_git_sha": before.get("candidate_git_sha"),
        "candidate_source_sha256": before.get("candidate_source_sha256"),
        "candidate_binary_sha256": before.get("candidate_binary_sha256"),
    }
    new_identity = {
        "candidate_git_sha": after.get("candidate_git_sha"),
        "candidate_source_sha256": after.get("candidate_source_sha256"),
        "candidate_binary_sha256": after.get("candidate_binary_sha256"),
    }

    return {
        "schema": "s3-benchmarks.bootstrap.stage04-expression-compare.v1",
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "baseline_identity": old_identity,
        "candidate_identity": new_identity,
        "improvements": improvements,
        "regressions": regressions,
        "not_reobserved": not_reobserved,
        "unchanged": unchanged,
        "improvement_count": len(improvements),
        "regression_count": len(regressions),
        "not_reobserved_count": len(not_reobserved),
        "regression_gate": "FAIL" if regressions else "PASS",
        "promotion_effect": "NONE_PROGRESS_SIGNAL_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = compare(_load(args.baseline), _load(args.candidate))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE04_COMPARE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STAGE04_REGRESSION_GATE={report['regression_gate']}")
    print(f"IMPROVEMENTS={report['improvement_count']}")
    print(f"REGRESSIONS={report['regression_count']}")
    return 0 if report["regression_gate"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
