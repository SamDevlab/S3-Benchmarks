"""Triage the first strict S3IR2 v2 conformance mismatch for Stage04.

This tool consumes the JSON emitted by S3's authoritative
verify_stage1_semantic_conformance_v2.py. It never claims semantic PASS itself;
it only maps the first reported mismatch to the smallest likely Stage04 repair
surface so candidate work can remain one-blocker-per-cycle.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


_RULES: tuple[tuple[str, str, str, str], ...] = (
    (
        "candidate stream fails internal S3IR2 v2 verification",
        "STREAM_STRUCTURE",
        "STREAM",
        "Fix the first internal S3IR2 structural/reference error before semantic comparison.",
    ),
    (
        "function count mismatch",
        "FUNCTION_DISCOVERY",
        "S1",
        "Check function/header discovery; do not patch expression lowering first.",
    ),
    (
        "signature metadata mismatch",
        "FUNCTION_SIGNATURE",
        "S1",
        "Check function kind, parameter count and result count metadata.",
    ),
    (
        "function owner mismatch",
        "FUNCTION_OWNERSHIP",
        "S1",
        "Check function ownership IDs/order before value or edge repair.",
    ),
    (
        "function 0 source identity mismatch",
        "FUNCTION_SOURCE_IDENTITY",
        "S1",
        "Check exact function name source span/length.",
    ),
    (
        "source identity mismatch",
        "SOURCE_IDENTITY",
        "S1",
        "Check exact ASCII source span/name for the affected binding/function/callee.",
    ),
    (
        "block count mismatch",
        "BLOCK_DISCOVERY",
        "S2",
        "Check block discovery/order before instruction-shape repair.",
    ),
    (
        "ordinal/instruction-count mismatch",
        "BLOCK_INSTRUCTION_COUNT",
        "S2",
        "Check statement lowering and emitted instruction count/order for this block.",
    ),
    (
        "instruction count mismatch",
        "INSTRUCTION_COUNT",
        "S2",
        "Find the first missing/extra instruction in source order.",
    ),
    (
        "instruction ",
        "INSTRUCTION_SHAPE",
        "S2",
        "Compare instruction ordinal/opcode/result_count/operand_count/aux_b against the hosted oracle.",
    ),
    (
        "parameter value count mismatch",
        "PARAMETER_VALUE_COUNT",
        "S1",
        "Check parameter V rows by declaration order and function ownership.",
    ),
    (
        "parameter value type/mutability mismatch",
        "PARAMETER_METADATA",
        "S1",
        "Check parameter V type/mutability; candidate value IDs may differ.",
    ),
    (
        "parameter source identity mismatch",
        "PARAMETER_SOURCE_IDENTITY",
        "S1",
        "Check exact parameter identifier source span/length.",
    ),
    (
        "missing local binding",
        "LOCAL_BINDING",
        "S1",
        "Emit/fix the separate local-binding V row: owner + exact name/span + type + mutability.",
    ),
    (
        "cannot resolve expected local value",
        "LOCAL_BINDING_OWNER",
        "S1",
        "Check local binding function owner and source identity.",
    ),
    (
        "result edge count mismatch",
        "RESULT_EDGE_COUNT",
        "S2",
        "Fix missing/duplicate R edges for the corresponding instruction.",
    ),
    (
        "result ordinal mismatch",
        "RESULT_EDGE_ORDINAL",
        "S2",
        "Fix R result ordinal ordering.",
    ),
    (
        "mapped value semantic metadata mismatch",
        "VALUE_METADATA",
        "S1",
        "Check mapped V owner/kind/type/mutability; never substitute physical storage identity.",
    ),
    (
        "mapped value missing",
        "VALUE_MISSING",
        "S1",
        "Check that every mapped logical result/binding has a V row.",
    ),
    (
        "missing mapped operand edge",
        "OPERAND_EDGE",
        "S2",
        "Fix O edge value identity or operand ordinal for the mapped instruction.",
    ),
    (
        "cannot map operand edge",
        "OPERAND_VALUE_MAPPING",
        "S1_S2",
        "First fix the missing mapped value/result identity, then re-check the O edge.",
    ),
    (
        "terminator value edge mismatch",
        "RETURN_VALUE_EDGE",
        "S2",
        "For Stage04 return fixtures, map T.return_value_id to the same logical expression result.",
    ),
    (
        "terminator kind mismatch",
        "TERMINATOR_KIND",
        "S4_OR_FIXTURE",
        "If this is a simple Stage04 return fixture, fix RETURN metadata; otherwise defer control-flow repair to Stage06.",
    ),
    (
        "call ",
        "CALL_DATAFLOW",
        "S3",
        "General call-dataflow repair belongs to Stage05; use a non-call Stage04 fixture unless this is a supported numeric cast incorrectly emitted as CALL.",
    ),
    (
        "missing call record",
        "CALL_RECORD",
        "S3",
        "General call records belong to Stage05. Numeric casts must be CONVERT, not CALL.",
    ),
    (
        "missing mapped call argument",
        "CALL_ARGUMENT_EDGE",
        "S3",
        "General call A-edge repair belongs to Stage05.",
    ),
    (
        "terminator target mismatch",
        "CONTROL_FLOW_TARGET",
        "S4",
        "Numeric branch target repair belongs to Stage06.",
    ),
)


def _classify(error: str) -> tuple[str, str, str]:
    lowered = error.lower()
    # Specific instruction-shape errors must be matched before the broad
    # instruction fallback.
    if "instruction" in lowered and "semantic shape mismatch" in lowered:
        return (
            "INSTRUCTION_SHAPE",
            "S2",
            "Compare instruction ordinal/opcode/result_count/operand_count/aux_b against the hosted oracle.",
        )
    if "instruction" in lowered and "owner/block mismatch" in lowered:
        return (
            "INSTRUCTION_OWNER_BLOCK",
            "S2",
            "Check mapped function/block ownership for this instruction.",
        )
    for needle, blocker, lane, action in _RULES:
        if needle.lower() in lowered:
            return blocker, lane, action
    return (
        "UNKNOWN_STRICT_MISMATCH",
        "UNKNOWN",
        "Preserve the exact fixture/stream/verifier JSON and inspect the first mismatch without broad speculative changes.",
    )


def triage(report: dict[str, Any]) -> dict[str, Any]:
    status = report.get("status")
    raw_errors = report.get("errors")
    errors = [str(item) for item in raw_errors] if isinstance(raw_errors, list) else []

    if status == "PASS" and not errors:
        return {
            "schema": "s3-benchmarks.bootstrap.stage04-conformance-triage.v1",
            "status": "NO_MISMATCH",
            "strict_conformance_status": "PASS",
            "first_error": None,
            "first_blocker": None,
            "likely_lane": None,
            "repair_action": None,
            "stage04_actionable": False,
            "promotion_effect": "NONE_TRIAGE_ONLY",
        }

    if not errors:
        return {
            "schema": "s3-benchmarks.bootstrap.stage04-conformance-triage.v1",
            "status": "BLOCKED_NO_ERROR_DETAIL",
            "strict_conformance_status": status,
            "first_error": None,
            "first_blocker": "MISSING_VERIFIER_DETAIL",
            "likely_lane": "UNKNOWN",
            "repair_action": "Re-run the authoritative verifier preserving its JSON errors array.",
            "stage04_actionable": False,
            "promotion_effect": "NONE_TRIAGE_ONLY",
        }

    first = errors[0]
    blocker, lane, action = _classify(first)
    stage04_actionable = lane in {"STREAM", "S1", "S2", "S1_S2"}
    return {
        "schema": "s3-benchmarks.bootstrap.stage04-conformance-triage.v1",
        "status": "FIRST_BLOCKER_CLASSIFIED",
        "strict_conformance_status": status,
        "first_error": first,
        "first_blocker": blocker,
        "likely_lane": lane,
        "repair_action": action,
        "stage04_actionable": stage04_actionable,
        "remaining_error_count": max(0, len(errors) - 1),
        "one_blocker_per_cycle": True,
        "promotion_effect": "NONE_TRIAGE_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("conformance_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        source = json.loads(args.conformance_json.read_text(encoding="utf-8"))
        if not isinstance(source, dict):
            raise ValueError("conformance JSON must be an object")
        result = triage(source)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE04_CONFORMANCE_TRIAGE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"TRIAGE={result['status']}")
    print(f"FIRST_BLOCKER={result['first_blocker']}")
    print(f"LIKELY_LANE={result['likely_lane']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
