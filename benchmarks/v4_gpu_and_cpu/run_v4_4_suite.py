"""Reproducible S3 V4.4 CPU & GPU benchmark suite with integrated Validation Engine."""

from __future__ import annotations

import argparse
import csv
import ctypes
import json
import math
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Callable

THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
S3_ROOT = BENCH_ROOT.parent / "S3"
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from validation_engine import validate_array


def _timing_stats(fn: Callable[[], Any], *, warmups: int = 3, samples: int = 11) -> dict[str, Any]:
    for _ in range(warmups):
        fn()
    times_ms: list[float] = []
    for _ in range(samples):
        t0 = time.perf_counter()
        fn()
        times_ms.append((time.perf_counter() - t0) * 1000.0)
    times_sorted = sorted(times_ms)
    qs = statistics.quantiles(times_sorted, n=4)
    return {
        "median_ms": round(statistics.median(times_sorted), 4),
        "q1_ms": round(qs[0], 4),
        "q3_ms": round(qs[2], 4),
        "iqr_ms": round(qs[2] - qs[0], 4),
        "min_ms": round(times_sorted[0], 4),
        "max_ms": round(times_sorted[-1], 4),
        "samples": samples,
        "warmups": warmups,
    }


def _compile_s3_lib(src_path: Path, opt: Any, *, regalloc: bool, cost_model: bool, tmp: Path, tag: str) -> ctypes.CDLL:
    from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
    from bootstrap.s3.pipeline import compile_source

    tc = NativeToolchain.detect()
    assert tc is not None, "NativeToolchain required"
    _, ap = compile_source(src_path.read_text(encoding="utf-8"), opt).require_ordinary_artifacts()
    asm = X8664Backend(register_allocation=regalloc, selective_hp_cost_model=cost_model)._generate_ffi(ap)
    so = tc.build_shared(asm, tmp / f"{tag}.so")
    return ctypes.CDLL(str(so))


def _build_c_reference(tmp: Path, opt_flag: str) -> ctypes.CDLL:
    c_src = tmp / "ref_kernels.c"
    c_src.write_text(
        """
#include <stdint.h>
double c_simpson(const double* y, int64_t n, double dx) {
    double odd = 0.0, even = 0.0;
    for (int64_t i = 1; i < n - 1; ++i) {
        if (i & 1) odd += y[i];
        else even += y[i];
    }
    return (dx / 3.0) * (y[0] + y[n - 1] + 4.0 * odd + 2.0 * even);
}
int64_t c_cg_dense(const double* a, const double* b, double* x, double* r, double* p, double* ap, int64_t n, double tol2, int64_t max_iter) {
    for (int64_t i = 0; i < n; ++i) {
        double ax = 0.0;
        for (int64_t j = 0; j < n; ++j) ax += a[i * n + j] * x[j];
        r[i] = b[i] - ax;
        p[i] = r[i];
    }
    double rs_old = 0.0;
    for (int64_t i = 0; i < n; ++i) rs_old += r[i] * r[i];
    if (rs_old <= tol2) return 0;
    for (int64_t it = 0; it < max_iter; ++it) {
        double pAp = 0.0;
        for (int64_t i = 0; i < n; ++i) {
            double s = 0.0;
            for (int64_t j = 0; j < n; ++j) s += a[i * n + j] * p[j];
            ap[i] = s;
            pAp += p[i] * s;
        }
        if (pAp <= 0.0) return -3;
        double alpha = rs_old / pAp;
        double rs_new = 0.0;
        for (int64_t i = 0; i < n; ++i) {
            x[i] += alpha * p[i];
            r[i] -= alpha * ap[i];
            rs_new += r[i] * r[i];
        }
        if (rs_new <= tol2) return it + 1;
        double beta = rs_new / rs_old;
        for (int64_t i = 0; i < n; ++i) p[i] = r[i] + beta * p[i];
        rs_old = rs_new;
    }
    return max_iter;
}
""",
        encoding="utf-8",
    )
    so = tmp / f"ref_{opt_flag.replace('-', '')}.so"
    subprocess.run(["cc", opt_flag, "-shared", "-fPIC", str(c_src), "-o", str(so)], check=True)
    lib = ctypes.CDLL(str(so))
    d_ptr = ctypes.POINTER(ctypes.c_double)
    lib.c_simpson.argtypes = [d_ptr, ctypes.c_int64, ctypes.c_double]
    lib.c_simpson.restype = ctypes.c_double
    lib.c_cg_dense.argtypes = [d_ptr] * 6 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
    lib.c_cg_dense.restype = ctypes.c_int64
    return lib


