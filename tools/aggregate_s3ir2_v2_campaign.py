"""Aggregate S3IR2 v2 evidence manifests against the frozen stage map.

This is a laboratory summary only. It never authorizes canonical Stage1 mutation
or bootstrap promotion. A stage can be marked evidence-PASS only when every
required mapped case is present and has strict S3 semantic conformance PASS.
Stage 07 additionally requires deterministic repeated bytes for every case.
The full campaign requires every mapped stage to be evidence-PASS.
"""

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


def aggregate(stage_map: dict[str, Any], case_manifests: dict[str, dict[str, Any]]) -> dict[str, Any]:
    stages: dict[str, Any] = {}
    for stage_id, stage in stage_map["stages"].items():
        required = list(stage["required_cases"])
        missing = [case_id for case_id in required if case_id not in case_manifests]
        structural_fail = []
        conformance_fail = []
        determinism_fail = []
        case_rows: list[dict[str, Any]] = []
        for case_id in required:
            manifest = case_manifests.get(case_id)
            if manifest is None:
                case_rows.append({"case_id": case_id, "status": "MISSING"})
                continue
            structural = str(manifest.get("structural_status", "UNKNOWN"))
            semantic = str(manifest.get("semantic_conformance_status", "UNKNOWN"))
            determinism = str(manifest.get("determinism_status", "NOT_EVALUATED"))
            if structural != "PASS":
                structural_fail.append(case_id)
            if semantic != "PASS":
                conformance_fail.append(case_id)
            if stage_id == "07_SERIALIZATION_S5" and determinism != "PASS":
                determinism_fail.append(case_id)
            case_rows.append({
                "case_id": case_id,
                "structural_status": structural,
                "semantic_conformance_status": semantic,
                "determinism_status": determinism,
                "qualification_gate": manifest.get("qualification_gate", "UNKNOWN"),
            })

        if missing:
            status = "INCOMPLETE_EVIDENCE"
        elif structural_fail:
            status = "STRUCTURAL_FAIL"
        elif conformance_fail:
            status = "SEMANTIC_CONFORMANCE_BLOCKED"
        elif determinism_fail:
            status = "DETERMINISM_BLOCKED"
        else:
            status = "PASS_EVIDENCE_SET"

        stages[stage_id] = {
            "status": status,
            "required_case_count": len(required),
            "observed_case_count": len(required) - len(missing),
            "missing_cases": missing,
            "structural_fail_cases": structural_fail,
            "conformance_fail_cases": conformance_fail,
            "determinism_fail_cases": determinism_fail,
            "gate_focus": list(stage.get("gate_focus", [])),
            "cases": case_rows,
        }

    all_stages_pass = bool(stages) and all(
        stage["status"] == "PASS_EVIDENCE_SET" for stage in stages.values()
    )
    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-campaign.v1",
        "protocol": "S3IR2 v2",
        "stages": stages,
        "full_v2_fixture_campaign": "PASS" if all_stages_pass else "BLOCKED",
        "promotion_effect": "NONE_LABORATORY_SUMMARY_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage-map", type=Path, required=True)
    parser.add_argument(
        "--case-manifest",
        action="append",
        default=[],
        metavar="CASE_ID=PATH",
        help="Evidence-set manifest for one deterministic corpus case.",
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    try:
        stage_map = _load(args.stage_map)
        manifests: dict[str, dict[str, Any]] = {}
        for item in args.case_manifest:
            case_id, sep, raw_path = item.partition("=")
            if not sep or not case_id or not raw_path:
                raise ValueError(f"invalid --case-manifest {item!r}; expected CASE_ID=PATH")
            if case_id in manifests:
                raise ValueError(f"duplicate case manifest: {case_id}")
            manifests[case_id] = _load(Path(raw_path))
        report = aggregate(stage_map, manifests)
    except (OSError, ValueError, json.JSONDecodeError, KeyError) as error:
        parser.exit(2, f"S3IR2_CAMPAIGN_ERROR={error}\n")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"FULL_V2_FIXTURE_CAMPAIGN={report['full_v2_fixture_campaign']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
