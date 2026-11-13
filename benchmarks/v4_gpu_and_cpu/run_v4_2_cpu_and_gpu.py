from __future__ import annotations

import argparse
import ctypes
import json
import math
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

BENCH_ROOT = Path(__file__).resolve().parents[2]
S3_ROOT = BENCH_ROOT.parent / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))


def _median_ms(fn, warmup: int = 2, reps: int = 7) -> float:
    for _ in range(warmup):
        fn()
    times = []
    for _ in range(reps):
        t0 = time.perf_counter()
        fn()
        times.append((time.perf_counter() - t0) * 1000.0)
    return round(statistics.median(times), 4)


def run_cpu_suite() -> dict[str, Any]:
    from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
    from bootstrap.s3.backends.x86_64.cost_model import evaluate_function_cost_model
    from bootstrap.s3.pipeline import OptimizationLevel, compile_source

    tc = NativeToolchain.detect()
    if tc is None:
        return {"status": "SKIPPED", "reason": "no_native_x86_64_toolchain_on_this_os"}

    v5_src = (S3_ROOT / "examples" / "horizons_v4" / "s3_sci_numerics_v5.s3").read_text(encoding="utf-8")
    _, ap_v5 = compile_source(v5_src, OptimizationLevel.O1).require_ordinary_artifacts()
    cost_metrics = {}
    for fn in ap_v5.functions:
        if not fn.external and fn.name != "main":
            d = evaluate_function_cost_model(fn)
            cost_metrics[fn.name] = {
                "hp02": d.apply_hp02,
                "hp03": d.apply_hp03,
                "hp10": d.apply_hp10,
                "metrics": d.metrics,
            }

    import shutil
    cc_bin = shutil.which("gcc") or shutil.which("clang") or "cc"
    results: dict[str, Any] = {"toolchain": cc_bin, "cost_model_decisions": cost_metrics, "kernels": {}}
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        # Compile S3 baseline (selective_hp_cost_model=False) vs S3 V4 CostModel (True)
        libs: dict[str, ctypes.CDLL] = {}
        for variant, sel in [("S3_O1_Base", False), ("S3_V4_CostModel", True)]:
            asm = X8664Backend(register_allocation=True, selective_hp_cost_model=sel)._generate_ffi(ap_v5)
            so = tc.build_shared(asm, tmp / f"v5_{variant}.so")
            lib = ctypes.CDLL(str(so))
            d_ptr = ctypes.POINTER(ctypes.c_double)
            lib.simpson_integrate.argtypes = [d_ptr, ctypes.c_int64, ctypes.c_int64, ctypes.c_double]
            lib.simpson_integrate.restype = ctypes.c_double
            lib.cg_solve_dense.argtypes = [d_ptr, ctypes.c_int64] * 6 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
            lib.cg_solve_dense.restype = ctypes.c_int64
            lib.rk4_adaptive_linear1d.argtypes = [ctypes.c_double] * 6 + [ctypes.c_int64]
            lib.rk4_adaptive_linear1d.restype = ctypes.c_double
            libs[variant] = lib

        # Compile equivalent C reference (-O2 and -O3)
        c_src = r"""
        #include <math.h>
        double c_simpson(const double *y, long n, double dx) {
            double acc = y[0] + y[n - 1];
            for (long i = 1; i < n - 1; i += 2) {
                acc += 4.0 * y[i];
                if (i + 1 < n - 1) acc += 2.0 * y[i + 1];
            }
            return (dx / 3.0) * acc;
        }
        long c_cg(const double *a, const double *b, double *x, double *r, double *p, double *ap, long n, double tol2, long max_iter) {
            double rs_old = 0.0;
            for (long i = 0; i < n; ++i) {
                double ax = 0.0;
                for (long j = 0; j < n; ++j) ax += a[i * n + j] * x[j];
                double ri = b[i] - ax;
                r[i] = ri; p[i] = ri; rs_old += ri * ri;
            }
            if (rs_old <= tol2) return 0;
            for (long it = 0; it < max_iter; ++it) {
                double p_ap = 0.0;
                for (long i = 0; i < n; ++i) {
                    double s = 0.0;
                    for (long j = 0; j < n; ++j) s += a[i * n + j] * p[j];
                    ap[i] = s; p_ap += p[i] * s;
                }
                double alpha = rs_old / p_ap, rs_new = 0.0;
                for (long i = 0; i < n; ++i) {
                    x[i] += alpha * p[i];
                    r[i] -= alpha * ap[i];
                    rs_new += r[i] * r[i];
                }
                if (rs_new <= tol2) return it + 1;
                double beta = rs_new / rs_old;
                for (long i = 0; i < n; ++i) p[i] = r[i] + beta * p[i];
                rs_old = rs_new;
            }
            return -1;
        }
        """
        c_path = tmp / "ref.c"
        c_path.write_text(c_src, encoding="utf-8")
        c_libs: dict[str, ctypes.CDLL] = {}
        for opt in ("O2", "O3"):
            so_c = tmp / f"ref_{opt}.so"
            subprocess.run([cc_bin, f"-{opt}", "-shared", "-fPIC", str(c_path), "-o", str(so_c), "-lm"], check=True)
            clib = ctypes.CDLL(str(so_c))
            d_ptr = ctypes.POINTER(ctypes.c_double)
            clib.c_simpson.argtypes = [d_ptr, ctypes.c_int64, ctypes.c_double]
            clib.c_simpson.restype = ctypes.c_double
            clib.c_cg.argtypes = [d_ptr] * 6 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
            clib.c_cg.restype = ctypes.c_int64
            c_libs[f"C_GCC_{opt}"] = clib

        # 1. Simpson N=2,001 x 500 reps (within default 100k instruction guard per call)
        n_sim = 2001
        dx = 2.0 / (n_sim - 1)
        ys = (ctypes.c_double * n_sim)(*[(i * dx) ** 3 for i in range(n_sim)])
        sim_res = {}
        for k, lib in libs.items():
            sim_res[k] = _median_ms(lambda l=lib: [l.simpson_integrate(ys, n_sim, n_sim, dx) for _ in range(500)])
        for k, clib in c_libs.items():
            sim_res[k] = _median_ms(lambda l=clib: [l.c_simpson(ys, n_sim, dx) for _ in range(500)])
        sim_res["speedup_cost_model_vs_base"] = round(sim_res["S3_O1_Base"] / sim_res["S3_V4_CostModel"], 3)
        results["kernels"]["simpson_2k_x500"] = sim_res

        # 2. CG Dense N=12 tridiagonal x 500 reps
        dim = 12
        a_arr = (ctypes.c_double * (dim * dim))()
        for i in range(dim):
            a_arr[i * dim + i] = 2.0
            if i > 0:
                a_arr[i * dim + (i - 1)] = -1.0
            if i + 1 < dim:
                a_arr[i * dim + (i + 1)] = -1.0
        b_arr = (ctypes.c_double * dim)(*([1.0] + [0.0] * (dim - 2) + [1.0]))
        x_arr = (ctypes.c_double * dim)()
        r_arr = (ctypes.c_double * dim)()
        p_arr = (ctypes.c_double * dim)()
        ap_arr = (ctypes.c_double * dim)()

        def _zero_x() -> None:
            for i in range(dim):
                x_arr[i] = 0.0

        cg_res = {}
        for k, lib in libs.items():
            def _run_s3(l=lib):
                for _ in range(500):
                    _zero_x()
                    l.cg_solve_dense(a_arr, dim * dim, b_arr, dim, x_arr, dim, r_arr, dim, p_arr, dim, ap_arr, dim, dim, 1e-20, 100)
            cg_res[k] = _median_ms(_run_s3)
        for k, clib in c_libs.items():
            def _run_c(l=clib):
                for _ in range(500):
                    _zero_x()
                    l.c_cg(a_arr, b_arr, x_arr, r_arr, p_arr, ap_arr, dim, 1e-20, 100)
            cg_res[k] = _median_ms(_run_c)
        cg_res["speedup_cost_model_vs_base"] = round(cg_res["S3_O1_Base"] / cg_res["S3_V4_CostModel"], 3)
        results["kernels"]["cg_dense_12x12_x500"] = cg_res

    return results


