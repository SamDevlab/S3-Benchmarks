"""Reproducible Benchmark Suite for S3 Autonomous Development V3.

Cleanly separates 6 measurement categories with cold vs warm latency breakdown,
exact mathematical parity checks, and verified negative controls:
  1. S3_CONVENTIONAL_NATIVE       (x86-64 compiled S3 without predictive_exact, 50M budget active)
  2. S3_PREDICTIVE_NATIVE         (x86-64 compiled S3 with predictive_exact=True / AVX2+FMA kernels)
  3. S3_PREDICTIVE_PYTHON_WRAPPER (Python predictive APIs, IR recognizer/checker, GF2/Hashlife V3 wrappers)
  4. C11_CONVENTIONAL_GCC_O3      (GCC -O3 C11 iterative reference loops & CSR CG-Jacobi)
  5. C11_PREDICTIVE_GCC_O3        (GCC -O3 C11 closed-form / circulant / resident Brent workspace)
  6. NEGATIVE_CONTROL             (Selector gates, runtime overflow fallbacks, rejections, chaotic aborts)
"""

from __future__ import annotations

import csv
import ctypes
import json
import platform
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
from bootstrap.s3.backends.x86_64.simd_features import compile_simd_lib, detect_cpu_features
from bootstrap.s3.backends.x86_64.toolchain import NativeToolchain
from bootstrap.s3.ir_emulator import IRExecutionError, execute_ir
from bootstrap.s3.numeric import NumericError
from bootstrap.s3.optimizer import OptimizationLevel
from bootstrap.s3.pipeline import CompilationCache, compile_source, compile_sources
from bootstrap.s3.predictive_compute import PredictiveComputeToolkit
from bootstrap.s3.predictive_compute_v2 import predictive_execute, predictive_execute_ir, predictive_select, predictive_verify
from bootstrap.s3.predictive_gf2 import (
    GF2LinearCACache,
    run_gf2_ca,
    step_gf2_rule_direct,
    verify_gf2_circulant_and_extract_poly,
)
from bootstrap.s3.predictive_hashlife_v2 import (
    HashlifeV2Engine,
    run_hashlife_v2_finite_grid,
    run_hashlife_v3_finite_grid,
)
from bootstrap.s3.predictive_native import get_native_predictive_library
from bootstrap.s3.predictive_native_lowering import apply_predictive_native_lowering
from bootstrap.s3.predictive_proof_checker import verify_translation_certificate
from bootstrap.s3.predictive_verifier import CorrectnessClass
from examples.compute.cellular_automata_toolkit import create_cellular_toolkit
from tools.numerics_oracle_v4_7 import GCC_CSR_JACOBI_C, build_poisson2d

_C11_BENCH_REF = r"""
#define _POSIX_C_SOURCE 200809L
#include <stdint.h>
#include <string.h>

int64_t c11_lcg_mod_loop(int64_t n, int64_t x0, int64_t m) {
    if (m <= 0) return x0;
    __int128 x = x0;
    for (int64_t i = 0; i < n; ++i) {
        __int128 nxt = 3 * x + 5;
        x = nxt % m;
    }
    return (int64_t)x;
}

int64_t c11_fib_mod_loop(int64_t n, int64_t m) {
    if (m <= 0) return 0;
    int64_t a = 0, b = 1;
    for (int64_t i = 0; i < n; ++i) {
        int64_t nb = (a + b) % m;
        a = b;
        b = nb;
    }
    return a;
}

int64_t c11_coupled2_loop(int64_t n, int64_t x0, int64_t y0, int64_t m) {
    if (m <= 0) return x0;
    int64_t x = x0, y = y0;
    for (int64_t i = 0; i < n; ++i) {
        int64_t nx = (2 * x + y + 1) % m;
        int64_t ny = (x + 3 * y + 2) % m;
        x = nx;
        y = ny;
    }
    return x;
}

int64_t c11_stride_sum_loop(int64_t n, int64_t x0, int64_t d) {
    int64_t x = x0;
    for (int64_t i = 0; i < n; ++i) {
        x += d;
    }
    return x;
}

void c11_gf2_periodic_loop(const int64_t *init, int32_t w, int32_t rule, int64_t steps, int64_t *out) {
    int64_t buf_a[512], buf_b[512];
    int64_t *cur = buf_a, *nxt = buf_b;
    memcpy(cur, init, (size_t)w * sizeof(int64_t));
    for (int64_t s = 0; s < steps; ++s) {
        for (int32_t i = 0; i < w; ++i) {
            int32_t l = cur[(i - 1 + w) % w] & 1;
            int32_t c = cur[i] & 1;
            int32_t r = cur[(i + 1) % w] & 1;
            nxt[i] = (rule >> ((l << 2) | (c << 1) | r)) & 1;
        }
        int64_t *tmp = cur; cur = nxt; nxt = tmp;
    }
    memcpy(out, cur, (size_t)w * sizeof(int64_t));
}

double c11_dot_f64(const double *a, const double *b, int64_t n) {
    double acc = 0.0;
    for (int64_t i = 0; i < n; ++i) {
        acc += a[i] * b[i];
    }
    return acc;
}
"""

_IR_BENCH_SRC = """
export fn lcg_mod(n: i64, x0: i64, m: i64) -> i64:
    mut i: i64 = 0
    mut x: i64 = x0
    while i < n:
        nxt: i64 = 3 * x + 5
        q: i64 = nxt / m
        x = nxt - q * m
        i = i + 1
    return x

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

export fn coupled2(n: i64, x0: i64, y0: i64, m: i64) -> i64:
    mut x: i64 = x0
    mut y: i64 = y0
    mut i: i64 = 0
    while i < n:
        sx: i64 = 2 * x + y + 1
        qx: i64 = sx / m
        nx: i64 = sx - qx * m
        sy: i64 = x + 3 * y + 2
        qy: i64 = sy / m
        ny: i64 = sy - qy * m
        x = nx
        y = ny
        i = i + 1
    return x

export fn stride_sum(n: i64, x0: i64, d: i64) -> i64:
    mut i: i64 = 0
    mut x: i64 = x0
    while i < n:
        x = x + d
        i = i + 1
    return x

export fn fp_loop(n: i64, x0: f64) -> f64:
    mut i: i64 = 0
    mut x: f64 = x0
    while i < n:
        x = 2.0 * x + 1.0
        i = i + 1
    return x

export fn nonlinear_quad(n: i64, x0: i64) -> i64:
    mut i: i64 = 0
    mut x: i64 = x0
    while i < n:
        x = x * x + 1
        i = i + 1
    return x

export fn main() -> i64:
    return 0
"""

