#!/usr/bin/env python3
"""Reproducible S3 V5 Ecosystem Forge benchmark suite.

Measures and validates across all active V5 workstreams in WSL2 Linux x86-64:
1. Predictive Compute CRChain native lowering (sum_i2, triangular_cubic) vs S3 standard .so
2. S3 x86-64 SIMD/F64/Poisson2D kernels vs GCC -O3
3. S3 Compact V19 (V5-COMPACT-TURBO) live paired throughput & SHA-256 identity
4. S3-Elite-Lab M48/M50/M55 DOOM WASM artifact/SHA/evidence verification
5. S3C-NG V7 differential corpus parity verification
"""

from __future__ import annotations

import csv
import ctypes
from datetime import datetime, timezone
import hashlib
import json
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Callable


THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
WORKSPACE_ROOT = BENCH_ROOT.parent
S3_ROOT = WORKSPACE_ROOT / "S3"
ELITE_LAB_ROOT = WORKSPACE_ROOT / "S3-Elite-Lab"
COMPACT_WT_ROOT = WORKSPACE_ROOT / "S3-wt-compact-v18"
S3CNG_WT_ROOT = WORKSPACE_ROOT / "S3-wt-s3cng"

for p in (str(BENCH_ROOT / "benchmarks" / "v4_gpu_and_cpu"), str(S3_ROOT)):
    if p not in sys.path:
        sys.path.insert(0, p)

from validation_engine import validate_array


SCEV_BENCH_SRC = """
export fn sum_i2(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 0
    while i < n:
        acc = acc + i * i
        i = i + 1
    return acc

export fn triangular_cubic(n: i64) -> i64:
    mut i: i64 = 0
    mut s1: i64 = 0
    mut s2: i64 = 0
    while i < n:
        s1 = s1 + i * i
        s2 = s2 + s1
        i = i + 1
    return s2

fn main() -> i64:
    return 0
"""


