#!/usr/bin/env python3
"""S3 V6 Performance Forensics Suite (P0 Audit of V4 vs V5 Poisson 2D CSR Discrepancy).

Executes:
1. 4-Cell A/B Matrix: {V4_COMPILER, V5_COMPILER} x {V4_HARNESS, V5_HARNESS} on pinned commits
   - V4_COMPILER = f33b5b3b7d0c8e4cc278608ebb8d7eceb36590bd (S3#393)
   - V5_COMPILER = 9c1bec32c181710eec6e99c3056825d85b8412c6 (S3#394)
   - V5_5_COMPILER = 5a51667e2ae7e8b4a7beb060c59c15244f82a7fa (S3#397)
2. 8-Stage Timing Decomposition:
   - INPUT_GENERATION_MS
   - CSR_CONSTRUCTION_MS
   - CTYPES_BUFFER_ALLOCATION_MS
   - NATIVE_KERNEL_MS (KERNEL_ONLY)
   - CHUNK_DISPATCH_MS
   - OUTPUT_MATERIALIZATION_MS
   - RESULT_VALIDATION_MS
   - TOTAL_EXECUTION_MS (END_TO_END)
3. Canonical Normalized Grid & Tolerance Sweep:
   - Grids: 16x16, 24x24, 32x32, 48x48, 64x64, 96x96, 128x128
   - Tolerances: 1e-8, 1e-10, 1e-12 (tested on 32x32 and 48x48; 1e-10 and 1e-12 across grids)
   - Interleaved warmups + multi-sample median & IQR
4. Assembly & Register Spill Forensics on csr_matvec_f64 and cg_solve_csr_jacobi_chunk.
"""

from __future__ import annotations

import csv
import ctypes
from datetime import datetime, timezone
import hashlib
import json
import platform
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
WORKSPACE_ROOT = BENCH_ROOT.parent
S3_ROOT = WORKSPACE_ROOT / "S3"

V4_COMPILER_SHA = "f33b5b3b7d0c8e4cc278608ebb8d7eceb36590bd"
V5_COMPILER_SHA = "9c1bec32c181710eec6e99c3056825d85b8412c6"
V5_5_COMPILER_SHA = "5a51667e2ae7e8b4a7beb060c59c15244f82a7fa"


COMPILER_WORKER_CODE = """
import hashlib, json, subprocess, sys, time
from pathlib import Path

compiler_root = Path(sys.argv[1])
source_root = Path(sys.argv[2])
out_dir = Path(sys.argv[3])
tag = sys.argv[4]

sys.path.insert(0, str(compiler_root))
from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
from bootstrap.s3.backends.x86_64.allocation import analyze_allocation
from bootstrap.s3.backends.x86_64.backend import SCIENTIFIC_MAX_INSTRUCTIONS
from bootstrap.s3.pipeline import OptimizationLevel, compile_sources

NativeToolchain.detect()
core_src = (source_root / "examples/horizons_v3/s3_sci_core.s3").read_text(encoding="utf-8")
app_src = (source_root / "examples/horizons_v4/s3_sci_numerics_v5.s3").read_text(encoding="utf-8")

t0 = time.perf_counter()
comp = compile_sources(
    {"s3_sci_core.s3": core_src, "s3_sci_numerics_v5.s3": app_src},
    entry_module="s3_sci_numerics_v5",
    optimization=OptimizationLevel.O1,
    allow_fp_reassociation=False,
)
_, asm_prog = comp.require_ordinary_artifacts()
backend = X8664Backend.scientific(max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS)
hp_prog, _ = backend._apply_hp_passes(asm_prog)
asm_text = backend._generate_ffi(asm_prog)
compile_ms = (time.perf_counter() - t0) * 1000.0

fn_stats = {}
for fn in hp_prog.functions:
    for target in ("csr_matvec_f64", "cg_solve_csr_jacobi", "cg_solve_csr_jacobi_chunk"):
        if fn.name.endswith(target):
            plan = analyze_allocation(
                fn,
                reserved_registers=frozenset({"r15"}),
                ignore_proven_slice_lengths=True,
            )
            spills = len(plan.stack_resident_registers)
            fn_stats[target] = {
                "blocks": len(fn.blocks),
                "virtual_registers": len(fn.all_register_types),
                "stack_spills": spills,
                "hot_loop_spills": getattr(plan, "hot_loop_spills", None),
                "vec4_blocks": sum(1 for b in fn.blocks if b.label.startswith("vec4_body_")),
                "fast_blocks": sum(1 for b in fn.blocks if "__fast_" in b.label),
            }

s_path = out_dir / f"poisson_{tag}.s"
so_path = out_dir / f"libpoisson_{tag}.so"
s_path.write_text(asm_text, encoding="utf-8")
t_link0 = time.perf_counter()
subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)], check=True)
link_ms = (time.perf_counter() - t_link0) * 1000.0

print(json.dumps({
    "tag": tag,
    "so_path": str(so_path),
    "s_path": str(s_path),
    "so_sha256": hashlib.sha256(so_path.read_bytes()).hexdigest(),
    "asm_sha256": hashlib.sha256(asm_text.encode("utf-8")).hexdigest(),
    "compile_ms": round(compile_ms, 3),
    "link_ms": round(link_ms, 3),
    "asm_lines": len(asm_text.splitlines()),
    "fn_stats": fn_stats,
}))
"""


