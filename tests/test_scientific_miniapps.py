from __future__ import annotations

import hashlib

from benchmarks.scientific.rmsd.expansion import expansion_cases
from benchmarks.scientific.rmsd.reference import batch_rmsd, rmsd


def test_rmsd_expansion_has_five_deterministic_profiles() -> None:
    first = expansion_cases()
    second = expansion_cases()
    assert [case.workload_id for case in first] == [
        "scientific.rmsd.small",
        "scientific.rmsd.medium",
        "scientific.rmsd.large",
        "scientific.rmsd.batch_large",
        "scientific.rmsd.matrix_large",
    ]
    assert [(case.workload_id, hashlib.sha256(case.source.encode()).hexdigest()) for case in first] == [
        (case.workload_id, hashlib.sha256(case.source.encode()).hexdigest()) for case in second
    ]


def test_rmsd_expansion_oracles_are_independent_and_positive() -> None:
    cases = expansion_cases()
    assert cases[0].expected == rmsd(tuple(float(i + 1) for i in range(7)), tuple(float(i + 2) for i in range(7)))
    pairs = [((float(i + 1), float(i + 2), float(i + 3)), (float(i + 2), float(i + 3), float(i + 4))) for i in range(64)]
    assert cases[3].expected == sum(batch_rmsd(pairs))
    assert cases[4].expected == 64.0
    assert all(case.expected > 0.0 for case in cases)


def test_rmsd_expansion_sources_preserve_flat_layout_and_sqrt() -> None:
    for case in expansion_cases():
        assert case.physical_layout == "flat f64_vector"
        assert not case.source.startswith("foreign fn sqrt(value: f64) -> f64\n")
        assert "candidate_sqrt" in case.source
        assert "while" in case.source
        assert case.index_mapping
