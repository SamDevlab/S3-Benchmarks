from __future__ import annotations

import json

from benchmarks.candidate_activation.workloads import performance_cases
from protocol.workload import canonical_json
from tools.native_measurement import _work_units


def test_performance_corpus_is_declared_and_excludes_capability_only_shapes():
    cases = performance_cases()
    assert {case.size for case in cases} == {"small", "medium"}
    assert all(case.workload_id != "compiler.tsvc.initial-subset" for case in cases)
    assert "scientific.rmsd.single" in {case.workload_id for case in cases}
    assert len(cases) == 31


def test_work_units_are_positive_and_stable_for_every_measurement_case():
    cases = performance_cases()
    first = [(case.workload_id, case.size, _work_units(case)) for case in cases]
    second = [(case.workload_id, case.size, _work_units(case)) for case in cases]
    assert first == second
    assert all(units > 0 for _workload_id, _size, units in first)


def test_measurement_policy_is_explicitly_process_e2e_not_kernel_time():
    payload = {
        "timing_scope": "PROCESS_E2E",
        "kernel_time": "NOT_AVAILABLE",
        "setup_scope": "PER_PROCESS_BEFORE_WORKLOAD",
        "anti_dce": "ONE_INTEGER_CANARY_AFTER_WORKLOAD",
        "warmups": 5,
        "repetitions": 30,
        "interleaved": True,
    }
    assert json.loads(canonical_json(payload)) == payload
