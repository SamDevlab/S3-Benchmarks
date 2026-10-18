from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path

CAMPAIGN = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CAMPAIGN))

from fixture import FORMAT, SEED, SIZE_COUNTS, expected_outputs, fixture_values, write_fixture  # noqa: E402


def test_manifest_pins_six_real_s3_inputs_across_four_categories() -> None:
    manifest = json.loads((CAMPAIGN / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["baseline_compiler_commit"] == "2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c"
    assert len(manifest["workloads"]) == 6
    categories = {category for workload in manifest["workloads"] for category in workload["category"]}
    assert len(categories) >= 4
    for workload in manifest["workloads"]:
        path = CAMPAIGN / workload["source"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == workload["sha256"]


def test_runtime_fixture_is_deterministic_and_complete(tmp_path: Path) -> None:
    first, second = tmp_path / "first.bin", tmp_path / "second.bin"
    digest_a = write_fixture(first, SEED)
    digest_b = write_fixture(second, SEED)
    assert digest_a == digest_b == hashlib.sha256(first.read_bytes()).hexdigest()
    assert first.read_bytes() == second.read_bytes()
    assert len(first.read_bytes()) == __import__("struct").calcsize(FORMAT)
    assert fixture_values(SEED)["valid_mask"] != fixture_values(SEED + 1)["valid_mask"]


def test_oracle_returns_all_six_workload_outputs_with_valid_domains() -> None:
    outputs = expected_outputs()
    assert set(outputs) == {
        "agent_energy_residual", "agent_point_bounds", "agent_raster_threshold_count",
        "agent_raster_valid_mean", "energy_series_aggregation", "point_cloud_summary",
    }
    assert all(len(output) > 0 for output in outputs.values())
    assert 0 <= outputs["agent_raster_threshold_count"][0] <= 364
    assert len(fixture_values()["coordinates"]) == 363


def test_interpreted_reference_matches_oracle_for_all_runtime_sizes(tmp_path: Path) -> None:
    fixture_path = tmp_path / "fixture.bin"
    write_fixture(fixture_path, SEED)
    for size in SIZE_COUNTS:
        for workload, expected in expected_outputs(SEED, size).items():
            completed = subprocess.run(
                [sys.executable, str(CAMPAIGN / "python_runner.py"), workload,
                 str(fixture_path), "1", size],
                check=True, text=True, capture_output=True,
            )
            actual = json.loads(completed.stdout)["outputs"]
            assert len(actual) == len(expected)
            for got, want in zip(actual, expected):
                if isinstance(want, int):
                    assert got == want
                else:
                    assert math.isclose(got, want, rel_tol=1e-10, abs_tol=1e-10)
