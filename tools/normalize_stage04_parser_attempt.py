"""Normalize one Stage04 parser-recovery KEY=VALUE attempt conservatively."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

HEX64 = re.compile(r"^[0-9a-f]{64}$")
KEY_RE = re.compile(r"^[A-Z0-9_]+$")
VALID_STATUS = {"PASS", "BLOCKED_SYNTAX", "BLOCKED_STRUCTURAL", "NOT_RUN"}


def _parse(text: str) -> tuple[dict[str, str], list[str]]:
    values: dict[str, str] = {}
    duplicates: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if KEY_RE.fullmatch(key) is None:
            continue
        if key in values:
            duplicates.append(key)
        values[key] = value
    return values, duplicates


def _optional_int(values: dict[str, str], key: str, errors: list[str]) -> int | None:
    raw = values.get(key)
    if raw is None or raw == "":
        return None
    try:
        value = int(raw)
    except ValueError:
        errors.append(f"{key} is not an integer")
        return None
    if value < 0:
        errors.append(f"{key} must be non-negative")
        return None
    return value


def normalize(text: str) -> dict[str, Any]:
    values, duplicates = _parse(text)
    errors: list[str] = []

    attempt_id = values.get("PARSER_ATTEMPT_ID")
    if not attempt_id:
        errors.append("PARSER_ATTEMPT_ID missing")

    source = values.get("CANDIDATE_SOURCE_SHA256")
    if source is None or HEX64.fullmatch(source) is None:
        errors.append("CANDIDATE_SOURCE_SHA256 must be 64 lowercase hex characters")

    status_raw = values.get("PARSER_STATUS")
    if status_raw is None or not status_raw.strip():
        errors.append("PARSER_STATUS missing")
        status = "MISSING"
    else:
        status = status_raw.upper()
        aliases = {
            "BLOCKED": "BLOCKED_SYNTAX",
            "SYNTAX_BLOCKED": "BLOCKED_SYNTAX",
            "STRUCTURAL_BLOCKED": "BLOCKED_STRUCTURAL",
            "NOT RUN": "NOT_RUN",
        }
        status = aliases.get(status, status)
        if status not in VALID_STATUS:
            errors.append(f"PARSER_STATUS invalid: {status}")

    line = _optional_int(values, "DIAGNOSTIC_LINE", errors)
    column = _optional_int(values, "DIAGNOSTIC_COLUMN", errors)

    report = {
        "schema": "s3-benchmarks.bootstrap.stage04-parser-attempt.v1",
        "attempt_id": attempt_id,
        "candidate_source_sha256": source,
        "parser_status": status,
        "diagnostic_code": values.get("DIAGNOSTIC_CODE") or None,
        "diagnostic_line": line,
        "diagnostic_column": column,
        "diagnostic_class": values.get("DIAGNOSTIC_CLASS") or None,
        "diagnostic_fingerprint": values.get("DIAGNOSTIC_FINGERPRINT") or None,
        "note": values.get("PARSER_NOTE") or None,
        "duplicate_keys": sorted(set(duplicates)),
        "normalization_errors": errors,
        "normalization_status": "PASS" if not errors and not duplicates else "BLOCKED",
        "evidence_policy": "KEY_VALUE_ONLY_NO_PROSE_INFERENCE",
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = normalize(args.report.read_text(encoding="utf-8"))
    except OSError as error:
        parser.exit(2, f"STAGE04_PARSER_ATTEMPT_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"NORMALIZATION={report['normalization_status']}")
    print(f"PARSER_STATUS={report['parser_status']}")
    return 0 if report["normalization_status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
