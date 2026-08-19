#!/usr/bin/env python3
"""Run the S3 async-runtime correctness preflight.

Performance timing is deliberately disabled until an equivalent native S3
workload and a suitable external reference implementation are both available.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
S3_REPO_DIR = Path(
    os.environ.get(
        "S3_CURRENT_REPO",
        os.environ.get("S3_REPO", BASE_DIR.parent / "S3"),
    )
).resolve()

sys.path.insert(0, str(BASE_DIR))
if S3_REPO_DIR.exists() and str(S3_REPO_DIR) not in sys.path:
    sys.path.insert(0, str(S3_REPO_DIR))

from benchmarks.async_runtime.harness.correctness import verify_behavioral_contract


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify S3 M1.71-M1.76 async-runtime behavioral contracts"
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Run correctness verification. Performance timing is intentionally unavailable.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=BASE_DIR / "reports" / "async-runtime-correctness.json",
    )
    args = parser.parse_args()

    if not args.verify_only:
        parser.error(
            "only --verify-only is supported; performance timing remains deferred until "
            "an equivalent native workload exists"
        )

    passed, report = verify_behavioral_contract()
    report["s3_repository"] = str(S3_REPO_DIR)
    report["runner"] = "tools/async_runtime_runner.py"

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if passed:
        print("ASYNC_RUNTIME_BEHAVIORAL_CORRECTNESS: PASS")
        print("PERFORMANCE_STATUS: DEFERRED_UNTIL_EQUIVALENT_NATIVE_WORKLOAD_EXISTS")
        print(f"REPORT: {args.output_json}")
        return 0

    print("ASYNC_RUNTIME_BEHAVIORAL_CORRECTNESS: FAIL", file=sys.stderr)
    print(json.dumps(report, indent=2, sort_keys=True), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
