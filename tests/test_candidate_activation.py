from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from benchmarks.candidate_activation.adapters import EXPECTED_S3_SHA, run_hosted_matrix
from benchmarks.candidate_activation.workloads import cases


def test_candidate_sources_are_deterministic_and_two_sized() -> None:
    first = [(case.workload_id, case.size, hashlib.sha256(case.source.encode()).hexdigest()) for case in cases()]
    second = [(case.workload_id, case.size, hashlib.sha256(case.source.encode()).hexdigest()) for case in cases()]
    assert first == second
    assert {case.size for case in cases()} == {"tiny", "small"}
    assert all("f64_vector" in case.source for case in cases())


def test_flat_layout_contract_is_explicit() -> None:
    matrix_cases = [case for case in cases() if case.workload_id in {"hpc.prk.transpose", "numerical.polybench.gemm", "language.plb2.matmul"}]
    assert len(matrix_cases) >= 6
    assert all(case.physical_layout == "flat f64_vector" for case in matrix_cases)
    assert all(case.index_mapping for case in matrix_cases)


@pytest.mark.skipif("S3_REPO" not in __import__("os").environ, reason="set S3_REPO for exact candidate execution")
def test_hosted_candidate_activation_matrix() -> None:
    observations = run_hosted_matrix(cases())
    assert observations
    failures = [item.to_dict() for item in observations if item.status != "CORRECTNESS_PASS"]
    assert not failures, json.dumps({"s3_sha": EXPECTED_S3_SHA, "failures": failures}, indent=2)

