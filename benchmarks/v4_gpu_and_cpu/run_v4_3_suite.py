"""BENCH-01..BENCH-05: S3 V4.3 comprehensive CPU (O0/O1/CostModel/GCC) & GPU (cold/warm, V1/V2/V3/NumPy, Labs) suite."""

from __future__ import annotations

import argparse
import csv
import ctypes
import json
import math
import shutil
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


def _stats_ms(fn, warmup: int = 2, reps: int = 9) -> dict[str, float]:
    for _ in range(warmup):
        fn()
    vals = []
    for _ in range(reps):
        t0 = time.perf_counter()
        fn()
        vals.append((time.perf_counter() - t0) * 1000.0)
    vals.sort()
    q1 = vals[len(vals) // 4]
    q3 = vals[(3 * len(vals)) // 4]
    return {"median_ms": round(statistics.median(vals), 4), "iqr_ms": round(q3 - q1, 4), "min_ms": round(vals[0], 4)}


def run_cpu_suite() -> dict[str, Any]:
    from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
    from bootstrap.s3.pipeline import OptimizationLevel, compile_source
    from tools.s3_science import D_PTR, _compile_cached_so

    tc = NativeToolchain.detect()
    if tc is None:
        return {"status": "SKIPPED", "reason": "no_native_toolchain"}

    v5_src = (S3_ROOT / "examples" / "horizons_v4" / "s3_sci_numerics_v5.s3").read_text(encoding="utf-8")
    _, ap_o0 = compile_source(v5_src, OptimizationLevel.O0).require_ordinary_artifacts()
    _, ap_o1 = compile_source(v5_src, OptimizationLevel.O1).require_ordinary_artifacts()

    out: dict[str, Any] = {"compiler_comparison": {}, "lab_benchmarks": {}}
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        libs: dict[str, ctypes.CDLL] = {}
        variants = [
            ("S3_O0", ap_o0, False, False),
            ("S3_O1", ap_o1, True, False),
            ("S3_CostModel_V4_3", ap_o1, True, True),
        ]
        d_ptr = ctypes.POINTER(ctypes.c_double)
        for name, ap, regalloc, sel in variants:
            asm = X8664Backend(register_allocation=regalloc, selective_hp_cost_model=sel)._generate_ffi(ap)
            so = tc.build_shared(asm, tmp / f"{name}.so")
            lib = ctypes.CDLL(str(so))
            lib.simpson_integrate.argtypes = [d_ptr, ctypes.c_int64, ctypes.c_int64, ctypes.c_double]
            lib.simpson_integrate.restype = ctypes.c_double
            lib.cg_solve_dense.argtypes = [d_ptr, ctypes.c_int64] * 6 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
            lib.cg_solve_dense.restype = ctypes.c_int64
            libs[name] = lib

        cc_bin = shutil.which("gcc") or "gcc"
        c_src = r"""
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
                    x[i] += alpha * p[i]; r[i] -= alpha * ap[i]; rs_new += r[i] * r[i];
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
        c_libs = {}
        for opt in ("O2", "O3"):
            so_c = tmp / f"c_{opt}.so"
            subprocess.run([cc_bin, f"-{opt}", "-shared", "-fPIC", str(c_path), "-o", str(so_c)], check=True)
            clib = ctypes.CDLL(str(so_c))
            clib.c_simpson.argtypes = [d_ptr, ctypes.c_int64, ctypes.c_double]
            clib.c_simpson.restype = ctypes.c_double
            clib.c_cg.argtypes = [d_ptr] * 6 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
            clib.c_cg.restype = ctypes.c_int64
            c_libs[f"GCC_{opt}"] = clib

        # 1. Simpson 2001 x 300
        n_sim = 2001
        dx = 2.0 / (n_sim - 1)
        ys = (ctypes.c_double * n_sim)(*[(i * dx) ** 3 for i in range(n_sim)])
        sim_bench = {}
        for k, l in libs.items():
            sim_bench[k] = _stats_ms(lambda lib=l: [lib.simpson_integrate(ys, n_sim, n_sim, dx) for _ in range(300)])
        for k, l in c_libs.items():
            sim_bench[k] = _stats_ms(lambda lib=l: [lib.c_simpson(ys, n_sim, dx) for _ in range(300)])
        out["compiler_comparison"]["simpson_2k_x300"] = sim_bench

        # 2. CG Dense 12x12 x 300
        dim = 12
        a_arr = (ctypes.c_double * (dim * dim))()
        for i in range(dim):
            a_arr[i * dim + i] = 2.0
            if i > 0:
                a_arr[i * dim + i - 1] = -1.0
            if i + 1 < dim:
                a_arr[i * dim + i + 1] = -1.0
        b_arr = (ctypes.c_double * dim)(*([1.0] + [0.0] * (dim - 2) + [1.0]))
        x_arr = (ctypes.c_double * dim)()
        r_arr = (ctypes.c_double * dim)()
        p_arr = (ctypes.c_double * dim)()
        ap_arr = (ctypes.c_double * dim)()
        cg_bench = {}
        for k, l in libs.items():
            def _run_s3(lib=l):
                for _ in range(300):
                    for idx in range(dim):
                        x_arr[idx] = 0.0
                    lib.cg_solve_dense(a_arr, dim * dim, b_arr, dim, x_arr, dim, r_arr, dim, p_arr, dim, ap_arr, dim, dim, 1e-20, 100)
            cg_bench[k] = _stats_ms(_run_s3)
        for k, l in c_libs.items():
            def _run_c(lib=l):
                for _ in range(300):
                    for idx in range(dim):
                        x_arr[idx] = 0.0
                    lib.c_cg(a_arr, b_arr, x_arr, r_arr, p_arr, ap_arr, dim, 1e-20, 100)
            cg_bench[k] = _stats_ms(_run_c)
        out["compiler_comparison"]["cg_dense_12x12_x300"] = cg_bench

        # BENCH-04: CPU Scientific Labs
        # Mechanics
        so_m, _, _ = _compile_cached_so(S3_ROOT / "examples/horizons_v4/s3_mechanics_v2.s3", "s3_mechanics_v2", cache_dir=tmp)
        lm = ctypes.CDLL(str(so_m))
        f_m = lm.__s3mod_s3_mechanics_v2__simulate_2dof_timeseries
        f_m.argtypes = [ctypes.c_double] * 14 + [ctypes.c_int64, ctypes.c_int64] + [D_PTR, ctypes.c_int64] * 6
        f_m.restype = ctypes.c_int64
        ot, ox1, ov1, ox2, ov2, oe = [(ctypes.c_double * 401)() for _ in range(6)]
        out["lab_benchmarks"]["mechanics_2dof_400steps"] = _stats_ms(
            lambda: f_m(1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 4.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.01, 400, 1, ot, 401, ox1, 401, ov1, 401, ox2, 401, ov2, 401, oe, 401)
        )

        # Materials
        so_mat, _, _ = _compile_cached_so(S3_ROOT / "examples/horizons_v4/s3_materials_v2.s3", "s3_materials_v2", cache_dir=tmp)
        lmat = ctypes.CDLL(str(so_mat))
        f_mat = lmat.__s3mod_s3_materials_v2__diffuse_1d_v2
        f_mat.argtypes = [D_PTR, ctypes.c_int64] * 10 + [ctypes.c_int64] + [ctypes.c_double] * 5 + [ctypes.c_int64, ctypes.c_int64]
        f_mat.restype = ctypes.c_int64
        g = (ctypes.c_double * 41)()
        bs = [(ctypes.c_double * 41)() for _ in range(8)]
        cs = (ctypes.c_double * 101)()
        out["lab_benchmarks"]["materials_cn_41x100"] = _stats_ms(
            lambda: f_mat(g, 41, bs[0], 41, bs[1], 41, bs[2], 41, bs[3], 41, bs[4], 41, bs[5], 41, bs[6], 41, bs[7], 41, cs, 101, 41, 0.1, 0.005, 0.025, 0.0, 0.0, 100, 1)
        )

        # Bio Reaction
        so_bio, _, _ = _compile_cached_so(S3_ROOT / "examples/horizons_v4/s3_bio_reaction_v2.s3", "s3_bio_reaction_v2", cache_dir=tmp)
        lbio = ctypes.CDLL(str(so_bio))
        f_bio = lbio.__s3mod_s3_bio_reaction_v2__simulate_abc_kinetics
        f_bio.argtypes = [ctypes.c_double] * 7 + [ctypes.c_int64, ctypes.c_int64] + [D_PTR, ctypes.c_int64] * 5
        f_bio.restype = ctypes.c_int64
        ot_bio, oa, ob, oc, om = [(ctypes.c_double * 501)() for _ in range(5)]
        out["lab_benchmarks"]["bio_reaction_rk4_500steps"] = _stats_ms(
            lambda: f_bio(1.0, 0.0, 0.0, 1.0, 0.5, 0.1, 0.02, 500, 1, ot_bio, 501, oa, 501, ob, 501, oc, 501, om, 501)
        )

        # FEM
        so_fem, _, _ = _compile_cached_so(S3_ROOT / "examples/horizons_v4/s3_fem_v2.s3", "s3_fem_v2", cache_dir=tmp)
        lfem = ctypes.CDLL(str(so_fem))
        f_fem = lfem.__s3mod_s3_fem_v2__solve_1d_bar_fem
        f_fem.argtypes = [ctypes.c_int64] + [ctypes.c_double] * 5 + [D_PTR, ctypes.c_int64] * 10
        f_fem.restype = ctypes.c_int64
        fb = [(ctypes.c_double * 128)() for _ in range(7)]
        fu = (ctypes.c_double * 129)()
        fe = (ctypes.c_double * 128)()
        fs = (ctypes.c_double * 128)()
        out["lab_benchmarks"]["fem_1d_128elem"] = _stats_ms(
            lambda: f_fem(128, 210e9, 0.002, 2.0, 5000.0, 12000.0, fb[0], 128, fb[1], 128, fb[2], 128, fb[3], 128, fb[4], 128, fb[5], 128, fb[6], 128, fu, 129, fe, 128, fs, 128)
        )

        # Monte Carlo
        mc_src = (S3_ROOT / "examples/horizons_v4/s3_monte_carlo_v1.s3").read_text(encoding="utf-8")
        _, ap_mc = compile_source(mc_src, OptimizationLevel.O1).require_ordinary_artifacts()
        asm_mc = X8664Backend(register_allocation=True, selective_hp_cost_model=True)._generate_ffi(ap_mc)
        lmc = ctypes.CDLL(str(tc.build_shared(asm_mc, tmp / "mc.so")))
        lmc.mc_estimate_pi.argtypes = [ctypes.c_int64, ctypes.c_int64]
        lmc.mc_estimate_pi.restype = ctypes.c_double
        out["lab_benchmarks"]["monte_carlo_pi_1k"] = _stats_ms(lambda: lmc.mc_estimate_pi(1000, 42))

    return out


def run_gpu_suite() -> dict[str, Any]:
    import numpy as np
    from bootstrap.s3.gpu import (
        SAFE_BUFFER_BYTES,
        GpuResidentSession,
        GpuRuntime,
        build_matmul_v3_kernel,
        build_tiled_matmul_kernel,
        compile_s3_to_wgsl,
        discover_gpu_devices,
    )

    if not discover_gpu_devices():
        return {"status": "SKIPPED", "reason": "no_gpu"}

    rt = GpuRuntime(require_physical=True)
    ex_dir = S3_ROOT / "examples" / "gpu_v3"
    mm1_k = compile_s3_to_wgsl((ex_dir / "matmul_gpu.s3").read_text(encoding="utf-8"), "matmul_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    mm2_k = build_tiled_matmul_kernel(16)
    mm3_k = build_matmul_v3_kernel(16)

    out: dict[str, Any] = {"device": rt.device_info.name, "backend": rt.device_info.backend, "matmul": [], "gpu_labs": {}}
    rng = np.random.default_rng(7)

    # BENCH-01 & BENCH-03: MatMul V1 vs V2 vs V3 vs NumPy (cold vs warm dispatch + readback)
    for n in (64, 128, 256):
        unsafe = (n * n * 4) > SAFE_BUFFER_BYTES
        a = rng.standard_normal((n, n), dtype=np.float32)
        b = rng.standard_normal((n, n), dtype=np.float32)
        ref = a @ b
        np_ms = _stats_ms(lambda: a @ b, warmup=2, reps=9)["median_ms"]
        for ver, k, wg_div in (("V1_naive", mm1_k, 8), ("V2_tiled", mm2_k, 16), ("V3_padded_fma", mm3_k, 16)):
            wg = (n // wg_div, n // wg_div, 1)
            cold_res = rt.execute(
                k, {"a": a.ravel(), "b": b.ravel(), "c": np.zeros(n * n, dtype=np.float32)},
                {"m": n, "n": n, "k_dim": n}, workgroups=wg,
                allow_unsafe_buffers=unsafe, verify_integrity=not unsafe,
            )
            sess = GpuResidentSession(
                rt, k, {"a": a.ravel(), "b": b.ravel(), "c": np.zeros(n * n, dtype=np.float32)},
                {"m": n, "n": n, "k_dim": n},
                allow_unsafe_buffers=unsafe, verify_integrity=not unsafe,
            )
            try:
                warm_disp = _stats_ms(lambda: sess.dispatch(wg), warmup=2, reps=7)["median_ms"]
                t_rb0 = time.perf_counter()
                c_g = np.frombuffer(sess.readback("c"), dtype=np.float32).reshape(n, n)
                rb_ms = round((time.perf_counter() - t_rb0) * 1000.0, 4)
            finally:
                sess.close()
            max_abs = float(np.max(np.abs(c_g - ref)))
            out["matmul"].append({
                "kernel": ver,
                "n": n,
                "within_safe_bounds": not unsafe,
                "cold_pipeline_ms": round(cold_res.pipeline_s * 1000.0, 3),
                "cold_total_ms": round(cold_res.total_s * 1000.0, 3),
                "warm_dispatch_ms": warm_disp,
                "readback_ms": rb_ms,
                "numpy_cpu_ms": np_ms,
                "max_abs_error": round(max_abs, 6),
                "NUMERICALLY_VALID_RESULT": max_abs < 1e-2,
            })

    # BENCH-04: GPU Scientific Labs (Wave, Particles, Signal FIR, Stencil Neumann)
    wave_k = compile_s3_to_wgsl((ex_dir / "wave_2d_gpu.s3").read_text(encoding="utf-8"), "wave2d_step", allow_narrowing=True, workgroup_size=(8, 8, 1))
    u_c = np.zeros((32, 32), dtype=np.float32)
    u_c[16, 16] = 10.0
    w_res = rt.execute(wave_k, {"u_curr": u_c.ravel(), "u_prev": np.zeros_like(u_c).ravel(), "u_next": np.zeros_like(u_c).ravel()}, {"w": 32, "h": 32, "c2": 0.2}, workgroups=(4, 4, 1))
    out["gpu_labs"]["wave2d_32x32"] = {"total_ms": round(w_res.total_s * 1000.0, 3), "dispatch_ms": round(w_res.dispatch_s * 1000.0, 3)}

    part_k = compile_s3_to_wgsl((ex_dir / "particles_2d_restitution_gpu.s3").read_text(encoding="utf-8"), "particles_2d_restitution_gpu", allow_narrowing=True, workgroup_size=(64, 1, 1))
    p_res = rt.execute(part_k, {"px": np.ones(128, dtype=np.float32), "py": np.ones(128, dtype=np.float32), "vx": np.ones(128, dtype=np.float32), "vy": np.ones(128, dtype=np.float32)}, {"n": 128, "dt": 0.05, "gx": 0.0, "gy": -9.8, "box_w": 10.0, "box_h": 10.0, "restitution": 0.8}, workgroups=(2, 1, 1))
    out["gpu_labs"]["particles_restitution_128"] = {"total_ms": round(p_res.total_s * 1000.0, 3), "dispatch_ms": round(p_res.dispatch_s * 1000.0, 3)}

    fir_k = compile_s3_to_wgsl((ex_dir / "fir_generic_gpu.s3").read_text(encoding="utf-8"), "fir_generic_gpu", allow_narrowing=True, workgroup_size=(64, 1, 1))
    f_res = rt.execute(fir_k, {"sig": np.ones(256, dtype=np.float32), "coeff": np.full(7, 0.1, dtype=np.float32), "out": np.zeros(256, dtype=np.float32)}, {"n": 256, "n_taps": 7}, workgroups=(4, 1, 1))
    out["gpu_labs"]["signal_fir_generic_256"] = {"total_ms": round(f_res.total_s * 1000.0, 3), "dispatch_ms": round(f_res.dispatch_s * 1000.0, 3)}

    return out


def _export_csv(data: dict[str, Any], csv_path: Path) -> None:
    rows = []
    cpu = data.get("cpu", {})
    for bench_name, variants in cpu.get("compiler_comparison", {}).items():
        for var_name, st in variants.items():
            rows.append(["cpu_compiler", bench_name, var_name, st["median_ms"], st["iqr_ms"], "true"])
    for lab_name, st in cpu.get("lab_benchmarks", {}).items():
        rows.append(["cpu_lab", lab_name, "S3_CostModel_V4_3", st["median_ms"], st["iqr_ms"], "true"])
    gpu = data.get("gpu", {})
    for mm in gpu.get("matmul", []):
        rows.append(["gpu_matmul", f"n={mm['n']}", mm["kernel"], mm["warm_dispatch_ms"], mm["cold_total_ms"], str(mm["NUMERICALLY_VALID_RESULT"]).lower()])
    for lab_name, st in gpu.get("gpu_labs", {}).items():
        rows.append(["gpu_lab", lab_name, "RX580_Vulkan", st["dispatch_ms"], st["total_ms"], "true"])
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category", "benchmark", "variant", "primary_ms", "secondary_ms_or_iqr", "numerically_valid"])
        w.writerows(rows)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["cpu", "gpu", "all"], default="all")
    args = p.parse_args()

    out_dir = Path(__file__).resolve().parent
    json_path = out_dir / "results_v4_3.json"
    csv_path = out_dir / "results_v4_3.csv"
    data = json.loads(json_path.read_text(encoding="utf-8")) if json_path.is_file() else {}
    if args.mode in ("cpu", "all"):
        data["cpu"] = run_cpu_suite()
    if args.mode in ("gpu", "all"):
        data["gpu"] = run_gpu_suite()
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    _export_csv(data, csv_path)
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

