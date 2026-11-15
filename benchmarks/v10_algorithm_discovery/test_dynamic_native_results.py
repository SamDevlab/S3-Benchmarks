"""Validate independently executed dynamic S3 vs GCC reference benchmark data."""
import json
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent


class DynamicGF2Benchmarks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((HERE/"native_gf2_dynamic_results_v10_3.json").read_text(encoding="utf-8"))

    def test_two_widths_single_s3_binary_for_all_runtime_horizons(self):
        self.assertEqual(self.data["status"],"EXPERIMENTAL_NATIVE_BENCHMARK_ONLY")
        self.assertTrue(self.data["s3_native_assembly"])
        self.assertFalse(self.data["s3_compiler_default_changed"])
        self.assertEqual([c["width"] for c in self.data["cases"]],[8,16])
        for case in self.data["cases"]:
            self.assertTrue(case["same_s3_shared_object_for_all_N"])
            self.assertEqual([r["N"] for r in case["samples"]],
                             [0,1,10,100,1000,10000,100000,1000000])
            self.assertGreater(case["native_smoke_checks"],60)
            self.assertGreater(case["dynamic_native_build_and_smoke_ms"],0)
            self.assertEqual(set(case["checked_python_public_api_ns"]),{"0","100","1000000"})

    def test_independent_algorithmic_reference_and_matched_generic(self):
        for case in self.data["cases"]:
            for row in case["samples"]:
                self.assertTrue(row["parity"])
                self.assertEqual(row["checked_states"],64)
                self.assertEqual(row["rounds"],9)
                times=row["median_ns"]
                self.assertEqual(set(times),{"iterative_c","s3_dynamic_native_raw",
                                             "cyclic_specialist_c","generic_matrix_c"})
                self.assertTrue(all(t>0 for t in times.values()))
                self.assertAlmostEqual(
                    row["s3_vs_matched_generic_c_ratio"],
                    times["s3_dynamic_native_raw"]/times["generic_matrix_c"],
                    delta=.0002,
                )
                self.assertAlmostEqual(
                    row["s3_vs_c_specialist_ratio"],
                    times["s3_dynamic_native_raw"]/times["cyclic_specialist_c"],
                    delta=.0002,
                )

    def test_research_classification_remains_experimental(self):
        self.assertEqual(self.data["known_algorithm_novelty"],"NONE_CLAIMED")
        self.assertIn("S3-generated x86-64",self.data["methods"]["S3"])
        self.assertTrue(any("proof gate" in note.lower() for note in self.data["caveats"]))


if __name__=="__main__":
    unittest.main()
