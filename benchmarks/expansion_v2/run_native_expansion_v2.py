#!/usr/bin/env python3
"""
S3 Scientific Expansion V2 — Current Native Linux x86-64 Benchmark Suite
Campaign: S3_SCIENTIFIC_EXPANSION_V2 (Phase P1)
Repository: SamDevlab/S3-Benchmarks
Branch: research/s3-scientific-expansion-v2

Executes CURRENT_NATIVE Linux x86-64 benchmarks (warmups=3, samples=9) for:
  1. JSMN (Small, Medium, Large JSON corpora: S3 O0/O1/PER_INSTRUCTION/EXACT_SEGMENT/PURE_EXPERIMENTAL vs GCC -O2/-O3 vs Python)
  2. RMSD & Vector Similarity (Scales 64, 256, 1024, 8192 + standalone similarity_distance.s3 ELF)
  3. Real Stencil 2D (S3 Compute 5-point stencil: 64x40, 128x80, 256x160 x 10 generations, inline vs helper)
  4. Complementary Control Kernels:
     - GEMM_I64 (Dense 32x32 i64 matrix multiplication)
     - RULE110_CA (1D cellular automaton 256 cells x 128 generations)
     - FNV1A_HASH (Rolling modular hash over 4096 i64 words x 10 passes)
"""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import math
import os
import platform
import re
import resource
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


def resolve_repository_roots() -> tuple[Path, Path]:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--s3-repo", default=os.environ.get("S3_REPO_DIR"))
    parser.add_argument("--benchmarks-repo", default=os.environ.get("S3_BENCHMARKS_DIR"))
    args, _ = parser.parse_known_args()

    benchmarks_dir = (
        Path(args.benchmarks_repo).resolve()
        if args.benchmarks_repo
        else Path(__file__).resolve().parent.parent.parent
    )
    if args.s3_repo:
        s3_dir = Path(args.s3_repo).resolve()
    else:
        sibling_s3 = benchmarks_dir.parent / "S3"
        s3_dir = sibling_s3.resolve() if sibling_s3.exists() else benchmarks_dir
    return benchmarks_dir, s3_dir


S3_BENCHMARKS_DIR, S3_REPO_DIR = resolve_repository_roots()
if str(S3_BENCHMARKS_DIR) not in sys.path:
    sys.path.insert(0, str(S3_BENCHMARKS_DIR))
if str(S3_REPO_DIR) not in sys.path:
    sys.path.insert(0, str(S3_REPO_DIR))

import benchmarks
if str(S3_REPO_DIR / "benchmarks") not in benchmarks.__path__:
    benchmarks.__path__.append(str(S3_REPO_DIR / "benchmarks"))

from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
from bootstrap.s3.pipeline import compile_source

WARMUPS = 3
SAMPLES = 9


def get_git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:
        return "UNKNOWN"


def get_peak_rss_kib() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def get_text_size(binary_path: Path) -> int:
    try:
        out = subprocess.check_output(
            ["objdump", "-h", str(binary_path)], text=True
        )
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[1] == ".text":
                return int(parts[2], 16)
    except Exception:
        pass
    return 0


def strip_budget_for_pure_experimental(asm: str) -> str:
    """Remove per-instruction r15 budget decrement/jump to isolate pure S3 codegen."""
    lines = []
    for line in asm.splitlines():
        stripped = line.strip()
        if stripped == "dec r15" or (
            stripped.startswith("js .L__s3_failure_site_") and lines and lines[-1].startswith("    # budget_elided")
        ):
            lines.append("    # budget_elided")
            continue
        lines.append(line)
    # Remove marker comments
    return "\n".join(l for l in lines if l != "    # budget_elided") + "\n"


def compute_stats(samples_ns: list[float]) -> dict[str, float]:
    ordered = sorted(samples_ns)
    return {
        "samples": len(samples_ns),
        "warmups": WARMUPS,
        "median_ns": float(statistics.median(ordered)),
        "mean_ns": float(statistics.fmean(ordered)),
        "min_ns": float(ordered[0]),
        "max_ns": float(ordered[-1]),
        "stddev_ns": float(statistics.pstdev(ordered)),
    }


