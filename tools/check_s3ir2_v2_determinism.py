"""Check exact-byte determinism for repeated S3IR2 v2 outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from tools.ingest_s3ir2_v2 import ingest


def check(paths: list[Path]) -> dict[str, object]:
    if len(paths) < 2:
        raise ValueError("need at least two streams")
    runs: list[dict[str, object]] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        report = ingest(text)
        runs.append({
            "path": str(path),
            "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "bytes": len(text.encode("utf-8")),
            "mask": report["completeness_mask"],
            "structural_status": report["structural_status"],
            "record_counts": report["record_counts"],
        })
    exact = len({str(run["sha256"]) for run in runs}) == 1
    structural = all(run["structural_status"] == "PASS" for run in runs)
    masks = len({int(run["mask"]) for run in runs}) == 1
    counts = len({json.dumps(run["record_counts"], sort_keys=True) for run in runs}) == 1
    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-determinism.v1",
        "run_count": len(runs),
        "runs": runs,
        "exact_bytes_identical": exact,
        "all_structurally_valid": structural,
        "all_masks_equal": masks,
        "all_record_counts_equal": counts,
        "status": "PASS" if exact and structural and masks and counts else "FAIL",
        "semantic_correctness_effect": "NONE",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("streams", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = check(args.streams)
    except (OSError, ValueError) as error:
        parser.exit(2, f"S3IR2_DETERMINISM_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"STATUS={report['status']}")
    return 0 if report["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
