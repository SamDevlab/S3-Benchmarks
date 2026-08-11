"""
Statistical analysis tools for S3 benchmark suite.
Provides N, min, max, median, mean, p95, stddev, relative speed ratios, and throughputs.
"""

import math
from typing import Any

def calculate_stats(samples_ns: list[float]) -> dict[str, float]:
    """Calculates statistical summary for execution time samples in nanoseconds."""
    if not samples_ns:
        return {
            "n": 0, "min": 0.0, "max": 0.0, "median": 0.0,
            "mean": 0.0, "p95": 0.0, "stddev": 0.0
        }

    sorted_samples = sorted(samples_ns)
    n = len(sorted_samples)
    min_val = sorted_samples[0]
    max_val = sorted_samples[-1]

    # Median
    if n % 2 == 1:
        median = sorted_samples[n // 2]
    else:
        median = (sorted_samples[n // 2 - 1] + sorted_samples[n // 2]) / 2.0

    # Mean
    mean = sum(sorted_samples) / n

    # P95
    p95_idx = int(0.95 * (n - 1))
    p95 = sorted_samples[p95_idx]

    # Stddev
    if n > 1:
        variance = sum((x - mean) ** 2 for x in sorted_samples) / (n - 1)
        stddev = math.sqrt(variance)
    else:
        stddev = 0.0

    return {
        "n": float(n),
        "min": min_val,
        "max": max_val,
        "median": median,
        "mean": mean,
        "p95": p95,
        "stddev": stddev,
    }

def format_relative_ratio(target_median: float, reference_median: float) -> tuple[float, str]:
    """
    Computes relative ratio taking reference_median as 1.00x.
    Returns (ratio_float, display_string).
    Lower time is better.
    """
    if reference_median <= 0.0 or target_median <= 0.0:
        return 1.0, "1.00x"
    
    ratio = target_median / reference_median
    if abs(ratio - 1.0) < 0.005:
        return ratio, "1.00x (baseline)"
    elif ratio > 1.0:
        return ratio, f"{ratio:.2f}x slower"
    else:
        speedup = reference_median / target_median
        return ratio, f"{speedup:.2f}x faster"

def calculate_throughput(median_ns: float, num_bytes: int, parses_per_sample: int) -> dict[str, float]:
    """Computes parses/sec and MB/sec based on sample duration in nanoseconds."""
    if median_ns <= 0.0:
        return {"parses_per_sec": 0.0, "mb_per_sec": 0.0}

    seconds = median_ns / 1e9
    total_parses = parses_per_sample
    total_bytes = num_bytes * parses_per_sample

    parses_per_sec = total_parses / seconds
    mb_per_sec = (total_bytes / (1024 * 1024)) / seconds

    return {
        "parses_per_sec": parses_per_sec,
        "mb_per_sec": mb_per_sec,
    }
