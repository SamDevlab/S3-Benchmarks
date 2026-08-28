"""Classify a host for S3 bootstrap correctness and performance use.

The classifier consumes observations. It does not change CPU governors, install
packages, stop services, or mutate the benchmark/S3 repositories.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = (
    ROOT / "laboratory" / "bootstrap-v1" / "performance-host-contract.json"
)


class HostObservationError(ValueError):
    pass


def _boolean(obs: dict[str, Any], name: str) -> bool:
    value = obs.get(name)
    if not isinstance(value, bool):
        raise HostObservationError(f"{name} must be boolean")
    return value


def _optional_number(obs: dict[str, Any], name: str) -> float | None:
    value = obs.get(name)
    if value is None:
        return None
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise HostObservationError(f"{name} must be numeric or null")
    if value < 0:
        raise HostObservationError(f"{name} must be non-negative")
    return float(value)


def classify(observations: dict[str, Any], contract: dict[str, Any]) -> dict[str, Any]:
    thresholds = contract["thresholds"]
    cpu_count = observations.get("cpu_count")
    if not isinstance(cpu_count, int) or isinstance(cpu_count, bool) or cpu_count < 1:
        raise HostObservationError("cpu_count must be a positive integer")

    os_name = observations.get("os")
    arch = observations.get("arch")
    load1 = _optional_number(observations, "load1")
    drift = _optional_number(observations, "control_drift_percent")

    correctness_checks = {
        "linux": os_name == contract["required_platform"]["os"],
        "x86_64": arch == contract["required_platform"]["arch"],
        "native_toolchain_ready": _boolean(observations, "native_toolchain_ready"),
        "source_worktree_clean": _boolean(observations, "source_worktree_clean"),
        "benchmark_worktree_clean": _boolean(
            observations, "benchmark_worktree_clean"
        ),
        "no_competing_compiler_or_test_processes": observations.get(
            "competing_compiler_or_test_processes"
        )
        == 0,
    }
    correctness_eligible = all(correctness_checks.values())

    characterization_drift_ok = (
        drift is not None
        and drift
        <= float(thresholds["characterization_control_drift_percent_max"])
    )
    characterization_eligible = correctness_eligible and characterization_drift_ok

    normalized_load1 = None if load1 is None else load1 / cpu_count
    comparative_drift_ok = (
        drift is not None
        and drift <= float(thresholds["comparative_control_drift_percent_max"])
    )
    load_ok = (
        normalized_load1 is not None
        and normalized_load1
        <= float(thresholds["comparative_normalized_load1_max"])
    )
    dedicated = not _boolean(observations, "virtualized")
    thermal_ok = not _boolean(observations, "thermal_throttled")

    comparative_checks = {
        "characterization_eligible": characterization_eligible,
        "dedicated_non_virtualized_host": dedicated,
        "comparative_control_drift_ok": comparative_drift_ok,
        "normalized_load_ok": load_ok,
        "no_thermal_throttling": thermal_ok,
    }
    comparative_performance_eligible = all(comparative_checks.values())

    if comparative_performance_eligible:
        classification = "NATIVE_COMPARATIVE_ELIGIBLE"
    elif characterization_eligible:
        classification = "CHARACTERIZATION_ONLY"
    elif correctness_eligible:
        classification = "CORRECTNESS_ONLY"
    else:
        classification = "HOST_NOT_ELIGIBLE"

    return {
        "schema": "s3.bootstrap-performance-host-classification.v1",
        "classification": classification,
        "correctness_eligible": correctness_eligible,
        "characterization_eligible": characterization_eligible,
        "comparative_performance_eligible": comparative_performance_eligible,
        "correctness_checks": correctness_checks,
        "comparative_checks": comparative_checks,
        "measurements": {
            "cpu_count": cpu_count,
            "load1": load1,
            "normalized_load1": normalized_load1,
            "control_drift_percent": drift,
        },
        "policy": {
            "performance_ineligibility_is_correctness_failure": False,
            "host_mutated": False,
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    args = parser.parse_args(argv)
    observations = json.loads(args.observations.read_text(encoding="utf-8"))
    contract = json.loads(args.contract.read_text(encoding="utf-8"))
    result = classify(observations, contract)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["correctness_eligible"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
