#!/usr/bin/env python3
"""V7 Compiler Research Experiment (Wave 17): Constant-Hoisting Mode Ablation.

Compares `experimental_hoist_constants_mode` across three controlled settings
under `instruction_budget_mode="loop-hybrid"` and `selective_hp_cost_model=True`:
  - "off"              : default S3 V7 policy (hoist_constants=False)
  - "all"              : aggressive loop-invariant TCONST hoisting (header + body)
  - "pressure-bounded" : hoist up to 2 high-value TCONSTs iff loop pressure <= 10 regs
"""

from __future__ import annotations

import ctypes
import json
import math
from pathlib import Path
import statistics
import sys
import tempfile
import time
from typing import Any

S3_ROOT = Path(__file__).resolve().parents[3] / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.assembly import AssemblyOpcode
from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
from bootstrap.s3.backends.x86_64.allocation import analyze_allocation_diagnostics
from bootstrap.s3.backends.x86_64.loop_bounds import _find_natural_loops
from bootstrap.s3.pipeline import OptimizationLevel, compile_source

MODES = ("off", "all", "pressure-bounded")

AXPY_DOT_SOURCE = """
export fn vec_axpy_dot(x: &[f64], y: &mut [f64], alpha: f64, n: i64) -> f64:
    mut acc: f64 = 0.0
    mut i: i64 = 0
    while i < n:
        mut nv: f64 = y[i] + alpha * x[i] + 0.0625
        y[i] = nv
        acc = acc + nv * x[i]
        i = i + 1
    return acc

fn main() -> i64:
    return 0
"""


def _build_poisson_csr(
    side: int,
) -> tuple[list[int], list[int], list[float], list[float], list[float], list[float]]:
    row_ptr = [0]
    col_idx: list[int] = []
    vals: list[float] = []
    diag: list[float] = []
    rhs: list[float] = []
    u_true: list[float] = []
    h = 1.0 / (side + 1)
    h2 = h * h
    for r in range(side):
        for c in range(side):
            row = r * side + c
            if r > 0:
                col_idx.append((r - 1) * side + c)
                vals.append(-1.0)
            if c > 0:
                col_idx.append(r * side + (c - 1))
                vals.append(-1.0)
            col_idx.append(row)
            vals.append(4.0)
            diag.append(4.0)
            if c + 1 < side:
                col_idx.append(r * side + (c + 1))
                vals.append(-1.0)
            if r + 1 < side:
                col_idx.append((r + 1) * side + c)
                vals.append(-1.0)
            row_ptr.append(len(col_idx))
            x = (c + 1) * h
            y = (r + 1) * h
            u_poly = 16.0 * x * (1.0 - x) * y * (1.0 - y)
            lap_poly = 32.0 * (y * (1.0 - y) + x * (1.0 - x))
            u_mode = 0.3 * math.sin(3.0 * math.pi * x) * math.sin(2.0 * math.pi * y)
            lap_mode = (13.0 * (math.pi ** 2)) * u_mode
            u = u_poly + u_mode
            lap_u = lap_poly + lap_mode
            u_true.append(u)
            rhs.append(lap_u * h2)
    return row_ptr, col_idx, vals, diag, rhs, u_true


def _compile_mode_program(
    source: str,
    mode: str,
    target_fn: str,
    so_path: Path,
) -> tuple[Path, dict[str, Any]]:
    _, ap = compile_source(source, OptimizationLevel.O1).require_ordinary_artifacts()
    backend = X8664Backend(
        max_instructions=50_000_000,
        register_allocation=True,
        instruction_budget_mode="loop-hybrid",
        selective_hp_cost_model=True,
        experimental_hoist_constants_mode=mode,
    )
    post_hp, _ = backend._apply_hp_passes(ap)
    target = next(fn for fn in post_hp.functions if fn.name == target_fn)
    diag = analyze_allocation_diagnostics(target)
    loop_labels = {lbl for _, blks in _find_natural_loops(target) for lbl in blks}
    tconst_in_loops = sum(
        1
        for blk in target.blocks
        if blk.label in loop_labels
        for ins in blk.instructions
        if ins.opcode is AssemblyOpcode.TCONST
    )
    asm = backend._generate_ffi(ap)
    tc = NativeToolchain.detect()
    assert tc is not None, "Linux x86-64 NativeToolchain required"
    tc.build_shared(asm, so_path)
    return so_path, {
        "function": target_fn,
        "stack_resident_vregs": diag.stack_resident_vregs,
        "allocated_vregs": diag.allocated_vregs,
        "total_vregs": diag.total_vregs,
        "f64_xmm_allocated": diag.f64_xmm_allocated,
        "f64_spilled": diag.f64_spilled,
        "tmov_same_color": diag.tmov_same_color,
        "tmov_diff_color": diag.tmov_diff_color,
        "tconst_in_loops_post_hp": tconst_in_loops,
        "asm_lines": asm.count("\n"),
        "asm_bytes": len(asm.encode("utf-8")),
    }


