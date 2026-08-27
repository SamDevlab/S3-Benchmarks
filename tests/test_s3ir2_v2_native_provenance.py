from __future__ import annotations

import hashlib
from pathlib import Path

from tools.validate_s3ir2_v2_native_provenance import validate


def _facts(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def _metadata(candidate_source: Path, binary: Path, fixture: Path, stream: Path) -> dict:
    source_sha, source_bytes = _facts(candidate_source)
    binary_sha, binary_bytes = _facts(binary)
    fixture_sha, fixture_bytes = _facts(fixture)
    stream_sha, stream_bytes = _facts(stream)
    return {
        "schema": "s3.stage1.native-semantic-evidence.v1",
        "candidate_git_sha": "a" * 40,
        "candidate_source_sha256": source_sha,
        "candidate_source_bytes": source_bytes,
        "candidate_binary_sha256": binary_sha,
        "candidate_binary_bytes": binary_bytes,
        "fixture_source_sha256": fixture_sha,
        "fixture_source_bytes": fixture_bytes,
        "stream_sha256": stream_sha,
        "stream_bytes": stream_bytes,
        "platform": {"os": "linux", "arch": "x86_64", "python": "3.14.4", "cc": "/usr/bin/cc"},
        "build": {"status": "PASS", "exit_code": 0},
        "run": {"status": "PASS", "exit_code": 0},
        "control_revision": 3,
    }


def test_native_provenance_passes_only_when_real_files_match(tmp_path: Path) -> None:
    candidate_source = tmp_path / "candidate.s3"
    binary = tmp_path / "candidate.bin"
    fixture = tmp_path / "fixture.s3"
    stream = tmp_path / "fixture.s3ir2"
    candidate_source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    binary.write_bytes(b"native-binary")
    fixture.write_text("fn main() -> i64:\n    return 2\n", encoding="utf-8")
    stream.write_text("S3IR2 2\nZ 0\n", encoding="utf-8")

    report = validate(
        _metadata(candidate_source, binary, fixture, stream),
        candidate_source=candidate_source,
        candidate_binary=binary,
        fixture_source=fixture,
        stream=stream,
    )
    assert report["status"] == "PASS"
    assert report["errors"] == []


def test_native_provenance_rejects_stream_hash_mismatch(tmp_path: Path) -> None:
    candidate_source = tmp_path / "candidate.s3"
    binary = tmp_path / "candidate.bin"
    fixture = tmp_path / "fixture.s3"
    stream = tmp_path / "fixture.s3ir2"
    candidate_source.write_text("candidate", encoding="utf-8")
    binary.write_bytes(b"binary")
    fixture.write_text("fixture", encoding="utf-8")
    stream.write_text("S3IR2 2\nZ 0\n", encoding="utf-8")
    metadata = _metadata(candidate_source, binary, fixture, stream)
    stream.write_text("S3IR2 2\nZ 31\n", encoding="utf-8")

    report = validate(
        metadata,
        candidate_source=candidate_source,
        candidate_binary=binary,
        fixture_source=fixture,
        stream=stream,
    )
    assert report["status"] == "FAIL"
    assert any("stream SHA-256 mismatch" in error for error in report["errors"])


def test_native_provenance_rejects_non_linux_x86_64(tmp_path: Path) -> None:
    candidate_source = tmp_path / "candidate.s3"
    binary = tmp_path / "candidate.bin"
    fixture = tmp_path / "fixture.s3"
    stream = tmp_path / "fixture.s3ir2"
    candidate_source.write_text("candidate", encoding="utf-8")
    binary.write_bytes(b"binary")
    fixture.write_text("fixture", encoding="utf-8")
    stream.write_text("stream", encoding="utf-8")
    metadata = _metadata(candidate_source, binary, fixture, stream)
    metadata["platform"] = {"os": "windows", "arch": "x86_64"}

    report = validate(
        metadata,
        candidate_source=candidate_source,
        candidate_binary=binary,
        fixture_source=fixture,
        stream=stream,
    )
    assert report["status"] == "FAIL"
    assert any("platform.os" in error for error in report["errors"])
