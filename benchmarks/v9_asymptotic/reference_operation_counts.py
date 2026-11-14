#!/usr/bin/env python3
"""V9 algorithmic operation counts: independent references, NOT S3 IR profiling.

Measured reference algorithms show exact iteration/composition counts;
their complexities apply to these algorithm families, not the entire
S3 compiled function (guards/fallbacks can have different costs).
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path

N_VALUES = [0, 1, 2, 3, 4, 5, 7, 8, 15, 16, 31, 32, 63, 64, 100, 1000, 10000, 1000000]
MODULUS = 1_000_000_007


@dataclass
class Cost:
    iterations: int = 0
    modular_multiplications: int = 0
    bit_tests: int = 0
    affine_compositions: int = 0
    divisions: int = 0
    polynomial_arithmetic_ops: int = 0

    def to_dict(self):
        return vars(self).copy()


def sum_loop(n: int, cost: Cost) -> int:
    acc = 5
    for i in range(max(n, 0)):
        num = i * i + 3 * i + 1
        acc += num // 2
        cost.iterations += 1
        cost.polynomial_arithmetic_ops += 6  # 2 mul, 3 add (including accum), 1 div
        cost.divisions += 1
    return acc


def sum_quasi_closed(n: int, cost: Cost) -> int:
    # Exactly the parity-split formula from the independent C reference.
    if n <= 0:
        return 5
    q, r = divmod(n, 2)
    cost.divisions += 1
    b1 = q
    b2 = q * (q - 1) // 2
    b3 = q * (q - 1) * (q - 2) // 6
    pair_sum = 2 * b1 + 12 * b2 + 8 * b3
    rem = r * (2 * q * q + 3 * q)
    cost.polynomial_arithmetic_ops += 20  # source-expression arithmetic, excludes divmod; NOT machine instructions
    return 5 + pair_sum + rem


def lcg_loop(n: int, x: int, m: int, cost: Cost) -> int:
    for _ in range(max(n, 0)):
        x = (3*x + 5) % m
        cost.iterations += 1
        cost.modular_multiplications += 1
    return x


def lcg_pow(n: int, x: int, m: int, cost: Cost) -> int:
    # Composition of affine maps, f(x)=3*x+5 mod m, binary exponentiation.
    if n <= 0:
        return x
    ar, br = 1, 0
    a, b = 3 % m, 5 % m
    e = n

    def mulmod(u, v):
        cost.modular_multiplications += 1
        return (u * v) % m

    while e > 0:
        cost.iterations += 1
        cost.bit_tests += 1
        if e & 1:
            br = (mulmod(a, br) + b) % m
            ar = mulmod(a, ar)
            cost.affine_compositions += 1
        b = (mulmod(a, b) + b) % m
        a = mulmod(a, a)
        cost.affine_compositions += 1
        e >>= 1
    return (mulmod(ar, x) + br) % m


def fib_loop(n: int, m: int, cost: Cost) -> int:
    a, b = 0, 1
    for _ in range(max(n, 0)):
        a, b = b, (a + b) % m
        cost.iterations += 1
    return a


def fib_doubling(n: int, m: int, cost: Cost) -> int:
    a, b = 0, 1
    for bit in bin(n)[2:] if n > 0 else "":
        cost.iterations += 1
        cost.bit_tests += 1
        c = a * (2*b - a) % m
        d = (a*a + b*b) % m
        cost.modular_multiplications += 3
        if bit == "1":
            a, b = d, (c + d) % m
        else:
            a, b = c, d
    return a


def reference_row(n: int) -> dict:
    sum_c = Cost()
    sum_value = sum_quasi_closed(n, sum_c)
    lcg_c = Cost()
    lcg_value = lcg_pow(n, 7, MODULUS, lcg_c)
    fib_c = Cost()
    fib_value = fib_doubling(n, MODULUS, fib_c)
    output = {
        "N": n,
        "N_bit_length": n.bit_length(),
        "N_popcount": n.bit_count(),
        "models": {
            "quasi_closed": {"value": sum_value, "operations": sum_c.to_dict(), "expected_step_bound": "constant"},
            "lcg_binary": {"value": lcg_value, "operations": lcg_c.to_dict(), "expected_step_bound": "bit_length(N)"},
            "fib_doubling": {"value": fib_value, "operations": fib_c.to_dict(), "expected_step_bound": "bit_length(N)"},
        },
        "analytical_naive_iteration_count": n,
        "direct_reference_comparison": "NOT_RUN",
    }
    # Independently execute conventional reference only where affordable; this
    # is differential validation on a finite set, not a universal proof.
    if n <= 1000:
        reference = [
            sum_loop(n, Cost()),
            lcg_loop(n, 7, MODULUS, Cost()),
            fib_loop(n, MODULUS, Cost()),
        ]
        actual = [sum_value, lcg_value, fib_value]
        if reference != actual:
            raise AssertionError(f"reference correctness failure for n={n}: {reference} vs {actual}")
        output["direct_reference_comparison"] = "PASS"
    # Exact combinatorial loop counts for these reference implementations.
    if n > 0:
        assert lcg_c.iterations == n.bit_length()
        assert lcg_c.affine_compositions == n.bit_length() + n.bit_count()
        assert lcg_c.modular_multiplications == 2*n.bit_length() + 2*n.bit_count() + 1
        assert fib_c.iterations == n.bit_length()
        assert fib_c.modular_multiplications == 3*n.bit_length()
    else:
        assert lcg_c.iterations == 0
        assert fib_c.iterations == 0
    assert sum_c.iterations == 0
    return output


def make_report() -> dict:
    return {
        "classification": "INDEPENDENT_ALGORITHMIC_REFERENCE_OPERATION_COUNTERS",
        "formal_S3_complexity_proof": False,
        "compiled_S3_instruction_count": "NOT_MEASURED",
        "model": "Unit-cost fixed-width word-RAM for in-domain N; Python reference arithmetic uses arbitrary precision.",
        "scope": "Optimized reference fast paths only; guards/overflows/fallbacks in compiled S3 may change global worst-case.",
        "families": {
            "sum_quasi_parity": {
                "iterative": "Theta(N) counted loop iterations",
                "closed_form": "Theta(1) count of polynomial arithmetic ops (within word-RAM model)",
                "big_O_claim": "CONDITIONAL_REFERENCE_ALGORITHM_ONLY",
            },
            "lcg_mod": {
                "iterative": "Theta(N) modular updates",
                "binary": "Theta(log(N)) binary affine compositions for N>=2",
                "exact_fast_loop_iterations": "N.bit_length()",
                "exact_affine_compositions": "N.bit_length() + N.bit_count()",
                "exact_modular_multiplications": "2*N.bit_length() + 2*N.bit_count() + 1 for N>0",
                "big_O_claim": "CONDITIONAL_REFERENCE_ALGORITHM_ONLY",
            },
            "fib_mod": {
                "iterative": "Theta(N) recurrence steps",
                "fast_doubling": "Theta(log(N)) bit steps for N>=2",
                "exact_fast_loop_iterations": "N.bit_length()",
                "exact_modular_multiplications": "3*N.bit_length() for N>0",
                "big_O_claim": "CONDITIONAL_REFERENCE_ALGORITHM_ONLY",
            },
        },
        "rows": [reference_row(n) for n in N_VALUES],
        "notes": [
            "Big O is not derived from timing, nor can constant factors establish new asymptotic classes.",
            "Modular multiplication may be superconstant for arbitrary precision; bit complexity must be specified separately.",
            "The fast path may contain a checked overflow guard with fallback Theta(N).",
            "Symbolic arithmetic count is not an instruction count, and a theoretical upper bound is not a compiler correctness proof.",
            "Comparisons against independent conventional algorithms are finite-domain samples, not formal proofs.",
        ],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, default=Path(__file__).with_name("operation_counts_v9.json"))
    args = p.parse_args()
    report = make_report()
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    for row in report["rows"]:
        print(
            f"N={row['N']:>10} bits={row['N_bit_length']:>2} "
            f"linear={row['analytical_naive_iteration_count']:>10} "
            f"closed={row['models']['quasi_closed']['operations']['iterations']} "
            f"lcg={row['models']['lcg_binary']['operations']['iterations']:>2} "
            f"fib={row['models']['fib_doubling']['operations']['iterations']:>2} "
            f"ref={row['direct_reference_comparison']}"
        )
    print(f"OUTPUT={args.out} ; COMPILED_S3_ASYMPTOTIC_PROOF=NO")


if __name__ == "__main__":
    main()
