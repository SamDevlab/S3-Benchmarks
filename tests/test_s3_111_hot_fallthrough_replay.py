from __future__ import annotations

import hashlib

import pytest

from tools.s3_111_hot_fallthrough_replay import parse_disassembly, verify_artifact


def test_independent_disassembly_parser_counts_instructions_and_branches() -> None:
    output = """
0000000000000000 <f>:
   0:\t48 89 e5 \tmov %rsp,%rbp
   3:\teb 01    \tjmp 6 <f+0x6>
   5:\tc3       \tret
"""

    assert parse_disassembly(output) == {
        "static_machine_instructions": 3,
        "static_branches": 1,
        "static_memory_references": 0,
    }


def test_artifact_verification_accepts_exact_bytes(tmp_path) -> None:
    artifact = tmp_path / "kernel.so"
    artifact.write_bytes(b"native-bytes")
    descriptor = {
        "file_name": artifact.name,
        "bytes": artifact.stat().st_size,
        "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
    }

    assert verify_artifact(artifact, descriptor)["sha256"] == descriptor["sha256"]


def test_artifact_verification_rejects_digest_mismatch(tmp_path) -> None:
    artifact = tmp_path / "kernel.so"
    artifact.write_bytes(b"native-bytes")
    descriptor = {"file_name": artifact.name, "bytes": artifact.stat().st_size, "sha256": "0" * 64}

    with pytest.raises(ValueError, match="bytes differ"):
        verify_artifact(artifact, descriptor)


def test_artifact_verification_rejects_path_name_mismatch(tmp_path) -> None:
    artifact = tmp_path / "other.so"
    artifact.write_bytes(b"native-bytes")
    descriptor = {"file_name": "kernel.so", "bytes": artifact.stat().st_size, "sha256": "0" * 64}

    with pytest.raises(ValueError, match="filename"):
        verify_artifact(artifact, descriptor)
