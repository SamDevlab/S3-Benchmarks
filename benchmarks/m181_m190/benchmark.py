"""Smoke-only characterization runner for correctness-certified campaigns."""

from __future__ import annotations

import argparse
import json
import platform
import sys
import time

from .common import EXECUTABLE_CHECKS, render, run_all, run_check


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", required=True, help="Only the bounded smoke protocol is supported")
    parser.add_argument("--repetitions", type=int, default=3)
    args = parser.parse_args()
    if args.repetitions <= 0 or args.repetitions > 10:
        raise SystemExit("repetitions must be in 1..10 for smoke mode")

    correctness = render(run_all())
    if correctness["failed"]:
        print(json.dumps({"status": "BLOCKED_CORRECTNESS", "correctness": correctness}, indent=2, sort_keys=True))
        return 1
    rows = []
    for name in EXECUTABLE_CHECKS:
        for _warmup in range(1):
            run_check(name)
        samples = []
        for _index in range(args.repetitions):
            started = time.perf_counter_ns()
            check = run_check(name)
            elapsed = time.perf_counter_ns() - started
            if check.status != "PASS":
                print(json.dumps({"status": "BLOCKED_CORRECTNESS", "check": check.as_json()}, indent=2, sort_keys=True))
                return 1
            samples.append(elapsed)
        rows.append({
            "name": name,
            "status": "CHARACTERIZATION_ONLY",
            "iterations": args.repetitions,
            "warmups": 1,
            "median_ns": sorted(samples)[len(samples) // 2],
            "min_ns": min(samples),
            "max_ns": max(samples),
            "fixture_hash": "deterministic-contract-v1",
        })
    payload = {
        "schema": "s3.m181-m190.smoke.v1",
        "status": "PASS_CHARACTERIZATION_ONLY",
        "correctness_gate": correctness["status"],
        "s3_commit": __import__("os").environ.get("S3_COMMIT", "UNSPECIFIED"),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "reference_toolchain": "UNAVAILABLE; no comparative timing claimed",
        "results": rows,
        "deferred_checks": [item["name"] for item in correctness["checks"] if item["status"] == "DEFERRED"],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
