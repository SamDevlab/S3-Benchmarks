"""Interleaved timing characterization of one already-pinned S3 candidate pair."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import platform
import random
import statistics
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.s3_111_candidate_replay import (
    EXPECTED_S3_COMMIT,
    EXPECTED_S3_TREE,
    EXPERIMENT_LABELS,
    _git,
    _load_pinned_benchmark,
    _verify_artifact,
)


def _paired_summary(
    baseline: list[float], candidate: list[float], *, seed: int, resamples: int = 10_000
) -> dict[str, Any]:
    if len(baseline) != len(candidate) or len(baseline) < 3:
        raise ValueError("paired timing requires equal sample counts >= 3")
    ratios = [left / right for left, right in zip(baseline, candidate, strict=True)]
    rng = random.Random(seed)
    bootstrap = sorted(
        statistics.median(rng.choices(ratios, k=len(ratios)))
        for _ in range(resamples)
    )
    low = bootstrap[int(0.025 * resamples)]
    high = bootstrap[int(0.975 * resamples) - 1]
    if low > 1.05:
        classification = "MATERIAL_IMPROVEMENT"
    elif high < 0.95:
        classification = "MATERIAL_REGRESSION"
    elif low >= 0.95 and high <= 1.05:
        classification = "NO_MATERIAL_CHANGE_WITHIN_5_PERCENT"
    else:
        classification = "INCONCLUSIVE"
    return {
        "baseline_over_candidate_median_ratio": statistics.median(ratios),
        "paired_bootstrap_95_percentile_interval": [low, high],
        "resamples": resamples,
        "seed": seed,
        "material_change_threshold": 0.05,
        "classification": classification,
    }


def characterize(
    *,
    source_root: Path,
    experiment_path: Path,
    binary_root: Path,
    workload_id: str = "engineering.point-cloud-summary.v1",
    iterations: int = 1000,
    warmups: int = 3,
    samples: int = 21,
) -> dict[str, Any]:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("candidate timing requires Linux x86-64")
    source_root = source_root.resolve()
    experiment_bytes = experiment_path.read_bytes()
    experiment = json.loads(experiment_bytes)
    experiment_id = experiment.get("experiment_id")
    label = EXPERIMENT_LABELS.get(experiment_id)
    if label != "store_to_load":
        raise ValueError("confirmatory run is restricted to the pinned STORE-to-LOAD candidate")
    if _git(source_root, "rev-parse", "HEAD") != EXPECTED_S3_COMMIT:
        raise ValueError("S3 source commit differs from the pinned control")
    if _git(source_root, "rev-parse", "HEAD^{tree}") != EXPECTED_S3_TREE:
        raise ValueError("S3 source tree differs from the pinned control")
    if _git(source_root, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("pinned S3 source checkout must be clean")
    control = experiment.get("control")
    if not isinstance(control, dict) or control.get("s3_commit") != EXPECTED_S3_COMMIT:
        raise ValueError("experiment and pinned S3 source identities differ")

    row = next(
        (item for item in experiment.get("workloads", []) if item.get("workload_id") == workload_id),
        None,
    )
    if row is None:
        raise ValueError(f"workload missing from experiment: {workload_id}")
    artifacts = row.get("native_artifacts")
    if not isinstance(artifacts, dict):
        raise ValueError("baseline/candidate binary descriptors are missing")
    baseline_path = binary_root / f"{workload_id}-baseline.so"
    candidate_path = binary_root / f"{workload_id}-{label}.so"
    baseline_artifact = _verify_artifact(baseline_path, artifacts.get("baseline"))
    candidate_artifact = _verify_artifact(candidate_path, artifacts.get(label))

    benchmark = _load_pinned_benchmark(source_root)
    _, references = benchmark._load_inputs()
    reference = next(
        item for item in references["workloads"] if item["workload_id"] == workload_id
    )
    libraries = {
        "baseline": ctypes.CDLL(str(baseline_path)),
        "candidate": ctypes.CDLL(str(candidate_path)),
    }
    calls = {}
    recorded = row["native_output"]
    for name, library in libraries.items():
        output = (ctypes.c_double * len(benchmark.OUTPUT_KEYS[workload_id]))()
        call = benchmark._make_call(library, reference, output)
        if call() != 0:
            raise RuntimeError(f"{name} correctness invocation failed")
        values = list(output)
        benchmark._check_output(values, reference["expected_output"], workload_id)
        expected_digest = recorded[name if name == "baseline" else label]["output_sha256"]
        actual_digest = hashlib.sha256(
            benchmark._json_bytes([round(value, 10) for value in values])
        ).hexdigest()
        if actual_digest != expected_digest:
            raise ValueError(f"{name} correctness output differs from pinned experiment")
        calls[name] = call

    for _ in range(warmups):
        for call in calls.values():
            if call() != 0:
                raise RuntimeError("candidate pair failed during warmup")

    timing_samples: dict[str, list[float]] = {"baseline": [], "candidate": []}
    paired_order: list[list[str]] = []
    for index in range(samples):
        order = ["baseline", "candidate"] if index % 2 == 0 else ["candidate", "baseline"]
        paired_order.append(order)
        for name in order:
            timing_samples[name].append(benchmark._measure(calls[name], iterations))

    return {
        "schema_version": "1.0.0",
        "report_kind": "S3_BENCHMARKS_PINNED_CANDIDATE_TIMING_CONFIRMATION",
        "experiment_id": experiment_id,
        "workload_id": workload_id,
        "status": "PASS",
        "classification": "CHARACTERIZATION_ONLY_NO_PROMOTION",
        "provenance": {
            "s3_commit": EXPECTED_S3_COMMIT,
            "s3_tree": EXPECTED_S3_TREE,
            "s3_worktree_clean": True,
            "experiment_sha256": hashlib.sha256(experiment_bytes).hexdigest(),
            "bench_commit": _git(Path(__file__).resolve().parents[1], "rev-parse", "HEAD"),
            "bench_tree": _git(Path(__file__).resolve().parents[1], "rev-parse", "HEAD^{tree}"),
            "bench_worktree_dirty": bool(
                _git(Path(__file__).resolve().parents[1], "status", "--porcelain")
            ),
            "target": "Linux x86-64",
            "timing_helper": "pinned S3 benchmark _measure; candidate order alternates per sample",
            "hardware_counters": "UNAVAILABLE_BY_POLICY_NOT_PROBED_AGAIN",
        },
        "protocol": {
            "warmups": warmups,
            "samples": samples,
            "iterations_per_sample": iterations,
            "paired_order": paired_order,
            "timing_class": "CHARACTERIZATION_ONLY",
            "native_speedup_claim": False,
        },
        "artifacts": {"baseline": baseline_artifact, "candidate": candidate_artifact},
        "correctness": {
            "baseline_reference": "PASS",
            "candidate_reference": "PASS",
            "baseline_output_sha256": recorded["baseline"]["output_sha256"],
            "candidate_output_sha256": recorded[label]["output_sha256"],
            "outputs_equal": recorded["baseline"]["output_sha256"]
            == recorded[label]["output_sha256"],
        },
        "timing": {
            "baseline": timing_samples["baseline"],
            "candidate": timing_samples["candidate"],
            "baseline_median_ns_per_call": statistics.median(timing_samples["baseline"]),
            "candidate_median_ns_per_call": statistics.median(timing_samples["candidate"]),
            "paired_baseline_over_candidate": _paired_summary(
                timing_samples["baseline"], timing_samples["candidate"], seed=111121
            ),
        },
        "static_tradeoff": {
            "native_binary_deltas": row["native_binary"]["delta"],
            "peak_live_delta": row["pressure_guard"]["peak_live_delta"],
            "stack_resident_virtual_delta": row["pressure_guard"]["stack_resident_virtual_delta"],
            "adaptive_candidate_selected": row["pressure_guard"]["adaptive_candidate_selected"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-source", type=Path, required=True)
    parser.add_argument("--experiment", type=Path, required=True)
    parser.add_argument("--binary-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = characterize(
        source_root=args.s3_source,
        experiment_path=args.experiment,
        binary_root=args.binary_root,
    )
    encoded = (json.dumps(report, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded)
    summary = report["timing"]["paired_baseline_over_candidate"]
    print(
        f"OUTPUT={args.output}\nTIMING={summary['classification']} "
        f"RATIO={summary['baseline_over_candidate_median_ratio']:.6f} "
        f"CI95={summary['paired_bootstrap_95_percentile_interval']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
