#!/usr/bin/env python3
"""Run the bounded Phase B scientific correctness matrix."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmarks.candidate_activation.adapters import native_case, run_hosted  # noqa: E402
from benchmarks.scientific.rmsd.expansion import expansion_cases  # noqa: E402
from protocol.provenance import require_commit  # noqa: E402


EXPECTED_S3_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"
UPSTREAM_REFERENCE = "charnley.rmsd"
UPSTREAM_SHA = "1ad8ecee48d95ab43b49bd9f2fe4f8f07d9106bd"


def _run_cases(s3_repo: Path, cases: tuple[Any, ...]) -> list[dict[str, Any]]:
    os.environ["S3_REPO"] = str(s3_repo)
    os.environ["S3_COMMIT"] = EXPECTED_S3_SHA
    from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend

    toolchain = NativeToolchain.detect()
    observations: list[dict[str, Any]] = []
    for case in cases:
        hosted: dict[str, Any] = {}
        try:
            for optimization in ("O0", "O1"):
                hosted[optimization] = run_hosted(case, optimization=optimization)
            hosted_pass = all(
                math.isclose(float(value), case.expected, rel_tol=1e-12, abs_tol=1e-12)
                for value in hosted.values()
            ) and math.isclose(float(hosted["O0"]), float(hosted["O1"]), rel_tol=1e-12, abs_tol=1e-12)
            if not hosted_pass:
                raise AssertionError(f"hosted mismatch: expected={case.expected} observed={hosted}")
            native_observed, native_observable = native_case(case, toolchain, X8664Backend)
            native_status = "PASS" if native_observed == 1 else "FAIL"
            status = "PASS" if native_status == "PASS" else "FAIL"
            error = None if status == "PASS" else f"native canary={native_observed}"
        except Exception as exc:
            native_observed = None
            native_observable = None
            native_status = "BLOCKED"
            status = "FAIL"
            error = f"{type(exc).__name__}: {exc}"
        observations.append(
            {
                "workload_id": case.workload_id,
                "size": case.size,
                "status": status,
                "expected": case.expected,
                "hosted": hosted,
                "native_canary": native_observed,
                "native_status": native_status,
                "native_observable": native_observable,
                "source_sha256": hashlib.sha256(case.source.encode("utf-8")).hexdigest(),
                "source_bytes": len(case.source.encode("utf-8")),
                "logical_shape": case.logical_shape,
                "physical_layout": case.physical_layout,
                "index_mapping": case.index_mapping,
                "error": error,
            }
        )
    return observations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--s3-sha", default=EXPECTED_S3_SHA)
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    benchmark_sha = require_commit(ROOT, args.benchmark_sha, label="benchmark repository")
    s3_repo = args.s3_repo.resolve()
    s3_sha = require_commit(s3_repo, args.s3_sha, label="S3 candidate")
    cases = expansion_cases()
    observations = _run_cases(s3_repo, cases)
    payload = {
        "campaign": "S3_BENCHMARKS_2_2_SCIENTIFIC_MINIAPPS",
        "benchmark_sha": benchmark_sha,
        "s3_sha": s3_sha,
        "upstream_reference": UPSTREAM_REFERENCE,
        "upstream_sha": UPSTREAM_SHA,
        "platform": {"system": platform.system(), "machine": platform.machine()},
        "rmsd_expansion": "PASS" if all(item["status"] == "PASS" for item in observations) else "FAIL",
        "scientific_hosted_correctness": "PASS" if all(item["hosted"] for item in observations) else "FAIL",
        "scientific_native_correctness": "PASS" if all(item["native_status"] == "PASS" for item in observations) else "FAIL",
        "observations": observations,
        "timing": "NOT_RUN",
        "synthetic_timing": "ABSENT",
        "s3_source_changed": "NO",
        "phase_b_gate": "PASS" if all(item["status"] == "PASS" for item in observations) else "BLOCKED",
        "status": "COMPLETE" if all(item["status"] == "PASS" for item in observations) else "BLOCKED",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"RMSD_EXPANSION={payload['rmsd_expansion']}")
    print(f"SCIENTIFIC_NATIVE_CORRECTNESS={payload['scientific_native_correctness']}")
    print(f"PHASE_B_GATE={payload['phase_b_gate']}")
    print(f"REPORT={args.output}")
    return 0 if payload["status"] == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
