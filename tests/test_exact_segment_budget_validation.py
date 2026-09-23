from __future__ import annotations

import pytest

import tools.run_exact_segment_budget_validation as validation
from tools.run_exact_segment_budget_validation import (
    VARIANTS,
    _balanced_order,
    _assert_same_program_instance,
    _cross_workload_result,
    _load_budget_plan_diagnostics,
    _recovery_metrics,
    _relative_delta,
    _sample_summary,
)


def test_balanced_interleaving_rotates_every_variant_once_per_repetition() -> None:
    for session_index in (0, 1):
        orders = [_balanced_order(index, session_index) for index in range(30)]
        assert all(sorted(order) == sorted(VARIANTS) for order in orders)
        position_counts = {variant: [0] * len(VARIANTS) for variant in VARIANTS}
        for order in orders:
            for position, variant in enumerate(order):
                position_counts[variant][position] += 1
        assert all(max(counts) - min(counts) <= 1 for counts in position_counts.values())


def test_second_session_uses_a_distinct_balanced_rotation() -> None:
    assert _balanced_order(0, 0) != _balanced_order(0, 1)
    assert _balanced_order(0, 0)[3:] + _balanced_order(0, 0)[:3] == _balanced_order(0, 1)


def test_p0_and_p2_require_the_same_compiled_program_object() -> None:
    program = object()
    assert _assert_same_program_instance(program, program, "test.workload") is True


def test_p0_and_p2_reject_distinct_compiled_program_objects() -> None:
    try:
        _assert_same_program_instance(object(), object(), "test.workload")
    except RuntimeError as exc:
        assert "same AssemblyProgram instance" in str(exc)
    else:
        raise AssertionError("distinct P0/P2 program objects were accepted")


def test_missing_segment_diagnostics_are_optional_for_control_only(monkeypatch: pytest.MonkeyPatch) -> None:
    module_name = "bootstrap.s3.backends.x86_64.instruction_budget"

    def missing_module(name: str) -> object:
        assert name == module_name
        raise ModuleNotFoundError("control revision predates the diagnostics module", name=module_name)

    monkeypatch.setattr(validation.importlib, "import_module", missing_module)
    assert _load_budget_plan_diagnostics(required=False) is None
    with pytest.raises(ModuleNotFoundError, match="predates the diagnostics module"):
        _load_budget_plan_diagnostics(required=True)


def test_missing_dependency_inside_segment_diagnostics_is_not_masked(monkeypatch: pytest.MonkeyPatch) -> None:
    def broken_module(name: str) -> object:
        raise ModuleNotFoundError("diagnostics dependency is missing", name="diagnostics_dependency")

    monkeypatch.setattr(validation.importlib, "import_module", broken_module)
    with pytest.raises(ModuleNotFoundError, match="diagnostics dependency"):
        _load_budget_plan_diagnostics(required=False)


def test_relative_session_delta_uses_the_predeclared_max_median_denominator() -> None:
    assert _relative_delta(100.0, 80.0) == 0.2
    assert _relative_delta(80.0, 100.0) == 0.2
    assert _relative_delta(0.0, 0.0) == 0.0


def test_recovery_metrics_keep_p0_p1_p2_and_pneg_distinct() -> None:
    result = _recovery_metrics({"P0": 100.0, "P1": 80.0, "P2": 60.0, "PNEG": 20.0})
    assert result["p1_recovered_budget_excess"] == 0.25
    assert result["p2_recovered_budget_excess"] == 0.5
    assert result["p2_incremental_recovery_over_p1"] == 0.25
    assert result["p2_over_pneg"] == 3.0


def test_zero_budget_excess_is_unavailable_not_divided() -> None:
    result = _recovery_metrics({"P0": 20.0, "P1": 20.0, "P2": 20.0, "PNEG": 20.0})
    assert result["p2_recovered_budget_excess"] is None


def test_cross_workload_classification_requires_all_six_cells() -> None:
    assert _cross_workload_result([0.5] * 6) == "STRONG_MATERIAL_RECOVERY"
    assert _cross_workload_result([0.25, 0.3, 0.4, 0.26, 0.49, 0.25]) == "USEFUL_MATERIAL_RECOVERY"
    assert _cross_workload_result([0.3, 0.1, 0.1, 0.1, 0.1, 0.1]) == "WORKLOAD_SENSITIVE"
    assert _cross_workload_result([0.1] * 6) == "SAFE_NOT_MATERIAL"
    assert _cross_workload_result([0.5] * 5) == "INCOMPLETE"


def test_sample_summary_fails_closed_on_missing_samples() -> None:
    incomplete = _sample_summary([{"status": "PASS", "elapsed_ns": 10}])
    assert incomplete == {"status": "INCOMPLETE", "valid_samples": 1, "expected_samples": 30}


def test_sample_summary_reports_the_full_repetition_count() -> None:
    rows = [{"status": "PASS", "elapsed_ns": index + 1} for index in range(30)]
    summary = _sample_summary(rows)
    assert summary["status"] == "PASS"
    assert summary["N"] == 30
    assert summary["median_ns"] == 15.5