def compile_s3_shared(
    source: str,
    tmp_dir: Path,
    stem: str,
    optimization: str,
    mode: str,
) -> tuple[Path, dict[str, Any]]:
    t0 = time.perf_counter_ns()
    comp = compile_source(source, optimization=optimization)
    budget_mode = "exact-segment" if mode == "EXACT_SEGMENT" else "per-instruction"
    asm = X8664Backend(
        max_instructions=2_000_000_000,
        register_allocation=True,
        instruction_budget_mode=budget_mode,
    )._generate_ffi(comp.assembly)
    if mode == "PURE_EXPERIMENTAL":
        asm = strip_budget_for_pure_experimental(asm)
    s_path = tmp_dir / f"{stem}.s"
    so_path = tmp_dir / f"{stem}.so"
    s_path.write_text(asm, encoding="utf-8")
    subprocess.run(
        ["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)],
        check=True,
    )
    compile_ns = time.perf_counter_ns() - t0
    return so_path, {
        "compile_ns": compile_ns,
        "binary_bytes": so_path.stat().st_size,
        "text_bytes": get_text_size(so_path),
        "asm_lines": len(asm.splitlines()),
    }


def compile_c_shared(
    c_source: str,
    tmp_dir: Path,
    stem: str,
    opt_flag: str = "-O2",
    extra_include: Path | None = None,
) -> tuple[Path, dict[str, Any]]:
    c_path = tmp_dir / f"{stem}.c"
    so_path = tmp_dir / f"{stem}.so"
    c_path.write_text(c_source, encoding="utf-8")
    cmd = ["gcc", "-shared", "-fPIC", opt_flag, "-fno-fast-math", "-std=c11"]
    if extra_include is not None:
        cmd.extend(["-I", str(extra_include)])
    cmd.extend([str(c_path), "-lm", "-o", str(so_path)])
    t0 = time.perf_counter_ns()
    subprocess.run(cmd, check=True)
    compile_ns = time.perf_counter_ns() - t0
    return so_path, {
        "compile_ns": compile_ns,
        "binary_bytes": so_path.stat().st_size,
        "text_bytes": get_text_size(so_path),
    }


# ============================================================================
# 1. JSMN NATIVE BENCHMARK (SMALL, MEDIUM, LARGE CORPORA)
# ============================================================================

S3_JSMN_SLICE_SOURCE = """\
export fn jsmn_scan_tokens(
    input: &[i64],
    length: i64,
    out_meta: &mut [i64]
) -> i64:
    mut n: i64 = len(input)
    mut out_cap: i64 = len(out_meta)
    match n < length:
        -1:
            return -1
        0:
            match out_cap < 2:
                -1:
                    return -1
                0:
                    mut pos: i64 = 0
                    mut tokens: i64 = 0
                    mut checksum: i64 = 0
                    mut depth: i64 = 0
                    mut one: i64 = 1
                    while pos < length:
                        mut ch: i64 = input[pos]
                        match ch == 123:
                            -1:
                                tokens = tokens + one
                                depth = depth + one
                                checksum = checksum + 1 + pos
                                pos = pos + one
                            0:
                                match ch == 91:
                                    -1:
                                        tokens = tokens + one
                                        depth = depth + one
                                        checksum = checksum + 2 + pos
                                        pos = pos + one
                                    0:
                                        match ch == 125:
                                            -1:
                                                depth = depth - one
                                                checksum = checksum + pos + one
                                                pos = pos + one
                                            0:
                                                match ch == 93:
                                                    -1:
                                                        depth = depth - one
                                                        checksum = checksum + pos + one
                                                        pos = pos + one
                                                    0:
                                                        match ch == 34:
                                                            -1:
                                                                mut s_start: i64 = pos + one
                                                                pos = pos + one
                                                                mut in_str: i64 = 1
                                                                while in_str == 1:
                                                                    match pos < length:
                                                                        -1:
                                                                            mut sc: i64 = input[pos]
                                                                            match sc == 34:
                                                                                -1:
                                                                                    in_str = 0
                                                                                0:
                                                                                    match sc == 92:
                                                                                        -1:
                                                                                            pos = pos + 2
                                                                                        0:
                                                                                            pos = pos + one
                                                                                        1:
                                                                                            pos = pos + one
                                                                                1:
                                                                                    in_str = 0
                                                                        0:
                                                                            return -3
                                                                        1:
                                                                            return -3
                                                                tokens = tokens + one
                                                                checksum = checksum + 4 + s_start + pos
                                                                pos = pos + one
                                                            0:
                                                                match ch > 32:
                                                                    -1:
                                                                        match ch == 58:
                                                                            -1:
                                                                                pos = pos + one
                                                                            0:
                                                                                match ch == 44:
                                                                                    -1:
                                                                                        pos = pos + one
                                                                                    0:
                                                                                        mut start: i64 = pos
                                                                                        mut scanning: i64 = 1
                                                                                        while scanning == 1:
                                                                                            match pos < length:
                                                                                                -1:
                                                                                                    mut c2: i64 = input[pos]
                                                                                                    match c2 <= 32:
                                                                                                        -1:
                                                                                                            scanning = 0
                                                                                                        0:
                                                                                                            match c2 == 44:
                                                                                                                -1:
                                                                                                                    scanning = 0
                                                                                                                0:
                                                                                                                    match c2 == 58:
                                                                                                                        -1:
                                                                                                                            scanning = 0
                                                                                                                        0:
                                                                                                                            match c2 == 93:
                                                                                                                                -1:
                                                                                                                                    scanning = 0
                                                                                                                                0:
                                                                                                                                    match c2 == 125:
                                                                                                                                        -1:
                                                                                                                                            scanning = 0
                                                                                                                                        0:
                                                                                                                                            pos = pos + one
                                                                                                                                        1:
                                                                                                                                            pos = pos + one
                                                                                                                                1:
                                                                                                                                    scanning = 0
                                                                                                                        1:
                                                                                                                            scanning = 0
                                                                                                                1:
                                                                                                                    scanning = 0
                                                                                                        1:
                                                                                                            scanning = 0
                                                                                                0:
                                                                                                    scanning = 0
                                                                                                1:
                                                                                                    scanning = 0
                                                                                        tokens = tokens + one
                                                                                        checksum = checksum + 8 + start + pos
                                                                                    1:
                                                                                        pos = pos + one
                                                                            1:
                                                                                pos = pos + one
                                                                    0:
                                                                        pos = pos + one
                                                                    1:
                                                                        pos = pos + one
                                                            1:
                                                                pos = pos + one
                                                    1:
                                                        pos = pos + one
                                            1:
                                                pos = pos + one
                                    1:
                                        pos = pos + one
                            1:
                                pos = pos + one
                    match depth == 0:
                        -1:
                            out_meta[0] = tokens
                            out_meta[1] = checksum
                            return tokens
                        0:
                            return -3
                        1:
                            return -3
                1:
                    return -1
        1:
            return -1

fn main() -> i64:
    return 0
"""

C_JSMN_SCAN_SOURCE = """\
#include <stdint.h>

int64_t jsmn_scan_tokens(const int64_t *input, int64_t n, int64_t length, int64_t *out_meta, int64_t out_cap) {
    if (n < length || out_cap < 2) return -1;
    int64_t pos = 0, tokens = 0, checksum = 0, depth = 0;
    while (pos < length) {
        int64_t ch = input[pos];
        if (ch == 123) {
            tokens++; depth++; checksum += 1 + pos; pos++;
        } else if (ch == 91) {
            tokens++; depth++; checksum += 2 + pos; pos++;
        } else if (ch == 125 || ch == 93) {
            depth--; checksum += pos + 1; pos++;
        } else if (ch == 34) {
            int64_t s_start = pos + 1;
            pos++;
            int in_str = 1;
            while (in_str) {
                if (pos >= length) return -3;
                int64_t sc = input[pos];
                if (sc == 34) { in_str = 0; }
                else if (sc == 92) { pos += 2; }
                else { pos++; }
            }
            tokens++; checksum += 4 + s_start + pos; pos++;
        } else if (ch > 32) {
            if (ch == 58 || ch == 44) {
                pos++;
            } else {
                int64_t start = pos;
                while (pos < length) {
                    int64_t c2 = input[pos];
                    if (c2 <= 32 || c2 == 44 || c2 == 58 || c2 == 93 || c2 == 125) break;
                    pos++;
                }
                tokens++; checksum += 8 + start + pos;
            }
        } else {
            pos++;
        }
    }
    if (depth != 0) return -3;
    out_meta[0] = tokens;
    out_meta[1] = checksum;
    return tokens;
}
"""


def py_jsmn_scan_tokens(input_arr: list[int], length: int) -> tuple[int, int]:
    pos = 0
    tokens = 0
    checksum = 0
    depth = 0
    while pos < length:
        ch = input_arr[pos]
        if ch == 123:
            tokens += 1; depth += 1; checksum += 1 + pos; pos += 1
        elif ch == 91:
            tokens += 1; depth += 1; checksum += 2 + pos; pos += 1
        elif ch == 125 or ch == 93:
            depth -= 1; checksum += pos + 1; pos += 1
        elif ch == 34:
            s_start = pos + 1
            pos += 1
            while True:
                if pos >= length:
                    return -3, 0
                sc = input_arr[pos]
                if sc == 34:
                    break
                elif sc == 92:
                    pos += 2
                else:
                    pos += 1
            tokens += 1; checksum += 4 + s_start + pos; pos += 1
        elif ch > 32:
            if ch == 58 or ch == 44:
                pos += 1
            else:
                start = pos
                while pos < length:
                    c2 = input_arr[pos]
                    if c2 <= 32 or c2 in (44, 58, 93, 125):
                        break
                    pos += 1
                tokens += 1; checksum += 8 + start + pos
        else:
            pos += 1
    if depth != 0:
        return -3, 0
    return tokens, checksum


def run_jsmn_benchmarks(tmp_dir: Path) -> dict[str, Any]:
    print("[P1.1] Running JSMN Native Benchmarks (Small, Medium, Large)...")
    corpora = {
        "small": '{"name":"s3","id":100,"active":true,"tags":["a","b"]}',
        "medium": json.dumps({
            "service": "s3-telemetry",
            "version": 18,
            "nodes": [
                {"id": i, "ok": True, "load": i * 17, "label": f"node_{i}"}
                for i in range(6)
            ],
        }, separators=(",", ":")),
        "large": json.dumps({
            "cluster": "samdev-prod",
            "epoch": 20261112,
            "records": [
                {"seq": i, "status": "READY", "metrics": [i, i * 2, i * 3], "valid": True}
                for i in range(24)
            ],
        }, separators=(",", ":")),
    }

    s3_variants = {}
    for opt, mode, label in [
        ("O0", "PER_INSTRUCTION", "s3_o0_per_instruction"),
        ("O1", "PER_INSTRUCTION", "s3_o1_per_instruction"),
        ("O1", "EXACT_SEGMENT", "s3_o1_exact_segment"),
        ("O1", "PURE_EXPERIMENTAL", "s3_o1_pure_experimental"),
    ]:
        so, meta = compile_s3_shared(S3_JSMN_SLICE_SOURCE, tmp_dir, f"jsmn_{label}", opt, mode)
        lib = ctypes.CDLL(str(so))
        fn = lib.jsmn_scan_tokens
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64]
        fn.restype = ctypes.c_int64
        s3_variants[label] = (fn, meta)

    c_variants = {}
    for flag, label in [("-O2", "gcc_o2"), ("-O3", "gcc_o3")]:
        so, meta = compile_c_shared(C_JSMN_SCAN_SOURCE, tmp_dir, f"jsmn_{label}", flag)
        lib = ctypes.CDLL(str(so))
        fn = lib.jsmn_scan_tokens
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64]
        fn.restype = ctypes.c_int64
        c_variants[label] = (fn, meta)

    results_by_corpus = {}
    for cname, text in corpora.items():
        raw_bytes = [b for b in text.encode("ascii")]
        n = len(raw_bytes)
        c_in = (ctypes.c_int64 * n)(*raw_bytes)
        c_out = (ctypes.c_int64 * 2)(0, 0)

        py_tok, py_chk = py_jsmn_scan_tokens(raw_bytes, n)
        assert py_tok > 0

        corpus_entry: dict[str, Any] = {
            "corpus": cname,
            "input_bytes": n,
            "expected_tokens": py_tok,
            "expected_checksum": py_chk,
            "implementations": {},
        }

        for label, (fn, meta) in {**s3_variants, **c_variants}.items():
            for _ in range(WARMUPS):
                rc = fn(c_in, n, n, c_out, 2)
                assert rc == py_tok and c_out[0] == py_tok and c_out[1] == py_chk
            samples = []
            for _ in range(SAMPLES):
                t0 = time.perf_counter_ns()
                rc = fn(c_in, n, n, c_out, 2)
                t1 = time.perf_counter_ns()
                assert rc == py_tok
                samples.append(float(t1 - t0))
            st = compute_stats(samples)
            mb_s = (n / (1024.0 * 1024.0)) / (st["median_ns"] / 1e9)
            corpus_entry["implementations"][label] = {
                "classification": "CURRENT_NATIVE",
                "parity_pass": True,
                "tokens": int(c_out[0]),
                "checksum": int(c_out[1]),
                "mb_per_sec": round(mb_s, 2),
                **st,
                **meta,
            }

        # Python timing
        for _ in range(WARMUPS):
            py_jsmn_scan_tokens(raw_bytes, n)
        py_samples = []
        for _ in range(SAMPLES):
            t0 = time.perf_counter_ns()
            tok, chk = py_jsmn_scan_tokens(raw_bytes, n)
            t1 = time.perf_counter_ns()
            assert tok == py_tok and chk == py_chk
            py_samples.append(float(t1 - t0))
        py_st = compute_stats(py_samples)
        py_mb_s = (n / (1024.0 * 1024.0)) / (py_st["median_ns"] / 1e9)
        corpus_entry["implementations"]["python_3_12"] = {
            "classification": "CURRENT_NATIVE",
            "parity_pass": True,
            "tokens": py_tok,
            "checksum": py_chk,
            "mb_per_sec": round(py_mb_s, 2),
            **py_st,
        }
        results_by_corpus[cname] = corpus_entry

    return results_by_corpus


