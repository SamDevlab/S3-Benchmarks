"""Preserve a reproducible S3IR2 v2 failure bundle for later minimization."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from tools.ingest_s3ir2_v2 import ingest


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _copy(path: Path, output: Path, name: str) -> dict[str, object]:
    target = output / name
    shutil.copyfile(path, target)
    return {
        "name": target.name,
        "sha256": _sha(target),
        "bytes": target.stat().st_size,
    }


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def capture(
    source: Path,
    stream: Path,
    conformance: Path,
    output: Path,
    *,
    candidate_source: Path | None = None,
    candidate_binary: Path | None = None,
    native_provenance: Path | None = None,
    native_binding: Path | None = None,
) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)

    files: dict[str, object] = {}
    files["source"] = _copy(source, output, "reproducer.s3")
    files["stream"] = _copy(stream, output, "candidate.s3ir2")
    files["conformance"] = _copy(conformance, output, "conformance.json")

    source_out = output / "reproducer.s3"
    stream_out = output / "candidate.s3ir2"
    conformance_out = output / "conformance.json"

    stream_text = stream_out.read_text(encoding="utf-8")
    ingest_report = ingest(stream_text, source_sha256=_sha(source_out))
    ingest_out = output / "ingest.json"
    ingest_out.write_text(
        json.dumps(ingest_report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    files["ingest"] = {
        "name": ingest_out.name,
        "sha256": _sha(ingest_out),
        "bytes": ingest_out.stat().st_size,
    }

    conformance_data = _load_json(conformance_out)
    candidate_identity: dict[str, object] = {
        "candidate_git_sha": None,
        "candidate_source_sha256": None,
        "candidate_binary_sha256": None,
        "control_revision": None,
        "native_provenance_status": "NOT_SUPPLIED",
        "native_binding_status": "NOT_SUPPLIED",
    }

    if candidate_source is not None:
        files["candidate_source"] = _copy(
            candidate_source,
            output,
            "candidate-source.s3",
        )
        candidate_identity["candidate_source_sha256"] = files["candidate_source"]["sha256"]

    if candidate_binary is not None:
        files["candidate_binary"] = _copy(
            candidate_binary,
            output,
            "candidate-binary",
        )
        candidate_identity["candidate_binary_sha256"] = files["candidate_binary"]["sha256"]

    if native_provenance is not None:
        files["native_provenance"] = _copy(
            native_provenance,
            output,
            "native-provenance.json",
        )
        provenance_data = _load_json(output / "native-provenance.json")
        candidate_identity["candidate_git_sha"] = provenance_data.get("candidate_git_sha")
        candidate_identity["control_revision"] = provenance_data.get("control_revision")
        candidate_identity["native_provenance_status"] = provenance_data.get(
            "status", "UNKNOWN"
        )
        actual_files = provenance_data.get("actual_files", {})
        if isinstance(actual_files, dict):
            source_facts = actual_files.get("candidate_source")
            binary_facts = actual_files.get("candidate_binary")
            if (
                candidate_identity["candidate_source_sha256"] is None
                and isinstance(source_facts, dict)
            ):
                candidate_identity["candidate_source_sha256"] = source_facts.get("sha256")
            if (
                candidate_identity["candidate_binary_sha256"] is None
                and isinstance(binary_facts, dict)
            ):
                candidate_identity["candidate_binary_sha256"] = binary_facts.get("sha256")

    if native_binding is not None:
        files["native_binding"] = _copy(
            native_binding,
            output,
            "native-binding.json",
        )
        binding_data = _load_json(output / "native-binding.json")
        candidate_identity["native_binding_status"] = binding_data.get("status", "UNKNOWN")
        primary = binding_data.get("primary")
        if isinstance(primary, dict):
            for field in (
                "candidate_git_sha",
                "candidate_source_sha256",
                "candidate_binary_sha256",
                "control_revision",
            ):
                if candidate_identity.get(field) is None:
                    candidate_identity[field] = primary.get(field)

    identity_errors: list[str] = []
    if candidate_source is not None and native_provenance is not None:
        provenance_source = candidate_identity.get("candidate_source_sha256")
        copied_source = files["candidate_source"]["sha256"]
        if provenance_source != copied_source:
            identity_errors.append("candidate source SHA differs from native provenance")
    if candidate_binary is not None and native_provenance is not None:
        provenance_binary = candidate_identity.get("candidate_binary_sha256")
        copied_binary = files["candidate_binary"]["sha256"]
        if provenance_binary != copied_binary:
            identity_errors.append("candidate binary SHA differs from native provenance")

    manifest: dict[str, object] = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-failure-bundle.v1",
        "source_sha256": files["source"]["sha256"],
        "stream_sha256": files["stream"]["sha256"],
        "conformance_sha256": files["conformance"]["sha256"],
        "ingest_sha256": files["ingest"]["sha256"],
        "conformance_status": conformance_data.get("status", "UNKNOWN"),
        "structural_status": ingest_report["structural_status"],
        "completeness_mask": ingest_report["completeness_mask"],
        "candidate_identity": candidate_identity,
        "candidate_identity_status": "PASS" if not identity_errors else "FAIL",
        "candidate_identity_errors": identity_errors,
        "files": files,
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
    parser.add_argument("--candidate-source", type=Path)
    parser.add_argument("--candidate-binary", type=Path)
    parser.add_argument("--native-provenance", type=Path)
    parser.add_argument("--native-binding", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = capture(
            args.source,
            args.stream,
            args.conformance,
            args.output,
            candidate_source=args.candidate_source,
            candidate_binary=args.candidate_binary,
            native_provenance=args.native_provenance,
            native_binding=args.native_binding,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_FAILURE_BUNDLE_ERROR={error}\n")
    print(f"OUTPUT={args.output}")
    print(f"CONFORMANCE_STATUS={manifest['conformance_status']}")
    print(f"CANDIDATE_IDENTITY={manifest['candidate_identity_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
