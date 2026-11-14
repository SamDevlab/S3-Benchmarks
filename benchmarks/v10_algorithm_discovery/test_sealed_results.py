"""Acceptance tests for the frozen-engine holdout and native GCC evidence.

The negative rare-trigger finding is a REQUIRED scientific failure recorded
for safety, not a test to be hidden or optimized away.
"""
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parent


class SealedChallengeResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/"sealed_results_v10.json").read_text(encoding="utf-8"))
        cls.native=json.loads((ROOT/"native_gcc_results_v10.json").read_text(encoding="utf-8"))

    def test_all_six_post_freeze_positive_holdouts(self):
        positives=[x for x in self.data["rows"] if x["heldout_expected_linear"]]
        self.assertEqual(len(positives),6)
        self.assertTrue(all(x["outcome"]=="PASS_POST_FREEZE_HOLDOUT" for x in positives))
        self.assertTrue(all(x["holdout_parity"] for x in positives))
        self.assertEqual(self.data["frozen_engine_commit"],"ab0b252")

    def test_exhaustive_small_width_only(self):
        little=next(r for r in self.data["rows"] if r["case"]=="sealed_rule90_8")
        large=next(r for r in self.data["rows"] if r["case"]=="sealed_rule150_32")
        self.assertTrue(little["exhaustive"])
        self.assertFalse(large["exhaustive"])

    def test_rare_nonlinearity_must_remain_a_failed_certification(self):
        row=next(x for x in self.data["rows"] if x["case"]=="sealed_rare_trigger_24")
        self.assertEqual(row["outcome"],"HOLDOUT_DETECTED_UNSAFE_CANDIDATE")
        self.assertTrue(row["holdout_errors_first_five"])
        self.assertEqual(self.data["score"]["unsafe_or_incorrect_acceptance_count"],1)
        self.assertFalse(self.data["score"]["safe_for_compiler_promotion"])

    def test_basic_nonlinear_rejections(self):
        rows=[x for x in self.data["rows"] if not x["heldout_expected_linear"]]
        self.assertEqual(len(rows),3)
        self.assertEqual(sum(x["outcome"]=="CORRECT_REJECTION" for x in rows),2)

    def test_native_c_uses_inferred_columns_with_differential_parity(self):
        self.assertEqual(self.native["backend"],"GCC_NATIVE_NOT_S3_NATIVE")
        self.assertFalse(self.native["blackbox_linearity_proof"])
        self.assertFalse(self.native["new_algorithm_claim"])
        self.assertEqual(len(self.native["samples"]),6)
        for case in self.native["samples"]:
            self.assertEqual(case["result"],"NATIVE_DIFFERENTIAL_PARITY_PASS")
            self.assertEqual(len(case["rows"]),5)
            self.assertTrue(all(row["checksum_valid"] for row in case["rows"]))
            self.assertTrue(all(row["native_inferred_ns"]>0 for row in case["rows"]))
            self.assertTrue(case["rows"][-1]["speedup_direct_over_inferred"]>1)

    def test_specialized_reference_not_silently_removed(self):
        cyclic=[x for x in self.native["samples"] if x["family"]=="cyclic"]
        self.assertEqual(len(cyclic),4)
        self.assertTrue(all(
            x["rows"][-1]["native_specialist_ns"] is not None for x in cyclic))
        self.assertTrue(any(
            x["rows"][-1]["native_specialist_ns"] < x["rows"][-1]["native_inferred_ns"]
            for x in cyclic))


if __name__=="__main__":
    unittest.main()
