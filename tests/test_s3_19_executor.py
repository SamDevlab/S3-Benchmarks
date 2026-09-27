from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import pytest

import tools.s3_19_executor as executor
from tools.s3_19_executor import (
    BINARY_VARIANTS,
    COMPILER_SOURCE_FILES,
    TIMING_VARIANTS,
    WORKLOADS,
    _checkout_source,
    _native_artifact_inventory,
    _safe_source_identity,
    _validate_benchmark_result,
)


def _git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, text=True
    ).stdout.strip()


def _local_source_repo(root: Path) -> tuple[Path, str, str]:
    repository = root / "source"
    repository.mkdir()
    _git(repository, "init", "-q", "-b", "main")
    _git(repository, "config", "user.name", "S3 executor test")
    _git(repository, "config", "user.email", "executor-test@example.invalid")
    (repository / "payload.txt").write_text("pinned\n", encoding="utf-8")
    script = repository / "tools/s3_15_native_workload_benchmark.py"
    script.parent.mkdir(parents=True)
    script.write_text("raise SystemExit(0)\n", encoding="utf-8")
    _git(repository, "add", "payload.txt", "tools/s3_15_native_workload_benchmark.py")
    _git(repository, "commit", "-q", "-m", "source checkpoint")
    return repository, _git(repository, "rev-parse", "HEAD"), _git(repository, "rev-parse", "HEAD^{tree}")


def test_executor_clones_exact_revision_without_mutating_source(tmp_path: Path) -> None:
    repository, revision, tree = _local_source_repo(tmp_path)
    source_status_before = _git(repository, "status", "--porcelain")

    checkout, actual_tree = _checkout_source(str(repository), revision, tmp_path / "run")

    assert _git(checkout, "rev-parse", "HEAD") == revision
    assert actual_tree == tree
    assert _git(checkout, "status", "--porcelain") == ""
    assert _git(repository, "status", "--porcelain") == source_status_before


def test_source_identity_redacts_credentials_and_rejects_tokenized_urls() -> None:
    assert _safe_source_identity("https://github.com/SamDevlab/S3.git") == "https://github.com/SamDevlab/S3.git"
    with pytest.raises(ValueError, match="must not embed credentials"):
        _safe_source_identity("https://user:secret@github.com/SamDevlab/S3.git")
    with pytest.raises(ValueError, match="must not embed credentials"):
        _safe_source_identity("https://github.com/SamDevlab/S3.git?token=secret")


def test_native_artifact_inventory_hashes_assemblies_and_binaries(tmp_path: Path) -> None:
    for index in range(15):
        (tmp_path / f"module-{index}.s").write_bytes(f"assembly {index}".encode())
    for index in range(16):
        (tmp_path / f"module-{index}.so").write_bytes(f"binary {index}".encode())

    inventory = _native_artifact_inventory(tmp_path)

    assert len(inventory) == 31
    assert sum(item["kind"] == "assembly" for item in inventory) == 15
    assert sum(item["kind"] == "shared_object" for item in inventory) == 16
    assert all(len(item["sha256"]) == 64 for item in inventory)


