"""Validate V11 S3 native automatic algorithm selection + physical GPU evidence.

Unit tests validate recorded artifact provenance/parity but are not
independent reruns of the hardware benchmarks. Re-run scripts for that.
"""
import json
import math
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent


class V11CoreResultsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.native=json.loads((HERE/"results_auto_native_v11.json").read_text(encoding="utf-8"))
        cls.gpu=json.loads((HERE/"results_gpu_physical_v11.json").read_text(encoding="utf-8"))
        cls.resident=json.loads((HERE/"results_gpu_resident_conway_v11.json").read_text(encoding="utf-8"))

    def test_auto_native_uses_real_s3_x86_and_same_proof_source(self):
        d=self.native
        self.assertFalse(d["novel_algorithm_claim"])
        self.assertFalse(d["automatic_production_compiler_pass"])
        self.assertEqual([c["width"] for c in d["cases"]],[8,16,32])
        for c in d["cases"]:
            self.assertEqual(c["selection"]["selected"],"GF2_CYCLIC_POLYNOMIAL")
            self.assertTrue(c["same_s3_binary_per_N_for_each_selected_algorithm"])
            self.assertEqual(c["selection"]["certificate_sha256"],c["proof_cert_sha256"])
            self.assertEqual(c["selection"]["original_ir_sha256"],c["source_ir_sha256"])
            self.assertEqual(len(c["samples"]),4)
            self.assertGreater(c["auto_native_build_ms"],0)
            self.assertGreater(c["auto_native_smoke_checks"],0)

    def test_native_checksums_and_independent_known_specialist(self):
        for c in self.native["cases"]:
            self.assertEqual([r["N"] for r in c["samples"]],[1,16,1000,1000000])
            for r in c["samples"]:
                self.assertTrue(r["parity"])
                self.assertEqual(r["differential_checks"],64)
                self.assertEqual(r["rounds"],9)
                values=r["median_ns"]
                self.assertTrue(all(math.isfinite(v) and v>0 for v in values.values()))
                self.assertEqual(set(values),{"s3_generic","s3_auto_selected","gcc_cyclic_specialist"})
                self.assertAlmostEqual(
                    r["auto_over_generic"],
                    values["s3_auto_selected"]/values["s3_generic"],
                    delta=.000003,
                )

    def test_real_physical_vulkan_gpu_without_emulation(self):
        g=self.gpu
        self.assertEqual(g["status"],"REAL_GPU_COMPILE_DISPATCH_READBACK_PARITY_PASS")
        self.assertTrue(g["device"]["is_physical"])
        self.assertEqual(g["device"]["backend"],"Vulkan")
        self.assertIn("RX 580",g["device"]["name"])
        self.assertEqual([x["N"] for x in g["cases"]],[1024,4096,16384])
        self.assertTrue(g["f64_to_f32_narrowing_explicit"])
        for row in g["cases"]:
            self.assertTrue(row["gpu_physical"])
            self.assertTrue(row["gpu_dispatch_success"])
            self.assertTrue(row["gpu_readback_success"])
            self.assertTrue(row["cpu_vs_gpu_f32_parity"])
            self.assertTrue(row["wgsl_f32_compiled_from_s3"])
            self.assertGreater(row["gpu_total_us_median"],0)
            self.assertGreater(row["cpu_numpy_us_median"],0)
            self.assertFalse(row["gpu_qualification"]["GPU_WORKLOAD_QUALIFIED"])

    def test_gpu_experiment_is_not_misclassified_as_auto_gpu_deploy(self):
        g=self.gpu
        self.assertTrue(any("not automatic" in s.lower() for s in g["limitations"]))
        self.assertTrue(all(
            r["gpu_qualification"]["reason"]=="host_dispatch_transfer_overhead_exceeds_compute"
            for r in g["cases"]
        ))

    def test_physical_gpu_resident_multigeneration_vs_numpy_parity(self):
        r=self.resident
        self.assertEqual(r["status"],"REAL_S3_WGSL_PHYSICAL_GPU_RESIDENT_PINGPONG_PARITY")
        self.assertTrue(r["device"]["is_physical"])
        self.assertEqual(r["device"]["backend"],"Vulkan")
        self.assertFalse(r["production_dispatch_auto_enabled"])
        self.assertEqual([x["width"] for x in r["cases"]],[64,128])
        for row in r["cases"]:
            self.assertTrue(row["s3_gpu_conway_correct"])
            self.assertTrue(row["gpu_physical"])
            self.assertEqual(row["steps"],50)
            self.assertLessEqual(row["per_buffer_bytes"],131072)
            self.assertGreater(row["gpu_total_ms_median"],0)
            self.assertGreater(row["cpu_numpy_total_ms_median"],0)
            self.assertGreater(row["gpu_dispatch_ms_median"],0)
            self.assertAlmostEqual(
                row["gpu_over_cpu_total_ratio"],
                row["gpu_total_ms_median"]/row["cpu_numpy_total_ms_median"],
                delta=.0003,
            )

    def test_gpu_residency_has_measured_not_universal_crossover(self):
        rows={x["width"]:x for x in self.resident["cases"]}
        self.assertGreater(rows[64]["gpu_over_cpu_total_ratio"],1)
        self.assertLess(rows[128]["gpu_over_cpu_total_ratio"],1)
        self.assertTrue(any("one physical" in x.lower() for x in self.resident["limits"]))



if __name__=="__main__":
    unittest.main()
