"""Classify S3IR2 v2 conformance failures into likely semantic lanes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

RULES = (
    ("S1_typed_values_and_bindings", ("value", "parameter", "binding", "source identity", "function")),
    ("S2_instruction_def_use", ("instruction", "operand", "result", "def", "use", "semantic shape")),
    ("S3_call_dataflow", ("call", "argument", "callee")),
    ("S4_complete_terminators", ("terminator", "branch3", "jump", "return", "target", "block")),
    ("S5_canonical_serialization", ("header", "mask", "serialization", "record", "parse", "stream")),
)


def classify(report: dict[str, object]) -> dict[str, object]:
    errors = [str(item) for item in report.get("errors", [])]
    scores = {lane: 0 for lane, _ in RULES}
    matched: dict[str, list[str]] = {lane: [] for lane, _ in RULES}
    for error in errors:
        lowered = error.lower()
        for lane, keywords in RULES:
            if any(keyword in lowered for keyword in keywords):
                scores[lane] += 1
                matched[lane].append(error)
    ordered = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    likely = [lane for lane, score in ordered if score > 0]
    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-failure-triage.v1",
        "input_status": report.get("status", "UNKNOWN"),
        "error_count": len(errors),
        "likely_lanes": likely,
        "scores": scores,
        "matched_errors": matched,
        "primary_lane": likely[0] if likely else "UNKNOWN",
        "control_plane_effect": "ADVISORY_ONLY",
        "promotion_effect": "NONE",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("conformance", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = json.loads(args.conformance.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_TRIAGE_ERROR={error}\n")
    result = classify(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PRIMARY_LANE={result['primary_lane']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
