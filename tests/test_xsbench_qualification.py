from __future__ import annotations

import hashlib
import math

from benchmarks.scientific.xsbench.contract import (
    DATA,
    FIXTURE_LOOKUPS,
    LOOKUPS_PER_CALL,
    QUERY_ENERGIES,
    QUERY_MATERIALS,
    WORKLOAD_ID,
    fixture_summary,
    fixture_metadata,
    fixture_pilots,
    hosted_source,
    oracle_lookup,
    oracle_result,
    pilot,
    s3_source,
)


def test_xsbench_contract_is_pinned_to_the_baseline_lookup_shape() -> None:
    case = pilot()
    assert case.workload_id == WORKLOAD_ID
    assert case.work_units_per_call == LOOKUPS_PER_CALL
    assert case.logical_shape.startswith("2 materials")
    assert case.family == "scientific-irregular"
    assert "while high - low > 1" in case.source
    assert "factor: f64" in case.source
    assert "checksum" in case.c_source


def test_xsbench_fixture_and_oracle_are_deterministic() -> None:
    first = pilot()
    second = pilot()
    assert first.source == second.source
    assert first.c_source == second.c_source
    assert hashlib.sha256(first.source.encode()).hexdigest() == hashlib.sha256(second.source.encode()).hexdigest()
    assert fixture_summary().data_values == len(DATA)
    assert len(QUERY_ENERGIES) == len(QUERY_MATERIALS) == LOOKUPS_PER_CALL
    assert math.isclose(oracle_result(), 2444.096, rel_tol=1e-12, abs_tol=1e-12)
    assert oracle_lookup(0.05, 0) > 0.0


def test_xsbench_source_preserves_flat_mapping_and_no_optimized_variant() -> None:
    source = s3_source()
    assert "export fn xs_lookup_batch(data: &[f64], metadata: &[i64])" in source
    assert "composition_index: i64 = material * 2 + position" in source
    assert "grid_base: i64 = 10 + nuclide * 25" in source
    assert "middle_energy_ticks: i64 = metadata[middle_index]" in source
    assert "match middle_energy_ticks <=> energy_ticks:" in source
    assert "fn xsbench_binary_search(metadata: &[i64]" in source
    assert "1:\n                high = middle" in source
    assert "xsbench_binary_search(metadata, nuclide, energy_ticks, 4)" in source
    assert "to_i64" not in source
    assert "return checksum" in source
    assert "openmp" not in source.lower()


def test_xsbench_hosted_source_executes_the_same_real_value_contract() -> None:
    source = hosted_source()
    assert "fn main() -> f64:" in source
    assert "fn xs_lookup_batch(data: &f64_vector, metadata: &i64_vector" in source
    assert "f64_vector_get(data," in source
    assert "i64_vector_get(metadata, middle_index)" in source
    assert "f64_vector_push" in source
    assert "return xs_lookup_batch(&data, &metadata)" in source


def test_xsbench_fixture_tiers_have_explicit_lookup_accounting() -> None:
    assert FIXTURE_LOOKUPS == {"TINY": 1, "SMALL": 4, "MEDIUM": 8}
    pilots = fixture_pilots()
    assert [pilot_item.workload_id.rsplit(".", 1)[-1] for pilot_item in pilots] == ["tiny", "small", "medium"]
    for fixture, lookup_count in FIXTURE_LOOKUPS.items():
        metadata = fixture_metadata(fixture)
        assert len(metadata) == 36
        assert metadata[35] == lookup_count
        assert fixture_summary(fixture).lookup_count == lookup_count
        assert math.isclose(fixture_summary(fixture).expected, oracle_result(lookup_count), rel_tol=1e-12, abs_tol=1e-12)
    assert "mut lookup_limit: i64 = metadata[35]" in s3_source()
