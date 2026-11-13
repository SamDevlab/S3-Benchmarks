"""Reproducible S3 V4.8 CPU & GPU benchmark suite reusing V4.4 Validation Engine & kernels."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
S3_ROOT = BENCH_ROOT.parent / "S3"
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from run_v4_4_suite import run_cpu_suite, run_gpu_suite


def _git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("cpu", "gpu"), required=True)
    args = parser.parse_args()

    out_json = THIS_DIR / "results_v4_8.json"
    out_csv = THIS_DIR / "results_v4_8.csv"
    data = json.loads(out_json.read_text(encoding="utf-8")) if out_json.exists() else {"cpu": [], "gpu": {}}
    s3_sha = _git_sha(S3_ROOT)
    bench_sha = _git_sha(BENCH_ROOT)
    data["metadata"] = {"campaign": "S3_V4_8", "compiler_sha": s3_sha, "source_sha": bench_sha}

    if args.mode == "cpu":
        recs = run_cpu_suite()
        for r in recs:
            r["COMPILER_SHA"] = s3_sha
            r["SOURCE_SHA"] = bench_sha
        data["cpu"] = recs
    else:
        gpu_res = run_gpu_suite()
        for r in gpu_res.get("records", []):
            r["COMPILER_SHA"] = s3_sha
            r["SOURCE_SHA"] = bench_sha
        data["gpu"] = gpu_res

    out_json.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    all_recs = list(data.get("cpu", [])) + list(data.get("gpu", {}).get("records", []))
    fields = [
        "BENCHMARK_ID", "COMPILER_SHA", "SOURCE_SHA", "KERNEL", "REFERENCE", "INPUT_SIZE", "PRECISION",
        "ATOL", "RTOL", "MAX_ABS_ERROR", "MAX_REL_ERROR", "RMS_ERROR", "MISMATCH_COUNT",
        "FIRST_MISMATCH_INDEX", "NUMERICAL_VALIDITY", "DATA_INTEGRITY", "PERFORMANCE_VALIDITY",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in all_recs:
            w.writerow({k: r.get(k) for k in fields})

    print(json.dumps({
        "total_records": len(all_recs),
        "valid": sum(1 for r in all_recs if r["NUMERICAL_VALIDITY"] == "VALID"),
        "invalid": sum(1 for r in all_recs if r["NUMERICAL_VALIDITY"] == "INVALID"),
        "compiler_sha": s3_sha,
        "source_sha": bench_sha,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
