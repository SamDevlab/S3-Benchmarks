#!/usr/bin/env python3
"""Fair, work-equivalent S3-vs-C High Performance Benchmark Suite (V1)."""

from __future__ import annotations

import argparse
import ctypes
import json
import math
import os
import resource
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Callable

HERE = Path(__file__).resolve().parent
S3_ROOT = HERE.parents[1].parent / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.backends.x86_64 import InstructionBudgetMode, X8664Backend
from bootstrap.s3.pipeline import OptimizationLevel, compile_source


def _text_bytes(so_path: Path) -> int:
    out = subprocess.run(["size", str(so_path)], capture_output=True, text=True, check=True).stdout
    return int(out.splitlines()[1].split()[0])


def _measure_child_rss_kib(so_path: Path, is_s3: bool) -> int:
    """Measure isolated child process max RSS loading and calling dot_i64 in the .so."""
    sym = "dot_i64"
    code = (
        "import ctypes, resource\n"
        f"lib = ctypes.CDLL({str(so_path)!r})\n"
        f"fn = getattr(lib, {sym!r})\n"
        "fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, "
        "ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64]\n"
        "fn.restype = ctypes.c_int64\n"
        "a = (ctypes.c_int64 * 1024)(*range(1024))\n"
        "b = (ctypes.c_int64 * 1024)(*([1]*1024))\n"
        "fn(a, 1024, b, 1024, 1024)\n"
        "print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)\n"
    )
    res = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    return int(res.stdout.strip().splitlines()[-1])


