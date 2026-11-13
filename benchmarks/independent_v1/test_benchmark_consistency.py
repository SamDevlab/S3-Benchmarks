#!/usr/bin/env python3
"""
Targeted test suite verifying reproducibility, evidence classification taxonomy,
and consistency of benchmark artifacts for SAMDEV_UNIFIED_V3_1.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

VALID_EVIDENCE_CLASSES = {
    "HISTORICAL_NATIVE",
    "CURRENT_NATIVE",
    "CURRENT_IR_EMULATION",
    "CORRECTNESS_ONLY",
    "STRUCTURAL_ONLY",
    "INCONCLUSIVE",
    "NOT_MEASURED",
}

BENCHMARK_DIR = Path(__file__).resolve().parent


class TestBenchmarkArtifactConsistency(unittest.TestCase):
    def setUp(self):
        self.results_json_path = BENCHMARK_DIR / "results.json"
        self.results_md_path = BENCHMARK_DIR / "RESULTS.md"
        self.bottlenecks_md_path = BENCHMARK_DIR / "BOTTLENECKS.md"
        self.runner_path = BENCHMARK_DIR / "run_benchmarks.py"

    def test_no_hardcoded_user_paths_in_runner(self):
        """Ensure runner contains no hardcoded absolute user paths."""
        text = self.runner_path.read_text(encoding="utf-8")
        self.assertNotIn("c:\\Users\\", text, "Found hardcoded Windows user path in runner")
        self.assertNotIn("/home/", text, "Found hardcoded Linux user path in runner")
        self.assertNotIn("/Users/", text, "Found hardcoded macOS user path in runner")

    def test_results_json_taxonomy_and_structure(self):
        """Verify results.json structure and evidence classification compliance."""
        self.assertTrue(self.results_json_path.exists(), "results.json must exist")
        with open(self.results_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("campaign"), "SAMDEV_UNIFIED_V3_1")
        self.assertIn("pinned_commits", data)
        self.assertIn("s3_repo", data["pinned_commits"])
        self.assertIn("s3_benchmarks_repo", data["pinned_commits"])

        # Check historical matrix
        cross = data.get("canonical_cross_language_pr33", {})
        self.assertEqual(cross.get("status"), "HISTORICAL_RECONCILIATION")
        for item in cross.get("matrix", []):
            classification = item.get("evidence_classification")
            self.assertIn(
                classification,
                VALID_EVIDENCE_CLASSES,
                f"Invalid evidence class: {classification}",
            )

        # Check live workloads
        live = data.get("live_workloads", {})
        self.assertIn("workload_a_jsmn", live)
        self.assertIn("workload_b_rmsd", live)
        self.assertIn("workload_c_stencil_2d", live)

        res_a = live["workload_a_jsmn"]
        self.assertTrue(res_a["parity_pass"])

        res_b = live["workload_b_rmsd"]
        self.assertTrue(res_b["parity_pass"])
        self.assertEqual(res_b["expected_checksum"], 29356)
        self.assertEqual(res_b["s3_checksum"], 29356)
        self.assertTrue(res_b["negative_test_passed"])

        res_c = live["workload_c_stencil_2d"]
        self.assertTrue(res_c["parity_pass"])
        self.assertEqual(res_c["workload_id"], "GEOSPATIAL_RASTER_WINDOW_STATISTICS")

    def test_results_md_content_integrity(self):
        """Verify RESULTS.md mentions mandatory evidence separation and accurate ratios."""
        self.assertTrue(self.results_md_path.exists(), "RESULTS.md must exist")
        text = self.results_md_path.read_text(encoding="utf-8")

        for cls_name in VALID_EVIDENCE_CLASSES:
            self.assertIn(cls_name, text, f"RESULTS.md must explain taxonomy class {cls_name}")

        # Check accurate ratio (8.99% or ~9%, not 3.21x conflated)
        self.assertIn("8.99%", text)
        self.assertIn("HISTORICAL_NATIVE", text)
        self.assertIn("CURRENT_IR_EMULATION", text)
        self.assertIn("29356", text)

    def test_bottlenecks_md_schema_and_criteria(self):
        """Verify each bottleneck in BOTTLENECKS.md has all required criteria."""
        self.assertTrue(self.bottlenecks_md_path.exists(), "BOTTLENECKS.md must exist")
        text = self.bottlenecks_md_path.read_text(encoding="utf-8")

        required_fields = [
            "Workload Identified",
            "Code SHA",
            "Configuration",
            "Observed Metric",
            "Evidence Source",
            "Causal Hypothesis",
            "Confidence Degree",
            "Required Experiment",
        ]

        for i in range(1, 6):
            section_header = f"## Bottleneck {i}:"
            self.assertIn(section_header, text, f"Missing {section_header} in BOTTLENECKS.md")

        for field in required_fields:
            occurrences = text.count(field)
            self.assertGreaterEqual(
                occurrences, 5, f"Field '{field}' must appear at least 5 times in BOTTLENECKS.md"
            )

        # Check LOOP_HYBRID correction
        self.assertIn("LOOP_HYBRID", text)
        self.assertIn("unsupported by evidence", text)


if __name__ == "__main__":
    unittest.main()

