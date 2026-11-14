"""Reproducible V5.5 Psychohistory & Discovery Benchmark Suite.

Fairly benchmarks S3 Native (O1, scientific 50M budget) vs GCC -O3 C11 vs Python,
measures automatic pattern discovery speedups & negative controls, evaluates
out-of-sample statistical predictors & calibration, tests 5-way unknown routing,
verifies H1-H6 collective scaling across N=100..1,000,000, and validates bit parity.
"""

from __future__ import annotations

import csv
import ctypes
from dataclasses import asdict, replace
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from typing import Any

_THIS_DIR = Path(__file__).resolve().parent
_BENCH_ROOT = _THIS_DIR.parent.parent
_WORKSPACE = _BENCH_ROOT.parent
_S3_REPO = _WORKSPACE / "S3"

if str(_S3_REPO) not in sys.path:
    sys.path.insert(0, str(_S3_REPO))

from bootstrap.s3 import OptimizationLevel, compile_source
from bootstrap.s3.backends.x86_64.backend import SCIENTIFIC_MAX_INSTRUCTIONS
from bootstrap.s3.ffi import build_shared_library_from_compilation
from bootstrap.s3.predictive_discovery import DiscoveryStatus, discover_ir_patterns
from bootstrap.s3.psychohistory import (
    CollectiveSimConfig,
    benchmark_checkpoint_compression,
    classify_and_route_unknown_series,
    compile_native_backends,
    evaluate_forecasters,
    evaluate_hypotheses_h1_to_h6,
    run_collective_simulation,
    run_ensemble_simulations,
)


def _c_i64_call(so_path: Path, fn_name: str, argtypes: list[object], *args: int) -> int:
    lib = ctypes.CDLL(str(so_path))
    fn = getattr(lib, fn_name)
    fn.argtypes = argtypes
    fn.restype = ctypes.c_int64
    return int(fn(*args))


def _time_native_fn(fn: Any, argtypes: list[object], args: tuple[int, ...], repeats: int = 30) -> tuple[int, float]:
    fn.argtypes = argtypes
    fn.restype = ctypes.c_int64
    # Warmup
    out = int(fn(*args))
    best_ms = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        out = int(fn(*args))
        best_ms = min(best_ms, (time.perf_counter() - t0) * 1000.0)
    return out, best_ms


def _run_discovery_benchmarks(tmp_dir: Path) -> dict[str, Any]:
    div_src = """
export fn sum_triangular(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 0
    while i < n:
        num: i64 = i * (i + 1)
        term: i64 = num / 2
        acc = acc + term
        i = i + 1
    return acc

fn main() -> i64:
    return sum_triangular(5)
"""
    coupled_src = """
export fn coupled_exchange_sum(n: i64, x0: i64, y0: i64) -> i64:
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
    return coupled_exchange_sum(5, 10, 20)
"""
    neg_chaos = """
export fn logistic_map_steps(n: i64, x0: i64) -> i64:
    mut i: i64 = 0
    mut x: i64 = x0
    while i < n:
        x = (39 * x * (1000 - x)) / 10000
        i = i + 1
    return x

fn main() -> i64:
    return logistic_map_steps(5, 250)
"""
    cases = [
        ("sum_triangular", div_src, [ctypes.c_int64], (10, 100, 10_000, 100_000), lambda t: (t,)),
        (
            "coupled_exchange_sum",
            coupled_src,
            [ctypes.c_int64, ctypes.c_int64, ctypes.c_int64],
            (6, 100, 10_000, 100_000),
            lambda t: (t, 15, -7),
        ),
    ]
    rows: list[dict[str, Any]] = []
    for fn_name, src, argtypes, t_vals, arg_fn in cases:
        c_def = compile_source(src, OptimizationLevel.O1, predictive_exact=False)
        c_opt = compile_source(src, OptimizationLevel.O1, predictive_exact=True, predictive_small_t_cutoff=12)
        drep = discover_ir_patterns(c_def.ir, fn_name)
        so_def = build_shared_library_from_compilation(
            c_def, tmp_dir / f"{fn_name}_def.so", max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS
        )
        so_opt = build_shared_library_from_compilation(
            c_opt, tmp_dir / f"{fn_name}_opt.so", max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS
        )
        lib_def = ctypes.CDLL(str(so_def))
        lib_opt = ctypes.CDLL(str(so_opt))
        fn_def = getattr(lib_def, fn_name)
        fn_opt = getattr(lib_opt, fn_name)
        for t in t_vals:
            args = arg_fn(t)
            out_def, ms_def = _time_native_fn(fn_def, argtypes, args, repeats=25 if t >= 10_000 else 100)
            out_opt, ms_opt = _time_native_fn(fn_opt, argtypes, args, repeats=200)
            assert out_def == out_opt, f"Parity mismatch on {fn_name} T={t}: {out_def} vs {out_opt}"
            rows.append({
                "kernel": fn_name,
                "T": t,
                "pattern_class": drep.patterns[0].pattern_class,
                "verification_status": drep.patterns[0].verification_status,
                "default_ms": ms_def,
                "discovered_opt_ms": ms_opt,
                "speedup": ms_def / max(1e-9, ms_opt),
                "output_i64": out_opt,
                "parity_exact": True,
            })

    c_neg = compile_source(neg_chaos, OptimizationLevel.O1, predictive_exact=True)
    d_neg = discover_ir_patterns(c_neg.ir, "logistic_map_steps")
    return {
        "speedup_rows": rows,
        "negative_control": {
            "function": "logistic_map_steps",
            "status": d_neg.patterns[0].verification_status,
            "pattern_class": d_neg.patterns[0].pattern_class,
            "lowered": "logistic_map_steps" in c_neg.predictive_lowered_functions,
        },
    }


