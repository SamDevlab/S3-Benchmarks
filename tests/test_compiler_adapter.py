from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from tools.compiler_adapter import CompilerAdapterError, resolve_artifact


def test_stage_artifact_requires_path_and_sha() -> None:
    with pytest.raises(CompilerAdapterError, match="artifact is required"):
        resolve_artifact("stage2", None, "0" * 64)


def test_stage_artifact_sha_mismatch_fails_closed(tmp_path: Path) -> None:
    artifact = tmp_path / "stage2"
    artifact.write_bytes(b"real artifact")
    wrong = hashlib.sha256(b"different").hexdigest()
    with pytest.raises(CompilerAdapterError, match="SHA-256 mismatch"):
        resolve_artifact("stage2", artifact, wrong)


def test_stage_artifact_validates_exact_bytes(tmp_path: Path) -> None:
    artifact = tmp_path / "stage3"
    artifact.write_bytes(b"real artifact")
    expected = hashlib.sha256(artifact.read_bytes()).hexdigest()
    resolved = resolve_artifact("stage3", artifact, expected)
    assert resolved.kind == "stage3"
    assert resolved.sha256 == expected


def test_stage_artifact_does_not_fallback_for_missing_file(tmp_path: Path) -> None:
    with pytest.raises(CompilerAdapterError, match="missing or empty"):
        resolve_artifact("stage3", tmp_path / "missing", "0" * 64)