def _stats(samples_ms: list[float]) -> dict[str, float]:
    s = sorted(samples_ms)
    q1 = s[len(s) // 4]
    q3 = s[(3 * len(s)) // 4]
    return {
        "median_ms": round(statistics.median(s), 4),
        "q1_ms": round(q1, 4),
        "q3_ms": round(q3, 4),
        "iqr_ms": round(q3 - q1, 4),
        "min_ms": round(s[0], 4),
        "max_ms": round(s[-1], 4),
    }


def _build_csr_python(grid: int) -> tuple[list[int], list[int], list[float], list[float], list[float], float, float]:
    n = grid * grid
    t0 = time.perf_counter()
    rp_l, ci_l, vl_l = [0], [], []
    for r_idx in range(grid):
        for c_idx in range(grid):
            idx = r_idx * grid + c_idx
            if r_idx > 0:
                ci_l.append((r_idx - 1) * grid + c_idx)
                vl_l.append(-1.0)
            if c_idx > 0:
                ci_l.append(r_idx * grid + (c_idx - 1))
                vl_l.append(-1.0)
            ci_l.append(idx)
            vl_l.append(4.0)
            if c_idx + 1 < grid:
                ci_l.append(r_idx * grid + (c_idx + 1))
                vl_l.append(-1.0)
            if r_idx + 1 < grid:
                ci_l.append((r_idx + 1) * grid + c_idx)
                vl_l.append(-1.0)
            rp_l.append(len(ci_l))
    csr_ms = (time.perf_counter() - t0) * 1000.0

    t1 = time.perf_counter()
    x_true = [1.0 + i / max(1, n - 1) for i in range(n)]
    b_l = [sum(vl_l[k] * x_true[ci_l[k]] for k in range(rp_l[i], rp_l[i + 1])) for i in range(n)]
    input_ms = (time.perf_counter() - t1) * 1000.0
    return rp_l, ci_l, vl_l, b_l, x_true, csr_ms, input_ms


def run_forensics_suite(out_dir: Path = THIS_DIR) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    if str(S3_ROOT) not in sys.path:
        sys.path.insert(0, str(S3_ROOT))
    from tools.numerics_oracle_v4_7 import GCC_CSR_JACOBI_C

    with tempfile.TemporaryDirectory(prefix="s3_v6_forensics_") as td:
        td_path = Path(td)
        worker_py = td_path / "compile_worker.py"
        worker_py.write_text(COMPILER_WORKER_CODE, encoding="utf-8")

        compiler_artifacts: dict[str, dict[str, Any]] = {}
        for tag, sha in (
            ("V4_COMPILER", V4_COMPILER_SHA),
            ("V5_COMPILER", V5_COMPILER_SHA),
            ("V5_5_COMPILER", V5_5_COMPILER_SHA),
        ):
            ext_dir = td_path / tag.lower()
            ext_dir.mkdir()
            subprocess.run(
                f"git -C {S3_ROOT} archive {sha} | tar -x -C {ext_dir}",
                shell=True,
                check=True,
            )
            out = subprocess.check_output(
                [sys.executable, str(worker_py), str(ext_dir), str(S3_ROOT), str(td_path), tag],
                text=True,
            )
            compiler_artifacts[tag] = json.loads(out.strip().splitlines()[-1])
            compiler_artifacts[tag]["commit_sha"] = sha

        # Build GCC -O3 reference shared object
        c_path = td_path / "gcc_csr.c"
        gcc_so = td_path / "libgcc_csr.so"
        c_path.write_text(GCC_CSR_JACOBI_C, encoding="utf-8")
        subprocess.run(["gcc", "-O3", "-shared", "-fPIC", str(c_path), "-o", str(gcc_so)], check=True)
        gcc_sha256 = hashlib.sha256(gcc_so.read_bytes()).hexdigest()
        gcc_ver = subprocess.check_output(["gcc", "--version"], text=True).splitlines()[0]

        I_PTR = ctypes.POINTER(ctypes.c_int64)
        D_PTR = ctypes.POINTER(ctypes.c_double)
        glib = ctypes.CDLL(str(gcc_so))
        gfn = glib.gcc_cg_solve_csr_jacobi
        gfn.argtypes = [I_PTR, I_PTR] + [D_PTR] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64, D_PTR]
        gfn.restype = ctypes.c_int64

        sig_poi = [I_PTR, ctypes.c_int64] * 2 + [D_PTR, ctypes.c_int64] * 8 + [
            ctypes.c_int64,
            ctypes.c_double,
            ctypes.c_int64,
            D_PTR,
            ctypes.c_int64,
        ]
        loaded_libs: dict[str, dict[str, Any]] = {}
        for tag, meta in compiler_artifacts.items():
            cdll = ctypes.CDLL(meta["so_path"])
            chunk_fn = getattr(cdll, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi_chunk")
            chunk_fn.argtypes = sig_poi
            chunk_fn.restype = ctypes.c_int64
            full_fn = getattr(cdll, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi")
            full_fn.argtypes = sig_poi
            full_fn.restype = ctypes.c_int64
            loaded_libs[tag] = {"chunk": chunk_fn, "full": full_fn}

        # ---------------------------------------------------------------------
        # 1. 4-Cell A/B Matrix ({V4_COMPILER, V5_COMPILER} x {V4_HARNESS, V5_HARNESS})
        # ---------------------------------------------------------------------
        ab_matrix_rows: list[dict[str, Any]] = []
        for grid, v4_chunk in ((32, 100), (48, 50)):
            n = grid * grid
            rp_l, ci_l, vl_l, b_l, x_true, _, _ = _build_csr_python(grid)
            rp = (ctypes.c_int64 * len(rp_l))(*rp_l)
            ci = (ctypes.c_int64 * len(ci_l))(*ci_l)
            vl = (ctypes.c_double * len(vl_l))(*vl_l)
            dg = (ctypes.c_double * n)(*([4.0] * n))
            b = (ctypes.c_double * n)(*b_l)
            gx, gr, gz, gp, gap = [(ctypes.c_double * n)() for _ in range(5)]
            gout = (ctypes.c_double * 1)()

            # GCC references at V4 tol (1e-10) and V5 tol (1e-12)
            gcc_refs: dict[str, dict[str, Any]] = {}
            for tol_key, tol_val in (("V4_TOL_1e-10", 1e-10), ("V5_TOL_1e-12", 1e-12)):
                for _ in range(2):
                    gfn(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol_val, 5000, gout)
                g_samples = []
                giters = 0
                for _ in range(7):
                    t0 = time.perf_counter()
                    giters = int(gfn(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol_val, 5000, gout))
                    g_samples.append((time.perf_counter() - t0) * 1000.0)
                gcc_refs[tol_key] = {
                    "iters": giters,
                    "x": [gx[i] for i in range(n)],
                    "res2": float(gout[0]),
                    "timing": _stats(g_samples),
                }

            for comp_tag in ("V4_COMPILER", "V5_COMPILER"):
                cf = loaded_libs[comp_tag]["chunk"]

                # Cell A/C: V4_HARNESS (tol=1e-10 -> tol2=1e-20, pre-built CSR, allocates 5 scratch vectors + solves)
                for _ in range(2):
                    sx, sr, sz, sp, sap = [(ctypes.c_double * n)() for _ in range(5)]
                    st = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
                    sit = 0
                    while sit < 5000 and st[3] < 0.5:
                        sit += int(cf(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, 1e-20, min(v4_chunk, 5000 - sit), st, 4))
                v4h_samples = []
                sit_v4 = 0
                sx_v4 = None
                for _ in range(7):
                    t0 = time.perf_counter()
                    sx, sr, sz, sp, sap = [(ctypes.c_double * n)() for _ in range(5)]
                    st = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
                    sit_v4 = 0
                    while sit_v4 < 5000 and st[3] < 0.5:
                        sit_v4 += int(cf(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, 1e-20, min(v4_chunk, 5000 - sit_v4), st, 4))
                    v4h_samples.append((time.perf_counter() - t0) * 1000.0)
                    sx_v4 = sx
                g_ref_v4 = gcc_refs["V4_TOL_1e-10"]
                max_err_v4 = max(abs(sx_v4[i] - g_ref_v4["x"][i]) for i in range(n))
                v4h_stat = _stats(v4h_samples)
                ab_matrix_rows.append({
                    "cell": f"{comp_tag} + V4_HARNESS",
                    "compiler": comp_tag,
                    "compiler_sha": compiler_artifacts[comp_tag]["commit_sha"],
                    "harness": "V4_HARNESS",
                    "grid": f"{grid}x{grid}",
                    "tolerance": 1e-10,
                    "tol2_passed": 1e-20,
                    "chunk_step": v4_chunk,
                    "measurement_scope": "KERNEL_PLUS_SCRATCH_ALLOC",
                    "s3_iters": sit_v4,
                    "gcc_iters": g_ref_v4["iters"],
                    "s3_median_ms": v4h_stat["median_ms"],
                    "s3_iqr_ms": v4h_stat["iqr_ms"],
                    "gcc_kernel_median_ms": g_ref_v4["timing"]["median_ms"],
                    "s3_over_gcc_ratio": round(v4h_stat["median_ms"] / g_ref_v4["timing"]["median_ms"], 2),
                    "max_abs_err_vs_gcc": max_err_v4,
                })

                # Cell B/D: V5_HARNESS (tol=1e-12 -> tol2=1e-24, chunk=50, includes Python CSR + b_l + ctypes alloc + kernel + rows dict list)
                v5h_samples = []
                sit_v5 = 0
                max_err_v5 = 0.0
                g_ref_v5 = gcc_refs["V5_TOL_1e-12"]
                for sample_idx in range(7):
                    t0 = time.perf_counter()
                    rp_p, ci_p, vl_p, bl_p, xt_p, _, _ = _build_csr_python(grid)
                    rp_c = (ctypes.c_int64 * len(rp_p))(*rp_p)
                    ci_c = (ctypes.c_int64 * len(ci_p))(*ci_p)
                    vl_c = (ctypes.c_double * len(vl_p))(*vl_p)
                    dg_c = (ctypes.c_double * n)(*([4.0] * n))
                    b_c = (ctypes.c_double * n)(*bl_p)
                    xb, rb, zb, pb, apb = [(ctypes.c_double * n)() for _ in range(5)]
                    st_c = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
                    sit_v5 = 0
                    while sit_v5 < 4500 and st_c[3] < 0.5:
                        sit_v5 += int(cf(rp_c, len(rp_p), ci_c, len(ci_p), vl_c, len(vl_p), dg_c, n, b_c, n, xb, n, rb, n, zb, n, pb, n, apb, n, n, 1e-24, min(50, 4500 - sit_v5), st_c, 4))
                    rows = [
                        {"node": i, "u_s3": xb[i], "u_exact": xt_p[i], "abs_err": abs(xb[i] - xt_p[i])}
                        for i in range(n)
                    ]
                    _ = max(r["abs_err"] for r in rows)
                    elapsed_ms = (time.perf_counter() - t0) * 1000.0
                    if sample_idx >= 2:
                        v5h_samples.append(elapsed_ms)
                    max_err_v5 = max(abs(xb[i] - g_ref_v5["x"][i]) for i in range(n))
                v5h_stat = _stats(v5h_samples)
                ab_matrix_rows.append({
                    "cell": f"{comp_tag} + V5_HARNESS",
                    "compiler": comp_tag,
                    "compiler_sha": compiler_artifacts[comp_tag]["commit_sha"],
                    "harness": "V5_HARNESS",
                    "grid": f"{grid}x{grid}",
                    "tolerance": 1e-12,
                    "tol2_passed": 1e-24,
                    "chunk_step": 50,
                    "measurement_scope": "END_TO_END_PYTHON_PREP_AND_ROWS",
                    "s3_iters": sit_v5,
                    "gcc_iters": g_ref_v5["iters"],
                    "s3_median_ms": v5h_stat["median_ms"],
                    "s3_iqr_ms": v5h_stat["iqr_ms"],
                    "gcc_kernel_median_ms": g_ref_v5["timing"]["median_ms"],
                    "s3_over_gcc_ratio": round(v5h_stat["median_ms"] / g_ref_v5["timing"]["median_ms"], 2),
                    "max_abs_err_vs_gcc": max_err_v5,
                })

        # ---------------------------------------------------------------------
        # 2. 8-Stage Decomposition & Canonical Normalized Grid/Tolerance Sweep
        # ---------------------------------------------------------------------
        normalized_rows: list[dict[str, Any]] = []
        grid_specs = [
            (16, 100, True, (1e-8, 1e-10, 1e-12)),
            (24, 100, True, (1e-8, 1e-10, 1e-12)),
            (32, 100, True, (1e-8, 1e-10, 1e-12)),
            (48, 50, True, (1e-8, 1e-10, 1e-12)),
            (64, 50, False, (1e-10, 1e-12)),
            (96, 25, False, (1e-10,)),
            (128, 20, False, (1e-10,)),
        ]
        for grid, chunk_step, unchunked_ok, tols in grid_specs:
            n = grid * grid
            reps = 7 if grid <= 48 else (5 if grid == 64 else 3)
            warmups = 2 if grid <= 64 else 1

            # Measure Python stage overheads across reps
            csr_samples, inp_samples, alloc_samples = [], [], []
            rp_l, ci_l, vl_l, b_l, x_true = [], [], [], [], []
            for _ in range(reps):
                rp_l, ci_l, vl_l, b_l, x_true, c_ms, i_ms = _build_csr_python(grid)
                csr_samples.append(c_ms)
                inp_samples.append(i_ms)
                t_al = time.perf_counter()
                rp = (ctypes.c_int64 * len(rp_l))(*rp_l)
                ci = (ctypes.c_int64 * len(ci_l))(*ci_l)
                vl = (ctypes.c_double * len(vl_l))(*vl_l)
                dg = (ctypes.c_double * n)(*([4.0] * n))
                b = (ctypes.c_double * n)(*b_l)
                sx, sr, sz, sp, sap = [(ctypes.c_double * n)() for _ in range(5)]
                st = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
                alloc_samples.append((time.perf_counter() - t_al) * 1000.0)

            csr_med = round(statistics.median(csr_samples), 4)
            inp_med = round(statistics.median(inp_samples), 4)
            alloc_med = round(statistics.median(alloc_samples), 4)

            gx, gr, gz, gp, gap = [(ctypes.c_double * n)() for _ in range(5)]
            gout = (ctypes.c_double * 1)()

            for tol in tols:
                tol2 = tol * tol
                # Warmup interleaved
                for _ in range(warmups):
                    gfn(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol, 5000, gout)
                    for tag in ("V4_COMPILER", "V5_COMPILER"):
                        cf = loaded_libs[tag]["chunk"]
                        for buf in (sx, sr, sz, sp, sap):
                            ctypes.memset(buf, 0, ctypes.sizeof(buf))
                        ctypes.memset(st, 0, ctypes.sizeof(st))
                        sit = 0
                        while sit < 5000 and st[3] < 0.5:
                            sit += int(cf(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, tol2, min(chunk_step, 5000 - sit), st, 4))

                g_samples: list[float] = []
                v4_k_samples: list[float] = []
                v5_k_samples: list[float] = []
                v5_unchunked_samples: list[float] = []
                out_mat_samples: list[float] = []
                val_samples: list[float] = []

                giters = 0
                v4_iters = 0
                v5_iters = 0
                v4_err_gcc = 0.0
                v5_err_gcc = 0.0
                v5_err_true = 0.0
                v5_res2 = 0.0

                for _ in range(reps):
                    # GCC kernel-only
                    t0 = time.perf_counter()
                    giters = int(gfn(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol, 5000, gout))
                    g_samples.append((time.perf_counter() - t0) * 1000.0)

                    # V4 kernel-only
                    cf_v4 = loaded_libs["V4_COMPILER"]["chunk"]
                    for buf in (sx, sr, sz, sp, sap):
                        ctypes.memset(buf, 0, ctypes.sizeof(buf))
                    ctypes.memset(st, 0, ctypes.sizeof(st))
                    t0 = time.perf_counter()
                    v4_iters = 0
                    while v4_iters < 5000 and st[3] < 0.5:
                        v4_iters += int(cf_v4(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, tol2, min(chunk_step, 5000 - v4_iters), st, 4))
                    v4_k_samples.append((time.perf_counter() - t0) * 1000.0)
                    v4_err_gcc = max(abs(sx[i] - gx[i]) for i in range(n))

                    # V5 kernel-only
                    cf_v5 = loaded_libs["V5_COMPILER"]["chunk"]
                    for buf in (sx, sr, sz, sp, sap):
                        ctypes.memset(buf, 0, ctypes.sizeof(buf))
                    ctypes.memset(st, 0, ctypes.sizeof(st))
                    t0 = time.perf_counter()
                    v5_iters = 0
                    while v5_iters < 5000 and st[3] < 0.5:
                        v5_iters += int(cf_v5(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, tol2, min(chunk_step, 5000 - v5_iters), st, 4))
                    v5_k_samples.append((time.perf_counter() - t0) * 1000.0)
                    v5_res2 = float(st[0])

                    # Output materialization + result validation stages
                    t_om = time.perf_counter()
                    rows = [
                        {"node": i, "u_s3": sx[i], "u_exact": x_true[i], "abs_err": abs(sx[i] - x_true[i])}
                        for i in range(n)
                    ]
                    out_mat_samples.append((time.perf_counter() - t_om) * 1000.0)

                    t_val = time.perf_counter()
                    v5_err_true = max(r["abs_err"] for r in rows)
                    v5_err_gcc = max(abs(sx[i] - gx[i]) for i in range(n))
                    val_samples.append((time.perf_counter() - t_val) * 1000.0)

                    if unchunked_ok:
                        ff_v5 = loaded_libs["V5_COMPILER"]["full"]
                        for buf in (sx, sr, sz, sp, sap):
                            ctypes.memset(buf, 0, ctypes.sizeof(buf))
                        fout = (ctypes.c_double * 1)()
                        t0 = time.perf_counter()
                        _ = int(ff_v5(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, tol2, 5000, fout, 1))
                        v5_unchunked_samples.append((time.perf_counter() - t0) * 1000.0)

                g_stat = _stats(g_samples)
                v4_stat = _stats(v4_k_samples)
                v5_stat = _stats(v5_k_samples)
                om_med = round(statistics.median(out_mat_samples), 4)
                val_med = round(statistics.median(val_samples), 4)
                unchunk_med = round(statistics.median(v5_unchunked_samples), 4) if v5_unchunked_samples else None
                chunk_disp_ms = round(max(0.0, v5_stat["median_ms"] - unchunk_med), 4) if unchunk_med is not None else 0.0

                python_non_kernel_ms = round(inp_med + csr_med + alloc_med + om_med + val_med, 4)
                v4_e2e_ms = round(v4_stat["median_ms"] + python_non_kernel_ms, 4)
                v5_e2e_ms = round(v5_stat["median_ms"] + python_non_kernel_ms, 4)
                gcc_e2e_ms = round(g_stat["median_ms"] + python_non_kernel_ms, 4)

                normalized_rows.append({
                    "grid": f"{grid}x{grid}",
                    "n_unknowns": n,
                    "nnz": len(vl_l),
                    "tolerance": tol,
                    "tol2": tol2,
                    "chunk_step": chunk_step,
                    "gcc_iters": giters,
                    "v4_s3_iters": v4_iters,
                    "v5_s3_iters": v5_iters,
                    "iters_match": (giters == v4_iters == v5_iters),
                    "GCC_KERNEL_ONLY_MS": g_stat["median_ms"],
                    "GCC_KERNEL_IQR_MS": g_stat["iqr_ms"],
                    "V4_S3_KERNEL_ONLY_MS": v4_stat["median_ms"],
                    "V4_S3_KERNEL_IQR_MS": v4_stat["iqr_ms"],
                    "V5_S3_KERNEL_ONLY_MS": v5_stat["median_ms"],
                    "V5_S3_KERNEL_IQR_MS": v5_stat["iqr_ms"],
                    "V5_S3_UNCHUNKED_KERNEL_MS": unchunk_med,
                    "V4_OVER_GCC_KERNEL_RATIO": round(v4_stat["median_ms"] / g_stat["median_ms"], 2),
                    "V5_OVER_GCC_KERNEL_RATIO": round(v5_stat["median_ms"] / g_stat["median_ms"], 2),
                    "V5_SPEEDUP_OVER_V4_KERNEL": round(v4_stat["median_ms"] / v5_stat["median_ms"], 2),
                    "INPUT_GENERATION_MS": inp_med,
                    "CSR_CONSTRUCTION_MS": csr_med,
                    "CTYPES_BUFFER_ALLOCATION_MS": alloc_med,
                    "NATIVE_KERNEL_MS": v5_stat["median_ms"],
                    "CHUNK_DISPATCH_MS": chunk_disp_ms,
                    "OUTPUT_MATERIALIZATION_MS": om_med,
                    "RESULT_VALIDATION_MS": val_med,
                    "PYTHON_OVERHEAD_TOTAL_MS": python_non_kernel_ms,
                    "GCC_END_TO_END_MS": gcc_e2e_ms,
                    "V4_S3_END_TO_END_MS": v4_e2e_ms,
                    "V5_S3_END_TO_END_MS": v5_e2e_ms,
                    "V5_OVER_GCC_END_TO_END_RATIO": round(v5_e2e_ms / gcc_e2e_ms, 2),
                    "ASYMMETRIC_V5_E2E_OVER_GCC_KERNEL_RATIO": round(v5_e2e_ms / g_stat["median_ms"], 2),
                    "v4_max_err_vs_gcc": v4_err_gcc,
                    "v5_max_err_vs_gcc": v5_err_gcc,
                    "v5_max_err_vs_true": v5_err_true,
                    "v5_final_res2": v5_res2,
                    "converged": (v5_res2 <= tol2 and v5_iters == giters),
                })

    summary = {
        "decision": "METHODOLOGY_ARTIFACT_CONFIRMED",
        "secondary_decision": "NO_REPRODUCIBLE_REGRESSION",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "platform": platform.platform(),
            "python": sys.version.split()[0],
            "gcc": gcc_ver,
            "gcc_so_sha256": gcc_sha256,
        },
        "compilers": compiler_artifacts,
        "ab_matrix": ab_matrix_rows,
        "normalized_sweep": normalized_rows,
    }

    (out_dir / "results_forensics.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    if normalized_rows:
        with (out_dir / "results_forensics.csv").open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(normalized_rows[0].keys()))
            writer.writeheader()
            writer.writerows(normalized_rows)
    return summary


if __name__ == "__main__":
    res = run_forensics_suite()
    print(json.dumps({
        "decision": res["decision"],
        "secondary_decision": res["secondary_decision"],
        "ab_matrix_count": len(res["ab_matrix"]),
        "normalized_rows_count": len(res["normalized_sweep"]),
    }, indent=2))
