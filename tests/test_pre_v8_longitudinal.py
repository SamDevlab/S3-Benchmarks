"""Contract tests only; the inline fixture values are not benchmark results."""

from __future__ import annotations

import json

import pytest

from tools.pre_v8_longitudinal import (
    ROOT,
    ValidationError,
    _check_plan,
    compare_records,
    validate_record,
)


def _record(language: str, *, revision: str | None = None, samples: list[int] | None = None):
    is_s3 = language == "S3"
    return {
        "schema_version": "s3.pre-v8-longitudinal-result.v1",
        "run_id": f"contract-test-{language}",
        "campaign_group": "PURE PERFORMANCE",
        "benchmark_repo_revision": "c" * 40,
        "compiler": {
            "language": language,
            "name": "S3 compiler" if is_s3 else f"{language} test compiler",
            "version": "test-only",
            "repository": "https://github.com/SamDevlab/S3.git" if is_s3 else None,
            "source_revision": revision if is_s3 else None,
            "working_tree_clean": True if is_s3 else None,
            "executable_sha256": "1" * 64,
        },
        "implementation": {
            "repository": "https://example.invalid/test-only",
            "revision": "d" * 40,
            "source_sha256": "2" * 64,
            "build_recipe_sha256": "3" * 64,
        },
        "workload": {
            "id": "test.workload.v1",
            "fixture_id": "contract-only-fixture",
            "dataset_sha256": "4" * 64,
            "work_units": 10,
        },
        "environment": {
            "os": "contract-test-only",
            "architecture": "contract-test-only",
            "fingerprint_sha256": "5" * 64,
        },
        "protocol": {
            "id": "contract-only-protocol",
            "sha256": "6" * 64,
            "warmups": 0,
            "samples": 3,
            "iterations_per_sample": 2,
            "ordering": "interleaved",
        },
        "stages": {
            "correctness": {"status": "PASS", "oracle": "test-only", "output_sha256": "7" * 64},
            "compilation": {"status": "PASS", "elapsed_ns": 100, "exit_code": 0},
            "execution": {
                "status": "PASS",
                "scope": "process_e2e",
                "samples_ns": samples if samples is not None else [1000, 1010, 990],
            },
            "binary_size": {"status": "PASS", "bytes": 512, "format": "PE"},
        },
    }


def test_preparation_plan_has_no_implemented_profiles_or_v7_pin():
    result = _check_plan()
    assert result["indexed_experiments"] >= 10


def test_s3_record_requires_a_clean_full_commit_pin():
    record = _record("S3", revision="not-a-full-sha")
    with pytest.raises(ValidationError, match="source_revision"):
        validate_record(record)


def test_failed_correctness_cannot_be_followed_by_passing_execution():
    record = _record("C")
    record["stages"]["correctness"] = {"status": "FAIL", "oracle": None, "output_sha256": None}
    with pytest.raises(ValidationError, match="only after correctness"):
        validate_record(record)


def test_comparison_keeps_build_execution_and_size_separate():
    records = [_record("C"), _record("Rust", samples=[800, 790, 810])]
    matrix = compare_records(records, "language")
    assert matrix["classification"] == "DESCRIPTIVE_ONLY_NO_SPEEDUP_CLAIM"
    assert matrix["rows"][0]["compilation"]["elapsed_ns"] == 100
    assert matrix["rows"][0]["binary_size"]["bytes"] == 512
    assert matrix["rows"][0]["execution"]["median_ns_per_work_unit"] == 50
    assert matrix["rows"][1]["execution"]["median_ns_per_work_unit"] == 40


def test_longitudinal_mode_rejects_changed_workload_source():
    baseline = _record("S3", revision="a" * 40)
    candidate = _record("S3", revision="b" * 40)
    candidate["implementation"]["source_sha256"] = "8" * 64
    with pytest.raises(ValidationError, match="identical workload source"):
        compare_records([baseline, candidate], "revision")


def test_mainline_evidence_index_sources_are_pinned():
    index_path = ROOT / "reports" / "pre-v8-historical-evidence-index-v1.json"
    index = json.loads(index_path.read_text(encoding="utf-8"))
    assert all(len(row["source_revision"]) == 40 for row in index["experiments"])
    assert all(
        len(source["blob_sha"]) == 40
        for row in index["experiments"]
        for source in row["sources"]
    )