def _run_scaling_benchmarks(artifacts: Any) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    specs = [
        ("independent", (100, 1_000, 10_000, 100_000, 1_000_000), dict(p_up=0.58, turnover=0.90)),
        ("curie_weiss", (100, 1_000, 10_000, 100_000, 1_000_000), dict(coupling_j=0.65, ext_field=0.05, turnover=0.70)),
        ("ring_k4", (100, 1_000, 10_000, 100_000, 1_000_000), dict(coupling_j=1.35, ext_field=0.0, turnover=0.70)),
    ]
    for model, ns, params in specs:
        for n in ns:
            steps = 20 if n <= 100_000 else 6
            cfg_s3 = CollectiveSimConfig(model=model, n_agents=n, steps=steps, seed=101, backend="s3_native", **params)
            cfg_c11 = replace(cfg_s3, backend="c11_gcc_o3")
            t_s3 = run_collective_simulation(cfg_s3, artifacts=artifacts)
            t_c11 = run_collective_simulation(cfg_c11, artifacts=artifacts)

            max_abs_err = max(abs(a - b) for a, b in zip(t_s3.magnetization, t_c11.magnetization))
            assert max_abs_err == 0.0
            assert t_s3.final_sample_states == t_c11.final_sample_states

            py_ms = None
            py_speedup = None
            if n <= 100_000:
                cfg_py = replace(cfg_s3, backend="python")
                t_py = run_collective_simulation(cfg_py, artifacts=artifacts)
                assert t_py.magnetization == t_s3.magnetization
                py_ms = t_py.wall_ms
                py_speedup = py_ms / max(1e-9, t_s3.wall_ms)

            rows.append({
                "model": model,
                "n_agents": n,
                "steps": steps,
                "s3_native_ms": t_s3.wall_ms,
                "c11_gcc_o3_ms": t_c11.wall_ms,
                "python_ms": py_ms,
                "s3_throughput_agent_steps_s": t_s3.agent_steps_per_sec,
                "c11_throughput_agent_steps_s": t_c11.agent_steps_per_sec,
                "s3_vs_c11_ratio": t_s3.wall_ms / max(1e-9, t_c11.wall_ms),
                "s3_vs_python_speedup": py_speedup,
                "peak_rss_kb": t_s3.peak_rss_kb,
                "max_abs_err_vs_c11": max_abs_err,
            })
    return {"scaling_rows": rows}


