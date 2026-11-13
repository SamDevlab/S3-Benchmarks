"""Compile one pinned S3 checkpoint in a process isolated from other SHAs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]


def sha256_file(path: Path) -> str:
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
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--fixture", action="append", required=True)
    parser.add_argument("--parses", type=int, default=10000)
    args = parser.parse_args()

    if str(args.s3_root) not in sys.path:
        sys.path.insert(0, str(args.s3_root.resolve()))
    sys.path.insert(0, str(BASE_DIR))
    from tools.artifacts import require_provenance
    from tools.runner import build_native_artifact, generate_native_assembly, render_s3_loop_source
    from bootstrap.s3.backends.x86_64 import NativeToolchain
    from bootstrap.s3.pipeline import compile_source
    from tools.assembly_analyzer import analyze_assembly_text

    provenance = require_provenance(
        s3_repo=args.s3_root.resolve(),
        requested_s3_sha=args.s3_sha,
        benchmark_repo=BASE_DIR,
        requested_benchmark_sha=args.benchmark_sha,
    )
    toolchain = NativeToolchain.detect()
    template = args.template.read_text(encoding="utf-8")
    args.output_dir.mkdir(parents=True, exist_ok=False)
    records: list[dict[str, object]] = []
    for fixture_arg in args.fixture:
        fixture_path = Path(fixture_arg).resolve()
        fixture_id = fixture_path.stem
        text = fixture_path.read_text(encoding="utf-8")
        source = render_s3_loop_source(template, text, args.parses)
        fixture_dir = args.output_dir / fixture_id
        fixture_dir.mkdir()
        source_path = fixture_dir / "source.s3"
        source_path.write_text(source, encoding="utf-8", newline="\n")
        variants: dict[str, dict[str, object]] = {}
        for optimization in ("O0", "O1"):
            variant_dir = fixture_dir / optimization
            variant_dir.mkdir()
            assembly = generate_native_assembly(
                compile_source(source, optimization).assembly,
                max_instructions=(1 << 62),
            )
            assembly_path = variant_dir / "program.s"
            assembly_path.write_text(assembly, encoding="utf-8", newline="\n")
            executable = variant_dir / "program"
            object_path, commands = build_native_artifact(assembly_path, executable, toolchain.compiler)
            metrics = analyze_assembly_text(assembly, f"{args.checkpoint}-{optimization}", executable).__dict__
            variants[optimization] = {
                "assembly": str(assembly_path),
                "object": str(object_path),
                "executable": str(executable),
                "assembly_sha256": hashlib.sha256(assembly.encode("utf-8")).hexdigest(),
                "executable_sha256": sha256_file(executable),
                "commands": commands,
                "metrics": metrics,
            }
        records.append({"fixture": fixture_id, "input_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "variants": variants})
    payload = {
        "schema": "s3.rc1.s3-checkpoint-artifacts.v1",
        "checkpoint": args.checkpoint,
        "provenance": provenance,
        "parses_per_sample": args.parses,
        "records": records,
    }
    (args.output_dir / "manifest.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"checkpoint": args.checkpoint, "status": "PASS", "fixtures": len(records)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