def run_cpu_suite() -> list[dict[str, Any]]:
    from bootstrap.s3.pipeline import OptimizationLevel

    records: list[dict[str, Any]] = []
    num_src = S3_ROOT / "examples/horizons_v4/s3_sci_numerics_v5.s3"
    d_ptr = ctypes.POINTER(ctypes.c_double)
    i_ptr = ctypes.POINTER(ctypes.c_int64)

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        variants = {
            "S3_O0": _compile_s3_lib(num_src, OptimizationLevel.O0, regalloc=False, cost_model=False, tmp=tmp, tag="s3_o0"),
            "S3_O1": _compile_s3_lib(num_src, OptimizationLevel.O1, regalloc=True, cost_model=False, tmp=tmp, tag="s3_o1"),
            "S3_CostModel_V4_4": _compile_s3_lib(num_src, OptimizationLevel.O1, regalloc=True, cost_model=True, tmp=tmp, tag="s3_cm"),
        }
        c_libs = {"GCC_O2": _build_c_reference(tmp, "-O2"), "GCC_O3": _build_c_reference(tmp, "-O3")}

        # 1. Simpson 2001 points (x300)
        n_s = 2001
        dx = 1.0 / (n_s - 1)
        ys = [math.sin(math.pi * (i * dx)) for i in range(n_s)]
        ys_c = (ctypes.c_double * n_s)(*ys)
        exact_simpson = 2.0 / math.pi

        for name, lib in variants.items():
            lib.simpson_integrate.argtypes = [d_ptr, ctypes.c_int64, ctypes.c_int64, ctypes.c_double]
            lib.simpson_integrate.restype = ctypes.c_double
            val = lib.simpson_integrate(ys_c, n_s, n_s, dx)
            rec = validate_array(
                benchmark_id=f"CPU_SIMPSON_2K_{name}",
                kernel=f"simpson_integrate:{name}",
                algorithm="quadrature",
                actual=[val],
                reference=[exact_simpson],
                reference_name="analytical_2_over_pi",
                precision="f64",
            )
            rec["TIMING"] = _timing_stats(lambda: [lib.simpson_integrate(ys_c, n_s, n_s, dx) for _ in range(300)])
            records.append(rec)

        for cname, clib in c_libs.items():
            val = clib.c_simpson(ys_c, n_s, dx)
            rec = validate_array(
                benchmark_id=f"CPU_SIMPSON_2K_{cname}",
                kernel=f"c_simpson:{cname}",
                algorithm="quadrature",
                actual=[val],
                reference=[exact_simpson],
                reference_name="analytical_2_over_pi",
                precision="f64",
            )
            rec["TIMING"] = _timing_stats(lambda: [clib.c_simpson(ys_c, n_s, dx) for _ in range(300)])
            records.append(rec)

        # 2. CG Dense & CSR & Jacobi CSR (12x12 SPD tridiagonal, x200)
        n_cg = 12
        a_mat = [[0.0] * n_cg for _ in range(n_cg)]
        for i in range(n_cg):
            a_mat[i][i] = 4.0
            if i > 0:
                a_mat[i][i - 1] = -1.0
            if i + 1 < n_cg:
                a_mat[i][i + 1] = -1.0
        x_true = [1.0 + i / (n_cg - 1) for i in range(n_cg)]
        b_vec = [sum(a_mat[i][j] * x_true[j] for j in range(n_cg)) for i in range(n_cg)]
        a_c = (ctypes.c_double * (n_cg * n_cg))(*[v for row in a_mat for v in row])
        b_c = (ctypes.c_double * n_cg)(*b_vec)
        x_c, r_c, p_c, ap_c = [(ctypes.c_double * n_cg)() for _ in range(4)]

        for name, lib in variants.items():
            lib.cg_solve_dense.argtypes = [d_ptr, ctypes.c_int64] * 6 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
            lib.cg_solve_dense.restype = ctypes.c_int64

            def _run_dense() -> None:
                ctypes.memset(x_c, 0, ctypes.sizeof(x_c))
                lib.cg_solve_dense(a_c, n_cg * n_cg, b_c, n_cg, x_c, n_cg, r_c, n_cg, p_c, n_cg, ap_c, n_cg, n_cg, 1e-12, 50)

            _run_dense()
            rec = validate_array(
                benchmark_id=f"CPU_CG_DENSE_12X12_{name}",
                kernel=f"cg_solve_dense:{name}",
                algorithm="cg",
                actual=list(x_c),
                reference=x_true,
                reference_name="analytical_spd_solution",
                precision="f64",
            )
            rec["TIMING"] = _timing_stats(lambda: [_run_dense() for _ in range(200)])
            records.append(rec)

        for cname, clib in c_libs.items():
            def _run_c_dense() -> None:
                ctypes.memset(x_c, 0, ctypes.sizeof(x_c))
                clib.c_cg_dense(a_c, b_c, x_c, r_c, p_c, ap_c, n_cg, 1e-12, 50)

            _run_c_dense()
            rec = validate_array(
                benchmark_id=f"CPU_CG_DENSE_12X12_{cname}",
                kernel=f"c_cg_dense:{cname}",
                algorithm="cg",
                actual=list(x_c),
                reference=x_true,
                reference_name="analytical_spd_solution",
                precision="f64",
            )
            rec["TIMING"] = _timing_stats(lambda: [_run_c_dense() for _ in range(200)])
            records.append(rec)

        # CSR & Jacobi CSR on S3_CostModel_V4_4
        cm_lib = variants["S3_CostModel_V4_4"]
        rp_l, ci_l, vl_l = [0], [], []
        for i in range(n_cg):
            for j in range(n_cg):
                if a_mat[i][j] != 0.0:
                    ci_l.append(j)
                    vl_l.append(float(a_mat[i][j]))
            rp_l.append(len(ci_l))
        rp_c = (ctypes.c_int64 * len(rp_l))(*rp_l)
        ci_c = (ctypes.c_int64 * len(ci_l))(*ci_l)
        vl_c = (ctypes.c_double * len(vl_l))(*vl_l)
        dg_c = (ctypes.c_double * n_cg)(*[float(a_mat[i][i]) for i in range(n_cg)])
        z_c = (ctypes.c_double * n_cg)()
        res2_c = (ctypes.c_double * 1)()

        cm_lib.cg_solve_csr.argtypes = [i_ptr, ctypes.c_int64] * 2 + [d_ptr, ctypes.c_int64] * 6 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
        cm_lib.cg_solve_csr.restype = ctypes.c_int64
        cm_lib.cg_solve_csr_jacobi.argtypes = [i_ptr, ctypes.c_int64] * 2 + [d_ptr, ctypes.c_int64] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64, d_ptr, ctypes.c_int64]
        cm_lib.cg_solve_csr_jacobi.restype = ctypes.c_int64

        def _run_csr() -> None:
            ctypes.memset(x_c, 0, ctypes.sizeof(x_c))
            cm_lib.cg_solve_csr(rp_c, len(rp_l), ci_c, len(ci_l), vl_c, len(vl_l), b_c, n_cg, x_c, n_cg, r_c, n_cg, p_c, n_cg, ap_c, n_cg, n_cg, 1e-12, 50)

        _run_csr()
        rec_csr = validate_array(
            benchmark_id="CPU_CG_CSR_12X12_S3_CostModel_V4_4",
            kernel="cg_solve_csr:S3_CostModel_V4_4",
            algorithm="cg",
            actual=list(x_c),
            reference=x_true,
            reference_name="analytical_spd_solution",
            precision="f64",
        )
        rec_csr["TIMING"] = _timing_stats(lambda: [_run_csr() for _ in range(200)])
        records.append(rec_csr)

        def _run_jacobi() -> None:
            ctypes.memset(x_c, 0, ctypes.sizeof(x_c))
            cm_lib.cg_solve_csr_jacobi(rp_c, len(rp_l), ci_c, len(ci_l), vl_c, len(vl_l), dg_c, n_cg, b_c, n_cg, x_c, n_cg, r_c, n_cg, z_c, n_cg, p_c, n_cg, ap_c, n_cg, n_cg, 1e-12, 50, res2_c, 1)

        _run_jacobi()
        rec_jac = validate_array(
            benchmark_id="CPU_CG_CSR_JACOBI_12X12_S3_CostModel_V4_4",
            kernel="cg_solve_csr_jacobi:S3_CostModel_V4_4",
            algorithm="cg",
            actual=list(x_c),
            reference=x_true,
            reference_name="analytical_spd_solution",
            precision="f64",
        )
        rec_jac["TIMING"] = _timing_stats(lambda: [_run_jacobi() for _ in range(200)])
        records.append(rec_jac)

    return records


