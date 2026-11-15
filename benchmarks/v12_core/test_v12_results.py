"""V12 artifact checks: new verified non-GF2 S3-native and physical GPU.

These validate recorded evidence, not independent re-execution of all
benchmarks. Re-run native and physical scripts to reproduce measurements.
"""
import json
import math
from pathlib import Path
import unittest


HERE=Path(__file__).resolve().parent


class V12Artifacts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.progression=json.loads(
            (HERE/"i64_progression_results_v12.json").read_text(encoding="utf-8"))
        cls.gpu=json.loads(
            (HERE/"gpu_calibration_v12.json").read_text(encoding="utf-8"))
        cls.profile=json.loads(
            (HERE/"native_codegen_profile_v12.json").read_text(encoding="utf-8"))

    def test_real_s3_native_non_gf2_evidence(self):
        p=self.progression
        self.assertEqual(p["algorithm_family"],"MONOTONIC_SIGNED_I64_ARITHMETIC_PROGRESSION")
        self.assertTrue(p["source_ir_proof"])
        self.assertFalse(p["blackbox_inference_used"])
        self.assertTrue(p["s3_native_backend_used"])
        self.assertFalse(p["automatic_production_promotion"])
        self.assertGreaterEqual(p["native_smoke_checks"],10)
        self.assertEqual([x["N"] for x in p["samples"]],[0,1,100,10000,1000000])
        self.assertGreater(p["specialized_cold_build_ms"],0)
        self.assertGreater(p["protected_python_api_median_ns"],0)
        for row in p["samples"]:
            self.assertTrue(row["parity"])
            self.assertEqual(row["differential_states"],64)
            self.assertEqual(row["rounds"],9)
            self.assertTrue(all(v>0 for v in row["median_ns"].values()))

    def test_big_o_only_for_specific_known_arithmetic_progression(self):
        p=self.progression
        self.assertEqual(p["delta"],7)
        one=p["samples"][1]["median_ns"]
        million=p["samples"][-1]["median_ns"]
        self.assertGreater(million["original_s3_n_steps"],one["original_s3_n_steps"])
        self.assertTrue(any("not a new algorithm" in s.lower() for s in p["limitations"]))

    def test_real_gpu_samples_and_exact_workload_dispatch(self):
        g=self.gpu
        self.assertTrue(g["device"]["is_physical"])
        self.assertEqual(g["device"]["backend"],"Vulkan")
        self.assertTrue(g["samples_are_raw_not_synthesized"])
        self.assertFalse(g["production_dispatch_changed"])
        self.assertEqual([x["evidence"]["width"] for x in g["cases"]],[64,128])
        for case in g["cases"]:
            e=case["evidence"]
            route=case["route"]
            self.assertTrue(case["exact_cell_parity"])
            self.assertTrue(case["gpu_real_physical"])
            self.assertTrue(e["s3_gpu_result_parity"])
            self.assertEqual(e["steps"],50)
            self.assertLessEqual(case["safe_per_buffer_bytes"],131072)
            self.assertEqual(len(e["cpu_total_ms_samples"]),7)
            self.assertEqual(len(e["gpu_total_ms_samples"]),7)
            self.assertTrue(all(t>0 for t in e["cpu_total_ms_samples"]))
            self.assertTrue(all(t>0 for t in e["gpu_total_ms_samples"]))
            self.assertFalse(route["automatic_production_dispatch_enabled"])
            self.assertIn(route["target"],("cpu","gpu"))
            self.assertGreater(route["cpu_median_ms"],0)
            self.assertGreater(route["gpu_median_ms"],0)
            if route["target"]=="gpu":
                self.assertTrue(route["safety_qualified"])
                self.assertGreater(
                    route["cpu_median_ms"]/route["gpu_median_ms"],1.2)

    def test_real_assembly_not_thought_experiment(self):
        d=self.profile
        self.assertEqual([c["width"] for c in d["cases"]],[16,32])
        for case in d["cases"]:
            self.assertEqual(case["s3_selected_algorithm"],"GF2_CYCLIC_POLYNOMIAL")
            self.assertGreater(case["s3_native_smoke_checks"],10)
            self.assertTrue(any("certified_step_dynamic" in key
                for key in case["s3_functions"]))
            self.assertTrue(any("cyclic_reference" in key
                for key in case["gcc_specialist_functions"]))
            self.assertTrue(all("@plt" not in key for key in case["s3_functions"]))
            for group in ("s3_functions","gcc_specialist_functions"):
                for metrics in case[group].values():
                    self.assertGreater(metrics["static_instructions"],0)
                    self.assertTrue(
                        metrics["static_instructions"] >= metrics["conditional_branches"])

    def test_no_invented_perf_claim_from_assembly_only(self):
        self.assertTrue(any("NOT dynamic" in s
            for s in self.profile["limitations"]))
        self.assertTrue(any("algorithmic" in s
            for s in self.profile["limitations"]))


if __name__=="__main__":
    unittest.main()