def _bench_poisson_48x48(source: str, workdir: Path, trials: int = 11) -> dict[str, Any]:
    side = 48
    n = side * side
    row_ptr, col_idx, vals, diag_vals, rhs, u_true = _build_poisson_csr(side)
    rp_len = len(row_ptr)
    nz_len = len(col_idx)
    tol2 = (1e-10) ** 2

    rp_c = (ctypes.c_int64 * rp_len)(*row_ptr)
    ci_c = (ctypes.c_int64 * nz_len)(*col_idx)
    va_c = (ctypes.c_double * nz_len)(*vals)
    dg_c = (ctypes.c_double * n)(*diag_vals)
    b_c = (ctypes.c_double * n)(*rhs)

    i64p = ctypes.POINTER(ctypes.c_int64)
    f64p = ctypes.POINTER(ctypes.c_double)

    compiled: dict[str, tuple[Any, dict[str, Any]]] = {}
    for mode in MODES:
        so_path, meta = _compile_mode_program(
            source, mode, "cg_solve_csr_jacobi_chunk", workdir / f"poisson_{mode}.so"
        )
        lib = ctypes.CDLL(str(so_path))
        fn = lib.cg_solve_csr_jacobi_chunk
        fn.argtypes = [
            i64p, ctypes.c_int64,
            i64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            f64p, ctypes.c_int64,
            ctypes.c_int64, ctypes.c_double, ctypes.c_int64,
            f64p, ctypes.c_int64,
        ]
        fn.restype = ctypes.c_int64
        compiled[mode] = (fn, meta)

    samples_by_mode: dict[str, list[float]] = {m: [] for m in MODES}
    last_by_mode: dict[str, tuple[int, float, list[float]]] = {}
    for trial in range(trials + 2):
        order = MODES[trial % len(MODES):] + MODES[: trial % len(MODES)]
        for mode in order:
            fn, _ = compiled[mode]
            x_c = (ctypes.c_double * n)()
            r_c = (ctypes.c_double * n)()
            z_c = (ctypes.c_double * n)()
            p_c = (ctypes.c_double * n)()
            ap_c = (ctypes.c_double * n)()
            st_c = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
            total_iters = 0
            t0 = time.perf_counter_ns()
            while total_iters < 5000 and st_c[3] < 0.5:
                step = min(100, 5000 - total_iters)
                rc = int(fn(
                    rp_c, rp_len,
                    ci_c, nz_len,
                    va_c, nz_len,
                    dg_c, n,
                    b_c, n,
                    x_c, n,
                    r_c, n,
                    z_c, n,
                    p_c, n,
                    ap_c, n,
                    n, tol2, step,
                    st_c, 4,
                ))
                assert rc >= 0, f"CG error rc={rc}"
                total_iters += rc
                if rc == 0:
                    break
            t1 = time.perf_counter_ns()
            if trial >= 2:
                samples_by_mode[mode].append((t1 - t0) / 1e6)
            last_by_mode[mode] = (total_iters, float(st_c[0]), [x_c[k] for k in range(n)])

    mode_results: dict[str, Any] = {}
    ref_x = last_by_mode["off"][2]
    ref_iters = last_by_mode["off"][0]
    for mode in MODES:
        _, meta = compiled[mode]
        last_iters, last_res2, last_x = last_by_mode[mode]
        samples_ms = samples_by_mode[mode]
        max_err_true = max(abs(a - b) for a, b in zip(last_x, u_true))
        assert last_iters > 50 and max_err_true < 1e-2, (
            f"unexpected CG convergence: iters={last_iters} res2={last_res2} err_true={max_err_true}"
        )
        max_diff = max(abs(a - b) for a, b in zip(last_x, ref_x))
        assert last_iters == ref_iters
        assert max_diff < 1e-12
        mode_results[mode] = {
            **meta,
            "iters": last_iters,
            "final_res2": last_res2,
            "max_abs_err_vs_true": max_err_true,
            "max_abs_diff_vs_off": max_diff,
            "median_ms": statistics.median(samples_ms),
            "min_ms": min(samples_ms),
            "max_ms": max(samples_ms),
        }
    return mode_results


