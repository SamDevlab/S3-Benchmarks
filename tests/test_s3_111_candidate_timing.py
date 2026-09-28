from __future__ import annotations

from tools.s3_111_candidate_timing import _paired_summary


def test_paired_summary_identifies_reproducible_material_ratio() -> None:
    baseline = [110.0 + (index % 3) for index in range(21)]
    candidate = [100.0 + (index % 3) for index in range(21)]

    result = _paired_summary(baseline, candidate, seed=11)

    assert result["classification"] == "MATERIAL_IMPROVEMENT"
    assert result["baseline_over_candidate_median_ratio"] > 1.05


def test_paired_summary_keeps_overlapping_small_effect_non_material() -> None:
    baseline = [100.0 + (index % 2) for index in range(21)]
    candidate = [101.0 + (index % 2) for index in range(21)]

    result = _paired_summary(baseline, candidate, seed=12)

    assert result["classification"] == "NO_MATERIAL_CHANGE_WITHIN_5_PERCENT"
