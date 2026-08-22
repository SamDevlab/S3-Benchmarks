"""Compile one pinned S3 native workload in a process-isolated child."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-root", type=Path, required=True)
    parser.add_argument("--s3-sha", required=True)
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--workload-id", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    # Keep benchmark packages ahead of the S3 checkout; both repositories have
    # a top-level ``benchmarks`` namespace, while bootstrap must come from S3.
    sys.path.insert(0, str(args.s3_root.resolve()))
    sys.path.insert(0, str(BASE_DIR))
    from benchmarks.rc1.native_workloads import NATIVE_WORKLOADS
    from tools.artifacts import require_provenance
    from tools.assembly_analyzer import analyze_assembly_text
    from tools.runner import build_native_artifact
    from bootstrap.s3.backends.x86_64 import NativeToolchain, generate_native_assembly
    from bootstrap.s3.pipeline import compile_source

    provenance = require_provenance(
        s3_repo=args.s3_root.resolve(),
        requested_s3_sha=args.s3_sha,
        benchmark_repo=BASE_DIR,
        requested_benchmark_sha=args.benchmark_sha,
    )
    workload = next((item for item in NATIVE_WORKLOADS if item.workload_id == args.workload_id), None)
    if workload is None:
        raise SystemExit(f"unknown native workload: {args.workload_id}")
    toolchain = NativeToolchain.detect()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=False)
    source_path = output_dir / "source.s3"
    source_path.write_text(workload.s3_source, encoding="utf-8", newline="\n")
    records: dict[str, dict[str, object]] = {}
    for optimization in ("O0", "O1"):
        variant_dir = output_dir / optimization
        variant_dir.mkdir()
        assembly = generate_native_assembly(
            compile_source(workload.s3_source, optimization).assembly,
            max_instructions=(1 << 62),
        )
        assembly_path = variant_dir / "program.s"
        assembly_path.write_text(assembly, encoding="utf-8", newline="\n")
        executable = variant_dir / "program"
        object_path, commands = build_native_artifact(assembly_path, executable, toolchain.compiler)
        metrics = analyze_assembly_text(assembly, f"{args.checkpoint}-{args.workload_id}-{optimization}", executable).__dict__
        records[optimization] = {
            "assembly": str(assembly_path),
            "object": str(object_path),
            "executable": str(executable),
            "assembly_sha256": hashlib.sha256(assembly.encode("utf-8")).hexdigest(),
            "executable_sha256": _sha256_file(executable),
            "commands": commands,
            "metrics": metrics,
        }
    manifest = {
        "schema": "s3.rc1.native-workload-artifacts.v1",
        "checkpoint": args.checkpoint,
        "workload_id": workload.workload_id,
        "workload_name": workload.name,
        "source_sha256": hashlib.sha256(workload.s3_source.encode("utf-8")).hexdigest(),
        "operations_per_run": workload.operations_per_run,
        "provenance": provenance,
        "records": records,
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"checkpoint": args.checkpoint, "workload": workload.workload_id, "status": "PASS"}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
