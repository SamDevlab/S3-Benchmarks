"""Record one immutable S3IR2 v2 laboratory checkpoint.

The recorder is intentionally append-only by path: it refuses to overwrite an
existing checkpoint. It binds candidate/source identity to the evidence-set
manifest so later candidate revisions cannot silently replace older evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


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
    manifest_bytes = evidence_manifest.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("evidence manifest must be a JSON object")

    checkpoint = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-checkpoint.v1",
        "protocol": "S3IR2 v2",
        "candidate_git_sha": candidate_sha,
        "candidate_source_sha256": candidate_source_sha256,
        "case_id": case_id,
        "stage_id": stage_id,
        "evidence_manifest": {
            "path": str(evidence_manifest),
            "sha256": _sha_bytes(manifest_bytes),
            "structural_status": manifest.get("structural_status", "UNKNOWN"),
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
