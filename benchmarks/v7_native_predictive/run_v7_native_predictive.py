#!/usr/bin/env python3
"""S3 V7 Real Native Predictive Compilation vs Conventional Native vs C11 GCC -O3 Benchmark."""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
import resource
import statistics
import subprocess
import sys
import tempfile
import time

BENCH_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = BENCH_ROOT.parent
S3_ROOT = WORKSPACE_ROOT / "S3"
OUT_DIR = Path(__file__).resolve().parent

if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3 import OptimizationLevel, compile_source
from bootstrap.s3.backends.x86_64 import NativeToolchain, generate_ffi_assembly, generate_native_assembly
from bootstrap.s3.codegen import generate_assembly
from bootstrap.s3.ffi import build_shared_library_from_compilation
from bootstrap.s3.ir_emulator import execute_ir
from bootstrap.s3.lexer import tokenize
from bootstrap.s3.optimizer import optimize_ir
from bootstrap.s3.parser import parse
from bootstrap.s3.predictive_discovery import discover_ir_patterns
from bootstrap.s3.predictive_native_lowering import apply_predictive_native_lowering, clear_all_predictive_caches
from bootstrap.s3.predictive_proof_checker import PredictiveVerificationCache
from bootstrap.s3.semantic import analyze

S3_CORPUS_TEMPLATE = """
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

export fn sum_i2(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 0
    while i < n:
        acc = acc + i * i
        i = i + 1
    return acc

export fn triangular_cubic(n: i64, acc0: i64, s0: i64) -> i64:
    mut i: i64 = 0
    mut s1: i64 = s0
    mut s2: i64 = acc0
    while i < n:
        s1 = s1 + i * i
        s2 = s2 + s1
        i = i + 1
    return s2

export fn sum_quasi_parity(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 5
    while i < n:
        num: i64 = i * i + 3 * i + 1
        acc = acc + (num / 2)
        i = i + 1
    return acc

export fn coupled_exchange(n: i64, x0: i64, y0: i64) -> i64:
    mut i: i64 = 0
    mut x: i64 = x0
    mut y: i64 = y0
    mut total: i64 = 0
    while i < n:
        flux: i64 = x - y + i
        x = x - flux
        y = y + flux
        total = total + x + y
        i = i + 1
    return total

fn main() -> i64:
    return sum_quasi_parity(10000)
"""

C11_CONVENTIONAL_SRC = r"""
#include <stdint.h>

int64_t lcg_mod(int64_t n, int64_t x0, int64_t m) {
    int64_t i = 0;
    int64_t x = x0;
    while (i < n) {
        int64_t nxt = 3 * x + 5;
        x = nxt - (nxt / m) * m;
        i = i + 1;
    }
    return x;
}

int64_t fib_mod(int64_t n, int64_t m) {
    int64_t a = 0, b = 1, i = 0;
    while (i < n) {
        int64_t s = a + b;
        int64_t nb = s - (s / m) * m;
        a = b;
        b = nb;
        i = i + 1;
    }
    return a;
}

int64_t sum_i2(int64_t n) {
    int64_t i = 0, acc = 0;
    while (i < n) {
        acc = acc + i * i;
        i = i + 1;
    }
    return acc;
}

int64_t triangular_cubic(int64_t n, int64_t acc0, int64_t s0) {
    int64_t i = 0, s1 = s0, s2 = acc0;
    while (i < n) {
        s1 = s1 + i * i;
        s2 = s2 + s1;
        i = i + 1;
    }
    return s2;
}

int64_t sum_quasi_parity(int64_t n) {
    int64_t i = 0, acc = 5;
    while (i < n) {
        int64_t num = i * i + 3 * i + 1;
        acc = acc + (num / 2);
        i = i + 1;
    }
    return acc;
}

int64_t coupled_exchange(int64_t n, int64_t x0, int64_t y0) {
    int64_t i = 0, x = x0, y = y0, total = 0;
    while (i < n) {
        int64_t flux = x - y + i;
        x = x - flux;
        y = y + flux;
        total = total + x + y;
        i = i + 1;
    }
    return total;
}
"""

