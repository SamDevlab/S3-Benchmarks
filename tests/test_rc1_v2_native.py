from __future__ import annotations

import pytest

from benchmarks.rc1.native_workloads import NATIVE_WORKLOADS
from benchmarks.rc1.statistics import bootstrap_median_ci, classify_paired_delta, robust_stats
from tools.p1_stability import _paired_delta, _sample_row


def test_v2_statistics_are_sample_level_and_deterministic():
    values = [10.0, 11.0, 12.0, 13.0, 14.0]
    stats = robust_stats(values)
    assert stats["count"] == 5
    assert stats["median"] == 12.0
    assert stats["iqr"] == 2.0
    assert bootstrap_median_ci(values) == bootstrap_median_ci(values)


def test_v2_classification_requires_stable_control():
    assert classify_paired_delta(-5.0, (-8.0, -2.0), True) == "IMPROVED"
    assert classify_paired_delta(5.0, (2.0, 8.0), True) == "REGRESSED"
    assert classify_paired_delta(-5.0, (-8.0, -2.0), False) == "INCONCLUSIVE"


def test_p1_pairing_uses_fixture_local_measurement_ordinals():
    rows = []
    for checkpoint, elapsed in (("H4", 100), ("H5", 90)):
        rows.append(_sample_row(run_id="r", block_id="block-000", sequence_index=len(rows), checkpoint=checkpoint, variant="O1", fixture="tiny", elapsed_ns=elapsed, parses=1, role="candidate", affinity="taskset -c 0", measurement_index=0))
    paired = _paired_delta(rows, "H4", "H5")
    assert paired["count"] == 1
    assert paired["median_percent"] == pytest.approx(-10.0)


def test_native_workloads_are_pinned_and_have_both_implementations():
    assert [item.workload_id for item in NATIVE_WORKLOADS] == ["P7", "P8", "P9"]
    for item in NATIVE_WORKLOADS:
        assert item.s3_source.strip().startswith("fn ")
        assert "program returned:" in item.c_source
        assert item.operations_per_run > 0
