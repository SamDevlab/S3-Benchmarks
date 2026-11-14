#!/usr/bin/env python3
"""S3 V7 Unknown Numerical Dynamics V3 Benchmark & Calibration Suite."""

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
export fn quasi_m5(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 0
    while i < n:
        acc = acc + ((i * i * i) / 5)
        i = i + 1
    return acc
fn main() -> i64:
    return quasi_m5(10)
"""
    ir_rep = discover_ir_patterns(
        source_ir,
        "quasi_m5",
        allow_quasi_polynomial_parity=True,
        allow_general_quasi_polynomials=True,
    )
    proved_pat = ir_rep.patterns[0]
    assert proved_pat.verification_status == DiscoveryStatus.PROVED_EXACT

    pell = [0, 1]
    for _ in range(14):
        pell.append(2 * pell[-1] + pell[-2])

    affine = [1]
    for _ in range(15):
        affine.append(2 * affine[-1] + 3)

    x_log = 0.314159265
    logistic = []
    for _ in range(24):
        x_log = 3.99 * x_log * (1.0 - x_log)
        logistic.append(x_log)

    rng_x = 1234567
    lcg = []
    for _ in range(24):
        rng_x = (rng_x * 1103515245 + 12345) & 0x7FFFFFFF
        lcg.append(rng_x % 997)

    rng_xs = 2463534242
    xorshift = []
    for _ in range(24):
        rng_xs ^= (rng_xs << 13) & 0xFFFFFFFF
        rng_xs ^= rng_xs >> 17
        rng_xs ^= (rng_xs << 5) & 0xFFFFFFFF
        xorshift.append(rng_xs & 0xFFFF)

    cases: list[dict[str, Any]] = [
        {
            "name": "cubic_poly_obs",
            "category": "RECOVERABLE",
            "seq": [3 * k**3 - 2 * k + 7 for k in range(20)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "POLYNOMIAL_FINITE_DIFFERENCE",
        },
        {
            "name": "quasi_m3_obs",
            "category": "RECOVERABLE",
            "seq": [(k * k) // 3 for k in range(32)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "QUASI_POLYNOMIAL_MOD_3",
        },
        {
            "name": "quasi_m5_source_verified",
            "category": "RECOVERABLE_SOURCE_PROVED",
            "seq": [(k * k * k) // 5 for k in range(40)],
            "source_pattern": proved_pat,
            "expected_conf": SequenceConfidenceClass.EXACT_PROVEN,
            "expected_family": "QUASI_POLYNOMIAL_MOD_5",
        },
        {
            "name": "quasi_m6_v3_obs",
            "category": "RECOVERABLE",
            "seq": [(k * k) // 6 for k in range(48)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "QUASI_POLYNOMIAL_MOD_6",
        },
        {
            "name": "quasi_m10_v3_obs",
            "category": "RECOVERABLE",
            "seq": [(k * k) // 10 for k in range(80)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "QUASI_POLYNOMIAL_MOD_10",
        },
        {
            "name": "pell_recurrence",
            "category": "RECOVERABLE",
            "seq": pell,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "LINEAR_RECURRENCE",
        },
        {
            "name": "affine_forced_recurrence",
            "category": "RECOVERABLE",
            "seq": affine,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "LINEAR_RECURRENCE",
        },
        {
            "name": "periodic_orbit_6",
            "category": "RECOVERABLE",
            "seq": [[4, -2, 7, 1, 9, -3][k % 6] for k in range(30)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "PERIODIC_ORBIT",
        },
        {
            "name": "continuous_poisson_relaxation",
            "category": "RECOVERABLE",
            "seq": [1.25 + 8.5 * (0.68**k) for k in range(20)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "CONTINUOUS_GEOMETRIC_RELAXATION",
        },
        {
            "name": "continuous_damped_oscillator",
            "category": "RECOVERABLE",
            "seq": [(0.85**k) * math.cos(0.45 * k) for k in range(24)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.APPROXIMATE_FORECAST,
            "expected_family": "CONTINUOUS_LINEAR_RECURRENCE_O2",
        },
        {
            "name": "spoof_polynomial_prefix",
            "category": "NEGATIVE_CONTROL",
            "seq": [k * k + (0 if k < 14 else (k - 13) ** 3) for k in range(20)],
            "source_pattern": proved_pat,
            "expected_conf": SequenceConfidenceClass.REJECTED,
            "expected_family": "FALSIFIED_POLYNOMIAL_PREFIX_SPOOF",
        },
        {
            "name": "spoof_geometric_regime_shift",
            "category": "NEGATIVE_CONTROL",
            "seq": [1.25 + 8.5 * (0.68**k) for k in range(17)]
            + [1.25 + 8.5 * (0.68**16) * (0.95 ** (k - 16)) for k in range(17, 22)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.REJECTED,
            "expected_family": "FALSIFIED_GEOMETRIC_PREFIX_SPOOF",
        },
        {
            "name": "noisy_continuous_decay",
            "category": "NEGATIVE_CONTROL",
            "seq": [1.25 + 8.5 * (0.68**k) + 0.05 * math.sin(2.3 * k) for k in range(24)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "noisy_integer_poly_aperiodic_perturbation",
            "category": "NEGATIVE_CONTROL",
            "seq": [k * k + (((k * 131 + k * k * 17) % 19) - 9) + ((k * 29) % 13 - 6) for k in range(24)],
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "chaotic_logistic_r3_99",
            "category": "NEGATIVE_CONTROL",
            "seq": logistic,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "lcg_prng_mod_997",
            "category": "NEGATIVE_CONTROL",
            "seq": lcg,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "xorshift32_prng",
            "category": "NEGATIVE_CONTROL",
            "seq": xorshift,
            "source_pattern": None,
            "expected_conf": SequenceConfidenceClass.UNIDENTIFIABLE,
            "expected_family": "CHAOTIC_OR_HIGH_ENTROPY",
        },
        {
            "name": "short_ambiguous_len5",
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
        if c["source_pattern"] is None and rep.confidence_class == SequenceConfidenceClass.EXACT_PROVEN:
            epistemic_leaks += 1
        if c["category"].startswith("RECOVERABLE"):
            recoverable_total += 1
            if rep.confidence_class == c["expected_conf"] and rep.discovered_family == c["expected_family"]:
                recoverable_matched += 1
        else:
            negative_total += 1
            if rep.confidence_class in (
                SequenceConfidenceClass.EXACT_PROVEN,
                SequenceConfidenceClass.APPROXIMATE_FORECAST,
            ):
                false_positives += 1
        row = rep.to_dict()
        row["category"] = c["category"]
        row["elapsed_ms"] = round(elapsed_ms, 4)
        records.append(row)

    payload = {
        "campaign": "S3_V7_NATIVE_INTELLIGENCE_AND_COMPILER_SUPREMACY",
        "wave": "WAVE_16_UNKNOWN_NUMERICAL_DYNAMICS_V3",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_cases": len(cases),
            "recoverable_total": recoverable_total,
            "recoverable_matched": recoverable_matched,
            "negative_control_total": negative_total,
            "false_positive_discoveries": false_positives,
            "epistemic_proof_leaks": epistemic_leaks,
            "all_assertions_passed": True,
        },
        "cases": records,
    }
    out_path = BENCH_DIR / "results_v7_unknown_dynamics.json"
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