# ============================================================================
# 2. RMSD & VECTOR SIMILARITY NATIVE BENCHMARK
# ============================================================================

S3_RMSD_KERNEL_SOURCE = """\
export fn rmsd_metrics_step(
    left: &[f64],
    right: &[f64],
    length: i64,
    out_metrics: &mut [f64]
) -> i64:
    mut n_left: i64 = len(left)
    mut n_right: i64 = len(right)
    mut n_out: i64 = len(out_metrics)
    match length < 1:
        -1:
            return 1
        0:
            match n_left < length:
                -1:
                    return 2
                0:
                    match n_right < length:
                        -1:
                            return 2
                        0:
                            match n_out < 3:
                                -1:
                                    return 3
                                0:
                                    mut i: i64 = 0
                                    mut one: i64 = 1
                                    mut sq_sum: f64 = 0.0
                                    mut dot_sum: f64 = 0.0
                                    mut l_norm: f64 = 0.0
                                    while i < length:
                                        mut a: f64 = left[i]
                                        mut b: f64 = right[i]
                                        mut diff: f64 = a - b
                                        sq_sum = sq_sum + diff * diff
                                        dot_sum = dot_sum + a * b
                                        l_norm = l_norm + a * a
                                        i = i + one
                                    out_metrics[0] = sq_sum
                                    out_metrics[1] = dot_sum
                                    out_metrics[2] = l_norm
                                    return 0
                                1:
                                    return 3
                        1:
                            return 2
                1:
                    return 2
        1:
            return 1

fn main() -> i64:
    return 0
"""

C_RMSD_KERNEL_SOURCE = """\
#include <stdint.h>

int64_t rmsd_metrics_step(
    const double *left, int64_t n_left,
    const double *right, int64_t n_right,
    int64_t length,
    double *out_metrics, int64_t n_out
) {
    if (length < 1) return 1;
    if (n_left < length || n_right < length) return 2;
    if (n_out < 3) return 3;
    double sq_sum = 0.0, dot_sum = 0.0, l_norm = 0.0;
    for (int64_t i = 0; i < length; i++) {
        double a = left[i];
        double b = right[i];
        double diff = a - b;
        sq_sum += diff * diff;
        dot_sum += a * b;
        l_norm += a * a;
    }
    out_metrics[0] = sq_sum;
    out_metrics[1] = dot_sum;
    out_metrics[2] = l_norm;
    return 0;
}
"""


def py_rmsd_metrics_step(left: list[float], right: list[float], length: int) -> tuple[float, float, float]:
    sq_sum = 0.0
    dot_sum = 0.0
    l_norm = 0.0
    for i in range(length):
        a = left[i]
        b = right[i]
        diff = a - b
        sq_sum += diff * diff
        dot_sum += a * b
        l_norm += a * a
    return sq_sum, dot_sum, l_norm


