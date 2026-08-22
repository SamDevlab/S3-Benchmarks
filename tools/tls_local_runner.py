#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EXPECTED_S3_SHA = "cd6804f72757d6936ca1ec6c20d5badf55d1aac4"
S3_REPO_DIR = Path(os.environ.get("S3_CURRENT_REPO", os.environ.get("S3_REPO", BASE_DIR.parent / "S3"))).resolve()

sys.path.insert(0, str(BASE_DIR))
if S3_REPO_DIR.exists() and str(S3_REPO_DIR) not in sys.path:
    sys.path.insert(0, str(S3_REPO_DIR))

from benchmarks.tls_local.harness.correctness import verify_behavioral_contract


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


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify S3 M1.75 local TLS state-machine contracts")
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--output-json", type=Path, default=BASE_DIR / "reports" / "tls-local-correctness.json")
    args = parser.parse_args()

    if not args.verify_only:
        parser.error("only --verify-only is supported")
    if not S3_REPO_DIR.exists():
        print(f"S3_CURRENT_REPO does not exist: {S3_REPO_DIR}", file=sys.stderr)
        return 2

    actual_s3_sha = _git_head(S3_REPO_DIR)
    if actual_s3_sha != EXPECTED_S3_SHA:
        print("TLS_LOCAL_BASELINE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_S3_SHA: {EXPECTED_S3_SHA}", file=sys.stderr)
        print(f"ACTUAL_S3_SHA: {actual_s3_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2

    passed, report = verify_behavioral_contract()
    report["expected_s3_sha"] = EXPECTED_S3_SHA
    report["actual_s3_sha"] = actual_s3_sha
    report["baseline_pin_match"] = True
    report["runner"] = "tools/tls_local_runner.py"
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if passed:
        print("TLS_LOCAL_BASELINE_PIN: PASS")
        print("TLS_LOCAL_CORRECTNESS: PASS")
        print("PERFORMANCE_STATUS: DEFERRED_UNTIL_VETTED_NATIVE_TLS_PROVIDER_IS_BENCHMARKABLE")
        print(f"REPORT: {args.output_json}")
        return 0

    print("TLS_LOCAL_CORRECTNESS: FAIL", file=sys.stderr)
    print(json.dumps(report, indent=2, sort_keys=True), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
