"""Import read-only S3 Stage1 evidence into a Bootstrap Laboratory snapshot.

The importer never mutates the S3 checkout and never promotes missing or ambiguous
evidence to PASS. It consumes the current semantic-IR requirements artifact,
verifies Git + canonical-source provenance, and attaches selected supplemental
Stage1 JSON evidence as provenance only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

RELATIONSHIP_GROUPS = {
    "typed_values": ("typed_value_definitions",),
    "instruction_def_use": (
        "instruction_operand_value_ids",
        "instruction_result_value_ids",
    ),
    "call_dataflow": ("call_argument_value_ids", "call_result_value_ids"),
    "complete_terminators": ("complete_terminator_values",),
    "canonical_serialization": ("canonical_serialized_ir",),
}

SUPPLEMENTAL_STAGE1_JSON = (
    "call-argument-pool-closure.json",
    "call-argument-pool-audit.json",
)
CANONICAL_STAGE1_SOURCE = Path("selfhost/compiler/s3c_stage1.s3")


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str | None:
    return _sha256_bytes(path.read_bytes()) if path.is_file() else None


def _git_head(repo: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    return value if len(value) == 40 else None


def _normalize_state(value: object, *, missing: str) -> str:
    if not isinstance(value, str):
        return missing
    upper = value.upper()
    if "PASS" in upper and not any(word in upper for word in ("NOT_PASS", "BLOCK", "FAIL")):
        return "PASS"
    if "FAIL" in upper:
        return "FAIL"
    if "NOT_AUTH" in upper:
        return "NOT_AUTHORIZED"
    if "NOT_CREATED" in upper:
        return "NOT_CREATED"
    if "NOT_STARTED" in upper:
        return "NOT_STARTED"
    if "DEFER" in upper:
        return "DEFERRED"
    if "BLOCK" in upper:
        return "BLOCKED"
    return missing


def _surface_state(relationships: dict[str, Any], names: tuple[str, ...]) -> str:
    values = [relationships.get(name) for name in names]
    if values and all(value is True for value in values):
        return "PASS"
    return "BLOCKED"


def _semantic_source_sha256(semantic: dict[str, Any]) -> str | None:
    source = semantic.get("source")
    if not isinstance(source, dict):
        return None
    value = source.get("sha256")
    return value if isinstance(value, str) and len(value) == 64 else None


def summarize_supplemental_json(
    path: Path,
    *,
    current_semantic_source_sha256: str | None = None,
) -> dict[str, Any]:
    """Return bounded provenance from a supplemental evidence JSON file.

    Supplemental evidence is never mapped into semantic surface PASS. If the
    supplemental measurement identifies a canonical source hash, applicability is
    compared with the current semantic-evidence source hash so retained historical
    reports cannot silently become current evidence.
    """
    raw = path.read_bytes()
    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"supplemental evidence must contain an object: {path}")

    measured_source_sha256 = None
    clean_source = payload.get("clean_source_gate")
    if isinstance(clean_source, dict):
        candidate = clean_source.get("source_sha256")
        if isinstance(candidate, str) and len(candidate) == 64:
            measured_source_sha256 = candidate

    if measured_source_sha256 is None or current_semantic_source_sha256 is None:
        source_applicability = "UNKNOWN"
    elif measured_source_sha256 == current_semantic_source_sha256:
        source_applicability = "MATCH"
    else:
        source_applicability = "HISTORICAL_SOURCE_MISMATCH"

    row: dict[str, Any] = {
        "path": str(path),
        "sha256": _sha256_bytes(raw),
        "status": payload.get("status"),
        "schema": payload.get("schema") or payload.get("schema_version"),
        "promotion_effect": "NONE_PROVENANCE_ONLY",
        "measured_source_sha256": measured_source_sha256,
        "current_semantic_source_sha256": current_semantic_source_sha256,
        "source_applicability": source_applicability,
    }
    pool = payload.get("pool")
    if isinstance(pool, dict):
        row["pool"] = {
            "required_capacity": pool.get("required_capacity"),
            "selected_capacity": pool.get("selected_capacity"),
            "headroom": pool.get("headroom"),
            "bank_sizes": pool.get("bank_sizes"),
        }
    runtime = payload.get("runtime_measurement")
    if isinstance(runtime, dict):
        row["runtime_measurement"] = {
            "total_calls": runtime.get("total_calls"),
            "total_call_arguments": runtime.get("total_call_arguments"),
            "max_call_arity": runtime.get("max_call_arity"),
            "pool_used": runtime.get("pool_used"),
            "pool_gate": runtime.get("pool_gate"),
        }
    remaining = payload.get("remaining_blocker")
    if isinstance(remaining, dict):
        row["remaining_blocker"] = {
            "id": remaining.get("id"),
            "stage": remaining.get("stage"),
            "stage1_to_stage2": remaining.get("stage1_to_stage2"),
            "stage3": remaining.get("stage3"),
        }
    return row


def snapshot_from_semantic_requirements(
    semantic: dict[str, Any],
    *,
    s3_commit: str,
    benchmark_commit: str,
    source_lock_valid: bool,
    benchmark_lock_valid: bool,
) -> dict[str, Any]:
    storage = semantic.get("storage_evidence")
    storage = storage if isinstance(storage, dict) else {}
    relationships = storage.get("semantic_relationships")
    relationships = relationships if isinstance(relationships, dict) else {}

    surfaces = {
        surface: _surface_state(relationships, required)
        for surface, required in RELATIONSHIP_GROUPS.items()
    }
    all_surfaces = all(state == "PASS" for state in surfaces.values())

    self_emit = _normalize_state(semantic.get("stage1_self_emit"), missing="BLOCKED")
    stage2 = _normalize_state(semantic.get("stage2"), missing="NOT_CREATED")
    stage3 = _normalize_state(semantic.get("stage3"), missing="NOT_STARTED")
    semantic_status = _normalize_state(semantic.get("status"), missing="BLOCKED")
    stage1 = "PASS" if semantic_status == "PASS" and all_surfaces else "BLOCKED"

    reference_ir = semantic.get("reference_typed_ir")
    reference_ir = reference_ir if isinstance(reference_ir, dict) else {}

    return {
        "schema": "s3.bootstrap-laboratory-snapshot.v1",
        "provenance": {
            "s3_commit": s3_commit,
            "benchmark_commit": benchmark_commit,
            "source_lock_valid": source_lock_valid,
            "benchmark_lock_valid": benchmark_lock_valid,
        },
        "bootstrap": {
            "stage0_reference": "PASS",
            "stage1": stage1,
            "stage1_self_emit": self_emit,
            "stage2": stage2,
            "stage3": stage3,
            "full_self_hosting": False,
        },
        "semantic_ir": surfaces,
        "determinism": {
            "stage1_stage2_stage3_equivalence": "NOT_AUTHORIZED"
            if stage2 != "PASS" or stage3 != "PASS"
            else "BLOCKED"
        },
        "resources": {
            "peak_rss_bytes": None,
            "compile_wall_seconds": None,
            "artifact_bytes": None,
            "assembly_bytes": None,
            "semantic_value_count": None,
            "instruction_count": None,
            "block_count": None,
            "call_count": None,
        },
        "performance_eligibility": {
            "correctness_pass": False,
            "equivalent_workload": False,
            "stable_environment": False,
            "performance_valid": False,
        },
        "evidence_notes": {
            "semantic_requirements_schema": semantic.get("schema"),
            "semantic_requirements_status": semantic.get("status"),
            "semantic_source_sha256": _semantic_source_sha256(semantic),
            "host_oracle_status": reference_ir.get("status"),
            "host_oracle_used_as_stage1_evidence": False,
            "missing_lossless_typed_lanes": semantic.get("missing_lossless_typed_lanes", []),
            "supplemental_evidence": [],
            "import_policy": "READ_ONLY_FAIL_CLOSED",
        },
    }


def import_checkout(
    s3_repo: Path,
    benchmark_repo: Path,
    *,
    expected_s3_commit: str | None = None,
    expected_benchmark_commit: str | None = None,
) -> dict[str, Any]:
    stage1_reports = s3_repo / "reports" / "selfhost" / "stage1"
    semantic_path = stage1_reports / "semantic-ir-requirements.json"
    if not semantic_path.is_file():
        raise FileNotFoundError(f"required evidence artifact not found: {semantic_path}")
    semantic = json.loads(semantic_path.read_text(encoding="utf-8"))
    if not isinstance(semantic, dict):
        raise ValueError("semantic IR requirements artifact must contain an object")

    s3_head = _git_head(s3_repo)
    bench_head = _git_head(benchmark_repo)
    s3_commit = s3_head or expected_s3_commit or "UNKNOWN_S3_COMMIT"
    benchmark_commit = bench_head or expected_benchmark_commit or "UNKNOWN_BENCHMARK_COMMIT"

    git_source_lock_valid = bool(
        s3_head and (expected_s3_commit is None or s3_head == expected_s3_commit)
    )
    semantic_source_sha256 = _semantic_source_sha256(semantic)
    actual_source_sha256 = _sha256_file(s3_repo / CANONICAL_STAGE1_SOURCE)
    semantic_source_lock_valid = bool(
        semantic_source_sha256
        and actual_source_sha256
        and semantic_source_sha256 == actual_source_sha256
    )
    source_lock_valid = git_source_lock_valid and semantic_source_lock_valid
    benchmark_lock_valid = bool(
        bench_head
        and (expected_benchmark_commit is None or bench_head == expected_benchmark_commit)
    )

    snapshot = snapshot_from_semantic_requirements(
        semantic,
        s3_commit=s3_commit,
        benchmark_commit=benchmark_commit,
        source_lock_valid=source_lock_valid,
        benchmark_lock_valid=benchmark_lock_valid,
    )
    snapshot["evidence_notes"].update(
        {
            "git_source_lock_valid": git_source_lock_valid,
            "semantic_source_lock_valid": semantic_source_lock_valid,
            "actual_canonical_source_sha256": actual_source_sha256,
        }
    )

    supplemental: list[dict[str, Any]] = []
    for filename in SUPPLEMENTAL_STAGE1_JSON:
        path = stage1_reports / filename
        if path.is_file():
            supplemental.append(
                summarize_supplemental_json(
                    path,
                    current_semantic_source_sha256=semantic_source_sha256,
                )
            )
    snapshot["evidence_notes"]["supplemental_evidence"] = supplemental
    return snapshot


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--benchmark-repo", type=Path, default=Path.cwd())
    parser.add_argument("--expected-s3-commit")
    parser.add_argument("--expected-benchmark-commit")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    snapshot = import_checkout(
        args.s3_repo,
        args.benchmark_repo,
        expected_s3_commit=args.expected_s3_commit,
        expected_benchmark_commit=args.expected_benchmark_commit,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OUTPUT={args.output}")
    print(f"S3_COMMIT={snapshot['provenance']['s3_commit']}")
    print(f"SOURCE_LOCK_VALID={snapshot['provenance']['source_lock_valid']}")
    print(f"STAGE1={snapshot['bootstrap']['stage1']}")
    print(f"STAGE2={snapshot['bootstrap']['stage2']}")
    print(f"SUPPLEMENTAL_EVIDENCE={len(snapshot['evidence_notes']['supplemental_evidence'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
