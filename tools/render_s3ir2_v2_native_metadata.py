"""Render native Stage1 semantic-run metadata from exact artifact files.

This helper reduces manual transcription risk. It computes hashes and byte sizes
for the candidate source/binary, fixture source, and emitted S3IR2 stream. The
output still must pass validate_s3ir2_v2_native_provenance.py before use.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def _facts(path: Path) -> tuple[str, int]:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def render(
    *,
    candidate_git_sha: str,
    candidate_source: Path,
    candidate_binary: Path,
    fixture_source: Path,
    stream: Path,
    control_revision: int,
    python_version: str,
    cc_path: str,
    build_exit_code: int,
    run_status: str,
    run_exit_code: int,
    os_name: str = "linux",
    arch: str = "x86_64",
) -> dict[str, object]:
    source_sha, source_bytes = _facts(candidate_source)
    binary_sha, binary_bytes = _facts(candidate_binary)
    fixture_sha, fixture_bytes = _facts(fixture_source)
    stream_sha, stream_bytes = _facts(stream)
    return {
        "schema": "s3.stage1.native-semantic-evidence.v1",
        "candidate_git_sha": candidate_git_sha,
        "candidate_source_sha256": source_sha,
        "candidate_source_bytes": source_bytes,
        "candidate_binary_sha256": binary_sha,
        "candidate_binary_bytes": binary_bytes,
        "fixture_source_sha256": fixture_sha,
        "fixture_source_bytes": fixture_bytes,
        "stream_sha256": stream_sha,
        "stream_bytes": stream_bytes,
        "platform": {
            "os": os_name,
            "arch": arch,
            "python": python_version,
            "cc": cc_path,
        },
        "build": {
            "status": "PASS" if build_exit_code == 0 else "FAIL",
            "exit_code": build_exit_code,
        },
        "run": {
            "status": run_status,
            "exit_code": run_exit_code,
        },
        "control_revision": control_revision,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-git-sha", required=True)
    parser.add_argument("--candidate-source", type=Path, required=True)
    parser.add_argument("--candidate-binary", type=Path, required=True)
    parser.add_argument("--fixture-source", type=Path, required=True)
    parser.add_argument("--stream", type=Path, required=True)
    parser.add_argument("--control-revision", type=int, required=True)
    parser.add_argument("--python-version", required=True)
    parser.add_argument("--cc-path", required=True)
    parser.add_argument("--build-exit-code", type=int, default=0)
    parser.add_argument("--run-status", choices=["PASS", "FAIL", "BLOCKED"], required=True)
    parser.add_argument("--run-exit-code", type=int, required=True)
    parser.add_argument("--os", dest="os_name", default="linux")
    parser.add_argument("--arch", default="x86_64")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        metadata = render(
            candidate_git_sha=args.candidate_git_sha,
            candidate_source=args.candidate_source,
            candidate_binary=args.candidate_binary,
            fixture_source=args.fixture_source,
            stream=args.stream,
            control_revision=args.control_revision,
            python_version=args.python_version,
            cc_path=args.cc_path,
            build_exit_code=args.build_exit_code,
            run_status=args.run_status,
            run_exit_code=args.run_exit_code,
            os_name=args.os_name,
            arch=args.arch,
        )
    except OSError as error:
        parser.exit(2, f"S3IR2_NATIVE_METADATA_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"OUTPUT={args.output}")
    print(f"BUILD={metadata['build']['status']}")
    print(f"RUN={metadata['run']['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
