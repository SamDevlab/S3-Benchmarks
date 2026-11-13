"""Reproducible benchmark suite for S3 Predictive Compute V1.

Measures discovery, verification, and execution cost vs conventional S3 native
evaluation and iterative references, including negative controls / fallbacks.
"""

from __future__ import annotations

import csv
import json
import statistics
import subprocess
import sys
import time
from array import array
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
S3_ROOT = BENCH_ROOT.parent / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.predictive_compute import (
    HashlifeEngine,
    PredictiveComputeToolkit,
    run_certified_linear_recurrence,
    run_empirical_sequence_prediction,
    run_hashlife_finite_grid,
)
from examples.compute.cellular_automata_toolkit import create_cellular_toolkit


def _git_sha(repo: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def _bench_ms(fn, warmups: int = 1, samples: int = 5) -> float:
    for _ in range(warmups):
        fn()
    vals = []
    for _ in range(samples):
        t0 = time.perf_counter()
        fn()
        vals.append((time.perf_counter() - t0) * 1000.0)
    return round(statistics.median(vals), 4)


def run_suite() -> dict[str, Any]:
    toolkit = create_cellular_toolkit(backend="native")
    conv_toolkit = create_cellular_toolkit(backend="native")
    pred = PredictiveComputeToolkit(toolkit)
    records: list[dict[str, Any]] = []

    try:
        # 1. Cycle-jump benchmarks (native S3 kernels)
        cases = [
            ("conway_blinker_16x16_t2000", "conway", 16, 16, 2000, "brent", 500),
            ("highlife_blinker_16x16_t2000", "highlife", 16, 16, 2000, "brent", 500),
            ("rule110_w15_t2000", "rule110", 15, 1, 2000, "brent", 500),
            ("cyclic_ternary_8x8_t1000", "cyclic_ternary", 8, 8, 1000, "brent", 500),
            ("rule30_w31_t200_neg_control", "rule30", 31, 1, 200, "brent", 40),
        ]
        for label, ca, w, h, steps, strat, budget in cases:
            init = [0] * (w * h)
            if ca in {"rule30", "rule110"}:
                init[w // 2] = 1
                if ca == "rule110":
                    init[w // 2 + 1] = 1
            elif ca == "cyclic_ternary":
                init = [(r * 3 + c) % 3 for r in range(h) for c in range(w)]
            else:
                cr, cc = h // 2, w // 2
                init[cr * w + cc - 1] = 1
                init[cr * w + cc] = 1
                init[cr * w + cc + 1] = 1

            res_pred = pred.run_steps(ca, init, w, h, steps, strategy=strat, discovery_step_budget=budget)
            if ca in conv_toolkit.prepared:
                conv_toolkit.release(ca)
            prep = conv_toolkit.prepare(ca, w, h, init)
            res_conv_state = prep.run(steps)
            exact_match = list(res_pred.final_state) == list(res_conv_state)

            pred_ms = _bench_ms(
                lambda: pred.run_steps(ca, init, w, h, steps, strategy=strat, discovery_step_budget=budget),
                warmups=1,
                samples=3,
            )
            conv_ms = _bench_ms(
                lambda: (prep.reset(init), prep.run(steps))[1],
                warmups=1,
                samples=3,
            )
            records.append(
                {
                    "benchmark_id": label,
                    "class": "cycle_jump_brent",
                    "ca_or_kernel": ca,
                    "steps": steps,
                    "accelerated": res_pred.accelerated,
                    "method_used": res_pred.certificate.method_used,
                    "soundness_class": res_pred.certificate.soundness_class,
                    "fallback_reason": res_pred.fallback_reason,
                    "discovery_ms": round(res_pred.discovery_ns / 1e6, 4),
                    "verification_ms": round(res_pred.verification_ns / 1e6, 4),
                    "predictive_median_ms": pred_ms,
                    "conventional_median_ms": conv_ms,
                    "speedup": round(conv_ms / max(1e-9, pred_ms), 2),
                    "exact_match": exact_match,
                }
            )

        # 2. Hashlife finite-safe + boundary-unsafe negative control + unbounded long horizon
        w, h = 64, 64
        safe_grid = [0] * (w * h)
        for dr, dc in ((0, 1), (1, 2), (2, 0), (2, 1), (2, 2)):
            safe_grid[(28 + dr) * w + (28 + dc)] = 1
        hl_res = run_hashlife_finite_grid(safe_grid, w, h, 20, rule="conway")
        if "conway" in conv_toolkit.prepared:
            conv_toolkit.release("conway")
        prep_hl = conv_toolkit.prepare("conway", w, h, safe_grid)
        conv_hl_state = prep_hl.run(20)
        hl_ms = _bench_ms(lambda: run_hashlife_finite_grid(safe_grid, w, h, 20, rule="conway"), warmups=1, samples=3)
        conv_hl_ms = _bench_ms(lambda: (prep_hl.reset(safe_grid), prep_hl.run(20))[1], warmups=1, samples=3)
        records.append(
            {
                "benchmark_id": "hashlife_conway_64x64_safe_t20",
                "class": "hashlife_quadtree",
                "ca_or_kernel": "conway",
                "steps": 20,
                "accelerated": hl_res.accelerated,
                "method_used": hl_res.certificate.method_used,
                "soundness_class": hl_res.certificate.soundness_class,
                "fallback_reason": hl_res.fallback_reason,
                "discovery_ms": 0.0,
                "verification_ms": round(hl_res.verification_ns / 1e6, 4),
                "predictive_median_ms": hl_ms,
                "conventional_median_ms": conv_hl_ms,
                "speedup": round(conv_hl_ms / max(1e-9, hl_ms), 2),
                "exact_match": list(hl_res.final_state) == list(conv_hl_state),
            }
        )

        # Unbounded Hashlife long horizon (T=1024)
        glider = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        t0 = time.perf_counter()
        out_1024 = HashlifeEngine("conway").advance_unbounded(glider, 1024)
        hl_1024_ms = round((time.perf_counter() - t0) * 1000.0, 4)
        records.append(
            {
                "benchmark_id": "hashlife_unbounded_glider_t1024",
                "class": "hashlife_quadtree",
                "ca_or_kernel": "conway_unbounded",
                "steps": 1024,
                "accelerated": True,
                "method_used": "hashlife_quadtree",
                "soundness_class": "PROVED_EXACT",
                "fallback_reason": None,
                "discovery_ms": 0.0,
                "verification_ms": 0.0,
                "predictive_median_ms": hl_1024_ms,
                "conventional_median_ms": None,
                "speedup": None,
                "exact_match": out_1024 == {(r + 256, c + 256) for r, c in glider},
            }
        )

        # 3. Linear recurrence matrix exponentiation vs iterative loop (T=10000)
        def _fib_iter(n: int) -> int:
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a

        fib_pred = run_certified_linear_recurrence([1, 1], [0, 1], 10_000)
        fib_iter_val = _fib_iter(10_000)
        fib_pred_ms = _bench_ms(lambda: run_certified_linear_recurrence([1, 1], [0, 1], 10_000), warmups=2, samples=5)
        fib_iter_ms = _bench_ms(lambda: _fib_iter(10_000), warmups=2, samples=5)
        records.append(
            {
                "benchmark_id": "linear_recurrence_fib_t10000",
                "class": "linear_recurrence_matmul",
                "ca_or_kernel": "fibonacci",
                "steps": 10_000,
                "accelerated": fib_pred.accelerated,
                "method_used": fib_pred.certificate.method_used,
                "soundness_class": fib_pred.certificate.soundness_class,
                "fallback_reason": None,
                "discovery_ms": 0.0,
                "verification_ms": 0.0,
                "predictive_median_ms": fib_pred_ms,
                "conventional_median_ms": fib_iter_ms,
                "speedup": round(fib_iter_ms / max(1e-9, fib_pred_ms), 2),
                "exact_match": fib_pred.final_state == fib_iter_val,
            }
        )

        # Negative control: nonlinear quadratic mod 97
        nl = [3]
        for _ in range(200):
            nl.append((nl[-1] * nl[-1] + 1) % 97)
        nl_res = run_empirical_sequence_prediction(
            lambda: nl[:14], prefix_len=14, target_index=150, max_order=4, min_verify_tail=4, conventional_eval=lambda i: nl[i]
        )
        records.append(
            {
                "benchmark_id": "nonlinear_mod97_neg_control",
                "class": "linear_recurrence_matmul",
                "ca_or_kernel": "quadratic_mod97",
                "steps": 150,
                "accelerated": nl_res.accelerated,
                "method_used": nl_res.certificate.method_used,
                "soundness_class": nl_res.certificate.soundness_class,
                "fallback_reason": nl_res.fallback_reason,
                "discovery_ms": round(nl_res.discovery_ns / 1e6, 4),
                "verification_ms": 0.0,
                "predictive_median_ms": round(nl_res.total_ns / 1e6, 4),
                "conventional_median_ms": None,
                "speedup": 1.0,
                "exact_match": nl_res.final_state == nl[150],
            }
        )
    finally:
        toolkit.close()
        conv_toolkit.close()

    return {
        "metadata": {
            "campaign": "S3_PREDICTIVE_COMPUTE_V1",
            "s3_sha": _git_sha(S3_ROOT),
            "benchmarks_sha": _git_sha(BENCH_ROOT),
        },
        "records": records,
    }


def main() -> int:
    report = run_suite()
    out_json = THIS_DIR / "results_predictive_v1.json"
    out_csv = THIS_DIR / "results_predictive_v1.csv"
    out_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    recs = report["records"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(recs[0].keys()))
        writer.writeheader()
        writer.writerows(recs)
    print(f"Predictive Compute V1 suite complete -> {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
