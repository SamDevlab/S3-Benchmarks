#!/usr/bin/env python3
"""S3 Scientific Horizons V3 — Native Linux x86-64 Scientific Computing Benchmarks.

Measures wall-time (median, min, max, p95), numerical error against exact analytical
oracles, code footprint (.text, assembly instructions), and peak RSS across:
  1. Mechanics Lab (Mass-Spring-Damper, RK4, 2000 steps)
  2. Materials & Diffusion Lab (1D FTCS Heat Equation, N=101, 500 steps)
  3. Bio Reaction Kinetics (First-order A -> B, RK4, 2000 steps + mass conservation)
  4. Biomechanics 1-DOF Viscoelastic Joint (RK4, 1000 steps)
  5. Structural 1D FEM 2-Element Bar (2x2 linear solve)
"""

from __future__ import annotations

import ctypes
import json
import math
import platform
import resource
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

S3_BENCHMARKS_DIR = Path(__file__).resolve().parents[2]
S3_REPO_DIR = S3_BENCHMARKS_DIR.parent / "S3"
for p in (str(S3_REPO_DIR), str(S3_REPO_DIR / "bootstrap")):
    if p not in sys.path:
        sys.path.insert(0, p)

from bootstrap.s3.backends.x86_64 import InstructionBudgetMode, NativeToolchain, X8664Backend
from bootstrap.s3.optimizer import OptimizationLevel
from bootstrap.s3.pipeline import compile_sources

WARMUPS = 3
SAMPLES = 9


def _git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "UNKNOWN"


def _stats(samples_ns: list[float]) -> dict[str, float]:
    ordered = sorted(samples_ns)
    p95_idx = min(len(ordered) - 1, int(0.95 * (len(ordered) - 1)))
    return {
        "samples": len(ordered),
        "median_ns": statistics.median(ordered),
        "mean_ns": statistics.mean(ordered),
        "min_ns": ordered[0],
        "max_ns": ordered[-1],
        "p95_ns": ordered[p95_idx],
        "iqr_ns": (statistics.quantiles(ordered, n=4)[2] - statistics.quantiles(ordered, n=4)[0])
        if len(ordered) >= 4
        else (ordered[-1] - ordered[0]),
    }


def _compile_v3_so(filename: str, opt: OptimizationLevel, mode: InstructionBudgetMode, tmp: Path) -> tuple[Path, dict[str, Any]]:
    v3_dir = S3_REPO_DIR / "examples" / "horizons_v3"
    sources = {
        "s3_sci_core.s3": (v3_dir / "s3_sci_core.s3").read_text(encoding="utf-8"),
        filename: (v3_dir / filename).read_text(encoding="utf-8"),
    }
    comp = compile_sources(sources, entry_module=filename.removesuffix(".s3"), optimization=opt)
    _, asm = comp.require_ordinary_artifacts()
    s3_insts = sum(len(b.instructions) for fn in asm.functions for b in fn.blocks)
    s3_blocks = sum(len(fn.blocks) for fn in asm.functions)
    asm_text = X8664Backend(
        max_instructions=500_000_000,
        register_allocation=True,
        instruction_budget_mode=mode,
    )._generate_ffi(asm)
    tag = f"{filename.removesuffix('.s3')}_{opt.value}_{mode.value}"
    s_path = tmp / f"{tag}.s"
    so_path = tmp / f"{tag}.so"
    s_path.write_text(asm_text, encoding="utf-8")
    subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)], check=True)
    text_bytes = 0
    try:
        out = subprocess.check_output(["objdump", "-h", str(so_path)], text=True)
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[1] == ".text":
                text_bytes = int(parts[2], 16)
    except Exception:
        pass
    return so_path, {
        "s3_asm_instructions": s3_insts,
        "s3_asm_blocks": s3_blocks,
        "text_bytes": text_bytes,
    }


