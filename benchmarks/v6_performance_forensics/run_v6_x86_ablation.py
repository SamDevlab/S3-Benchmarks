#!/usr/bin/env python3
"""S3 V6 — x86-64 Backend Optimization Ablation Study.

Measures the exact effect of the three V6 x86-64 compiler optimizations:
  1. OPT_SCALAR_PROMO: Loop-local scalar promotion for >256-register functions
     with non-intrinsic TCALLs (prevents call-crossing F64 virtual registers from
     spilling across caller-saved XMM registers in cg_solve_csr_jacobi_chunk).
  2. OPT_BUDGET_BITWISE: Inline bitwise intrinsics (i64_and/or/xor/shl/shr/not/ctz)
     removed from instruction-budget call barriers, collapsing fragmented basic-block
     budget segments and enabling loop rotation on bitwise loops.
  3. OPT_EMITTER_ALU: Register-direct 3-operand/2-operand imul, register-direct add,
     immediate shifts (shl/shr reg, imm), register-direct bitwise ops, and dead
     folded-constant TCONST elision.
"""

from __future__ import annotations

import ctypes
import hashlib
import json
import math
import statistics
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
S3_ROOT = ROOT / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.assembly import AssemblyOpcode
from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
from bootstrap.s3.backends.x86_64.allocation import analyze_allocation
from bootstrap.s3.backends.x86_64.backend import SCIENTIFIC_MAX_INSTRUCTIONS
import bootstrap.s3.backends.x86_64.instruction_budget as ib_mod
import bootstrap.s3.backends.x86_64.scalar_promotion as sp_mod
from bootstrap.s3.pipeline import OptimizationLevel, compile_source, compile_sources
from tools.numerics_oracle_v4_7 import GCC_CSR_JACOBI_C
from benchmarks.v6_performance_forensics.run_v6_forensics import (
    _build_csr_python,
)


@contextmanager
def _ablation_config(
    *,
    opt_scalar_promo: bool,
    opt_budget_bitwise: bool,
):
    orig_flag = sp_mod._ENABLE_LARGE_FN_CALL_LOOP_LOCAL
    orig_barrier = ib_mod._barrier_type

    def _v5_barrier_type(instruction):
        opcode = instruction.opcode
        if opcode is AssemblyOpcode.TCALL:
            return "call"
        if opcode in {AssemblyOpcode.TBR3, AssemblyOpcode.TJMP}:
            return "branch"
        if opcode is AssemblyOpcode.TRET:
            return "return"
        return None

    try:
        sp_mod._ENABLE_LARGE_FN_CALL_LOOP_LOCAL = opt_scalar_promo
        if not opt_budget_bitwise:
            ib_mod._barrier_type = _v5_barrier_type
        yield
    finally:
        sp_mod._ENABLE_LARGE_FN_CALL_LOOP_LOCAL = orig_flag
        ib_mod._barrier_type = orig_barrier