def _bench_grid_i64(
    kernel_id: str,
    source: str,
    fn_name: str,
    diag_fn_name: str,
    initial: list[int],
    width: int,
    height: int,
    steps: int,
    workdir: Path,
    trials: int = 13,
) -> dict[str, Any]:
    total = width * height
    i64p = ctypes.POINTER(ctypes.c_int64)
    compiled_grid: dict[str, tuple[Any, dict[str, Any]]] = {}
    for mode in MODES:
        so_path, meta = _compile_mode_program(
            source, mode, diag_fn_name, workdir / f"{kernel_id}_{mode}.so"
        )
        lib = ctypes.CDLL(str(so_path))
        fn = getattr(lib, fn_name)
        fn.argtypes = [i64p, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, i64p, ctypes.c_int64]
        fn.restype = ctypes.c_int64
        compiled_grid[mode] = (fn, meta)

    samples_by_mode: dict[str, list[float]] = {m: [] for m in MODES}
    checksum_by_mode: dict[str, int] = {}
    for trial in range(trials + 2):
        order = MODES[trial % len(MODES):] + MODES[: trial % len(MODES)]
        for mode in order:
            fn, _ = compiled_grid[mode]
            a = (ctypes.c_int64 * total)(*initial)
            b = (ctypes.c_int64 * total)()
            t0 = time.perf_counter_ns()
            for _ in range(steps):
                fn(a, total, width, height, b, total)
                a, b = b, a
            t1 = time.perf_counter_ns()
            if trial >= 2:
                samples_by_mode[mode].append((t1 - t0) / 1e6)
            checksum_by_mode[mode] = sum(a[k] for k in range(total)) & 0xFFFFFFFFFFFFFFFF

    ref_checksum = checksum_by_mode["off"]
    mode_results: dict[str, Any] = {}
    for mode in MODES:
        _, meta = compiled_grid[mode]
        checksum = checksum_by_mode[mode]
        samples_ms = samples_by_mode[mode]
        assert checksum == ref_checksum
        mode_results[mode] = {
            **meta,
            "checksum": checksum,
            "parity_ok": checksum == ref_checksum,
            "median_ms": statistics.median(samples_ms),
            "min_ms": min(samples_ms),
            "max_ms": max(samples_ms),
        }
    return mode_results


def _bench_axpy_dot(workdir: Path, n: int = 1024, repeats: int = 1200, trials: int = 13) -> dict[str, Any]:
    f64p = ctypes.POINTER(ctypes.c_double)
    x_init = [(k % 97) * 0.0125 + 0.1 for k in range(n)]
    y_init = [(k % 53) * 0.025 - 0.5 for k in range(n)]
    x_c = (ctypes.c_double * n)(*x_init)

    compiled_axpy: dict[str, tuple[Any, dict[str, Any]]] = {}
    for mode in MODES:
        so_path, meta = _compile_mode_program(
            AXPY_DOT_SOURCE, mode, "vec_axpy_dot", workdir / f"axpy_dot_{mode}.so"
        )
        lib = ctypes.CDLL(str(so_path))
        fn = lib.vec_axpy_dot
        fn.argtypes = [f64p, ctypes.c_int64, f64p, ctypes.c_int64, ctypes.c_double, ctypes.c_int64]
        fn.restype = ctypes.c_double
        compiled_axpy[mode] = (fn, meta)

    samples_by_mode: dict[str, list[float]] = {m: [] for m in MODES}
    dot_by_mode: dict[str, float] = {}
    for trial in range(trials + 2):
        order = MODES[trial % len(MODES):] + MODES[: trial % len(MODES)]
        for mode in order:
            fn, _ = compiled_axpy[mode]
            y_c = (ctypes.c_double * n)(*y_init)
            t0 = time.perf_counter_ns()
            acc = 0.0
            for _ in range(repeats):
                acc = fn(x_c, n, y_c, n, 0.25, n)
            t1 = time.perf_counter_ns()
            if trial >= 2:
                samples_by_mode[mode].append((t1 - t0) / 1e6)
            dot_by_mode[mode] = float(acc)

    ref_dot = dot_by_mode["off"]
    mode_results: dict[str, Any] = {}
    for mode in MODES:
        _, meta = compiled_axpy[mode]
        last_dot = dot_by_mode[mode]
        samples_ms = samples_by_mode[mode]
        rel_diff = abs(last_dot - ref_dot) / max(1.0, abs(ref_dot))
        assert rel_diff < 1e-12
        mode_results[mode] = {
            **meta,
            "final_dot": last_dot,
            "rel_diff_vs_off": rel_diff,
            "median_ms": statistics.median(samples_ms),
            "min_ms": min(samples_ms),
            "max_ms": max(samples_ms),
        }
    return mode_results


