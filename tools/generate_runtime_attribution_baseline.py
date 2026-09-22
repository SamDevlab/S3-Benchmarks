"""Generate only the pinned S3 XSBench assembly for attribution evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmarks.scientific.xsbench.contract import s3_source
from tools.ffi_direct_kernel_methodology import S3_FFI_MAX_INSTRUCTIONS, _activate_s3_modules


EXPECTED_S3_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generate(s3_repo: Path, output: Path) -> dict[str, object]:
    pipeline = _activate_s3_modules(s3_repo)
    from bootstrap.s3.backends.x86_64 import generate_ffi_assembly

    output.mkdir(parents=True, exist_ok=True)
    records: dict[str, object] = {}
    for optimization in ("O0", "O1"):
        compilation = pipeline.compile_source(s3_source(), optimization)
        _, ordinary = compilation.require_ordinary_artifacts()
        assembly = generate_ffi_assembly(ordinary, max_instructions=S3_FFI_MAX_INSTRUCTIONS)
        path = output / f"scientific-xsbench-compatible_lookup-medium-S3_FFI_{optimization}.s"
        path.write_text(assembly, encoding="utf-8", newline="\n")
        records[optimization] = {
            "path": str(path),
            "sha256": _sha256(path),
            "bytes": path.stat().st_size,
            "s3_sha": EXPECTED_S3_SHA,
            "max_instructions": S3_FFI_MAX_INSTRUCTIONS,
        }
    manifest = output / "reproduction.json"
    manifest.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(generate(args.s3_repo, args.output), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
