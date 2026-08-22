"""Run deterministic P2-P18 contract probes and persist no timing claims."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from benchmarks.rc1.workloads import run_all_contract_probes  # noqa: E402
from tools.artifacts import require_provenance  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--s3-sha", required=True)
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-markdown", type=Path, required=True)
    args = parser.parse_args()

    provenance = require_provenance(
        s3_repo=args.s3_repo,
        requested_s3_sha=args.s3_sha,
        benchmark_repo=BASE_DIR,
        requested_benchmark_sha=args.benchmark_sha,
    )
    rows = run_all_contract_probes()
    if any(row["contract_probe"] != "PASS" for row in rows):
        raise SystemExit("contract probe failed")
    payload = {
        "schema": "s3.rc1.workload-status.v1",
        "campaign": "rc1-longitudinal-native-20260822",
        "provenance": provenance,
        "contract_probe": "PASS",
        "timing_claim": "NONE",
        "workloads": rows,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "# RC1 P2-P18 workload status",
        "",
        "Contract probes validate pinned input/output declarations only. No row is a performance result.",
        "",
        "| Workload | Class | Contract | Canonical status | Timing |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| {row['workload']} | {row['comparison_class']} | {row['contract_probe']} | {row['canonical_status']} | {row['performance_status']} |")
    args.output_markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WORKLOAD_CONTRACTS={len(rows)}")
    print("WORKLOAD_CONTRACT_PROBE=PASS")
    print("TIMING_CLAIM=NONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

