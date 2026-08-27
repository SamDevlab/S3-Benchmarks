from __future__ import annotations

import hashlib
from pathlib import Path

from tools.generate_bootstrap_fuzz_corpus import cases, generate


def test_case_ids_and_sources_are_deterministic() -> None:
    first = cases()
    second = cases()
    assert first == second
    assert len({case.case_id for case in first}) == len(first)
    assert all(case.source.endswith("\n") for case in first)


def test_generator_writes_hash_locked_manifest(tmp_path: Path) -> None:
    manifest = generate(tmp_path)
    assert manifest["schema"] == "s3.bootstrap-fuzz-corpus.v1"
    assert manifest["deterministic"] is True
    assert manifest["compiler_invoked"] is False
    assert manifest["case_count"] == len(cases())
    assert {
        "wide_literals",
        "parameters",
        "calls",
        "locals",
        "control_flow",
        "control_flow_calls",
        "arrays_control_flow",
    } <= set(manifest["categories"])

    for record in manifest["cases"]:
        data = (tmp_path / record["path"]).read_bytes()
        assert hashlib.sha256(data).hexdigest() == record["sha256"]
        assert len(data) == record["bytes"]


def test_seventh_parameter_case_is_explicit_fail_closed_probe() -> None:
    case = next(item for item in cases() if item.case_id == "parameter_ordinal_6")
    assert "g: i64" in case.source
    assert "return g" in case.source
    assert "FAIL_CLOSED" in case.current_stage1_expectation
    assert "call_dataflow" in case.required_surfaces


def test_nested_and_reused_call_results_require_def_use_and_call_dataflow() -> None:
    selected = {
        case.case_id: case
        for case in cases()
        if case.case_id in {"nested_calls", "call_result_reuse"}
    }
    assert set(selected) == {"nested_calls", "call_result_reuse"}
    for case in selected.values():
        assert "instruction_def_use" in case.required_surfaces
        assert "call_dataflow" in case.required_surfaces


def test_wide_literal_cases_are_not_preclassified_as_compiler_failures() -> None:
    wide = [case for case in cases() if case.category == "wide_literals"]
    assert len(wide) == 2
    assert all("VALID_SOURCE" in case.current_stage1_expectation for case in wide)


def test_control_flow_cases_require_complete_terminators() -> None:
    selected = [
        case
        for case in cases()
        if case.category in {"control_flow", "control_flow_calls", "arrays_control_flow"}
    ]
    assert len(selected) == 4
    assert all("complete_terminators" in case.required_surfaces for case in selected)
    assert any("match -1:" in case.source for case in selected)
    assert any("while value <=> 3:" in case.source for case in selected)
