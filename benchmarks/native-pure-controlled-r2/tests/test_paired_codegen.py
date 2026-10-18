from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1]))
from paired_codegen import (  # noqa: E402
    artifact_identity,
    function_assembly_shape,
    orientation_schedule,
    paired_metrics,
)


@pytest.mark.parametrize("samples", [15, 16, 41])
def test_orientation_schedule_balances_pair_position(samples: int) -> None:
    schedule = orientation_schedule(samples, seed=124)
    assert len(schedule) == samples
    assert sum(schedule) == (samples + 1) // 2
    assert schedule == orientation_schedule(samples, seed=124)


def test_paired_metrics_keeps_pairing_and_reports_exact_gain() -> None:
    result = paired_metrics(
        [100.0 + index for index in range(15)],
        [50.0 + index / 2 for index in range(15)],
        seed=9,
    )
    assert result["paired_rounds"] == 15
    assert result["median_ratio"] == pytest.approx(0.5)
    assert result["median_delta_ns_per_call"] == pytest.approx(-53.5)
    assert result["bootstrap_95ci_median_ratio"] == pytest.approx([0.5, 0.5])


def test_paired_metrics_rejects_unpaired_inputs() -> None:
    with pytest.raises(ValueError, match="equal nonzero lengths"):
        paired_metrics([1.0], [], seed=2)


def test_build_worker_identity_includes_workload() -> None:
    row = {
        "revision_label": "CANDIDATE",
        "profile": "PURE_EXPERIMENTAL/O1",
        "workload": "energy_series_aggregation",
    }
    identity = artifact_identity(row)
    assert identity == ("CANDIDATE", "PURE_EXPERIMENTAL", "energy_series_aggregation")


def test_function_assembly_shape_distinguishes_scratch_and_resident_loads(tmp_path: Path) -> None:
    baseline = tmp_path / "baseline.s"
    candidate = tmp_path / "candidate.s"
    baseline.write_text(
        "kernel:\n"
        "    mov r10, rdi\n"
        "    mov r11, rsi\n"
        "    mov rax, rdx\n"
        "    cmp rax, r11\n"
        "    jae .Lfail\n"
        "    mov r11, qword ptr [r10 + rax * 8]\n"
        "    mov rdi, r11\n"
        ".size kernel, .-kernel\n",
        encoding="utf-8",
    )
    candidate.write_text(
        "kernel:\n"
        "    cmp rdx, rsi\n"
        "    jae .Lfail\n"
        "    mov rdi, qword ptr [rdi + rdx * 8]\n"
        ".size kernel, .-kernel\n",
        encoding="utf-8",
    )
    before = function_assembly_shape(baseline, "kernel")
    after = function_assembly_shape(candidate, "kernel")

    assert before["scratch_scaled_qword_loads"] == 1
    assert before["resident_register_scaled_qword_loads"] == 0
    assert after["scratch_scaled_qword_loads"] == 0
    assert after["resident_register_scaled_qword_loads"] == 1
    assert after["resident_base_scaled_qword_loads"] == 1
    assert before["static_assembly_instruction_lines"] - after["static_assembly_instruction_lines"] == 4


def test_function_assembly_shape_counts_resident_base_with_index_scratch(tmp_path: Path) -> None:
    assembly = tmp_path / "hybrid.s"
    assembly.write_text(
        "kernel:\n"
        "    mov rax, rdx\n"
        "    cmp rax, rsi\n"
        "    jae .Lfail\n"
        "    mov rdx, qword ptr [r14 + rax * 8]\n"
        ".size kernel, .-kernel\n",
        encoding="utf-8",
    )

    shape = function_assembly_shape(assembly, "kernel")

    assert shape["scratch_scaled_qword_loads"] == 0
    assert shape["resident_register_scaled_qword_loads"] == 0
    assert shape["resident_base_scaled_qword_loads"] == 1
