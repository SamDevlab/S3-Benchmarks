"""Validate native provenance for one Stage1 S3IR2 v2 stream.

The validator recomputes hashes and byte sizes from the actual candidate source,
native candidate binary, fixture source, and emitted stream. Metadata alone is
never treated as proof.
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


def _facts(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": str(path),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }


def validate(
    metadata: dict[str, Any],
    *,
    candidate_source: Path,
    candidate_binary: Path,
    fixture_source: Path,
    stream: Path,
) -> dict[str, Any]:
    errors: list[str] = []
    if metadata.get("schema") != "s3.stage1.native-semantic-evidence.v1":
        errors.append("invalid or missing metadata schema")

    git_sha = str(metadata.get("candidate_git_sha", ""))
    if not HEX40.fullmatch(git_sha):
        errors.append("candidate_git_sha must be 40 lowercase hex characters")

    control_revision = metadata.get("control_revision")
    if not isinstance(control_revision, int) or isinstance(control_revision, bool) or control_revision < 1:
        errors.append("control_revision must be an integer >= 1")

    platform = metadata.get("platform", {})
    if not isinstance(platform, dict):
        errors.append("platform must be an object")
        platform = {}
    if str(platform.get("os", "")).lower() != "linux":
        errors.append("platform.os must be linux")
    if str(platform.get("arch", "")).lower() != "x86_64":
        errors.append("platform.arch must be x86_64")

    build = metadata.get("build", {})
    if not isinstance(build, dict):
        errors.append("build must be an object")
        build = {}
    if build.get("status") != "PASS" or build.get("exit_code") != 0:
        errors.append("native build must have status PASS and exit_code 0")

    run = metadata.get("run", {})
    if not isinstance(run, dict):
        errors.append("run must be an object")
        run = {}
    if run.get("status") != "PASS":
        errors.append("native run must have status PASS")
    if not isinstance(run.get("exit_code"), int) or isinstance(run.get("exit_code"), bool):
        errors.append("run.exit_code must be an integer")

    actual = {
        "candidate_source": _facts(candidate_source),
        "candidate_binary": _facts(candidate_binary),
        "fixture_source": _facts(fixture_source),
        "stream": _facts(stream),
    }
    declared_pairs = {
        "candidate_source": ("candidate_source_sha256", "candidate_source_bytes"),
        "candidate_binary": ("candidate_binary_sha256", "candidate_binary_bytes"),
        "fixture_source": ("fixture_source_sha256", "fixture_source_bytes"),
        "stream": ("stream_sha256", "stream_bytes"),
    }
    for label, (sha_key, bytes_key) in declared_pairs.items():
        declared_sha = metadata.get(sha_key)
        declared_bytes = metadata.get(bytes_key)
        if not isinstance(declared_sha, str) or not HEX64.fullmatch(declared_sha):
            errors.append(f"{sha_key} must be 64 lowercase hex characters")
        elif declared_sha != actual[label]["sha256"]:
            errors.append(f"{label} SHA-256 mismatch")
        if not isinstance(declared_bytes, int) or isinstance(declared_bytes, bool) or declared_bytes < 0:
            errors.append(f"{bytes_key} must be a non-negative integer")
        elif declared_bytes != actual[label]["bytes"]:
            errors.append(f"{label} byte-size mismatch")

    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-native-provenance.v1",
        "protocol": "S3IR2 v2",
        "status": "PASS" if not errors else "FAIL",
        "candidate_git_sha": git_sha,
        "control_revision": control_revision,
        "platform": platform,
        "build": build,
        "run": run,
        "actual_files": actual,
        "errors": errors,
        "promotion_effect": "NONE_PROVENANCE_GATE_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--candidate-source", type=Path, required=True)
    parser.add_argument("--candidate-binary", type=Path, required=True)
    parser.add_argument("--fixture-source", type=Path, required=True)
    parser.add_argument("--stream", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
        if not isinstance(metadata, dict):
            raise ValueError("metadata must be a JSON object")
        report = validate(
            metadata,
            candidate_source=args.candidate_source,
            candidate_binary=args.candidate_binary,
            fixture_source=args.fixture_source,
            stream=args.stream,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_NATIVE_PROVENANCE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"NATIVE_PROVENANCE={report['status']}")
    print(f"ERRORS={len(report['errors'])}")
    return 0 if report["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
