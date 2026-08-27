"""Preserve a reproducible S3IR2 v2 failure bundle for later minimization."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from tools.ingest_s3ir2_v2 import ingest


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def capture(
    source: Path,
    stream: Path,
    conformance: Path,
    output: Path,
) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    source_out = output / "reproducer.s3"
    stream_out = output / "candidate.s3ir2"
    conformance_out = output / "conformance.json"
    shutil.copyfile(source, source_out)
    shutil.copyfile(stream, stream_out)
    shutil.copyfile(conformance, conformance_out)

    stream_text = stream_out.read_text(encoding="utf-8")
    ingest_report = ingest(stream_text, source_sha256=_sha(source_out))
    ingest_out = output / "ingest.json"
    ingest_out.write_text(
        json.dumps(ingest_report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    conformance_data = json.loads(conformance_out.read_text(encoding="utf-8"))
    manifest: dict[str, object] = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-failure-bundle.v1",
        "source_sha256": _sha(source_out),
        "stream_sha256": _sha(stream_out),
        "conformance_sha256": _sha(conformance_out),
        "ingest_sha256": _sha(ingest_out),
        "conformance_status": conformance_data.get("status", "UNKNOWN"),
        "structural_status": ingest_report["structural_status"],
        "completeness_mask": ingest_report["completeness_mask"],
        "files": {
            "source": source_out.name,
            "stream": stream_out.name,
            "conformance": conformance_out.name,
            "ingest": ingest_out.name,
        },
        "minimization_status": "NOT_RUN",
        "promotion_effect": "NONE_FAILURE_EVIDENCE_ONLY",
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--stream", type=Path, required=True)
    parser.add_argument("--conformance", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = capture(args.source, args.stream, args.conformance, args.output)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_FAILURE_BUNDLE_ERROR={error}\n")
    print(f"OUTPUT={args.output}")
    print(f"CONFORMANCE_STATUS={manifest['conformance_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