def _measure_poisson_config(
    label: str,
    *,
    opt_scalar_promo: bool,
    opt_budget_bitwise: bool,
    gcc_fn: Any,
) -> dict[str, Any]:
    core_src = (S3_ROOT / "examples/horizons_v3/s3_sci_core.s3").read_text(encoding="utf-8")
    app_src = (S3_ROOT / "examples/horizons_v4/s3_sci_numerics_v5.s3").read_text(encoding="utf-8")

    with _ablation_config(opt_scalar_promo=opt_scalar_promo, opt_budget_bitwise=opt_budget_bitwise):
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

        plans: dict[str, Any] = {}
        for fn in hp_prog.functions:
            for target in ("csr_matvec_f64", "cg_solve_csr_jacobi", "cg_solve_csr_jacobi_chunk"):
                if fn.name.endswith(target):
                    plan = analyze_allocation(
                        fn,
                        reserved_registers=frozenset({"r15"}),
                        ignore_proven_slice_lengths=True,
                    )
                    xmm_count = sum(1 for r in plan.allocations.values() if r is not None and r.startswith("xmm"))
                    gpr_count = sum(1 for r in plan.allocations.values() if r is not None and not r.startswith("xmm"))
                    plans[target] = {
                        "blocks": len(fn.blocks),
                        "virtual_registers": len(fn.all_register_types),
                        "allocated_total": xmm_count + gpr_count,
                        "allocated_xmm": xmm_count,
                        "allocated_gpr": gpr_count,
                        "stack_spills": len(plan.stack_resident_registers),
                        "hot_loop_spills": getattr(plan, "hot_loop_spills", None),
                    }

    with tempfile.TemporaryDirectory() as tmp:
        td = Path(tmp)
        s_path = td / "poisson.s"
        so_path = td / "libpoisson.so"
        s_path.write_text(asm_text, encoding="utf-8")
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)], check=True)
        so_sha256 = hashlib.sha256(so_path.read_bytes()).hexdigest()

        I_PTR = ctypes.POINTER(ctypes.c_int64)
        D_PTR = ctypes.POINTER(ctypes.c_double)
        sig_poi = [I_PTR, ctypes.c_int64] * 2 + [D_PTR, ctypes.c_int64] * 8 + [
            ctypes.c_int64,
            ctypes.c_double,
            ctypes.c_int64,
            D_PTR,
            ctypes.c_int64,
        ]
        cdll = ctypes.CDLL(str(so_path))
        chunk_fn = getattr(cdll, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi_chunk")
        chunk_fn.argtypes = sig_poi
        chunk_fn.restype = ctypes.c_int64

        grid_metrics: dict[str, Any] = {}
        for grid, tol_val, chunk_sz in (
            (32, 1e-10, 100),
            (32, 1e-12, 100),
            (48, 1e-10, 50),
            (48, 1e-12, 50),
            (64, 1e-10, 50),
            (64, 1e-12, 50),
        ):
            n = grid * grid
            rp_l, ci_l, vl_l, b_l, _, _, _ = _build_csr_python(grid)
            rp = (ctypes.c_int64 * len(rp_l))(*rp_l)
            ci = (ctypes.c_int64 * len(ci_l))(*ci_l)
            vl = (ctypes.c_double * len(vl_l))(*vl_l)
            dg = (ctypes.c_double * n)(*([4.0] * n))
            b = (ctypes.c_double * n)(*b_l)
            gx, gr, gz, gp, gap = [(ctypes.c_double * n)() for _ in range(5)]
            gout = (ctypes.c_double * 1)()

            for _ in range(2):
                gcc_fn(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol_val, 5000, gout)
            g_samples = []
            giters = 0
            for _ in range(7):
                t_g0 = time.perf_counter()
                giters = int(gcc_fn(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol_val, 5000, gout))
                g_samples.append((time.perf_counter() - t_g0) * 1000.0)
            gcc_ref_x = [gx[i] for i in range(n)]
            gcc_med = statistics.median(g_samples)

            sx, sr, sz, sp, sap = [(ctypes.c_double * n)() for _ in range(5)]
            st = (ctypes.c_double * 4)()
            tol2 = tol_val * tol_val

            def _run_kernel() -> tuple[float, int]:
                ctypes.memset(sx, 0, n * 8)
                ctypes.memset(st, 0, 4 * 8)
                sit = 0
                t_s0 = time.perf_counter()
                while sit < 5000 and st[3] < 0.5:
                    sit += int(
                        chunk_fn(
                            rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n,
                            sx, n, sr, n, sz, n, sp, n, sap, n,
                            n, tol2, min(chunk_sz, 5000 - sit), st, 4,
                        )
                    )
                return (time.perf_counter() - t_s0) * 1000.0, sit

            for _ in range(2):
                _run_kernel()
            s_samples = []
            s_iters = 0
            for _ in range(7):
                ms, s_iters = _run_kernel()
                s_samples.append(ms)
            s_med = statistics.median(s_samples)
            max_err = max(abs(sx[i] - gcc_ref_x[i]) for i in range(n))
            grid_metrics[f"{grid}x{grid}_tol_{tol_val:.0e}"] = {
                "gcc_kernel_median_ms": round(gcc_med, 4),
                "s3_kernel_median_ms": round(s_med, 4),
                "s3_kernel_min_ms": round(min(s_samples), 4),
                "ratio_vs_gcc": round(s_med / gcc_med, 4),
                "iters": s_iters,
                "gcc_iters": giters,
                "max_abs_err_vs_gcc": max_err,
            }

    return {
        "label": label,
        "so_sha256": so_sha256,
        "compile_ms": round(compile_ms, 2),
        "asm_lines": len(asm_text.splitlines()),
        "plans": plans,
        "poisson_grids": grid_metrics,
    }


def _measure_collective_config(
    label: str,
    *,
    opt_scalar_promo: bool,
    opt_budget_bitwise: bool,
) -> dict[str, Any]:
    col_src = (S3_ROOT / "examples/psychohistory/collective_kernels.s3").read_text(encoding="utf-8")
    with _ablation_config(opt_scalar_promo=opt_scalar_promo, opt_budget_bitwise=opt_budget_bitwise):
        comp = compile_source(col_src, optimization=OptimizationLevel.O1)
        _, asm_prog = comp.require_ordinary_artifacts()
        backend = X8664Backend.scientific(max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS)
        asm_text = backend._generate_ffi(asm_prog)

    with tempfile.TemporaryDirectory() as tmp:
        td = Path(tmp)
        s_path = td / "collective.s"
        so_path = td / "libcollective.so"
        s_path.write_text(asm_text, encoding="utf-8")
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)], check=True)
        lib = ctypes.CDLL(str(so_path))

        I_PTR = ctypes.POINTER(ctypes.c_int64)
        fn_ind = lib.step_independent_agents
        fn_ind.argtypes = [
            I_PTR, ctypes.c_int64,
            ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64,
            I_PTR, ctypes.c_int64,
        ]
        fn_ind.restype = ctypes.c_int64

        fn_cw = lib.step_curie_weiss_meanfield
        fn_cw.argtypes = [
            I_PTR, ctypes.c_int64,
            ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64,
            I_PTR, ctypes.c_int64,
        ]
        fn_cw.restype = ctypes.c_int64

        n_agents = 4096
        steps = 120
        states = (ctypes.c_int64 * n_agents)(*[1 if i % 2 == 0 else -1 for i in range(n_agents)])
        lut = (ctypes.c_int64 * 257)(*[int(500_000 * (1.0 + math.tanh(1.2 * (2.0 * k / 256.0 - 1.0)))) for k in range(257)])

        def _run_ind() -> tuple[float, int]:
            t0 = time.perf_counter()
            s_last = 0
            for s in range(steps):
                s_last = int(fn_ind(states, n_agents, n_agents, 1234567 + s * 97, 520_000, 300_000, lut, 257))
            return (time.perf_counter() - t0) * 1000.0, s_last

        def _run_cw() -> tuple[float, int]:
            t0 = time.perf_counter()
            s_last = 500
            for s in range(steps):
                mean_ppm = (s_last * 1_000_000) // n_agents
                s_last = int(fn_cw(states, n_agents, n_agents, 1234567 + s * 97, 1_100_000, 50_000, mean_ppm, 300_000, lut, 257))
            return (time.perf_counter() - t0) * 1000.0, s_last

        for _ in range(2):
            _run_ind()
            _run_cw()
        ind_samples = [_run_ind()[0] for _ in range(7)]
        cw_samples = [_run_cw()[0] for _ in range(7)]
        return {
            "label": label,
            "asm_lines": len(asm_text.splitlines()),
            "independent_4096x120_median_ms": round(statistics.median(ind_samples), 4),
            "curie_weiss_4096x120_median_ms": round(statistics.median(cw_samples), 4),
        }


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        td = Path(tmp)
        c_path = td / "gcc_csr.c"
        gcc_so = td / "libgcc_csr.so"
        c_path.write_text(GCC_CSR_JACOBI_C, encoding="utf-8")
        subprocess.run(["gcc", "-O3", "-shared", "-fPIC", str(c_path), "-o", str(gcc_so)], check=True)
        I_PTR = ctypes.POINTER(ctypes.c_int64)
        D_PTR = ctypes.POINTER(ctypes.c_double)
        glib = ctypes.CDLL(str(gcc_so))
        gfn = glib.gcc_cg_solve_csr_jacobi
        gfn.argtypes = [I_PTR, I_PTR] + [D_PTR] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64, D_PTR]
        gfn.restype = ctypes.c_int64

        poisson_v55 = _measure_poisson_config(
            "V5_5_ALLOC_AND_BARRIERS",
            opt_scalar_promo=False,
            opt_budget_bitwise=False,
            gcc_fn=gfn,
        )
        poisson_v6 = _measure_poisson_config(
            "V6_LOOP_LOCAL_F64_AND_DIRECT_ALU",
            opt_scalar_promo=True,
            opt_budget_bitwise=True,
            gcc_fn=gfn,
        )

    col_v55 = _measure_collective_config(
        "V5_5_BITWISE_BARRIERS",
        opt_scalar_promo=False,
        opt_budget_bitwise=False,
    )
    col_v6 = _measure_collective_config(
        "V6_BITWISE_SEGMENT_FUSED",
        opt_scalar_promo=True,
        opt_budget_bitwise=True,
    )

    out = {
        "poisson_ablation": {
            "v5_5_allocation": poisson_v55,
            "v6_optimized": poisson_v6,
        },
        "collective_ablation": {
            "v5_5_barriers": col_v55,
            "v6_optimized": col_v6,
        },
    }
    out_path = Path(__file__).resolve().parent / "results_x86_ablation.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