def _valid_result(tmp_path: Path) -> tuple[dict, Path, str, str]:
    checkout = tmp_path / "pinned"
    checkout.mkdir()
    source_hashes = {}
    for relative in COMPILER_SOURCE_FILES:
        path = checkout / Path(*relative.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(relative, encoding="utf-8")
        source_hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    revision = "a" * 40
    tree = "b" * 40
    result = {
        "source_revision": {
            "git_commit": revision,
            "git_tree": tree,
            "worktree_clean": True,
            "identity_source": "explicit_source_checkout_provenance",
        },
        "compiler_source_sha256": source_hashes,
        "protocol": {
            "default_instruction_budget_mode": "per-instruction",
            "c_flags": ["-O1", "-fno-fast-math", "-ffp-contract=off", "-fno-tree-vectorize"],
        },
        "workloads": {},
    }
    for workload_id in WORKLOADS:
        result["workloads"][workload_id] = {
            "correctness": "PASS_ALL_BUILDS",
            "timings": {
                name: {
                    "sample_count": 3,
                    "median_ns_per_call": 100.0,
                    "minimum_ns_per_call": 90.0,
                    "maximum_ns_per_call": 110.0,
                }
                for name in TIMING_VARIANTS
            },
            "timing_protocol": {
                "iterations_per_sample": 10,
                "warmups": 1,
                "samples": 3,
            },
            "native_candidate_output_sha256": {name: "c" * 64 for name in TIMING_VARIANTS},
            "binary_metrics": {
                name: {
                    "text_section_bytes": 100,
                    "exported_function_bytes": 80,
                    "static_machine_instructions": 20,
                }
                for name in BINARY_VARIANTS
            },
            "per_over_exact_segment_ratio": 1.1,
            "per_over_loop_hybrid_ratio": 1.05,
            "compact_ea_applied": False,
        }
    return result, checkout, revision, tree


def test_executor_validates_source_hashes_and_correctness_before_accepting_result(tmp_path: Path) -> None:
    result, checkout, revision, tree = _valid_result(tmp_path)

    verified = _validate_benchmark_result(
        result,
        checkout=checkout,
        revision=revision,
        tree=tree,
        iterations=10,
        warmups=1,
        samples=3,
    )

    assert set(verified["verified_compiler_source_sha256"]) == set(COMPILER_SOURCE_FILES)
    assert set(verified["workloads"]) == set(WORKLOADS)

    legacy_identity_result = json.loads(json.dumps(result))
    legacy_identity_result["source_revision"]["identity_source"] = "local_git_checkout"
    _validate_benchmark_result(
        legacy_identity_result,
        checkout=checkout,
        revision=revision,
        tree=tree,
        iterations=10,
        warmups=1,
        samples=3,
    )


def test_executor_fails_closed_on_identity_source_hash_or_correctness_mismatch(tmp_path: Path) -> None:
    result, checkout, revision, tree = _valid_result(tmp_path)
    arguments = {
        "checkout": checkout,
        "revision": revision,
        "tree": tree,
        "iterations": 10,
        "warmups": 1,
        "samples": 3,
    }

    bad_identity = json.loads(json.dumps(result))
    bad_identity["source_revision"]["git_tree"] = "d" * 40
    with pytest.raises(ValueError, match="source identity"):
        _validate_benchmark_result(bad_identity, **arguments)

    unknown_identity_source = json.loads(json.dumps(result))
    unknown_identity_source["source_revision"]["identity_source"] = "unverified_external_claim"
    with pytest.raises(ValueError, match="source identity"):
        _validate_benchmark_result(unknown_identity_source, **arguments)

    bad_hash = json.loads(json.dumps(result))
    bad_hash["compiler_source_sha256"][COMPILER_SOURCE_FILES[0]] = "e" * 64
    with pytest.raises(ValueError, match="source hash mismatch"):
        _validate_benchmark_result(bad_hash, **arguments)

    bad_correctness = json.loads(json.dumps(result))
    bad_correctness["workloads"][WORKLOADS[0]]["correctness"] = "FAIL"
    with pytest.raises(ValueError, match="correctness did not pass"):
        _validate_benchmark_result(bad_correctness, **arguments)


def test_multi_sha_executor_runs_exact_revisions_in_deterministic_isolated_paths(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    revisions = ["b" * 40, "a" * 40]
    calls: list[tuple[str, Path, Path]] = []

    def fake_execute(**kwargs: object) -> dict[str, object]:
        revision = str(kwargs["revision"])
        calls.append((revision, kwargs["work_root"], kwargs["output_dir"]))
        return {"status": "PASS", "s3_commit": revision}

    monkeypatch.setattr(executor, "execute", fake_execute)
    output = tmp_path / "matrix-output"
    work = tmp_path / "matrix-work"

    report = executor.execute_matrix(
        source_url="https://github.com/SamDevlab/S3.git",
        revisions=revisions,
        work_root=work,
        output_dir=output,
    )

    assert report["status"] == "PASS"
    assert report["revision_order"] == ["a" * 40, "b" * 40]
    assert report["execution_order"] == "serial_ascending_sha"
    assert [call[0] for call in calls] == ["a" * 40, "b" * 40]
    assert calls[0][1] == work / ("a" * 40)
    assert calls[0][2] == output / ("a" * 40)
    assert json.loads((output / "multi-sha-result-v1.json").read_text())["status"] == "PASS"


@pytest.mark.parametrize(
    "revisions, message",
    [
        (["a" * 40, "a" * 40], "contains duplicates"),
        (["not-a-full-sha"], "full lowercase 40-character Git SHA"),
    ],
)
def test_multi_sha_executor_rejects_ambiguous_revision_sets_before_side_effects(
    tmp_path: Path, revisions: list[str], message: str
) -> None:
    output = tmp_path / "matrix-output"
    work = tmp_path / "matrix-work"

    with pytest.raises(ValueError, match=message):
        executor.execute_matrix(
            source_url="https://github.com/SamDevlab/S3.git",
            revisions=revisions,
            work_root=work,
            output_dir=output,
        )

    assert not output.exists()
    assert not work.exists()


def test_multi_sha_executor_records_one_failure_and_continues_to_next_revision(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    revisions = ["a" * 40, "b" * 40]
    calls: list[str] = []

    def fake_execute(**kwargs: object) -> dict[str, object]:
        revision = str(kwargs["revision"])
        calls.append(revision)
        if revision == "a" * 40:
            raise RuntimeError("incompatible benchmark protocol")
        return {"status": "PASS", "s3_commit": revision}

    monkeypatch.setattr(executor, "execute", fake_execute)
    report = executor.execute_matrix(
        source_url="https://github.com/SamDevlab/S3.git",
        revisions=revisions,
        work_root=tmp_path / "matrix-work",
        output_dir=tmp_path / "matrix-output",
    )

    assert calls == revisions
    assert report["status"] == "FAIL"
    assert [row["status"] for row in report["runs"]] == ["FAIL", "PASS"]
    assert "incompatible benchmark protocol" in report["runs"][0]["error"]
