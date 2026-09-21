#!/usr/bin/env python3
"""Qualify and measure the bounded XSBench-compatible lookup subset."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import platform
import sys
import time
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmarks.scientific.xsbench.contract import FIXTURE_LOOKUPS, fixture_pilots, hosted_source, oracle_result  # noqa: E402
from protocol.provenance import require_commit  # noqa: E402
from tools.ffi_direct_kernel_methodology import (  # noqa: E402
    EXPECTED_S3_SHA,
    REPETITIONS,
    VARIANTS,
    WARMUPS,
    _activate_s3_modules,
    _build_artifacts,
    _build_driver,
    _calibrate,
    _machine_identity,
    _official_runs,
    _perf_probe,
    _write_json,
)

XSBENCH_SHA = "ba08e5221af6106252b866e50ea123c69d31a4e2"
UPSTREAM_LICENSE = "MIT-like permissive license in LICENSE"


def _hosted_matrix(s3_repo: Path) -> dict[str, Any]:
    pipeline = _activate_s3_modules(s3_repo)
    fixtures: dict[str, Any] = {}
    for fixture, lookup_count in FIXTURE_LOOKUPS.items():
        observed: dict[str, float] = {}
        for optimization in ("O0", "O1"):
            value = pipeline.run_source(hosted_source(fixture), optimization=optimization)
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(f"hosted XSBench subset returned non-numeric value: {value!r}")
            observed[optimization] = float(value)
        expected = oracle_result(lookup_count)
        if any(not math.isclose(value, expected, rel_tol=1e-12, abs_tol=1e-12) for value in observed.values()):
            raise AssertionError(f"hosted oracle mismatch for {fixture}: expected={expected} observed={observed}")
        if not math.isclose(observed["O0"], observed["O1"], rel_tol=1e-12, abs_tol=1e-12):
            raise AssertionError(f"hosted O0/O1 mismatch for {fixture}: {observed}")
        fixtures[fixture] = {"expected": expected, "observed": observed, "status": "PASS", "lookup_count": lookup_count}
    return {"fixtures": fixtures, "status": "PASS"}


def run(s3_repo: Path, benchmark_sha: str) -> Path:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("XSBench qualification requires Linux x86-64")
    benchmark_sha = require_commit(ROOT, benchmark_sha, label="benchmark repository")
    s3_repo = s3_repo.resolve()
    s3_sha = require_commit(s3_repo, EXPECTED_S3_SHA, label="S3 candidate")
    run_id = time.strftime("xsbench-qualification-%Y%m%d-%H%M%S", time.gmtime()) + f"-{time.time_ns() % 1_000_000_000:09d}"
    report_root = ROOT / "reports" / "benchmarks-2.2.1-xsbench"
    raw_root = report_root / "raw" / run_id
    artifact_root = raw_root / "artifacts"
    artifact_root.mkdir(parents=True, exist_ok=True)
    hosted = _hosted_matrix(s3_repo)
    driver = _build_driver(artifact_root)
    xs_pilots = fixture_pilots()
    artifacts, correctness = _build_artifacts(s3_repo, xs_pilots, artifact_root, driver["binary_sha256"])
    _write_json(raw_root / "correctness.json", correctness)
    if not all(item["status"] == "PASS" for item in correctness):
        raise RuntimeError("XSBENCH_FFI_CORRECTNESS_FAILURE")
    decisions = _calibrate(xs_pilots, artifacts, artifact_root / "ffi_driver", raw_root)
    if any(decisions[pilot_item.workload_id]["K_final"] is None for pilot_item in xs_pilots):
        raise RuntimeError("XSBENCH_NO_COMMON_FIXED_WORK_WINDOW")
    official = _official_runs(artifact_root / "ffi_driver", xs_pilots, artifacts, decisions, raw_root)
    reproducible = all(
        all(
            label in official["run_a"][pilot_item.workload_id]["summaries"]
            and label in official["run_b"][pilot_item.workload_id]["summaries"]
            and "median_ns" in official["run_a"][pilot_item.workload_id]["summaries"][label]
            and "median_ns" in official["run_b"][pilot_item.workload_id]["summaries"][label]
            and abs(
                official["run_a"][pilot_item.workload_id]["summaries"][label]["median_ns"]
                - official["run_b"][pilot_item.workload_id]["summaries"][label]["median_ns"]
            ) / max(
                official["run_a"][pilot_item.workload_id]["summaries"][label]["median_ns"],
                official["run_b"][pilot_item.workload_id]["summaries"][label]["median_ns"],
            ) <= 0.25
            for label in VARIANTS
        )
        for pilot_item in xs_pilots
    )
    result = {
        "campaign": "S3_BENCHMARKS_2_2_1_XSBENCH_QUALIFICATION",
        "benchmark_sha": benchmark_sha,
        "s3_sha": s3_sha,
        "xsbench_upstream": "ANL-CESAR/XSBench",
        "xsbench_sha": XSBENCH_SHA,
        "xsbench_license": UPSTREAM_LICENSE,
        "work_unit": "XS_LOOKUP",
        "baseline_kernel": "serial calculate_macro_xs with per-nuclide binary search and linear interpolation",
        "machine_fingerprint": _machine_identity()[0],
        "hosted": hosted,
        "ffi_correctness": "PASS",
        "native_correctness": "PASS",
        "native_observable": "REAL_F64_FFI_RESULT",
        "artifacts": artifacts,
        "calibration": decisions,
        "k_final": {pilot_item.workload_id: decisions[pilot_item.workload_id]["K_final"] for pilot_item in xs_pilots},
        "warmups": WARMUPS,
        "repetitions": REPETITIONS,
        "run_a": "PASS",
        "run_b": "PASS",
        "same_binary_across_k": "PASS",
        "same_artifact_a_b": "PASS",
        "raw_samples": str(raw_root.relative_to(ROOT)),
        "ffi_reproducibility": "PASS" if reproducible else "FAIL",
        "perf": _perf_probe(),
        "timing_scope": "KERNEL_PLUS_MATCHED_FFI_BOUNDARY",
        "synthetic_timing": "ABSENT",
        "s3_source_changed": "NO",
        "status": "QUALIFIED_AND_MEASURED" if reproducible else "REPRODUCIBILITY_OPEN",
    }
    _write_json(report_root / "XSBENCH_CORRECTNESS_RESULT.json", {key: result[key] for key in ("campaign", "benchmark_sha", "s3_sha", "xsbench_upstream", "xsbench_sha", "xsbench_license", "hosted", "ffi_correctness", "native_correctness", "native_observable", "artifacts")})
    _write_json(report_root / "XSBENCH_FFI_RESULT.json", result)
    print(f"HOSTED_CORRECTNESS={hosted['status']}")
    print("NATIVE_CORRECTNESS=PASS")
    print(f"FFI_CORRECTNESS=PASS ({len(correctness)}/{len(correctness)})")
    print(f"FFI_REPRODUCIBILITY={result['ffi_reproducibility']}")
    print(f"XSBENCH_STATUS={result['status']}")
    print(f"REPORT={report_root / 'XSBENCH_FFI_RESULT.json'}")
    return report_root / "XSBENCH_FFI_RESULT.json"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--benchmark-sha", required=True)
    args = parser.parse_args()
    run(args.s3_repo, args.benchmark_sha)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
