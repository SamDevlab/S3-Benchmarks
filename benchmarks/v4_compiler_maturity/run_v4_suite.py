"""Reproducible Benchmark Suite for S3 V4 Native Compiler Maturity & Mathematical Optimization.

Measures 6 non-overlapping execution categories with cold compile vs warm cache latency,
amortization break-even, exact numerical/bit parity, and strict negative controls:
  1. S3_CONVENTIONAL_NATIVE       (x86-64 compiled S3 without predictive_exact, 50M budget)
  2. S3_PREDICTIVE_NATIVE         (x86-64 compiled S3 with predictive_exact=True, AVX2/FMA, or S3 GF(2) native)
  3. S3_PREDICTIVE_PYTHON_WRAPPER (Python predictive APIs, Hashlife V3/V4, SCEV, compiler-explain)
  4. C11_CONVENTIONAL_GCC_O3      (GCC -O3 C11 iterative reference loops & CSR CG-Jacobi)
  5. C11_PREDICTIVE_GCC_O3        (GCC -O3 C11 GF(2)[x]/(x^W-1) circulant kernel & closed-form refs)
  6. NEGATIVE_CONTROL             (Strict defaults, small-T cutoffs, overflow trap parity, Hashlife abort, tamper & SCEV rejections)
"""

from __future__ import annotations

import csv
import ctypes
import json
import math
import platform
import random
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from array import array
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
S3_ROOT = BENCH_ROOT.parent / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.backends.x86_64.backend import SCIENTIFIC_MAX_INSTRUCTIONS, X8664Backend, generate_ffi_assembly
from bootstrap.s3.backends.x86_64.simd_features import detect_cpu_features
from bootstrap.s3.backends.x86_64.toolchain import NativeToolchain
from bootstrap.s3.compiler_explain import explain_compilation
from bootstrap.s3.ir_emulator import IRExecutionError, execute_ir
from bootstrap.s3.numeric import NumericError
from bootstrap.s3.optimizer import OptimizationLevel
from bootstrap.s3.pipeline import CompilationCache, compile_source, compile_sources
from bootstrap.s3.predictive_compute_v2 import predictive_execute, predictive_verify
from bootstrap.s3.predictive_gf2 import (
    GF2LinearCACache,
    run_gf2_ca,
    verify_gf2_circulant_and_extract_poly,
)
from bootstrap.s3.predictive_gf2_s3 import get_s3_gf2_library
from bootstrap.s3.predictive_hashlife_v2 import run_hashlife_v2_finite_grid, run_hashlife_v3_finite_grid
from bootstrap.s3.predictive_native import get_native_predictive_library
from bootstrap.s3.predictive_native_lowering import PredictiveLoweringCache, apply_predictive_native_lowering
from bootstrap.s3.predictive_proof_checker import PredictiveVerificationCache, verify_translation_certificate
from bootstrap.s3.predictive_scev import analyze_scev_module, verify_scev_against_ir
from bootstrap.s3.predictive_verifier import CorrectnessClass
from tools.numerics_oracle_v4_7 import GCC_CSR_JACOBI_C, build_poisson2d

_C11_V4_REF = r"""
#include <math.h>
#include <stdint.h>

int64_t c11_lcg_mod(int64_t n, int64_t x0, int64_t m) {
    if (m <= 0) return x0;
    __int128 x = x0;
    for (int64_t i = 0; i < n; ++i) {
        x = (3 * x + 5) % m;
    }
    return (int64_t)x;
}

int64_t c11_tribonacci_mod(int64_t n, int64_t m) {
    if (m <= 0) return 0;
    int64_t a = 0, b = 1, c = 1;
    for (int64_t i = 0; i < n; ++i) {
        int64_t na = b;
        int64_t nb = c;
        int64_t nc = (a + b + c) % m;
        a = na; b = nb; c = nc;
    }
    return a;
}

int64_t c11_tetranacci_mod(int64_t n, int64_t m) {
    if (m <= 0) return 0;
    int64_t a = 0, b = 0, c = 1, d = 1;
    for (int64_t i = 0; i < n; ++i) {
        int64_t nxt = (a + b + c + d) % m;
        a = b; b = c; c = d; d = nxt;
    }
    return a;
}

int64_t c11_lcg_dyn_shifted(int64_t n, int64_t x0, int64_t a, int64_t b, int64_t m) {
    if (m <= 0) return x0;
    __int128 x = x0;
    for (int64_t i = 0; i < n; ++i) {
        x = (a * x + b) % m;
    }
    return (int64_t)x;
}

double c11_dot_f64(const double *a, const double *b, int64_t n) {
    double acc = 0.0;
    for (int64_t i = 0; i < n; ++i) {
        acc += a[i] * b[i];
    }
    return acc;
}

double c11_vec_scale_add(const double *x, const double *y, double *out, double alpha, int64_t n) {
    for (int64_t i = 0; i < n; ++i) {
        out[i] = alpha * x[i] + y[i];
    }
    return out[0];
}
"""

_IR_V4_SRC = """
export fn lcg_mod(n: i64, x0: i64, m: i64) -> i64:
    mut i: i64 = 0
    mut x: i64 = x0
    while i < n:
        nxt: i64 = 3 * x + 5
        q: i64 = nxt / m
        x = nxt - q * m
        i = i + 1
    return x

export fn fib_mod(n: i64, m: i64) -> i64:
    mut a: i64 = 0
    mut b: i64 = 1
    mut i: i64 = 0
    while i < n:
        s: i64 = a + b
        q: i64 = s / m
        nb: i64 = s - q * m
        a = b
        b = nb
        i = i + 1
    return a

export fn tribonacci_mod(n: i64, m: i64) -> i64:
    mut a: i64 = 0
    mut b: i64 = 1
    mut c: i64 = 1
    mut i: i64 = 0
    while i < n:
        s: i64 = a + b + c
        q: i64 = s / m
        nc: i64 = s - q * m
        a = b
        b = c
        c = nc
        i = i + 1
    return a

export fn tetranacci_mod(n: i64, m: i64) -> i64:
    mut a: i64 = 0
    mut b: i64 = 0
    mut c: i64 = 1
    mut d: i64 = 1
    mut i: i64 = 0
    while i < n:
        s: i64 = a + b + c + d
        q: i64 = s / m
        nd: i64 = s - q * m
        a = b
        b = c
        c = d
        d = nd
        i = i + 1
    return a

export fn lcg_dyn_shifted(n: i64, x0: i64, a: i64, b: i64, m: i64) -> i64:
    mut i: i64 = 2
    mut x: i64 = x0
    while i < n:
        nxt: i64 = a * x + b
        q: i64 = nxt / m
        x = nxt - q * m
        i = i + 1
    return x

export fn sum_mod_ind(n: i64, m: i64) -> i64:
    mut s: i64 = 0
    mut i: i64 = 0
    while i < n:
        nxt: i64 = s + i
        q: i64 = nxt / m
        s = nxt - q * m
        i = i + 1
    return s

export fn main() -> i64:
    return lcg_mod(10, 7, 1000000007)
"""

