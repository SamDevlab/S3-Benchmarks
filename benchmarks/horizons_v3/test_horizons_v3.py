"""Consistency and numerical parity tests for S3 Scientific Horizons V3 benchmarks."""

from __future__ import annotations

import json
from pathlib import Path

RESULTS_V3 = Path(__file__).resolve().parent / "results_v3.json"


def test_results_v3_exists_and_all_experiments_pass() -> None:
    assert RESULTS_V3.exists()
    data = json.loads(RESULTS_V3.read_text(encoding="utf-8"))
    assert data["campaign"] == "S3_SCIENTIFIC_HORIZONS_V3"
    exps = data["experiments"]
    expected = {
        "mechanics_lab_2000steps",
        "materials_diffusion_101x500",
        "bio_reaction_kinetics_2000steps",
        "biomechanics_joint_1000steps",
        "fem_1d_bar_2elem",
    }
    assert expected <= set(exps)
    for name in expected:
        for profile in ("s3_o0_per_instruction", "s3_o1_per_instruction", "s3_o1_exact_segment"):
            entry = exps[name][profile]
            assert entry["parity_pass"] is True, f"{name} {profile} failed parity"
            assert entry["median_ns"] > 0
