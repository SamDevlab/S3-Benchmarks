from __future__ import annotations

import json

import pytest

from tools.artifacts import ArtifactError, RunIdentity, file_record, load_manifest
from benchmarks.jsmn.harness import correctness


def _artifact(run: RunIdentity, fixture: str = "tiny_04_arr"):
    path = run.path("fixtures", fixture, "s3-o1")
    path.mkdir(parents=True, exist_ok=True)
    return path / "program.s"


def test_distinct_runs_never_resolve_to_the_same_writable_path(tmp_path):
    first = RunIdentity.create(tmp_path / "artifacts", "run-a")
    second = RunIdentity.create(tmp_path / "artifacts", "run-b")

    assert _artifact(first) != _artifact(second)
    assert _artifact(first).parent != _artifact(second).parent


def test_baseline_and_candidate_runs_cannot_share_native_outputs(tmp_path):
    baseline = RunIdentity.create(tmp_path / "artifacts", "baseline")
    candidate = RunIdentity.create(tmp_path / "artifacts", "candidate")

    baseline_path = _artifact(baseline)
    candidate_path = _artifact(candidate)
    baseline_path.write_text("baseline", encoding="utf-8")
    candidate_path.write_text("candidate", encoding="utf-8")

    assert baseline_path != candidate_path
    assert baseline_path.read_text(encoding="utf-8") == "baseline"
    assert candidate_path.read_text(encoding="utf-8") == "candidate"


def test_manifest_loader_cannot_fall_back_to_another_run(tmp_path):
    first = RunIdentity.create(tmp_path / "artifacts", "run-a")
    second = RunIdentity.create(tmp_path / "artifacts", "run-b")
    first.write_json_once("artifact-manifest.json", {"run_id": "run-a", "artifacts": []})

    with pytest.raises(ArtifactError, match="missing current-run artifact"):
        load_manifest(second)


def test_completed_artifact_is_not_overwritten(tmp_path):
    run = RunIdentity.create(tmp_path / "artifacts", "run-a")
    run.write_json_once("artifact-manifest.json", {"run_id": "run-a", "value": 1})

    with pytest.raises(ArtifactError, match="refusing to overwrite"):
        run.write_json_once("artifact-manifest.json", {"run_id": "run-a", "value": 2})

    assert json.loads(run.require_file("artifact-manifest.json").read_text()) ["value"] == 1


def test_missing_current_run_artifact_fails_closed(tmp_path):
    run = RunIdentity.create(tmp_path / "artifacts", "run-a")

    with pytest.raises(ArtifactError, match="missing current-run artifact"):
        run.require_file("fixtures/tiny_04_arr/s3-o1/program")


def test_manifest_records_hash_and_run_provenance(tmp_path):
    run = RunIdentity.create(tmp_path / "artifacts", "run-a")
    path = _artifact(run)
    path.write_bytes(b"stable-assembly")
    record = {
        "run_id": run.run_id,
        "fixture_id": "tiny_04_arr",
        "assembly": file_record(run, path),
    }
    run.write_json_once(
        "artifact-manifest.json",
        {
            "run_id": run.run_id,
            "provenance": {"s3_commit": "a" * 40, "benchmark_commit": "b" * 40},
            "artifacts": [record],
        },
    )

    manifest = load_manifest(run)
    assert manifest["provenance"]["s3_commit"] == "a" * 40
    assert manifest["artifacts"][0]["assembly"]["sha256"]
    assert manifest["artifacts"][0]["assembly"]["bytes"] == len(b"stable-assembly")


def test_same_synthetic_input_has_stable_digest_accounting(tmp_path):
    first = RunIdentity.create(tmp_path / "artifacts", "run-a")
    second = RunIdentity.create(tmp_path / "artifacts", "run-b")
    first_path = _artifact(first)
    second_path = _artifact(second)
    first_path.write_bytes(b"identical")
    second_path.write_bytes(b"identical")

    assert file_record(first, first_path)["sha256"] == file_record(second, second_path)["sha256"]


def test_missing_captured_memory_is_structured_and_never_passes(monkeypatch):
    frame = {
        11: [0] * 32,
        12: [0] * 32,
        13: [None] + [0] * 31,
        14: [0] * 32,
        15: [0] * 32,
    }
    monkeypatch.setattr(correctness, "run_source_with_buffer_capture", lambda *args, **kwargs: (1, [frame]))
    monkeypatch.setattr(correctness, "_diagnostic_assembly_sha256", lambda *args: "assembly-digest")

    with pytest.raises(correctness.CapturedMemoryError) as raised:
        correctness.run_s3_jsmn(
            "unused template",
            "{}",
            "O1",
            diagnostic_context={
                "s3_sha": "a" * 40,
                "run_id": "run-synthetic",
            },
        )

    assert raised.value.details == {
        "s3_sha": "a" * 40,
        "run_id": "run-synthetic",
        "fixture": "UNSPECIFIED",
        "variant": "S3-O1",
        "token_index": 0,
        "memory_index": 13,
        "field": "end",
        "assembly_sha256": "assembly-digest",
    }
