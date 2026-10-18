from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1]))
from combine_sessions import pair_records  # noqa: E402


def _pair() -> list[dict[str, object]]:
    common = {
        "phase": "measured",
        "profile": "PURE_EXPERIMENTAL",
        "workload": "energy_series_aggregation",
        "size": "small",
        "round": 3,
        "pair_id": "PURE_EXPERIMENTAL|energy_series_aggregation|small|3",
        "fixture_sha256": "fixture",
        "source_sha256": "source",
        "work_units_per_call": 42,
        "pair_order": ["CANDIDATE", "BASELINE"],
    }
    return [
        {**common, "revision": "CANDIDATE", "position_in_pair": 0, "ns_per_call": 9.0},
        {**common, "revision": "BASELINE", "position_in_pair": 1, "ns_per_call": 10.0},
    ]


def test_pair_records_preserves_randomized_orientation() -> None:
    paired = pair_records(_pair())
    values = paired[("PURE_EXPERIMENTAL", "energy_series_aggregation", "small", 3)]
    assert values["BASELINE"]["ns_per_call"] == 10.0
    assert values["CANDIDATE"]["ns_per_call"] == 9.0


def test_pair_records_rejects_missing_or_duplicate_observation() -> None:
    rows = _pair()
    with pytest.raises(ValueError, match="exactly two"):
        pair_records(rows[:1])
    with pytest.raises(ValueError, match="exactly two"):
        pair_records(rows + [rows[0]])


def test_pair_records_rejects_inconsistent_inputs() -> None:
    rows = _pair()
    rows[1] = {**rows[1], "fixture_sha256": "other-fixture"}
    with pytest.raises(ValueError, match="fixture_sha256"):
        pair_records(rows)