C11_MATH_ACCEL_SRC = r"""
#include <stdint.h>

static int64_t mod_mul(int64_t a, int64_t b, int64_t m) {
    return (int64_t)(((__int128)a * (__int128)b) % (__int128)m);
}

int64_t lcg_mod(int64_t n, int64_t x0, int64_t m) {
    if (n <= 0 || m <= 0 || x0 < 0) {
        int64_t i = 0, x = x0;
        while (i < n) {
            int64_t nxt = 3 * x + 5;
            x = nxt % m;
            i++;
        }
        return x;
    }
    int64_t a_pow = 1, b_acc = 0;
    int64_t ca = 3 % m, cb = 5 % m;
    int64_t e = n;
    while (e > 0) {
        if (e & 1) {
            b_acc = (mod_mul(ca, b_acc, m) + cb) % m;
            a_pow = mod_mul(a_pow, ca, m);
        }
        cb = (mod_mul(ca, cb, m) + cb) % m;
        ca = mod_mul(ca, ca, m);
        e >>= 1;
    }
    return (mod_mul(a_pow, x0 % m, m) + b_acc) % m;
}

int64_t fib_mod(int64_t n, int64_t m) {
    if (n <= 0 || m <= 1) {
        int64_t a = 0, b = 1, i = 0;
        while (i < n) {
            int64_t s = a + b;
            int64_t nb = s - (s / m) * m;
            a = b; b = nb; i++;
        }
        return a;
    }
    int64_t a = 0, b = 1;
    for (int bit = 62; bit >= 0; --bit) {
        if (((n >> bit) == 0)) continue;
        int64_t two_b_a = (2 * b - a + m) % m;
        int64_t c = mod_mul(a, two_b_a, m);
        int64_t d = (mod_mul(a, a, m) + mod_mul(b, b, m)) % m;
        if ((n >> bit) & 1) {
            a = d;
            b = (c + d) % m;
        } else {
            a = c;
            b = d;
        }
    }
    return a;
}

int64_t sum_i2(int64_t n) {
    if (n <= 0) return 0;
    __int128 t = n;
    return (int64_t)((t - 1) * t * (2 * t - 1) / 6);
}

int64_t triangular_cubic(int64_t n, int64_t acc0, int64_t s0) {
    if (n <= 0) return acc0;
    __int128 t = n;
    __int128 b1 = t;
    __int128 b2 = t * (t - 1) / 2;
    __int128 b3 = t * (t - 1) * (t - 2) / 6;
    __int128 b4 = t * (t - 1) * (t - 2) * (t - 3) / 24;
    return (int64_t)((__int128)acc0 + (__int128)s0 * b1 + b2 + 3 * b3 + 2 * b4);
}

int64_t sum_quasi_parity(int64_t n) {
    if (n <= 0) return 5;
    __int128 q = n / 2;
    __int128 r = n & 1;
    __int128 b1 = q, b2 = q * (q - 1) / 2, b3 = q * (q - 1) * (q - 2) / 6;
    __int128 pair_sum = 2 * b1 + 12 * b2 + 8 * b3;
    __int128 rem = r * (2 * q * q + 3 * q);
    return (int64_t)(5 + pair_sum + rem);
}

int64_t coupled_exchange(int64_t n, int64_t x0, int64_t y0) {
    if (n <= 0) return 0;
    __int128 t = n;
    return (int64_t)(t * ((__int128)x0 + (__int128)y0));
}
"""

