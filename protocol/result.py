"""Machine-readable result-v2 envelope with raw-sample preservation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from .measurement import MeasurementProtocol, summarize_samples


class ResultError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class BenchmarkResult:
    run_id: str
    benchmark_repo_sha: str
    s3_sha: str
    upstream_shas: dict[str, str]
    environment: dict[str, Any]
    workload: dict[str, Any]
    variant: dict[str, Any]
    correctness: dict[str, Any]
    build: dict[str, Any]
    measurement_protocol: MeasurementProtocol
    samples: tuple[float, ...]
    work_units: int
    artifact_metrics: dict[str, Any]
    hardware_metrics: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        if self.measurement_protocol.synthetic_timing:
            raise ResultError("synthetic timing cannot be serialized")
        stats = summarize_samples(self.samples, self.work_units) if self.samples else {}
        return {
            "schema": "s3.benchmark.result.v2",
            "run": {
                "run_id": self.run_id,
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "reproducibility_level": "SINGLE_RUN",
            },
            "provenance": {
                "benchmark_repo_sha": self.benchmark_repo_sha,
                "s3_sha": self.s3_sha,
                "upstream_shas": dict(sorted(self.upstream_shas.items())),
            },
            "environment": self.environment,
            "workload": self.workload,
            "variant": self.variant,
            "correctness": self.correctness,
            "build": self.build,
            "measurement_protocol": {
                "timing_scope": self.measurement_protocol.timing_scope,
                "warmups": self.measurement_protocol.warmups,
                "repetitions": self.measurement_protocol.repetitions,
                "target_sample_duration_ns": self.measurement_protocol.target_sample_duration_ns,
                "interleaved": self.measurement_protocol.interleaved,
                "synthetic_timing": self.measurement_protocol.synthetic_timing,
            },
            "samples": list(self.samples),
            "statistics": stats,
            "artifact_metrics": self.artifact_metrics,
            "hardware_metrics": self.hardware_metrics,
            "derived_metrics": {
                "energy": "NOT_MEASURED",
                "perf_counters": "NOT_AVAILABLE",
            },
        }