_SIMD_KERNEL_SRC = """
export fn dot_product(a: &[f64], b: &[f64]) -> f64:
    n: i64 = len(a)
    mut acc: f64 = 0.0
    mut i: i64 = 0
    while i < n:
        acc = acc + a[i] * b[i]
        i = i + 1
    return acc

export fn vec_scale_add(x: &[f64], y: &[f64], out: &mut [f64], alpha: f64) -> f64:
    n: i64 = len(x)
    mut i: i64 = 0
    while i < n:
        out[i] = alpha * x[i] + y[i]
        i = i + 1
    return out[0]

export fn main() -> i64:
    return 0
"""

_NEG_STATIC_SRC = """
export fn sum_small() -> i64:
    mut s: i64 = 0
    mut i: i64 = 0
    while i < 10:
        s = s + i
        i = i + 1
    return s

export fn fib(n: i64) -> i64:
    mut a: i64 = 0
    mut b: i64 = 1
    mut i: i64 = 0
    while i < n:
        nb: i64 = a + b
        a = b
        b = nb
        i = i + 1
    return a

export fn fp_loop(n: i64, x0: i64) -> f64:
    mut s: f64 = 0.0
    mut i: i64 = 0
    while i < n:
        s = s + 1.5
        i = i + 1
    return s

export fn nonlinear_quad(n: i64, x0: i64) -> i64:
    mut x: i64 = x0
    mut i: i64 = 0
    while i < n:
        x = x * x + 1
        i = i + 1
    return x

export fn main() -> i64:
    return sum_small()
"""

_SCEV_BENCH_SRC = """
export fn helper(v: i64) -> i64:
    return v + 3

export fn poly_acc(n: i64) -> i64:
    mut acc: i64 = 5
    mut i: i64 = 0
    while i < n:
        acc = acc + i * i + 2 * i + 1
        i = i + 1
    return acc

export fn triangular_cubic(n: i64) -> i64:
    mut s1: i64 = 0
    mut s2: i64 = 0
    mut i: i64 = 0
    while i < n:
        s1 = s1 + i * i
        s2 = s2 + s1
        i = i + 1
    return s2

export fn neg_impure(n: i64) -> i64:
    mut s: i64 = 0
    mut i: i64 = 0
    while i < n:
        s = s + helper(i)
        i = i + 1
    return s

export fn neg_exponential(n: i64) -> i64:
    mut s: i64 = 1
    mut i: i64 = 0
    while i < n:
        s = s * 2
        i = i + 1
    return s

export fn main() -> i64:
    return poly_acc(10) + triangular_cubic(10)
"""


def _git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(repo), text=True).strip()
    except Exception:
        return "UNKNOWN"


