"""CLI for the M1.81-M1.90 correctness-before-performance gate."""

from __future__ import annotations

import argparse
import json

from .common import render, run_all


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    payload = render(run_all())
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(f"CAMPAIGN={payload['campaign']}")
        print(f"CORRECTNESS_STATUS={payload['status']}")
        print(f"PASS={payload['passed']}")
        print(f"FAIL={payload['failed']}")
        print(f"DEFERRED={payload['deferred']}")
        for item in payload["checks"]:
            print(f"CHECK_{item['name'].upper()}={item['status']}")
    return 1 if payload["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

