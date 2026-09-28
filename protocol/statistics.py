"""Generic statistics; raw samples are always retained by callers."""

from __future__ import annotations

import math
import statistics
from typing import Iterable


def summarize(samples: Iterable[float]) -> dict[str, float | int]:
    values = [float(value) for value in samples]
    if not values:
        raise ValueError("at least one measured sample is required")
    ordered = sorted(values)
    median = statistics.median(ordered)
    deviations = sorted(abs(value - median) for value in ordered)
    mad = statistics.median(deviations)
    mean = statistics.fmean(ordered)
    stddev = statistics.stdev(ordered) if len(ordered) > 1 else 0.0
    p95_index = max(0, math.ceil(0.95 * len(ordered)) - 1)
    return {
        "n": len(ordered),
        "min": ordered[0],
        "median": median,
        "mean": mean,
        "max": ordered[-1],
        "p95": ordered[p95_index],
        "stddev": stddev,
        "mad": mad,
        "cv": (stddev / mean) if mean else 0.0,
    }
