from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

from tools.s3_17_native_lowering_lab import (
    DATASET_PATH,
    FIXTURE_PATH,
    MANIFEST_PATH,
    CONTROL_ADAPTER_PATH,
    _build_command,
    _text_artifact_sha256,
    load_contract,
)


def test_manifest_pins_sources_and_external_reference_fixture() -> None:
    manifest, fixture, dataset = load_contract(require_candidate_sha=False)
    assert manifest["experiment_id"] == "EXP-S3-17-LOWERING-002"
    assert manifest["s3_control_sha"] == "4ddc7a64a4c395460181db0e8957f085d8bb12a9"
    assert len(manifest["workloads"]) == 3
    assert len(fixture["workloads"]) == 3
    assert _text_artifact_sha256(FIXTURE_PATH.read_bytes()) == manifest["reference_fixture"]["sha256"]
    assert _text_artifact_sha256(DATASET_PATH.read_bytes()) == manifest["dataset_manifest"]["sha256"]
    assert manifest["reference_fixture"]["upstream_revision"] == manifest["s3_control_sha"]
    assert manifest["protocol"]["max_instructions"] == 1_000_000_000
    assert manifest["protocol"]["optimization"] == "O1"
    assert manifest["protocol"]["source_syntax"] == "0.6"
    assert manifest["budget_provenance"]["source_sha256"] == "f1ba247af3e38b9bcc2559c6f298b0116ad345b2f55842758c87b09f119ab06e"
    assert dataset["energy"]["dc_capacity_w"] == 5000.0


def test_public_build_command_runs_s3_cli_as_a_subprocess() -> None:
    command = _build_command(
        Path("/opt/s3-candidate"),
        Path("/opt/s3-candidate/workload.s3"),
        Path("/tmp/workload.so"),
        Path("/tmp/workload.s"),
        optimization="O1",
        source_syntax="0.6",
        max_instructions=1_000_000_000,
    )
    assert command[1:4] == ["-m", "bootstrap.s3.cli", "ffi-build"]
    assert command[command.index("--native-policy") + 1] == "baseline"
    assert command[command.index("-O") + 1] == "1"
    assert command[command.index("--source-syntax") + 1] == "0.6"
    assert command[command.index("--max-instructions") + 1] == "1000000000"
    assert "-o" in command and "--keep-assembly" in command


def test_control_budget_adapter_is_pinned_and_limited_to_cli_facade() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    adapter = manifest["control_build_adapter"]
    patch = CONTROL_ADAPTER_PATH.read_text(encoding="utf-8")
    assert hashlib.sha256(patch.encode()).hexdigest() == adapter["sha256"]
    paths = [
        line.removeprefix("diff --git a/").split(" b/", 1)[1]
        for line in patch.splitlines()
        if line.startswith("diff --git a/")
    ]
    assert paths == ["bootstrap/s3/cli.py", "bootstrap/s3/ffi.py"]
    assert adapter["files"] == paths
    assert "optimization=optimization" in patch
    assert "mode=mode" in patch


def test_lab_runner_does_not_import_private_s3_modules() -> None:
    source = Path(__file__).parents[1] / "tools" / "s3_17_native_lowering_lab.py"
    tree = ast.parse(source.read_text(encoding="utf-8"))
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    assert not any(name == "bootstrap.s3" or name.startswith("bootstrap.s3.") for name in imported)
    assert "bootstrap.s3.cli" in source.read_text(encoding="utf-8")


def test_reference_fixture_contains_external_engines_and_expected_hashes() -> None:
    manifest, fixture, _ = load_contract(require_candidate_sha=False)
    by_id = {record["workload_id"]: record for record in fixture["workloads"]}
    assert set(by_id) == {item["workload_id"] for item in manifest["workloads"]}
    assert {record["reference_engine"] for record in fixture["workloads"]} == {"Open3D", "Rasterio", "pvlib"}
    for record in fixture["workloads"]:
        encoded = (json.dumps(record["expected_output"], sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
        assert hashlib.sha256(encoded).hexdigest() == record["output_sha256"]


def test_candidate_sha_is_required_before_running_measurements(tmp_path: Path) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    manifest["s3_candidate_sha"] = None
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    try:
        load_contract(manifest_path=manifest_path, require_candidate_sha=True)
    except ValueError as exc:
        assert "exact S3 candidate commit SHA" in str(exc)
    else:
        raise AssertionError("un-pinned S3 candidate was accepted")


def test_pinned_text_artifact_hash_ignores_checkout_line_endings() -> None:
    lf = b"first\nsecond\n"
    crlf = lf.replace(b"\n", b"\r\n")
    assert _text_artifact_sha256(lf) == _text_artifact_sha256(crlf)
