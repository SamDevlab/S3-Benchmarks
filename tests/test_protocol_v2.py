from __future__ import annotations

import json
from pathlib import Path

import pytest

from protocol.correctness import exact, not_supported
from protocol.measurement import MeasurementProtocol, interleave, summarize_samples
from protocol.provenance import ProvenanceError, require_commit
from protocol.registry import load_registry, registry_digest
from protocol.result import BenchmarkResult
from protocol.workload import WorkloadStatus, canonical_json, load_workload


ROOT = Path(__file__).resolve().parents[1]


def test_registry_is_deterministic_and_contains_rmsd_and_candidate_families():
    registry = load_registry(ROOT)
    assert registry_digest(registry) == registry_digest(json.loads(canonical_json(registry)))
    ids = [workload["id"] for workload in registry["workloads"]]
    assert ids == sorted(ids)
    assert "scientific.rmsd.single" in ids
    assert "memory.babelstream.initial" in ids
    assert "compiler.tsvc.initial" in ids


def test_rmsd_manifest_is_correctness_pass_and_not_supported_workloads_are_explicit():
    rmsd = load_workload(ROOT / "benchmarks/scientific/rmsd/manifest.json")
    batch = load_workload(ROOT / "benchmarks/scientific/rmsd/batch-manifest.json")
    assert rmsd.status is WorkloadStatus.CORRECTNESS_PASS
    assert batch.status is WorkloadStatus.NOT_SUPPORTED_YET
    assert batch.correctness_contract["first_missing_capability"]


def test_generic_statistics_preserve_raw_samples_and_derived_work_units():
    result = summarize_samples([10, 12, 14, 16], work_units=2)
    assert result["raw_samples"] == [10, 12, 14, 16]
    assert result["n"] == 4
    assert result["mad"] == 2.0
    assert result["ns_per_work_unit"] == 6.5
    assert result["cv"] > 0


def test_interleaving_is_deterministic_and_alternates_direction():
    assert interleave(["A", "B"], 3) == ["A", "B", "B", "A", "A", "B"]


def test_measurement_protocol_rejects_synthetic_timing():
    with pytest.raises(ValueError, match="synthetic timing"):
        MeasurementProtocol(synthetic_timing=True)


def test_correctness_and_not_supported_contracts_are_explicit():
    assert exact(14.0, 14.0).status == "PASS"
    result = not_supported(capability="arrays", evidence="missing", minimum_required_capability="arrays")
    assert result.status == "NOT_SUPPORTED_YET"
    assert result.first_missing_capability == "arrays"


def test_provenance_fails_closed_for_wrong_sha(tmp_path):
    import subprocess

    subprocess.run(["git", "init", str(tmp_path)], check=True, capture_output=True)
    with pytest.raises(ProvenanceError):
        require_commit(tmp_path, "0" * 40, label="test")


def test_result_v2_preserves_raw_samples_and_declares_unavailable_metrics():
    result = BenchmarkResult(
        run_id="run-test",
        benchmark_repo_sha="a" * 40,
        s3_sha="b" * 40,
        upstream_shas={"example": "c" * 40},
        environment={"os": "test"},
        workload={"id": "scientific.rmsd.single", "family": "scientific", "work_unit": "coordinate"},
        variant={"id": "python-oracle", "role": "CORRECTNESS_ORACLE"},
        correctness={"status": "PASS"},
        build={},
        measurement_protocol=MeasurementProtocol(repetitions=2),
        samples=(10.0, 12.0),
        work_units=2,
        artifact_metrics={"binary_size": "NOT_AVAILABLE"},
        hardware_metrics={"peak_rss": "NOT_AVAILABLE"},
    ).to_dict()
    assert result["schema"] == "s3.benchmark.result.v2"
    assert result["samples"] == [10.0, 12.0]
    assert result["statistics"]["n"] == 2
    assert result["derived_metrics"]["energy"] == "NOT_MEASURED"
