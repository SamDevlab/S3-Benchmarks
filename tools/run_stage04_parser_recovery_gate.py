"""Normalize Stage04 parser-attempt reports and analyze recovery progression."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tools.analyze_stage04_parser_recovery import analyze
from tools.normalize_stage04_parser_attempt import normalize


def run(report_paths: list[Path], output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    attempts: list[dict] = []
    normalization_failures: list[dict] = []

    for index, path in enumerate(report_paths):
        normalized = normalize(path.read_text(encoding="utf-8"))
        normalized_path = output / f"attempt-{index:03d}.json"
        normalized_path.write_text(
            json.dumps(normalized, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        if normalized["normalization_status"] != "PASS":
            normalization_failures.append(
                {
                    "index": index,
                    "path": str(path),
                    "errors": normalized["normalization_errors"],
                    "duplicates": normalized["duplicate_keys"],
                }
            )
        attempts.append(normalized)

    if normalization_failures:
        result = {
            "schema": "s3-benchmarks.bootstrap.stage04-parser-recovery-gate.v1",
            "status": "BLOCKED_NORMALIZATION",
            "attempt_count": len(attempts),
            "normalization_failures": normalization_failures,
            "recovery": None,
            "promotion_effect": "NONE_DIAGNOSTIC_TRACKING_ONLY",
        }
    else:
        recovery = analyze(attempts)
        result = {
            "schema": "s3-benchmarks.bootstrap.stage04-parser-recovery-gate.v1",
            "status": recovery["status"],
            "attempt_count": recovery["attempt_count"],
            "normalization_failures": [],
            "recovery": recovery,
            "promotion_effect": "NONE_DIAGNOSTIC_TRACKING_ONLY",
        }

    (output / "parser-recovery.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="append", type=Path, default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = run(args.report, args.output)
    except OSError as error:
        parser.exit(2, f"STAGE04_PARSER_RECOVERY_GATE_ERROR={error}\n")
    print(f"PARSER_RECOVERY_GATE={result['status']}")
    return 0 if result["status"] not in {"BLOCKED_NORMALIZATION", "INVALID_EVIDENCE", "STALLED_REPAIR"} else 3


if __name__ == "__main__":
    raise SystemExit(main())
