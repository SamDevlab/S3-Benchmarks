"""Compare two S3IR2 v2 campaign reports and fail closed on regressions.

The comparison is candidate-relative laboratory evidence. It does not promote a
compiler. A regression is any previously passing structural, semantic, or
required-determinism case that ceases to pass in the newer campaign, or a stage
that falls from PASS_EVIDENCE_SET.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _case_map(stage: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(row["case_id"]): row
        for row in stage.get("cases", [])
        if isinstance(row, dict) and "case_id" in row
    }


def compare(baseline: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    regressions: list[dict[str, str]] = []
    improvements: list[dict[str, str]] = []

    baseline_stages = baseline.get("stages", {})
    candidate_stages = candidate.get("stages", {})
    for stage_id, old_stage in baseline_stages.items():
        new_stage = candidate_stages.get(stage_id)
        if not isinstance(new_stage, dict):
            regressions.append({
                "stage": str(stage_id),
                "case": "*",
                "dimension": "stage_presence",
                "before": str(old_stage.get("status", "UNKNOWN")),
                "after": "MISSING",
            })
            continue

        old_status = str(old_stage.get("status", "UNKNOWN"))
        new_status = str(new_stage.get("status", "UNKNOWN"))
        if old_status == "PASS_EVIDENCE_SET" and new_status != "PASS_EVIDENCE_SET":
            regressions.append({
                "stage": str(stage_id),
                "case": "*",
                "dimension": "stage_status",
                "before": old_status,
                "after": new_status,
            })
        elif old_status != "PASS_EVIDENCE_SET" and new_status == "PASS_EVIDENCE_SET":
            improvements.append({
                "stage": str(stage_id),
                "case": "*",
                "dimension": "stage_status",
                "before": old_status,
                "after": new_status,
            })

        old_cases = _case_map(old_stage)
        new_cases = _case_map(new_stage)
        for case_id, old_case in old_cases.items():
            new_case = new_cases.get(case_id)
            if new_case is None:
                regressions.append({
                    "stage": str(stage_id),
                    "case": case_id,
                    "dimension": "case_presence",
                    "before": "PRESENT",
                    "after": "MISSING",
                })
                continue
            dimensions = (
                ("structural_status", "PASS"),
                ("semantic_conformance_status", "PASS"),
            )
            for dimension, passing in dimensions:
                before = str(old_case.get(dimension, "UNKNOWN"))
                after = str(new_case.get(dimension, "UNKNOWN"))
                if before == passing and after != passing:
                    regressions.append({
                        "stage": str(stage_id),
                        "case": case_id,
                        "dimension": dimension,
                        "before": before,
                        "after": after,
                    })
                elif before != passing and after == passing:
                    improvements.append({
                        "stage": str(stage_id),
                        "case": case_id,
                        "dimension": dimension,
                        "before": before,
                        "after": after,
                    })

            if stage_id == "07_SERIALIZATION_S5":
                before = str(old_case.get("determinism_status", "UNKNOWN"))
                after = str(new_case.get("determinism_status", "UNKNOWN"))
                if before == "PASS" and after != "PASS":
                    regressions.append({
                        "stage": str(stage_id),
                        "case": case_id,
                        "dimension": "determinism_status",
                        "before": before,
                        "after": after,
                    })
                elif before != "PASS" and after == "PASS":
                    improvements.append({
                        "stage": str(stage_id),
                        "case": case_id,
                        "dimension": "determinism_status",
                        "before": before,
                        "after": after,
                    })

    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-campaign-compare.v1",
        "regression_gate": "FAIL" if regressions else "PASS",
        "regression_count": len(regressions),
        "improvement_count": len(improvements),
        "regressions": regressions,
        "improvements": improvements,
        "promotion_effect": "NONE_REGRESSION_SIGNAL_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
        report = compare(baseline, candidate)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_COMPARE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"REGRESSION_GATE={report['regression_gate']}")
    print(f"REGRESSIONS={report['regression_count']}")
    return 0 if report["regression_gate"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
