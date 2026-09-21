#!/usr/bin/env python3
"""Run the bounded RMSD correctness gate against one immutable S3 checkout."""

from __future__ import annotations

import math
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from protocol.provenance import require_commit


EXPECTED_S3_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"


def main() -> int:
    s3_repo = Path(os.environ.get("S3_REPO", r"C:\Users\samue\Downloads\S3\S3-native-semantic-execution")).resolve()
    require_commit(s3_repo, os.environ.get("S3_COMMIT", EXPECTED_S3_SHA), label="S3 candidate")
    sys.path.insert(0, str(s3_repo))
    from bootstrap.s3.pipeline import compile_source, run_source

    source = (ROOT / "benchmarks/scientific/rmsd/rmsd.s3").read_text(encoding="utf-8")
    expected = math.sqrt(14.0 / 3.0)
    for optimization in ("O0", "O1"):
        compilation = compile_source(source, optimization=optimization)
        observed = run_source(source, optimization=optimization)
        if not math.isclose(observed, expected, rel_tol=1e-12, abs_tol=1e-12):
            raise SystemExit(f"RMSD correctness failure for {optimization}: {observed!r}")
        if not any(
            getattr(instruction, "callee", None) == "sqrt"
            for function in compilation.assembly.functions
            for instruction in function.instructions
        ):
            raise SystemExit(f"RMSD sqrt call missing for {optimization}")
    print("RMSD_SINGLE_CORRECTNESS=PASS")
    print("RMSD_EXPECTED=2.160246899469287")
    print(f"S3_CANDIDATE_SHA={os.environ.get('S3_COMMIT', EXPECTED_S3_SHA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
