#!/usr/bin/env python3
"""Run the S3 package resolver/cache/reproducibility correctness preflight."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
EXPECTED_S3_SHA = "cd6804f72757d6936ca1ec6c20d5badf55d1aac4"
EXPECTED_CARGO_SHA = "514c56dd7321eecbfdcf9b6479519cf4edfab906"
EXPECTED_UV_SHA = "5c170b8022c5565a1d4ada3406077d8fdf7f9088"
S3_REPO_DIR = Path(
    os.environ.get(
        "S3_CURRENT_REPO",
        os.environ.get("S3_REPO", BASE_DIR.parent / "S3"),
    )
).resolve()

sys.path.insert(0, str(BASE_DIR))
if S3_REPO_DIR.exists() and str(S3_REPO_DIR) not in sys.path:
    sys.path.insert(0, str(S3_REPO_DIR))

from benchmarks.package_repro.harness.correctness import verify_behavioral_contract


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
        description="Verify S3 M1.56/M1.79/M1.80 package reproducibility contracts"
    )
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument(
        "--output-json",
        type=Path,
        default=BASE_DIR / "reports" / "package-repro-correctness.json",
    )
    args = parser.parse_args()

    if not args.verify_only:
        parser.error(
            "only --verify-only is supported; resolver/cache timing remains deferred until "
            "an equivalent native workload exists"
        )

    if not S3_REPO_DIR.exists():
        print(f"S3_CURRENT_REPO does not exist: {S3_REPO_DIR}", file=sys.stderr)
        return 2

    actual_s3_sha = _git_head(S3_REPO_DIR)
    if actual_s3_sha != EXPECTED_S3_SHA:
        print("PACKAGE_REPRO_S3_BASELINE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_S3_SHA: {EXPECTED_S3_SHA}", file=sys.stderr)
        print(f"ACTUAL_S3_SHA: {actual_s3_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2

    actual_cargo_sha = _reference_sha("rust-lang/cargo")
    actual_uv_sha = _reference_sha("astral-sh/uv")
    if actual_cargo_sha != EXPECTED_CARGO_SHA:
        print("PACKAGE_REPRO_CARGO_REFERENCE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_CARGO_SHA: {EXPECTED_CARGO_SHA}", file=sys.stderr)
        print(f"ACTUAL_CARGO_SHA: {actual_cargo_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2
    if actual_uv_sha != EXPECTED_UV_SHA:
        print("PACKAGE_REPRO_UV_REFERENCE_PIN: FAIL", file=sys.stderr)
        print(f"EXPECTED_UV_SHA: {EXPECTED_UV_SHA}", file=sys.stderr)
        print(f"ACTUAL_UV_SHA: {actual_uv_sha or 'UNKNOWN'}", file=sys.stderr)
        return 2

    passed, report = verify_behavioral_contract()
    report.update(
        {
            "s3_repository": str(S3_REPO_DIR),
            "expected_s3_sha": EXPECTED_S3_SHA,
            "actual_s3_sha": actual_s3_sha,
            "baseline_pin_match": True,
            "cargo_repository": "rust-lang/cargo",
            "expected_cargo_sha": EXPECTED_CARGO_SHA,
            "actual_cargo_sha": actual_cargo_sha,
            "cargo_reference_pin_match": True,
            "uv_repository": "astral-sh/uv",
            "expected_uv_sha": EXPECTED_UV_SHA,
            "actual_uv_sha": actual_uv_sha,
            "uv_reference_pin_match": True,
            "runner": "tools/package_repro_runner.py",
        }
    )

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if passed:
        print("PACKAGE_REPRO_S3_BASELINE_PIN: PASS")
        print("PACKAGE_REPRO_CARGO_REFERENCE_PIN: PASS")
        print("PACKAGE_REPRO_UV_REFERENCE_PIN: PASS")
        print("PACKAGE_REPRO_BEHAVIORAL_CORRECTNESS: PASS")
        print("PERFORMANCE_STATUS: DEFERRED_UNTIL_EQUIVALENT_NATIVE_RESOLVER_WORKLOAD_EXISTS")
        print(f"S3_SHA: {actual_s3_sha}")
        print(f"CARGO_SHA: {actual_cargo_sha}")
        print(f"UV_SHA: {actual_uv_sha}")
        print(f"REPORT: {args.output_json}")
        return 0

    print("PACKAGE_REPRO_BEHAVIORAL_CORRECTNESS: FAIL", file=sys.stderr)
    print(json.dumps(report, indent=2, sort_keys=True), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
