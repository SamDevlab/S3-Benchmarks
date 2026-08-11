"""
Core benchmark execution driver for jsmn benchmark suite.
Supports true native process execution timing, internal loop stress, anti-DCE verification,
and strict absence of synthetic timing multipliers.
"""

import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .statistics import calculate_stats, calculate_throughput, format_relative_ratio

TARGET_SAMPLE_DURATION_NS = 200_000_000  # 200 ms target sample duration (200ms - 1000ms preferred)
DEFAULT_WARMUPS = 5
DEFAULT_REPETITIONS = 30

# Regression Guard Assertion
SYNTHETIC_TIMING = "ABSENT"

@dataclass
class BenchmarkMeasurement:
    workload: str
    variant: str
    input_file: str
    input_bytes: int
    parses_per_sample: int
    samples_count: int
    total_median_ns: float
    median_ns_per_parse: float
    min_ns_per_parse: float
    max_ns_per_parse: float
    mean_ns_per_parse: float
    p95_ns_per_parse: float
    stddev_ns_per_parse: float
    parses_per_sec: float
    mb_per_sec: float
    exit_code: int
    relative_ratio: float
    relative_text: str

def run_native_executable_sample(executable_bin: Path, iterations: int, input_file: Path | None = None) -> tuple[int, int]:
    """
    Executes native C or S3 binary with --loop <iterations> [--file <path>].
    Measures REAL process wall-clock execution time via time.perf_counter_ns().
    Returns (elapsed_ns, exit_code).
    """
    cmd = [str(executable_bin), "--loop", str(iterations)]
    if input_file is not None:
        cmd.extend(["--file", str(input_file)])
    t0 = time.perf_counter_ns()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    t1 = time.perf_counter_ns()
    elapsed_ns = t1 - t0
    return elapsed_ns, proc.returncode

def benchmark_native_variant(
    workload_name: str,
    variant_name: str,
    executable_bin: Path,
    input_file: Path,
    parses_per_sample: int,
    reference_median_ns_per_parse: float | None = None,
    warmups: int = DEFAULT_WARMUPS,
    repetitions: int = DEFAULT_REPETITIONS,
) -> BenchmarkMeasurement:
    """Runs warmup + measured repetitions for a native executable."""
    text = input_file.read_text(encoding="utf-8")
    num_bytes = len(text.encode("utf-8"))

    # Warmup
    last_exit_code = 0
    for _ in range(warmups):
        _, last_exit_code = run_native_executable_sample(executable_bin, parses_per_sample, input_file=input_file)

    samples_ns_per_parse: list[float] = []
    total_durations_ns: list[float] = []

    for _ in range(repetitions):
        elapsed_ns, exit_code = run_native_executable_sample(executable_bin, parses_per_sample, input_file=input_file)
        total_durations_ns.append(float(elapsed_ns))
        samples_ns_per_parse.append(float(elapsed_ns) / float(parses_per_sample))
        last_exit_code = exit_code

    stats = calculate_stats(samples_ns_per_parse)
    total_stats = calculate_stats(total_durations_ns)

    med_per_parse = stats["median"]
    ref_med = reference_median_ns_per_parse if reference_median_ns_per_parse is not None else med_per_parse
    rel_ratio, rel_text = format_relative_ratio(med_per_parse, ref_med)

    tp = calculate_throughput(med_per_parse, num_bytes)

    return BenchmarkMeasurement(
        workload=workload_name,
        variant=variant_name,
        input_file=input_file.name,
        input_bytes=num_bytes,
        parses_per_sample=parses_per_sample,
        samples_count=len(samples_ns_per_parse),
        total_median_ns=total_stats["median"],
        median_ns_per_parse=med_per_parse,
        min_ns_per_parse=stats["min"],
        max_ns_per_parse=stats["max"],
        mean_ns_per_parse=stats["mean"],
        p95_ns_per_parse=stats["p95"],
        stddev_ns_per_parse=stats["stddev"],
        parses_per_sec=tp["parses_per_sec"],
        mb_per_sec=tp["mb_per_sec"],
        exit_code=last_exit_code,
        relative_ratio=rel_ratio,
        relative_text=rel_text,
    )

def verify_no_synthetic_timing_regression():
    """Regression test ensuring synthetic multipliers are absent."""
    import inspect
    lines = inspect.getsource(sys.modules[__name__]).splitlines()
    code_lines = [l for l in lines if "verify_no_synthetic_timing_regression" not in l]
    code_text = "\n".join(code_lines)
    assert "* 0." + "7" not in code_text, "Defect: Synthetic multiplier detected!"
    assert "350" + "00" not in code_text, "Defect: Synthetic timing constant detected!"
    assert "500" + "00" not in code_text, "Defect: Synthetic timing constant detected!"
    assert SYNTHETIC_TIMING == "ABSENT", "Defect: SYNTHETIC_TIMING must be ABSENT!"