def _run_prediction_and_routing_benchmarks(artifacts: Any) -> dict[str, Any]:
    pred_rows: list[dict[str, Any]] = []
    trajs = {
        "independent_N10k": (
            run_collective_simulation(
                CollectiveSimConfig(model="independent", n_agents=10_000, steps=120, p_up=0.58, turnover=0.80, seed=77, backend="s3_native"),
                artifacts=artifacts,
            ).magnetization,
            None,
            None,
        ),
        "curie_weiss_j0.4": (
            run_collective_simulation(
                CollectiveSimConfig(model="curie_weiss", n_agents=10_000, steps=120, coupling_j=0.40, ext_field=0.10, turnover=0.60, seed=77, backend="s3_native"),
                artifacts=artifacts,
            ).magnetization,
            0.40,
            0.10,
        ),
        "curie_weiss_j1.0_crit": (
            run_collective_simulation(
                CollectiveSimConfig(model="curie_weiss", n_agents=10_000, steps=120, coupling_j=1.0, ext_field=0.0, turnover=0.60, seed=77, backend="s3_native"),
                artifacts=artifacts,
            ).magnetization,
            1.0,
            0.0,
        ),
        "regime_shock": (
            run_collective_simulation(
                CollectiveSimConfig(model="regime_shock", n_agents=10_000, steps=120, coupling_j=0.50, shock_prob=0.08, shock_amp=0.90, seed=77, backend="s3_native"),
                artifacts=artifacts,
            ).magnetization,
            0.50,
            0.0,
        ),
        "congestion_flow": (
            run_collective_simulation(
                CollectiveSimConfig(model="congestion", n_agents=2_000, steps=120, ext_field=0.35, turnover=0.60, seed=77, backend="python"),
                artifacts=artifacts,
            ).magnetization,
            None,
            None,
        ),
    }

    for name, (series, cj, hf) in trajs.items():
        for horizon in (1, 5):
            cmp_rep = evaluate_forecasters(series, series_name=name, horizon=horizon, coupling_j=cj, ext_field=hf)
            for ev in cmp_rep.evaluations:
                pred_rows.append({
                    "series": name,
                    "horizon": horizon,
                    "model": ev.model_name,
                    "mae": ev.mae,
                    "rmse": ev.rmse,
                    "relative_error": ev.relative_error,
                    "picp_90": ev.prediction_interval_coverage,
                    "calibration_error": ev.calibration_error,
                    "mean_interval_width": ev.mean_interval_width,
                    "interval_score_90": ev.interval_score_90,
                    "is_best_rmse": ev.model_name == cmp_rep.best_model_by_rmse,
                })

    # Blind 5-way strategy classification across 7 distinct unknown generators
    aff_src = """
export fn sum_seq(n: i64) -> i64:
    mut i: i64 = 0
    mut s: i64 = 0
    while i < n:
        s = s + 2 * i + 1
        i = i + 1
    return s
fn main() -> i64:
    return sum_seq(5)
"""
    comp_ir = compile_source(aff_src, OptimizationLevel.O1)
    x = 0.217
    chaos: list[float] = []
    for _ in range(100):
        x = 3.9 * x * (1.0 - x)
        chaos.append(x)

    unknown_cases = [
        classify_and_route_unknown_series([float(k * k) for k in range(50)], series_name="ir_verified_affine", ir_module=comp_ir.ir, fn_name="sum_seq"),
        classify_and_route_unknown_series([float((k * 3) % 7) for k in range(60)], series_name="periodic_mod_7_no_ir"),
        classify_and_route_unknown_series(chaos, series_name="logistic_chaos_r3.9"),
        classify_and_route_unknown_series(trajs["curie_weiss_j0.4"][0], series_name="weak_coupled_abm"),
        classify_and_route_unknown_series(trajs["curie_weiss_j1.0_crit"][0], series_name="critical_coupled_abm"),
        classify_and_route_unknown_series(trajs["regime_shock"][0], series_name="shocked_regime_shift"),
        classify_and_route_unknown_series([0.1, 0.25, -0.05, 0.3], series_name="short_insufficient"),
    ]
    return {
        "prediction_rows": pred_rows,
        "unknown_routing": [asdict(u) for u in unknown_cases],
    }


def _run_scaling_exponents_and_compression(artifacts: Any) -> dict[str, Any]:
    seeds = (11, 22, 33, 44, 55, 66)
    ns = (100, 1_000, 10_000, 100_000)
    hyp_results = evaluate_hypotheses_h1_to_h6(artifacts=artifacts, seeds=seeds, scale_ns=ns)
    compression_rows = [
        benchmark_checkpoint_compression(n_agents=n, seed=42, bias=0.65)
        for n in (10_000, 100_000, 1_000_000)
    ]
    doom_summary = None
    doom_bench = _WORKSPACE / "S3-Elite-Lab" / "docs" / "reports" / "evidence" / "m55" / "benchmark.json"
    if doom_bench.exists():
        doom_data = json.loads(doom_bench.read_text(encoding="utf-8"))
        doom_summary = {
            "source_file": str(doom_bench),
            "read_only_gameplay_unmodified": True,
            "benchmark_keys": sorted(doom_data.keys()),
        }
    return {
        "hypotheses": [asdict(h) for h in hyp_results],
        "checkpoint_compression": compression_rows,
        "optional_doom_telemetry_note": doom_summary,
    }


