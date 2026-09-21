"""Deterministic RMSD expansion cases for the scientific mini-app phase."""

from __future__ import annotations

from dataclasses import replace

from benchmarks.candidate_activation.workloads import (
    WorkloadCase,
    _rmsd_batch_source,
    _rmsd_matrix_source,
    _rmsd_single_source,
)

from .reference import batch_rmsd, rmsd


def _single_case(profile: str, length: int) -> WorkloadCase:
    left = tuple(float(index + 1) for index in range(length))
    right = tuple(float(index + 2) for index in range(length))
    expected = rmsd(left, right)
    base = WorkloadCase(
        workload_id=f"scientific.rmsd.{profile.lower()}",
        size=profile,
        source=_rmsd_single_source(length),
        expected=expected,
        classification="SUPPORTED_WITH_BENCHMARK_ADAPTER",
        logical_shape=f"two vectors of length {length}",
        physical_layout="flat f64_vector",
        index_mapping="i",
    )
    return replace(base, expected=float(expected))


def _batch_large_case(pair_count: int, coordinates: int = 3) -> WorkloadCase:
    pairs = [
        (
            tuple(float(pair * coordinates + coordinate + 1) for coordinate in range(coordinates)),
            tuple(float(pair * coordinates + coordinate + 2) for coordinate in range(coordinates)),
        )
        for pair in range(pair_count)
    ]
    expected = sum(batch_rmsd(pairs))
    return WorkloadCase(
        workload_id="scientific.rmsd.batch_large",
        size="BATCH_LARGE",
        source=_rmsd_batch_source(pair_count),
        expected=float(expected),
        classification="SUPPORTED_WITH_BENCHMARK_ADAPTER",
        logical_shape=f"{pair_count} vector pairs x {coordinates} coordinates",
        physical_layout="flat f64_vector",
        index_mapping="pair * coordinates + coordinate",
    )


def _matrix_large_case(dimension: int, coordinates: int = 3) -> WorkloadCase:
    pair = ((1.0,) * coordinates, (2.0,) * coordinates)
    expected = sum(batch_rmsd([pair])[0] for _ in range(dimension * dimension))
    return WorkloadCase(
        workload_id="scientific.rmsd.matrix_large",
        size="MATRIX_LARGE",
        source=_rmsd_matrix_source(dimension),
        expected=float(expected),
        classification="SUPPORTED_WITH_BENCHMARK_ADAPTER",
        logical_shape=f"{dimension} x {dimension} pair matrix x {coordinates} coordinates",
        physical_layout="flat f64_vector",
        index_mapping="(row * dimension + column) * coordinates + coordinate",
    )


def expansion_cases() -> tuple[WorkloadCase, ...]:
    """Return the frozen RMSD expansion matrix in deterministic order."""

    return (
        _single_case("SMALL", 7),
        _single_case("MEDIUM", 31),
        _single_case("LARGE", 127),
        _batch_large_case(64),
        _matrix_large_case(8),
    )