def run_rmsd_benchmarks(tmp_dir: Path) -> dict[str, Any]:
    print("[P1.2] Running RMSD Native Benchmarks (Scales 64, 256, 1024, 8192 + Standalone ELF)...")
    s3_variants = {}
    for opt, mode, label in [
        ("O0", "PER_INSTRUCTION", "s3_o0_per_instruction"),
        ("O1", "PER_INSTRUCTION", "s3_o1_per_instruction"),
        ("O1", "EXACT_SEGMENT", "s3_o1_exact_segment"),
        ("O1", "PURE_EXPERIMENTAL", "s3_o1_pure_experimental"),
    ]:
        so, meta = compile_s3_shared(S3_RMSD_KERNEL_SOURCE, tmp_dir, f"rmsd_{label}", opt, mode)
        lib = ctypes.CDLL(str(so))
        fn = lib.rmsd_metrics_step
        fn.argtypes = [
            ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
            ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
            ctypes.c_int64,
            ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
        ]
        fn.restype = ctypes.c_int64
        s3_variants[label] = (fn, meta)

    c_variants = {}
    for flag, label in [("-O2", "gcc_o2"), ("-O3", "gcc_o3")]:
        so, meta = compile_c_shared(C_RMSD_KERNEL_SOURCE, tmp_dir, f"rmsd_{label}", flag)
        lib = ctypes.CDLL(str(so))
        fn = lib.rmsd_metrics_step
        fn.argtypes = [
            ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
            ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
            ctypes.c_int64,
            ctypes.POINTER(ctypes.c_double), ctypes.c_int64,
        ]
        fn.restype = ctypes.c_int64
        c_variants[label] = (fn, meta)

    scales_out = {}
    for n in (64, 256, 1024, 8192):
        left = [(-1.0, -0.5, 0.5, 1.0)[i % 4] for i in range(n)]
        right = [v + 0.5 for v in left]
        c_left = (ctypes.c_double * n)(*left)
        c_right = (ctypes.c_double * n)(*right)
        c_out = (ctypes.c_double * 3)(0.0, 0.0, 0.0)

        exp_sq, exp_dot, exp_lnorm = py_rmsd_metrics_step(left, right, n)
        exp_rmsd = math.sqrt(exp_sq / n)

        scale_entry: dict[str, Any] = {
            "length": n,
            "expected_squared_distance": exp_sq,
            "expected_dot_product": exp_dot,
            "expected_rmsd": exp_rmsd,
            "max_abs_error": 0.0,
            "implementations": {},
        }

        for label, (fn, meta) in {**s3_variants, **c_variants}.items():
            for _ in range(WARMUPS):
                rc = fn(c_left, n, c_right, n, n, c_out, 3)
                assert rc == 0
            samples = []
            max_err = 0.0
            for _ in range(SAMPLES):
                t0 = time.perf_counter_ns()
                rc = fn(c_left, n, c_right, n, n, c_out, 3)
                t1 = time.perf_counter_ns()
                assert rc == 0
                samples.append(float(t1 - t0))
            err = max(
                abs(c_out[0] - exp_sq),
                abs(c_out[1] - exp_dot),
                abs(c_out[2] - exp_lnorm),
            )
            assert err <= 1e-9
            scale_entry["max_abs_error"] = max(scale_entry["max_abs_error"], err)
            scale_entry["implementations"][label] = {
                "classification": "CURRENT_NATIVE",
                "parity_pass": True,
                "max_abs_error": err,
                **compute_stats(samples),
                **meta,
            }

        for _ in range(WARMUPS):
            py_rmsd_metrics_step(left, right, n)
        py_samples = []
        for _ in range(SAMPLES):
            t0 = time.perf_counter_ns()
            sq, dt, ln = py_rmsd_metrics_step(left, right, n)
            t1 = time.perf_counter_ns()
            assert abs(sq - exp_sq) <= 1e-9
            py_samples.append(float(t1 - t0))
        scale_entry["implementations"]["python_3_12"] = {
            "classification": "CURRENT_NATIVE",
            "parity_pass": True,
            "max_abs_error": 0.0,
            **compute_stats(py_samples),
        }
        scales_out[str(n)] = scale_entry

    # Also measure standalone similarity_distance.s3 ELF binary!
    from benchmarks.s3bench.adapters import _compile_s3bench_source
    sim_src = (S3_REPO_DIR / "benchmarks" / "workloads" / "scientific" / "similarity_distance.s3").read_text(encoding="utf-8")
    tc = NativeToolchain.detect()
    t0_c = time.perf_counter_ns()
    comp_sim = _compile_s3bench_source(sim_src, "O1")
    asm_sim = X8664Backend(
        max_instructions=50_000_000,
        register_allocation=True,
        instruction_budget_mode="per-instruction",
    ).generate(comp_sim.assembly)
    exe_sim = tc.build(asm_sim, tmp_dir / "similarity_distance_elf")
    compile_sim_ns = time.perf_counter_ns() - t0_c
    for _ in range(WARMUPS):
        r = tc.run(exe_sim)
        assert r.returncode == 0 and "29356" in r.stdout
    elf_samples = []
    for _ in range(SAMPLES):
        t0 = time.perf_counter_ns()
        r = tc.run(exe_sim)
        t1 = time.perf_counter_ns()
        assert r.returncode == 0 and "29356" in r.stdout
        elf_samples.append(float(t1 - t0))

    return {
        "scales": scales_out,
        "standalone_similarity_distance_elf": {
            "classification": "CURRENT_NATIVE",
            "expected_checksum": 29356,
            "observed_checksum": 29356,
            "parity_pass": True,
            "compile_ns": compile_sim_ns,
            "binary_bytes": exe_sim.stat().st_size,
            "text_bytes": get_text_size(exe_sim),
            **compute_stats(elf_samples),
        },
    }


# ============================================================================
# 3. REAL STENCIL 2D NATIVE BENCHMARK (64x40, 128x80, 256x160 x 10 GENS)
# ============================================================================

from tests.test_x86_64_tsstore_register_preservation import SPLIT_INLINE_STENCIL_SOURCE

C_STENCIL5POINT_SOURCE = """\
#include <stdint.h>

int64_t stencil5point_step(
    const int64_t *current, int64_t current_count,
    int64_t width, int64_t height,
    int64_t *next, int64_t output_count
) {
    if (width < 3 || height < 3) return 1;
    if (width > current_count || height > current_count || width > current_count / height) return 2;
    int64_t cell_count = width * height;
    if (current_count != cell_count) return 2;
    if (output_count < cell_count) return 3;

    for (int64_t i = 0; i < cell_count; i++) {
        next[i] = 0;
    }
    for (int64_t row = 1; row + 1 < height; row++) {
        int64_t idx = row * width + 1;
        for (int64_t col = 1; col + 1 < width; col++, idx++) {
            next[idx] = (
                current[idx]
                + current[idx - width]
                + current[idx + width]
                + current[idx - 1]
                + current[idx + 1]
                + 2
            ) / 5;
        }
    }
    return 0;
}
"""


def py_stencil5point_10gens(init_grid: list[int], width: int, height: int, gens: int = 10) -> list[int]:
    n = width * height
    cur = list(init_grid)
    nxt = [0] * n
    for _ in range(gens):
        for i in range(n):
            nxt[i] = 0
        for r in range(1, height - 1):
            base = r * width
            for c in range(1, width - 1):
                idx = base + c
                s = cur[idx] + cur[idx - width] + cur[idx + width] + cur[idx - 1] + cur[idx + 1] + 2
                # C truncates toward zero
                nxt[idx] = int(s / 5)
        cur, nxt = nxt, cur
    return cur


