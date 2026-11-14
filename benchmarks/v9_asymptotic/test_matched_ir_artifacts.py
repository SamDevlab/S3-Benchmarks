"""Sanity-check committed V9 2x2 same-IR experimental artifacts."""
import json
import math
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED = {
    "C_SIGNED_OVERFLOW_ABSENT",
    "C_DIVISION_EQUIVALENT",
    "C_CAST_EQUIVALENT",
    "C_ABI_COMPATIBLE",
    "C_RUNTIME_GUARDS_PRESENT",
}


def validate_artifact(data: dict):
    assert data["status"] == "EXPLORATORY_MATCHED_IR_BENCHMARK"
    assert data["semantic_equivalence_proof"] is False
    irs = data["ir_hashes_by_mode"]
    for left, right in (("B", "E"), ("G", "H"), ("J", "H")):
        assert irs[left] == irs[right], f"IR mismatch: {left}/{right}"
        assert data["equal_ir_pairs_verified"][left + "_" + right]
    assert set(data["structural_C_obligations"]) == EXPECTED
    assert all(v == "PROVED" for v in data["structural_C_obligations"].values())
    assert data["results"]
    for row in data["results"]:
        assert row["all_cross_backend_checksums_match"]
        for mode in ("B", "E", "G", "H", "J"):
            val = row["medians_ns"][mode]
            assert math.isfinite(val) and val > 0, (mode, row)
        assert math.isclose(
            row["ratios"]["gcc_vs_s3_matched_cleaned_J_over_H"],
            row["medians_ns"]["J"] / row["medians_ns"]["H"],
            rel_tol=0.0001,
        )


class MatchedIRArtifactTests(unittest.TestCase):
    def test_five_round_artifact(self):
        d = json.loads((ROOT / "matched_ir_ablation_v9.json").read_text(encoding="utf-8"))
        validate_artifact(d)
        self.assertEqual(len(d["results"]), 9)
        self.assertEqual(d["rounds"], 5)

    def test_ten_round_artifact(self):
        d = json.loads((ROOT / "matched_ir_ablation_v9_repeat.json").read_text(encoding="utf-8"))
        validate_artifact(d)
        self.assertEqual(len(d["results"]), 9)
        self.assertEqual(d["rounds"], 10)

    def test_corrupt_ir_hash_is_rejected(self):
        d = json.loads((ROOT / "matched_ir_ablation_v9_repeat.json").read_text(encoding="utf-8"))
        d["ir_hashes_by_mode"]["H"] = {"sum_quasi_parity": "tampered"}
        with self.assertRaises(AssertionError):
            validate_artifact(d)


if __name__ == "__main__":
    unittest.main()
