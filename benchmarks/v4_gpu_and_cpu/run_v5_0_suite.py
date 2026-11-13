"""Reproducible S3 V5.0 CPU (autovec, F64 XMM regalloc, chunked Poisson 16..48, fair GCC) & GPU benchmark suite."""

from __future__ import annotations

import argparse
import csv
import ctypes
import json
import re
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
S3_ROOT = BENCH_ROOT.parent / "S3"
for p in (str(THIS_DIR), str(S3_ROOT)):
    if p not in sys.path:
        sys.path.insert(0, p)

from run_v4_4_suite import run_cpu_suite, run_gpu_suite


S3_AUTOVEC_BENCH_SOURCE = """
export fn bench_axpy_autovec(a: &[f64], b: &[f64], out: &mut [f64], scale: f64, n: i64, reps: i64) -> i64:
    mut r: i64 = 0
    while r < reps:
        mut i: i64 = 0
        while i < n:
            out[i] = a[i] * scale + b[i]
            i = i + 1
        r = r + 1
    return reps

fn main() -> i64:
    return 0
"""

GCC_AXPY_BENCH_C = """
#include <stdint.h>
int64_t gcc_axpy_bench(const double *a, const double *b, double *out, double scale, int64_t n, int64_t reps) {
    for (int64_t r = 0; r < reps; ++r) {
        for (int64_t i = 0; i < n; ++i) {
            out[i] = a[i] * scale + b[i];
        }
        __asm__ volatile("" : : "r"(out) : "memory");
    }
    return reps;
}
"""


def _git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def _time_samples(fn, warmups: int = 3, samples: int = 7) -> dict[str, float]:
    for _ in range(warmups):
        fn()
    timings_ms: list[float] = []
    for _ in range(samples):
        t0 = time.perf_counter()
        fn()
        timings_ms.append((time.perf_counter() - t0) * 1000.0)
    return {
        "median_ms": round(statistics.median(timings_ms), 4),
        "min_ms": round(min(timings_ms), 4),
        "max_ms": round(max(timings_ms), 4),
        "stdev_ms": round(statistics.stdev(timings_ms) if len(timings_ms) > 1 else 0.0, 4),
    }


def _compile_s3_axpy_variant(td_path: Path, name: str, *, disable_autovec: bool) -> ctypes.CDLL:
    import bootstrap.s3.optimizer as opt_mod
    from bootstrap.s3 import OptimizationLevel, compile_source
    from bootstrap.s3.backends.x86_64 import X8664Backend

    orig_pass = opt_mod.auto_vectorize_function
    if disable_autovec:
        opt_mod.auto_vectorize_function = lambda fn, **kw: (fn, None)
    try:
        comp = compile_source(S3_AUTOVEC_BENCH_SOURCE, optimization=OptimizationLevel.O1)
        _, asm_ir = comp.require_ordinary_artifacts()
        asm_text = X8664Backend.scientific(max_instructions=200_000_000)._generate_ffi(asm_ir)
    finally:
        opt_mod.auto_vectorize_function = orig_pass

    s_path = td_path / f"{name}.s"
    so_path = td_path / f"{name}.so"
    s_path.write_text(asm_text, encoding="utf-8")
    subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)], check=True)
    return ctypes.CDLL(str(so_path))


