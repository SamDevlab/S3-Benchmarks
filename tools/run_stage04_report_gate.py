"""Normalize a Codex Stage04 report and evaluate it against the frozen gate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tools.evaluate_stage04_expression_checkpoint import evaluate
from tools.normalize_codex_stage04_report import normalize


def run(report_text: str, contract: dict, output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    normalized = normalize(report_text)
    normalized_path = output / "normalized-stage04-checkpoint.json"
    normalized_path.write_text(
        json.dumps(normalized, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    if normalized["normalization_status"] != "PASS":
        evaluation = {
            "schema": "s3-benchmarks.bootstrap.stage04-report-gate.v1",
            "status": "BLOCKED_NORMALIZATION",
            "normalization_status": normalized["normalization_status"],
            "normalization_errors": normalized["normalization_errors"],
            "duplicate_keys": normalized["duplicate_keys"],
            "stage04_gate": "NOT_EVALUATED",
            "next_stage_candidate": None,
            "promotion_effect": "NONE_LABORATORY_GATE_ONLY",
        }
    else:
        gate = evaluate(contract, normalized)
        evaluation = {
            "schema": "s3-benchmarks.bootstrap.stage04-report-gate.v1",
            "status": "PASS" if gate["status"] == "PASS" else "BLOCKED_STAGE04",
            "normalization_status": "PASS",
            "stage04_gate": gate["status"],
            "blocked_fields": gate["blocked_fields"],
            "status_field_failures": gate.get("status_field_failures", []),
            "errors": gate["errors"],
            "candidate_git_sha": gate["candidate_git_sha"],
            "candidate_source_sha256": gate["candidate_source_sha256"],
            "candidate_binary_sha256": gate["candidate_binary_sha256"],
            "control_revision": gate["control_revision"],
            "first_real_blocker": normalized.get("first_real_blocker"),
            "reported_next_stage": normalized.get("reported_next_stage"),
            "next_stage_candidate": gate["next_stage_candidate"],
            "promotion_effect": "NONE_LABORATORY_GATE_ONLY",
        }

    output_path = output / "stage04-gate.json"
    output_path.write_text(
        json.dumps(evaluation, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return evaluation


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        contract = json.loads(args.contract.read_text(encoding="utf-8"))
        if not isinstance(contract, dict):
            raise ValueError("contract must be a JSON object")
        result = run(args.report.read_text(encoding="utf-8"), contract, args.output)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE04_REPORT_GATE_ERROR={error}\n")
    print(f"REPORT_GATE={result['status']}")
    print(f"STAGE04_GATE={result['stage04_gate']}")
    return 0 if result["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
