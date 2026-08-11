"""
Core benchmark execution driver for jsmn benchmark suite.
Supports loop stress scaling, monotonic timing, anti-optimization verification,
and separate setup vs parser execution timing.
"""

import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .statistics import calculate_stats, calculate_throughput, format_relative_ratio

TARGET_SAMPLE_DURATION_NS = 100_000_000  # 100 ms target sample duration
DEFAULT_WARMUPS = 5
DEFAULT_REPETITIONS = 30

@dataclass
class BenchmarkMeasurement:
    workload: str
    variant: str
    input_file: str
    input_bytes: int
    parses_per_sample: int
    samples_count: int
    median_ns: float
    min_ns: float
    max_ns: float
    mean_ns: float
    p95_ns: float
    stddev_ns: float
    parses_per_sec: float
    mb_per_sec: float
    checksum: int
    relative_ratio: float
    relative_text: str

def calibrate_iteration_multiplier(
    runner_cmd_fn, text: str, initial_iterations: int = 100
) -> int:
    """Calibrates iteration multiplier so each sample lasts >= 100ms."""
    iterations = initial_iterations
    for _ in range(5):
        res = runner_cmd_fn(text, iterations)
        elapsed = res.get("elapsed_ns", 0)
        if elapsed >= TARGET_SAMPLE_DURATION_NS:
            return iterations
        if elapsed <= 0:
            iterations *= 10
        else:
            scale = TARGET_SAMPLE_DURATION_NS / elapsed
            iterations = max(int(iterations * scale * 1.1), iterations * 2)
        if iterations > 10_000_000:
            break
    return iterations

def run_c_benchmark_sample(c_bin: Path, text: str, iterations: int) -> dict[str, Any]:
    """Runs single benchmark sample using C runner binary."""
    proc = subprocess.run(
        [str(c_bin), "--benchmark", str(iterations), text],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(proc.stdout.strip())

def benchmark_variant(
    workload_name: str,
    variant_name: str,
    runner_fn,
    input_file: Path,
    reference_median: float | None = None,
    warmups: int = DEFAULT_WARMUPS,
    repetitions: int = DEFAULT_REPETITIONS,
) -> BenchmarkMeasurement:
    """Runs full warmup + measured repetitions for a single variant and input file."""
    text = input_file.read_text(encoding="utf-8")
    num_bytes = len(text.encode("utf-8"))

    # Calibrate multiplier
    iterations = calibrate_iteration_multiplier(runner_fn, text, initial_iterations=100)

    # Warmup
    for _ in range(warmups):
        runner_fn(text, iterations)

    samples_ns: list[float] = []
    last_checksum = 0

    for _ in range(repetitions):
        res = runner_fn(text, iterations)
        samples_ns.append(float(res["elapsed_ns"]))
        last_checksum = res["checksum"]

    stats = calculate_stats(samples_ns)
    tp = calculate_throughput(stats["median"], num_bytes, iterations)

    ref_med = reference_median if reference_median is not None else stats["median"]
    rel_ratio, rel_text = format_relative_ratio(stats["median"], ref_med)

    return BenchmarkMeasurement(
        workload=workload_name,
        variant=variant_name,
        input_file=input_file.name,
        input_bytes=num_bytes,
        parses_per_sample=iterations,
        samples_count=len(samples_ns),
        median_ns=stats["median"],
        min_ns=stats["min"],
        max_ns=stats["max"],
        mean_ns=stats["mean"],
        p95_ns=stats["p95"],
        stddev_ns=stats["stddev"],
        parses_per_sec=tp["parses_per_sec"],
        mb_per_sec=tp["mb_per_sec"],
        checksum=last_checksum,
        relative_ratio=rel_ratio,
        relative_text=rel_text,
    )
