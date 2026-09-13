"""Triage the first authoritative Stage05 S3IR2 v2 conformance mismatch.

Consumes the JSON emitted by S3's verify_stage1_semantic_conformance_v2.py and
maps only the first error to the smallest Stage05 repair surface. This tool is
triage-only and never promotes S3/S3IR2 completeness.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _classify(error: str) -> tuple[str, str]:
    lowered = error.lower()
    if "candidate stream fails internal s3ir2 v2 verification" in lowered:
        return "STREAM_STRUCTURE", "Fix the first internal stream error before semantic call comparison."
    if "semantic shape mismatch" in lowered and "instruction" in lowered:
        return "CALL_INSTRUCTION_SHAPE", "If this is the CALL instruction, compare opcode 14, result_count, operand_count and ordinal."
    if "result edge count mismatch" in lowered or "result ordinal mismatch" in lowered:
        return "R_RESULT_EDGE", "Repair the call result R definition/ordinal before C/A."
    if "cannot map operand edge" in lowered or "missing mapped operand edge" in lowered:
        return "O_OPERAND_OR_VALUE_MAPPING", "Repair mapped semantic value identity or ordered O edge before A."
    if "missing call record" in lowered:
        return "C_RECORD_ATTACHMENT", "Emit C for the mapped CALL instruction; do not invent a second instruction identity."
    if "call semantic metadata mismatch" in lowered:
        return "C_METADATA", "Compare callee_kind, mapped callee_function_id, argument_count and result_count."
    if "call source identity mismatch" in lowered:
        return "C_SOURCE_SPAN", "Repair exact ASCII callee_name_start/callee_name_length."
    if "cannot map call argument edge" in lowered:
        return "VALUE_MAPPING_BEFORE_A", "The expected argument value is not mapped; inspect V/R/O identity before patching A."
    if "missing mapped call argument" in lowered:
        return "A_ARGUMENT_EDGE", "Repair A instruction id, argument ordinal or mapped semantic value identity."
    if "mapped value" in lowered or "parameter" in lowered or "local binding" in lowered:
        return "UPSTREAM_VALUE_MAPPING", "Repair S1 semantic value mapping before Stage05 call-edge metadata."
    return "UNKNOWN_STAGE05_MISMATCH", "Preserve the exact verifier JSON and inspect only the first error."


def triage(report: dict[str, Any]) -> dict[str, Any]:
    status = report.get("status")
    errors_raw = report.get("errors")
    errors = [str(item) for item in errors_raw] if isinstance(errors_raw, list) else []

    if status == "PASS" and not errors:
        return {
            "schema": "s3-benchmarks.bootstrap.stage05-conformance-triage.v1",
            "status": "NO_MISMATCH",
            "strict_conformance_status": "PASS",
            "first_error": None,
            "first_blocker": None,
            "repair_action": None,
            "continue_broadening": True,
            "promotion_effect": "NONE_TRIAGE_ONLY",
        }

    if not errors:
        return {
            "schema": "s3-benchmarks.bootstrap.stage05-conformance-triage.v1",
            "status": "BLOCKED_NO_ERROR_DETAIL",
            "strict_conformance_status": status,
            "first_error": None,
            "first_blocker": "MISSING_VERIFIER_DETAIL",
            "repair_action": "Re-run the authoritative verifier preserving its JSON errors array.",
            "continue_broadening": False,
            "promotion_effect": "NONE_TRIAGE_ONLY",
        }

    first = errors[0]
    blocker, action = _classify(first)
    return {
        "schema": "s3-benchmarks.bootstrap.stage05-conformance-triage.v1",
        "status": "FIRST_BLOCKER_CLASSIFIED",
        "strict_conformance_status": status,
        "first_error": first,
        "first_blocker": blocker,
        "repair_action": action,
        "remaining_error_count": max(0, len(errors) - 1),
        "continue_broadening": False,
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
        parser.exit(2, f"STAGE05_CONFORMANCE_TRIAGE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"TRIAGE={result['status']}")
    print(f"FIRST_BLOCKER={result['first_blocker']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
