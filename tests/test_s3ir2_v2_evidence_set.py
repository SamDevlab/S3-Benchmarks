from __future__ import annotations

import json
from pathlib import Path

from tools.ingest_s3ir2_v2_evidence_set import ingest_set
from tools.render_s3ir2_v2_native_metadata import render
from tools.validate_s3ir2_v2_native_provenance import validate


STREAM = """\
S3IR2 2
F 0 1 0 4 0 1
B 0 0 0 1 0
V 0 0 3 3 0 1 0 -1
I 0 0 0 0 23 0 1 -1 -1
O 0 0 0
T 0 1 -1 -1 -1 -1 0
Z 31
"""


def _base_files(tmp_path: Path) -> tuple[Path, Path, Path, Path]:
    candidate_source = tmp_path / "candidate.s3"
    candidate_binary = tmp_path / "candidate.bin"
    source = tmp_path / "case.s3"
    conformance = tmp_path / "conformance.json"
    candidate_source.write_text("fn compiler_probe() -> i64:\n    return 0\n", encoding="utf-8")
    candidate_binary.write_bytes(b"native-stage1-candidate")
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    conformance.write_text(json.dumps({"status": "PASS", "errors": []}) + "\n", encoding="utf-8")
    return candidate_source, candidate_binary, source, conformance


def _stream(path: Path) -> Path:
    path.write_text(STREAM, encoding="utf-8")
    return path


def _native_report(
    path: Path,
    *,
    candidate_source: Path,
    candidate_binary: Path,
    fixture_source: Path,
    stream: Path,
    candidate_git_sha: str = "a" * 40,
) -> Path:
    metadata = render(
        candidate_git_sha=candidate_git_sha,
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=fixture_source,
        stream=stream,
        control_revision=3,
        python_version="3.14.4",
        cc_path="/usr/bin/cc",
        build_exit_code=0,
        run_status="PASS",
        run_exit_code=0,
    )
    report = validate(
        metadata,
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=fixture_source,
        stream=stream,
    )
    assert report["status"] == "PASS"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def test_evidence_set_requires_repeat_determinism_for_gate(tmp_path: Path) -> None:
    candidate_source, candidate_binary, source, conformance = _base_files(tmp_path)
    stream = _stream(tmp_path / "case.s3ir2")
    native = _native_report(
        tmp_path / "native.json",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=source,
        stream=stream,
    )
    manifest = ingest_set(
        source=source,
        stream=stream,
        conformance=conformance,
        repeats=[],
        native_provenance=native,
        repeat_native_provenance=[],
        output=tmp_path / "out",
    )
    assert manifest["structural_status"] == "PASS"
    assert manifest["semantic_conformance_status"] == "PASS"
    assert manifest["native_provenance_status"] == "PASS"
    assert manifest["determinism_status"] == "NOT_EVALUATED"
    assert manifest["qualification_gate"] == "BLOCKED"


def test_repeat_without_repeat_native_provenance_stays_blocked(tmp_path: Path) -> None:
    candidate_source, candidate_binary, source, conformance = _base_files(tmp_path)
    stream = _stream(tmp_path / "case.s3ir2")
    repeat = _stream(tmp_path / "repeat.s3ir2")
    native = _native_report(
        tmp_path / "native.json",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=source,
        stream=stream,
    )
    manifest = ingest_set(
        source=source,
        stream=stream,
        conformance=conformance,
        repeats=[repeat],
        native_provenance=native,
        repeat_native_provenance=[],
        output=tmp_path / "out",
    )
    assert manifest["determinism_status"] == "PASS"
    assert manifest["native_provenance_status"] == "BLOCKED"
    assert manifest["qualification_gate"] == "BLOCKED"


def test_repeat_from_different_binary_stays_blocked(tmp_path: Path) -> None:
    candidate_source, candidate_binary, source, conformance = _base_files(tmp_path)
    stream = _stream(tmp_path / "case.s3ir2")
    repeat = _stream(tmp_path / "repeat.s3ir2")
    native = _native_report(
        tmp_path / "native.json",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=source,
        stream=stream,
    )
    other_binary = tmp_path / "other.bin"
    other_binary.write_bytes(b"different-native-stage1-candidate")
    repeat_native = _native_report(
        tmp_path / "repeat-native.json",
        candidate_source=candidate_source,
        candidate_binary=other_binary,
        fixture_source=source,
        stream=repeat,
    )
    manifest = ingest_set(
        source=source,
        stream=stream,
        conformance=conformance,
        repeats=[repeat],
        native_provenance=native,
        repeat_native_provenance=[repeat_native],
        output=tmp_path / "out",
    )
    assert manifest["determinism_status"] == "PASS"
    assert manifest["native_provenance_status"] == "BLOCKED"
    assert manifest["qualification_gate"] == "BLOCKED"


def test_evidence_set_passes_lab_gate_with_all_bound_native_runs(tmp_path: Path) -> None:
    candidate_source, candidate_binary, source, conformance = _base_files(tmp_path)
    stream = _stream(tmp_path / "case.s3ir2")
    repeat2 = _stream(tmp_path / "repeat2.s3ir2")
    repeat3 = _stream(tmp_path / "repeat3.s3ir2")
    native = _native_report(
        tmp_path / "native.json",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=source,
        stream=stream,
    )
    repeat_native2 = _native_report(
        tmp_path / "repeat-native2.json",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=source,
        stream=repeat2,
    )
    repeat_native3 = _native_report(
        tmp_path / "repeat-native3.json",
        candidate_source=candidate_source,
        candidate_binary=candidate_binary,
        fixture_source=source,
        stream=repeat3,
    )
    output = tmp_path / "out"
    manifest = ingest_set(
        source=source,
        stream=stream,
        conformance=conformance,
        repeats=[repeat2, repeat3],
        native_provenance=native,
        repeat_native_provenance=[repeat_native2, repeat_native3],
        output=output,
    )
    assert manifest["structural_status"] == "PASS"
    assert manifest["semantic_conformance_status"] == "PASS"
    assert manifest["determinism_status"] == "PASS"
    assert manifest["native_provenance_status"] == "PASS"
    assert manifest["qualification_gate"] == "PASS"
    assert (output / "ingest.json").exists()
    assert (output / "native-binding.json").exists()
    assert (output / "determinism.json").exists()
    assert (output / "scorecard.json").exists()
    assert (output / "evidence-manifest.json").exists()
