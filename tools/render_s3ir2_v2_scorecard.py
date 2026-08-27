"""Render a fail-closed S3IR2 v2 qualification scorecard.

This tool deliberately separates what the candidate stream *declares* from what
SamDevlab/S3's strict conformance verifier has actually proven. It never promotes
S1-S5 from a completeness bit alone.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

LANES = (
    "S1_typed_values_and_bindings",
    "S2_instruction_def_use",
    "S3_call_dataflow",
    "S4_complete_terminators",
    "S5_canonical_serialization",
)


def build_scorecard(
    ingest: dict[str, Any],
    *,
    conformance: dict[str, Any] | None = None,
    determinism: dict[str, Any] | None = None,
) -> dict[str, Any]:
    structural = str(ingest.get("structural_status", "UNKNOWN"))
    semantic = (
        str(conformance.get("status", "UNKNOWN"))
        if conformance is not None
        else "NOT_EVALUATED"
    )
    deterministic = (
        str(determinism.get("status", "UNKNOWN"))
        if determinism is not None
        else "NOT_EVALUATED"
    )

    dimensions: dict[str, Any] = {}
    for lane in LANES:
        declared = str(ingest.get("lanes", {}).get(lane, "BLOCKED"))
        proven = "BLOCKED"
        if declared == "PASS_DECLARED" and structural == "PASS" and semantic == "PASS":
            proven = "PASS"
        dimensions[lane] = {
            "declared": declared,
            "structural": structural,
            "semantic_conformance": semantic,
            "proven": proven,
        }

    all_lanes = all(row["proven"] == "PASS" for row in dimensions.values())
    s5_deterministic = deterministic == "PASS"
    qualification = (
        "PASS"
        if all_lanes and s5_deterministic
        else "BLOCKED"
    )

    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-scorecard.v1",
        "protocol": "S3IR2 v2",
        "stream_sha256": ingest.get("stream_sha256"),
        "source_sha256": ingest.get("source_sha256"),
        "completeness_mask": ingest.get("completeness_mask"),
        "dimensions": dimensions,
        "structural_status": structural,
        "semantic_conformance_status": semantic,
        "determinism_status": deterministic,
        "all_five_lanes_proven": all_lanes,
        "s5_deterministic_repeat_proven": s5_deterministic,
        "qualification_gate": qualification,
        "promotion_effect": "NONE_LABORATORY_EVIDENCE_ONLY",
        "single_numeric_score": None,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ingest", type=Path, required=True)
    parser.add_argument("--conformance", type=Path)
    parser.add_argument("--determinism", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    ingest = json.loads(args.ingest.read_text(encoding="utf-8"))
    conformance = (
        json.loads(args.conformance.read_text(encoding="utf-8"))
        if args.conformance is not None
        else None
    )
    determinism = (
        json.loads(args.determinism.read_text(encoding="utf-8"))
        if args.determinism is not None
        else None
    )
    report = build_scorecard(
        ingest,
        conformance=conformance,
        determinism=determinism,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"QUALIFICATION_GATE={report['qualification_gate']}")
    print(f"SEMANTIC_CONFORMANCE={report['semantic_conformance_status']}")
    print(f"DETERMINISM={report['determinism_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