def run_gpu_suite() -> dict[str, Any]:
    import numpy as np
    from bootstrap.s3.gpu import (
        GpuRuntime,
        SAFE_BUFFER_BYTES,
        build_tiled_matmul_kernel,
        compile_s3_to_wgsl,
        discover_gpu_devices,
    )

    devices = discover_gpu_devices()
    if not devices:
        return {"status": "SKIPPED", "reason": "no_gpu_device_on_this_os"}

    rt = GpuRuntime(require_physical=True)
    out: dict[str, Any] = {
        "device": rt.device_info.name,
        "backend": rt.device_info.backend,
        "safe_buffer_bytes": SAFE_BUFFER_BYTES,
        "matmul": [],
        "stencil2d": [],
        "v4_2_labs": [],
    }

    # 1. MatMul scaling: 64, 128 (within safe boundary) vs 256 (beyond safe boundary)
    rng = np.random.default_rng(42)
    tiled_k = build_tiled_matmul_kernel(16)
    for n in (64, 128, 256):
        a = rng.standard_normal((n, n), dtype=np.float32)
        b = rng.standard_normal((n, n), dtype=np.float32)
        c = np.zeros((n, n), dtype=np.float32)
        cpu_ms = _median_ms(lambda: a @ b, warmup=1, reps=5)
        within_safe = (n * n * 4) <= SAFE_BUFFER_BYTES
        res = rt.execute(
            tiled_k,
            {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()},
            {"m": n, "n": n, "k_dim": n},
            workgroups=(math.ceil(n / 16), math.ceil(n / 16), 1),
            verify_integrity=within_safe,
            enforce_safe_bounds=within_safe,
        )
        c_gpu = np.frombuffer(res.outputs["c"], dtype=np.float32).reshape(n, n)
        c_ref = a @ b
        max_abs = float(np.max(np.abs(c_gpu - c_ref)))
        valid = bool(np.allclose(c_gpu, c_ref, rtol=1e-3, atol=1e-2))
        out["matmul"].append({
            "n": n,
            "buffer_bytes": n * n * 4,
            "within_safe_bounds": within_safe,
            "cpu_numpy_ms": cpu_ms,
            "gpu_total_ms": round(res.total_s * 1000.0, 3),
            "gpu_dispatch_ms": round(res.dispatch_s * 1000.0, 3),
            "max_abs_error": max_abs,
            "PERFORMANCE_MEASURED": True,
            "NUMERICALLY_VALID_RESULT": valid,
        })

    # 2. Stencil 2D 64x64 (4096 elems <= 32768 safe boundary), steps 1, 10, 50, 100
    st_src = (S3_ROOT / "examples" / "gpu_v3" / "stencil2d_gpu.s3").read_text(encoding="utf-8")
    st_k = compile_s3_to_wgsl(st_src, "stencil2d_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    side = 64
    u0 = np.zeros((side, side), dtype=np.float32)
    u0[side // 2, side // 2] = 100.0
    c_val = np.float32(0.1)

    def _cpu_stencil(steps: int) -> np.ndarray:
        u = u0.copy()
        for _ in range(steps):
            nxt = u.copy()
            nxt[1:-1, 1:-1] = u[1:-1, 1:-1] + c_val * (
                u[:-2, 1:-1] + u[2:, 1:-1] + u[1:-1, :-2] + u[1:-1, 2:] - np.float32(4.0) * u[1:-1, 1:-1]
            )
            u = nxt
        return u

    for steps in (1, 10, 50, 100):
        cpu_ms = _median_ms(lambda s=steps: _cpu_stencil(s), warmup=1, reps=5)
        u_ref = _cpu_stencil(steps)
        res = rt.execute_pingpong(
            st_k, "u_in", "u_out",
            {"u_in": u0.ravel(), "u_out": u0.copy().ravel()},
            {"w": side, "h": side, "c": 0.1},
            steps=steps,
            workgroups=(side // 8, side // 8, 1),
        )
        u_gpu = np.frombuffer(res.outputs["final"], dtype=np.float32).reshape(side, side)
        max_abs = float(np.max(np.abs(u_gpu - u_ref)))
        valid = bool(np.allclose(u_gpu, u_ref, rtol=1e-4, atol=1e-4))
        out["stencil2d"].append({
            "side": side,
            "steps": steps,
            "cpu_numpy_ms": cpu_ms,
            "gpu_total_ms": round(res.total_s * 1000.0, 3),
            "gpu_dispatch_ms": round(res.dispatch_s * 1000.0, 3),
            "max_abs_error": max_abs,
            "PERFORMANCE_MEASURED": True,
            "NUMERICALLY_VALID_RESULT": valid,
        })

    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["cpu", "gpu", "all"], default="all")
    parser.add_argument("--out", default=str(Path(__file__).resolve().parent / "results_v4_2.json"))
    args = parser.parse_args()

    out_path = Path(args.out)
    existing = json.loads(out_path.read_text(encoding="utf-8")) if out_path.is_file() else {}
    if args.mode in ("cpu", "all"):
        existing["cpu"] = run_cpu_suite()
    if args.mode in ("gpu", "all"):
        existing["gpu"] = run_gpu_suite()

    out_path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(existing, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