def _stats(samples_s: list[float]) -> dict[str, float]:
    ms = sorted(s * 1000.0 for s in samples_s)
    n = len(ms)
    med = statistics.median(ms)
    q1 = ms[n // 4]
    q3 = ms[(3 * n) // 4]
    iqr = q3 - q1
    mean = statistics.mean(ms)
    sd = statistics.stdev(ms) if n > 1 else 0.0
    half_ci = 1.96 * sd / math.sqrt(n) if n > 1 else 0.0
    return {
        "median_ms": med,
        "iqr_ms": iqr,
        "mean_ms": mean,
        "ci95_low_ms": max(0.0, mean - half_ci),
        "ci95_high_ms": mean + half_ci,
        "min_ms": ms[0],
        "max_ms": ms[-1],
    }


def compile_variants(build_dir: Path) -> dict[str, dict[str, Any]]:
    build_dir.mkdir(parents=True, exist_ok=True)
    c_src = HERE / "kernels.c"
    s3_src = (HERE / "kernels.s3").read_text(encoding="utf-8")
    variants: dict[str, dict[str, Any]] = {}

    for name, flags in [
        ("c_O2", ["-O2"]),
        ("c_O3", ["-O3"]),
        ("c_O2_checked", ["-O2", "-DWITH_CHECKS"]),
    ]:
        so_path = build_dir / f"{name}.so"
        t0 = time.perf_counter()
        subprocess.run(["gcc", *flags, "-shared", "-fPIC", str(c_src), "-lm", "-o", str(so_path)], check=True)
        assemble_s = time.perf_counter() - t0
        variants[name] = {
            "so_path": so_path,
            "is_s3": False,
            "compile_s": 0.0,
            "assemble_s": assemble_s,
            "text_bytes": _text_bytes(so_path),
            "native_program_rss_kib": _measure_child_rss_kib(so_path, is_s3=False),
        }

    s3_configs = [
        ("s3_O0_per_inst", OptimizationLevel.O0, False, InstructionBudgetMode.PER_INSTRUCTION),
        ("s3_O1_per_inst", OptimizationLevel.O1, True, InstructionBudgetMode.PER_INSTRUCTION),
        ("s3_O1_exact_seg", OptimizationLevel.O1, True, InstructionBudgetMode.EXACT_SEGMENT),
        ("s3_O1_loop_hyb", OptimizationLevel.O1, True, InstructionBudgetMode.LOOP_HYBRID),
    ]
    compiled_cache: dict[OptimizationLevel, tuple[Any, float]] = {}
    for opt in (OptimizationLevel.O0, OptimizationLevel.O1):
        t0 = time.perf_counter()
        comp = compile_source(s3_src, opt)
        compiled_cache[opt] = (comp, time.perf_counter() - t0)

    for name, opt, regalloc, mode in s3_configs:
        comp, compile_s = compiled_cache[opt]
        _, ap = comp.require_ordinary_artifacts()
        t_emit = time.perf_counter()
        asm_text = X8664Backend(
            max_instructions=200_000_000,
            register_allocation=regalloc,
            instruction_budget_mode=mode,
        )._generate_ffi(ap)
        s_path = build_dir / f"{name}.s"
        so_path = build_dir / f"{name}.so"
        s_path.write_text(asm_text, encoding="utf-8")
        subprocess.run(["gcc", "-shared", "-nostdlib", "-Wl,--build-id=none", str(s_path), "-o", str(so_path)], check=True)
        assemble_s = time.perf_counter() - t_emit
        variants[name] = {
            "so_path": so_path,
            "is_s3": True,
            "compile_s": compile_s,
            "assemble_s": assemble_s,
            "text_bytes": _text_bytes(so_path),
            "native_program_rss_kib": _measure_child_rss_kib(so_path, is_s3=True),
        }

    return variants


def _bind(lib: ctypes.CDLL, is_s3: bool) -> dict[str, Any]:
    pfx = ""
    d_ptr = ctypes.POINTER(ctypes.c_double)
    i_ptr = ctypes.POINTER(ctypes.c_int64)

    dot = getattr(lib, pfx + "dot_i64")
    dot.argtypes = [i_ptr, ctypes.c_int64, i_ptr, ctypes.c_int64, ctypes.c_int64]
    dot.restype = ctypes.c_int64

    axpy = getattr(lib, pfx + "axpy_f64")
    axpy.argtypes = [ctypes.c_double, d_ptr, ctypes.c_int64, d_ptr, ctypes.c_int64, ctypes.c_int64]
    axpy.restype = ctypes.c_int64

    s1d = getattr(lib, pfx + "stencil_1d_f64")
    s1d.argtypes = [d_ptr, ctypes.c_int64, d_ptr, ctypes.c_int64, d_ptr, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_double]
    s1d.restype = ctypes.c_int64

    s2d = getattr(lib, pfx + "stencil_2d_f64")
    s2d.argtypes = [d_ptr, ctypes.c_int64, d_ptr, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_double]
    s2d.restype = ctypes.c_int64

    mm = getattr(lib, pfx + "matmul_f64")
    mm.argtypes = [d_ptr, ctypes.c_int64, d_ptr, ctypes.c_int64, d_ptr, ctypes.c_int64, ctypes.c_int64]
    mm.restype = ctypes.c_int64

    th = getattr(lib, pfx + "thomas_f64")
    th.argtypes = [d_ptr, ctypes.c_int64] * 7 + [ctypes.c_int64]
    th.restype = ctypes.c_int64

    rk4 = getattr(lib, pfx + "rk4_osc_f64")
    rk4.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int64]
    rk4.restype = ctypes.c_double

    ver = getattr(lib, pfx + "verlet_osc_f64")
    ver.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int64]
    ver.restype = ctypes.c_double

    return {"dot": dot, "axpy": axpy, "s1d": s1d, "s2d": s2d, "mm": mm, "th": th, "rk4": rk4, "ver": ver}


