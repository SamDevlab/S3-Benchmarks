"""Deterministic workload/upstream registry loading."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .workload import BenchmarkWorkload, canonical_json, load_workload
from .provenance import SHA_RE


def load_registry(root: Path) -> dict[str, Any]:
    upstream_path = root / "references" / "upstreams-v2.json"
    raw = json.loads(upstream_path.read_text(encoding="utf-8"))
    if raw.get("schema_version") != 2:
        raise ValueError("upstream registry schema_version must be 2")
    references = raw.get("references")
    if not isinstance(references, list):
        raise ValueError("upstream registry references must be a list")
    ids = [entry.get("id") for entry in references]
    if any(not isinstance(value, str) for value in ids) or ids != sorted(ids):
        raise ValueError("upstream registry must be deterministically ordered by id")
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate upstream id")
    for entry in references:
        required = {"id", "name", "repository", "immutable_commit_sha", "license", "purpose", "workload_subset", "vendoring_policy"}
        missing = sorted(required.difference(entry))
        if missing:
            raise ValueError(f"upstream entry {entry.get('id')!r} missing: {', '.join(missing)}")
        sha = entry["immutable_commit_sha"]
        if not isinstance(sha, str) or SHA_RE.fullmatch(sha) is None:
            raise ValueError(f"upstream {entry['id']} does not have an immutable commit SHA")
        if any(token in entry["repository"].lower() for token in ("/main", "/master", "/latest")):
            raise ValueError(f"floating upstream repository identity: {entry['repository']}")
    workloads = []
    for path in sorted((root / "benchmarks").glob("**/*manifest.json")):
        workloads.append(load_workload(path))
    workloads.sort(key=lambda item: item.id)
    workload_ids = [item.id for item in workloads]
    if workload_ids != sorted(workload_ids) or len(workload_ids) != len(set(workload_ids)):
        raise ValueError("workload manifests must have unique deterministic ids")
    return {"schema_version": 2, "references": references, "workloads": [item.to_dict() for item in workloads]}


def registry_digest(registry: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(registry).encode("utf-8")).hexdigest()
