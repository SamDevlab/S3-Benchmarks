"""Fail-closed immutable provenance checks."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
import subprocess


SHA_RE = re.compile(r"^[0-9a-f]{40}$")


class ProvenanceError(RuntimeError):
    pass


def git_head(repo: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise ProvenanceError(f"cannot resolve Git HEAD for {repo}") from error
    value = result.stdout.strip()
    if not SHA_RE.fullmatch(value):
        raise ProvenanceError(f"non-immutable Git identity for {repo}: {value!r}")
    return value


def require_commit(repo: Path, expected: str, *, label: str) -> str:
    if not SHA_RE.fullmatch(expected):
        raise ProvenanceError(f"{label} must be a full commit SHA")
    actual = git_head(repo)
    if actual != expected:
        raise ProvenanceError(f"{label} mismatch: expected {expected}, got {actual}")
    return actual


def sha256_file(path: Path) -> str:
    if not path.is_file():
        raise ProvenanceError(f"missing file for digest: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
