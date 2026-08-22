"""Run-scoped native benchmark artifact and provenance primitives."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Any
import uuid


_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
_FIXTURE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$")
_VARIANTS = frozenset({"c", "s3-o0", "s3-o1"})


class ArtifactError(RuntimeError):
    """Raised when an artifact or run-isolation contract is violated."""


class ProvenanceError(ArtifactError):
    """Raised before execution when a pinned repository HEAD is not exact."""


def sha256_file(path: Path) -> str:
    """Return a file digest, refusing missing or non-regular artifacts."""

    if not path.is_file():
        raise ArtifactError(f"missing artifact: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_head(repo: Path) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--verify", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise ProvenanceError(f"cannot resolve Git HEAD for {repo}") from error
    value = completed.stdout.strip()
    if _SHA_RE.fullmatch(value) is None:
        raise ProvenanceError(f"Git HEAD is not a full SHA for {repo}: {value!r}")
    return value


def require_provenance(
    *,
    s3_repo: Path,
    requested_s3_sha: str,
    benchmark_repo: Path,
    requested_benchmark_sha: str,
) -> dict[str, str]:
    """Resolve and compare both repository SHAs before any native work."""

    if _SHA_RE.fullmatch(requested_s3_sha) is None:
        raise ProvenanceError("requested S3 SHA must be a full commit SHA")
    if _SHA_RE.fullmatch(requested_benchmark_sha) is None:
        raise ProvenanceError("requested benchmark SHA must be a full commit SHA")
    actual_s3_sha = git_head(s3_repo)
    actual_benchmark_sha = git_head(benchmark_repo)
    if actual_s3_sha != requested_s3_sha or actual_benchmark_sha != requested_benchmark_sha:
        raise ProvenanceError(
            "STOP_PROVENANCE_MISMATCH: "
            f"S3 expected {requested_s3_sha} got {actual_s3_sha}; "
            f"benchmark expected {requested_benchmark_sha} got {actual_benchmark_sha}"
        )
    return {
        "s3_commit": actual_s3_sha,
        "benchmark_commit": actual_benchmark_sha,
    }


def _generated_run_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"run-{timestamp}-{os.getpid()}-{uuid.uuid4().hex[:12]}"


def _validate_run_id(run_id: str) -> str:
    if _RUN_ID_RE.fullmatch(run_id) is None:
        raise ArtifactError(f"invalid run id: {run_id!r}")
    return run_id


def _validate_fixture_id(fixture_id: str) -> str:
    if _FIXTURE_RE.fullmatch(fixture_id) is None:
        raise ArtifactError(f"invalid fixture id: {fixture_id!r}")
    return fixture_id


@dataclass(frozen=True, slots=True)
class RunIdentity:
    """A non-reusable writable root for one benchmark invocation."""

    artifact_root: Path
    run_id: str
    run_root: Path

    @classmethod
    def create(cls, artifact_root: Path, run_id: str | None = None) -> "RunIdentity":
        artifact_root = artifact_root.resolve()
        artifact_root.mkdir(parents=True, exist_ok=True)
        selected = _validate_run_id(run_id or _generated_run_id())
        run_root = artifact_root / selected
        try:
            run_root.mkdir()
        except FileExistsError as error:
            raise ArtifactError(f"run id already exists; refusing reuse: {selected}") from error
        (run_root / "fixtures").mkdir()
        return cls(artifact_root, selected, run_root)

    def path(self, *parts: str) -> Path:
        candidate = (self.run_root.joinpath(*parts)).resolve()
        try:
            candidate.relative_to(self.run_root)
        except ValueError as error:
            raise ArtifactError(f"artifact path escapes run root: {candidate}") from error
        return candidate

    def fixture_root(self, fixture_id: str) -> Path:
        fixture_id = _validate_fixture_id(fixture_id)
        path = self.path("fixtures", fixture_id)
        path.mkdir(exist_ok=False)
        return path

    def variant_root(self, fixture_id: str, variant: str) -> Path:
        if variant not in _VARIANTS:
            raise ArtifactError(f"unsupported artifact variant: {variant}")
        path = self.path("fixtures", _validate_fixture_id(fixture_id), variant)
        path.mkdir(parents=True, exist_ok=False)
        return path

    def require_file(self, relative_path: str) -> Path:
        path = self.path(*Path(relative_path).parts)
        if not path.is_file():
            raise ArtifactError(f"missing current-run artifact: {relative_path}")
        return path

    def write_json_once(self, relative_path: str, value: Any) -> Path:
        path = self.path(*Path(relative_path).parts)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with path.open("x", encoding="utf-8", newline="\n") as stream:
                json.dump(value, stream, indent=2, sort_keys=True)
                stream.write("\n")
        except FileExistsError as error:
            raise ArtifactError(f"refusing to overwrite completed artifact: {path}") from error
        return path

    def relative(self, path: Path) -> str:
        try:
            return path.resolve().relative_to(self.run_root).as_posix()
        except ValueError as error:
            raise ArtifactError(f"artifact is outside run root: {path}") from error


def file_record(run: RunIdentity, path: Path | None) -> dict[str, Any]:
    """Record a current-run file without permitting a missing fallback."""

    if path is None:
        return {"path": None, "sha256": None, "bytes": None}
    resolved = path.resolve()
    return {
        "path": run.relative(resolved),
        "sha256": sha256_file(resolved),
        "bytes": resolved.stat().st_size,
    }


def load_manifest(run: RunIdentity) -> dict[str, Any]:
    """Load only the explicitly named current run manifest."""

    path = run.require_file("artifact-manifest.json")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ArtifactError(f"invalid current-run artifact manifest: {path}") from error
    if value.get("run_id") != run.run_id:
        raise ArtifactError("artifact manifest run id mismatch")
    return value
