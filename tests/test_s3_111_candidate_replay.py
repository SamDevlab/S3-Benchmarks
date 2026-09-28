from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from tools.s3_111_candidate_replay import _verify_artifact


def test_candidate_replay_verifies_exact_native_artifact_descriptor(tmp_path: Path) -> None:
    artifact = tmp_path / "candidate.so"
    payload = b"independent native artifact"
    artifact.write_bytes(payload)

    verified = _verify_artifact(
        artifact,
        {
            "file_name": "candidate.so",
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        },
    )

    assert verified["file_name"] == artifact.name
    assert verified["bytes"] == len(payload)


def test_candidate_replay_rejects_digest_or_filename_mismatch(tmp_path: Path) -> None:
    artifact = tmp_path / "candidate.so"
    artifact.write_bytes(b"candidate")
    descriptor = {
        "file_name": "candidate.so",
        "bytes": len(b"candidate"),
        "sha256": "0" * 64,
    }

    with pytest.raises(ValueError, match="bytes do not match"):
        _verify_artifact(artifact, descriptor)

    descriptor["sha256"] = hashlib.sha256(b"candidate").hexdigest()
    descriptor["file_name"] = "../candidate.so"
    with pytest.raises(ValueError, match="filename"):
        _verify_artifact(artifact, descriptor)


def test_candidate_replay_rejects_symlink_artifacts(tmp_path: Path) -> None:
    target = tmp_path / "target.so"
    link = tmp_path / "candidate.so"
    target.write_bytes(b"candidate")
    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks are unavailable on this host")
    descriptor = {
        "file_name": "candidate.so",
        "bytes": len(b"candidate"),
        "sha256": hashlib.sha256(b"candidate").hexdigest(),
    }

    with pytest.raises(ValueError, match="regular file"):
        _verify_artifact(link, descriptor)
