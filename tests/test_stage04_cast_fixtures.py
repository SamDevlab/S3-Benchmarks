from __future__ import annotations

from tools.generate_stage04_cast_fixtures import cases, generate


def test_stage04_cast_fixture_contract(tmp_path) -> None:
    manifest = generate(tmp_path)
    rows = {row["case_id"]: row for row in manifest["cases"]}

    assert set(rows) == {
        "cast_tryte_to_i64",
        "cast_i64_to_f64",
        "cast_i64_to_tryte",
        "cast_invalid_f64_to_tryte",
    }
    assert manifest["compiler_invoked"] is False
    assert manifest["s3ir2_convert_shape"] == {
        "opcode": 10,
        "result_count": 1,
        "operand_count": 1,
        "aux_a": -1,
        "aux_b": -1,
        "ordered_operand_edges": 1,
        "result_edges": 1,
    }
    assert rows["cast_tryte_to_i64"]["strict_conformance_eligible"] is True
    assert rows["cast_i64_to_f64"]["strict_conformance_eligible"] is True
    assert rows["cast_i64_to_tryte"]["strict_conformance_eligible"] is True
    assert rows["cast_invalid_f64_to_tryte"]["strict_conformance_eligible"] is False


def test_cast_sources_use_parameters_not_literal_only() -> None:
    source_by_id = {case.case_id: case.source for case in cases()}
    for case_id in ("cast_tryte_to_i64", "cast_i64_to_f64", "cast_i64_to_tryte"):
        source = source_by_id[case_id]
        assert "value:" in source
        assert "return to_" in source
        assert "(value)" in source
