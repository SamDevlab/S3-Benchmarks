#!/usr/bin/env python3
"""S3 V8 Unknown Numerical Dynamics V4 — Blind Split Benchmark & Abstention Calibration."""

from __future__ import annotations

from datetime import datetime, timezone
import json
import math
from pathlib import Path
import sys
import time
from typing import Any

BENCH_DIR = Path(__file__).resolve().parent
BENCH_ROOT = BENCH_DIR.parents[1]
S3_ROOT = BENCH_ROOT.parent / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.predictive_discovery import (  # noqa: E402
    DiscoveryStatus,
    SequenceConfidenceClass,
    discover_ir_patterns,
    discover_sequence_structure,
)


def main() -> int:
    source_ir = """
export fn quasi_m7(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 0
    while i < n:
        acc = acc + ((i * i) / 7)
        i = i + 1
    return acc
fn main() -> i64:
    return quasi_m7(10)
"""
    ir_rep = discover_ir_patterns(
        source_ir,
        "quasi_m7",
        allow_quasi_polynomial_parity=True,
        allow_general_quasi_polynomials=True,
        allow_arbitrary_quasi_polynomials=True,
    )
    proved_pat = ir_rep.patterns[0]
    assert proved_pat.verification_status == DiscoveryStatus.PROVED_EXACT

    pell = [0, 1]
    for _ in range(16):
        pell.append(2 * pell[-1] + pell[-2])

    chebyshev_rec = [1, 2]
    for _ in range(16):
        chebyshev_rec.append(3 * chebyshev_rec[-1] - chebyshev_rec[-2])

    x_log = 0.314159265
    logistic = []
    for _ in range(28):
        x_log = 3.99 * x_log * (1.0 - x_log)
        logistic.append(x_log)

    collatz = [27]
    for _ in range(31):
        x = collatz[-1]
        collatz.append(x // 2 if x % 2 == 0 else 3 * x + 1)

    rng_xs = 2463534242
    xorshift = []
    for _ in range(24):
        rng_xs ^= (rng_xs << 13) & 0xFFFFFFFF
        rng_xs ^= rng_xs >> 17
        rng_xs ^= (rng_xs << 5) & 0xFFFFFFFF
        xorshift.append(rng_xs & 0xFFFF)

    cases: list[dict[str, Any]] = [
        # DESIGN
        {
            "name": "design_cubic_poly",
            "split": "DESIGN",
            "category": "RECOVERABLE",
            "seq": [3 * k**3 - 2 * k + 7 for k in range(20)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "POLYNOMIAL_FINITE_DIFFERENCE",
        },
        {
            "name": "design_quasi_m7_source_verified",
            "split": "DESIGN",
            "category": "RECOVERABLE_SOURCE_PROVED",
            "seq": [(k * k) // 7 for k in range(56)],
            "source_pattern": proved_pat,
            "expected_conf": SequenceConfidenceClass.EXACT_PROVEN,
            "expected_family": "QUASI_POLYNOMIAL_MOD_7",
        },
        {
            "name": "design_pell_recurrence",
            "split": "DESIGN",
            "category": "RECOVERABLE",
            "seq": pell,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "LINEAR_RECURRENCE",
        },
        # VALIDATION
        {
            "name": "val_quasi_m6_obs",
            "split": "VALIDATION",
            "category": "RECOVERABLE",
            "seq": [(k * k) // 6 for k in range(48)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "QUASI_POLYNOMIAL_MOD_6",
        },
        {
            "name": "val_quasi_m9_obs",
            "split": "VALIDATION",
            "category": "RECOVERABLE",
            "seq": [(k * k + k) // 9 for k in range(72)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "QUASI_POLYNOMIAL_MOD_9",
        },
        {
            "name": "val_quasi_m12_obs",
            "split": "VALIDATION",
            "category": "RECOVERABLE",
            "seq": [(k * k + k) // 12 for k in range(96)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "QUASI_POLYNOMIAL_MOD_12",
        },
        {
            "name": "val_continuous_poisson_relaxation",
            "split": "VALIDATION",
            "category": "RECOVERABLE",
            "seq": [1.25 + 8.5 * (0.68**k) for k in range(20)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "CONTINUOUS_GEOMETRIC_RELAXATION",
        },
        # HIDDEN_TEST
        {
            "name": "hidden_quasi_m15_obs",
            "split": "HIDDEN_TEST",
            "category": "RECOVERABLE",
            "seq": [(k * k + k) // 15 for k in range(120)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "QUASI_POLYNOMIAL_MOD_15",
        },
        {
            "name": "hidden_chebyshev_recurrence",
            "split": "HIDDEN_TEST",
            "category": "RECOVERABLE",
            "seq": chebyshev_rec,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "LINEAR_RECURRENCE",
        },
        {
            "name": "hidden_periodic_orbit_7",
            "split": "HIDDEN_TEST",
            "category": "RECOVERABLE",
            "seq": [[5, -1, 8, 2, -4, 7, 0][k % 7] for k in range(35)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "PERIODIC_ORBIT",
        },
        {
            "name": "hidden_damped_oscillator",
            "split": "HIDDEN_TEST",
            "category": "RECOVERABLE",
            "seq": [(0.88**k) * math.cos(0.37 * k) for k in range(24)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "CONTINUOUS_LINEAR_RECURRENCE_O2",
        },
        # ADVERSARIAL_TEST
        {
            "name": "adv_spoof_polynomial_prefix",
            "split": "ADVERSARIAL_TEST",
            "category": "NEGATIVE_CONTROL",
            "seq": [k * k + (0 if k < 14 else (k - 13) ** 3) for k in range(20)],
            "source_pattern": proved_pat,
            "expected_conf": SequenceConfidenceClass.REJECTED,
            "expected_family": "FALSIFIED_POLYNOMIAL_PREFIX_SPOOF",
        },
        {
            "name": "adv_spoof_geometric_regime_shift",
            "split": "ADVERSARIAL_TEST",
            "category": "NEGATIVE_CONTROL",
            "seq": [1.25 + 8.5 * (0.68**k) for k in range(17)]
            + [1.25 + 8.5 * (0.68**16) * (0.95 ** (k - 16)) for k in range(17, 22)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.REJECTED,
            "expected_family": "FALSIFIED_GEOMETRIC_PREFIX_SPOOF",
        },
        {
            "name": "adv_collatz_hailstone_27",
            "split": "ADVERSARIAL_TEST",
            "category": "NEGATIVE_CONTROL",
            "seq": collatz,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "adv_chaotic_logistic_r3_99",
            "split": "ADVERSARIAL_TEST",
            "category": "NEGATIVE_CONTROL",
            "seq": logistic,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "adv_xorshift32_prng",
            "split": "ADVERSARIAL_TEST",
            "category": "NEGATIVE_CONTROL",
            "seq": xorshift,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "adv_noisy_continuous_decay",
            "split": "ADVERSARIAL_TEST",
            "category": "NEGATIVE_CONTROL",
            "seq": [1.25 + 8.5 * (0.68**k) + 0.05 * math.sin(2.3 * k) for k in range(24)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "adv_short_ambiguous_len5",
            "split": "ADVERSARIAL_TEST",
            "category": "NEGATIVE_CONTROL",
            "seq": [1, 2, 4, 7, 11],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.INSUFFICIENT_EVIDENCE,
            "expected_family": "INSUFFICIENT_SAMPLE_LENGTH",
        },
    ]

    records: list[dict[str, Any]] = []
    recoverable_total = 0
    recoverable_matched = 0
    negative_total = 0
    false_positives = 0
    epistemic_leaks = 0
    by_split: dict[str, dict[str, int]] = {}

    for c in cases:
        t0 = time.perf_counter()
        rep = discover_sequence_structure(
            c["seq"],
            sequence_name=c["name"],
            horizon=4,
            source_pattern=c["source_pattern"],
        )
        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        assert rep.confidence_class == c["expected_conf"], (c["name"], rep)
        assert rep.discovered_family == c["expected_family"], (c["name"], rep)
        sp = by_split.setdefault(c["split"], {"total": 0, "passed": 0})
        sp["total"] += 1
        sp["passed"] += 1
        if c["source_pattern"] is None and rep.confidence_class == SequenceConfidenceClass.EXACT_PROVEN:
            epistemic_leaks += 1
        if c["category"].startswith("RECOVERABLE"):
            recoverable_total += 1
            recoverable_matched += 1
        else:
            negative_total += 1
            if rep.confidence_class in (
                SequenceConfidenceClass.EXACT_PROVEN,
                SequenceConfidenceClass.APPROXIMATE_FORECAST,
            ):
                false_positives += 1
        row = rep.to_dict()
        row["split"] = c["split"]
        row["category"] = c["category"]
        row["elapsed_ms"] = round(elapsed_ms, 4)
        records.append(row)

    payload = {
        "campaign": "S3_V8_MATHEMATICAL_COMPILER_FUSION",
        "suite": "UNKNOWN_NUMERICAL_DYNAMICS_V4",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_cases": len(cases),
            "recoverable_total": recoverable_total,
            "recoverable_matched": recoverable_matched,
            "negative_control_total": negative_total,
            "false_positive_discoveries": false_positives,
            "epistemic_proof_leaks": epistemic_leaks,
            "by_split": by_split,
            "all_assertions_passed": True,
        },
        "cases": records,
    }
    out_path = BENCH_DIR / "results_v8_unknown_dynamics_v4.json"
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