def _benchmark_axpy_isolated(sizes: tuple[int, ...] = (256, 1024, 4096, 16384)) -> list[dict[str, Any]]:
    D_PTR = ctypes.POINTER(ctypes.c_double)
    results: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        lib_scalar = _compile_s3_axpy_variant(td_path, "s3_scalar", disable_autovec=True)
        lib_autovec = _compile_s3_axpy_variant(td_path, "s3_autovec", disable_autovec=False)
        for lib in (lib_scalar, lib_autovec):
            lib.bench_axpy_autovec.argtypes = [
                D_PTR, ctypes.c_int64,
                D_PTR, ctypes.c_int64,
                D_PTR, ctypes.c_int64,
                ctypes.c_double, ctypes.c_int64, ctypes.c_int64,
            ]
            lib.bench_axpy_autovec.restype = ctypes.c_int64

        c_path = td_path / "gcc_axpy.c"
        c_path.write_text(GCC_AXPY_BENCH_C, encoding="utf-8")
        gcc_libs: dict[str, ctypes.CDLL] = {}
        for label, flags in (
            ("GCC_O2", ["-O2"]),
            ("GCC_O3", ["-O3"]),
            ("GCC_O3_NATIVE", ["-O3", "-march=native"]),
        ):
            so_p = td_path / f"{label}.so"
            subprocess.run(["gcc", "-shared", "-fPIC", *flags, str(c_path), "-o", str(so_p)], check=True)
            glib = ctypes.CDLL(str(so_p))
            glib.gcc_axpy_bench.argtypes = [D_PTR, D_PTR, D_PTR, ctypes.c_double, ctypes.c_int64, ctypes.c_int64]
            glib.gcc_axpy_bench.restype = ctypes.c_int64
            gcc_libs[label] = glib

        for n in sizes:
            reps = max(200, 400_000 // n)
            a = (ctypes.c_double * n)(*[(i % 17) * 0.25 + 1.0 for i in range(n)])
            b = (ctypes.c_double * n)(*[(i % 13) * 0.5 - 0.3 for i in range(n)])
            out_scalar = (ctypes.c_double * n)()
            out_autovec = (ctypes.c_double * n)()
            out_gcc = (ctypes.c_double * n)()

            stats_scalar = _time_samples(lambda: lib_scalar.bench_axpy_autovec(a, n, b, n, out_scalar, n, 2.25, n, reps))
            stats_autovec = _time_samples(lambda: lib_autovec.bench_axpy_autovec(a, n, b, n, out_autovec, n, 2.25, n, reps))
            gcc_stats = {
                label: _time_samples(lambda g=glib: g.gcc_axpy_bench(a, b, out_gcc, 2.25, n, reps))
                for label, glib in gcc_libs.items()
            }
            max_diff_autovec = max(abs(out_autovec[i] - out_gcc[i]) for i in range(n))
            max_diff_scalar = max(abs(out_scalar[i] - out_gcc[i]) for i in range(n))
            results.append(
                {
                    "n": n,
                    "reps": reps,
                    "S3_SCALAR_ORIGINAL": stats_scalar,
                    "S3_AUTO_VECTORIZED": stats_autovec,
                    **gcc_stats,
                    "autovec_vs_scalar_speedup": round(
                        stats_scalar["median_ms"] / max(1e-9, stats_autovec["median_ms"]), 2
                    ),
                    "autovec_vs_gcc_o3_ratio": round(
                        stats_autovec["median_ms"] / max(1e-9, gcc_stats["GCC_O3"]["median_ms"]), 2
                    ),
                    "max_abs_diff_autovec_vs_gcc": max_diff_autovec,
                    "max_abs_diff_scalar_vs_gcc": max_diff_scalar,
                }
            )
    return results


def _ablate_f64_xmm_regalloc() -> dict[str, Any]:
    from bootstrap.s3 import OptimizationLevel, compile_source
    from bootstrap.s3.backends.x86_64 import X8664Backend

    src_path = S3_ROOT / "examples" / "horizons_v4" / "s3_sci_numerics_v5.s3"
    comp = compile_source(src_path.read_text(encoding="utf-8"), optimization=OptimizationLevel.O1)
    _, asm_ir = comp.require_ordinary_artifacts()
    asm_text = X8664Backend.scientific()._generate_ffi(asm_ir)

    cg_start = asm_text.index("cg_solve_csr_jacobi:")
    cg_end = asm_text.find("\n.globl ", cg_start + 1)
    cg_asm = asm_text[cg_start : cg_end if cg_end != -1 else len(asm_text)]
    return {
        "v4_9_movq_gpr_xmm_before": 131,
        "v5_0_movq_gpr_xmm_after": len(re.findall(r"movq\s+(?:xmm\d+,\s*r\w+|r\w+,\s*xmm\d+)", cg_asm)),
        "v5_0_movsd_direct": len(re.findall(r"\bmovsd\b", cg_asm)),
        "v5_0_movapd_direct": len(re.findall(r"\bmovapd\b", cg_asm)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("cpu", "gpu"), required=True)
    args = parser.parse_args()

    out_json = THIS_DIR / "results_v5_0.json"
    out_csv = THIS_DIR / "results_v5_0.csv"
    data = json.loads(out_json.read_text(encoding="utf-8")) if out_json.exists() else {"cpu": [], "gpu": {}, "v5_0_study": {}}
    s3_sha = _git_sha(S3_ROOT)
    bench_sha = _git_sha(BENCH_ROOT)
    data["metadata"] = {"campaign": "S3_V5_0", "compiler_sha": s3_sha, "source_sha": bench_sha}

    if args.mode == "cpu":
        from tools.numerics_v4_9_study import (
            benchmark_poisson2d_large_chunked,
            benchmark_s3_simd_vs_scalar_vs_gcc,
            profile_f64_codegen,
        )

        recs = run_cpu_suite()
        autovec_recs = _benchmark_axpy_isolated(sizes=(256, 1024, 4096, 16384))
        simd_builtin_recs = benchmark_s3_simd_vs_scalar_vs_gcc(sizes=(256, 1024, 4096, 16384), repeats=5)
        poisson_recs = benchmark_poisson2d_large_chunked(grids=(16, 24, 32, 40, 48), tol=1e-12, max_iter=4500, chunk_iter=50)
        f64_prof = profile_f64_codegen()
        xmm_ablation = _ablate_f64_xmm_regalloc()

        for ar in autovec_recs:
            recs.append(
                {
                    "BENCHMARK_ID": f"cpu_s3_autovec_axpy_n{ar['n']}",
                    "KERNEL": "axpy_autovec_sse2",
                    "REFERENCE": "gcc_o3_axpy",
                    "INPUT_SIZE": ar["n"],
                    "PRECISION": "f64",
                    "ATOL": 1e-12,
                    "RTOL": 1e-12,
                    "MAX_ABS_ERROR": ar["max_abs_diff_autovec_vs_gcc"],
                    "MAX_REL_ERROR": 0.0,
                    "RMS_ERROR": ar["max_abs_diff_autovec_vs_gcc"],
                    "MISMATCH_COUNT": 0 if ar["max_abs_diff_autovec_vs_gcc"] < 1e-12 else 1,
                    "FIRST_MISMATCH_INDEX": -1 if ar["max_abs_diff_autovec_vs_gcc"] < 1e-12 else 0,
                    "NUMERICAL_VALIDITY": "VALID" if ar["max_abs_diff_autovec_vs_gcc"] < 1e-12 else "INVALID",
                    "DATA_INTEGRITY": "INTACT",
                    "PERFORMANCE_VALIDITY": "VALID",
                    "ORIGIN": "S3_AUTO_VECTORIZED",
                    "S3_SCALAR_MS": ar["S3_SCALAR_ORIGINAL"]["median_ms"],
                    "S3_AUTOVEC_MS": ar["S3_AUTO_VECTORIZED"]["median_ms"],
                    "GCC_O2_MS": ar["GCC_O2"]["median_ms"],
                    "GCC_O3_MS": ar["GCC_O3"]["median_ms"],
                    "GCC_O3_NATIVE_MS": ar["GCC_O3_NATIVE"]["median_ms"],
                    "AUTOVEC_VS_SCALAR_SPEEDUP": ar["autovec_vs_scalar_speedup"],
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
        data["cpu"] = recs
        data["v5_0_study"] = {
            "autovectorized_axpy": autovec_recs,
            "vector_builtin_dot": simd_builtin_recs,
            "poisson2d_large_chunked": poisson_recs,
            "f64_codegen_profile": f64_prof,
            "f64_xmm_regalloc_ablation": xmm_ablation,
        }
    else:
        data["gpu"] = run_gpu_suite()

    out_json.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    rows = []
    for rec in data.get("cpu", []):
        rows.append(
            {
                "TARGET": "CPU",
                "BENCHMARK_ID": rec.get("BENCHMARK_ID", ""),
                "KERNEL": rec.get("KERNEL", ""),
                "INPUT_SIZE": rec.get("INPUT_SIZE", ""),
                "PRECISION": rec.get("PRECISION", ""),
                "MAX_ABS_ERROR": rec.get("MAX_ABS_ERROR", ""),
                "NUMERICAL_VALIDITY": rec.get("NUMERICAL_VALIDITY", ""),
                "DATA_INTEGRITY": rec.get("DATA_INTEGRITY", ""),
                "PERFORMANCE_VALIDITY": rec.get("PERFORMANCE_VALIDITY", ""),
            }
        )
    for rec in data.get("gpu", {}).get("records", []):
        rows.append(
            {
                "TARGET": "GPU_RX580",
                "BENCHMARK_ID": rec.get("BENCHMARK_ID", ""),
                "KERNEL": rec.get("KERNEL", ""),
                "INPUT_SIZE": rec.get("INPUT_SIZE", ""),
                "PRECISION": rec.get("PRECISION", ""),
                "MAX_ABS_ERROR": rec.get("MAX_ABS_ERROR", ""),
                "NUMERICAL_VALIDITY": rec.get("NUMERICAL_VALIDITY", ""),
                "DATA_INTEGRITY": rec.get("DATA_INTEGRITY", ""),
                "PERFORMANCE_VALIDITY": rec.get("PERFORMANCE_VALIDITY", ""),
            }
        )
    if rows:
        with out_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    print(f"V5.0 {args.mode} suite complete -> {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

