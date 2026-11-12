"""Pytest gate for S3 Scientific Horizons V4 benchmarks."""

from __future__ import annotations

import json
from pathlib import Path

RESULTS_PATH = Path(__file__).resolve().parent / "results_v4.json"


def test_results_v4_parity_and_rss_separation() -> None:
    assert RESULTS_PATH.exists(), "Run run_horizons_v4.py first"
    data = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    assert data["host_python_rss_kib"] > 0
    for exp_name, profiles in data["experiments"].items():
        for prof_name, metrics in profiles.items():
            assert metrics["parity_pass"] is True, f"{exp_name}/{prof_name} failed parity"
        assert "c_gcc_o2" in profiles and "c_gcc_o3" in profiles
        assert "s3_o1_loop_hybrid" in profiles
