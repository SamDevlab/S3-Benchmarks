"""Record one immutable S3IR2 v2 laboratory checkpoint.

The recorder is append-only by path and binds the requested candidate identity to
the identity already proven inside the evidence-set manifest. External SHA
arguments cannot override or relabel the evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def record(
    *,
    candidate_sha: str,
    candidate_source_sha256: str,
    case_id: str,
    stage_id: str,
    evidence_manifest: Path,
    output: Path,
) -> dict[str, Any]:
    if output.exists():
        raise FileExistsError(f"checkpoint already exists: {output}")
    if not HEX40.fullmatch(candidate_sha):
        raise ValueError("candidate_sha must be 40 lowercase hex characters")
    if not HEX64.fullmatch(candidate_source_sha256):
        raise ValueError("candidate_source_sha256 must be 64 lowercase hex characters")
    if not case_id.strip():
        raise ValueError("case_id must be non-empty")
    if not stage_id.strip():
        raise ValueError("stage_id must be non-empty")

    manifest_bytes = evidence_manifest.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("evidence manifest must be a JSON object")

    manifest_candidate_sha = manifest.get("candidate_git_sha")
    manifest_source_sha = manifest.get("candidate_source_sha256")
    if manifest_candidate_sha != candidate_sha:
        raise ValueError("candidate_sha does not match evidence manifest candidate_git_sha")
    if manifest_source_sha != candidate_source_sha256:
        raise ValueError(
            "candidate_source_sha256 does not match evidence manifest candidate_source_sha256"
        )

    candidate_binary_sha = manifest.get("candidate_binary_sha256")
    if not isinstance(candidate_binary_sha, str) or not HEX64.fullmatch(candidate_binary_sha):
        raise ValueError("evidence manifest lacks a valid candidate_binary_sha256")

    checkpoint = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-checkpoint.v1",
        "protocol": "S3IR2 v2",
        "candidate_git_sha": candidate_sha,
        "candidate_source_sha256": candidate_source_sha256,
        "candidate_binary_sha256": candidate_binary_sha,
        "control_revision": manifest.get("control_revision"),
        "case_id": case_id,
        "stage_id": stage_id,
        "evidence_manifest": {
            "path": str(evidence_manifest),
            "sha256": _sha_bytes(manifest_bytes),
            "structural_status": manifest.get("structural_status", "UNKNOWN"),
            "native_provenance_status": manifest.get("native_provenance_status", "UNKNOWN"),
            "semantic_conformance_status": manifest.get("semantic_conformance_status", "UNKNOWN"),
            "determinism_status": manifest.get("determinism_status", "NOT_EVALUATED"),
            "qualification_gate": manifest.get("qualification_gate", "UNKNOWN"),
        },
        "immutable": True,
        "promotion_effect": "NONE_PROVENANCE_ONLY",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(checkpoint, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return checkpoint


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-sha", required=True)
    parser.add_argument("--candidate-source-sha256", required=True)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--stage-id", required=True)
    parser.add_argument("--evidence-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        checkpoint = record(
            candidate_sha=args.candidate_sha,
            candidate_source_sha256=args.candidate_source_sha256,
            case_id=args.case_id,
            stage_id=args.stage_id,
            evidence_manifest=args.evidence_manifest,
            output=args.output,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_CHECKPOINT_ERROR={error}\n")
    print(f"CHECKPOINT={args.output}")
    print(f"QUALIFICATION_GATE={checkpoint['evidence_manifest']['qualification_gate']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