def _git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def _time_samples(fn: Callable[[], Any], warmups: int = 3, samples: int = 9) -> dict[str, Any]:
    last = None
    for _ in range(warmups):
        last = fn()
    vals: list[float] = []
    for _ in range(samples):
        t0 = time.perf_counter()
        last = fn()
        vals.append((time.perf_counter() - t0) * 1000.0)
    vals_sorted = sorted(vals)
    q1 = vals_sorted[len(vals_sorted) // 4]
    q3 = vals_sorted[(3 * len(vals_sorted)) // 4]
    return {
        "median_ms": round(statistics.median(vals), 6),
        "q1_ms": round(q1, 6),
        "q3_ms": round(q3, 6),
        "iqr_ms": round(q3 - q1, 6),
        "min_ms": round(min(vals), 6),
        "max_ms": round(max(vals), 6),
        "samples": samples,
        "warmups": warmups,
        "last_value": last,
    }


def _oracle_sum_i2(n: int) -> int:
    if n <= 0:
        return 0
    return (n - 1) * n * (2 * n - 1) // 6


def _oracle_triangular_cubic(n: int) -> int:
    if n <= 1:
        return 0
    total = 0
    # sum_{i=0..n-1} sum_{j=0..i} j^2 = sum_{j=0..n-1} (n - j) * j^2
    # = n * (n-1)*n*(2n-1)/6 - ((n-1)*n/2)^2
    m = n - 1
    s2 = m * n * (2 * n - 1) // 6
    s3 = (m * n // 2) ** 2
    total = n * s2 - s3
    return total


def benchmark_crchain_native() -> list[dict[str, Any]]:
    from bootstrap.s3.backends.x86_64.backend import SCIENTIFIC_MAX_INSTRUCTIONS, generate_ffi_assembly
    from bootstrap.s3.backends.x86_64.toolchain import NativeToolchain
    from bootstrap.s3.pipeline import compile_source

    c_std = compile_source(
        SCEV_BENCH_SRC,
        optimization="O1",
        predictive_exact=False,
        predictive_small_t_cutoff=4,
    )
    c_cr = compile_source(
        SCEV_BENCH_SRC,
        optimization="O1",
        predictive_exact=True,
        predictive_small_t_cutoff=4,
    )
    if "sum_i2" not in c_cr.predictive_lowered_functions or "triangular_cubic" not in c_cr.predictive_lowered_functions:
        raise RuntimeError(f"Expected CRChain lowering for sum_i2 and triangular_cubic, got {c_cr.predictive_lowered_functions}")

    _, ap_std = c_std.require_ordinary_artifacts()
    _, ap_cr = c_cr.require_ordinary_artifacts()
    asm_std = generate_ffi_assembly(ap_std, max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS)
    asm_cr = generate_ffi_assembly(ap_cr, max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS)

    tc = NativeToolchain.detect()
    rows: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        so_std = tc.build_shared(asm_std, td_path / "std.so")
        so_cr = tc.build_shared(asm_cr, td_path / "cr.so")
        lib_std = ctypes.CDLL(str(so_std))
        lib_cr = ctypes.CDLL(str(so_cr))

        specs = (
            ("sum_i2", _oracle_sum_i2, (10, 100, 1000, 10000, 100000)),
            ("triangular_cubic", _oracle_triangular_cubic, (10, 100, 1000, 10000, 100000)),
        )
        for fn_name, oracle_fn, sizes in specs:
            f_std = getattr(lib_std, fn_name)
            f_cr = getattr(lib_cr, fn_name)
            f_std.argtypes = [ctypes.c_int64]
            f_std.restype = ctypes.c_int64
            f_cr.argtypes = [ctypes.c_int64]
            f_cr.restype = ctypes.c_int64
            for t_val in sizes:
                reps = 200 if t_val <= 1000 else (20 if t_val <= 10000 else 5)

                def _run_std(fn=f_std, tv=t_val, rp=reps) -> int:
                    out = 0
                    for _ in range(rp):
                        out = int(fn(tv))
                    return out

                def _run_cr(fn=f_cr, tv=t_val, rp=reps) -> int:
                    out = 0
                    for _ in range(rp):
                        out = int(fn(tv))
                    return out

                t_std = _time_samples(_run_std, warmups=3, samples=9)
                t_cr = _time_samples(_run_cr, warmups=3, samples=9)
                expected = oracle_fn(t_val)
                val_std = int(t_std.pop("last_value"))
                val_cr = int(t_cr.pop("last_value"))
                exact = val_std == expected and val_cr == expected
                rows.append(
                    {
                        "BENCHMARK_ID": f"CRCHAIN_{fn_name}_T{t_val}",
                        "KERNEL": fn_name,
                        "T_STEPS": t_val,
                        "CALLS_PER_SAMPLE": reps,
                        "EXPECTED_VALUE": expected,
                        "STD_NATIVE_VALUE": val_std,
                        "CRCHAIN_NATIVE_VALUE": val_cr,
                        "EXACT_PARITY": exact,
                        "NUMERICAL_VALIDITY": "VALID" if exact else "INVALID",
                        "DATA_INTEGRITY": "PASS" if exact else "VALUE_MISMATCH",
                        "STD_MEDIAN_MS": t_std["median_ms"],
                        "CRCHAIN_MEDIAN_MS": t_cr["median_ms"],
                        "SPEEDUP": round(t_std["median_ms"] / max(1e-9, t_cr["median_ms"]), 2),
                        "STD_TIMING": t_std,
                        "CRCHAIN_TIMING": t_cr,
                    }
                )
    return rows


def benchmark_x86_scientific() -> dict[str, Any]:
    from tools.numerics_v4_9_study import (
        benchmark_poisson2d_large_chunked,
        benchmark_s3_simd_vs_scalar_vs_gcc,
        profile_f64_codegen,
    )

    simd_recs = benchmark_s3_simd_vs_scalar_vs_gcc(sizes=(256, 1024, 4096, 16384), repeats=5)
    poisson_recs = benchmark_poisson2d_large_chunked(grids=(16, 24, 32, 48), tol=1e-12, max_iter=4500, chunk_iter=50)
    f64_prof = profile_f64_codegen()

    validated_poisson = []
    for pr in poisson_recs:
        ok = pr["s3_iters"] == pr["gcc_iters"] and pr["s3_max_err_vs_gcc"] < 1e-10 and pr["s3_max_err_vs_true"] < 1e-10
        validated_poisson.append(
            {
                **pr,
                "NUMERICAL_VALIDITY": "VALID" if ok else "INVALID",
                "DATA_INTEGRITY": "PASS" if ok else "TOLERANCE_EXCEEDED",
            }
        )

    ablation_path = S3_ROOT / "ablation_v4_3_report.json"
    ablation = json.loads(ablation_path.read_text(encoding="utf-8")) if ablation_path.exists() else {}
    return {
        "simd_dot_vs_gcc": simd_recs,
        "poisson2d_chunked_vs_gcc": validated_poisson,
        "f64_codegen_profile": f64_prof,
        "regalloc_spill_ablation": ablation.get("cost_model_decisions", {}),
    }


def benchmark_compact_v19() -> dict[str, Any]:
    script = COMPACT_WT_ROOT / "benchmarks" / "s3-compact-v19" / "run_v19_benchmark.py"
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(
            [
                sys.executable,
                str(script),
                "--out-dir",
                td,
                "--warmups",
                "1",
                "--repeats",
                "3",
            ],
            cwd=str(COMPACT_WT_ROOT),
            check=True,
        )
        return json.loads((Path(td) / "results.json").read_text(encoding="utf-8"))


def benchmark_doom_wasm() -> dict[str, Any]:
    subprocess.run(
        ["node", "--test-isolation=none", "--test", "tests/doom-m55-line-trace.test.mjs"],
        cwd=str(ELITE_LAB_ROOT),
        check=True,
    )
    records = {}
    for milestone, wasm_name, ev_name in (
        ("m48", "assembly/doom/generated/m48/doom_simulation_m48.wasm", "docs/reports/evidence/m48/microbenchmark.json"),
        ("m50", "assembly/doom/generated/m50/doom_simulation_m50.wasm", "docs/reports/evidence/m50/kernel-benchmark.json"),
        ("m55", "assembly/doom/generated/m55/doom_line_trace_m55.wasm", "docs/reports/evidence/m55/benchmark.json"),
    ):
        wasm_path = ELITE_LAB_ROOT / wasm_name
        sha256 = hashlib.sha256(wasm_path.read_bytes()).hexdigest()
        ev = json.loads((ELITE_LAB_ROOT / ev_name).read_text(encoding="utf-8"))
        sha_match = ev.get("moduleSha256") == sha256
        records[milestone] = {
            "wasm_bytes": wasm_path.stat().st_size,
            "module_sha256": sha256,
            "evidence_sha_match": sha_match,
            "evidence_path": ev_name,
            "evidence": ev,
        }
    return records


def verify_s3cng_corpus() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_v7_differential_corpus.py", "-q"],
        cwd=str(S3CNG_WT_ROOT),
        capture_output=True,
        text=True,
        check=True,
    )
    out = proc.stdout.strip()
    return {
        "repo_sha": _git_sha(S3CNG_WT_ROOT),
        "command": "python3 -m pytest tests/test_v7_differential_corpus.py -q",
        "exit_code": proc.returncode,
        "output": out,
    }


def main() -> int:
    crchain_rows = benchmark_crchain_native()
    x86_sci = benchmark_x86_scientific()
    compact_v19 = benchmark_compact_v19()
    doom_wasm = benchmark_doom_wasm()
    s3cng = verify_s3cng_corpus()

    payload = {
        "campaign": "S3_V5_ECOSYSTEM_FORGE",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "commits": {
            "S3": _git_sha(S3_ROOT),
            "S3-Elite-Lab": _git_sha(ELITE_LAB_ROOT),
            "S3-Benchmarks": _git_sha(BENCH_ROOT),
            "S3-wt-compact-v18": _git_sha(COMPACT_WT_ROOT),
            "S3-wt-s3cng": _git_sha(S3CNG_WT_ROOT),
        },
        "crchain_native": crchain_rows,
        "x86_64_scientific": x86_sci,
        "compact_v19": {
            "payload_sha256_identity": compact_v19.get("payload_sha256_identity", {}),
            "speedups_vs_wt_local_O0": compact_v19.get("speedups_vs_wt_local_O0", {}),
            "modes_summary": {
                mode: {
                    "opt_level": info.get("opt_level"),
                    "corpora": {
                        cname: {
                            "encode_mb_per_sec": round(cinfo.get("encode_mb_per_sec", 0.0), 2),
                            "decode_mb_per_sec": round(cinfo.get("decode_mb_per_sec", 0.0), 2),
                            "output_bytes": cinfo.get("output_bytes"),
                        }
                        for cname, cinfo in info.get("corpora", {}).items()
                    },
                }
                for mode, info in compact_v19.get("modes", {}).items()
            },
        },
        "doom_wasm": doom_wasm,
        "s3cng_corpus": s3cng,
    }

    out_json = THIS_DIR / "results.json"
    out_csv = THIS_DIR / "results.csv"
    out_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    csv_rows: list[dict[str, Any]] = []
    for row in crchain_rows:
        csv_rows.append(
            {
                "CATEGORY": "PREDICTIVE_CRCHAIN",
                "BENCHMARK_ID": row["BENCHMARK_ID"],
                "SIZE_OR_STEPS": row["T_STEPS"],
                "BASELINE_MS_OR_MBS": row["STD_MEDIAN_MS"],
                "CANDIDATE_MS_OR_MBS": row["CRCHAIN_MEDIAN_MS"],
                "SPEEDUP": row["SPEEDUP"],
                "VALIDITY": row["NUMERICAL_VALIDITY"],
            }
        )
    for row in x86_sci["simd_dot_vs_gcc"]:
        csv_rows.append(
            {
                "CATEGORY": "X86_64_SIMD_DOT",
                "BENCHMARK_ID": f"SIMD_DOT_N{row['n']}",
                "SIZE_OR_STEPS": row["n"],
                "BASELINE_MS_OR_MBS": row["s3_scalar_ms"],
                "CANDIDATE_MS_OR_MBS": row["s3_simd_ms"],
                "SPEEDUP": row["simd_vs_scalar_speedup"],
                "VALIDITY": "VALID" if row["max_abs_diff_vs_gcc"] < 1e-9 else "INVALID",
            }
        )
    for row in x86_sci["poisson2d_chunked_vs_gcc"]:
        csv_rows.append(
            {
                "CATEGORY": "POISSON2D_CG_JACOBI",
                "BENCHMARK_ID": f"POISSON_{row['grid']}",
                "SIZE_OR_STEPS": row["n_unknowns"],
                "BASELINE_MS_OR_MBS": row["gcc_exec_ms"],
                "CANDIDATE_MS_OR_MBS": row["s3_exec_ms"],
                "SPEEDUP": round(row["gcc_exec_ms"] / max(1e-9, row["s3_exec_ms"]), 3),
                "VALIDITY": row["NUMERICAL_VALIDITY"],
            }
        )
    for cname, sp in payload["compact_v19"]["speedups_vs_wt_local_O0"].items():
        base_mbs = payload["compact_v19"]["modes_summary"]["wt_local_O0"]["corpora"][cname]["encode_mb_per_sec"]
        cand_mbs = payload["compact_v19"]["modes_summary"]["s3_v5_O1_default"]["corpora"][cname]["encode_mb_per_sec"]
        csv_rows.append(
            {
                "CATEGORY": "S3_COMPACT_TURBO_MB_S",
                "BENCHMARK_ID": f"COMPACT_{cname}",
                "SIZE_OR_STEPS": payload["compact_v19"]["modes_summary"]["s3_v5_O1_default"]["corpora"][cname]["output_bytes"],
                "BASELINE_MS_OR_MBS": base_mbs,
                "CANDIDATE_MS_OR_MBS": cand_mbs,
                "SPEEDUP": round(sp.get("s3_v5_O1_default", 0.0), 2),
                "VALIDITY": "VALID" if payload["compact_v19"]["payload_sha256_identity"].get(cname) else "INVALID",
            }
        )

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        writer.writeheader()
        writer.writerows(csv_rows)

    print(f"V5 suite complete -> {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