def _bench_fn(call_fn) -> dict[str, float]:
    for _ in range(WARMUPS):
        call_fn()
    samples: list[float] = []
    for _ in range(SAMPLES):
        t0 = time.perf_counter_ns()
        call_fn()
        t1 = time.perf_counter_ns()
        samples.append(float(t1 - t0))
    return _stats(samples)


def main() -> None:
    NativeToolchain.detect()
    D_PTR = ctypes.POINTER(ctypes.c_double)
    profiles = [
        (OptimizationLevel.O0, InstructionBudgetMode.PER_INSTRUCTION, "s3_o0_per_instruction"),
        (OptimizationLevel.O1, InstructionBudgetMode.PER_INSTRUCTION, "s3_o1_per_instruction"),
        (OptimizationLevel.O1, InstructionBudgetMode.EXACT_SEGMENT, "s3_o1_exact_segment"),
    ]

    results: dict[str, Any] = {
        "campaign": "S3_SCIENTIFIC_HORIZONS_V3",
        "environment": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "s3_sha": _git_sha(S3_REPO_DIR),
        "benchmarks_sha": _git_sha(S3_BENCHMARKS_DIR),
        "experiments": {},
    }

    with tempfile.TemporaryDirectory(prefix="s3_v3_bench_", dir="/tmp") as td:
        tmp = Path(td)

        # 1. Mechanics Lab (2000 steps, dt=0.001, t=2.0, m=1, c=0, k=4)
        mech_out: dict[str, Any] = {}
        x_exact = math.cos(4.0)
        for opt, mode, label in profiles:
            so, meta = _compile_v3_so("s3_mechanics_lab.s3", opt, mode, tmp)
            lib = ctypes.CDLL(str(so))
            fn = lib.__s3mod_s3_mechanics_lab__ffi_simulate_oscillator
            fn.argtypes = [ctypes.c_double] * 7 + [ctypes.c_int64, D_PTR, ctypes.c_int64]
            fn.restype = ctypes.c_int64
            buf = (ctypes.c_double * 6)()

            def run_m():
                assert fn(1.0, 0.0, 1.0, 0.0, 4.0, 0.0, 0.001, 2000, buf, 6) == 0

            st = _bench_fn(run_m)
            err_x = abs(buf[0] - x_exact)
            err_e = abs(buf[5] - 2.0)
            mech_out[label] = {
                **st,
                **meta,
                "x_final": buf[0],
                "total_energy": buf[5],
                "abs_error_x": err_x,
                "abs_error_energy": err_e,
                "parity_pass": err_x < 1e-10 and err_e < 1e-10,
            }
        results["experiments"]["mechanics_lab_2000steps"] = mech_out

        # 2. Materials & Diffusion Lab (N=101, 500 steps, dx=0.01, dt=0.0004, alpha=0.05 -> r=0.2)
        diff_out: dict[str, Any] = {}
        n_g = 101
        dx = 1.0 / (n_g - 1)
        alpha = 0.05
        dt = 0.0004
        steps_d = 500
        t_fin = dt * steps_d
        init_t = [math.sin(math.pi * i * dx) for i in range(n_g)]
        exact_t = [math.sin(math.pi * i * dx) * math.exp(-alpha * (math.pi ** 2) * t_fin) for i in range(n_g)]
        for opt, mode, label in profiles:
            so, meta = _compile_v3_so("s3_materials_diffusion.s3", opt, mode, tmp)
            lib = ctypes.CDLL(str(so))
            fn = lib.__s3mod_s3_materials_diffusion__diffuse_1d_ftcs
            fn.argtypes = [D_PTR, ctypes.c_int64, D_PTR, ctypes.c_int64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int64]
            fn.restype = ctypes.c_int64
            cur = (ctypes.c_double * n_g)()
            nxt = (ctypes.c_double * n_g)()

            def run_d():
                for idx in range(n_g):
                    cur[idx] = init_t[idx]
                assert fn(cur, n_g, nxt, n_g, alpha, dt, dx, steps_d) == 0

            st = _bench_fn(run_d)
            max_err = max(abs(cur[i] - exact_t[i]) for i in range(n_g))
            diff_out[label] = {
                **st,
                **meta,
                "max_abs_error": max_err,
                "cfl_r": alpha * dt / (dx * dx),
                "parity_pass": max_err < 1e-4,
            }
        results["experiments"]["materials_diffusion_101x500"] = diff_out

        # 3. Bio Reaction Kinetics (2000 steps, dt=0.001, k=0.5)
        bio_out: dict[str, Any] = {}
        a_ex = 10.0 * math.exp(-1.0)
        for opt, mode, label in profiles:
            so, meta = _compile_v3_so("s3_bio_reaction_kinetics.s3", opt, mode, tmp)
            lib = ctypes.CDLL(str(so))
            fn = lib.__s3mod_s3_bio_reaction_kinetics__ffi_reaction_a_to_b
            fn.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int64, D_PTR, ctypes.c_int64]
            fn.restype = ctypes.c_int64
            ab = (ctypes.c_double * 3)()

            def run_b():
                assert fn(10.0, 2.0, 0.5, 0.001, 2000, ab, 3) == 0

            st = _bench_fn(run_b)
            err_a = abs(ab[0] - a_ex)
            err_mass = abs(ab[2] - 12.0)
            bio_out[label] = {
                **st,
                **meta,
                "abs_error_a": err_a,
                "mass_conservation_error": err_mass,
                "parity_pass": err_a < 1e-11 and err_mass < 1e-12,
            }
        results["experiments"]["bio_reaction_kinetics_2000steps"] = bio_out

        # 4. Biomechanics Joint (1000 steps)
        joint_out: dict[str, Any] = {}
        for opt, mode, label in profiles:
            so, meta = _compile_v3_so("s3_biomechanics_joint.s3", opt, mode, tmp)
            lib = ctypes.CDLL(str(so))
            fn = lib.__s3mod_s3_biomechanics_joint__ffi_simulate_joint
            fn.argtypes = [ctypes.c_double] * 7 + [ctypes.c_int64, D_PTR, ctypes.c_int64]
            fn.restype = ctypes.c_int64
            jo = (ctypes.c_double * 2)()

            def run_j():
                assert fn(0.0, 0.0, 0.05, 0.2, 5.0, 1.0, 0.002, 1000, jo, 2) == 0

            st = _bench_fn(run_j)
            joint_out[label] = {**st, **meta, "theta_final": jo[0], "parity_pass": abs(jo[0] - 0.2) < 5e-3}
        results["experiments"]["biomechanics_joint_1000steps"] = joint_out

        # 5. Structural 1D FEM 2-Element Bar
        fem_out: dict[str, Any] = {}
        for opt, mode, label in profiles:
            so, meta = _compile_v3_so("s3_fem_1d_bar.s3", opt, mode, tmp)
            lib = ctypes.CDLL(str(so))
            fn = lib.__s3mod_s3_fem_1d_bar__ffi_solve_bar_2elem
            fn.argtypes = [ctypes.c_double] * 6 + [D_PTR, ctypes.c_int64]
            fn.restype = ctypes.c_int64
            uo = (ctypes.c_double * 2)()

            def run_f():
                assert fn(1000.0, 1.0, 1000.0, 1.0, 0.0, 100.0, uo, 2) == 0

            st = _bench_fn(run_f)
            fem_out[label] = {
                **st,
                **meta,
                "u1": uo[0],
                "u2": uo[1],
                "max_abs_error": max(abs(uo[0] - 0.1), abs(uo[1] - 0.2)),
                "parity_pass": max(abs(uo[0] - 0.1), abs(uo[1] - 0.2)) < 1e-12,
            }
        results["experiments"]["fem_1d_bar_2elem"] = fem_out

    results["peak_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out_path = Path(__file__).resolve().parent / "results_v3.json"
    out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Wrote {out_path} (peak_rss_kib={results['peak_rss_kib']})")


if __name__ == "__main__":
    main()
