"""Measurement protocol primitives independent of any benchmark family."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable

from .statistics import summarize


@dataclass(frozen=True, slots=True)
class MeasurementProtocol:
    warmups: int = 0
    repetitions: int = 1
    target_sample_duration_ns: int | None = None
    timing_scope: str = "PROCESS_E2E"
    interleaved: bool = False
    synthetic_timing: bool = False

    def __post_init__(self) -> None:
        if self.warmups < 0 or self.repetitions < 1:
            raise ValueError("warmups must be >= 0 and repetitions must be >= 1")
        if self.timing_scope not in {"COMPILE", "STARTUP", "KERNEL", "PROCESS_E2E"}:
            raise ValueError(f"unsupported timing scope: {self.timing_scope}")
        if self.synthetic_timing:
            raise ValueError("synthetic timing is forbidden")


def interleave(labels: Iterable[str], repetitions: int) -> list[str]:
    """Return a deterministic round-robin order for comparable variants."""

    names = tuple(labels)
    if not names or repetitions < 1:
        raise ValueError("labels and repetitions must be non-empty")
    return [name for repetition in range(repetitions) for name in (names if repetition % 2 == 0 else names[::-1])]


def measure_callable(
    operation: Callable[[], Any],
    *,
    warmups: int,
    repetitions: int,
    clock: Callable[[], int],
) -> tuple[list[int], list[Any]]:
    """Measure real elapsed nanoseconds; warmups are excluded from samples."""

    for _ in range(warmups):
        operation()
    samples: list[int] = []
    outputs: list[Any] = []
    for _ in range(repetitions):
        start = clock()
        outputs.append(operation())
        samples.append(clock() - start)
    return samples, outputs


def summarize_samples(samples: Iterable[float], work_units: int) -> dict[str, Any]:
    if work_units < 1:
        raise ValueError("work_units must be positive")
    values = list(samples)
    summary = summarize(values)
    summary["raw_samples"] = values
    summary["work_units"] = work_units
    summary["ns_per_work_unit"] = summary["median"] / work_units
    summary["work_units_per_sec"] = 1_000_000_000.0 * work_units / summary["median"]
    return summary
