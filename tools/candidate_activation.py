#!/usr/bin/env python3
"""Run the bounded 2.0.1 candidate activation matrix.

This tool performs correctness only.  It never records timing and never
changes the S3 checkout.  Native execution is deliberately a separate mode.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmarks.candidate_activation.adapters import native_case, run_hosted_matrix
from benchmarks.candidate_activation.workloads import cases


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--native", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    workload_cases = cases()
    if args.native:
        if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
            raise SystemExit("NATIVE_BLOCKED=ENVIRONMENT_GAP: Linux x86-64 is required")
        from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
        toolchain = NativeToolchain.detect()
        observations = []
        for case in workload_cases:
            try:
                observed, observable = native_case(case, toolchain, X8664Backend)
                expected_canary = 1
                status = "NATIVE_PASS" if observed == expected_canary else "NATIVE_FAIL"
                error = None if status == "NATIVE_PASS" else f"expected canary {expected_canary}, observed {observed}"
                observations.append({"workload_id": case.workload_id, "size": case.size, "status": status, "expected": case.expected, "expected_canary": expected_canary, "observed": observed, "native_observable": observable, "error": error})
            except Exception as exc:
                observations.append({"workload_id": case.workload_id, "size": case.size, "status": "NATIVE_BLOCKED", "expected": case.expected, "expected_canary": 1, "observed": None, "native_observable": None, "error": f"{type(exc).__name__}: {exc}"})
    else:
        observations = [item.to_dict() for item in run_hosted_matrix(workload_cases)]
    output = args.output or ROOT / "reports/benchmarks-2.0.1-candidate-activation/activation-results.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    generated_dir = output.parent / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)
    generated_sources = []
    for case in workload_cases:
        filename = f"{case.workload_id.replace('.', '_')}__{case.size}.s3"
        source_path = generated_dir / filename
        source_bytes = case.source.encode("utf-8")
        source_path.write_bytes(source_bytes)
        generated_sources.append(
            {
                "workload_id": case.workload_id,
                "size": case.size,
                "path": source_path.relative_to(ROOT).as_posix()
                if source_path.is_relative_to(ROOT)
                else str(source_path),
                "sha256": hashlib.sha256(source_bytes).hexdigest(),
                "bytes": len(source_bytes),
            }
        )
    payload = {
        "s3_candidate_sha": "e07d0b5464bf472b2ca18993f3e196a234ff0fc5",
        "performance_results_valid": "NO_NEW_PERFORMANCE_RESULTS",
        "generated_sources": generated_sources,
        "observations": observations,
    }
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OBSERVATIONS={len(observations)}")
    print(f"REPORT={output}")
    return 0 if all(item["status"] in {"CORRECTNESS_PASS", "NATIVE_PASS"} for item in observations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
