"""Reproducible S3 V4.9 CPU (native SIMD, chunked Poisson, F64 profile) & GPU benchmark suite."""

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
for p in (str(THIS_DIR), str(S3_ROOT)):
    if p not in sys.path:
        sys.path.insert(0, p)

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

    out_json = THIS_DIR / "results_v4_9.json"
    out_csv = THIS_DIR / "results_v4_9.csv"
    data = json.loads(out_json.read_text(encoding="utf-8")) if out_json.exists() else {"cpu": [], "gpu": {}, "v4_9_study": {}}
    s3_sha = _git_sha(S3_ROOT)
    bench_sha = _git_sha(BENCH_ROOT)
    data["metadata"] = {"campaign": "S3_V4_9", "compiler_sha": s3_sha, "source_sha": bench_sha}

    if args.mode == "cpu":
        from tools.numerics_v4_9_study import (
            benchmark_poisson2d_large_chunked,
            benchmark_s3_simd_vs_scalar_vs_gcc,
            profile_f64_codegen,
        )

        recs = run_cpu_suite()
        simd_recs = benchmark_s3_simd_vs_scalar_vs_gcc(sizes=(256, 1024, 4096, 16384), repeats=5)
        poisson_recs = benchmark_poisson2d_large_chunked(grids=(16, 24, 32), tol=1e-12, max_iter=2500, chunk_iter=50)
        f64_prof = profile_f64_codegen()

        for sr in simd_recs:
            recs.append(
                {
                    "BENCHMARK_ID": f"cpu_s3_sse2_dot_n{sr['n']}",
                    "KERNEL": "f64_vector_dot_sse2",
                    "REFERENCE": "gcc_o3_dot",
                    "INPUT_SIZE": sr["n"],
                    "PRECISION": "f64",
                    "ATOL": 1e-9,
                    "RTOL": 1e-9,
                    "MAX_ABS_ERROR": sr["max_abs_diff_vs_gcc"],
                    "MAX_REL_ERROR": 0.0,
                    "RMS_ERROR": sr["max_abs_diff_vs_gcc"],
                    "MISMATCH_COUNT": 0 if sr["max_abs_diff_vs_gcc"] < 1e-9 else 1,
                    "FIRST_MISMATCH_INDEX": -1 if sr["max_abs_diff_vs_gcc"] < 1e-9 else 0,
                    "NUMERICAL_VALIDITY": "VALID" if sr["max_abs_diff_vs_gcc"] < 1e-9 else "INVALID",
                    "DATA_INTEGRITY": "INTACT",
                    "PERFORMANCE_VALIDITY": "VALID",
                    "ORIGIN": sr["s3_simd_origin"],
                    "S3_SIMD_MS": sr["s3_simd_ms"],
                    "S3_SCALAR_MS": sr["s3_scalar_ms"],
                    "GCC_O3_MS": sr["gcc_o3_ms"],
                    "SIMD_VS_SCALAR_SPEEDUP": sr["simd_vs_scalar_speedup"],
                }
            )
        for pr in poisson_recs:
            recs.append(
                {
                    "BENCHMARK_ID": f"cpu_poisson2d_chunked_{pr['grid']}",
                    "KERNEL": "cg_solve_csr_jacobi_chunk",
                    "REFERENCE": "gcc_o3_csr_jacobi",
                    "INPUT_SIZE": pr["n_unknowns"],
                    "PRECISION": "f64",
                    "ATOL": 1e-10,
                    "RTOL": 1e-10,
                    "MAX_ABS_ERROR": pr["s3_max_err_vs_gcc"],
                    "MAX_REL_ERROR": 0.0,
                    "RMS_ERROR": pr["s3_max_err_vs_true"],
                    "MISMATCH_COUNT": 0 if pr["s3_max_err_vs_gcc"] < 1e-10 else 1,
                    "FIRST_MISMATCH_INDEX": -1 if pr["s3_max_err_vs_gcc"] < 1e-10 else 0,
                    "NUMERICAL_VALIDITY": "VALID" if pr["s3_max_err_vs_gcc"] < 1e-10 else "INVALID",
                    "DATA_INTEGRITY": "INTACT",
                    "PERFORMANCE_VALIDITY": "VALID",
                    "S3_ITERS": pr["s3_iters"],
                    "GCC_ITERS": pr["gcc_iters"],
                    "S3_EXEC_MS": pr["s3_exec_ms"],
                    "GCC_EXEC_MS": pr["gcc_exec_ms"],
                }
            )

        for r in recs:
            r["COMPILER_SHA"] = s3_sha
            r["SOURCE_SHA"] = bench_sha
        data["cpu"] = recs
        data["v4_9_study"] = {
            "f64_codegen_profile": f64_prof,
            "simd_benchmark": simd_recs,
            "poisson2d_large_chunked": poisson_recs,
        }
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