BENCH_DRIVER_C = r"""
#define _POSIX_C_SOURCE 199309L
#include <dlfcn.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static volatile int64_t g_sink = 0;

int64_t noop_i64(int64_t a) { return a; }

static double now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec * 1e9 + (double)ts.tv_nsec;
}

int main(int argc, char **argv) {
    if (argc < 6) {
        fprintf(stderr, "usage: bench_driver <so_path> <fn_name> <argc_mode> <n> <repeats> [arg2] [arg3]\n");
        return 2;
    }
    const char *so_path = argv[1];
    const char *fn_name = argv[2];
    int argc_mode = atoi(argv[3]);
    int64_t n = strtoll(argv[4], NULL, 10);
    long repeats = atol(argv[5]);
    int64_t a2 = argc > 6 ? strtoll(argv[6], NULL, 10) : 0;
    int64_t a3 = argc > 7 ? strtoll(argv[7], NULL, 10) : 0;

    void *handle = dlopen(so_path, RTLD_NOW);
    if (!handle) {
        fprintf(stderr, "dlopen error: %s\n", dlerror());
        return 3;
    }
    void *sym = dlsym(handle, fn_name);
    if (!sym) {
        fprintf(stderr, "dlsym error: %s\n", dlerror());
        return 4;
    }

    int64_t out = 0;
    double t0 = 0.0, t1 = 0.0;
    if (argc_mode == 1) {
        typedef int64_t (*fn1_t)(int64_t);
        fn1_t fn = (fn1_t)sym;
        out = fn(n);
        t0 = now_ns();
        int64_t acc = 0;
        for (long r = 0; r < repeats; ++r) {
            acc ^= fn(n);
        }
        t1 = now_ns();
        g_sink = acc;
    } else if (argc_mode == 2) {
        typedef int64_t (*fn2_t)(int64_t, int64_t);
        fn2_t fn = (fn2_t)sym;
        out = fn(n, a2);
        t0 = now_ns();
        int64_t acc = 0;
        for (long r = 0; r < repeats; ++r) {
            acc ^= fn(n, a2);
        }
        t1 = now_ns();
        g_sink = acc;
    } else {
        typedef int64_t (*fn3_t)(int64_t, int64_t, int64_t);
        fn3_t fn = (fn3_t)sym;
        out = fn(n, a2, a3);
        t0 = now_ns();
        int64_t acc = 0;
        for (long r = 0; r < repeats; ++r) {
            acc ^= fn(n, a2, a3);
        }
        t1 = now_ns();
        g_sink = acc;
    }
    double total_ns = t1 - t0;
    printf("{\"output\": %lld, \"repeats\": %ld, \"total_ns\": %.3f, \"per_call_us\": %.6f}\n",
           (long long)out, repeats, total_ns, (total_ns / (double)repeats) / 1000.0);
    dlclose(handle);
    return 0;
}
"""

WORKLOADS = [
    ("sum_quasi_parity", 1, [], [1, 2, 5, 10, 100, 1000, 10000, 100000, 1000000]),
    ("sum_i2", 1, [], [1, 2, 5, 10, 100, 1000, 10000, 100000, 1000000]),
    ("lcg_mod", 3, [7, 1000000007], [1, 2, 5, 10, 100, 1000, 10000, 100000, 1000000]),
    ("fib_mod", 2, [1000000007], [1, 2, 5, 10, 100, 1000, 10000, 100000, 1000000]),
    ("triangular_cubic", 3, [13, -7], [1, 2, 5, 10, 100, 1000, 10000]),
    ("coupled_exchange", 3, [10, -3], [1, 2, 5, 10, 100, 1000, 10000, 100000, 1000000]),
]