def make_workloads(fns: dict[str, Any]) -> dict[str, Callable[[], float]]:
    # Pre-allocated buffers reused across calls (exact same memory footprint)
    n_vec = 50_000
    a_i = (ctypes.c_int64 * n_vec)(*[(i % 17) - 8 for i in range(n_vec)])
    b_i = (ctypes.c_int64 * n_vec)(*[(i % 13) + 1 for i in range(n_vec)])

    x_f = (ctypes.c_double * n_vec)(*[math.sin(0.001 * i) for i in range(n_vec)])
    y_f = (ctypes.c_double * n_vec)(*[1.0 for _ in range(n_vec)])

    n_1d = 4_096
    u_1d = (ctypes.c_double * n_1d)(*[math.sin(math.pi * i / (n_1d - 1)) for i in range(n_1d)])
    a_1d = (ctypes.c_double * n_1d)()
    b_1d = (ctypes.c_double * n_1d)()

    rows_2d, cols_2d = 64, 64
    n_2d = rows_2d * cols_2d
    a_2d = (ctypes.c_double * n_2d)(*[1.0 if (i % cols_2d == 0 or i // cols_2d == 0) else 0.0 for i in range(n_2d)])
    b_2d = (ctypes.c_double * n_2d)(*a_2d)

    n_mm = 48
    m_a = (ctypes.c_double * (n_mm * n_mm))(*[((i * 7 + 3) % 11) * 0.1 for i in range(n_mm * n_mm)])
    m_b = (ctypes.c_double * (n_mm * n_mm))(*[((i * 5 + 1) % 13) * 0.1 for i in range(n_mm * n_mm)])
    m_c = (ctypes.c_double * (n_mm * n_mm))()

    n_th = 2_048
    th_a = (ctypes.c_double * n_th)(*[-1.0 for _ in range(n_th)])
    th_b = (ctypes.c_double * n_th)(*[4.0 for _ in range(n_th)])
    th_c = (ctypes.c_double * n_th)(*[-1.0 for _ in range(n_th)])
    th_d = (ctypes.c_double * n_th)(*[1.0 for _ in range(n_th)])
    th_cp = (ctypes.c_double * n_th)()
    th_dp = (ctypes.c_double * n_th)()
    th_x = (ctypes.c_double * n_th)()

    def run_dot() -> float:
        return float(fns["dot"](a_i, n_vec, b_i, n_vec, n_vec))

    def run_axpy() -> float:
        y_f[0] = 1.0
        y_f[n_vec - 1] = 1.0
        fns["axpy"](0.25, x_f, n_vec, y_f, n_vec, n_vec)
        return float(y_f[1234])

    def run_s1d() -> float:
        fns["s1d"](u_1d, n_1d, a_1d, n_1d, b_1d, n_1d, n_1d, 50, 0.2)
        return float(a_1d[n_1d // 2])

    def run_s2d() -> float:
        for i in range(n_2d):
            a_2d[i] = 1.0 if (i % cols_2d == 0 or i // cols_2d == 0) else 0.0
            b_2d[i] = a_2d[i]
        fns["s2d"](a_2d, n_2d, b_2d, n_2d, rows_2d, cols_2d, 20, 0.1)
        return float(a_2d[32 * cols_2d + 32])

    def run_mm() -> float:
        fns["mm"](m_a, n_mm * n_mm, m_b, n_mm * n_mm, m_c, n_mm * n_mm, n_mm)
        return float(m_c[0] + m_c[n_mm * n_mm - 1])

    def run_th() -> float:
        fns["th"](th_a, n_th, th_b, n_th, th_c, n_th, th_d, n_th, th_cp, n_th, th_dp, n_th, th_x, n_th, n_th)
        return float(th_x[n_th // 2])

    def run_rk4() -> float:
        return float(fns["rk4"](1.0, 0.0, 4.0, 0.001, 10_000))

    def run_ver() -> float:
        return float(fns["ver"](1.0, 0.0, 4.0, 0.001, 10_000))

    return {
        "dot_i64_50k": run_dot,
        "axpy_f64_50k": run_axpy,
        "stencil_1d_4096x50": run_s1d,
        "stencil_2d_64x64x20": run_s2d,
        "matmul_f64_48": run_mm,
        "thomas_f64_2048": run_th,
        "rk4_osc_10k": run_rk4,
        "verlet_osc_10k": run_ver,
    }


def run_suite(trials: int = 15, warmups: int = 3, out_path: Path | None = None) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="s3_hp_v1_") as td:
        variants = compile_variants(Path(td))
        bound: dict[str, dict[str, Callable[[], float]]] = {}
        for vname, info in variants.items():
            lib = ctypes.CDLL(str(info["so_path"]))
            bound[vname] = make_workloads(_bind(lib, info["is_s3"]))

        kernel_names = list(next(iter(bound.values())).keys())
        variant_names = list(variants.keys())
        timings: dict[str, dict[str, list[float]]] = {k: {v: [] for v in variant_names} for k in kernel_names}
        outputs: dict[str, dict[str, float]] = {k: {} for k in kernel_names}

        for k in kernel_names:
            for _ in range(warmups):
                for v in variant_names:
                    bound[v][k]()
            for t in range(trials):
                order = variant_names if t % 2 == 0 else list(reversed(variant_names))
                for v in order:
                    t0 = time.perf_counter()
                    val = bound[v][k]()
                    dt = time.perf_counter() - t0
                    timings[k][v].append(dt)
                    outputs[k][v] = val

        summary: dict[str, Any] = {
            "meta": {
                "trials": trials,
                "warmups": warmups,
                "pmu_status": "PMU_UNAVAILABLE",
                "host_python_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                "variants": {
                    v: {
                        "compile_s": info["compile_s"],
                        "assemble_s": info["assemble_s"],
                        "text_bytes": info["text_bytes"],
                        "native_program_rss_kib": info["native_program_rss_kib"],
                    }
                    for v, info in variants.items()
                },
            },
            "kernels": {},
        }

        for k in kernel_names:
            ref_val = outputs[k]["c_O2"]
            c_o2_med = _stats(timings[k]["c_O2"])["median_ms"]
            c_chk_med = _stats(timings[k]["c_O2_checked"])["median_ms"]
            k_res: dict[str, Any] = {}
            for v in variant_names:
                st = _stats(timings[k][v])
                diff = abs(outputs[k][v] - ref_val)
                st["parity_abs_diff"] = diff
                st["ratio_vs_c_O2"] = st["median_ms"] / c_o2_med if c_o2_med > 0 else 0.0
                st["ratio_vs_c_O2_checked"] = st["median_ms"] / c_chk_med if c_chk_med > 0 else 0.0
                k_res[v] = st
            summary["kernels"][k] = k_res

        if out_path:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        return summary


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--trials", type=int, default=15)
    p.add_argument("--warmups", type=int, default=3)
    p.add_argument("--out", default=str(HERE / "results_baseline.json"))
    args = p.parse_args()
    res = run_suite(trials=args.trials, warmups=args.warmups, out_path=Path(args.out))
    print(f"Host Python RSS (KiB): {res['meta']['host_python_rss_kib']}")
    for v, m in res["meta"]["variants"].items():
        print(f"Variant {v:16s}: .text={m['text_bytes']:6d}B compile={m['compile_s']:.3f}s asm={m['assemble_s']:.3f}s child_rss={m['native_program_rss_kib']}KiB")
    print("\n--- Median ms (ratio vs c_O2 | ratio vs c_O2_checked) ---")
    for k, kv in res["kernels"].items():
        parts = [f"{v}={kv[v]['median_ms']:.3f}ms({kv[v]['ratio_vs_c_O2']:.2f}x)" for v in ("c_O2", "c_O3", "c_O2_checked", "s3_O0_per_inst", "s3_O1_per_inst", "s3_O1_exact_seg", "s3_O1_loop_hyb")]
        max_diff = max(kv[v]["parity_abs_diff"] for v in kv)
        print(f"{k:20s} | max_diff={max_diff:.2e} | " + " | ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
