"""Correctness contracts shared by all workload adapters."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class CorrectnessResult:
    status: str
    expected: Any = None
    observed: Any = None
    exact_match: bool | None = None
    abs_error: float | None = None
    rel_error: float | None = None
    tolerance: dict[str, float] | None = None
    first_missing_capability: str | None = None
    evidence: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "expected": self.expected,
            "observed": self.observed,
            "exact_match": self.exact_match,
            "abs_error": self.abs_error,
            "rel_error": self.rel_error,
            "tolerance": self.tolerance,
            "first_missing_capability": self.first_missing_capability,
            "evidence": self.evidence,
        }


def exact(expected: Any, observed: Any) -> CorrectnessResult:
    matched = expected == observed
    return CorrectnessResult(
        status="PASS" if matched else "FAIL",
        expected=expected,
        observed=observed,
        exact_match=matched,
    )


def not_supported(*, capability: str, evidence: str, minimum_required_capability: str) -> CorrectnessResult:
    return CorrectnessResult(
        status="NOT_SUPPORTED_YET",
        first_missing_capability=capability,
        evidence=evidence,
        tolerance={"minimum_required_capability": minimum_required_capability},
    )
