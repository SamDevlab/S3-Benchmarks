"""Ingest a complete S3IR2 v2 evidence set into the Bootstrap Laboratory."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from tools.check_s3ir2_v2_determinism import check as check_determinism
from tools.classify_s3ir2_v2_failure import classify
from tools.ingest_s3ir2_v2 import ingest
from tools.render_s3ir2_v2_scorecard import build_scorecard


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ingest_set(
    *,
    source: Path,
    stream: Path,
    conformance: Path,
    repeats: list[Path],
    native_provenance: Path | None,
    output: Path,
) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    source_sha = _sha(source)
    stream_text = stream.read_text(encoding="utf-8")
    structural = ingest(stream_text, source_sha256=source_sha)
    conformance_data = json.loads(conformance.read_text(encoding="utf-8"))
    native_data = (
        json.loads(native_provenance.read_text(encoding="utf-8"))
        if native_provenance is not None
        else None
    )

    ingest_path = output / "ingest.json"
    ingest_path.write_text(
        json.dumps(structural, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    determinism_data: dict[str, object] | None = None
    determinism_path: Path | None = None
    if repeats:
        determinism_data = check_determinism([stream, *repeats])
        determinism_path = output / "determinism.json"
        determinism_path.write_text(
            json.dumps(determinism_data, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    scorecard = build_scorecard(
        structural,
        conformance=conformance_data,
        determinism=determinism_data,
        native_provenance=native_data,
    )
    scorecard_path = output / "scorecard.json"
    scorecard_path.write_text(
        json.dumps(scorecard, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    triage_path: Path | None = None
    if str(conformance_data.get("status", "UNKNOWN")) != "PASS":
        triage = classify(conformance_data)
        triage_path = output / "triage.json"
        triage_path.write_text(
            json.dumps(triage, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    files: dict[str, object] = {
        "source": {"path": str(source), "sha256": source_sha},
        "stream": {"path": str(stream), "sha256": _sha(stream)},
        "conformance": {"path": str(conformance), "sha256": _sha(conformance)},
        "ingest": {"path": str(ingest_path), "sha256": _sha(ingest_path)},
        "scorecard": {"path": str(scorecard_path), "sha256": _sha(scorecard_path)},
    }
    if native_provenance is not None:
        files["native_provenance"] = {
            "path": str(native_provenance),
            "sha256": _sha(native_provenance),
        }
    if determinism_path is not None:
        files["determinism"] = {
            "path": str(determinism_path),
            "sha256": _sha(determinism_path),
        }
    if triage_path is not None:
        files["triage"] = {"path": str(triage_path), "sha256": _sha(triage_path)}

    manifest: dict[str, object] = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-evidence-set.v1",
        "protocol": "S3IR2 v2",
        "files": files,
        "repeat_stream_count": len(repeats),
        "structural_status": structural["structural_status"],
        "semantic_conformance_status": conformance_data.get("status", "UNKNOWN"),
        "determinism_status": (
            determinism_data.get("status", "UNKNOWN")
            if determinism_data is not None
            else "NOT_EVALUATED"
        ),
        "native_provenance_status": (
            native_data.get("status", "UNKNOWN")
            if isinstance(native_data, dict)
            else "NOT_EVALUATED"
        ),
        "qualification_gate": scorecard["qualification_gate"],
        "promotion_effect": "NONE_LABORATORY_EVIDENCE_ONLY",
    }
    manifest_path = output / "evidence-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--stream", type=Path, required=True)
    parser.add_argument("--conformance", type=Path, required=True)
    parser.add_argument("--repeat-stream", action="append", type=Path, default=[])
    parser.add_argument("--native-provenance", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = ingest_set(
            source=args.source,
            stream=args.stream,
            conformance=args.conformance,
            repeats=args.repeat_stream,
            native_provenance=args.native_provenance,
            output=args.output,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_EVIDENCE_SET_ERROR={error}\n")
    print(f"QUALIFICATION_GATE={manifest['qualification_gate']}")
    print(f"SEMANTIC_CONFORMANCE={manifest['semantic_conformance_status']}")
    print(f"DETERMINISM={manifest['determinism_status']}")
    print(f"NATIVE_PROVENANCE={manifest['native_provenance_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
