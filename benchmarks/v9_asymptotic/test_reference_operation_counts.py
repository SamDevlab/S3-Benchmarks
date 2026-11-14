"""Independent reference operation counts; no claims about actual S3 instructions."""
import random
import unittest

from reference_operation_counts import (
    Cost,
    MODULUS,
    fib_doubling,
    fib_loop,
    lcg_loop,
    lcg_pow,
    make_report,
    sum_loop,
    sum_quasi_closed,
)


class ReferenceCountsTests(unittest.TestCase):
    def test_closed_form_matches_loop_on_fixed_and_random_inputs(self):
        r = random.Random(1107)
        for n in [0, 1, 2, 3, 31, 100, 999, 1000] + [r.randint(0, 1000) for _ in range(50)]:
            baseline_cost, fast_cost = Cost(), Cost()
            self.assertEqual(sum_loop(n, baseline_cost), sum_quasi_closed(n, fast_cost))
            self.assertEqual(baseline_cost.iterations, n)
            self.assertEqual(fast_cost.iterations, 0)
            self.assertEqual(baseline_cost.polynomial_arithmetic_ops, 6*n)
            if n > 0:
                self.assertEqual(fast_cost.polynomial_arithmetic_ops, 20)
                self.assertEqual(fast_cost.divisions, 1)

    def test_lcg_binary_composition_counts_and_correctness(self):
        r = random.Random(2208)
        for n in [0, 1, 2, 3, 100, 1000] + [r.randint(0, 1000) for _ in range(50)]:
            baseline_cost, fast_cost = Cost(), Cost()
            a = lcg_loop(n, 7, MODULUS, baseline_cost)
            b = lcg_pow(n, 7, MODULUS, fast_cost)
            self.assertEqual(a, b)
            self.assertEqual(baseline_cost.iterations, n)
            self.assertEqual(fast_cost.iterations, n.bit_length())
            if n > 0:
                self.assertEqual(fast_cost.affine_compositions, n.bit_length() + n.bit_count())
                self.assertEqual(fast_cost.modular_multiplications, 2*n.bit_length() + 2*n.bit_count() + 1)

    def test_fib_fast_doubling_counts_and_correctness(self):
        r = random.Random(3309)
        for n in [0, 1, 2, 3, 100, 1000] + [r.randint(0, 1000) for _ in range(50)]:
            baseline_cost, fast_cost = Cost(), Cost()
            a = fib_loop(n, MODULUS, baseline_cost)
            b = fib_doubling(n, MODULUS, fast_cost)
            self.assertEqual(a, b)
            self.assertEqual(baseline_cost.iterations, n)
            self.assertEqual(fast_cost.iterations, n.bit_length())
            self.assertEqual(fast_cost.modular_multiplications, 3*n.bit_length())

    def test_million_has_twenty_binary_steps_not_million(self):
        report = make_report()
        last = report["rows"][-1]
        self.assertEqual(last["N"], 1000000)
        self.assertEqual(last["analytical_naive_iteration_count"], 1000000)
        self.assertEqual(last["models"]["lcg_binary"]["operations"]["iterations"], 20)
        self.assertEqual(last["models"]["fib_doubling"]["operations"]["iterations"], 20)
        self.assertFalse(report["formal_S3_complexity_proof"])
        self.assertEqual(report["compiled_S3_instruction_count"], "NOT_MEASURED")


if __name__ == "__main__":
    unittest.main()
