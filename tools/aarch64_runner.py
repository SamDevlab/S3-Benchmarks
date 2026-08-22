#!/usr/bin/env python3
"""Run the S3 M1.77/M1.78 ARM64 structural preflight.

This runner verifies the exact S3 baseline and the pinned LLVM reference
metadata before executing the S3 structural contract.  It does not invoke LLVM
and it does not publish comparative performance/code-quality results.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
EXPECTED_S3_SHA = "cd6804f72757d6936ca1ec6c20d5badf55d1aac4"
EXPECTED_LLVM_SHA = "b562ef546e46face7172d174e1a5f5454c470eee"
S3_REPO_DIR = Path(
    os.environ.get(
        "S3_CURRENT_REPO",
        os.environ.get("S3_REPO", BASE_DIR.parent / "S3"),
    )
).resolve()

sys.path.insert(0, str(BASE_DIR))
if S3_REPO_DIR.exists() and str(S3_REPO_DIR) not in sys.path:
    sys.path.insert(0, str(S3_REPO_DIR))

from benchmarks.aarch64.harness.structural import verify_structural_contract


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


def _llvm_reference_sha() -> str | None:
    path = BASE_DIR / "references" / "upstreams-m171-m180.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    for item in payload.get("references", []):
        if item.get("repository") == "llvm/llvm-project":
            value = item.get("commit")
            return value if isinstance(value, str) else None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify S3 M1.77/M1.78 AArch64 structural contracts"
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Run structural verification only. Runtime/code-quality comparison is unavailable.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=BASE_DIR / "reports" / "aarch64-structural.json",
    )
    args = parser.parse_args()

    if not args.verify_only:
        parser.error(
            "only --verify-only is supported; native execution and comparative code-quality "
            "remain deferred"
        )

    if not S3_REPO_DIR.exists():
        print(f"S3_CURRENT_REPO does not exist: {S3_REPO_DIR}", file=sys.stderr)
        return 2

    actual_s3_sha = _git_head(S3_REPO_DIR)
    if actual_s3_sha != EXPECTED_S3_SHA:
        print("AARCH64_S3_BASELINE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_S3_SHA: {EXPECTED_S3_SHA}", file=sys.stderr)
        print(f"ACTUAL_S3_SHA: {actual_s3_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2

    actual_llvm_sha = _llvm_reference_sha()
    if actual_llvm_sha != EXPECTED_LLVM_SHA:
        print("AARCH64_LLVM_REFERENCE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_LLVM_SHA: {EXPECTED_LLVM_SHA}", file=sys.stderr)
        print(f"ACTUAL_LLVM_SHA: {actual_llvm_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2

    passed, report = verify_structural_contract()
    report.update(
        {
            "s3_repository": str(S3_REPO_DIR),
            "expected_s3_sha": EXPECTED_S3_SHA,
            "actual_s3_sha": actual_s3_sha,
            "s3_baseline_pin_match": True,
            "llvm_repository": "llvm/llvm-project",
            "expected_llvm_sha": EXPECTED_LLVM_SHA,
            "actual_llvm_sha": actual_llvm_sha,
            "llvm_reference_pin_match": True,
            "runner": "tools/aarch64_runner.py",
        }
    )

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if passed:
        print("AARCH64_S3_BASELINE_PIN: PASS")
        print("AARCH64_LLVM_REFERENCE_PIN: PASS")
        print("AARCH64_STRUCTURAL_CORRECTNESS: PASS")
        print("LLVM_ORACLE_EXECUTION: DEFERRED_PINNED_REFERENCE_ONLY")
        print("COMPARATIVE_CODE_QUALITY: INVALID_UNTIL_NATIVE_OBJECT_PIPELINE_EXISTS")
        print("EXECUTION_BENCHMARK: DEFERRED")
        print(f"S3_SHA: {actual_s3_sha}")
        print(f"LLVM_SHA: {actual_llvm_sha}")
        print(f"REPORT: {args.output_json}")
        return 0

    print("AARCH64_STRUCTURAL_CORRECTNESS: FAIL", file=sys.stderr)
    print(json.dumps(report, indent=2, sort_keys=True), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
