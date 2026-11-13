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


def _actual_sha(report: dict[str, Any], label: str) -> str | None:
    actual = report.get("actual_files")
    if not isinstance(actual, dict):
        return None
    item = actual.get(label)
    if not isinstance(item, dict):
        return None
    value = item.get("sha256")
    return value if isinstance(value, str) else None


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

    copied_candidate_source_sha: str | None = None
    copied_candidate_binary_sha: str | None = None
    if candidate_source is not None:
        files["candidate_source"] = _copy(
            candidate_source,
            output,
            "candidate-source.s3",
        )
        copied_candidate_source_sha = str(files["candidate_source"]["sha256"])
    if candidate_binary is not None:
        files["candidate_binary"] = _copy(
            candidate_binary,
            output,
            "candidate-binary",
        )
        copied_candidate_binary_sha = str(files["candidate_binary"]["sha256"])

    provenance_data: dict[str, Any] | None = None
    if native_provenance is not None:
        files["native_provenance"] = _copy(
            native_provenance,
            output,
            "native-provenance.json",
        )
        provenance_data = _load_json(output / "native-provenance.json")

    binding_data: dict[str, Any] | None = None
    if native_binding is not None:
        files["native_binding"] = _copy(
            native_binding,
            output,
            "native-binding.json",
        )
        binding_data = _load_json(output / "native-binding.json")

    proven_candidate_source_sha = (
        _actual_sha(provenance_data, "candidate_source")
        if provenance_data is not None
        else None
    )
    proven_candidate_binary_sha = (
        _actual_sha(provenance_data, "candidate_binary")
        if provenance_data is not None
        else None
    )
    proven_fixture_sha = (
        _actual_sha(provenance_data, "fixture_source")
        if provenance_data is not None
        else None
    )
    proven_stream_sha = (
        _actual_sha(provenance_data, "stream")
        if provenance_data is not None
        else None
    )

    candidate_identity: dict[str, object] = {
        "candidate_git_sha": (
            provenance_data.get("candidate_git_sha")
            if provenance_data is not None
            else None
        ),
        "control_revision": (
            provenance_data.get("control_revision")
            if provenance_data is not None
            else None
        ),
        "copied_candidate_source_sha256": copied_candidate_source_sha,
        "proven_candidate_source_sha256": proven_candidate_source_sha,
        "copied_candidate_binary_sha256": copied_candidate_binary_sha,
        "proven_candidate_binary_sha256": proven_candidate_binary_sha,
        "proven_fixture_source_sha256": proven_fixture_sha,
        "proven_stream_sha256": proven_stream_sha,
        "native_provenance_status": (
            provenance_data.get("status", "UNKNOWN")
            if provenance_data is not None
            else "NOT_SUPPLIED"
        ),
        "native_binding_status": (
            binding_data.get("status", "UNKNOWN")
            if binding_data is not None
            else "NOT_SUPPLIED"
        ),
    }

    identity_errors: list[str] = []
    bundle_fixture_sha = str(files["source"]["sha256"])
    bundle_stream_sha = str(files["stream"]["sha256"])

    if provenance_data is not None:
        if provenance_data.get("status") != "PASS":
            identity_errors.append("native provenance status is not PASS")
        if proven_fixture_sha != bundle_fixture_sha:
            identity_errors.append("bundle fixture SHA differs from native provenance")
        if proven_stream_sha != bundle_stream_sha:
            identity_errors.append("bundle stream SHA differs from native provenance")
        if candidate_source is not None and proven_candidate_source_sha != copied_candidate_source_sha:
            identity_errors.append("candidate source SHA differs from native provenance")
        if candidate_binary is not None and proven_candidate_binary_sha != copied_candidate_binary_sha:
            identity_errors.append("candidate binary SHA differs from native provenance")

    if binding_data is not None:
        if binding_data.get("status") != "PASS":
            identity_errors.append("native binding status is not PASS")
        primary = binding_data.get("primary")
        if not isinstance(primary, dict):
            identity_errors.append("native binding lacks primary identity")
        else:
            comparisons = {
                "candidate_git_sha": candidate_identity.get("candidate_git_sha"),
                "candidate_source_sha256": proven_candidate_source_sha,
                "candidate_binary_sha256": proven_candidate_binary_sha,
                "fixture_source_sha256": proven_fixture_sha,
                "stream_sha256": proven_stream_sha,
                "control_revision": candidate_identity.get("control_revision"),
            }
            for field, expected in comparisons.items():
                if expected is not None and primary.get(field) != expected:
                    identity_errors.append(
                        f"native binding primary {field} differs from native provenance"
                    )

    if native_provenance is None and (
        candidate_source is not None or candidate_binary is not None or native_binding is not None
    ):
        identity_errors.append(
            "candidate/native-binding artifacts supplied without native provenance"
        )

    manifest: dict[str, object] = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-failure-bundle.v1",
        "source_sha256": bundle_fixture_sha,
        "stream_sha256": bundle_stream_sha,
        "conformance_sha256": files["conformance"]["sha256"],
        "ingest_sha256": files["ingest"]["sha256"],
        "conformance_status": conformance_data.get("status", "UNKNOWN"),
        "structural_status": ingest_report["structural_status"],
        "completeness_mask": ingest_report["completeness_mask"],
        "candidate_identity": candidate_identity,
        "candidate_identity_status": (
            "PASS"
            if provenance_data is not None and not identity_errors
            else ("NOT_SUPPLIED" if provenance_data is None and not identity_errors else "FAIL")
        ),
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
