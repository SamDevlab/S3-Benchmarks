"""Generic, workload-independent evidence contracts for S3-Benchmarks."""

from .correctness import CorrectnessResult, not_supported
from .measurement import MeasurementProtocol, summarize_samples
from .provenance import ProvenanceError, require_commit
from .registry import load_registry, registry_digest
from .result import BenchmarkResult, ResultError
from .workload import BenchmarkWorkload, WorkloadStatus, load_workload

__all__ = [
    "BenchmarkWorkload",
    "BenchmarkResult",
    "CorrectnessResult",
    "MeasurementProtocol",
    "ProvenanceError",
    "ResultError",
    "WorkloadStatus",
    "load_registry",
    "load_workload",
    "not_supported",
    "registry_digest",
    "require_commit",
    "summarize_samples",
]