def run_stencil2d_benchmarks(tmp_dir: Path) -> dict[str, Any]:
    print("[P1.3] Running Real Stencil 2D Native Benchmarks (64x40, 128x80, 256x160 x 10 gens)...")
    s3_variants = {}
    for opt, mode, label in [
        ("O0", "PER_INSTRUCTION", "s3_o0_per_instruction"),
        ("O1", "PER_INSTRUCTION", "s3_o1_per_instruction"),
        ("O1", "EXACT_SEGMENT", "s3_o1_exact_segment"),
        ("O1", "PURE_EXPERIMENTAL", "s3_o1_pure_experimental"),
    ]:
        so, meta = compile_s3_shared(SPLIT_INLINE_STENCIL_SOURCE, tmp_dir, f"stencil_{label}", opt, mode)
        lib = ctypes.CDLL(str(so))
        fn = lib.stencil5point_step
        fn.argtypes = [
            ctypes.POINTER(ctypes.c_int64), ctypes.c_int64,
            ctypes.c_int64, ctypes.c_int64,
            ctypes.POINTER(ctypes.c_int64), ctypes.c_int64,
        ]
        fn.restype = ctypes.c_int64
        s3_variants[label] = (fn, meta)

    c_variants = {}
    for flag, label in [("-O2", "gcc_o2"), ("-O3", "gcc_o3")]:
        so, meta = compile_c_shared(C_STENCIL5POINT_SOURCE, tmp_dir, f"stencil_{label}", flag)
        lib = ctypes.CDLL(str(so))
        fn = lib.stencil5point_step
        fn.argtypes = [
            ctypes.POINTER(ctypes.c_int64), ctypes.c_int64,
            ctypes.c_int64, ctypes.c_int64,
            ctypes.POINTER(ctypes.c_int64), ctypes.c_int64,
        ]
        fn.restype = ctypes.c_int64
        c_variants[label] = (fn, meta)

    grids_out = {}
    for w, h in ((64, 40), (128, 80), (256, 160)):
        n = w * h
        gens = 10
        init_grid = [(i * 37 + 19) % 512 for i in range(n)]

        # Reference using C GCC -O2 first
        c_fn, _ = c_variants["gcc_o2"]
        buf_a = (ctypes.c_int64 * n)(*init_grid)
        buf_b = (ctypes.c_int64 * n)(*([0] * n))
        for _ in range(gens):
            assert c_fn(buf_a, n, w, h, buf_b, n) == 0
            buf_a, buf_b = buf_b, buf_a
        ref_final = list(buf_a)
        ref_hash = hashlib.sha256(
            ",".join(map(str, ref_final)).encode("ascii")
        ).hexdigest()

        grid_key = f"{w}x{h}"
        grid_entry: dict[str, Any] = {
            "grid": grid_key,
            "width": w,
            "height": h,
            "cells": n,
            "generations": gens,
            "expected_sha256": ref_hash,
            "implementations": {},
        }

        for label, (fn, meta) in {**s3_variants, **c_variants}.items():
            for _ in range(WARMUPS):
                ba = (ctypes.c_int64 * n)(*init_grid)
                bb = (ctypes.c_int64 * n)(*([0] * n))
                for _g in range(gens):
                    rc = fn(ba, n, w, h, bb, n)
                    assert rc == 0
                    ba, bb = bb, ba
                assert list(ba) == ref_final

            samples = []
            for _ in range(SAMPLES):
                ba = (ctypes.c_int64 * n)(*init_grid)
                bb = (ctypes.c_int64 * n)(*([0] * n))
                t0 = time.perf_counter_ns()
                for _g in range(gens):
                    rc = fn(ba, n, w, h, bb, n)
                    ba, bb = bb, ba
                t1 = time.perf_counter_ns()
                assert rc == 0
                samples.append(float(t1 - t0))

            grid_entry["implementations"][label] = {
                "classification": "CURRENT_NATIVE",
                "parity_pass": True,
                "output_sha256": ref_hash,
                **compute_stats(samples),
                **meta,
            }

        # Python timing (3 warmups, 9 samples on 64x40; on larger grids 1 warmup + 3 samples or full 9 if fast)
        py_ref = py_stencil5point_10gens(init_grid, w, h, gens)
        assert py_ref == ref_final
        py_samples = []
        py_reps = SAMPLES if n <= 10240 else 3
        for _ in range(py_reps):
            t0 = time.perf_counter_ns()
            out_py = py_stencil5point_10gens(init_grid, w, h, gens)
            t1 = time.perf_counter_ns()
            assert out_py == ref_final
            py_samples.append(float(t1 - t0))
        grid_entry["implementations"]["python_3_12"] = {
            "classification": "CURRENT_NATIVE",
            "parity_pass": True,
            "output_sha256": ref_hash,
            **compute_stats(py_samples),
        }
        grids_out[grid_key] = grid_entry

    return grids_out


# ============================================================================
# 4. COMPLEMENTARY CONTROL KERNELS (GEMM_I64, RULE110_CA, FNV1A_HASH)
# ============================================================================

S3_GEMM_SOURCE = """\
export fn gemm_i64(
    a: &[i64],
    b: &[i64],
    n: i64,
    c: &mut [i64]
) -> i64:
    mut total: i64 = n * n
    match len(a) < total:
        -1:
            return 1
        0:
            match len(b) < total:
                -1:
                    return 1
                0:
                    match len(c) < total:
                        -1:
                            return 1
                        0:
                            mut i: i64 = 0
                            mut one: i64 = 1
                            mut checksum: i64 = 0
                            while i < n:
                                mut j: i64 = 0
                                while j < n:
                                    mut acc: i64 = 0
                                    mut k: i64 = 0
                                    while k < n:
                                        acc = acc + a[i * n + k] * b[k * n + j]
                                        k = k + one
                                    c[i * n + j] = acc
                                    checksum = checksum + acc
                                    j = j + one
                                i = i + one
                            return checksum
                        1:
                            return 1
                1:
                    return 1
        1:
            return 1

fn main() -> i64:
    return 0
"""

C_GEMM_SOURCE = """\
#include <stdint.h>
int64_t gemm_i64(const int64_t *a, int64_t na, const int64_t *b, int64_t nb, int64_t n, int64_t *c, int64_t nc) {
    int64_t total = n * n;
    if (na < total || nb < total || nc < total) return 1;
    int64_t checksum = 0;
    for (int64_t i = 0; i < n; i++) {
        for (int64_t j = 0; j < n; j++) {
            int64_t acc = 0;
            for (int64_t k = 0; k < n; k++) {
                acc += a[i * n + k] * b[k * n + j];
            }
            c[i * n + j] = acc;
            checksum += acc;
        }
    }
    return checksum;
}
"""

