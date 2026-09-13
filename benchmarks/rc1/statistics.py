"""Deterministic paired statistics for RC1 stability campaigns."""

from __future__ import annotations

import math
import random
import statistics
from typing import Iterable


def _quantile(values: list[float], fraction: float) -> float:
    if not values:
        raise ValueError("statistics require at least one value")
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = (len(ordered) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def robust_stats(values: Iterable[float]) -> dict[str, float | int]:
    samples = [float(value) for value in values]
    if not samples:
        raise ValueError("statistics require at least one value")
    median = statistics.median(samples)
    deviations = [abs(value - median) for value in samples]
    return {
        "count": len(samples),
        "min": min(samples),
        "max": max(samples),
        "mean": statistics.fmean(samples),
        "median": median,
        "p25": _quantile(samples, 0.25),
        "p75": _quantile(samples, 0.75),
        "iqr": _quantile(samples, 0.75) - _quantile(samples, 0.25),
        "mad": statistics.median(deviations),
    }


def bootstrap_median_ci(values: Iterable[float], *, seed: int = 0, resamples: int = 2000) -> tuple[float, float]:
    samples = [float(value) for value in values]
    if not samples:
        raise ValueError("bootstrap requires at least one value")
    rng = random.Random(seed)
    medians = [
        statistics.median(rng.choice(samples) for _ in samples)
        for _ in range(resamples)
    ]
    return _quantile(medians, 0.025), _quantile(medians, 0.975)


def classify_paired_delta(delta_percent: float, ci95: tuple[float, float], control_stable: bool) -> str:
    if not control_stable:
        return "INCONCLUSIVE"
    low, high = ci95
    if delta_percent <= -3.0 and high < 0.0:
        return "IMPROVED"
    if delta_percent >= 3.0 and low > 0.0:
        return "REGRESSED"
    return "UNCHANGED_WITHIN_NOISE"