_SMALL_STATIC_SRC = """
export fn sum_small() -> i64:
    mut i: i64 = 0
    mut s: i64 = 0
    while i < 10:
        s = s + i
        i = i + 1
    return s

export fn main() -> i64:
    return sum_small()
"""


def _git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def _time_fn(fn, *, warmups: int = 1, repeats: int = 7) -> tuple[Any, float, float, float]:
    """Return (value, cold_ms, warm_median_ms, warm_iqr_ms)."""
    tc0 = time.perf_counter_ns()
    val = fn()
    cold_ms = (time.perf_counter_ns() - tc0) / 1e6
    for _ in range(max(0, warmups - 1)):
        fn()
    samples_ms: list[float] = []
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        fn()
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
    row = {
        "suite": suite,
        "case": case,
        "category": category,
        "horizon": horizon,
        "cold_ms": cold_ms,
        "warm_median_ms": warm_median_ms,
        "warm_iqr_ms": warm_iqr_ms,
        "compile_cold_ms": compile_cold_ms,
        "speedup_warm_vs_cold": round(cold_ms / warm_median_ms, 2) if (cold_ms and warm_median_ms and warm_median_ms > 0) else None,
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


def _compile_c11_refs(tmp_dir: Path) -> tuple[ctypes.CDLL, ctypes.CDLL]:
    gcc = shutil.which("gcc")
    if not gcc:
        raise RuntimeError("gcc not found")
    ref_c = tmp_dir / "v3_bench_ref.c"
    ref_so = tmp_dir / "libv3_bench_ref.so"
    ref_c.write_text(_C11_BENCH_REF, encoding="utf-8")
    subprocess.run([gcc, "-O3", "-std=c11", "-shared", "-fPIC", str(ref_c), "-o", str(ref_so)], check=True)
    lib = ctypes.CDLL(str(ref_so))
    lib.c11_lcg_mod_loop.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
    lib.c11_lcg_mod_loop.restype = ctypes.c_int64
    lib.c11_fib_mod_loop.argtypes = [ctypes.c_int64, ctypes.c_int64]
    lib.c11_fib_mod_loop.restype = ctypes.c_int64
    lib.c11_coupled2_loop.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
    lib.c11_coupled2_loop.restype = ctypes.c_int64
    lib.c11_stride_sum_loop.argtypes = [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
    lib.c11_stride_sum_loop.restype = ctypes.c_int64
    i64_p = ctypes.POINTER(ctypes.c_int64)
    lib.c11_gf2_periodic_loop.argtypes = [i64_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int64, i64_p]
    lib.c11_gf2_periodic_loop.restype = None
    d_p = ctypes.POINTER(ctypes.c_double)
    lib.c11_dot_f64.argtypes = [d_p, d_p, ctypes.c_int64]
    lib.c11_dot_f64.restype = ctypes.c_double

    csr_c = tmp_dir / "gcc_csr.c"
    csr_so = tmp_dir / "libgcc_csr.so"
    csr_c.write_text(GCC_CSR_JACOBI_C, encoding="utf-8")
    subprocess.run([gcc, "-O3", "-shared", "-fPIC", str(csr_c), "-o", str(csr_so)], check=True)
    csr_lib = ctypes.CDLL(str(csr_so))
    csr_lib.gcc_cg_solve_csr_jacobi.argtypes = [i64_p, i64_p] + [d_p] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64, d_p]
    csr_lib.gcc_cg_solve_csr_jacobi.restype = ctypes.c_int64
    return lib, csr_lib


def _step_periodic_eca(state: list[int], rule: int) -> list[int]:
    """Execute one periodic elementary 1D cellular automaton step (including nonlinear rules)."""
    w = len(state)
    return [
        (rule >> (((state[(i - 1) % w] & 1) << 2) | ((state[i] & 1) << 1) | (state[(i + 1) % w] & 1))) & 1
        for i in range(w)
    ]


def run_suite() -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    native_lib = get_native_predictive_library()
    toolchain = NativeToolchain.detect()

    with tempfile.TemporaryDirectory() as tmpd_str:
        tmpd = Path(tmpd_str)
        c11_ref, c11_csr = _compile_c11_refs(tmpd)

        # ------------------------------------------------------------------
        # 1. IR Recurrences across 6 categories (T=10 .. T=10^12)
        # ------------------------------------------------------------------
        t0 = time.perf_counter_ns()
        comp_conv = compile_source(_IR_BENCH_SRC, optimization=OptimizationLevel.O1, predictive_exact=False)
        conv_so = tmpd / "s3_ir_conv.so"
        toolchain.build_shared(
            generate_ffi_assembly(comp_conv.require_ordinary_artifacts()[1], max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS),
            conv_so,
        )
        s3_conv_compile_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)
        s3_conv_lib = ctypes.CDLL(str(conv_so))

        t0 = time.perf_counter_ns()
        comp_pred = compile_source(_IR_BENCH_SRC, optimization=OptimizationLevel.O1, predictive_exact=True)
        pred_so = tmpd / "s3_ir_pred.so"
        toolchain.build_shared(
            generate_ffi_assembly(comp_pred.require_ordinary_artifacts()[1], max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS),
            pred_so,
        )
        s3_pred_compile_ms = round((time.perf_counter_ns() - t0) / 1e6, 3)
        s3_pred_lib = ctypes.CDLL(str(pred_so))

        for fn_name, argtypes in (
            ("lcg_mod", [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]),
            ("fib", [ctypes.c_int64]),
            ("fib_mod", [ctypes.c_int64, ctypes.c_int64]),
            ("coupled2", [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]),
            ("stride_sum", [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]),
        ):
            for lib in (s3_conv_lib, s3_pred_lib):
                fn = getattr(lib, fn_name)
                fn.argtypes = argtypes
                fn.restype = ctypes.c_int64

        assert comp_conv.ir is not None and comp_pred.ir is not None
        cert_by_fn = {
            "lcg_mod": next(c for c in comp_pred.predictive_certificates if "lcg_mod" in c.transformation_id),
            "fib_mod": next(c for c in comp_pred.predictive_certificates if "fib_mod" in c.transformation_id),
            "coupled2": next(c for c in comp_pred.predictive_certificates if "coupled2" in c.transformation_id),
            "stride_sum": next(c for c in comp_pred.predictive_certificates if "stride_sum" in c.transformation_id),
        }
        checker_ok = {}
        for fn_name, cert in cert_by_fn.items():
            if fn_name == "lcg_mod":
                probes = [(0, 7, 1_000_000_007), (1, 7, 1_000_000_007), (5, 7, 1_000_000_007)]
            elif fn_name == "fib_mod":
                probes = [(0, 1_000_000_007), (1, 1_000_000_007), (6, 1_000_000_007)]
            elif fn_name == "coupled2":
                probes = [(0, 1, 3, 1_000_000_007), (1, 1, 3, 1_000_000_007), (4, 1, 3, 1_000_000_007)]
            else:
                probes = [(0, 100, 3), (1, 100, 3), (5, 100, 3)]
            verdict = verify_translation_certificate(
                comp_conv.ir,
                fn_name,
                cert,
                target_ir=comp_pred.ir,
                source_text=_IR_BENCH_SRC,
                differential_probes=probes,
                concrete_eval_fn=lambda a, _fn=fn_name: execute_ir(comp_conv.ir, entry=_fn, arguments=list(a)),
            )
            checker_ok[fn_name] = verdict.accepted

        mod_p = 1_000_000_007
        for T in (10, 1_000, 100_000, 1_000_000, 10**9, 10**12):
            case = f"lcg_mod_T{T}"
            c11_conv_warm = None
            s3_conv_warm = None
            ref_val = int(s3_pred_lib.lcg_mod(T, 7, mod_p))

            if T <= 1_000_000:
                s3v, s3c, s3w, s3iqr = _time_fn(lambda t=T: int(s3_conv_lib.lcg_mod(t, 7, mod_p)))
                s3_conv_warm = s3w
                _rec(
                    records,
                    suite="ir_native_lcg_mod",
                    case=case,
                    category="S3_CONVENTIONAL_NATIVE",
                    horizon=T,
                    cold_ms=s3c,
                    warm_median_ms=s3w,
                    warm_iqr_ms=s3iqr,
                    compile_cold_ms=s3_conv_compile_ms,
                    exact_match=(s3v == ref_val),
                    accelerated=False,
                    soundness_class="CONVENTIONAL_BASELINE",
                )
            if T <= 10_000_000:
                c11v, c11c, c11w, c11iqr = _time_fn(lambda t=T: int(c11_ref.c11_lcg_mod_loop(t, 7, mod_p)))
                c11_conv_warm = c11w
                _rec(
                    records,
                    suite="ir_native_lcg_mod",
                    case=case,
                    category="C11_CONVENTIONAL_GCC_O3",
                    horizon=T,
                    cold_ms=c11c,
                    warm_median_ms=c11w,
                    warm_iqr_ms=c11iqr,
                    exact_match=(c11v == ref_val),
                    accelerated=False,
                    soundness_class="CONVENTIONAL_BASELINE",
                )

            p_val, p_c, p_w, p_iqr = _time_fn(lambda t=T: int(s3_pred_lib.lcg_mod(t, 7, mod_p)))
            _rec(
                records,
                suite="ir_native_lcg_mod",
                case=case,
                category="S3_PREDICTIVE_NATIVE",
                horizon=T,
                cold_ms=p_c,
                warm_median_ms=p_w,
                warm_iqr_ms=p_iqr,
                compile_cold_ms=s3_pred_compile_ms,
                exact_match=(p_val == ref_val and checker_ok["lcg_mod"]),
                accelerated=(T >= 40),
                soundness_class=cert_by_fn["lcg_mod"].correctness_class,
                speedup_vs_s3_conv_native=round(s3_conv_warm / p_w, 2) if (s3_conv_warm and p_w > 0) else None,
                speedup_vs_c11_conv_gcc_o3=round(c11_conv_warm / p_w, 2) if (c11_conv_warm and p_w > 0) else None,
            )

            c11p_v, c11p_c, c11p_w, c11p_iqr = _time_fn(
                lambda t=T: native_lib.run_scalar_affine_mod(3, 5, 7, mod_p, t)
            )
            _rec(
                records,
                suite="ir_native_lcg_mod",
                case=case,
                category="C11_PREDICTIVE_GCC_O3",
                horizon=T,
                cold_ms=c11p_c,
                warm_median_ms=c11p_w,
                warm_iqr_ms=c11p_iqr,
                exact_match=(c11p_v == ref_val),
                accelerated=True,
                soundness_class=cert_by_fn["lcg_mod"].correctness_class,
                speedup_vs_s3_conv_native=round(s3_conv_warm / c11p_w, 2) if (s3_conv_warm and c11p_w > 0) else None,
                speedup_vs_c11_conv_gcc_o3=round(c11_conv_warm / c11p_w, 2) if (c11_conv_warm and c11p_w > 0) else None,
            )

            py_res, py_c, py_w, py_iqr = _time_fn(
                lambda t=T: predictive_execute_ir(comp_conv.ir, "lcg_mod", [t, 7, mod_p]),
                warmups=1,
                repeats=3,
            )
            sel = predictive_select(source_or_module=comp_conv.ir, function_name="lcg_mod", steps=T)
            _rec(
                records,
                suite="ir_native_lcg_mod",
                case=case,
                category="S3_PREDICTIVE_PYTHON_WRAPPER" if T >= 40 else "NEGATIVE_CONTROL",
                horizon=T,
                cold_ms=py_c,
                warm_median_ms=py_w,
                warm_iqr_ms=py_iqr,
                exact_match=(py_res.final_state == ref_val),
                accelerated=py_res.accelerated,
                soundness_class=py_res.certificate.soundness_class,
                speedup_vs_s3_conv_native=round(s3_conv_warm / py_w, 2) if (s3_conv_warm and py_w > 0) else None,
                speedup_vs_c11_conv_gcc_o3=round(c11_conv_warm / py_w, 2) if (c11_conv_warm and py_w > 0) else None,
                notes=f"selector={sel.decision}",
            )

        # Coupled 2x2 & fib_mod & stride_sum at T=100k (parity + speedup) and T=10^12
        for fn_name, args_100k, args_t12, c11_conv_fn in (
            ("fib_mod", (100_000, mod_p), (10**12, mod_p), lambda a: int(c11_ref.c11_fib_mod_loop(*a))),
            ("coupled2", (100_000, 1, 3, mod_p), (10**12, 1, 3, mod_p), lambda a: int(c11_ref.c11_coupled2_loop(*a))),
            ("stride_sum", (100_000, 100, 3), (10**12, 100, 3), lambda a: int(c11_ref.c11_stride_sum_loop(*a))),
        ):
            s3_cfn = getattr(s3_conv_lib, fn_name)
            s3_pfn = getattr(s3_pred_lib, fn_name)
            cval, cc, cw, ciqr = _time_fn(lambda: int(s3_cfn(*args_100k)))
            gcval, gcc_c, gcc_w, gcc_iqr = _time_fn(lambda: c11_conv_fn(args_100k))
            pval, pc, pw, piqr = _time_fn(lambda: int(s3_pfn(*args_100k)))
            p12_val, p12_c, p12_w, p12_iqr = _time_fn(lambda: int(s3_pfn(*args_t12)))
            _rec(
                records, suite="ir_native_multi", case=f"{fn_name}_T100k", category="S3_CONVENTIONAL_NATIVE",
                horizon=100_000, cold_ms=cc, warm_median_ms=cw, warm_iqr_ms=ciqr,
                exact_match=(cval == pval), accelerated=False, soundness_class="CONVENTIONAL_BASELINE",
            )
            _rec(
                records, suite="ir_native_multi", case=f"{fn_name}_T100k", category="C11_CONVENTIONAL_GCC_O3",
                horizon=100_000, cold_ms=gcc_c, warm_median_ms=gcc_w, warm_iqr_ms=gcc_iqr,
                exact_match=(gcval == pval), accelerated=False, soundness_class="CONVENTIONAL_BASELINE",
            )
            _rec(
                records, suite="ir_native_multi", case=f"{fn_name}_T100k", category="S3_PREDICTIVE_NATIVE",
                horizon=100_000, cold_ms=pc, warm_median_ms=pw, warm_iqr_ms=piqr,
                exact_match=(pval == cval and checker_ok[fn_name]), accelerated=True,
                soundness_class=cert_by_fn[fn_name].correctness_class,
                speedup_vs_s3_conv_native=round(cw / pw, 2),
                speedup_vs_c11_conv_gcc_o3=round(gcc_w / pw, 2),
            )
            _rec(
                records, suite="ir_native_multi", case=f"{fn_name}_T1e12", category="S3_PREDICTIVE_NATIVE",
                horizon=10**12, cold_ms=p12_c, warm_median_ms=p12_w, warm_iqr_ms=p12_iqr,
                exact_match=checker_ok[fn_name], accelerated=True,
                soundness_class=cert_by_fn[fn_name].correctness_class,
                extra={"value_mod": p12_val},
            )

        # ------------------------------------------------------------------
        # 2. GF(2) Circulant Rules {60, 90, 102, 150} (AV3-009)
        # ------------------------------------------------------------------
        gf2_cache = GF2LinearCACache()
        for w in (64, 256):
            init_gf2 = [1 if (i % 7 == 0) else 0 for i in range(w)]
            in_i64 = (ctypes.c_int64 * w)(*init_gf2)
            out_i64 = (ctypes.c_int64 * w)()
            for T in (1_000, 100_000, 10**12):
                case = f"rule90_periodic_w{w}_T{T}"
                c11_w_ms = None
                c11_ref_state = None
                if T <= 100_000:
                    _, g_c, g_w, g_iqr = _time_fn(lambda r=90, t=T: c11_ref.c11_gf2_periodic_loop(in_i64, w, r, t, out_i64))
                    c11_ref_state = [out_i64[i] for i in range(w)]
                    c11_w_ms = g_w
                    _rec(
                        records, suite="gf2_circulant_ca", case=case, category="C11_CONVENTIONAL_GCC_O3",
                        horizon=T, cold_ms=g_c, warm_median_ms=g_w, warm_iqr_ms=g_iqr,
                        exact_match=True, accelerated=False, soundness_class="CONVENTIONAL_BASELINE",
                    )

                run_gf2_ca(init_gf2, 90, T, boundary="periodic", cache=GF2LinearCACache())  # measure cold uncached below
                pyc_res, pyc_c, pyc_w, pyc_iqr = _time_fn(
                    lambda t=T: run_gf2_ca(init_gf2, 90, t, boundary="periodic"),
                    warmups=0,
                    repeats=3,
                )
                run_gf2_ca(init_gf2, 90, T, boundary="periodic", cache=gf2_cache)
                pyw_res, pyw_c, pyw_w, pyw_iqr = _time_fn(
                    lambda t=T: run_gf2_ca(init_gf2, 90, t, boundary="periodic", cache=gf2_cache),
                    warmups=1,
                    repeats=5,
                )
                c11p_res, c11p_c, c11p_w, c11p_iqr = _time_fn(
                    lambda t=T: native_lib.run_gf2_circulant_fast_forward(init_gf2, 90, t),
                    warmups=1,
                    repeats=7,
                )
                parity = (
                    list(pyc_res.final_state) == list(pyw_res.final_state) == list(c11p_res[0])
                    and (c11_ref_state is None or list(pyc_res.final_state) == c11_ref_state)
                )
                _rec(
                    records, suite="gf2_circulant_ca", case=case, category="S3_PREDICTIVE_PYTHON_WRAPPER",
                    horizon=T, cold_ms=pyc_c, warm_median_ms=pyw_w, warm_iqr_ms=pyw_iqr,
                    exact_match=parity, accelerated=True, soundness_class=pyw_res.certificate.soundness_class,
                    speedup_vs_c11_conv_gcc_o3=round(c11_w_ms / pyw_w, 2) if (c11_w_ms and pyw_w > 0) else None,
                    notes=f"cold_no_cache_ms={pyc_c}",
                )
                _rec(
                    records, suite="gf2_circulant_ca", case=case, category="C11_PREDICTIVE_GCC_O3",
                    horizon=T, cold_ms=c11p_c, warm_median_ms=c11p_w, warm_iqr_ms=c11p_iqr,
                    exact_match=parity, accelerated=True, soundness_class="MATHEMATICAL_PROOF_WITH_ASSUMPTIONS",
                    speedup_vs_c11_conv_gcc_o3=round(c11_w_ms / c11p_w, 2) if (c11_w_ms and c11p_w > 0) else None,
                    extra={"kernel_us": round(c11p_res[1] / 1e3, 3)},
                )

        # Verify rules 60, 102, 150 at W=256 T=64 against direct periodic step
        for r in (60, 102, 150):
            init256 = [1 if (i % 9 == 0) else 0 for i in range(256)]
            dir_state = array("q", init256)
            for _ in range(64):
                dir_state = step_gf2_rule_direct(dir_state, r, boundary="periodic")
            c11_circ_out, c11_k_ns = native_lib.run_gf2_circulant_fast_forward(init256, r, 10**12)
            py_circ_out = run_gf2_ca(init256, r, 10**12, boundary="periodic")
            dir_c11_64, _ = native_lib.run_gf2_circulant_fast_forward(init256, r, 64)
            _rec(
                records, suite="gf2_circulant_ca", case=f"rule{r}_periodic_w256_T1e12",
                category="C11_PREDICTIVE_GCC_O3", horizon=10**12,
                cold_ms=round(c11_k_ns / 1e6, 5), warm_median_ms=round(c11_k_ns / 1e6, 5),
                exact_match=(list(dir_c11_64) == list(dir_state) and list(c11_circ_out) == list(py_circ_out.final_state)),
                accelerated=True, soundness_class="MATHEMATICAL_PROOF_WITH_ASSUMPTIONS",
            )

        # ------------------------------------------------------------------
        # 3. Hashlife V3 Adaptive Abort & Resident C11 Brent (AV3-010)
        # ------------------------------------------------------------------
        rp64 = array("q", [0]) * (64 * 64)
        for dr, dc in ((0, 1), (0, 2), (1, 0), (1, 1), (2, 1)):
            rp64[(32 + dr) * 64 + (32 + dc)] = 1
        c11_rp64, c11_rp64_c, c11_rp64_w, _ = _time_fn(lambda: native_lib.run_conventional_ca("conway", rp64, 64, 64, 500), warmups=1, repeats=3)
        hl2_rp64, hl2_rp64_c, hl2_rp64_w, _ = _time_fn(
            lambda: run_hashlife_v2_finite_grid(rp64, 64, 64, 500, rule="conway", engine=HashlifeV2Engine("conway")),
            warmups=0, repeats=1,
        )
        hl3_rp64, hl3_rp64_c, hl3_rp64_w, _ = _time_fn(
            lambda: run_hashlife_v3_finite_grid(rp64, 64, 64, 500, rule="conway"),
            warmups=0, repeats=2,
        )
        _rec(
            records, suite="hashlife_v3_and_brent", case="conway_r_pentomino_64x64_T500",
            category="C11_CONVENTIONAL_GCC_O3", horizon=500, cold_ms=c11_rp64_c, warm_median_ms=c11_rp64_w,
            exact_match=True, accelerated=False, soundness_class="CONVENTIONAL_BASELINE",
        )
        _rec(
            records, suite="hashlife_v3_and_brent", case="conway_r_pentomino_64x64_T500_v2_baseline",
            category="S3_PREDICTIVE_PYTHON_WRAPPER", horizon=500, cold_ms=hl2_rp64_c, warm_median_ms=hl2_rp64_w,
            exact_match=(list(hl2_rp64.final_state) == list(c11_rp64[0])), accelerated=True,
            soundness_class="MATHEMATICAL_PROOF_WITH_ASSUMPTIONS",
            speedup_vs_c11_conv_gcc_o3=round(c11_rp64_w / hl2_rp64_c, 3),
        )
        _rec(
            records, suite="hashlife_v3_and_brent", case="conway_r_pentomino_64x64_T500_v3_abort",
            category="NEGATIVE_CONTROL", horizon=500, cold_ms=hl3_rp64_c, warm_median_ms=hl3_rp64_w,
            exact_match=(list(hl3_rp64.final_state) == list(c11_rp64[0])), accelerated=False,
            soundness_class=hl3_rp64.certificate.soundness_class,
            speedup_vs_c11_conv_gcc_o3=round(c11_rp64_w / hl3_rp64_w, 3),
            notes=f"V2/V3_speedup={round(hl2_rp64_c / hl3_rp64_c, 2)}x, method={hl3_rp64.certificate.method_used}",
            extra=hl3_rp64.certificate.details,
        )

        # Structured 128x128 tiled gliders T=4096
        gl128 = array("q", [0]) * (128 * 128)
        for br in range(4, 108, 32):
            for bc in range(4, 108, 32):
                for dr, dc in ((0, 1), (1, 2), (2, 0), (2, 1), (2, 2)):
                    gl128[(br + dr) * 128 + (bc + dc)] = 1
        c11_gl, c11_gl_c, c11_gl_w, _ = _time_fn(lambda: native_lib.run_conventional_ca("conway", gl128, 128, 128, 4096), warmups=0, repeats=1)
        hl3_gl, hl3_gl_c, hl3_gl_w, _ = _time_fn(lambda: run_hashlife_v3_finite_grid(gl128, 128, 128, 4096, rule="conway"), warmups=0, repeats=2)
        _rec(
            records, suite="hashlife_v3_and_brent", case="conway_tiled_gliders_128x128_T4096",
            category="C11_CONVENTIONAL_GCC_O3", horizon=4096, cold_ms=c11_gl_c, warm_median_ms=c11_gl_w,
            exact_match=True, accelerated=False, soundness_class="CONVENTIONAL_BASELINE",
        )
        _rec(
            records, suite="hashlife_v3_and_brent", case="conway_tiled_gliders_128x128_T4096",
            category="S3_PREDICTIVE_PYTHON_WRAPPER", horizon=4096, cold_ms=hl3_gl_c, warm_median_ms=hl3_gl_w,
            exact_match=(list(hl3_gl.final_state) == list(c11_gl[0])), accelerated=hl3_gl.accelerated,
            soundness_class=hl3_gl.certificate.soundness_class,
            speedup_vs_c11_conv_gcc_o3=round(c11_gl_w / hl3_gl_c, 2),
        )

        # Resident C11 Brent workspace vs Python V1 & bit-packed
        g16 = array("q", [0]) * (16 * 16)
        for dr, dc in ((0, 1), (1, 2), (2, 0), (2, 1), (2, 2)):
            g16[(2 + dr) * 16 + (2 + dc)] = 1
        g16_words = array("Q", [0]) * 4
        for i, bit in enumerate(g16):
            if bit:
                g16_words[i >> 6] |= 1 << (i & 63)

        tk_v1 = create_cellular_toolkit(backend="native")
        try:
            pred_v1 = PredictiveComputeToolkit(tk_v1)
            v1_b_res, v1_b_c, v1_b_w, _ = _time_fn(
                lambda: pred_v1.run_steps("conway", list(g16), 16, 16, 1_000_000, strategy="brent", discovery_step_budget=512),
                warmups=0, repeats=2,
            )
            ws_before = native_lib.workspace_stats()["alloc_count"]
            c11_b_res, c11_b_c, c11_b_w, c11_b_iqr = _time_fn(
                lambda: native_lib.run_brent_ca("conway", g16, 16, 16, 1_000_000, discovery_step_budget=512),
                warmups=1, repeats=7,
            )
            c11_pk_res, c11_pk_c, c11_pk_w, _ = _time_fn(
                lambda: native_lib.run_brent_ca_packed("conway", g16_words, 16, 16, 1_000_000, discovery_step_budget=512),
                warmups=1, repeats=7,
            )
            ws_after = native_lib.workspace_stats()
            unpacked_pk = [((c11_pk_res.final_state[i >> 6] >> (i & 63)) & 1) for i in range(256)]
            brent_match = list(v1_b_res.final_state) == list(c11_b_res.final_state) == unpacked_pk
            _rec(
                records, suite="hashlife_v3_and_brent", case="conway_glider_16x16_T1e6_brent_v1_py",
                category="S3_PREDICTIVE_PYTHON_WRAPPER", horizon=1_000_000, cold_ms=v1_b_c, warm_median_ms=v1_b_w,
                exact_match=brent_match, accelerated=v1_b_res.accelerated,
                soundness_class=v1_b_res.certificate.soundness_class,
            )
            _rec(
                records, suite="hashlife_v3_and_brent", case="conway_glider_16x16_T1e6_brent_resident",
                category="C11_PREDICTIVE_GCC_O3", horizon=1_000_000, cold_ms=c11_b_c, warm_median_ms=c11_b_w,
                warm_iqr_ms=c11_b_iqr, exact_match=brent_match and (ws_after["alloc_count"] == ws_before),
                accelerated=c11_b_res.accelerated, soundness_class=c11_b_res.certificate.soundness_class,
                extra={"warm_realloc_delta": ws_after["alloc_count"] - ws_before, "packed_warm_ms": c11_pk_w},
            )
        finally:
            tk_v1.close()

        # ------------------------------------------------------------------
        # 4. Scientific Compiler Poisson 2D & AVX2+FMA Dot Product (AV3-005/006/008)
        # ------------------------------------------------------------------
        core_src = (S3_ROOT / "examples/horizons_v3/s3_sci_core.s3").read_text(encoding="utf-8")
        app_src = (S3_ROOT / "examples/horizons_v4/s3_sci_numerics_v5.s3").read_text(encoding="utf-8")
        t_pc0 = time.perf_counter_ns()
        p_comp = compile_sources(
            {"s3_sci_core.s3": core_src, "s3_sci_numerics_v5.s3": app_src},
            entry_module="s3_sci_numerics_v5",
            optimization=OptimizationLevel.O1,
        )
        _, p_asm = p_comp.require_ordinary_artifacts()
        sci_backend = X8664Backend.scientific(max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS)
        p_so = tmpd / "s3_numerics_v5.so"
        p_s = tmpd / "s3_numerics_v5.s"
        p_s.write_text(sci_backend._generate_ffi(p_asm), encoding="utf-8")
        subprocess.run([shutil.which("gcc"), "-shared", "-fPIC", "-O2", str(p_s), "-o", str(p_so)], check=True)
        poisson_compile_ms = round((time.perf_counter_ns() - t_pc0) / 1e6, 3)

        plib = ctypes.CDLL(str(p_so))
        I_PTR = ctypes.POINTER(ctypes.c_int64)
        D_PTR = ctypes.POINTER(ctypes.c_double)
        s3_cg_chunk = getattr(plib, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi_chunk")
        s3_cg_chunk.argtypes = [I_PTR, ctypes.c_int64] * 2 + [D_PTR, ctypes.c_int64] * 8 + [ctypes.c_int64, ctypes.c_double, ctypes.c_int64, D_PTR, ctypes.c_int64]
        s3_cg_chunk.restype = ctypes.c_int64

        for grid, cstep in ((32, 50), (48, 50), (64, 50), (80, 25), (96, 25)):
            n = grid * grid
            rp_l, ci_l, vl_l, b_l, _ = build_poisson2d(grid)
            rp = (ctypes.c_int64 * len(rp_l))(*rp_l)
            ci = (ctypes.c_int64 * len(ci_l))(*ci_l)
            vl = (ctypes.c_double * len(vl_l))(*vl_l)
            dg = (ctypes.c_double * n)(*([4.0] * n))
            b = (ctypes.c_double * n)(*b_l)
            gx, gr, gz, gp, gap = [(ctypes.c_double * n)() for _ in range(5)]
            gout = (ctypes.c_double * 1)()
            sx, sr, sz, sp, sap = [(ctypes.c_double * n)() for _ in range(5)]

            def run_gcc_cg():
                ctypes.memset(gx, 0, ctypes.sizeof(gx))
                return c11_csr.gcc_cg_solve_csr_jacobi(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, 1e-10, 5000, gout)

            def run_s3_cg():
                ctypes.memset(sx, 0, ctypes.sizeof(sx))
                st = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
                it = 0
                while it < 5000 and st[3] < 0.5:
                    step = min(cstep, 5000 - it)
                    rc = s3_cg_chunk(rp, len(rp_l), ci, len(ci_l), vl, len(vl_l), dg, n, b, n, sx, n, sr, n, sz, n, sp, n, sap, n, n, 1e-20, step, st, 4)
                    if rc < 0:
                        raise RuntimeError(f"S3 CG failed rc={rc}")
                    it += rc
                return it

            giters, gc_c, gc_w, gc_iqr = _time_fn(run_gcc_cg, warmups=1, repeats=3)
            siters, s3_c, s3_w, s3_iqr = _time_fn(run_s3_cg, warmups=1, repeats=3)
            max_err = max(abs(sx[i] - gx[i]) for i in range(n))
            _rec(
                records, suite="poisson2d_native_scaling", case=f"poisson_{grid}x{grid}_cg_jacobi",
                category="C11_CONVENTIONAL_GCC_O3", horizon=n, cold_ms=gc_c, warm_median_ms=gc_w, warm_iqr_ms=gc_iqr,
                exact_match=True, accelerated=False, soundness_class="NUMERICAL_ORACLE_GCC_O3",
                extra={"iters": int(giters)},
            )
            _rec(
                records, suite="poisson2d_native_scaling", case=f"poisson_{grid}x{grid}_cg_jacobi",
                category="S3_CONVENTIONAL_NATIVE", horizon=n, cold_ms=s3_c, warm_median_ms=s3_w, warm_iqr_ms=s3_iqr,
                compile_cold_ms=poisson_compile_ms, exact_match=(siters == giters and max_err < 1e-10),
                accelerated=False, soundness_class="SCIENTIFIC_50M_BUDGET_VERIFIED",
                speedup_vs_c11_conv_gcc_o3=round(gc_w / s3_w, 3),
                extra={"iters": int(siters), "max_err_vs_gcc": max_err, "s3_gcc_ratio": round(s3_w / gc_w, 2)},
            )

        # AVX2 + FMA Dot Product vs Strict S3 & GCC -O3 (N=16384)
        feats = detect_cpu_features()
        dot_src = """\
export fn dot_f64(a: &[f64], b: &[f64], n: i64) -> f64:
    mut zero: i64 = 0
    mut one: i64 = 1
    mut acc: f64 = 0.0
    mut i: i64 = zero
    while i < n:
        acc = acc + a[i] * b[i]
        i = i + one
    return acc
fn main() -> i64:
    return 0
"""
        dot_strict = compile_source(dot_src, OptimizationLevel.O1, allow_fp_reassociation=False)
        dot_so = tmpd / "s3_dot_strict.so"
        toolchain.build_shared(
            generate_ffi_assembly(dot_strict.require_ordinary_artifacts()[1], max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS),
            dot_so,
        )
        dlib = ctypes.CDLL(str(dot_so))
        dlib.dot_f64.argtypes = [D_PTR, ctypes.c_int64, D_PTR, ctypes.c_int64, ctypes.c_int64]
        dlib.dot_f64.restype = ctypes.c_double
        avx_so, _, isa_name = compile_simd_lib(prefer_avx2=True)
        avx_lib = ctypes.CDLL(str(avx_so))
        avx_lib.s3_simd_dot_f64.argtypes = [D_PTR, D_PTR, ctypes.c_int64]
        avx_lib.s3_simd_dot_f64.restype = ctypes.c_double

        n_dot = 16384
        va = (ctypes.c_double * n_dot)(*[(i % 13) * 0.125 for i in range(n_dot)])
        vb = (ctypes.c_double * n_dot)(*[(i % 7) * 0.25 + 0.5 for i in range(n_dot)])
        gd_v, gd_c, gd_w, _ = _time_fn(lambda: c11_ref.c11_dot_f64(va, vb, n_dot), warmups=2, repeats=9)
        sd_v, sd_c, sd_w, _ = _time_fn(lambda: dlib.dot_f64(va, n_dot, vb, n_dot, n_dot), warmups=2, repeats=9)
        ad_v, ad_c, ad_w, _ = _time_fn(lambda: avx_lib.s3_simd_dot_f64(va, vb, n_dot), warmups=2, repeats=9)
        _rec(records, suite="simd_avx2_fma", case="dot_f64_16384", category="C11_CONVENTIONAL_GCC_O3", horizon=n_dot, cold_ms=gd_c, warm_median_ms=gd_w, exact_match=True, soundness_class="NUMERICAL_ORACLE_GCC_O3")
        _rec(records, suite="simd_avx2_fma", case="dot_f64_16384_strict_s3", category="S3_CONVENTIONAL_NATIVE", horizon=n_dot, cold_ms=sd_c, warm_median_ms=sd_w, exact_match=(abs(sd_v - gd_v) < 1e-8), speedup_vs_c11_conv_gcc_o3=round(gd_w / sd_w, 2), soundness_class="IEEE_STRICT_NO_REASSOC")
        _rec(records, suite="simd_avx2_fma", case=f"dot_f64_16384_{isa_name}", category="S3_PREDICTIVE_NATIVE", horizon=n_dot, cold_ms=ad_c, warm_median_ms=ad_w, exact_match=(abs(ad_v - gd_v) < 1e-8), accelerated=True, speedup_vs_c11_conv_gcc_o3=round(gd_w / ad_w, 2), speedup_vs_s3_conv_native=round(sd_w / ad_w, 2), soundness_class="OPT_IN_SIMD_KERNEL", extra={"cpu_features": feats})

        # ------------------------------------------------------------------
        # 5. Negative Controls & Safety Gate Enforcements
        # ------------------------------------------------------------------
        static_comp = compile_source(_SMALL_STATIC_SRC, optimization=OptimizationLevel.O1, predictive_exact=True)
        static_rep = apply_predictive_native_lowering(compile_source(_SMALL_STATIC_SRC, OptimizationLevel.O1).ir, source_text=_SMALL_STATIC_SRC)
        _rec(
            records, suite="negative_controls", case="static_small_T10_gate", category="NEGATIVE_CONTROL", horizon=10,
            cold_ms=0.0, warm_median_ms=0.0,
            exact_match=("sum_small" not in static_comp.predictive_lowered_functions and "SELECTOR_USE_CONVENTIONAL_STATIC_SMALL_T" in static_rep.skipped_functions.get("sum_small", "")),
            accelerated=False, soundness_class="SELECTOR_GATED_CONVENTIONAL",
        )

        # Runtime fib(92) i64 overflow parity against conventional IRExecutionError/NumericError
        fib92_trapped = False
        try:
            execute_ir(comp_pred.ir, entry="fib", arguments=[92])
        except (NumericError, IRExecutionError):
            fib92_trapped = True
        _rec(
            records, suite="negative_controls", case="fib92_i64_intermediate_overflow_fallback", category="NEGATIVE_CONTROL", horizon=92,
            cold_ms=0.0, warm_median_ms=0.0, exact_match=fib92_trapped, accelerated=False, soundness_class="OVERFLOW_TRAP_PARITY_PRESERVED",
        )

        for neg_fn, neg_args in (("fp_loop", [100, 1]), ("nonlinear_quad", [10, 2])):
            ncert = predictive_verify(comp_conv.ir, neg_fn, arguments=neg_args)
            _rec(
                records, suite="negative_controls", case=f"ir_reject_{neg_fn}", category="NEGATIVE_CONTROL", horizon=neg_args[0],
                cold_ms=0.0, warm_median_ms=0.0, exact_match=(ncert.correctness_class == CorrectnessClass.REJECTED),
                accelerated=False, soundness_class=ncert.correctness_class,
            )

        for bad_rule in (30, 110):
            poly, cert_r = verify_gf2_circulant_and_extract_poly(
                lambda s, rr=bad_rule: _step_periodic_eca(s, rr), 31
            )
            _rec(
                records, suite="negative_controls", case=f"gf2_reject_rule{bad_rule}", category="NEGATIVE_CONTROL", horizon=1,
                cold_ms=0.0, warm_median_ms=0.0,
                exact_match=(
                    poly is None
                    and cert_r.correctness_class == CorrectnessClass.COUNTEREXAMPLE_FOUND
                    and cert_r.counterexample is not None
                    and cert_r.counterexample.get("reason") == "NONLINEAR_OVER_GF2"
                ),
                accelerated=False, soundness_class=cert_r.correctness_class,
            )

        # Cache isolation check: default compilation leaves predictive_exact=False
        iso_cache = CompilationCache()
        def_comp = iso_cache.compile(_IR_BENCH_SRC, optimization=OptimizationLevel.O1)
        _rec(
            records, suite="negative_controls", case="default_predictive_exact_off_isolation", category="NEGATIVE_CONTROL", horizon=0,
            cold_ms=0.0, warm_median_ms=0.0, exact_match=(len(def_comp.predictive_lowered_functions) == 0),
            accelerated=False, soundness_class="DEFAULT_OPT_IN_ISOLATED",
        )

    all_exact = all(bool(r["exact_match"]) for r in records)
    return {
        "campaign": "S3_AUTONOMOUS_DEVELOPMENT_V3",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "s3_git_sha": _git_sha(S3_ROOT),
        "bench_git_sha": _git_sha(BENCH_ROOT),
        "environment": {
            "platform": platform.platform(),
            "python": platform.python_version(),
            "cpu_features": detect_cpu_features(),
            "scientific_max_instructions": SCIENTIFIC_MAX_INSTRUCTIONS,
        },
        "summary": {
            "total_records": len(records),
            "all_exact_match": all_exact,
            "categories": sorted({r["category"] for r in records}),
        },
        "records": records,
    }


def main() -> int:
    report = run_suite()
    out_json = THIS_DIR / "results.json"
    out_csv = THIS_DIR / "results.csv"
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
    assert report["summary"]["all_exact_match"], "One or more parity / negative control checks failed!"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