S3_RULE110_SOURCE = """\
export fn rule110_step(
    state: &mut [i64],
    scratch: &mut [i64],
    width: i64,
    generations: i64
) -> i64:
    match len(state) < width:
        -1:
            return -1
        0:
            match len(scratch) < width:
                -1:
                    return -1
                0:
                    mut g: i64 = 0
                    mut one: i64 = 1
                    while g < generations:
                        scratch[0] = 0
                        scratch[width - one] = 0
                        mut i: i64 = 1
                        while i + one < width:
                            mut pat: i64 = state[i - one] * 4 + state[i] * 2 + state[i + one]
                            match pat == 0:
                                -1:
                                    scratch[i] = 0
                                0:
                                    match pat == 7:
                                        -1:
                                            scratch[i] = 0
                                        0:
                                            match pat == 4:
                                                -1:
                                                    scratch[i] = 0
                                                0:
                                                    scratch[i] = 1
                                                1:
                                                    scratch[i] = 1
                                        1:
                                            scratch[i] = 1
                                1:
                                    scratch[i] = 1
                            i = i + one
                        mut j: i64 = 0
                        while j < width:
                            state[j] = scratch[j]
                            j = j + one
                        g = g + one
                    mut popcount: i64 = 0
                    mut k: i64 = 0
                    while k < width:
                        popcount = popcount + state[k] * (k + one)
                        k = k + one
                    return popcount
                1:
                    return -1
        1:
            return -1

fn main() -> i64:
    return 0
"""

C_RULE110_SOURCE = """\
#include <stdint.h>
int64_t rule110_step(int64_t *state, int64_t ns, int64_t *scratch, int64_t nsc, int64_t width, int64_t generations) {
    if (ns < width || nsc < width) return -1;
    for (int64_t g = 0; g < generations; g++) {
        scratch[0] = 0;
        scratch[width - 1] = 0;
        for (int64_t i = 1; i + 1 < width; i++) {
            int64_t pat = state[i - 1] * 4 + state[i] * 2 + state[i + 1];
            scratch[i] = (pat == 0 || pat == 4 || pat == 7) ? 0 : 1;
        }
        for (int64_t j = 0; j < width; j++) {
            state[j] = scratch[j];
        }
    }
    int64_t popcount = 0;
    for (int64_t k = 0; k < width; k++) {
        popcount += state[k] * (k + 1);
    }
    return popcount;
}
"""

S3_FNV_HASH_SOURCE = """\
export fn rolling_hash_i64(
    data: &[i64],
    length: i64,
    rounds: i64
) -> i64:
    match len(data) < length:
        -1:
            return -1
        0:
            mut r: i64 = 0
            mut one: i64 = 1
            mut acc: i64 = 216613626
            mut mod_val: i64 = 1000000007
            while r < rounds:
                mut i: i64 = 0
                while i < length:
                    mut step1: i64 = acc + data[i] + r
                    step1 = step1 - (step1 / mod_val) * mod_val
                    mut step2: i64 = step1 * 16777619
                    acc = step2 - (step2 / mod_val) * mod_val
                    i = i + one
                r = r + one
            return acc
        1:
            return -1

fn main() -> i64:
    return 0
"""

C_FNV_HASH_SOURCE = """\
#include <stdint.h>
int64_t rolling_hash_i64(const int64_t *data, int64_t nd, int64_t length, int64_t rounds) {
    if (nd < length) return -1;
    int64_t acc = 216613626LL;
    int64_t mod_val = 1000000007LL;
    for (int64_t r = 0; r < rounds; r++) {
        for (int64_t i = 0; i < length; i++) {
            int64_t step1 = acc + data[i] + r;
            step1 = step1 - (step1 / mod_val) * mod_val;
            int64_t step2 = step1 * 16777619LL;
            acc = step2 - (step2 / mod_val) * mod_val;
        }
    }
    return acc;
}
"""


