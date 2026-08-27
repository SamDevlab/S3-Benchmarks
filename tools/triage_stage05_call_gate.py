"""Classify the Stage05 internal-call gate without promoting semantic completeness.

Consumes KEY=VALUE summaries from Codex. Masks are routing evidence only; strict
conformance remains authoritative for call semantics.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _parse(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        out[key.strip()] = value.strip()
    return out


def _int(value: str | None) -> int | None:
    try:
        return int(value) if value is not None else None
    except ValueError:
        return None


def triage(fields: dict[str, str]) -> dict[str, Any]:
    masks = {
        "zero": _int(fields.get("ZERO_ARG_Z_MASK")),
        "one": _int(fields.get("ONE_ARG_Z_MASK")),
        "two": _int(fields.get("TWO_ARG_Z_MASK")),
    }
    strict = (fields.get("STRICT_CONFORMANCE_STATUS") or "NOT_RUN").upper()
    first_error = fields.get("STRICT_FIRST_ERROR", "")
    base = {
        "schema": "s3-benchmarks.bootstrap.stage05-call-gate-triage.v1",
        "masks": masks,
        "strict_conformance_status": strict,
        "promotion_effect": "NONE_TRIAGE_ONLY",
        "arrays_unlocked": False,
        "foreign_calls_unlocked": False,
    }

    observed = [value for value in masks.values() if value is not None]
    if any(value == 0 for value in observed):
        return {**base, "classification": "VALID_CALL_REGRESSION_OR_FAIL_CLOSED", "next_owner": "FIRST_Z0_FIXTURE", "action": "Stop on the first valid call that returned Z0 and preserve its raw stream; do not open arrays."}

    if strict in {"FAIL", "FAILED"}:
        return {**base, "classification": "STRICT_CALL_CONFORMANCE_MISMATCH", "next_owner": "STRICT_ERRORS_0", "first_error": first_error, "action": "Fix only verifier errors[0]; keep arrays and foreign calls locked."}

    if strict == "PASS" and observed and any(value == 3 for value in observed):
        return {**base, "classification": "CALL_SEMANTICS_PASS_S3_MASK_NOT_CLAIMED", "next_owner": "STAGE05_S3_COMPLETENESS_PREDICATE", "action": "Inspect only the candidate Stage05/S3 completeness predicate. Determine the unset required condition; do not force bit 4."}

    if strict == "PASS" and observed and all(value == 7 for value in observed):
        return {**base, "classification": "INTERNAL_CALL_GATE_READY", "next_owner": "NEXT_INTERNAL_CALL_REGRESSION", "action": "Continue nested/result-reuse/unresolved internal-call regressions on the same binary. Arrays remain locked until the internal matrix is stable."}

    if observed and all(value in {3, 7} for value in observed):
        return {**base, "classification": "RUN_STRICT_CONFORMANCE_BEFORE_ARRAYS", "next_owner": "STRICT_STAGE05_CONFORMANCE_ONE_ARG", "action": "Run the current stage-local strict conformance gate on the one-argument fixture before any arrays or foreign-call edit."}

    return {**base, "classification": "INCOMPLETE_CALL_GATE_EVIDENCE", "next_owner": "PRESERVE_CURRENT_BUILD_RESULTS", "action": "Provide zero/one/two argument masks and strict status before broadening."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("summary", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = triage(_parse(args.summary.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"CLASSIFICATION={result['classification']}")
    print(f"NEXT_OWNER={result['next_owner']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