def main() -> int:
    sci_src = (S3_ROOT / "examples/horizons_v4/s3_sci_numerics_v5.s3").read_text(encoding="utf-8")
    stencil_src = (S3_ROOT / "examples/compute/stencil5point.s3").read_text(encoding="utf-8")
    conway_src = (S3_ROOT / "examples/compute/conway.s3").read_text(encoding="utf-8")

    w, h = 64, 64
    conway_init = [1 if ((r * 13 + c * 7) % 5 == 0) else 0 for r in range(h) for c in range(w)]
    stencil_init = [(i * 31 + 7) % 256 for i in range(w * h)]

    with tempfile.TemporaryDirectory(prefix="s3-v7-compiler-research-") as tmp:
        workdir = Path(tmp)
        workloads = {
            "poisson_csr_48x48_tol1e10": _bench_poisson_48x48(sci_src, workdir),
            "stencil5point_64x64_250": _bench_grid_i64(
                "stencil", stencil_src, "stencil5point_step", "stencil5point_step", stencil_init, w, h, 250, workdir
            ),
            "conway_step_64x64_150": _bench_grid_i64(
                "conway", conway_src, "conway_step", "step_rule", conway_init, w, h, 150, workdir
            ),
            "axpy_dot_f64_1024": _bench_axpy_dot(workdir),
        }

    comparisons: dict[str, Any] = {}
    pb_speedups: list[float] = []
    all_speedups: list[float] = []
    pb_spill_deltas: dict[str, int] = {}
    all_spill_deltas: dict[str, int] = {}

    for name, modes in workloads.items():
        base_ms = modes["off"]["median_ms"]
        all_ms = modes["all"]["median_ms"]
        pb_ms = modes["pressure-bounded"]["median_ms"]
        sp_all = base_ms / all_ms if all_ms > 0 else 0.0
        sp_pb = base_ms / pb_ms if pb_ms > 0 else 0.0
        all_speedups.append(sp_all)
        pb_speedups.append(sp_pb)
        all_spill_deltas[name] = (
            modes["all"]["stack_resident_vregs"] - modes["off"]["stack_resident_vregs"]
        )
        pb_spill_deltas[name] = (
            modes["pressure-bounded"]["stack_resident_vregs"]
            - modes["off"]["stack_resident_vregs"]
        )
        comparisons[name] = {
            "off_median_ms": round(base_ms, 4),
            "all_median_ms": round(all_ms, 4),
            "pressure_bounded_median_ms": round(pb_ms, 4),
            "speedup_all_vs_off": round(sp_all, 4),
            "speedup_pressure_bounded_vs_off": round(sp_pb, 4),
            "spill_delta_all_vs_off": all_spill_deltas[name],
            "spill_delta_pb_vs_off": pb_spill_deltas[name],
        }

    geomean_pb = math.prod(pb_speedups) ** (1.0 / len(pb_speedups))
    geomean_all = math.prod(all_speedups) ** (1.0 / len(all_speedups))
    any_pb_spill_regression = any(delta > 0 for delta in pb_spill_deltas.values())
    verdict = (
        "GO"
        if geomean_pb >= 1.03 and not any_pb_spill_regression and min(pb_speedups) >= 0.99
        else "NO_GO_DEFAULT_OFF_PRESERVED"
    )

    report = {
        "campaign": "S3_V7_WAVE17_COMPILER_RESEARCH",
        "experiment": "experimental_hoist_constants_mode",
        "default_mode_preserved": "off",
        "workloads": workloads,
        "comparisons": comparisons,
        "summary": {
            "geomean_speedup_all_vs_off": round(geomean_all, 4),
            "geomean_speedup_pressure_bounded_vs_off": round(geomean_pb, 4),
            "max_spill_delta_all": max(all_spill_deltas.values()),
            "max_spill_delta_pressure_bounded": max(pb_spill_deltas.values()),
            "decision": verdict,
        },
    }
    out_path = Path(__file__).resolve().with_name("results_v7_compiler_research.json")
    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(json.dumps(report["comparisons"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
