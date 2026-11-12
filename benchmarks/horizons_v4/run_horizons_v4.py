#!/usr/bin/env python3
"""S3 Scientific Horizons V4 — S3 vs C (gcc -O2/-O3) Benchmarks & Bottleneck Study.

Separates HOST_PYTHON_RSS_KIB from NATIVE_PROGRAM_RSS_KIB (via standalone native_runner).
Evaluates S3 O0 PER_INSTRUCTION, S3 O1 PER_INSTRUCTION, S3 O1 EXACT_SEGMENT,
S3 O1 LOOP_HYBRID, C gcc -O2, and C gcc -O3 on:
  1. Materials Diffusion 1D (N=101, 500 steps): FTCS & Crank-Nicolson
  2. Mechanics 2-DOF Coupled Oscillator (2000 steps): Velocity Verlet
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

HERE = Path(__file__).resolve().parent
S3_BENCHMARKS_DIR = HERE.parents[1]
S3_REPO_DIR = S3_BENCHMARKS_DIR.parent / "S3"
for p in (str(S3_REPO_DIR), str(S3_REPO_DIR / "bootstrap")):
    if p not in sys.path:
        sys.path.insert(0, p)

from bootstrap.s3.backends.x86_64 import InstructionBudgetMode, NativeToolchain, X8664Backend
from bootstrap.s3.optimizer import OptimizationLevel
from bootstrap.s3.pipeline import compile_sources

WARMUPS = 2
SAMPLES = 7
D_PTR = ctypes.POINTER(ctypes.c_double)


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
    }


def _text_and_file_bytes(so_path: Path) -> tuple[int, int]:
    text_bytes = 0
    try:
        out = subprocess.check_output(["objdump", "-h", str(so_path)], text=True)
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[1] == ".text":
                text_bytes = int(parts[2], 16)
    except Exception:
        pass
    return text_bytes, so_path.stat().st_size


def _compile_s3(filename: str, module: str, opt: OptimizationLevel, mode: InstructionBudgetMode, tmp: Path) -> tuple[Path, dict[str, Any]]:
    core = S3_REPO_DIR / "examples" / "horizons_v3" / "s3_sci_core.s3"
    app = S3_REPO_DIR / "examples" / "horizons_v4" / filename
    t0 = time.perf_counter()
    comp = compile_sources({"s3_sci_core.s3": core.read_text(encoding="utf-8"), filename: app.read_text(encoding="utf-8")}, entry_module=module, optimization=opt)
    _, asm = comp.require_ordinary_artifacts()
    asm_text = X8664Backend(max_instructions=500_000_000, register_allocation=True, instruction_budget_mode=mode)._generate_ffi(asm)
    tag = f"{module}_{opt.value}_{mode.value}"
    s_path = tmp / f"{tag}.s"
    so_path = tmp / f"{tag}.so"
    s_path.write_text(asm_text, encoding="utf-8")
    subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)], check=True)
    compile_ms = (time.perf_counter() - t0) * 1000.0
    text_b, file_b = _text_and_file_bytes(so_path)
    return so_path, {
        "compile_ms": compile_ms,
        "s3_asm_instructions": sum(len(b.instructions) for fn in asm.functions for b in fn.blocks),
        "text_bytes": text_b,
        "artifact_bytes": file_b,
    }


def _compile_c(opt_flag: str, tmp: Path) -> tuple[Path, dict[str, Any]]:
    t0 = time.perf_counter()
    so_path = tmp / f"c_oracles_{opt_flag.strip('-')}.so"
    subprocess.run(["gcc", "-shared", "-fPIC", opt_flag, str(HERE / "c_oracles.c"), "-lm", "-o", str(so_path)], check=True)
    compile_ms = (time.perf_counter() - t0) * 1000.0
    text_b, file_b = _text_and_file_bytes(so_path)
    return so_path, {"compile_ms": compile_ms, "text_bytes": text_b, "artifact_bytes": file_b}


def _bench_fn(fn) -> dict[str, float]:
    for _ in range(WARMUPS):
        fn()
    samples = []
    for _ in range(SAMPLES):
        t0 = time.perf_counter_ns()
        fn()
        t1 = time.perf_counter_ns()
        samples.append(float(t1 - t0))
    return _stats(samples)


def main() -> None:
    NativeToolchain.detect()
    s3_profiles = [
        (OptimizationLevel.O0, InstructionBudgetMode.PER_INSTRUCTION, "s3_o0_per_instruction"),
        (OptimizationLevel.O1, InstructionBudgetMode.PER_INSTRUCTION, "s3_o1_per_instruction"),
        (OptimizationLevel.O1, InstructionBudgetMode.EXACT_SEGMENT, "s3_o1_exact_segment"),
        (OptimizationLevel.O1, InstructionBudgetMode.LOOP_HYBRID, "s3_o1_loop_hybrid"),
    ]
    results: dict[str, Any] = {
        "campaign": "S3_SCIENTIFIC_HORIZONS_V4_REAL_EXPANSION",
        "environment": {"platform": platform.platform(), "machine": platform.machine(), "python": platform.python_version()},
        "s3_sha": _git_sha(S3_REPO_DIR),
        "benchmarks_sha": _git_sha(S3_BENCHMARKS_DIR),
        "experiments": {"diffusion_101x500_ftcs": {}, "diffusion_101x500_crank_nicolson": {}, "mechanics_2dof_verlet_2000": {}},
    }

    with tempfile.TemporaryDirectory(prefix="s3_v4_bench_", dir="/tmp") as td:
        tmp = Path(td)
        runner_bin = tmp / "native_runner"
        subprocess.run(["gcc", "-O2", str(HERE / "native_runner.c"), "-ldl", "-lm", "-o", str(runner_bin)], check=True)

        n_g, steps_d, alpha, dt_d = 101, 500, 0.05, 0.0004
        dx = 1.0 / (n_g - 1)
        t_fin = dt_d * steps_d
        init_t = [math.sin(math.pi * i * dx) for i in range(n_g)]
        exact_t = [math.sin(math.pi * i * dx) * math.exp(-alpha * (math.pi ** 2) * t_fin) for i in range(n_g)]

        def _measure_s3_diff(so_path: Path, meta: dict[str, Any], method_code: int) -> dict[str, Any]:
            t_load0 = time.perf_counter()
            lib = ctypes.CDLL(str(so_path))
            load_ms = (time.perf_counter() - t_load0) * 1000.0
            fn = lib.__s3mod_s3_materials_v2__diffuse_1d_v2
            fn.argtypes = [D_PTR, ctypes.c_int64] * 10 + [ctypes.c_int64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int64, ctypes.c_int64]
            fn.restype = ctypes.c_int64
            cur = (ctypes.c_double * n_g)()
            nxt = (ctypes.c_double * n_g)()
            a = (ctypes.c_double * n_g)(); b = (ctypes.c_double * n_g)(); c = (ctypes.c_double * n_g)(); d = (ctypes.c_double * n_g)()
            cp = (ctypes.c_double * n_g)(); dp = (ctypes.c_double * n_g)(); sol = (ctypes.c_double * n_g)()
            cser = (ctypes.c_double * (steps_d + 1))()

            def call():
                for i in range(n_g):
                    cur[i] = init_t[i]
                assert fn(cur, n_g, nxt, n_g, a, n_g, b, n_g, c, n_g, d, n_g, cp, n_g, dp, n_g, sol, n_g, cser, steps_d + 1, n_g, alpha, dt_d, dx, 0.0, 0.0, steps_d, method_code) == 0

            st = _bench_fn(call)
            max_err = max(abs(cur[i] - exact_t[i]) for i in range(n_g))
            rss_out = subprocess.check_output([str(runner_bin), "s3_diff", str(so_path), "__s3mod_s3_materials_v2__diffuse_1d_v2"], text=True).strip()
            return {**st, **meta, "load_ms": load_ms, "max_abs_error": max_err, "native_program_rss_kib": int(rss_out), "parity_pass": max_err < 1e-4}

        for opt, mode, label in s3_profiles:
            so_d, meta_d = _compile_s3("s3_materials_v2.s3", "s3_materials_v2", opt, mode, tmp)
            results["experiments"]["diffusion_101x500_ftcs"][label] = _measure_s3_diff(so_d, meta_d, 0)
            results["experiments"]["diffusion_101x500_crank_nicolson"][label] = _measure_s3_diff(so_d, meta_d, 1)

            so_m, meta_m = _compile_s3("s3_mechanics_v2.s3", "s3_mechanics_v2", opt, mode, tmp)
            t_load0 = time.perf_counter()
            lib_m = ctypes.CDLL(str(so_m))
            load_ms = (time.perf_counter() - t_load0) * 1000.0
            fn_m = lib_m.__s3mod_s3_mechanics_v2__simulate_2dof_timeseries
            fn_m.argtypes = [ctypes.c_double] * 14 + [ctypes.c_int64, ctypes.c_int64] + [D_PTR, ctypes.c_int64] * 6
            fn_m.restype = ctypes.c_int64
            sm = 2000; nm = sm + 1
            t_a = (ctypes.c_double * nm)(); x1_a = (ctypes.c_double * nm)(); v1_a = (ctypes.c_double * nm)()
            x2_a = (ctypes.c_double * nm)(); v2_a = (ctypes.c_double * nm)(); e_a = (ctypes.c_double * nm)()

            def call_m():
                assert fn_m(1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 2.0, 1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.005, sm, 1, t_a, nm, x1_a, nm, v1_a, nm, x2_a, nm, v2_a, nm, e_a, nm) == 0

            st_m = _bench_fn(call_m)
            e_drift = max(abs(e_a[i] - e_a[0]) for i in range(nm))
            results["experiments"]["mechanics_2dof_verlet_2000"][label] = {**st_m, **meta_m, "load_ms": load_ms, "final_x1": x1_a[sm], "max_energy_drift": e_drift, "parity_pass": e_drift < 1e-4}

        for opt_flag, clabel in (("-O2", "c_gcc_o2"), ("-O3", "c_gcc_o3")):
            so_c, meta_c = _compile_c(opt_flag, tmp)
            lib_c = ctypes.CDLL(str(so_c))
            fn_cf = lib_c.c_diffuse_1d_ftcs
            fn_cf.argtypes = [D_PTR, D_PTR, ctypes.c_int64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int64]
            fn_cf.restype = ctypes.c_int64
            cur = (ctypes.c_double * n_g)(); nxt = (ctypes.c_double * n_g)()

            def call_cf():
                for i in range(n_g): cur[i] = init_t[i]
                assert fn_cf(cur, nxt, n_g, alpha, dt_d, dx, 0.0, 0.0, steps_d) == 0

            st_cf = _bench_fn(call_cf)
            rss_c = int(subprocess.check_output([str(runner_bin), "c_ftcs", str(so_c), "c_diffuse_1d_ftcs"], text=True).strip())
            results["experiments"]["diffusion_101x500_ftcs"][clabel] = {**st_cf, **meta_c, "max_abs_error": max(abs(cur[i] - exact_t[i]) for i in range(n_g)), "native_program_rss_kib": rss_c, "parity_pass": True}

            fn_cc = lib_c.c_diffuse_1d_crank_nicolson
            fn_cc.argtypes = [D_PTR] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int64]
            fn_cc.restype = ctypes.c_int64
            a = (ctypes.c_double * n_g)(); b = (ctypes.c_double * n_g)(); c = (ctypes.c_double * n_g)(); d = (ctypes.c_double * n_g)()
            cp = (ctypes.c_double * n_g)(); dp = (ctypes.c_double * n_g)(); sol = (ctypes.c_double * n_g)()

            def call_cc():
                for i in range(n_g): cur[i] = init_t[i]
                assert fn_cc(cur, a, b, c, d, cp, dp, sol, n_g, alpha, dt_d, dx, 0.0, 0.0, steps_d) == 0

            st_cc = _bench_fn(call_cc)
            results["experiments"]["diffusion_101x500_crank_nicolson"][clabel] = {**st_cc, **meta_c, "max_abs_error": max(abs(cur[i] - exact_t[i]) for i in range(n_g)), "native_program_rss_kib": rss_c, "parity_pass": True}

            fn_cm = lib_c.c_mechanics_2dof_verlet
            fn_cm.argtypes = [ctypes.c_double] * 10 + [ctypes.c_int64] + [D_PTR] * 5
            fn_cm.restype = ctypes.c_int64
            sm = 2000; nm = sm + 1
            x1_a = (ctypes.c_double * nm)(); v1_a = (ctypes.c_double * nm)(); x2_a = (ctypes.c_double * nm)(); v2_a = (ctypes.c_double * nm)(); e_a = (ctypes.c_double * nm)()

            def call_cm():
                assert fn_cm(1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 2.0, 1.0, 2.0, 0.005, sm, x1_a, v1_a, x2_a, v2_a, e_a) == 0

            st_cm = _bench_fn(call_cm)
            e_drift_c = max(abs(e_a[i] - e_a[0]) for i in range(nm))
            results["experiments"]["mechanics_2dof_verlet_2000"][clabel] = {**st_cm, **meta_c, "final_x1": x1_a[sm], "max_energy_drift": e_drift_c, "native_program_rss_kib": rss_c, "parity_pass": True}

    results["host_python_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    out_path = HERE / "results_v4.json"
    out_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (host_python_rss_kib={results['host_python_rss_kib']})")


if __name__ == "__main__":
    main()