def run_gpu_suite() -> dict[str, Any]:
    import numpy as np
    from bootstrap.s3.gpu import (
        SAFE_BUFFER_BYTES,
        GpuIntegrityError,
        GpuResidentSession,
        GpuRuntime,
        build_matmul_v3_kernel,
        build_tiled_matmul_kernel,
        compile_s3_to_wgsl,
        discover_gpu_devices,
    )

    if not discover_gpu_devices():
        return {"status": "SKIPPED", "records": []}

    rt = GpuRuntime(require_physical=True)
    ex_dir = S3_ROOT / "examples" / "gpu_v3"
    mm1_k = compile_s3_to_wgsl((ex_dir / "matmul_gpu.s3").read_text(encoding="utf-8"), "matmul_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    mm2_k = build_tiled_matmul_kernel(16)
    mm3_k = build_matmul_v3_kernel(16)
    records: list[dict[str, Any]] = []
    rng = np.random.default_rng(7)

    for n in (64, 128, 256):
        a = rng.standard_normal((n, n), dtype=np.float32)
        b = rng.standard_normal((n, n), dtype=np.float32)
        ref = a @ b
        numpy_timing = _timing_stats(lambda: a @ b, warmups=5, samples=21)
        allow_unsafe = (n * n * 4) > SAFE_BUFFER_BYTES

        for kname, kern, wg in (
            ("V1_naive", mm1_k, (n // 8, n // 8, 1)),
            ("V2_tiled", mm2_k, (n // 16, n // 16, 1)),
            ("V3_padded_fma", mm3_k, (n // 16, n // 16, 1)),
        ):
            try:
                cold = rt.execute(
                    kern,
                    {"a": a.ravel(), "b": b.ravel(), "c": np.zeros(n * n, dtype=np.float32)},
                    {"m": n, "n": n, "k_dim": n},
                    workgroups=wg,
                    allow_unsafe_buffers=allow_unsafe,
                )
                sess = GpuResidentSession(
                    rt, kern, {"a": a.ravel(), "b": b.ravel(), "c": np.zeros(n * n, dtype=np.float32)},
                    {"m": n, "n": n, "k_dim": n}, allow_unsafe_buffers=allow_unsafe,
                )
                try:
                    warm_timing = _timing_stats(lambda: sess.dispatch(wg), warmups=3, samples=11)
                    c_gpu = np.frombuffer(sess.readback("c"), dtype=np.float32).reshape(n, n)
                finally:
                    sess.close()

                rec = validate_array(
                    benchmark_id=f"GPU_MATMUL_{kname}_{n}",
                    kernel=f"matmul:{kname}",
                    algorithm="matmul",
                    actual=c_gpu,
                    reference=ref,
                    reference_name="numpy_f32_matmul",
                    precision="f32",
                    k_dim=n,
                )
                rec["TIMING"] = {
                    "cold_pipeline_ms": round(cold.pipeline_s * 1000.0, 4),
                    "h2d_ms": round(cold.h2d_s * 1000.0, 4),
                    "warm_dispatch": warm_timing,
                    "readback_ms": round(cold.d2h_s * 1000.0, 4),
                    "end_to_end_cold_ms": round(cold.total_s * 1000.0, 4),
                    "numpy_cpu": numpy_timing,
                }
            except GpuIntegrityError as exc:
                rec = {
                    "BENCHMARK_ID": f"GPU_MATMUL_{kname}_{n}",
                    "KERNEL": f"matmul:{kname}",
                    "REFERENCE": "numpy_f32_matmul",
                    "INPUT_SIZE": n * n,
                    "PRECISION": "f32",
                    "ATOL": None,
                    "RTOL": None,
                    "MAX_ABS_ERROR": None,
                    "MAX_REL_ERROR": None,
                    "RMS_ERROR": None,
                    "MISMATCH_COUNT": None,
                    "FIRST_MISMATCH_INDEX": None,
                    "NUMERICAL_VALIDITY": "INVALID",
                    "DATA_INTEGRITY": f"CORRUPTION_SUSPECTED:RUNTIME_INTEGRITY_REJECTED:{exc}",
                    "PERFORMANCE_VALIDITY": "DIAGNOSTIC_ONLY",
                    "TIMING": {"numpy_cpu": numpy_timing},
                }
            records.append(rec)

    # Safe GPU Labs with per-run numerical validation
    w_k = compile_s3_to_wgsl((ex_dir / "wave_2d_gpu.s3").read_text(encoding="utf-8"), "wave2d_step", allow_narrowing=True, workgroup_size=(8, 8, 1))
    u_prev = np.zeros((32, 32), dtype=np.float32)
    u_curr = np.zeros((32, 32), dtype=np.float32)
    u_curr[16, 16] = 1.0
    u_next = np.zeros((32, 32), dtype=np.float32)
    w_res = rt.execute(w_k, {"u_prev": u_prev.ravel(), "u_curr": u_curr.ravel(), "u_next": u_next.ravel()}, {"w": 32, "h": 32, "c2": 0.2}, workgroups=(4, 4, 1))
    u_gpu = np.frombuffer(w_res.outputs["u_next"], dtype=np.float32).reshape(32, 32)
    u_ref = np.zeros_like(u_curr)
    for y in range(1, 31):
        for x in range(1, 31):
            lap = u_curr[y - 1, x] + u_curr[y + 1, x] + u_curr[y, x - 1] + u_curr[y, x + 1] - np.float32(4.0) * u_curr[y, x]
            u_ref[y, x] = np.float32(2.0) * u_curr[y, x] - u_prev[y, x] + np.float32(0.2) * lap
    w_rec = validate_array(benchmark_id="GPU_LAB_WAVE2D_32X32", kernel="wave2d_gpu", algorithm="stencil", actual=u_gpu, reference=u_ref, reference_name="numpy_wave2d_f32", precision="f32")
    w_rec["TIMING"] = {"end_to_end_ms": round(w_res.total_s * 1000.0, 4), "dispatch_ms": round(w_res.dispatch_s * 1000.0, 4)}
    records.append(w_rec)

    return {"device": rt.device_info.name, "backend": rt.device_info.backend, "records": records}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("cpu", "gpu"), required=True)
    args = parser.parse_args()
    out_json = THIS_DIR / "results_v4_4.json"
    out_csv = THIS_DIR / "results_v4_4.csv"
    data = json.loads(out_json.read_text(encoding="utf-8")) if out_json.exists() else {"cpu": [], "gpu": {}}
    if args.mode == "cpu":
        data["cpu"] = run_cpu_suite()
    else:
        data["gpu"] = run_gpu_suite()
    out_json.write_text(json.dumps(data, indent=2), encoding="utf-8")

    # Flatten CSV
    all_recs = list(data.get("cpu", [])) + list(data.get("gpu", {}).get("records", []))
    fields = [
        "BENCHMARK_ID", "KERNEL", "REFERENCE", "INPUT_SIZE", "PRECISION", "ATOL", "RTOL",
        "MAX_ABS_ERROR", "MAX_REL_ERROR", "RMS_ERROR", "MISMATCH_COUNT", "FIRST_MISMATCH_INDEX",
        "NUMERICAL_VALIDITY", "DATA_INTEGRITY", "PERFORMANCE_VALIDITY",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in all_recs:
            w.writerow({k: r.get(k) for k in fields})
    print(json.dumps({"total_records": len(all_recs), "valid": sum(1 for r in all_recs if r["NUMERICAL_VALIDITY"] == "VALID"), "invalid": sum(1 for r in all_recs if r["NUMERICAL_VALIDITY"] == "INVALID")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
