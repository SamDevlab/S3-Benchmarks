"""V12 benchmark artifact integrity, not hard-coded speedup CI gates."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def validate_sample(sample):
    assert sample["parity"] is True
    assert sample["checks"] == 64
    assert sample["rounds"] == 9
    assert sample["N"] >= 0
    for name in (
        "s3_generic", "s3_v11", "s3_v12",
        "gcc_matched_scan", "gcc_sparse",
    ):
        assert sample["median_ns"][name] > 0
    assert sample["v12_over_v11"] > 0
    assert sample["v12_over_gcc_sparse"] > 0


def test_full_corpus_has_real_native_parity_and_c_references():
    result = read("results_auto_native_v12.json")
    assert result["s3_native_assembly"] is True
    assert result["algorithmic_novelty"] is False
    assert result["compiler_levels"] == {"s3": "O1", "c_reference": "GCC -O3"}
    assert len(result["cases"]) == 8
    observed = set()
    for case in result["cases"]:
        observed.add((case["family"], case["width"]))
        assert len(case["samples"]) == 4
        assert {s["N"] for s in case["samples"]} == {1, 64, 4096, 1_000_003}
        assert len(case["source_ir_sha256"]) == 64
        assert len(case["certificate_sha256"]) == 64
        for sample in case["samples"]:
            validate_sample(sample)
    assert ("rule90", 8) in observed
    assert ("invertible", 31) in observed
    assert ("rotation", 31) in observed


def test_non_degenerate_and_nilpotent_controls_are_distinct():
    result = read("results_auto_native_v12.json")
    for case in result["cases"]:
        if case["family"] == "rule90":
            assert case["nonzero_output_at_large_horizon"] is False
        else:
            assert case["nonzero_output_at_large_horizon"] is True


def test_holdout_is_additional_odd_width_five_tap_family():
    result = read("results_holdout_native_v12.json")
    assert result["independent_blind_replication"] is False
    assert result["first_run_without_candidate_tuning"] is True
    assert result["seed"] == 2026111407
    assert {c["width"] for c in result["cases"]} == {9, 23, 29}
    for case in result["cases"]:
        assert len(case["taps"]) == 5
        assert len(set(case["taps"])) == 5
        assert len(case["samples"]) == 3
        assert {s["N"] for s in case["samples"]} == {37, 10001, 1000003}
        for s in case["samples"]:
            validate_sample(s)


def test_assembly_counts_cannot_be_mistaken_for_pmu():
    for case in read("results_auto_native_v12.json")["cases"]:
        for label in ("s3_generic", "s3_v11", "s3_v12"):
            stats = case["assembly"][label]
            assert not stats["instruction_count_is_dynamic"]
            assert stats["total_disassembled_instructions_including_plt"] > 0
            assert stats["shared_library_bytes"] > 0


def test_no_gpu_measurement_claim_is_created_by_native_suite():
    result = read("results_auto_native_v12.json")
    assert "gpu_measurements" not in result
    assert "automatic_production_dispatch" not in result
