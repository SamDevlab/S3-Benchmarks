"""Summarize case-level semantic coverage without promoting it to IR closure.

A case PASS demonstrates observable parity for that source only. It never changes
the authoritative semantic surface state imported from Stage1 evidence.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

SURFACES = (
    "typed_values",
    "instruction_def_use",
    "call_dataflow",
    "complete_terminators",
    "canonical_serialization",
)


def summarize(snapshot: dict[str, Any], differential: dict[str, Any]) -> dict[str, Any]:
    rows: dict[str, dict[str, Any]] = {}
    cases = differential.get("cases", [])
    for surface in SURFACES:
        relevant = [case for case in cases if surface in case.get("required_surfaces", [])]
        counts: dict[str, int] = {}
        for case in relevant:
            classification = str(case.get("classification", "UNKNOWN"))
            counts[classification] = counts.get(classification, 0) + 1
        pass_count = counts.get("PASS", 0)
        rows[surface] = {
            "authoritative_ir_state": snapshot.get("semantic_ir", {}).get(surface, "BLOCKED"),
            "applicable_cases": len(relevant),
            "parity_pass_cases": pass_count,
            "case_parity_ratio": (pass_count / len(relevant)) if relevant else None,
            "classifications": dict(sorted(counts.items())),
            "case_evidence_promotes_ir_surface": False,
        }

    total = len(cases)
    passed = sum(1 for case in cases if case.get("classification") == "PASS")
    blocked = sum(1 for case in cases if case.get("classification") == "STAGE1_BLOCKED")
    mismatches = sum(1 for case in cases if case.get("classification") == "SEMANTIC_MISMATCH")
    return {
        "schema": "s3.bootstrap-semantic-coverage.v1",
        "case_count": total,
        "case_parity_pass": passed,
        "case_parity_ratio": (passed / total) if total else None,
        "stage1_blocked_cases": blocked,
        "semantic_mismatches": mismatches,
        "surfaces": rows,
        "interpretation": (
            "Case coverage is differential behavioral evidence only. Authoritative IR closure "
            "continues to come from Stage1 semantic evidence and validators."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--differential", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    differential = json.loads(args.differential.read_text(encoding="utf-8"))
    report = summarize(snapshot, differential)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OUTPUT={args.output}")
    print(f"CASE_PARITY_PASS={report['case_parity_pass']}/{report['case_count']}")
    print(f"SEMANTIC_MISMATCHES={report['semantic_mismatches']}")
    return 2 if report["semantic_mismatches"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
