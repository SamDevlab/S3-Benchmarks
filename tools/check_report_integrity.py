#!/usr/bin/env python3
"""Validate that benchmark prose does not overstate available measurements."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED_COMPARATIVE_VARIANTS = {
    "C-GCC-O2",
    "S3-O0-NATIVE",
    "S3-O1-NATIVE",
}

FORBIDDEN_WITHOUT_COMPARATIVE_DATA = (
    "yield a measurable reduction",
    "measured native performance under internal parse loop stress provides",
    "demonstrates a performance improvement",
    "demonstrates a performance advantage",
)


def _has_positive_timing(row: object) -> bool:
    if not isinstance(row, dict):
        return False
    value = row.get("median_ns_per_parse")
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def validate_report(json_path: Path, markdown_path: Path) -> list[str]:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    markdown = markdown_path.read_text(encoding="utf-8")
    markdown_lower = markdown.lower()

    measured_results = [row for row in data.get("results", []) if _has_positive_timing(row)]
    measured_variants = {
        row.get("variant")
        for row in measured_results
        if isinstance(row.get("variant"), str)
    }
    comparative_available = REQUIRED_COMPARATIVE_VARIANTS.issubset(measured_variants)

    errors: list[str] = []
    if not comparative_available:
        for phrase in FORBIDDEN_WITHOUT_COMPARATIVE_DATA:
            if phrase in markdown_lower:
                errors.append(
                    f"performance claim present without comparative native data: {phrase!r}"
                )

        if "performance_data_available**: no" not in markdown_lower:
            errors.append(
                "report without comparative native data must declare PERFORMANCE_DATA_AVAILABLE: NO"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reject benchmark reports whose prose overstates available timing data."
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=Path("reports/jsmn-baseline.json"),
        help="benchmark JSON report",
    )
    parser.add_argument(
        "--markdown",
        type=Path,
        default=Path("reports/jsmn-baseline.md"),
        help="benchmark Markdown report",
    )
    args = parser.parse_args()

    errors = validate_report(args.json, args.markdown)
    if errors:
        print("REPORT_INTEGRITY: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("REPORT_INTEGRITY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
