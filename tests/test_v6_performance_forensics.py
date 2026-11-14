"""Verification tests for the S3 V6 Performance Forensics Suite (P0 V4 vs V5 Audit)."""

from __future__ import annotations

import csv
import json
from pathlib import Path


BENCH_ROOT = Path(__file__).resolve().parents[1]
FORENSICS_DIR = BENCH_ROOT / "benchmarks" / "v6_performance_forensics"


def test_v6_forensics_artifacts_and_decisions() -> None:
    json_path = FORENSICS_DIR / "results_forensics.json"
    csv_path = FORENSICS_DIR / "results_forensics.csv"
    assert json_path.is_file(), "Missing results_forensics.json"
    assert csv_path.is_file(), "Missing results_forensics.csv"

    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["decision"] == "METHODOLOGY_ARTIFACT_CONFIRMED"
    assert data["secondary_decision"] == "NO_REPRODUCIBLE_REGRESSION"

    compilers = data["compilers"]
    assert compilers["V4_COMPILER"]["commit_sha"] == "f33b5b3b7d0c8e4cc278608ebb8d7eceb36590bd"
    assert compilers["V5_COMPILER"]["commit_sha"] == "9c1bec32c181710eec6e99c3056825d85b8412c6"
    assert compilers["V5_5_COMPILER"]["commit_sha"] == "5a51667e2ae7e8b4a7beb060c59c15244f82a7fa"


def test_v6_ab_matrix_proves_harness_asymmetry_and_v5_compiler_gain() -> None:
    data = json.loads((FORENSICS_DIR / "results_forensics.json").read_text(encoding="utf-8"))
    ab = data["ab_matrix"]
    assert len(ab) == 8  # 2 grids (32x32, 48x48) x 4 cells

    by_grid_cell = {(r["grid"], r["cell"]): r for r in ab}
    for grid in ("32x32", "48x48"):
        v4c_v4h = by_grid_cell[(grid, "V4_COMPILER + V4_HARNESS")]
        v4c_v5h = by_grid_cell[(grid, "V4_COMPILER + V5_HARNESS")]
        v5c_v4h = by_grid_cell[(grid, "V5_COMPILER + V4_HARNESS")]
        v5c_v5h = by_grid_cell[(grid, "V5_COMPILER + V5_HARNESS")]

        # 1. Exact numerical parity (0.0 error vs GCC and identical iterations)
        for row in (v4c_v4h, v4c_v5h, v5c_v4h, v5c_v5h):
            assert row["s3_iters"] == row["gcc_iters"]
            assert row["max_abs_err_vs_gcc"] == 0.0

        # 2. V5 compiler is strictly faster than V4 compiler on V4_HARNESS
        assert v5c_v4h["s3_median_ms"] < v4c_v4h["s3_median_ms"]

        # 3. V5_HARNESS adds multi-millisecond Python CSR/buffer/output overhead to both V4 and V5 compilers
        assert v4c_v5h["s3_median_ms"] > v4c_v4h["s3_median_ms"] * 2.0
        assert v5c_v5h["s3_median_ms"] > v5c_v4h["s3_median_ms"] * 2.0


def test_v6_normalized_sweep_stages_and_convergence() -> None:
    data = json.loads((FORENSICS_DIR / "results_forensics.json").read_text(encoding="utf-8"))
    rows = data["normalized_sweep"]
    assert len(rows) >= 16

    required_stages = {
        "INPUT_GENERATION_MS",
        "CSR_CONSTRUCTION_MS",
        "CTYPES_BUFFER_ALLOCATION_MS",
        "NATIVE_KERNEL_MS",
        "CHUNK_DISPATCH_MS",
        "OUTPUT_MATERIALIZATION_MS",
        "RESULT_VALIDATION_MS",
        "GCC_KERNEL_ONLY_MS",
        "V4_S3_KERNEL_ONLY_MS",
        "V5_S3_KERNEL_ONLY_MS",
        "GCC_END_TO_END_MS",
        "V4_S3_END_TO_END_MS",
        "V5_S3_END_TO_END_MS",
    }
    for r in rows:
        assert required_stages.issubset(r.keys())
        assert r["iters_match"] is True
        assert r["converged"] is True
        assert r["v4_max_err_vs_gcc"] == 0.0
        assert r["v5_max_err_vs_gcc"] == 0.0
        assert r["V5_SPEEDUP_OVER_V4_KERNEL"] >= 1.15
        assert r["V5_OVER_GCC_KERNEL_RATIO"] <= 1.65

    with (FORENSICS_DIR / "results_forensics.csv").open("r", encoding="utf-8") as f:
        csv_rows = list(csv.DictReader(f))
    assert len(csv_rows) == len(rows)
