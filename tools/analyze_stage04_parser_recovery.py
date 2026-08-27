"""Analyze Stage04 parser-repair attempts without promoting semantic lanes."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

HEX64 = re.compile(r"^[0-9a-f]{64}$")
VALID_STATUS = {"PASS", "BLOCKED_SYNTAX", "BLOCKED_STRUCTURAL", "NOT_RUN"}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def _fingerprint(attempt: dict[str, Any]) -> str | None:
    explicit = attempt.get("diagnostic_fingerprint")
    if isinstance(explicit, str) and explicit:
        return explicit
    code = attempt.get("diagnostic_code")
    cls = attempt.get("diagnostic_class")
    line = attempt.get("diagnostic_line")
    column = attempt.get("diagnostic_column")
    parts: list[str] = []
    if isinstance(code, str) and code:
        parts.append(f"code={code}")
    if isinstance(cls, str) and cls:
        parts.append(f"class={cls}")
    if isinstance(line, int):
        parts.append(f"line={line}")
    if isinstance(column, int):
        parts.append(f"column={column}")
    return "|".join(parts) if parts else None


def analyze(attempts: list[dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []
    rows: list[dict[str, Any]] = []
    consecutive_same_changed_source = 0
    last_fp: str | None = None
    last_source: str | None = None
    stalled = False

    for index, raw in enumerate(attempts):
        attempt_id = raw.get("attempt_id")
        source = raw.get("candidate_source_sha256")
        status = raw.get("parser_status")
        if not isinstance(attempt_id, str) or not attempt_id:
            errors.append(f"attempt {index}: missing attempt_id")
        if not isinstance(source, str) or HEX64.fullmatch(source) is None:
            errors.append(f"attempt {index}: invalid candidate_source_sha256")
        if status not in VALID_STATUS:
            errors.append(f"attempt {index}: invalid parser_status {status!r}")

        fp = _fingerprint(raw)
        if status == "PASS":
            classification = "PARSER_RECOVERED"
            consecutive_same_changed_source = 0
        elif status == "NOT_RUN":
            classification = "NOT_RUN"
            consecutive_same_changed_source = 0
        elif fp is None:
            classification = "BLOCKED_UNCLASSIFIED"
            consecutive_same_changed_source = 0
        elif last_fp is None:
            classification = "INITIAL_BLOCKER"
            consecutive_same_changed_source = 0
        elif source == last_source and fp == last_fp:
            classification = "REOBSERVATION_ONLY"
        elif source != last_source and fp != last_fp:
            classification = "FORWARD_RECOVERY_PROGRESS"
            consecutive_same_changed_source = 0
        elif source != last_source and fp == last_fp:
            consecutive_same_changed_source += 1
            classification = (
                "STALLED_REPAIR"
                if consecutive_same_changed_source >= 2
                else "SAME_BLOCKER_AFTER_CHANGE"
            )
            stalled = stalled or classification == "STALLED_REPAIR"
        else:
            classification = "DIAGNOSTIC_CHANGED_SAME_SOURCE"
            consecutive_same_changed_source = 0

        rows.append(
            {
                "attempt_id": attempt_id,
                "candidate_source_sha256": source,
                "parser_status": status,
                "diagnostic_fingerprint": fp,
                "classification": classification,
            }
        )
        if status != "NOT_RUN":
            last_fp = fp
            last_source = source if isinstance(source, str) else None

    parser_recovered = bool(rows) and rows[-1]["parser_status"] == "PASS"
    if errors:
        status = "INVALID_EVIDENCE"
    elif parser_recovered:
        status = "PARSER_RECOVERED"
    elif stalled:
        status = "STALLED_REPAIR"
    elif any(row["classification"] == "FORWARD_RECOVERY_PROGRESS" for row in rows):
        status = "RECOVERY_PROGRESS"
    else:
        status = "PARSER_BLOCKED"

    return {
        "schema": "s3-benchmarks.bootstrap.stage04-parser-recovery-report.v1",
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "status": status,
        "attempt_count": len(rows),
        "parser_recovered": parser_recovered,
        "stalled_repair_detected": stalled,
        "attempts": rows,
        "errors": errors,
        "expr_parser_syntax_projection": "PASS" if parser_recovered else "BLOCKED",
        "s1_projection": "NOT_EVALUATED_BY_PARSER_RECOVERY",
        "s2_projection": "NOT_EVALUATED_BY_PARSER_RECOVERY",
        "promotion_effect": "NONE_DIAGNOSTIC_TRACKING_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempt", action="append", type=Path, default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        attempts = [_load(path) for path in args.attempt]
        report = analyze(attempts)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE04_PARSER_RECOVERY_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"PARSER_RECOVERY={report['status']}")
    print(f"ATTEMPTS={report['attempt_count']}")
    return 0 if report["status"] not in {"INVALID_EVIDENCE", "STALLED_REPAIR"} else 3


if __name__ == "__main__":
    raise SystemExit(main())
