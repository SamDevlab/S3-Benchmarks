"""Render a compact human-readable Stage04 gate summary from normalized JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def render(report: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"REPORT_GATE={report.get('status', 'UNKNOWN')}")
    lines.append(f"STAGE04_GATE={report.get('stage04_gate', 'UNKNOWN')}")
    lines.append(f"CONTROL_REVISION={report.get('control_revision', 'UNKNOWN')}")
    lines.append(f"CANDIDATE_GIT_SHA={report.get('candidate_git_sha') or 'UNKNOWN'}")
    lines.append(f"CANDIDATE_SOURCE_SHA256={report.get('candidate_source_sha256') or 'UNKNOWN'}")
    lines.append(f"CANDIDATE_BINARY_SHA256={report.get('candidate_binary_sha256') or 'NOT_RECORDED'}")

    blocked = report.get("blocked_fields", [])
    if isinstance(blocked, list):
        lines.append("BLOCKED_FIELDS=" + (",".join(str(item) for item in blocked) if blocked else "NONE"))
    else:
        lines.append("BLOCKED_FIELDS=INVALID")

    status_failures = report.get("status_field_failures", [])
    if isinstance(status_failures, list) and status_failures:
        rendered = []
        for item in status_failures:
            if isinstance(item, dict):
                rendered.append(
                    f"{item.get('field')}:{item.get('observed')} not-in {item.get('allowed')}"
                )
            else:
                rendered.append(str(item))
        lines.append("STATUS_FIELD_FAILURES=" + " | ".join(rendered))
    else:
        lines.append("STATUS_FIELD_FAILURES=NONE")

    errors = report.get("errors") or report.get("normalization_errors") or []
    if isinstance(errors, list):
        lines.append("ERRORS=" + (" | ".join(str(item) for item in errors) if errors else "NONE"))
    else:
        lines.append("ERRORS=INVALID")

    lines.append(f"FIRST_REAL_BLOCKER={report.get('first_real_blocker') or 'NOT_RECORDED'}")
    lines.append(f"REPORTED_NEXT_STAGE={report.get('reported_next_stage') or 'NONE'}")
    lines.append(f"LAB_NEXT_STAGE_CANDIDATE={report.get('next_stage_candidate') or 'NONE'}")
    lines.append("PROMOTION_EFFECT=NONE")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("gate_json", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        value = json.loads(args.gate_json.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("gate JSON must be an object")
        text = render(value)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"STAGE04_SUMMARY_ERROR={error}\n")
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