def _time_fn(fn, *args, repeats: int = 7, warmups: int = 1) -> tuple[Any, float, float, float]:
    t0 = time.perf_counter_ns()
    val = fn(*args)
    cold_ms = (time.perf_counter_ns() - t0) / 1e6
    for _ in range(max(0, warmups - 1)):
        fn(*args)
    samples_ms: list[float] = []
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        val = fn(*args)
        samples_ms.append((time.perf_counter_ns() - t0) / 1e6)
    samples_ms.sort()
    q1 = samples_ms[len(samples_ms) // 4]
    q3 = samples_ms[(3 * len(samples_ms)) // 4]
    return val, round(cold_ms, 5), round(statistics.median(samples_ms), 5), round(q3 - q1, 5)


def _rec(
    records: list[dict[str, Any]],
    *,
    suite: str,
    case: str,
    category: str,
    horizon: int,
    cold_ms: float | None,
    warm_median_ms: float | None,
    warm_iqr_ms: float | None = None,
    compile_cold_ms: float | None = None,
    exact_match: bool = True,
    accelerated: bool = False,
    soundness_class: str = "",
    speedup_vs_s3_conv_native: float | None = None,
    speedup_vs_c11_conv_gcc_o3: float | None = None,
    notes: str = "",
    extra: dict[str, Any] | None = None,
) -> None:
    row: dict[str, Any] = {
        "suite": suite,
        "case": case,
        "category": category,
        "horizon": horizon,
        "cold_ms": cold_ms,
        "warm_median_ms": warm_median_ms,
        "warm_iqr_ms": warm_iqr_ms,
        "compile_cold_ms": compile_cold_ms,
        "speedup_warm_vs_cold": (
            round(cold_ms / warm_median_ms, 2)
            if (cold_ms and warm_median_ms and warm_median_ms > 0)
            else None
        ),
        "exact_match": exact_match,
        "accelerated": accelerated,
        "soundness_class": soundness_class,
        "speedup_vs_s3_conv_native": speedup_vs_s3_conv_native,
        "speedup_vs_c11_conv_gcc_o3": speedup_vs_c11_conv_gcc_o3,
        "notes": notes,
    }
    if extra:
        row["extra"] = extra
    records.append(row)


def _build_s3_so(asm_prog: Any, tmp_dir: Path, name: str, *, max_instructions: int | None = SCIENTIFIC_MAX_INSTRUCTIONS) -> tuple[ctypes.CDLL, float]:
    t0 = time.perf_counter_ns()
    if max_instructions is None:
        asm_text = generate_ffi_assembly(asm_prog)
    else:
        backend = X8664Backend.scientific(max_instructions=max_instructions)
        asm_text = backend._generate_ffi(asm_prog)
    s_path = tmp_dir / f"{name}.s"
    so_path = tmp_dir / f"lib{name}.so"
    s_path.write_text(asm_text, encoding="utf-8")
    gcc = shutil.which("gcc") or "gcc"
    subprocess.run([gcc, "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)], check=True)
    link_ms = (time.perf_counter_ns() - t0) / 1e6
    return ctypes.CDLL(str(so_path)), round(link_ms, 3)


def _step_periodic_eca(state: list[int], rule: int) -> list[int]:
    w = len(state)
    return [
        (rule >> (((state[(i - 1) % w] & 1) << 2) | ((state[i] & 1) << 1) | (state[(i + 1) % w] & 1))) & 1
        for i in range(w)
    ]


def _make_tiled_glider_grid(width: int, height: int) -> array:
    grid = array("q", [0] * (width * height))
    glider = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for br in range(8, height - 8, 16):
        for bc in range(8, width - 8, 16):
            for dr, dc in glider:
                grid[(br + dr) * width + (bc + dc)] = 1
    return grid


def _make_rpentomino_grid(width: int, height: int) -> array:
    grid = array("q", [0] * (width * height))
    cr, cc = height // 2, width // 2
    for dr, dc in [(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)]:
        grid[(cr + dr) * width + (cc + dc)] = 1
    return grid


def run_v4_suite() -> dict[str, Any]:
    NativeToolchain.detect()
    records: list[dict[str, Any]] = []
    gcc = shutil.which("gcc") or "gcc"
    I_PTR = ctypes.POINTER(ctypes.c_int64)
    D_PTR = ctypes.POINTER(ctypes.c_double)

    with tempfile.TemporaryDirectory(prefix="s3_v4_suite_") as tmp:
        tmp_dir = Path(tmp)

        # Compile GCC -O3 reference C11 library
        c_ref_path = tmp_dir / "v4_ref.c"
        so_ref_path = tmp_dir / "libv4_ref.so"
        c_ref_path.write_text(_C11_V4_REF, encoding="utf-8")
        subprocess.run([gcc, "-O3", "-std=c11", "-shared", "-fPIC", str(c_ref_path), "-o", str(so_ref_path)], check=True)
        cref = ctypes.CDLL(str(so_ref_path))
        cref.c11_lcg_mod.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
        cref.c11_lcg_mod.restype = ctypes.c_int64
        cref.c11_tribonacci_mod.argtypes = [ctypes.c_int64, ctypes.c_int64]
        cref.c11_tribonacci_mod.restype = ctypes.c_int64
        cref.c11_tetranacci_mod.argtypes = [ctypes.c_int64, ctypes.c_int64]
        cref.c11_tetranacci_mod.restype = ctypes.c_int64
        cref.c11_lcg_dyn_shifted.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
        cref.c11_lcg_dyn_shifted.restype = ctypes.c_int64
        cref.c11_dot_f64.argtypes = [D_PTR, D_PTR, ctypes.c_int64]
        cref.c11_dot_f64.restype = ctypes.c_double
        cref.c11_vec_scale_add.argtypes = [D_PTR, D_PTR, D_PTR, ctypes.c_double, ctypes.c_int64]
        cref.c11_vec_scale_add.restype = ctypes.c_double

        # Compile GCC -O3 CSR CG-Jacobi reference
        c_csr_path = tmp_dir / "gcc_csr.c"
        so_csr_path = tmp_dir / "libgcc_csr.so"
        c_csr_path.write_text(GCC_CSR_JACOBI_C, encoding="utf-8")
        subprocess.run([gcc, "-O3", "-shared", "-fPIC", str(c_csr_path), "-o", str(so_csr_path)], check=True)
        gcsr = ctypes.CDLL(str(so_csr_path))
        gcsr_fn = gcsr.gcc_cg_solve_csr_jacobi
        gcsr_fn.argtypes = [I_PTR, I_PTR] + [D_PTR] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64, D_PTR]
        gcsr_fn.restype = ctypes.c_int64

        # =====================================================================
        # 1. Compilation Latency, Cold/Warm Cache & Amortization Break-Even
        # =====================================================================
        mem_cache = CompilationCache()
        t0 = time.perf_counter_ns()
        comp_conv = mem_cache.compile(_IR_V4_SRC, optimization=OptimizationLevel.O1, predictive_exact=False)
        conv_compile_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)

        t0 = time.perf_counter_ns()
        comp_pred = mem_cache.compile(_IR_V4_SRC, optimization=OptimizationLevel.O1, predictive_exact=True)
        pred_cold_compile_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)

        _, mem_warm_cold, mem_warm_med, mem_warm_iqr = _time_fn(
            lambda: mem_cache.compile(_IR_V4_SRC, optimization=OptimizationLevel.O1, predictive_exact=True),
            repeats=7,
            warmups=1,
        )

        # Disk-backed PredictiveVerificationCache + PredictiveLoweringCache cold vs warm
        ver_cache = PredictiveVerificationCache(disk_dir=tmp_dir / "ver_cache")
        low_cache = PredictiveLoweringCache(disk_dir=tmp_dir / "low_cache")
        t0 = time.perf_counter_ns()
        low_cold = apply_predictive_native_lowering(
            comp_conv.ir,
            source_text=_IR_V4_SRC,
            verification_cache=ver_cache,
            cache=low_cache,
        )
        disk_cold_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)

        # Warm disk reload with fresh in-memory cache objects sharing disk_dir
        ver_disk = PredictiveVerificationCache(disk_dir=tmp_dir / "ver_cache")
        low_disk = PredictiveLoweringCache(disk_dir=tmp_dir / "low_cache")
        t0 = time.perf_counter_ns()
        low_warm_disk = apply_predictive_native_lowering(
            comp_conv.ir,
            source_text=_IR_V4_SRC,
            verification_cache=ver_disk,
            cache=low_disk,
        )
        disk_warm_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)

        _, inmem_low_cold, inmem_low_med, inmem_low_iqr = _time_fn(
            lambda: apply_predictive_native_lowering(
                comp_conv.ir,
                source_text=_IR_V4_SRC,
                verification_cache=ver_cache,
                cache=low_cache,
            ),
            repeats=5,
            warmups=1,
        )

        _rec(
            records,
            suite="compile_cache",
            case="compile_o1_conventional_6fn_cold",
            category="S3_CONVENTIONAL_NATIVE",
            horizon=6,
            cold_ms=conv_compile_ms,
            warm_median_ms=conv_compile_ms,
            compile_cold_ms=conv_compile_ms,
            exact_match=True,
            accelerated=False,
            soundness_class="CONVENTIONAL_COMPILE",
        )
        _rec(
            records,
            suite="compile_cache",
            case="compile_o1_predictive_exact_6fn_cold",
            category="S3_PREDICTIVE_NATIVE",
            horizon=6,
            cold_ms=pred_cold_compile_ms,
            warm_median_ms=mem_warm_med,
            warm_iqr_ms=mem_warm_iqr,
            compile_cold_ms=pred_cold_compile_ms,
            exact_match=(len(comp_pred.predictive_lowered_functions) == 6),
            accelerated=True,
            soundness_class="STATIC_PRECONDITIONS_VERIFIED",
            notes=f"warm_mem_compile_ms={mem_warm_med}; conv_compile_ms={conv_compile_ms}",
        )
        _rec(
            records,
            suite="compile_cache",
            case="predictive_lowering_disk_cache_cold_vs_warm",
            category="S3_PREDICTIVE_PYTHON_WRAPPER",
            horizon=6,
            cold_ms=disk_cold_ms,
            warm_median_ms=disk_warm_ms,
            compile_cold_ms=disk_cold_ms,
            exact_match=(
                tuple(low_warm_disk.lowered_functions) == tuple(low_cold.lowered_functions)
                and len(low_warm_disk.lowered_functions) == 6
            ),
            accelerated=True,
            soundness_class="SHA256_DISK_CACHE_VERIFIED",
            notes=f"inmem_cache_warm_ms={inmem_low_med} (iqr={inmem_low_iqr}); disk_warm_ms={disk_warm_ms}",
        )

        # Build native shared libraries for _IR_V4_SRC
        lib_conv, conv_link_ms = _build_s3_so(comp_conv.assembly, tmp_dir, "v4_conv")
        lib_pred, pred_link_ms = _build_s3_so(comp_pred.assembly, tmp_dir, "v4_pred")

        for lib in (lib_conv, lib_pred):
            lib.lcg_mod.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
            lib.lcg_mod.restype = ctypes.c_int64
            lib.tribonacci_mod.argtypes = [ctypes.c_int64, ctypes.c_int64]
            lib.tribonacci_mod.restype = ctypes.c_int64
            lib.tetranacci_mod.argtypes = [ctypes.c_int64, ctypes.c_int64]
            lib.tetranacci_mod.restype = ctypes.c_int64
            lib.lcg_dyn_shifted.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
            lib.lcg_dyn_shifted.restype = ctypes.c_int64
            lib.sum_mod_ind.argtypes = [ctypes.c_int64, ctypes.c_int64]
            lib.sum_mod_ind.restype = ctypes.c_int64

        # =====================================================================
        # 2. MathOptIR Generalized Native Lowering & Amortization (up to T=10^12)
        # =====================================================================
        MOD = 1_000_000_007
        for T in (10, 1_000, 1_000_000, 1_000_000_000, 1_000_000_000_000):
            pv, pc_cold, pc_med, pc_iqr = _time_fn(lib_pred.lcg_mod, T, 7, MOD)
            if T <= 1_000_000:
                cv, cc_cold, cc_med, cc_iqr = _time_fn(lib_conv.lcg_mod, T, 7, MOD)
                gv, gc_cold, gc_med, gc_iqr = _time_fn(cref.c11_lcg_mod, T, 7, MOD)
                py_res = predictive_execute(_IR_V4_SRC, function_name="lcg_mod", arguments=[T, 7, MOD])
                _, pw_cold, pw_med, pw_iqr = _time_fn(
                    lambda: predictive_execute(_IR_V4_SRC, function_name="lcg_mod", arguments=[T, 7, MOD]),
                    repeats=3,
                    warmups=1,
                ) if T >= 1000 else (py_res, 0.0, 0.0, 0.0)
                match_all = (pv == cv == gv == py_res.final_state)
                sp_s3 = round(cc_med / pc_med, 2) if pc_med > 0 else None
                sp_gcc = round(gc_med / pc_med, 2) if pc_med > 0 else None
                amort_calls = (
                    math.ceil((pred_cold_compile_ms - conv_compile_ms) / max(1e-9, cc_med - pc_med))
                    if T >= 1000 and cc_med > pc_med
                    else None
                )
                _rec(
                    records, suite="ir_native_v4", case=f"lcg_mod_T{T}", category="S3_CONVENTIONAL_NATIVE",
                    horizon=T, cold_ms=cc_cold, warm_median_ms=cc_med, warm_iqr_ms=cc_iqr,
                    compile_cold_ms=round(conv_compile_ms + conv_link_ms, 3), exact_match=(cv == gv),
                    accelerated=False, soundness_class="CONVENTIONAL_EXACT",
                )
                _rec(
                    records, suite="ir_native_v4", case=f"lcg_mod_T{T}", category="C11_CONVENTIONAL_GCC_O3",
                    horizon=T, cold_ms=gc_cold, warm_median_ms=gc_med, warm_iqr_ms=gc_iqr,
                    exact_match=True, accelerated=False, soundness_class="GCC_O3_REF",
                )
                _rec(
                    records, suite="ir_native_v4", case=f"lcg_mod_T{T}",
                    category=("NEGATIVE_CONTROL" if T == 10 else "S3_PREDICTIVE_NATIVE"),
                    horizon=T, cold_ms=pc_cold, warm_median_ms=pc_med, warm_iqr_ms=pc_iqr,
                    compile_cold_ms=round(pred_cold_compile_ms + pred_link_ms, 3),
                    exact_match=match_all, accelerated=(T > 10),
                    soundness_class=("USE_CONVENTIONAL_SMALL_T" if T == 10 else "STATIC_PRECONDITIONS_VERIFIED"),
                    speedup_vs_s3_conv_native=sp_s3, speedup_vs_c11_conv_gcc_o3=sp_gcc,
                    notes=(f"amortization_calls={amort_calls}" if amort_calls else "runtime_small_t_bypass"),
                )
                if T >= 1000:
                    _rec(
                        records, suite="ir_native_v4", case=f"lcg_mod_T{T}", category="S3_PREDICTIVE_PYTHON_WRAPPER",
                        horizon=T, cold_ms=pw_cold, warm_median_ms=pw_med, warm_iqr_ms=pw_iqr,
                        exact_match=(py_res.final_state == gv), accelerated=True,
                        soundness_class="STATIC_PRECONDITIONS_VERIFIED",
                    )
            else:
                # Verify T=10^9 and T=10^12 against predictive_execute closed form
                py_res = predictive_execute(_IR_V4_SRC, function_name="lcg_mod", arguments=[T, 7, MOD])
                _rec(
                    records, suite="ir_native_v4", case=f"lcg_mod_T{T}", category="S3_PREDICTIVE_NATIVE",
                    horizon=T, cold_ms=pc_cold, warm_median_ms=pc_med, warm_iqr_ms=pc_iqr,
                    compile_cold_ms=round(pred_cold_compile_ms + pred_link_ms, 3),
                    exact_match=(pv == py_res.final_state), accelerated=True,
                    soundness_class="STATIC_PRECONDITIONS_VERIFIED",
                    notes=f"value={pv}; O(log T) binary exp verified against Python closed form",
                )

        # New V4 KxK matrix, 5-param shifted LCG, and unreduced-induction modular loops
        v4_ir_cases = [
            ("tribonacci_mod_k3_T100k", lib_pred.tribonacci_mod, lib_conv.tribonacci_mod, cref.c11_tribonacci_mod, (100_000, MOD), 100_000),
            ("tetranacci_mod_k4_T100k", lib_pred.tetranacci_mod, lib_conv.tetranacci_mod, cref.c11_tetranacci_mod, (100_000, MOD), 100_000),
            ("lcg_dyn_shifted_5param_T1M", lib_pred.lcg_dyn_shifted, lib_conv.lcg_dyn_shifted, None, (1_000_002, 13, 11, 7, MOD), 1_000_000),
            ("sum_mod_ind_T100k", lib_pred.sum_mod_ind, lib_conv.sum_mod_ind, None, (100_000, MOD), 100_000),
        ]
        for cname, pfn, cfn, gfn_ref, args, h in v4_ir_cases:
            pv, pc_cold, pc_med, pc_iqr = _time_fn(pfn, *args)
            cv, cc_cold, cc_med, cc_iqr = _time_fn(cfn, *args)
            if gfn_ref is not None:
                gv, gc_cold, gc_med, gc_iqr = _time_fn(gfn_ref, *args)
            else:
                gv, gc_cold, gc_med, gc_iqr = cref.c11_lcg_dyn_shifted(1_000_000, 13, 11, 7, MOD) if "dyn" in cname else cv, 0.0, None, None
            match_ok = (pv == cv) and (gfn_ref is None or pv == gv) and ("dyn" not in cname or pv == gv)
            if gfn_ref is not None:
                _rec(
                    records, suite="ir_native_v4", case=cname, category="C11_CONVENTIONAL_GCC_O3",
                    horizon=h, cold_ms=gc_cold, warm_median_ms=gc_med, warm_iqr_ms=gc_iqr,
                    exact_match=True, accelerated=False, soundness_class="GCC_O3_REF",
                )
            _rec(
                records, suite="ir_native_v4", case=cname, category="S3_CONVENTIONAL_NATIVE",
                horizon=h, cold_ms=cc_cold, warm_median_ms=cc_med, warm_iqr_ms=cc_iqr,
                exact_match=(not gfn_ref or cv == gv), accelerated=False, soundness_class="CONVENTIONAL_EXACT",
            )
            _rec(
                records, suite="ir_native_v4", case=cname, category="S3_PREDICTIVE_NATIVE",
                horizon=h, cold_ms=pc_cold, warm_median_ms=pc_med, warm_iqr_ms=pc_iqr,
                exact_match=match_ok, accelerated=True, soundness_class="STATIC_PRECONDITIONS_VERIFIED",
                speedup_vs_s3_conv_native=round(cc_med / pc_med, 2) if pc_med > 0 else None,
                speedup_vs_c11_conv_gcc_o3=round(gc_med / pc_med, 2) if (gc_med and pc_med > 0) else None,
            )

        # Verify T=10^12 on k=3 Tribonacci
        pv_t12, t12_cold, t12_med, t12_iqr = _time_fn(lib_pred.tribonacci_mod, 1_000_000_000_000, MOD)
        py_t12 = predictive_execute(_IR_V4_SRC, function_name="tribonacci_mod", arguments=[1_000_000_000_000, MOD])
        _rec(
            records, suite="ir_native_v4", case="tribonacci_mod_k3_T1e12", category="S3_PREDICTIVE_NATIVE",
            horizon=1_000_000_000_000, cold_ms=t12_cold, warm_median_ms=t12_med, warm_iqr_ms=t12_iqr,
            exact_match=(pv_t12 == py_t12.final_state), accelerated=True, soundness_class="STATIC_PRECONDITIONS_VERIFIED",
            notes=f"value={pv_t12}",
        )

        # =====================================================================
        # 3. Compiler-Emitted AVX2/FMA & Poisson 2D CSR (32x32..128x128 inside 50M)
        # =====================================================================
        t0 = time.perf_counter_ns()
        comp_simd_strict = compile_source(_SIMD_KERNEL_SRC, optimization=OptimizationLevel.O1, allow_fp_reassociation=False)
        simd_strict_compile_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)
        lib_simd_strict, simd_strict_link_ms = _build_s3_so(comp_simd_strict.assembly, tmp_dir, "simd_strict")

        t0 = time.perf_counter_ns()
        comp_simd_fma = compile_source(_SIMD_KERNEL_SRC, optimization=OptimizationLevel.O1, allow_fp_reassociation=True)
        lib_simd_fma, _ = _build_s3_so(comp_simd_fma.assembly, tmp_dir, "simd_fma")

        for lib in (lib_simd_strict, lib_simd_fma):
            lib.dot_product.argtypes = [D_PTR, ctypes.c_int64, D_PTR, ctypes.c_int64]
            lib.dot_product.restype = ctypes.c_double
            lib.vec_scale_add.argtypes = [D_PTR, ctypes.c_int64, D_PTR, ctypes.c_int64, D_PTR, ctypes.c_int64, ctypes.c_double]
            lib.vec_scale_add.restype = ctypes.c_double

        n_vec = 16384
        rng_fp = random.Random(20261114)
        a_arr = (ctypes.c_double * n_vec)(*[rng_fp.uniform(-1.0, 1.0) for _ in range(n_vec)])
        b_arr = (ctypes.c_double * n_vec)(*[rng_fp.uniform(-1.0, 1.0) for _ in range(n_vec)])
        out_s3 = (ctypes.c_double * n_vec)()
        out_c = (ctypes.c_double * n_vec)()

        sv, sc_cold, sc_med, sc_iqr = _time_fn(lib_simd_strict.vec_scale_add, a_arr, n_vec, b_arr, n_vec, out_s3, n_vec, 2.5, repeats=15)
        gv_vec, gc_cold, gc_med, gc_iqr = _time_fn(cref.c11_vec_scale_add, a_arr, b_arr, out_c, 2.5, n_vec, repeats=15)
        vec_err = max(abs(out_s3[i] - out_c[i]) for i in range(n_vec))
        _rec(
            records, suite="simd_avx2_compiler", case="vec_scale_add_N16384_gcc_o3", category="C11_CONVENTIONAL_GCC_O3",
            horizon=n_vec, cold_ms=gc_cold, warm_median_ms=gc_med, warm_iqr_ms=gc_iqr,
            exact_match=True, accelerated=False, soundness_class="GCC_O3_REF",
        )
        _rec(
            records, suite="simd_avx2_compiler", case="vec_scale_add_N16384_s3_avx2_strict", category="S3_CONVENTIONAL_NATIVE",
            horizon=n_vec, cold_ms=sc_cold, warm_median_ms=sc_med, warm_iqr_ms=sc_iqr,
            compile_cold_ms=round(simd_strict_compile_ms + simd_strict_link_ms, 3),
            exact_match=(vec_err == 0.0), accelerated=False, soundness_class="BIT_EXACT_IEEE754_AVX2",
            speedup_vs_c11_conv_gcc_o3=round(gc_med / sc_med, 2) if sc_med > 0 else None,
            notes=f"compiler-emitted F64X4 vaddpd/vmulpd, max_err={vec_err}",
        )

        # dot_product strict vs opt-in FMA vs GCC -O3
        g_dot, gd_cold, gd_med, gd_iqr = _time_fn(cref.c11_dot_f64, a_arr, b_arr, n_vec, repeats=15)
        s_dot, sd_cold, sd_med, sd_iqr = _time_fn(lib_simd_strict.dot_product, a_arr, n_vec, b_arr, n_vec, repeats=15)
        f_dot, fd_cold, fd_med, fd_iqr = _time_fn(lib_simd_fma.dot_product, a_arr, n_vec, b_arr, n_vec, repeats=15)
        _rec(
            records, suite="simd_avx2_compiler", case="dot_f64_N16384_gcc_o3", category="C11_CONVENTIONAL_GCC_O3",
            horizon=n_vec, cold_ms=gd_cold, warm_median_ms=gd_med, warm_iqr_ms=gd_iqr,
            exact_match=True, accelerated=False, soundness_class="GCC_O3_STRICT_FP",
        )
        _rec(
            records, suite="simd_avx2_compiler", case="dot_f64_N16384_s3_strict_fp", category="S3_CONVENTIONAL_NATIVE",
            horizon=n_vec, cold_ms=sd_cold, warm_median_ms=sd_med, warm_iqr_ms=sd_iqr,
            exact_match=(s_dot == g_dot), accelerated=False, soundness_class="STRICT_IEEE754_0ULP",
            speedup_vs_c11_conv_gcc_o3=round(gd_med / sd_med, 2) if sd_med > 0 else None,
        )
        _rec(
            records, suite="simd_avx2_compiler", case="dot_f64_N16384_s3_optin_avx2_fma", category="S3_PREDICTIVE_NATIVE",
            horizon=n_vec, cold_ms=fd_cold, warm_median_ms=fd_med, warm_iqr_ms=fd_iqr,
            exact_match=(abs(f_dot - g_dot) < 1e-9), accelerated=True, soundness_class="OPT_IN_FP_REASSOC_AVX2_FMA",
            speedup_vs_s3_conv_native=round(sd_med / fd_med, 2) if fd_med > 0 else None,
            speedup_vs_c11_conv_gcc_o3=round(gd_med / fd_med, 2) if fd_med > 0 else None,
            notes=f"abs_err={abs(f_dot - g_dot):.3e}",
        )

        # Poisson 2D CSR CG-Jacobi across 32x32..128x128
        core_src = (S3_ROOT / "examples" / "horizons_v3" / "s3_sci_core.s3").read_text(encoding="utf-8")
        app_src = (S3_ROOT / "examples" / "horizons_v4" / "s3_sci_numerics_v5.s3").read_text(encoding="utf-8")
        sig_poi = [I_PTR, ctypes.c_int64] * 2 + [D_PTR, ctypes.c_int64] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64, D_PTR, ctypes.c_int64]

        t0 = time.perf_counter_ns()
        comp_poi_strict = compile_sources(
            {"s3_sci_core.s3": core_src, "s3_sci_numerics_v5.s3": app_src},
            entry_module="s3_sci_numerics_v5",
            optimization=OptimizationLevel.O1,
            allow_fp_reassociation=False,
        )
        poi_strict_compile_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)
        lib_poi_strict, poi_strict_link_ms = _build_s3_so(comp_poi_strict.assembly, tmp_dir, "poi_strict")
        comp_poi_fma = compile_sources(
            {"s3_sci_core.s3": core_src, "s3_sci_numerics_v5.s3": app_src},
            entry_module="s3_sci_numerics_v5",
            optimization=OptimizationLevel.O1,
            allow_fp_reassociation=True,
        )
        lib_poi_fma, _ = _build_s3_so(comp_poi_fma.assembly, tmp_dir, "poi_fma")

        for lpoi in (lib_poi_strict, lib_poi_fma):
            cf = getattr(lpoi, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi_chunk")
            cf.argtypes = sig_poi
            cf.restype = ctypes.c_int64

        strict_cf = getattr(lib_poi_strict, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi_chunk")
        fma_cf = getattr(lib_poi_fma, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi_chunk")

        for grid, chunk_step in ((32, 100), (48, 50), (64, 50), (96, 25), (128, 20)):
            n = grid * grid
            rp_l, ci_l, vl_l, b_l, _ = build_poisson2d(grid)
            rp = (ctypes.c_int64 * len(rp_l))(*rp_l)
            ci = (ctypes.c_int64 * len(ci_l))(*ci_l)
            vl = (ctypes.c_double * len(vl_l))(*vl_l)
            dg = (ctypes.c_double * n)(*([4.0] * n))
            b = (ctypes.c_double * n)(*b_l)
            gx, gr, gz, gp, gap = [(ctypes.c_double * n)() for _ in range(5)]
            gout = (ctypes.c_double * 1)()

            def run_gcc_p():
                return gcsr_fn(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, 1e-10, 5000, gout)

            def run_s3_p(cf):
                sx, sr, sz, sp, sap = [(ctypes.c_double * n)() for _ in range(5)]
                st = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
                sit = 0
                while sit < 5000 and st[3] < 0.5:
                    rc = cf(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, 1e-20, min(chunk_step, 5000 - sit), st, 4)
                    if rc < 0:
                        return -1, sx
                    sit += rc
                return sit, sx

            rep_p = 3 if grid <= 64 else 2
            giters, g_cold, g_med, g_iqr = _time_fn(run_gcc_p, repeats=rep_p, warmups=1)
            (siters_s, sx_s), s_cold, s_med, s_iqr = _time_fn(run_s3_p, strict_cf, repeats=rep_p, warmups=1)
            (siters_f, sx_f), f_cold, f_med, f_iqr = _time_fn(run_s3_p, fma_cf, repeats=rep_p, warmups=1)
            err_s = max(abs(sx_s[i] - gx[i]) for i in range(n))
            err_f = max(abs(sx_f[i] - gx[i]) for i in range(n))

            _rec(
                records, suite="poisson2d_v4_csr", case=f"poisson_{grid}x{grid}_gcc_o3", category="C11_CONVENTIONAL_GCC_O3",
                horizon=n, cold_ms=g_cold, warm_median_ms=g_med, warm_iqr_ms=g_iqr,
                exact_match=True, accelerated=False, soundness_class="GCC_O3_STRICT_FP", notes=f"iters={giters}",
            )
            _rec(
                records, suite="poisson2d_v4_csr", case=f"poisson_{grid}x{grid}_s3_avx2_strict", category="S3_CONVENTIONAL_NATIVE",
                horizon=n, cold_ms=s_cold, warm_median_ms=s_med, warm_iqr_ms=s_iqr,
                compile_cold_ms=round(poi_strict_compile_ms + poi_strict_link_ms, 3),
                exact_match=(siters_s == giters and err_s == 0.0), accelerated=False,
                soundness_class="STRICT_IEEE754_50M_BUDGET",
                speedup_vs_c11_conv_gcc_o3=round(g_med / s_med, 3) if s_med > 0 else None,
                notes=f"iters={siters_s}, max_err={err_s:.1e}, ratio_vs_gcc={round(s_med/g_med, 2)}x",
            )
            _rec(
                records, suite="poisson2d_v4_csr", case=f"poisson_{grid}x{grid}_s3_optin_fma", category="S3_PREDICTIVE_NATIVE",
                horizon=n, cold_ms=f_cold, warm_median_ms=f_med, warm_iqr_ms=f_iqr,
                exact_match=(siters_f == giters and err_f < 1e-10), accelerated=True,
                soundness_class="OPT_IN_FP_REASSOC_50M_BUDGET",
                speedup_vs_s3_conv_native=round(s_med / f_med, 3) if f_med > 0 else None,
                speedup_vs_c11_conv_gcc_o3=round(g_med / f_med, 3) if f_med > 0 else None,
                notes=f"iters={siters_f}, max_err={err_f:.2e}",
            )

        # =====================================================================
        # 4. S3-Compiled GF(2)[x]/(x^W-1) Native Kernel & Hashlife V4
        # =====================================================================
        s3_gf2 = get_s3_gf2_library()
        s3_gf2_compile_metrics = s3_gf2.ensure_compiled()
        s3_gf2_compile_ms = round(float(s3_gf2_compile_metrics.get("compile_ms", 0.0)) + float(s3_gf2_compile_metrics.get("gcc_link_ms", 0.0)), 3)
        native_ca = get_native_predictive_library()

        for w in (64, 128, 256):
            rng_gf = random.Random(9000 + w)
            init = [rng_gf.randint(0, 1) for _ in range(w)]
            nwords = (w + 63) // 64
            uwords = [0] * nwords
            for i_bit, val in enumerate(init):
                if val & 1:
                    uwords[i_bit >> 6] |= 1 << (i_bit & 63)
            in_arr = (ctypes.c_int64 * nwords)(*[u - (1 << 64) if u >= (1 << 63) else u for u in uwords])
            out_s3_arr = (ctypes.c_int64 * nwords)()
            work_arr = (ctypes.c_int64 * 24)()
            scratch_arr = (ctypes.c_int64 * 8)()

            # Measure genuine S3-compiled GF(2) native kernel directly vs S3 conventional 10k-step extrapolated & C11
            _, s3_k_cold, s3_k_med, s3_k_iqr = _time_fn(
                s3_gf2._lib.gf2_circulant_fast_forward_s3, in_arr, nwords, w, 90, 1_000_000, out_s3_arr, nwords, work_arr, 24, repeats=21
            )
            _, s3_conv_cold, s3_conv_med10k, s3_conv_iqr = _time_fn(
                s3_gf2._lib.gf2_conventional_ca_s3, in_arr, nwords, w, 90, 10_000, out_s3_arr, nwords, scratch_arr, 8, repeats=7
            )
            s3_conv_est_1m = round(s3_conv_med10k * 100.0, 4)

            s3_fast_wrap, s3w_cold, s3w_med, s3w_iqr = _time_fn(s3_gf2.run_gf2_circulant_fast_forward, init, 90, 1_000_000, repeats=15)
            (c11_bits, c11_kernel_ns), c11_cold, c11_med, c11_iqr = _time_fn(native_ca.run_gf2_circulant_fast_forward, init, 90, 1_000_000, repeats=15)
            c11_k_med = round(float(c11_kernel_ns) / 1e6, 5)
            parity_ok = (list(s3_fast_wrap.final_state) == list(c11_bits))

            _rec(
                records, suite="gf2_s3_native", case=f"gf2_s3_conv_est_W{w}_T1M", category="S3_CONVENTIONAL_NATIVE",
                horizon=1_000_000, cold_ms=round(s3_conv_cold * 100.0, 4), warm_median_ms=s3_conv_est_1m,
                compile_cold_ms=s3_gf2_compile_ms, exact_match=True, accelerated=False,
                soundness_class="CONVENTIONAL_S3_10K_SCALED", notes=f"10k_measured_ms={s3_conv_med10k}",
            )
            _rec(
                records, suite="gf2_s3_native", case=f"gf2_c11_circulant_W{w}_T1M", category="C11_PREDICTIVE_GCC_O3",
                horizon=1_000_000, cold_ms=c11_cold, warm_median_ms=c11_med, warm_iqr_ms=c11_iqr,
                exact_match=parity_ok, accelerated=True, soundness_class="MATHEMATICAL_PROOF_WITH_ASSUMPTIONS",
                notes=f"c11_in_kernel_ms={c11_k_med}",
            )
            _rec(
                records, suite="gf2_s3_native", case=f"gf2_s3_circulant_native_W{w}_T1M", category="S3_PREDICTIVE_NATIVE",
                horizon=1_000_000, cold_ms=s3_k_cold, warm_median_ms=s3_k_med, warm_iqr_ms=s3_k_iqr,
                compile_cold_ms=s3_gf2_compile_ms, exact_match=parity_ok, accelerated=True,
                soundness_class="MATHEMATICAL_PROOF_WITH_ASSUMPTIONS",
                speedup_vs_s3_conv_native=round(s3_conv_est_1m / s3_k_med, 1) if s3_k_med > 0 else None,
                speedup_vs_c11_conv_gcc_o3=round(c11_med / s3_k_med, 2) if s3_k_med > 0 else None,
                notes=f"s3_wrapper_ms={s3w_med}; raw_s3_vs_c11_wrapper={round(s3_k_med/c11_med, 2)}x",
            )

        # Verify W=256 T=10^12 parity for rules 60, 90, 102, 150
        init256 = [1 if i % 7 == 0 else 0 for i in range(256)]
        for rule in (60, 90, 102, 150):
            r_s3 = predictive_execute("rule90", ca_initial_state=init256, width=256, height=1, steps=10**12, boundary="periodic", backend="gf2_s3") if rule == 90 else s3_gf2.run_gf2_circulant_fast_forward(init256, rule, 10**12)
            c_ref, _ = native_ca.run_gf2_circulant_fast_forward(init256, rule, 10**12)
            _rec(
                records, suite="gf2_s3_native", case=f"gf2_s3_rule{rule}_W256_T1e12", category="S3_PREDICTIVE_NATIVE",
                horizon=10**12, cold_ms=round(r_s3.execution_ns / 1e6, 5), warm_median_ms=round(r_s3.execution_ns / 1e6, 5),
                exact_match=(list(r_s3.final_state) == list(c_ref)), accelerated=True,
                soundness_class="MATHEMATICAL_PROOF_WITH_ASSUMPTIONS",
            )

        # Hashlife V4 dense chaotic prefilter vs V2 vs C11 + tiled gliders
        rng_ca = random.Random(4242)
        dense_rand = array("q", [1 if rng_ca.random() < 0.30 else 0 for _ in range(64 * 64)])
        (c11_ca, _), c_ca_cold, c_ca_med, c_ca_iqr = _time_fn(native_ca.run_conventional_ca, "conway", dense_rand, 64, 64, 500, repeats=3)
        hl_pre, pre_cold, pre_med, pre_iqr = _time_fn(run_hashlife_v3_finite_grid, dense_rand, 64, 64, 500, repeats=3)
        _rec(
            records, suite="hashlife_v4", case="conway_dense_chaotic_64x64_T500_c11", category="C11_CONVENTIONAL_GCC_O3",
            horizon=500, cold_ms=c_ca_cold, warm_median_ms=c_ca_med, warm_iqr_ms=c_ca_iqr,
            exact_match=True, accelerated=False, soundness_class="C11_CA_ORACLE",
        )
        _rec(
            records, suite="hashlife_v4", case="conway_dense_chaotic_64x64_T500_v4_prefilter", category="NEGATIVE_CONTROL",
            horizon=500, cold_ms=pre_cold, warm_median_ms=pre_med, warm_iqr_ms=pre_iqr,
            exact_match=(list(hl_pre.final_state) == list(c11_ca) and hl_pre.fallback_reason == "CHAOTIC_PREFILTER_DENSE_ENTROPY" and hl_pre.certificate.details["nodes_created"] == 0),
            accelerated=False, soundness_class="CHAOTIC_PREFILTER_C11_HANDOFF",
            speedup_vs_c11_conv_gcc_o3=round(c_ca_med / pre_med, 3) if pre_med > 0 else None,
        )

        tiled = _make_tiled_glider_grid(128, 128)
        (c11_tg, _), tg_c_cold, tg_c_med, tg_c_iqr = _time_fn(native_ca.run_conventional_ca, "conway", tiled, 128, 128, 4096, repeats=1, warmups=0)
        hl_tg, tg_h_cold, tg_h_med, tg_h_iqr = _time_fn(run_hashlife_v3_finite_grid, tiled, 128, 128, 4096, repeats=3, warmups=1)
        _rec(
            records, suite="hashlife_v4", case="conway_tiled_gliders_128x128_T4096_c11", category="C11_CONVENTIONAL_GCC_O3",
            horizon=4096, cold_ms=tg_c_cold, warm_median_ms=tg_c_med, exact_match=True, accelerated=False, soundness_class="C11_CA_ORACLE",
        )
        _rec(
            records, suite="hashlife_v4", case="conway_tiled_gliders_128x128_T4096_hl_v4", category="S3_PREDICTIVE_PYTHON_WRAPPER",
            horizon=4096, cold_ms=tg_h_cold, warm_median_ms=tg_h_med, warm_iqr_ms=tg_h_iqr,
            exact_match=(list(hl_tg.final_state) == list(c11_tg)), accelerated=True,
            soundness_class="MATHEMATICAL_PROOF_WITH_ASSUMPTIONS",
            speedup_vs_c11_conv_gcc_o3=round(tg_c_cold / tg_h_cold, 2) if tg_h_cold > 0 else None,
        )

        # =====================================================================
        # 5. Workbench V9 compiler-explain, SCEV CR Prototype & Negative Controls
        # =====================================================================
        comp_scev = compile_source(_SCEV_BENCH_SRC, optimization=OptimizationLevel.O1)
        v_poly = verify_scev_against_ir(comp_scev.ir, "poly_acc", [[0], [5], [20]])
        v_tri = verify_scev_against_ir(comp_scev.ir, "triangular_cubic", [[0], [5], [20]])
        scev_rep = analyze_scev_module(comp_scev.ir)
        _rec(
            records, suite="scev_and_negative_controls", case="scev_poly_deg3_and_cascaded_deg4_parity",
            category="S3_PREDICTIVE_PYTHON_WRAPPER", horizon=20, cold_ms=0.0, warm_median_ms=0.0,
            exact_match=(v_poly["verified"] and v_tri["verified"] and scev_rep["triangular_cubic"].max_degree == 4),
            accelerated=True, soundness_class="CHAINS_OF_RECURRENCES_CR",
        )
        _rec(
            records, suite="scev_and_negative_controls", case="scev_negative_controls_impure_and_exp",
            category="NEGATIVE_CONTROL", horizon=0, cold_ms=0.0, warm_median_ms=0.0,
            exact_match=(
                scev_rep["neg_impure"].loops[0].rejection_reason == "NEGATIVE_CONTROL_IMPURE_CALL"
                and scev_rep["neg_exponential"].loops[0].rejection_reason == "NEGATIVE_CONTROL_NON_POLYNOMIAL_RECURRENCE"
            ),
            accelerated=False, soundness_class="NEGATIVE_CONTROL_REJECTED",
        )

        exp_poi = explain_compilation(app_src, allow_fp_reassociation=False, source_name="s3_sci_numerics_v5.s3")
        _rec(
            records, suite="scev_and_negative_controls", case="workbench_v9_compiler_explain_poisson",
            category="S3_PREDICTIVE_PYTHON_WRAPPER", horizon=len(exp_poi["functions"]), cold_ms=0.0, warm_median_ms=0.0,
            exact_match=(exp_poi["workbench_version"] == "9.0" and exp_poi["summary"]["vector_loops_applied"] >= 13),
            accelerated=False, soundness_class="TELEMETRY_VERIFIED",
        )

        # Negative controls: default opt-in isolation, static cutoff, overflow trap, tampered cert, nonlinear GF(2)
        def_comp = CompilationCache().compile(_IR_V4_SRC, optimization=OptimizationLevel.O1)
        _rec(
            records, suite="scev_and_negative_controls", case="default_predictive_exact_false_isolation",
            category="NEGATIVE_CONTROL", horizon=0, cold_ms=0.0, warm_median_ms=0.0,
            exact_match=(len(def_comp.predictive_lowered_functions) == 0), accelerated=False, soundness_class="DEFAULT_OPT_IN_ISOLATED",
        )

        comp_neg_conv = compile_source(_NEG_STATIC_SRC, optimization=OptimizationLevel.O1, predictive_exact=False)
        comp_neg_pred = compile_source(_NEG_STATIC_SRC, optimization=OptimizationLevel.O1, predictive_exact=True, predictive_small_t_cutoff=100)
        low_neg = apply_predictive_native_lowering(comp_neg_conv.ir, source_text=_NEG_STATIC_SRC, small_t_cutoff=100)
        fib92_trapped = False
        try:
            execute_ir(comp_neg_pred.ir, entry="fib", arguments=[92])
        except (NumericError, IRExecutionError):
            fib92_trapped = True
        _rec(
            records, suite="scev_and_negative_controls", case="fib92_overflow_and_small_t10_cutoff",
            category="NEGATIVE_CONTROL", horizon=92, cold_ms=0.0, warm_median_ms=0.0,
            exact_match=(fib92_trapped and low_neg.skipped_functions.get("sum_small") == "SELECTOR_USE_CONVENTIONAL_STATIC_SMALL_T"),
            accelerated=False, soundness_class="TRAP_AND_CUTOFF_PRESERVED",
        )

        # SHA-256 tamper rejection test
        tampered_cert = comp_pred.predictive_certificates[0]
        tampered_fn = tampered_cert.details.get("recognizer", {}).get("function_name", "lcg_mod")
        from dataclasses import replace as dc_replace
        bad_verdict = verify_translation_certificate(
            comp_conv.ir,
            tampered_fn,
            dc_replace(tampered_cert, target_ir_sha="0" * 64),
            target_ir=comp_pred.ir,
            source_text=_IR_V4_SRC,
        )
        _rec(
            records, suite="scev_and_negative_controls", case="proof_checker_tamper_detection",
            category="NEGATIVE_CONTROL", horizon=0, cold_ms=0.0, warm_median_ms=0.0,
            exact_match=(not bad_verdict.accepted), accelerated=False, soundness_class="TAMPER_REJECTED",
        )

        for rule_bad in (30, 110):
            poly_bad, cert_bad = verify_gf2_circulant_and_extract_poly(lambda s, rr=rule_bad: _step_periodic_eca(s, rr), 31)
            _rec(
                records, suite="scev_and_negative_controls", case=f"gf2_reject_nonlinear_rule{rule_bad}",
                category="NEGATIVE_CONTROL", horizon=1, cold_ms=0.0, warm_median_ms=0.0,
                exact_match=(poly_bad is None and cert_bad.correctness_class == CorrectnessClass.COUNTEREXAMPLE_FOUND),
                accelerated=False, soundness_class=cert_bad.correctness_class,
            )

    all_exact = all(bool(r["exact_match"]) for r in records)
    return {
        "campaign": "S3_V4_NATIVE_COMPILER_MATURITY",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "s3_git_sha": _git_sha(S3_ROOT),
        "bench_git_sha": _git_sha(BENCH_ROOT),
        "environment": {
            "platform": platform.platform(),
            "python": platform.python_version(),
            "cpu_features": detect_cpu_features(),
            "scientific_max_instructions": SCIENTIFIC_MAX_INSTRUCTIONS,
            "default_predictive_exact": False,
            "default_fp_reassociation": False,
        },
        "summary": {
            "total_records": len(records),
            "all_exact_match": all_exact,
            "categories": sorted({r["category"] for r in records}),
            "suites": sorted({r["suite"] for r in records}),
        },
        "records": records,
    }


def main() -> int:
    report = run_v4_suite()
    out_json = THIS_DIR / "results_v4.json"
    out_csv = THIS_DIR / "results_v4.csv"
    out_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    csv_cols = [
        "suite",
        "case",
        "category",
        "horizon",
        "cold_ms",
        "warm_median_ms",
        "warm_iqr_ms",
        "compile_cold_ms",
        "speedup_warm_vs_cold",
        "exact_match",
        "accelerated",
        "soundness_class",
        "speedup_vs_s3_conv_native",
        "speedup_vs_c11_conv_gcc_o3",
        "notes",
    ]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_cols)
        writer.writeheader()
        for r in report["records"]:
            writer.writerow({k: r.get(k, "") for k in csv_cols})

    print(json.dumps(report["summary"], indent=2))
    assert report["summary"]["all_exact_match"], "V4 benchmark suite parity/negative control failure!"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
