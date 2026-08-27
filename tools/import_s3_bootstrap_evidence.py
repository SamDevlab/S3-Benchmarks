"""Import read-only S3 Stage1 evidence into a Bootstrap Laboratory snapshot.

The importer never mutates the S3 checkout and never promotes missing or ambiguous
evidence to PASS. It consumes the current semantic-IR requirements artifact when
available and can verify exact Git provenance for both repositories.
"""

from __future__ import annotations

import argparse
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
    # False, missing, malformed, or mixed evidence stays fail-closed.
    return "BLOCKED"


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
    host_oracle_status = reference_ir.get("status")

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
            "host_oracle_status": host_oracle_status,
            "host_oracle_used_as_stage1_evidence": False,
            "missing_lossless_typed_lanes": semantic.get("missing_lossless_typed_lanes", []),
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
    semantic_path = s3_repo / "reports" / "selfhost" / "stage1" / "semantic-ir-requirements.json"
    if not semantic_path.is_file():
        raise FileNotFoundError(f"required evidence artifact not found: {semantic_path}")
    semantic = json.loads(semantic_path.read_text(encoding="utf-8"))
    if not isinstance(semantic, dict):
        raise ValueError("semantic IR requirements artifact must contain an object")

    s3_head = _git_head(s3_repo)
    bench_head = _git_head(benchmark_repo)
    s3_commit = s3_head or expected_s3_commit or "UNKNOWN_S3_COMMIT"
    benchmark_commit = bench_head or expected_benchmark_commit or "UNKNOWN_BENCHMARK_COMMIT"
    source_lock_valid = bool(
        s3_head
        and (expected_s3_commit is None or s3_head == expected_s3_commit)
    )
    benchmark_lock_valid = bool(
        bench_head
        and (expected_benchmark_commit is None or bench_head == expected_benchmark_commit)
    )
    return snapshot_from_semantic_requirements(
        semantic,
        s3_commit=s3_commit,
        benchmark_commit=benchmark_commit,
        source_lock_valid=source_lock_valid,
        benchmark_lock_valid=benchmark_lock_valid,
    )


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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
