from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from tools.s3_112_candidate_matrix import (
    _disjoint_new_paths,
    _paired_summary,
    _write_once,
    sample_order,
    validate_spec,
)


def _variant(variant_id: str, revision: str, *, policy: str = "baseline") -> dict[str, str]:
    return {
        "id": variant_id,
        "revision": revision,
        "optimization": "O1",
        "native_policy": policy,
        "instruction_budget_mode": "per-instruction",
    }


def _spec() -> dict[str, object]:
    base = "a" * 40
    candidate = "b" * 40
    return {
        "schema_version": "s3.candidate-matrix.v1",
        "experiment_id": "EXP-S3-112-ABLATION-001",
        "source_url": "https://github.com/SamDevlab/S3.git",
        "control": _variant("BASE", base),
        "candidates": [
            _variant("A", candidate),
            _variant("B", candidate, policy="compact-ea"),
            _variant("A+B", candidate),
        ],
        "workloads": ["engineering.point-cloud-summary.v1"],
        "protocol": {
            "iterations_per_sample": 50,
            "warmups": 2,
            "samples": 7,
            "bootstrap_resamples": 100,
            "seed": 42,
        },
    }


def test_candidate_matrix_validates_explicit_base_ablation_and_combined_variants() -> None:
    spec = validate_spec(_spec())

    assert [row["id"] for row in [spec["control"], *spec["candidates"]]] == [
        "BASE",
        "A",
        "B",
        "A+B",
    ]
    assert spec["source_identity"] == "https://github.com/SamDevlab/S3.git"
    assert spec["protocol"]["samples"] == 7


@pytest.mark.parametrize(
    "mutate, message",
    [
        (lambda spec: spec["candidates"].append(spec["candidates"][0]), "variant IDs must be unique"),
        (lambda spec: spec["candidates"][0].update(revision="A" * 40), "full lowercase Git SHA"),
        (lambda spec: spec.update(workloads=["unknown.workload.v1"]), "unsupported identity"),
        (lambda spec: spec["protocol"].update(samples=2), "samples must be an integer"),
        (lambda spec: spec.update(source_url="https://user:secret@example.invalid/repo"), "must not embed credentials"),
    ],
)
def test_candidate_matrix_rejects_ambiguous_or_unsafe_specs(mutate, message: str) -> None:
    spec = _spec()
    mutate(spec)

    with pytest.raises(ValueError, match=message):
        validate_spec(spec)


def test_sample_order_rotates_and_reverses_without_dropping_variants() -> None:
    labels = ["BASE", "A", "B", "A+B"]

    orders = [sample_order(labels, index) for index in range(8)]

    assert orders[0] == labels
    assert orders[1] == ["BASE", "A+B", "B", "A"]
    assert all(set(order) == set(labels) and len(order) == len(labels) for order in orders)
    assert orders == [sample_order(labels, index) for index in range(8)]


def test_paired_summary_classifies_large_separated_effect() -> None:
    result = _paired_summary(
        [110.0] * 7,
        [100.0] * 7,
        seed=17,
        resamples=100,
    )

    assert result["baseline_over_candidate_median_ratio"] == 1.1
    assert result["classification"] == "MATERIAL_IMPROVEMENT"


def test_matrix_paths_must_be_new_and_disjoint(tmp_path) -> None:
    work = tmp_path / "work"
    output = tmp_path / "evidence"

    resolved_work, resolved_output = _disjoint_new_paths(work, output)

    assert resolved_work == work.resolve()
    assert resolved_output == output.resolve()
    with pytest.raises(ValueError, match="must be disjoint"):
        _disjoint_new_paths(work, work / "nested")
    work.mkdir()
    with pytest.raises(FileExistsError, match="must be new"):
        _disjoint_new_paths(work, output)


def test_evidence_writer_refuses_to_overwrite_existing_file(tmp_path) -> None:
    path = tmp_path / "result.json"
    _write_once(path, b"first\n")

    with pytest.raises(FileExistsError):
        _write_once(path, b"replacement\n")

    assert path.read_bytes() == b"first\n"


def test_documented_script_entrypoint_loads_project_tools_package() -> None:
    script = Path(__file__).resolve().parents[1] / "tools" / "s3_112_candidate_matrix.py"
    result = subprocess.run(
        [sys.executable, script, "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "explicit matrix" in result.stdout
