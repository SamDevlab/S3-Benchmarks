from __future__ import annotations

import json
from pathlib import Path

from tools.classify_bootstrap_host import classify

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "laboratory" / "bootstrap-v1" / "performance-host-contract.json"


def _contract() -> dict:
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def _base() -> dict:
    return {
        "os": "linux",
        "arch": "x86_64",
        "cpu_count": 8,
        "load1": 0.10,
        "control_drift_percent": None,
        "native_toolchain_ready": True,
        "source_worktree_clean": True,
        "benchmark_worktree_clean": True,
        "competing_compiler_or_test_processes": 0,
        "virtualized": True,
        "thermal_throttled": False,
    }


def test_current_vm_shape_is_correctness_only_until_drift_is_measured() -> None:
    result = classify(_base(), _contract())
    assert result["classification"] == "CORRECTNESS_ONLY"
    assert result["correctness_eligible"] is True
    assert result["characterization_eligible"] is False
    assert result["comparative_performance_eligible"] is False


def test_vm_can_characterize_but_not_certify_comparative_performance() -> None:
    observations = _base()
    observations["control_drift_percent"] = 1.0
    result = classify(observations, _contract())
    assert result["classification"] == "CHARACTERIZATION_ONLY"
    assert result["correctness_eligible"] is True
    assert result["characterization_eligible"] is True
    assert result["comparative_performance_eligible"] is False


def test_dedicated_stable_linux_host_can_be_comparative_eligible() -> None:
    observations = _base()
    observations.update(
        {
            "virtualized": False,
            "control_drift_percent": 1.0,
            "load1": 0.5,
        }
    )
    result = classify(observations, _contract())
    assert result["classification"] == "NATIVE_COMPARATIVE_ELIGIBLE"
    assert result["comparative_performance_eligible"] is True


def test_high_control_drift_never_becomes_performance_evidence() -> None:
    observations = _base()
    observations["control_drift_percent"] = 13.10
    result = classify(observations, _contract())
    assert result["classification"] == "CORRECTNESS_ONLY"
    assert result["correctness_eligible"] is True
    assert result["characterization_eligible"] is False


def test_dirty_checkout_blocks_even_correctness_host_eligibility() -> None:
    observations = _base()
    observations["source_worktree_clean"] = False
    result = classify(observations, _contract())
    assert result["classification"] == "HOST_NOT_ELIGIBLE"
    assert result["correctness_eligible"] is False