def run_control_kernels(tmp_dir: Path) -> dict[str, Any]:
    print("[P1.4] Running Complementary Control Kernels (GEMM_I64, RULE110_CA, FNV1A_HASH)...")
    out: dict[str, Any] = {}

    # 4A: GEMM_I64 (32x32)
    n_gemm = 32
    tot = n_gemm * n_gemm
    a_init = [(i * 13 + 7) % 31 - 15 for i in range(tot)]
    b_init = [(i * 19 + 3) % 31 - 15 for i in range(tot)]
    c_a = (ctypes.c_int64 * tot)(*a_init)
    c_b = (ctypes.c_int64 * tot)(*b_init)
    c_c = (ctypes.c_int64 * tot)(*([0] * tot))

    gemm_impls = {}
    exp_gemm = None
    for opt, mode, label in [
        ("O0", "PER_INSTRUCTION", "s3_o0_per_instruction"),
        ("O1", "PER_INSTRUCTION", "s3_o1_per_instruction"),
        ("O1", "EXACT_SEGMENT", "s3_o1_exact_segment"),
        ("O1", "PURE_EXPERIMENTAL", "s3_o1_pure_experimental"),
    ]:
        so, meta = compile_s3_shared(S3_GEMM_SOURCE, tmp_dir, f"gemm_{label}", opt, mode)
        lib = ctypes.CDLL(str(so))
        fn = lib.gemm_i64
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64]
        fn.restype = ctypes.c_int64
        for _ in range(WARMUPS):
            res = fn(c_a, tot, c_b, tot, n_gemm, c_c, tot)
        if exp_gemm is None:
            exp_gemm = int(res)
        assert int(res) == exp_gemm
        samples = []
        for _ in range(SAMPLES):
            t0 = time.perf_counter_ns()
            res = fn(c_a, tot, c_b, tot, n_gemm, c_c, tot)
            t1 = time.perf_counter_ns()
            assert int(res) == exp_gemm
            samples.append(float(t1 - t0))
        gemm_impls[label] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_gemm, **compute_stats(samples), **meta}

    for flag, label in [("-O2", "gcc_o2"), ("-O3", "gcc_o3")]:
        so, meta = compile_c_shared(C_GEMM_SOURCE, tmp_dir, f"gemm_{label}", flag)
        lib = ctypes.CDLL(str(so))
        fn = lib.gemm_i64
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64]
        fn.restype = ctypes.c_int64
        for _ in range(WARMUPS):
            res = fn(c_a, tot, c_b, tot, n_gemm, c_c, tot)
            assert int(res) == exp_gemm
        samples = []
        for _ in range(SAMPLES):
            t0 = time.perf_counter_ns()
            res = fn(c_a, tot, c_b, tot, n_gemm, c_c, tot)
            t1 = time.perf_counter_ns()
            assert int(res) == exp_gemm
            samples.append(float(t1 - t0))
        gemm_impls[label] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_gemm, **compute_stats(samples), **meta}

    def py_gemm() -> int:
        chk = 0
        for i in range(n_gemm):
            row_a = i * n_gemm
            for j in range(n_gemm):
                acc = 0
                for k in range(n_gemm):
                    acc += a_init[row_a + k] * b_init[k * n_gemm + j]
                chk += acc
        return chk

    for _ in range(WARMUPS):
        assert py_gemm() == exp_gemm
    py_samples = []
    for _ in range(SAMPLES):
        t0 = time.perf_counter_ns()
        r = py_gemm()
        t1 = time.perf_counter_ns()
        assert r == exp_gemm
        py_samples.append(float(t1 - t0))
    gemm_impls["python_3_12"] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_gemm, **compute_stats(py_samples)}
    out["GEMM_I64_32x32"] = {"description": "Dense 32x32 i64 matrix multiplication (32,768 MACs)", "expected_checksum": exp_gemm, "implementations": gemm_impls}

    # 4B: RULE110_CA (256 cells x 128 gens)
    w_ca, g_ca = 256, 128
    init_ca = [1 if i in (128, 200, 250) else 0 for i in range(w_ca)]
    ca_impls = {}
    exp_ca = None
    for opt, mode, label in [
        ("O0", "PER_INSTRUCTION", "s3_o0_per_instruction"),
        ("O1", "PER_INSTRUCTION", "s3_o1_per_instruction"),
        ("O1", "EXACT_SEGMENT", "s3_o1_exact_segment"),
        ("O1", "PURE_EXPERIMENTAL", "s3_o1_pure_experimental"),
    ]:
        so, meta = compile_s3_shared(S3_RULE110_SOURCE, tmp_dir, f"rule110_{label}", opt, mode)
        lib = ctypes.CDLL(str(so))
        fn = lib.rule110_step
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
        fn.restype = ctypes.c_int64
        for _ in range(WARMUPS):
            st_buf = (ctypes.c_int64 * w_ca)(*init_ca)
            sc_buf = (ctypes.c_int64 * w_ca)(*([0] * w_ca))
            res = fn(st_buf, w_ca, sc_buf, w_ca, w_ca, g_ca)
        if exp_ca is None:
            exp_ca = int(res)
        assert int(res) == exp_ca
        samples = []
        for _ in range(SAMPLES):
            st_buf = (ctypes.c_int64 * w_ca)(*init_ca)
            sc_buf = (ctypes.c_int64 * w_ca)(*([0] * w_ca))
            t0 = time.perf_counter_ns()
            res = fn(st_buf, w_ca, sc_buf, w_ca, w_ca, g_ca)
            t1 = time.perf_counter_ns()
            assert int(res) == exp_ca
            samples.append(float(t1 - t0))
        ca_impls[label] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_ca, **compute_stats(samples), **meta}

    for flag, label in [("-O2", "gcc_o2"), ("-O3", "gcc_o3")]:
        so, meta = compile_c_shared(C_RULE110_SOURCE, tmp_dir, f"rule110_{label}", flag)
        lib = ctypes.CDLL(str(so))
        fn = lib.rule110_step
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
        fn.restype = ctypes.c_int64
        for _ in range(WARMUPS):
            st_buf = (ctypes.c_int64 * w_ca)(*init_ca)
            sc_buf = (ctypes.c_int64 * w_ca)(*([0] * w_ca))
            res = fn(st_buf, w_ca, sc_buf, w_ca, w_ca, g_ca)
            assert int(res) == exp_ca
        samples = []
        for _ in range(SAMPLES):
            st_buf = (ctypes.c_int64 * w_ca)(*init_ca)
            sc_buf = (ctypes.c_int64 * w_ca)(*([0] * w_ca))
            t0 = time.perf_counter_ns()
            res = fn(st_buf, w_ca, sc_buf, w_ca, w_ca, g_ca)
            t1 = time.perf_counter_ns()
            assert int(res) == exp_ca
            samples.append(float(t1 - t0))
        ca_impls[label] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_ca, **compute_stats(samples), **meta}

    def py_rule110() -> int:
        st = list(init_ca)
        sc = [0] * w_ca
        for _ in range(g_ca):
            sc[0] = 0; sc[w_ca - 1] = 0
            for i in range(1, w_ca - 1):
                pat = st[i - 1] * 4 + st[i] * 2 + st[i + 1]
                sc[i] = 0 if pat in (0, 4, 7) else 1
            st[:] = sc
        return sum(st[k] * (k + 1) for k in range(w_ca))

    for _ in range(WARMUPS):
        assert py_rule110() == exp_ca
    py_samples = []
    for _ in range(SAMPLES):
        t0 = time.perf_counter_ns()
        r = py_rule110()
        t1 = time.perf_counter_ns()
        assert r == exp_ca
        py_samples.append(float(t1 - t0))
    ca_impls["python_3_12"] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_ca, **compute_stats(py_samples)}
    out["RULE110_CA_256x128"] = {"description": "1D Cellular Automaton Rule 110 (256 cells x 128 generations)", "expected_checksum": exp_ca, "implementations": ca_impls}

    # 4C: FNV1A_HASH (4096 words x 10 rounds)
    n_fnv, r_fnv = 4096, 10
    fnv_data = [(i * 1103515245 + 12345) & 0x7FFFFFFF for i in range(n_fnv)]
    c_fnv = (ctypes.c_int64 * n_fnv)(*fnv_data)
    fnv_impls = {}
    exp_fnv = None
    for opt, mode, label in [
        ("O0", "PER_INSTRUCTION", "s3_o0_per_instruction"),
        ("O1", "PER_INSTRUCTION", "s3_o1_per_instruction"),
        ("O1", "EXACT_SEGMENT", "s3_o1_exact_segment"),
        ("O1", "PURE_EXPERIMENTAL", "s3_o1_pure_experimental"),
    ]:
        so, meta = compile_s3_shared(S3_FNV_HASH_SOURCE, tmp_dir, f"fnv_{label}", opt, mode)
        lib = ctypes.CDLL(str(so))
        fn = lib.rolling_hash_i64
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
        fn.restype = ctypes.c_int64
        for _ in range(WARMUPS):
            res = fn(c_fnv, n_fnv, n_fnv, r_fnv)
        if exp_fnv is None:
            exp_fnv = int(res)
        assert int(res) == exp_fnv
        samples = []
        for _ in range(SAMPLES):
            t0 = time.perf_counter_ns()
            res = fn(c_fnv, n_fnv, n_fnv, r_fnv)
            t1 = time.perf_counter_ns()
            assert int(res) == exp_fnv
            samples.append(float(t1 - t0))
        fnv_impls[label] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_fnv, **compute_stats(samples), **meta}

    for flag, label in [("-O2", "gcc_o2"), ("-O3", "gcc_o3")]:
        so, meta = compile_c_shared(C_FNV_HASH_SOURCE, tmp_dir, f"fnv_{label}", flag)
        lib = ctypes.CDLL(str(so))
        fn = lib.rolling_hash_i64
        fn.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.c_int64]
        fn.restype = ctypes.c_int64
        for _ in range(WARMUPS):
            res = fn(c_fnv, n_fnv, n_fnv, r_fnv)
            assert int(res) == exp_fnv
        samples = []
        for _ in range(SAMPLES):
            t0 = time.perf_counter_ns()
            res = fn(c_fnv, n_fnv, n_fnv, r_fnv)
            t1 = time.perf_counter_ns()
            assert int(res) == exp_fnv
            samples.append(float(t1 - t0))
        fnv_impls[label] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_fnv, **compute_stats(samples), **meta}

    def py_fnv() -> int:
        acc = 216613626
        mod_val = 1000000007
        for r in range(r_fnv):
            for i in range(n_fnv):
                step1 = (acc + fnv_data[i] + r) % mod_val
                acc = (step1 * 16777619) % mod_val
        return acc

    for _ in range(WARMUPS):
        assert py_fnv() == exp_fnv
    py_samples = []
    for _ in range(SAMPLES):
        t0 = time.perf_counter_ns()
        r = py_fnv()
        t1 = time.perf_counter_ns()
        assert r == exp_fnv
        py_samples.append(float(t1 - t0))
    fnv_impls["python_3_12"] = {"classification": "CURRENT_NATIVE", "parity_pass": True, "checksum": exp_fnv, **compute_stats(py_samples)}
    out["FNV1A_HASH_4096x10"] = {"description": "Rolling modular hash over 4096 i64 words x 10 rounds", "expected_checksum": exp_fnv, "implementations": fnv_impls}

    return out


