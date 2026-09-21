#!/usr/bin/env python3
"""Validate and materialize the S3 Evidence Lab 2.0 registry.

This command is intentionally separate from ``tools/runner.py``.  It does not
compile S3 or run a benchmark; it validates the external evidence contracts
and produces deterministic coverage/blocker views.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from protocol.registry import load_registry, registry_digest


def _coverage(registry: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    missing: dict[str, list[str]] = {}
    for workload in registry["workloads"]:
        status = workload["status"]
        supported = status != "NOT_SUPPORTED_YET"
        row = {
            "workload_id": workload["id"],
            "family": workload["family"],
            "status": status,
            "implemented": status not in {"CANDIDATE", "UPSTREAM_PINNED", "NOT_SUPPORTED_YET"},
            "correctness_pass": status in {"CORRECTNESS_PASS", "NATIVE_PASS", "MEASURED", "REPRODUCED", "EXTERNALIZED"},
            "native_pass": status in {"NATIVE_PASS", "MEASURED", "REPRODUCED", "EXTERNALIZED"},
            "measured": status in {"MEASURED", "REPRODUCED", "EXTERNALIZED"},
            "not_supported": not supported,
        }
        rows.append(row)
        contract = workload["correctness_contract"]
        capability = contract.get("first_missing_capability")
        if not supported and capability:
            missing.setdefault(capability, []).append(workload["id"])
    blocker_rows = [
        {"capability": capability, "workload_count": len(workloads), "workloads": sorted(workloads)}
        for capability, workloads in sorted(missing.items())
    ]
    return rows, blocker_rows


def write_reports(root: Path, registry: dict[str, Any]) -> tuple[Path, Path]:
    rows, blockers = _coverage(registry)
    report_root = root / "reports" / "benchmarks-2.0-foundation"
    report_root.mkdir(parents=True, exist_ok=True)
    coverage = {
        "schema": "s3.capability-coverage.v1",
        "registry_digest": registry_digest(registry),
        "rows": rows,
        "summary": {
            "workloads": len(rows),
            "correctness_pass": sum(row["correctness_pass"] for row in rows),
            "native_pass": sum(row["native_pass"] for row in rows),
            "measured": sum(row["measured"] for row in rows),
            "not_supported": sum(row["not_supported"] for row in rows),
        },
    }
    coverage_json = report_root / "capability-coverage.json"
    coverage_json.write_text(json.dumps(coverage, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    coverage_md = report_root / "capability-coverage.md"
    lines = [
        "# S3 Evidence Lab 2.0 Capability Coverage",
        "",
        f"Registry digest: `{coverage['registry_digest']}`",
        "",
        "| Workload | Family | Status | Correctness | Native | Measured |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['workload_id']}` | {row['family']} | {row['status']} | "
            f"{row['correctness_pass']} | {row['native_pass']} | {row['measured']} |"
        )
    lines.extend(["", "## Missing capabilities", "", "| Capability | Workload count | Workloads |", "|---|---:|---|"])
    for blocker in blockers:
        lines.append(f"| `{blocker['capability']}` | {blocker['workload_count']} | {', '.join(f'`{item}`' for item in blocker['workloads'])} |")
    coverage_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return coverage_json, coverage_md


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the S3 Evidence Lab registry")
    parser.add_argument("--check", action="store_true", help="validate and write deterministic coverage reports")
    args = parser.parse_args()
    registry = load_registry(ROOT)
    digest = registry_digest(registry)
    print(f"REGISTRY_DIGEST={digest}")
    print(f"WORKLOADS={len(registry['workloads'])}")
    if args.check:
        json_path, markdown_path = write_reports(ROOT, registry)
        print(f"CAPABILITY_COVERAGE_JSON={json_path}")
        print(f"CAPABILITY_COVERAGE_MD={markdown_path}")
    print("REGISTRY_VALIDATION=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
