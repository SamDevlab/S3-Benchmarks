from __future__ import annotations

import math
from pathlib import Path

from benchmarks.candidate_activation.workloads import performance_cases
from tools.direct_kernel_methodology import (
    DEFAULT_K_LEVELS,
    audit_timing_capabilities,
    build_amortized_s3_source,
    build_matched_c_source,
    expected_repeated_value,
    fit_slope,
    pilot_cases,
    _fixed_pressure_map,
    _fixed_work_summary,
    _select_fixed_work_level,
    _select_adaptive_levels,
)


def test_required_pilot_set_is_fixed_and_uses_medium_flat_workloads():
    pilots = pilot_cases()
    assert [pilot.workload_id for pilot in pilots] == [
        "memory.babelstream.triad",
        "hpc.prk.nstream",
        "numerical.polybench.gemm",
        "scientific.rmsd.batch",
    ]
    assert all(pilot.size == "medium" for pilot in pilots)
    assert all(pilot.case.physical_layout == "flat f64_vector" for pilot in pilots)


def test_s3_amortization_keeps_setup_outside_repeated_kernel():
    pilot = next(item for item in pilot_cases() if item.workload_id == "memory.babelstream.triad")
    source = build_amortized_s3_source(pilot.case.source, 100)
    assert source.count("while repetition < 100:") == 1
    assert source.index("f64_vector_new") < source.index("while repetition < 100:")
    assert source.index("f64_vector_push") < source.index("while repetition < 100:")
    assert source.count("last_result = total") == 1
    assert source.rstrip().endswith("return last_result")


def test_matched_c_references_are_flat_and_do_not_use_blas_or_fast_math():
    for pilot in pilot_cases():
        source = build_matched_c_source(pilot, 10)
        assert "malloc(" in source
        assert "for (size_t repetition = 0; repetition < 10; ++repetition)" in source
        assert "printf(\"program returned: %d\\n\"" in source
        assert "blas" not in source.lower()
        assert "-ffast-math" not in source
        assert "-Ofast" not in source


def test_matched_c_references_compare_the_final_kernel_result_not_a_sum_of_runs():
    for pilot in pilot_cases():
        source = build_matched_c_source(pilot, 10)
        assert "observable = total;" in source or "observable = checksum;" in source
        assert "observable += total;" not in source
        assert "observable += checksum;" not in source
        assert "fabs(observable -" in source


def test_repeated_work_values_match_the_declared_kernel_contract():
    for pilot in pilot_cases():
        one = expected_repeated_value(pilot, 1)
        assert math.isclose(one, pilot.case.expected, rel_tol=1e-12, abs_tol=1e-12)
        repeated = expected_repeated_value(pilot, DEFAULT_K_LEVELS[-1])
        assert math.isfinite(repeated)
        if pilot.workload_id == "hpc.prk.nstream":
            assert repeated == 589496.0
        else:
            assert repeated == pilot.case.expected


def test_repeated_work_rejects_non_positive_iteration_counts():
    pilot = pilot_cases()[0]
    for iterations in (0, -1):
        try:
            expected_repeated_value(pilot, iterations)
        except ValueError:
            pass
        else:
            raise AssertionError("non-positive iterations must be rejected")


def test_slope_model_is_empirical_and_reports_fit_quality():
    fit = fit_slope([(1, 110.0), (10, 200.0), (100, 1100.0)])
    assert fit["valid"] is True
    assert fit["interpretation"] == "EMPIRICAL_SLOPE"
    assert fit["slope_ns_per_iteration"] > 0
    assert 0.0 <= fit["r_squared"] <= 1.0
    assert "residual_summary" in fit


def test_adaptive_levels_keep_three_common_levels_under_the_guard():
    probes = {
        "S3_O0": {"elapsed_ns": 100_000.0},
        "S3_O1": {"elapsed_ns": 120_000.0},
        "GCC_O2": {"elapsed_ns": 80_000.0},
    }
    levels, guard = _select_adaptive_levels(probes)
    assert levels == (1, 10, 100, 1000)
    assert guard["skipped"] == {}


def test_fixed_work_selects_one_common_level_and_prefers_the_target_window():
    calibration = [
        {"K": 1000, "status": "PASS", "fastest_ns": 260_000_000, "slowest_ns": 900_000_000},
        {"K": 2000, "status": "PASS", "fastest_ns": 700_000_000, "slowest_ns": 2_400_000_000},
    ]
    selected = _select_fixed_work_level(calibration)
    assert selected is not None
    assert selected["K"] == 2000


def test_fixed_work_summary_reports_work_normalized_statistics():
    summary = _fixed_work_summary([100, 110, 120, 130, 140], 10)
    assert summary["N"] == 5
    assert summary["median_ns"] == 120
    assert summary["ns_per_work_unit"] == 12
    assert summary["p95_ns"] == 140
    assert summary["mad_ns"] == 10


def test_fixed_work_no_window_does_not_claim_run_ab_evidence():
    result = {
        "fixed_work_window": False,
        "same_machine_reproduction": "NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW",
        "same_binary_run_a_run_b": "NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW",
        "perf": {"available": "NO"},
    }
    pressure_map = _fixed_pressure_map(result)
    variability = next(item for item in pressure_map["pressures"] if item["pressure"] == "MEASUREMENT_VARIABILITY")
    assert pressure_map["status"] == "NOT_ACTIONABLE_NO_COMMON_FIXED_WORK_WINDOW"
    assert variability["classification"] == "NOT_ASSESSED"
    assert "not executed" in variability["evidence"]


def test_timing_audit_does_not_claim_a_direct_s3_timer_or_kernel_abi(tmp_path: Path):
    (tmp_path / "sample.s3").write_text("export fn sample() -> i64:\n    return 1\n", encoding="utf-8")
    audit = audit_timing_capabilities(tmp_path)
    assert audit["DIRECT_INTERNAL_TIMER_AVAILABLE"] == "NO"
    assert audit["EXPORTED_KERNEL_CALL_AVAILABLE"] == "NO"
    assert audit["EXTERNAL_AMORTIZATION_REQUIRED"] == "YES"