def _iqr(xs: list[float]) -> float:
    s = sorted(xs)
    q1 = s[len(s) // 4]
    q3 = s[(3 * len(s)) // 4]
    return q3 - q1


def _calibrate_repeats(driver: Path, so_path: Path, fn_name: str, argc_mode: int, n: int, extra_args: list[int], target_ms: float = 5.0) -> tuple[int, int]:
    base_cmd = [str(driver), str(so_path), fn_name, str(argc_mode), str(n)]
    tail = [str(x) for x in extra_args]
    probe_reps = "2" if n >= 10000 else "50"
    calib = json.loads(subprocess.check_output(base_cmd + [probe_reps] + tail, text=True))
    per_us = max(calib["per_call_us"], 0.002)
    repeats = max(5, min(2_000_000, int((target_ms * 1000.0) / per_us)))
    return int(calib["output"]), repeats


def _run_c_fixed_repeats(driver: Path, so_path: Path, fn_name: str, argc_mode: int, n: int, extra_args: list[int], repeats: int) -> tuple[int, float]:
    cmd = [str(driver), str(so_path), fn_name, str(argc_mode), str(n), str(repeats)] + [str(x) for x in extra_args]
    res = json.loads(subprocess.check_output(cmd, text=True))
    return int(res["output"]), float(res["per_call_us"])


def _measure_cold_breakdown(work_dir: Path) -> dict[str, object]:
    """Run an isolated subprocess with clean caches to capture cold timings & RSS."""
    script = f"""
import json, os, pathlib, resource, sys, tempfile, time
sys.path.insert(0, {str(S3_ROOT)!r})
os.environ["S3_FFI_CACHE_DIR"] = {str(work_dir / 'cold_ffi_cache')!r}
os.environ["S3_NATIVE_CACHE_DIR"] = {str(work_dir / 'cold_elf_cache')!r}
from bootstrap.s3 import OptimizationLevel, compile_source
from bootstrap.s3.backends.x86_64 import NativeToolchain, generate_ffi_assembly, generate_native_assembly
from bootstrap.s3.codegen import generate_assembly
from bootstrap.s3.lowering import lower
from bootstrap.s3.optimizer import optimize_ir
from bootstrap.s3.parser import parse
from bootstrap.s3.predictive_discovery import discover_ir_patterns
from bootstrap.s3.predictive_native_lowering import apply_predictive_native_lowering, clear_all_predictive_caches
from bootstrap.s3.semantic import analyze

src = {S3_CORPUS_TEMPLATE!r}
clear_all_predictive_caches()

t0 = time.perf_counter()
ast = parse(src)
sem = analyze(ast)
ir0 = lower(ast, sem)
ir_opt = optimize_ir(ir0, OptimizationLevel.O1, allow_fp_reassociation=False)
t_frontend = (time.perf_counter() - t0) * 1000.0

t0 = time.perf_counter()
disc_rep = discover_ir_patterns(ir_opt, run_empirical_probes=False, allow_quasi_polynomial_parity=True)
t_disc = (time.perf_counter() - t0) * 1000.0

t0 = time.perf_counter()
low_nocheck = apply_predictive_native_lowering(
    ir_opt, source_text=src, use_cache=False, verify_with_checker=False, allow_quasi_polynomial_parity=True
)
t_cert_lower = (time.perf_counter() - t0) * 1000.0

t0 = time.perf_counter()
low_checked = apply_predictive_native_lowering(
    ir_opt, source_text=src, use_cache=False, verify_with_checker=True, allow_quasi_polynomial_parity=True
)
t_checker_total = (time.perf_counter() - t0) * 1000.0
t_proof_checker = max(0.0, t_checker_total - t_cert_lower)

t0 = time.perf_counter()
asm_prog = generate_assembly(low_checked.module)
ffi_asm = generate_ffi_assembly(asm_prog, max_instructions=50_000_000)
t_asm = (time.perf_counter() - t0) * 1000.0

tc = NativeToolchain.detect()
t0 = time.perf_counter()
so_p = tc.build_shared(ffi_asm, pathlib.Path({str(work_dir)!r}) / 'cold_pred.so')
t_link = (time.perf_counter() - t0) * 1000.0

# Also measure conventional S3 cold compile+asm+link + ELF footprint
t0 = time.perf_counter()
c_conv = compile_source(src, OptimizationLevel.O1, predictive_exact=False)
asm_conv = generate_ffi_assembly(c_conv.assembly, max_instructions=50_000_000)
so_c = tc.build_shared(asm_conv, pathlib.Path({str(work_dir)!r}) / 'cold_conv.so')
t_conv_cold = (time.perf_counter() - t0) * 1000.0

elf_c = tc.build(generate_native_assembly(c_conv.assembly, max_instructions=50_000_000), pathlib.Path({str(work_dir)!r}) / 'cold_conv_elf')
elf_p = tc.build(generate_native_assembly(generate_assembly(low_checked.module), max_instructions=50_000_000), pathlib.Path({str(work_dir)!r}) / 'cold_pred_elf')

# Warm IR emulator reference for sum_quasi_parity(10000) (V6 metric reproduction check)
from bootstrap.s3.ir_emulator import execute_ir
t0 = time.perf_counter()
execute_ir(ir_opt, entry='sum_quasi_parity', arguments=[10000])
ir_conv_ms = (time.perf_counter() - t0) * 1000.0
t0 = time.perf_counter()
execute_ir(low_checked.module, entry='sum_quasi_parity', arguments=[10000])
ir_pred_ms = (time.perf_counter() - t0) * 1000.0

rss_kb = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print(json.dumps({{
    'FRONTEND_IR_OPT_MS': round(t_frontend, 3),
    'DISCOVERY_MS': round(t_disc, 3),
    'CERTIFICATE_GENERATION_MS': round(t_cert_lower, 3),
    'PROOF_CHECKER_MS': round(t_proof_checker, 3),
    'COMPILER_MS': round(t_frontend + t_checker_total, 3),
    'ASSEMBLY_MS': round(t_asm, 3),
    'LINK_MS': round(t_link, 3),
    'COLD_END_TO_END_MS': round(t_frontend + t_checker_total + t_asm + t_link, 3),
    'CONV_COLD_END_TO_END_MS': round(t_conv_cold, 3),
    'PEAK_RSS_KB': rss_kb,
    'so_pred_bytes': so_p.stat().st_size,
    'so_conv_bytes': so_c.stat().st_size,
    'elf_pred_bytes': elf_p.stat().st_size,
    'elf_conv_bytes': elf_c.stat().st_size,
    'lowered_functions': list(low_checked.lowered_functions),
    'v6_ir_emulator_quasi_10000': {{
        'conv_ir_ms': round(ir_conv_ms, 4),
        'pred_ir_ms': round(ir_pred_ms, 4),
        'ir_speedup': round(ir_conv_ms / max(ir_pred_ms, 1e-6), 2),
    }},
}}))
"""
    raw = subprocess.check_output([sys.executable, "-c", script], text=True)
    return json.loads(raw)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="s3-v7-native-bench-") as td:
        tdp = Path(td)
        cold_info = _measure_cold_breakdown(tdp / "cold")

        # Build clean warm shared libraries & C11 benchmarks
        c_conv = compile_source(S3_CORPUS_TEMPLATE, OptimizationLevel.O1, predictive_exact=False)
        c_pred = compile_source(S3_CORPUS_TEMPLATE, OptimizationLevel.O1, predictive_exact=True)
        so_s3_conv = build_shared_library_from_compilation(c_conv, tdp / "s3_conv.so", max_instructions=50_000_000)
        so_s3_pred = build_shared_library_from_compilation(c_pred, tdp / "s3_pred.so", max_instructions=50_000_000)

        c_conv_src = tdp / "c_conv.c"
        c_math_src = tdp / "c_math.c"
        drv_src = tdp / "bench_driver.c"
        c_conv_src.write_text(C11_CONVENTIONAL_SRC, encoding="utf-8")
        c_math_src.write_text(C11_MATH_ACCEL_SRC, encoding="utf-8")
        drv_src.write_text(BENCH_DRIVER_C, encoding="utf-8")

        so_c_conv = tdp / "c11_conv.so"
        so_c_math = tdp / "c11_math.so"
        driver_bin = tdp / "bench_driver"

        subprocess.run(["gcc", "-O3", "-shared", "-fPIC", str(c_conv_src), "-o", str(so_c_conv)], check=True)
        subprocess.run(["gcc", "-O3", "-shared", "-fPIC", str(c_math_src), "-o", str(so_c_math)], check=True)
        subprocess.run(["gcc", "-O3", str(drv_src), "-ldl", "-o", str(driver_bin)], check=True)

        # Inspect GCC -O3 disassembly of c11_conv sum_i2 vs sum_quasi_parity to detect GCC closed-form SCEV!
        objdump = subprocess.check_output(["objdump", "-d", str(so_c_conv)], text=True)
        gcc_notes = {}
        for fn in ("sum_i2", "sum_quasi_parity", "lcg_mod", "fib_mod", "triangular_cubic", "coupled_exchange"):
            idx = objdump.find(f"<{fn}>:")
            chunk = objdump[idx : idx + 1200] if idx != -1 else ""
            has_backward_jmp = ("<" + fn + "+") in chunk and any(
                line for line in chunk.splitlines() if "\tj" in line
            )
            gcc_notes[fn] = "KEEP_LOOP_OR_BRANCH" if has_backward_jmp else "CLOSED_FORM_OR_NO_LOOP"

        modes = [
            ("S3_CONVENTIONAL_NATIVE", so_s3_conv),
            ("S3_PREDICTIVE_NATIVE", so_s3_pred),
            ("C11_CONVENTIONAL_GCC_O3", so_c_conv),
            ("C11_MATHEMATICAL_ACCELERATED_GCC_O3", so_c_math),
        ]

        trials = 11
        sweep_rows = []
        breakeven_summary = {}

        for fn_name, argc_mode, extra_args, t_list in WORKLOADS:
            fn_cross_t = None
            for t in t_list:
                samples: dict[str, list[float]] = {m: [] for m, _ in modes}
                outputs: dict[str, int] = {}
                mode_repeats: dict[str, int] = {}
                # Verify once & calibrate repeats once per (workload, mode, T)
                for m_name, so_p in modes:
                    out_v, reps = _calibrate_repeats(driver_bin, so_p, fn_name, argc_mode, t, extra_args, target_ms=5.0)
                    outputs[m_name] = out_v
                    mode_repeats[m_name] = reps
                assert len(set(outputs.values())) == 1, f"Parity mismatch on {fn_name}({t}): {outputs}"

                # Alternating trials
                for tr in range(trials):
                    order = modes if (tr % 2 == 0) else list(reversed(modes))
                    for m_name, so_p in order:
                        _, per_us = _run_c_fixed_repeats(
                            driver_bin, so_p, fn_name, argc_mode, t, extra_args, mode_repeats[m_name]
                        )
                        samples[m_name].append(per_us)

                stats_by_mode = {}
                for m_name, _ in modes:
                    xs = samples[m_name]
                    stats_by_mode[m_name] = {
                        "median_us": round(statistics.median(xs), 6),
                        "iqr_us": round(_iqr(xs), 6),
                        "min_us": round(min(xs), 6),
                        "max_us": round(max(xs), 6),
                    }

                s3_conv_med = stats_by_mode["S3_CONVENTIONAL_NATIVE"]["median_us"]
                s3_pred_med = stats_by_mode["S3_PREDICTIVE_NATIVE"]["median_us"]
                c11_conv_med = stats_by_mode["C11_CONVENTIONAL_GCC_O3"]["median_us"]
                c11_math_med = stats_by_mode["C11_MATHEMATICAL_ACCELERATED_GCC_O3"]["median_us"]
                sp_vs_s3_conv = round(s3_conv_med / max(s3_pred_med, 1e-9), 3)
                sp_vs_c11_conv = round(c11_conv_med / max(s3_pred_med, 1e-9), 3)
                ratio_vs_c11_math = round(s3_pred_med / max(c11_math_med, 1e-9), 3)
                if fn_cross_t is None and s3_pred_med < s3_conv_med:
                    fn_cross_t = t

                sweep_rows.append({
                    "workload": fn_name,
                    "T": t,
                    "exact_output": outputs["S3_CONVENTIONAL_NATIVE"],
                    "modes": stats_by_mode,
                    "s3_pred_speedup_vs_s3_conv": sp_vs_s3_conv,
                    "s3_pred_speedup_vs_c11_conv_gcc_o3": sp_vs_c11_conv,
                    "s3_pred_ratio_vs_c11_math_gcc_o3": ratio_vs_c11_math,
                })

            max_t_row = [r for r in sweep_rows if r["workload"] == fn_name][-1]
            savings_per_call_ms = (
                max_t_row["modes"]["S3_CONVENTIONAL_NATIVE"]["median_us"]
                - max_t_row["modes"]["S3_PREDICTIVE_NATIVE"]["median_us"]
            ) / 1000.0
            cold_overhead_delta_ms = max(0.0, cold_info["COLD_END_TO_END_MS"] - cold_info["CONV_COLD_END_TO_END_MS"])
            amort_calls_at_max_t = (
                math.ceil(cold_overhead_delta_ms / savings_per_call_ms)
                if savings_per_call_ms > 0
                else None
            )
            breakeven_summary[fn_name] = {
                "warm_crossover_T": fn_cross_t,
                "max_T_tested": max_t_row["T"],
                "max_T_speedup_vs_s3_conv": max_t_row["s3_pred_speedup_vs_s3_conv"],
                "max_T_speedup_vs_c11_conv_gcc_o3": max_t_row["s3_pred_speedup_vs_c11_conv_gcc_o3"],
                "cold_overhead_delta_ms": round(cold_overhead_delta_ms, 3),
                "cold_amortized_calls_at_max_T": amort_calls_at_max_t,
            }

        quasi_10k = next(r for r in sweep_rows if r["workload"] == "sum_quasi_parity" and r["T"] == 10000)
        payload = {
            "campaign": "S3_V7_NATIVE_INTELLIGENCE_AND_COMPILER_SUPREMACY",
            "wave": "WAVE_01_04_REAL_NATIVE_PREDICTIVE_BENCHMARK",
            "gcc_version": subprocess.check_output(["gcc", "--version"], text=True).splitlines()[0],
            "cold_compilation_breakdown": cold_info,
            "binary_sizes_bytes": {
                "s3_conv_so": so_s3_conv.stat().st_size,
                "s3_pred_so": so_s3_pred.stat().st_size,
                "c11_conv_so": so_c_conv.stat().st_size,
                "c11_math_so": so_c_math.stat().st_size,
                "s3_conv_elf": cold_info["elf_conv_bytes"],
                "s3_pred_elf": cold_info["elf_pred_bytes"],
            },
            "gcc_o3_loop_observations": gcc_notes,
            "v6_873x_ir_claim_vs_v7_native_reality_at_T10000": {
                "v6_claimed_ir_emulator_speedup": 873.0,
                "v7_reproduced_ir_emulator": cold_info["v6_ir_emulator_quasi_10000"],
                "v7_real_native_s3_conv_us": quasi_10k["modes"]["S3_CONVENTIONAL_NATIVE"]["median_us"],
                "v7_real_native_s3_pred_us": quasi_10k["modes"]["S3_PREDICTIVE_NATIVE"]["median_us"],
                "v7_real_native_c11_conv_us": quasi_10k["modes"]["C11_CONVENTIONAL_GCC_O3"]["median_us"],
                "v7_real_native_c11_math_us": quasi_10k["modes"]["C11_MATHEMATICAL_ACCELERATED_GCC_O3"]["median_us"],
                "v7_real_native_speedup_vs_s3_conv": quasi_10k["s3_pred_speedup_vs_s3_conv"],
                "v7_real_native_speedup_vs_c11_conv": quasi_10k["s3_pred_speedup_vs_c11_conv_gcc_o3"],
            },
            "breakeven_summary": breakeven_summary,
            "sweep": sweep_rows,
        }
        out_path = OUT_DIR / "results_v7_native_predictive.json"
        out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print("Wrote", out_path)
        print("V6 873x vs V7 native reality (T=10000 sum_quasi_parity):")
        print(json.dumps(payload["v6_873x_ir_claim_vs_v7_native_reality_at_T10000"], indent=2))
        print("Cold breakdown:")
        print(json.dumps(cold_info, indent=2))
        print("Breakeven summary:")
        print(json.dumps(breakeven_summary, indent=2))


if __name__ == "__main__":
    main()
