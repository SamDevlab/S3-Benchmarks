"""Compare available Stage1/Stage2/Stage3 evidence without inventing missing stages.

Byte identity and observable equivalence are deliberately separate. By default,
Stage2/Stage3 byte identity is reported when both artifacts exist, while semantic
observable equivalence is evaluated only from explicitly supplied observation files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

STAGES = ("stage1", "stage2", "stage3")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare(
    artifacts: dict[str, Path | None],
    observations: dict[str, Path | None],
) -> dict[str, Any]:
    artifact_rows: dict[str, Any] = {}
    observation_rows: dict[str, Any] = {}
    for stage in STAGES:
        artifact = artifacts.get(stage)
        artifact_rows[stage] = {
            "available": bool(artifact and artifact.is_file()),
            "path": str(artifact) if artifact else None,
            "sha256": _sha(artifact) if artifact and artifact.is_file() else None,
            "bytes": artifact.stat().st_size if artifact and artifact.is_file() else None,
        }
        observation = observations.get(stage)
        observation_rows[stage] = {
            "available": bool(observation and observation.is_file()),
            "path": str(observation) if observation else None,
            "sha256": _sha(observation) if observation and observation.is_file() else None,
        }

    s2 = artifact_rows["stage2"]["sha256"]
    s3 = artifact_rows["stage3"]["sha256"]
    stage2_stage3_byte_identity: bool | None = None
    if s2 is not None and s3 is not None:
        stage2_stage3_byte_identity = s2 == s3

    observation_hashes = [observation_rows[stage]["sha256"] for stage in STAGES]
    observable_equivalence: bool | None = None
    if all(value is not None for value in observation_hashes):
        observable_equivalence = len(set(observation_hashes)) == 1

    missing_artifacts = [stage for stage in STAGES if not artifact_rows[stage]["available"]]
    missing_observations = [stage for stage in STAGES if not observation_rows[stage]["available"]]
    if observable_equivalence is True:
        equivalence_state = "PASS"
    elif observable_equivalence is False:
        equivalence_state = "FAIL"
    else:
        equivalence_state = "NOT_AVAILABLE"

    return {
        "schema": "s3.bootstrap-stage-equivalence.v1",
        "artifacts": artifact_rows,
        "observations": observation_rows,
        "missing_artifacts": missing_artifacts,
        "missing_observations": missing_observations,
        "stage2_stage3_byte_identity": stage2_stage3_byte_identity,
        "stage1_stage2_stage3_observable_equivalence": equivalence_state,
        "full_self_hosting_claim": False,
        "interpretation": (
            "Byte identity is a reproducibility property. Observable equivalence is a semantic property. "
            "Missing stages remain NOT_AVAILABLE and are never treated as zero-sized or equal."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for stage in STAGES:
        parser.add_argument(f"--{stage}-artifact", type=Path)
        parser.add_argument(f"--{stage}-observation", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    artifacts = {stage: getattr(args, f"{stage}_artifact") for stage in STAGES}
    observations = {stage: getattr(args, f"{stage}_observation") for stage in STAGES}
    report = compare(artifacts, observations)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OUTPUT={args.output}")
    print(f"EQUIVALENCE={report['stage1_stage2_stage3_observable_equivalence']}")
    print(f"STAGE2_STAGE3_BYTE_IDENTITY={report['stage2_stage3_byte_identity']}")
    return 2 if report["stage1_stage2_stage3_observable_equivalence"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
