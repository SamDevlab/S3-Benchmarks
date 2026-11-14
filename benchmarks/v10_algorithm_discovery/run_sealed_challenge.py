#!/usr/bin/env python3
"""Evaluate frozen generic engine on post-freeze unseen GF(2) oracles.

The evaluator is independent of blackbox_gf2.py. This is *not* evidence that
the S3 compiler automatically discovered an algorithm; engine is Python-only.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import random
import statistics
import subprocess
import time

from blackbox_gf2 import infer_gf2_map, NotCertified
from sealed_challenge import cases, rotate

HERE = Path(__file__).resolve().parent
N_STEPS = [0, 1, 2, 3, 7, 17, 31, 64, 127]


def cyclic_product(a: int, b: int, width: int) -> int:
    """Independent polynomial multiplication mod x^width-1 over GF(2)."""
    value = 0
    while a:
        bit = a & -a
        a ^= bit
        value ^= rotate(b, bit.bit_length()-1, width)
    return value


def cyclic_power(poly: int, n: int, width: int) -> int:
    out = 1
    while n:
        if n & 1:
            out = cyclic_product(out, poly, width)
        poly = cyclic_product(poly, poly, width)
        n >>= 1
    return out


def iterate(step, state, n):
    for _ in range(n):
        state = step(state)
    return state


def timed(fn, rounds=5):
    samples = []
    result = None
    for _ in range(rounds):
        t = time.perf_counter_ns()
        result = fn()
        samples.append(time.perf_counter_ns() - t)
    return result, statistics.median(samples)


def evaluation():
    rng = random.Random(225091)
    rows = []
    for challenge in cases():
        entry = {
            "case": challenge.id,
            "width": challenge.width,
            "heldout_expected_linear": challenge.expected_linear,
            "family_for_independent_evaluation_only": challenge.family,
        }
        t = time.perf_counter_ns()
        try:
            model = infer_gf2_map(challenge.step, challenge.width, probes=128, seed=4051)
        except NotCertified as error:
            entry["inference_result"] = "REJECTED"
            entry["rejection"] = str(error)
            entry["discovery_ms"] = round((time.perf_counter_ns()-t)/1e6, 4)
            entry["outcome"] = "CORRECT_REJECTION" if not challenge.expected_linear else "FALSE_REJECTION"
            rows.append(entry)
            print(challenge.id, entry["outcome"], entry["rejection"], flush=True)
            continue
        entry["discovery_ms"] = round((time.perf_counter_ns()-t)/1e6, 4)
        entry["inference_result"] = model.status
        entry["exhaustive"] = model.exhaustive
        entry["oracle_calls"] = model.oracle_calls
        entry["verification_checks"] = model.checks

        # Never use held-out oracle characteristics inside inference.
        points = [0, (1 << challenge.width)-1, 1, 2, 3]
        points += [rng.getrandbits(challenge.width) for _ in range(30)]
        if challenge.rare_trigger is not None:
            points.append(challenge.rare_trigger)  # hidden adversarial holdout after inference
        errors = []
        evaluated = 0
        for state in points:
            for n in N_STEPS:
                oracle_answer = iterate(challenge.step, state, n)
                candidate_answer = model.advance(state, n)
                evaluated += 1
                if oracle_answer != candidate_answer:
                    errors.append({"state": state, "N": n, "oracle": oracle_answer, "candidate": candidate_answer})
                    if len(errors) >= 5:
                        break
            if len(errors) >= 5:
                break
        entry["holdout_checks"] = evaluated
        entry["holdout_errors_first_five"] = errors
        entry["holdout_parity"] = not errors

        # Rule-specific reference is only available to external evaluator,
        # never passed to the discovery engine.
        if challenge.polynomial is not None and not errors:
            for n in (4096, 1000003):
                for state in [1, 0x12345678 & ((1<<challenge.width)-1)]:
                    expected = cyclic_product(
                        cyclic_power(challenge.polynomial, n, challenge.width),
                        state, challenge.width)
                    got = model.advance(state, n)
                    evaluated += 1
                    if expected != got:
                        errors.append({"state":state,"N":n,"oracle_independent_polynomial":expected,"candidate":got})
            entry["high_N_independent_polynomial_checks"] = 4
            entry["holdout_parity"] = not errors

        if not challenge.expected_linear:
            entry["outcome"] = "UNSAFE_FALSE_ACCEPT" if not errors else "HOLDOUT_DETECTED_UNSAFE_CANDIDATE"
        elif errors:
            entry["outcome"] = "FALSE_ACCEPTED_BAD_TRANSFORMATION"
        else:
            entry["outcome"] = "PASS_POST_FREEZE_HOLDOUT"
            entry["timings"] = {}
            # Runtime measurements here include Python call overhead: they are
            # only exploratory and must not be described as native S3/GCC benchmarks.
            for n in (100, 1000, 10000, 100000):
                state = rng.getrandbits(challenge.width)
                got_baseline, conventional_ns = timed(lambda: iterate(challenge.step, state, n))
                got_candidate, candidate_ns = timed(lambda: model.advance(state, n))
                if got_baseline != got_candidate:
                    raise AssertionError("benchmark state mismatch")
                special_ns = None
                if challenge.polynomial is not None:
                    got_special, special_ns = timed(lambda: cyclic_product(
                        cyclic_power(challenge.polynomial, n, challenge.width),
                        state, challenge.width))
                    if got_special != got_candidate:
                        raise AssertionError("independent polynomial benchmark mismatch")
                entry["timings"][str(n)] = {
                    "direct_iterative_python_ns": conventional_ns,
                    "inferred_matrix_python_ns": candidate_ns,
                    "known_cyclic_polynomial_python_ns": special_ns,
                    "speedup_vs_direct_only": round(conventional_ns / candidate_ns, 3),
                }
        rows.append(entry)
        print(challenge.id, entry["outcome"],
              f"checks={entry['holdout_checks']}",
              f"discover_ms={entry['discovery_ms']}", flush=True)

    positive = [r for r in rows if r["heldout_expected_linear"]]
    negative = [r for r in rows if not r["heldout_expected_linear"]]
    unsafe = [r for r in negative if r["outcome"] in ("UNSAFE_FALSE_ACCEPT", "HOLDOUT_DETECTED_UNSAFE_CANDIDATE")]
    return {
        "campaign": "S3_V10_GENERIC_Gf2_ALGORITHM_DISCOVERY_CHALLENGE",
        "classification": "PYTHON_BLACK_BOX_DISCOVERY_EXPERIMENT_NOT_INTEGRATED_WITH_S3_COMPILER",
        "frozen_engine_commit": "ab0b252",
        "discovery_rule_hardcoding": False,
        "source_proof": "NOT_AVAILABLE_FOR_OPAQUE_ORACLES",
        "oracle_linearity_certification": "EXHAUSTIVE_ONLY_FOR_SMALL_WIDTH_OTHERS_PROBABILISTIC",
        "out_of_sample_protocol": "engine committed before separate sealed challenge cases",
        "rows": rows,
        "score": {
            "heldout_linear_passes": sum(r["outcome"]=="PASS_POST_FREEZE_HOLDOUT" for r in positive),
            "heldout_linear_total": len(positive),
            "nonlinear_rejected_pre_holdout": sum(r["outcome"]=="CORRECT_REJECTION" for r in negative),
            "nonlinear_total": len(negative),
            "unsafe_or_incorrect_acceptance_count": len(unsafe),
            "safe_for_compiler_promotion": False,
        },
        "caveats": [
            "Finite oracle tests do not prove a function globally linear; a rare nonlinear counterexample can evade BLR sampling.",
            "The inferred GF(2) matrix and repeated-squaring algorithm are known mathematics, not a novel asymptotic algorithm.",
            "Python blackbox prototype only; not a S3 compiler pass, S3 IR or native x86-64 output.",
            "For cyclic oracles an independent specialized polynomial algorithm may be faster than generic matrix powers.",
            "Discovery, training, proof and first-execution costs must be amortized; isolated warm runtime speedups are insufficient.",
            "Never deploy a probabilistically accepted candidate without source-derived proof or complete domain certification.",
        ],
    }


def main():
    report = evaluation()
    out = HERE / "sealed_results_v10.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("SUMMARY", json.dumps(report["score"], sort_keys=True), flush=True)
    print("RESULTS=" + str(out), flush=True)


if __name__ == "__main__":
    main()
