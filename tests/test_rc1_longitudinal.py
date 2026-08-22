from __future__ import annotations

import json

import pytest

from benchmarks.rc1.workloads import WORKLOADS, run_all_contract_probes, workload_map
from tools.rc1_longitudinal import _control_drift, _delta, _geomean


def test_rc1_workload_registry_is_complete_and_unique():
    assert [workload.workload_id for workload in WORKLOADS] == [f"P{i}" for i in range(2, 19)]
    assert len(workload_map()) == 17


def test_contract_probes_are_correctness_only_and_fail_closed_on_claims():
    rows = run_all_contract_probes()
    assert len(rows) == 17
    assert all(row["contract_probe"] == "PASS" for row in rows)
    assert all(row["canonical_status"] == "EXPERIMENTAL_WORKLOAD" for row in rows)
    assert all(row["performance_status"] == "DEFERRED_BY_CAPABILITY" for row in rows)
    assert all(row["native_timing"] == "NOT_RUN" for row in rows)
    assert all(row["s3_vs_c_claim"] == "NO" for row in rows)


def test_math_uses_positive_geomean_and_percentage_delta():
    assert _geomean([1.0, 4.0]) == pytest.approx(2.0)
    assert _delta(90.0, 100.0) == pytest.approx(-10.0)
    with pytest.raises(Exception):
        _geomean([0.0, 1.0])


def test_control_drift_crosses_declared_threshold():
    rows = [
        {"c_o2_ns_per_parse_geomean": 100.0},
        {"c_o2_ns_per_parse_geomean": 106.0},
    ]
    drift = _control_drift(rows)
    assert drift["classification"] == "HIGH"
    assert drift["relative_range"] == pytest.approx(0.06)


def test_raw_workload_payload_is_json_stable():
    row = run_all_contract_probes()[0]
    assert len(row["input_sha256"]) == 64
    assert json.dumps(row, sort_keys=True)

