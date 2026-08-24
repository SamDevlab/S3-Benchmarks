"""Explicit compiler-artifact adapter for certified benchmark runs.

The historical Python reference remains available.  Stage2 and Stage3 are
deliberately strict: an absent artifact, missing expected SHA, or mismatch is
an error and never falls back to the reference compiler.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


class CompilerAdapterError(RuntimeError):
    """Raised when a requested compiler backend cannot be proven."""


@dataclass(frozen=True, slots=True)
class CompilerArtifact:
    kind: str
    path: Path
    sha256: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_artifact(kind: str, path: Path | None, expected_sha256: str | None) -> CompilerArtifact:
    if kind not in {"stage2", "stage3"}:
        raise CompilerAdapterError(f"artifact resolution is only valid for stage2/stage3, got {kind!r}")
    if path is None:
        raise CompilerAdapterError(f"{kind} compiler artifact is required")
    path = path.resolve()
    if not path.is_file() or path.stat().st_size == 0:
        raise CompilerAdapterError(f"{kind} compiler artifact is missing or empty: {path}")
    if not expected_sha256:
        raise CompilerAdapterError(f"{kind} compiler artifact SHA-256 is required")
    actual = sha256_file(path)
    if actual != expected_sha256.lower():
        raise CompilerAdapterError(f"{kind} compiler artifact SHA-256 mismatch: expected {expected_sha256}, got {actual}")
    return CompilerArtifact(kind, path, actual)


def compile(
    compiler_kind: str,
    compiler_artifact: Path | None,
    source: Path,
    output: Path,
    *,
    optimization: str = "O0",
    cwd: Path | None = None,
    expected_sha256: str | None = None,
    timeout: float = 60.0,
) -> subprocess.CompletedProcess[str]:
    """Compile one source using an explicit backend.

    The artifact CLI contract is ``<artifact> build <source> -o <output> -O
    <level>``.  The adapter validates the bytes before invocation and does not
    search the PATH or invoke Python when an artifact backend is requested.
    """

    source = source.resolve()
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if compiler_kind == "python-reference":
        s3_repo = Path.cwd()
        command = [sys.executable, "-m", "bootstrap.s3.cli", "build", str(source), "-o", str(output), "-O", optimization]
        return subprocess.run(command, cwd=str(cwd or s3_repo), check=False, capture_output=True, text=True, timeout=timeout)
    artifact = resolve_artifact(compiler_kind, compiler_artifact, expected_sha256)
    command = [str(artifact.path), "build", str(source), "-o", str(output), "-O", optimization]
    return subprocess.run(command, cwd=str(cwd or artifact.path.parent), check=False, capture_output=True, text=True, timeout=timeout)
