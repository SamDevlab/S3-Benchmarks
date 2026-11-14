"""Validate stored S3 emulator instruction-observer evidence (not a Big-O proof)."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent


class S3IRDynamicEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "ir_dynamic_operations_v9.json").read_text(encoding="utf-8"))
        cls.guards = json.loads((ROOT / "ir_guard_fallback_probes_v9.json").read_text(encoding="utf-8"))

    def profile(self, fn, n):
        return next(x for x in self.data["rows"] if x["function"] == fn and x["N"] == n)

    def guard(self, case, n):
        return next(x for x in self.guards["cases"] if x["case"] == case and x["N"] == n)

    def test_actual_observer_results_are_in_domain_and_equivalent(self):
        self.assertEqual(self.data["classification"],
                         "ACTUAL_S3_IR_DYNAMIC_OPCODE_COUNTS_FROM_EXISTING_EMULATOR_OBSERVER")
        self.assertFalse(self.data["formal_complexity_proof"])
        self.assertEqual(len(self.data["rows"]), 48)
        self.assertTrue(all(x["results_match_independent_reference"] for x in self.data["rows"]))

    def test_quasi_closed_path_ir_count_stops_growing_for_large_n(self):
        for n in (64, 128, 256, 512, 1024, 4096):
            r = self.profile("sum_quasi_parity", n)
            orig = r["modes"]["CONVENTIONAL_OPTIMIZED_IR"]["counts"]["executed_ir_opcodes"]
            pred = r["modes"]["PREDICTIVE_CLEANED_IR"]["counts"]["executed_ir_opcodes"]
            self.assertGreater(orig, pred)
            self.assertGreater(orig, n * 10)
            self.assertLess(pred, 340)

    def test_modular_fast_path_uses_fewer_ir_ops_at_high_n(self):
        for fn in ("lcg_mod", "fib_mod"):
            r64, r4096 = self.profile(fn, 64), self.profile(fn, 4096)
            orig64 = r64["modes"]["CONVENTIONAL_OPTIMIZED_IR"]["counts"]["executed_ir_opcodes"]
            orig4096 = r4096["modes"]["CONVENTIONAL_OPTIMIZED_IR"]["counts"]["executed_ir_opcodes"]
            pred64 = r64["modes"]["PREDICTIVE_CLEANED_IR"]["counts"]["executed_ir_opcodes"]
            pred4096 = r4096["modes"]["PREDICTIVE_CLEANED_IR"]["counts"]["executed_ir_opcodes"]
            self.assertGreater(orig4096 / orig64, 50)
            self.assertLess(pred4096 / pred64, 4)

    def test_negative_seed_and_modulus_trigger_expensive_branch(self):
        for label in ("negative_seed", "negative_modulus"):
            r = self.guard(label, 1024)
            self.assertTrue(r["parity"])
            self.assertGreater(r["modes"]["PREDICTIVE_CLEANED_IR"]["ir_ops"], 14000)
        fast = self.guard("eligible_positive", 1024)
        self.assertTrue(fast["parity"])
        self.assertLess(fast["modes"]["PREDICTIVE_CLEANED_IR"]["ir_ops"], 600)

    def test_all_adversarial_guard_probes_preserve_observed_parity(self):
        self.assertEqual(len(self.guards["cases"]), 16)
        self.assertTrue(all(r["parity"] for r in self.guards["cases"]))
        self.assertEqual(self.guards["status"], "BOUNDED_IR_ADVERSARIAL_PROBES_NOT_PROOF")


if __name__ == "__main__":
    unittest.main()
