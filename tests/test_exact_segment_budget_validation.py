from __future__ import annotations

import pytest

import tools.run_exact_segment_budget_validation as validation
from tools.run_exact_segment_budget_validation import (
    VARIANTS,
    _balanced_order,
    _assert_same_program_instance,
    _create_backend,
    _cross_workload_result,
    _added_text_recovery,
    _executable_text_metrics,
    _hardening_result,
    _load_budget_plan_diagnostics,
    _recovery_metrics,
    _relative_delta,
    _sample_summary,
    _segment_plan_sha256,
    _slow_path_instruction_count,
    _write_raw_manifest,
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


def test_legacy_backend_accepts_only_the_unchanged_default_mode() -> None:
    class LegacyBackend:
        def __init__(self, *, max_instructions: int) -> None:
            self.max_instructions = max_instructions

    backend = _create_backend(LegacyBackend, "per-instruction")
    assert backend.max_instructions > 0
    with pytest.raises(RuntimeError, match="does not support the requested experimental"):
        _create_backend(LegacyBackend, "exact-segment")


def test_experimental_backend_receives_the_requested_mode() -> None:
    class ExperimentalBackend:
        def __init__(self, *, max_instructions: int, instruction_budget_mode: str) -> None:
            self.max_instructions = max_instructions
            self.instruction_budget_mode = instruction_budget_mode

    backend = _create_backend(ExperimentalBackend, "exact-segment")
    assert backend.max_instructions > 0
    assert backend.instruction_budget_mode == "exact-segment"


def test_relative_session_delta_uses_the_predeclared_max_median_denominator() -> None:
    assert _relative_delta(100.0, 80.0) == 0.2
    assert _relative_delta(80.0, 100.0) == 0.2
    assert _relative_delta(0.0, 0.0) == 0.0


def test_recovery_metrics_compare_p2h_with_p2_and_pneg() -> None:
    result = _recovery_metrics({"P0": 100.0, "P2": 60.0, "P2H": 50.0, "PNEG": 20.0})
    assert result["p2_recovered_budget_excess"] == 0.5
    assert result["p2h_recovered_budget_excess"] == 0.625
    assert result["p2h_vs_p2"] == 50.0 / 60.0
    assert result["p2_over_pneg"] == 3.0


def test_zero_budget_excess_is_unavailable_not_divided() -> None:
    result = _recovery_metrics({"P0": 20.0, "P2": 20.0, "P2H": 20.0, "PNEG": 20.0})
    assert result["p2_recovered_budget_excess"] is None
    assert result["p2h_recovered_budget_excess"] is None
    assert result["p2h_vs_p2"] == 1.0


def test_added_text_recovery_preserves_growth_and_regression_signs() -> None:
    assert _added_text_recovery(100, 200, 175) == 0.25
    assert _added_text_recovery(100, 200, 225) == -0.25
    assert _added_text_recovery(100, 100, 90) is None


def test_segment_plan_hash_uses_canonical_key_order() -> None:
    assert _segment_plan_sha256({"a": 1, "b": 2}) == _segment_plan_sha256({"b": 2, "a": 1})


def test_slow_instruction_counter_handles_inline_failure_labels() -> None:
    assembly = """\
.L_s3_f1_fn_b1_entry:
    cmp rax, r10
.L__s3_budget_0_slow:
    cmp rax, 10
.L__s3_failure_site_0:
    lea rsi, [rip + message]
    jmp __s3_fail_message
.L__s3_budget_0_continue:
    ret
"""
    assert _slow_path_instruction_count(assembly) == 3


def test_slow_instruction_counter_counts_cold_section_including_labels() -> None:
    assembly = """\
.section .text.unlikely,"ax",@progbits
.L__s3_budget_0_slow:
    cmp rax, 10
.L__s3_failure_site_0:
    jmp __s3_fail_message
.section .text
"""
    assert _slow_path_instruction_count(assembly) == 2


def test_executable_text_metrics_separate_hot_cold_and_all_ax_sections(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path,
) -> None:
    output = """\
  [ 1] .text             PROGBITS 0000000000001000 001000 000100 00  AX  0   0 16
  [ 2] .text.unlikely    PROGBITS 0000000000001100 001100 000020 00  AX  0   0 16
  [ 3] .rodata           PROGBITS 0000000000001200 001200 000050 00   A  0   0 16
  [ 4] .plt              PROGBITS 0000000000001300 001300 000010 00  AX  0   0 16
"""
    monkeypatch.setattr(validation.shutil, "which", lambda name: "/usr/bin/readelf")
    monkeypatch.setattr(
        validation,
        "_run",
        lambda command: validation.subprocess.CompletedProcess(command, 0, output, ""),
    )
    executable = tmp_path / "candidate.so"

    assert _executable_text_metrics(executable) == {
        "hot_text_bytes": 0x100,
        "cold_text_bytes": 0x20,
        "total_executable_text_bytes": 0x130,
    }


def test_hardening_classification_requires_all_six_cells_and_frozen_thresholds() -> None:
    cells = [
        {
            "correctness_pass": True,
            "reproducibility_pass": True,
            "p2h_vs_p2": 1.05,
            "p2h_recovered_budget_excess": 0.50,
            "added_text_recovery": 0.25,
            "hot_text_recovery": 0.25,
        }
        for _ in range(6)
    ]
    assert _hardening_result(cells) == "QUALIFIED"
    assert _hardening_result(cells[:5]) == "INCOMPLETE"
    cells[4]["p2h_vs_p2"] = 1.050001
    assert _hardening_result(cells) == "REJECTED_PERFORMANCE_REGRESSION"


def test_hardening_classifies_cold_layout_only_separately() -> None:
    cells = [
        {
            "correctness_pass": True,
            "reproducibility_pass": True,
            "p2h_vs_p2": 1.0,
            "p2h_recovered_budget_excess": 0.7,
            "added_text_recovery": 0.0,
            "hot_text_recovery": 0.25,
        }
        for _ in range(6)
    ]
    assert _hardening_result(cells) == "HOT_LAYOUT_QUALIFIED"


def test_raw_evidence_manifest_is_verified_and_never_replaced(tmp_path) -> None:
    evidence = tmp_path / "raw"
    evidence.mkdir()
    artifact = evidence / "nested" / "artifact.bin"
    artifact.parent.mkdir()
    artifact.write_bytes(b"frozen")

    manifest = _write_raw_manifest(evidence)

    assert manifest == {"path": "raw-evidence-manifest.json", "entry_count": 1}
    with pytest.raises(RuntimeError, match="refusing to replace immutable"):
        _write_raw_manifest(evidence)


def test_timing_variants_exclude_closed_p1_comparison() -> None:
    assert VARIANTS == (
        "P0_O0", "P2_O0", "P2H_O0", "PNEG_O0",
        "P0_O1", "P2_O1", "P2H_O1", "PNEG_O1",
    )


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
