"""Unit tests for empirical slopes; these must not be interpreted as proof of Big O."""
import json
import math
import tempfile
import unittest
from pathlib import Path

from analyze_growth import analyze, fit_loglog


class ScalingAnalysisTests(unittest.TestCase):
    def test_effective_exponents(self):
        ns = [100, 1000, 10000, 100000, 1000000]
        for exponent, expected in [(0, 0), (1, 1), (2, 2)]:
            points = [{"N": n, "median_ns": 20 + (n / 100) ** exponent} for n in ns]
            # Large constant overhead can reduce finite-window slopes.
            if exponent == 0:
                self.assertAlmostEqual(fit_loglog(points), 0.0, delta=0.001)
            else:
                self.assertGreater(fit_loglog(points), exponent - 0.45)

    def test_logarithm_is_not_constant_complexity_proof(self):
        ns = [100, 1000, 10000, 100000, 1000000]
        points = [{"N": n, "median_ns": 60 + 30 * math.log2(n)} for n in ns]
        slope = fit_loglog(points)
        self.assertGreater(slope, 0)
        self.assertLess(slope, 0.30)

    def test_invalid_and_wrong_results_are_not_accepted(self):
        rows = [
            {"function": "sum_i2", "T": n, "modes": {
                "A": {"name": "S3_CONVENTIONAL_NATIVE", "median_ns": float(n), "above_noise_floor": True},
                "G": {"name": "S3_PREDICTIVE_NATIVE_CLEANED_EXACT", "median_ns": 50., "above_noise_floor": True}
            }, "correctness": {
                "S3_CONVENTIONAL_NATIVE": True,
                "S3_PREDICTIVE_NATIVE_CLEANED_EXACT": False}}
            for n in [100, 1000, 10000, 100000, 1000000]
        ]
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "synthetic.json"
            p.write_text(json.dumps({"results": rows}), encoding="utf-8")
            data = analyze([p])
        self.assertEqual(len(data["rows"]), 1)
        self.assertEqual(data["rows"][0]["mode"], "A")
        self.assertEqual(data["complexity_certification"], "NOT_PROVED")


if __name__ == "__main__":
    unittest.main()
