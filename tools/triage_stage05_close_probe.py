"""Classify the current Stage05 parser probe without semantic promotion.

Input is a text file containing KEY=VALUE lines copied from the paired Codex
checkpoint or raw normalized probe summary. The tool maps the first observed
parse_ok transition to one repair owner. It never mutates S3 and never claims
S3 conformance PASS.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


_TRUE_VALUES = {"-1", "true", "TRUE", "valid", "VALID", "pass", "PASS"}
_FALSE_VALUES = {"0", "false", "FALSE", "invalid", "INVALID", "fail", "FAIL"}


def _parse_lines(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if key:
            result[key] = value
    return result


def _truth(value: str | None) -> bool | None:
    if value is None:
        return None
    if value in _TRUE_VALUES:
        return True
    if value in _FALSE_VALUES:
        return False
    return None


def triage(fields: dict[str, str]) -> dict[str, Any]:
    before_special = _truth(fields.get("BEFORE_SPECIAL_OPEN_PARSE_OK"))
    after_special = _truth(fields.get("AFTER_SPECIAL_OPEN_PARSE_OK"))
    special_open_active = _truth(fields.get("SPECIAL_OPEN_ACTIVE"))
    argument_parse_started = _truth(fields.get("ARGUMENT_PARSE_STARTED"))

    before = _truth(fields.get("BEFORE_CLOSE_PARSE_OK"))
    after = _truth(fields.get("AFTER_CLOSE_PARSE_OK"))
    z_mask_raw = fields.get("Z_MASK")
    try:
        z_mask = int(z_mask_raw) if z_mask_raw is not None else None
    except ValueError:
        z_mask = None

    base: dict[str, Any] = {
        "schema": "s3-benchmarks.bootstrap.stage05-parser-probe-triage.v2",
        "before_special_open_parse_ok": before_special,
        "after_special_open_parse_ok": after_special,
        "special_open_active": special_open_active,
        "argument_parse_started": argument_parse_started,
        "before_close_parse_ok": before,
        "after_close_parse_ok": after,
        "z_mask": z_mask,
        "promotion_effect": "NONE_TRIAGE_ONLY",
        "one_blocker_per_cycle": True,
    }

    # Revision-17 root cause: the Stage05 synthetic open marker is valid parser
    # state, but the legacy operand dispatcher must not consume/reject it as a
    # normal operand before argument parsing begins.
    if (
        special_open_active is True
        and before_special is True
        and after_special is False
        and argument_parse_started is False
    ):
        return {
            **base,
            "status": "FIRST_BLOCKER_CLASSIFIED",
            "classification": "SYNTHETIC_CALL_OPEN_KIND_FALLS_THROUGH_LEGACY_OPERAND_DISPATCH",
            "next_owner": "LEGACY_OPERAND_DISPATCH_SPECIAL_OPEN_GUARD",
            "repair_action": "Guard only the legacy operand-dispatch rejection while stage05_special_open is active; preserve all normal operand behavior and do not modify call-close or comparison truth conventions.",
            "continue_broadening": False,
        }

    if before is False:
        return {
            **base,
            "status": "FIRST_BLOCKER_CLASSIFIED",
            "classification": "ARGUMENT_STOP_OR_TOKEN_BEFORE_RIGHT_PAREN",
            "next_owner": "ARGUMENT_STOP_OR_TOKEN_BEFORE_RIGHT_PAREN",
            "repair_action": "Inspect only the argument-expression stop predicate and token immediately before RIGHT_PAREN. Do not patch call-close bookkeeping yet.",
            "continue_broadening": False,
        }

    if before is True and after is False:
        return {
            **base,
            "status": "FIRST_BLOCKER_CLASSIFIED",
            "classification": "RIGHT_PAREN_CALL_CLOSE",
            "next_owner": "CURRENT_CODE_EQ_2_CALL_CLOSE",
            "repair_action": "Find the first exact close condition that flips parse_ok: arity/argument-complete predicate, single depth decrement, generic RIGHT_PAREN fallthrough, or call-frame restoration. Patch one proven condition only.",
            "continue_broadening": False,
        }

    if before is True and after is True and z_mask == 0:
        return {
            **base,
            "status": "PARSER_CLOSE_CLEARED",
            "classification": "POST_PARSE_FINALIZATION_OR_COMPLETENESS",
            "next_owner": "STRICT_STAGE05_CONFORMANCE_FIRST_MISMATCH",
            "repair_action": "Regenerate a clean candidate and run strict Stage05 conformance before any further parser edit.",
            "continue_broadening": False,
        }

    if before is True and after is True and z_mask == 7:
        return {
            **base,
            "status": "MINIMAL_CALL_MASK_READY",
            "classification": "PARSER_CLOSE_VALID_STAGE05_MASK_READY",
            "next_owner": "STRICT_STAGE05_CONFORMANCE",
            "repair_action": "Run strict Stage05 conformance on the same minimal internal-call fixture. Do not infer semantic PASS from Z 7 alone.",
            "continue_broadening": False,
        }

    return {
        **base,
        "status": "BLOCKED_INCOMPLETE_EVIDENCE",
        "classification": "INSUFFICIENT_PARSER_PROBE",
        "next_owner": "PRESERVE_RAW_PROBE",
        "repair_action": "Provide either the special-open before/after state or the close before/after state from one run before choosing a repair.",
        "continue_broadening": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("probe_text", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    try:
        fields = _parse_lines(args.probe_text.read_text(encoding="utf-8"))
        result = triage(fields)
    except OSError as error:
        parser.exit(2, f"STAGE05_PARSER_TRIAGE_ERROR={error}\n")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"TRIAGE={result['status']}")
    print(f"CLASSIFICATION={result['classification']}")
    print(f"NEXT_OWNER={result['next_owner']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