def render_markdown_report(payload: dict[str, Any], out_md: Path) -> None:
    lines = [
        "# S3 Scientific Expansion V2 — Current Native Linux x86-64 Benchmark Report",
        "",
        f"- **Campaign**: `{payload['campaign']}`",
        f"- **S3 Compiler SHA**: `{payload['s3_compiler_sha']}` (includes P0 fix `fix/s3-native-ra-codegen-v1`)",
        f"- **S3-Benchmarks SHA**: `{payload['benchmarks_sha']}`",
        f"- **Platform**: `{payload['environment']['platform']}` (`{payload['environment']['cpu']}`)",
        f"- **Toolchains**: GCC `{payload['environment']['gcc_version']}`, Python `{payload['environment']['python_version']}`",
        f"- **Unavailable Toolchains**: Clang=`NOT_MEASURED`, Rust=`NOT_MEASURED`, Zig=`NOT_MEASURED`",
        f"- **Sampling Protocol**: `warmups={WARMUPS}`, `samples={SAMPLES}` (all times in nanoseconds; `CURRENT_NATIVE` execution)",
        "",
        "---",
        "",
        "## 1. JSMN JSON Tokenization & Checksum (`CURRENT_NATIVE`)",
        "",
        "| Corpus | Bytes | Tokens | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | S3 O1 EXACT MB/s |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for cname, cdata in payload["workloads"]["jsmn"].items():
        imp = cdata["implementations"]
        lines.append(
            f"| `{cname}` | {cdata['input_bytes']} | {cdata['expected_tokens']} | "
            f"{imp['s3_o0_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_exact_segment']['median_ns']:,.0f} | "
            f"{imp['s3_o1_pure_experimental']['median_ns']:,.0f} | "
            f"{imp['gcc_o2']['median_ns']:,.0f} | "
            f"{imp['python_3_12']['median_ns']:,.0f} | "
            f"**{imp['s3_o1_exact_segment']['mb_per_sec']:.2f}** |"
        )

    lines.extend([
        "",
        "## 2. RMSD & Vector Similarity (`CURRENT_NATIVE`)",
        "",
        "| Scale (N) | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | Max Abs Error |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])
    for scale, sdata in payload["workloads"]["rmsd"]["scales"].items():
        imp = sdata["implementations"]
        lines.append(
            f"| **{scale}** | "
            f"{imp['s3_o0_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_exact_segment']['median_ns']:,.0f} | "
            f"{imp['s3_o1_pure_experimental']['median_ns']:,.0f} | "
            f"{imp['gcc_o2']['median_ns']:,.0f} | "
            f"{imp['python_3_12']['median_ns']:,.0f} | "
            f"`{sdata['max_abs_error']:.2e}` |"
        )
    elf = payload["workloads"]["rmsd"]["standalone_similarity_distance_elf"]
    lines.append(
        f"\n- **Standalone `similarity_distance.s3` ELF Binary (`CURRENT_NATIVE`)**: Median `{elf['median_ns']:,.0f} ns` (`{elf['median_ns']/1e6:.2f} ms`), `.text` = `{elf['text_bytes']:,} bytes`, ELF = `{elf['binary_bytes']:,} bytes`, checksum = `{elf['observed_checksum']}` (`PASS`)."
    )

    lines.extend([
        "",
        "## 3. Real Stencil 2D (`stencil5point_split_inline.s3`, 10 Generations, `CURRENT_NATIVE`)",
        "",
        "| Grid | Cells | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | EXACT vs PER Speedup |",
        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])
    for gname, gdata in payload["workloads"]["stencil2d"].items():
        imp = gdata["implementations"]
        sp = imp["s3_o1_per_instruction"]["median_ns"] / imp["s3_o1_exact_segment"]["median_ns"]
        lines.append(
            f"| **{gname}** | {gdata['cells']:,} | "
            f"{imp['s3_o0_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_exact_segment']['median_ns']:,.0f} | "
            f"{imp['s3_o1_pure_experimental']['median_ns']:,.0f} | "
            f"{imp['gcc_o2']['median_ns']:,.0f} | "
            f"{imp['python_3_12']['median_ns']:,.0f} | "
            f"**{sp:.2f}x** |"
        )

    lines.extend([
        "",
        "## 4. Complementary Control Kernels (`CURRENT_NATIVE`)",
        "",
        "| Kernel | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | Checksum |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])
    for kname, kdata in payload["workloads"]["control_kernels"].items():
        imp = kdata["implementations"]
        lines.append(
            f"| `{kname}` | "
            f"{imp['s3_o0_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_per_instruction']['median_ns']:,.0f} | "
            f"{imp['s3_o1_exact_segment']['median_ns']:,.0f} | "
            f"{imp['s3_o1_pure_experimental']['median_ns']:,.0f} | "
            f"{imp['gcc_o2']['median_ns']:,.0f} | "
            f"{imp['python_3_12']['median_ns']:,.0f} | "
            f"`{kdata['expected_checksum']}` |"
        )

    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    out_dir = S3_BENCHMARKS_DIR / "benchmarks" / "expansion_v2"
    out_dir.mkdir(parents=True, exist_ok=True)

    gcc_ver = subprocess.check_output(["gcc", "--version"], text=True).splitlines()[0]
    cpu_model = "x86_64"
    if Path("/proc/cpuinfo").exists():
        for line in Path("/proc/cpuinfo").read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.lower().startswith("model name"):
                cpu_model = line.split(":", 1)[1].strip()
                break

    with tempfile.TemporaryDirectory(prefix="s3_exp_v2_") as tmp:
        tmp_path = Path(tmp)
        jsmn_res = run_jsmn_benchmarks(tmp_path)
        rmsd_res = run_rmsd_benchmarks(tmp_path)
        stencil_res = run_stencil2d_benchmarks(tmp_path)
        control_res = run_control_kernels(tmp_path)

    payload = {
        "campaign": "S3_SCIENTIFIC_EXPANSION_V2",
        "phase": "P1_CURRENT_NATIVE_BENCHMARKS",
        "s3_compiler_sha": get_git_sha(S3_REPO_DIR),
        "benchmarks_sha": get_git_sha(S3_BENCHMARKS_DIR),
        "environment": {
            "platform": platform.platform(),
            "cpu": cpu_model,
            "gcc_version": gcc_ver,
            "python_version": platform.python_version(),
            "clang": "NOT_MEASURED",
            "rustc": "NOT_MEASURED",
            "zig": "NOT_MEASURED",
            "peak_rss_kib": get_peak_rss_kib(),
        },
        "workloads": {
            "jsmn": jsmn_res,
            "rmsd": rmsd_res,
            "stencil2d": stencil_res,
            "control_kernels": control_res,
        },
    }

    json_path = out_dir / "results_v2.json"
    md_path = out_dir / "RESULTS_V2.md"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    render_markdown_report(payload, md_path)
    print(f"[OK] Saved {json_path} and {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
