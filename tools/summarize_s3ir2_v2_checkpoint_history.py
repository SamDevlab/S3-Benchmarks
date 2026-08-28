"""Summarize immutable S3IR2 v2 checkpoints across candidate revisions.

Checkpoint order is explicit: the order of --checkpoint arguments defines the
observed history. Git SHAs are identifiers, never sorted numerically or
lexicographically to infer time. A previously passing case is only marked lost
when the newer candidate re-observes that same case and it no longer passes;
missing reruns are reported separately as not re-observed.
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


def summarize(stage_map: dict[str, Any], checkpoints: list[dict[str, Any]]) -> dict[str, Any]:
    required_by_stage = {
        str(stage_id): set(str(case_id) for case_id in stage.get("required_cases", []))
        for stage_id, stage in stage_map.get("stages", {}).items()
        if isinstance(stage, dict)
    }

    candidate_order: list[str] = []
    candidates: dict[str, dict[str, Any]] = {}
    errors: list[str] = []

    for sequence, checkpoint in enumerate(checkpoints):
        if checkpoint.get("schema") != "s3-benchmarks.bootstrap.s3ir2-v2-checkpoint.v1":
            errors.append(f"checkpoint {sequence}: invalid schema")
            continue
        candidate_sha = checkpoint.get("candidate_git_sha")
        source_sha = checkpoint.get("candidate_source_sha256")
        binary_sha = checkpoint.get("candidate_binary_sha256")
        stage_id = str(checkpoint.get("stage_id", ""))
        case_id = str(checkpoint.get("case_id", ""))
        evidence = checkpoint.get("evidence_manifest")
        if not isinstance(candidate_sha, str) or not candidate_sha:
            errors.append(f"checkpoint {sequence}: missing candidate_git_sha")
            continue
        if not isinstance(evidence, dict):
            errors.append(f"checkpoint {sequence}: missing evidence_manifest")
            continue

        if candidate_sha not in candidates:
            candidate_order.append(candidate_sha)
            candidates[candidate_sha] = {
                "candidate_git_sha": candidate_sha,
                "candidate_source_sha256": source_sha,
                "candidate_binary_sha256": binary_sha,
                "control_revision": checkpoint.get("control_revision"),
                "first_sequence": sequence,
                "last_sequence": sequence,
                "cases": {},
            }
        candidate = candidates[candidate_sha]
        candidate["last_sequence"] = sequence
        for field, value in (
            ("candidate_source_sha256", source_sha),
            ("candidate_binary_sha256", binary_sha),
            ("control_revision", checkpoint.get("control_revision")),
        ):
            current = candidate.get(field)
            if current is None:
                candidate[field] = value
            elif value is not None and current != value:
                errors.append(
                    f"checkpoint {sequence}: candidate {candidate_sha} changes {field}"
                )

        case_key = f"{stage_id}:{case_id}"
        if case_key in candidate["cases"]:
            errors.append(
                f"checkpoint {sequence}: duplicate case checkpoint for {candidate_sha} {case_key}"
            )
            continue
        candidate["cases"][case_key] = {
            "stage_id": stage_id,
            "case_id": case_id,
            "sequence": sequence,
            "structural_status": evidence.get("structural_status", "UNKNOWN"),
            "native_provenance_status": evidence.get("native_provenance_status", "UNKNOWN"),
            "semantic_conformance_status": evidence.get("semantic_conformance_status", "UNKNOWN"),
            "determinism_status": evidence.get("determinism_status", "NOT_EVALUATED"),
            "qualification_gate": evidence.get("qualification_gate", "UNKNOWN"),
        }

    timeline: list[dict[str, Any]] = []
    previous_passed_cases: set[str] = set()
    for ordinal, candidate_sha in enumerate(candidate_order):
        candidate = candidates[candidate_sha]
        stages: dict[str, Any] = {}
        observed_case_keys = set(candidate["cases"])
        passing_case_keys = {
            key
            for key, row in candidate["cases"].items()
            if row.get("qualification_gate") == "PASS"
        }
        for stage_id, required_cases in required_by_stage.items():
            observed_rows = [
                row
                for row in candidate["cases"].values()
                if row.get("stage_id") == stage_id
            ]
            observed_cases = {str(row.get("case_id")) for row in observed_rows}
            passing_cases = {
                str(row.get("case_id"))
                for row in observed_rows
                if row.get("qualification_gate") == "PASS"
            }
            missing = sorted(required_cases - observed_cases)
            failing = sorted(
                str(row.get("case_id"))
                for row in observed_rows
                if row.get("qualification_gate") != "PASS"
            )
            if missing:
                status = "INCOMPLETE_EVIDENCE"
            elif failing:
                status = "BLOCKED"
            elif required_cases and required_cases <= passing_cases:
                status = "PASS_EVIDENCE_SET"
            else:
                status = "NO_REQUIRED_CASES"
            stages[stage_id] = {
                "status": status,
                "required_cases": sorted(required_cases),
                "observed_cases": sorted(observed_cases),
                "passing_cases": sorted(passing_cases),
                "missing_cases": missing,
                "blocked_cases": failing,
            }

        newly_passing = sorted(passing_case_keys - previous_passed_cases)
        reobserved_previous = previous_passed_cases & observed_case_keys
        lost_passing = sorted(reobserved_previous - passing_case_keys)
        not_reobserved = sorted(previous_passed_cases - observed_case_keys)
        timeline.append({
            "ordinal": ordinal,
            "candidate_git_sha": candidate_sha,
            "candidate_source_sha256": candidate.get("candidate_source_sha256"),
            "candidate_binary_sha256": candidate.get("candidate_binary_sha256"),
            "control_revision": candidate.get("control_revision"),
            "first_sequence": candidate.get("first_sequence"),
            "last_sequence": candidate.get("last_sequence"),
            "stage_status": stages,
            "passing_case_count": len(passing_case_keys),
            "newly_passing_cases": newly_passing,
            "lost_passing_cases": lost_passing,
            "not_reobserved_previous_pass_cases": not_reobserved,
        })
        previous_passed_cases = passing_case_keys

    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-checkpoint-history.v1",
        "candidate_count": len(timeline),
        "checkpoint_count": len(checkpoints),
        "ordering_policy": "EXPLICIT_CHECKPOINT_ARGUMENT_ORDER",
        "timeline": timeline,
        "errors": errors,
        "status": "PASS" if not errors else "FAIL",
        "promotion_effect": "NONE_HISTORY_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage-map", type=Path, required=True)
    parser.add_argument("--checkpoint", action="append", type=Path, default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        stage_map = _load(args.stage_map)
        checkpoints = [_load(path) for path in args.checkpoint]
        report = summarize(stage_map, checkpoints)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_HISTORY_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STATUS={report['status']}")
    print(f"CANDIDATES={report['candidate_count']}")
    print(f"CHECKPOINTS={report['checkpoint_count']}")
    return 0 if report["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
