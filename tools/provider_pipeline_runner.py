#!/usr/bin/env python3
"""Run the MoneyPrinterTurbo-inspired S3 provider pipeline preflight."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
EXPECTED_S3_SHA = "cd6804f72757d6936ca1ec6c20d5badf55d1aac4"
EXPECTED_MONEYPRINTER_SHA = "d4c0e45da4ac0889af77f7307f52f9d5d4f74942"
S3_REPO_DIR = Path(
    os.environ.get(
        "S3_CURRENT_REPO",
        os.environ.get("S3_REPO", BASE_DIR.parent / "S3"),
    )
).resolve()

sys.path.insert(0, str(BASE_DIR))
if S3_REPO_DIR.exists() and str(S3_REPO_DIR) not in sys.path:
    sys.path.insert(0, str(S3_REPO_DIR))

from benchmarks.provider_pipeline.harness.correctness import verify_behavioral_contract


def _git_head(repository: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(repository), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    return value if len(value) == 40 else None


def _reference_sha(repository: str) -> str | None:
    path = BASE_DIR / "references" / "upstreams-m171-m180.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    for item in payload.get("references", []):
        if item.get("repository") == repository:
            value = item.get("commit")
            return value if isinstance(value, str) else None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify the S3 MoneyPrinterTurbo-inspired local provider pipeline"
    )
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument(
        "--output-json",
        type=Path,
        default=BASE_DIR / "reports" / "provider-pipeline-correctness.json",
    )
    args = parser.parse_args()

    if not args.verify_only:
        parser.error(
            "only --verify-only is supported; application performance remains deferred until "
            "an equivalent native S3 workload exists"
        )

    if not S3_REPO_DIR.exists():
        print(f"S3_CURRENT_REPO does not exist: {S3_REPO_DIR}", file=sys.stderr)
        return 2

    actual_s3_sha = _git_head(S3_REPO_DIR)
    if actual_s3_sha != EXPECTED_S3_SHA:
        print("PROVIDER_PIPELINE_S3_BASELINE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_S3_SHA: {EXPECTED_S3_SHA}", file=sys.stderr)
        print(f"ACTUAL_S3_SHA: {actual_s3_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2

    actual_reference_sha = _reference_sha("harry0703/MoneyPrinterTurbo")
    if actual_reference_sha != EXPECTED_MONEYPRINTER_SHA:
        print("PROVIDER_PIPELINE_REFERENCE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_MONEYPRINTER_SHA: {EXPECTED_MONEYPRINTER_SHA}", file=sys.stderr)
        print(f"ACTUAL_MONEYPRINTER_SHA: {actual_reference_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2

    passed, report = verify_behavioral_contract()
    report.update(
        {
            "s3_repository": str(S3_REPO_DIR),
            "expected_s3_sha": EXPECTED_S3_SHA,
            "actual_s3_sha": actual_s3_sha,
            "s3_baseline_pin_match": True,
            "reference_repository": "harry0703/MoneyPrinterTurbo",
            "expected_reference_sha": EXPECTED_MONEYPRINTER_SHA,
            "actual_reference_sha": actual_reference_sha,
            "reference_pin_match": True,
            "reference_execution": "NOT_RUN_METADATA_AND_ARCHITECTURE_REFERENCE_ONLY",
            "runner": "tools/provider_pipeline_runner.py",
        }
    )

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if passed:
        print("PROVIDER_PIPELINE_S3_BASELINE_PIN: PASS")
        print("PROVIDER_PIPELINE_REFERENCE_PIN: PASS")
        print("PROVIDER_PIPELINE_BEHAVIORAL_CORRECTNESS: PASS")
        print("PUBLIC_INTERNET_REQUIRED: NO")
        print("EXTERNAL_PROVIDER_CALLS: NO")
        print("SECRETS_REQUIRED: NO")
        print("PERFORMANCE_STATUS: DEFERRED_UNTIL_EQUIVALENT_NATIVE_S3_APPLICATION_WORKLOAD_EXISTS")
        print(f"S3_SHA: {actual_s3_sha}")
        print(f"MONEYPRINTER_SHA: {actual_reference_sha}")
        print(f"REPORT: {args.output_json}")
        return 0

    print("PROVIDER_PIPELINE_BEHAVIORAL_CORRECTNESS: FAIL", file=sys.stderr)
    print(json.dumps(report, indent=2, sort_keys=True), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