def _write_outputs(payload: dict[str, Any]) -> None:
    (_THIS_DIR / "results.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    csv_path = _THIS_DIR / "results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["section", "name", "metric_or_n", "value_1", "value_2", "value_3", "notes"])
        for r in payload["discovery"]["speedup_rows"]:
            w.writerow([
                "discovery",
                r["kernel"],
                f"T={r['T']}",
                f"{r['default_ms']:.6f}",
                f"{r['discovered_opt_ms']:.6f}",
                f"{r['speedup']:.2f}x",
                r["pattern_class"],
            ])
        for r in payload["scaling"]["scaling_rows"]:
            w.writerow([
                "scaling",
                r["model"],
                f"N={r['n_agents']}",
                f"{r['s3_native_ms']:.4f}",
                f"{r['c11_gcc_o3_ms']:.4f}",
                f"{r['s3_vs_c11_ratio']:.3f}",
                f"py_ms={r['python_ms']};err={r['max_abs_err_vs_c11']}",
            ])
        for h in payload["hypotheses_and_compression"]["hypotheses"]:
            w.writerow([
                "hypothesis",
                h["hypothesis_id"],
                h["status"],
                json.dumps(h["observed_metrics"]),
                "",
                "",
                h["falsification_criterion"],
            ])

    lines = [
        "# S3 V5.5 Psychohistory & Discovery Benchmark Suite",
        "",
        "Generated cleanly on Linux (`WSL`, Python `3.12.3`, GCC `-O3 -march=native`) using `S3` `O1` native ELF shared libraries (`scientific` 50M budget).",
        "",
        "## 1. Automatic Pattern Discovery (`O(T)` Default vs `O(1)` Discovered Lowered)",
        "",
        "| Kernel | T | Default ms | Discovered Opt ms | Speedup | Status |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for r in payload["discovery"]["speedup_rows"]:
        lines.append(
            f"| `{r['kernel']}` | {r['T']} | {r['default_ms']:.5f} | {r['discovered_opt_ms']:.5f} | {r['speedup']:.2f}x | `{r['verification_status']}` |"
        )
    lines.extend([
        "",
        "## 2. Collective Dynamics Native Scaling (`N = 100 .. 1,000,000`)",
        "",
        "| Model | N Agents | Steps | S3 Native ms | C11 GCC -O3 ms | S3/C11 Ratio | Python ms | S3 vs Python | Max Err vs C11 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ])
    for r in payload["scaling"]["scaling_rows"]:
        py_s = f"{r['python_ms']:.3f}" if r["python_ms"] is not None else "n/a"
        sp_s = f"{r['s3_vs_python_speedup']:.1f}x" if r["s3_vs_python_speedup"] is not None else "n/a"
        lines.append(
            f"| `{r['model']}` | {r['n_agents']} | {r['steps']} | {r['s3_native_ms']:.3f} | {r['c11_gcc_o3_ms']:.3f} | {r['s3_vs_c11_ratio']:.2f}x | {py_s} | {sp_s} | {r['max_abs_err_vs_c11']:.1f} |"
        )
    lines.extend([
        "",
        "## 3. Falsifiable Hypotheses H1-H6 (Multi-Seed, N=100..100,000)",
        "",
        "| Hypothesis | Status | Observed Summary |",
        "| --- | --- | --- |",
    ])
    for h in payload["hypotheses_and_compression"]["hypotheses"]:
        lines.append(f"| `{h['hypothesis_id']}` | `{h['status']}` | `{json.dumps(h['observed_metrics'])}` |")

    lines.extend([
        "",
        "## 4. Blind Unknown Dynamics 5-Way Routing",
        "",
        "| Series | Decision | Detected Regime | IR Proof Status |",
        "| --- | --- | --- | --- |",
    ])
    for u in payload["prediction"]["unknown_routing"]:
        lines.append(f"| `{u['series_name']}` | `{u['decision']}` | `{u['detected_regime']}` | `{u['ir_proof_status']}` |")

    (_THIS_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="s3_v5_5_bench_") as tmp_str:
        tmp_dir = Path(tmp_str)
        artifacts = compile_native_backends(tmp_dir / "kernels")
        discovery = _run_discovery_benchmarks(tmp_dir)
        scaling = _run_scaling_benchmarks(artifacts)
        prediction = _run_prediction_and_routing_benchmarks(artifacts)
        hyp_comp = _run_scaling_exponents_and_compression(artifacts)

    payload = {
        "campaign": "S3_V5_5_PSYCHOHISTORY_RESEARCH",
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "discovery": discovery,
        "scaling": scaling,
        "prediction": prediction,
        "hypotheses_and_compression": hyp_comp,
    }
    _write_outputs(payload)
    print("BENCHMARK_COMPLETE", _THIS_DIR / "results.json")


if __name__ == "__main__":
    main()
