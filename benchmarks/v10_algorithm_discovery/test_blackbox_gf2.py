"""White-box unit tests for the generic inference engine (not challenge holdout)."""
import random
import unittest

from blackbox_gf2 import (
    NotCertified, apply_columns, compose_columns, infer_gf2_map,
)


def step_matrix(columns, x):
    return apply_columns(tuple(columns), x)


class GF2EngineTests(unittest.TestCase):
    def test_generic_dense_map_exhaustive(self):
        cols = (0b11110001, 0b01100110, 0b10010010, 0b00000111,
                0b10110110, 0b00111001, 0b10001010, 0b11010101)
        f = lambda x: step_matrix(cols, x)
        model = infer_gf2_map(f, 8, exhaustive_limit=8)
        self.assertTrue(model.exhaustive)
        self.assertEqual(model.columns, cols)
        for n in (0, 1, 2, 3, 4, 7, 8, 15, 19, 24):
            for x in range(256):
                baseline = x
                for _ in range(n):
                    baseline = f(baseline)
                self.assertEqual(model.advance(x, n), baseline)

    def test_random_linear_maps_and_semigroup(self):
        rng = random.Random(9081)
        for width in (12, 16, 32):
            cols = tuple(rng.getrandbits(width) for _ in range(width))
            oracle = lambda x: step_matrix(cols, x)
            model = infer_gf2_map(oracle, width, probes=128, seed=52)
            self.assertFalse(model.exhaustive)
            for _ in range(35):
                x = rng.getrandbits(width)
                a, b = rng.randint(0, 1000), rng.randint(0, 1000)
                self.assertEqual(
                    model.advance(x, a+b),
                    model.advance(model.advance(x, a), b)
                )

    def test_reject_affine(self):
        with self.assertRaises(NotCertified):
            infer_gf2_map(lambda x: (x ^ 1) & 255, 8)

    def test_reject_nonlinear_by_exhaustive_search(self):
        with self.assertRaises(NotCertified):
            infer_gf2_map(lambda x: (x ^ ((x & 2) * (x & 1))) & 255, 8)

    def test_reject_random_nonlinear_by_blr(self):
        width = 24
        mask = (1 << width) - 1
        def nonlinear(x):
            return (x ^ ((x & (x >> 3)) << 2)) & mask
        with self.assertRaises(NotCertified):
            infer_gf2_map(nonlinear, width, probes=128, seed=7)

    def test_count_exact_binary_steps(self):
        model = infer_gf2_map(lambda x: (x << 1) & 255, 8, exhaustive_limit=8)
        for n in (0, 1, 4, 7, 31, 1000000):
            result, cnt = model.advance_with_counts(3, n)
            self.assertEqual(result, model.advance(3, n))
            self.assertEqual(cnt["matrix_vector_applications"], n.bit_count())
            self.assertEqual(cnt["matrix_compositions"], max(0, n.bit_length()-1))
            self.assertEqual(cnt["generation_loop_steps"], 0)

    def test_validate_contract(self):
        with self.assertRaises(ValueError):
            infer_gf2_map(lambda x: x, 0)
        with self.assertRaises(NotCertified):
            infer_gf2_map(lambda x: -1, 4)
        model = infer_gf2_map(lambda x: x, 4, exhaustive_limit=4)
        for x, n in [(-1, 3), (1 << 4, 1), (2, -1)]:
            with self.assertRaises(ValueError):
                model.advance(x, n)

    def test_matrix_composition(self):
        rng = random.Random(2077)
        for width in (7, 19, 32):
            a = tuple(rng.getrandbits(width) for _ in range(width))
            b = tuple(rng.getrandbits(width) for _ in range(width))
            c = compose_columns(a, b)
            for _ in range(50):
                x = rng.getrandbits(width)
                self.assertEqual(
                    apply_columns(c, x),
                    apply_columns(a, apply_columns(b, x))
                )


if __name__ == "__main__":
    unittest.main()
