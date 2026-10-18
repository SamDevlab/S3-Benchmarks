from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path

CAMPAIGN = Path(__file__).resolve().parents[1]
RESULTS = CAMPAIGN / "results"


def _jsonl(name: str) -> list[dict[str, object]]:
    return [json.loads(line) for line in (RESULTS / name).read_text(encoding="utf-8").splitlines()]


def test_evidence_index_authenticates_every_delivered_result_file() -> None:
    index = json.loads((RESULTS / "evidence-index.json").read_text(encoding="utf-8"))
    assert index["schema"] == "s3-native-pure-controlled-evidence-index/v1"
    assert set(index["files"]) == {
        "builds.jsonl", "expected-v1.json", "invalid_cases.jsonl", "raw_samples.jsonl",
        "report.md", "run-manifest.json", "runtime-fixture-v1.bin", "startup_samples.jsonl",
        "summary.json",
    }
    for name, metadata in index["files"].items():
        data = (RESULTS / name).read_bytes()
        assert len(data) == metadata["bytes"], name
        assert hashlib.sha256(data).hexdigest() == metadata["sha256"], name


def test_final_run_cardinality_and_baseline_pins() -> None:
    manifest = json.loads((RESULTS / "run-manifest.json").read_text(encoding="utf-8"))
    expected = json.loads((RESULTS / "expected-v1.json").read_text(encoding="utf-8"))
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    campaign_manifest = json.loads((CAMPAIGN / "manifest.json").read_text(encoding="utf-8"))
    workloads = {item["id"]: item["sha256"] for item in campaign_manifest["workloads"]}

    assert campaign_manifest["status"] == "complete"
    assert manifest["baseline_compiler_commit"] == "2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c"
    assert manifest["experimental_parent_commit"] == manifest["baseline_compiler_commit"]
    assert manifest["v7_dependency"] == "NONE"
    assert manifest["source_hashes"] == workloads
    assert set(expected["outputs_by_size"]) == {"small", "medium", "full"}
    assert all(set(outputs) == set(workloads) for outputs in expected["outputs_by_size"].values())
    assert summary["result"] == "COMPLETE"
    assert summary["workloads_qualified"] == 6
    assert summary["measured_cell_count"] == 4590

    builds = _jsonl("builds.jsonl")
    raw = _jsonl("raw_samples.jsonl")
    startup = _jsonl("startup_samples.jsonl")
    invalid = _jsonl("invalid_cases.jsonl")
    measured = [row for row in raw if row["phase"] == "measured"]
    configs = Counter((row["workload"], row["size"], row["language"], row["profile"], row["optimization"])
                      for row in measured)

    assert len(builds) == 56
    assert len(raw) == 5508
    assert len(startup) == 918
    assert len(invalid) == 144
    assert len(measured) == 4590
    assert len(configs) == 306
    assert set(configs.values()) == {15}
    assert all(row["result"] == "PASS" and row["short_output_status"] == 2 for row in invalid)


def test_every_final_measured_output_matches_the_pinned_oracle() -> None:
    expected = json.loads((RESULTS / "expected-v1.json").read_text(encoding="utf-8"))["outputs_by_size"]
    for row in _jsonl("raw_samples.jsonl"):
        if row["phase"] != "measured":
            continue
        wanted = expected[row["size"]][row["workload"]]
        actual = row["outputs"]
        assert len(actual) == len(wanted), (row["workload"], row["size"])
        for got, want in zip(actual, wanted):
            if isinstance(want, int):
                assert got == want, (row["workload"], row["size"], got, want)
            else:
                assert math.isclose(got, want, rel_tol=1e-10, abs_tol=1e-10), (
                    row["workload"], row["size"], got, want
                )
