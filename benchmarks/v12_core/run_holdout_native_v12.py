#!/usr/bin/env python3
"""Fixed-seed held-out family, W9/W23/W29, no tuning after first execution.

The V12 source emitter and benchmark policy were authored before this file.
This is not a secret blind independent replication or evidence of new math.
"""
from __future__ import annotations

import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
S3_ROOT = HERE.parents[2] / "S3"
sys.path.insert(0, str(S3_ROOT))
from bootstrap.s3.pipeline import compile_source, OptimizationLevel
from bootstrap.s3.gf2_ir_certificate import certify_gf2_ir, certified_gf2_fast_forward
from bootstrap.s3.gf2_dynamic_native import compile_certified_gf2_dynamic


def source_for_taps(w: int, taps: tuple[int, ...]) -> str:
    def term(k: int) -> str:
        if k == 0:
            return "x"
        return f"i64_or(i64_shl(x, {k}), i64_shr(x, {w-k}))"
    expr = term(taps[0])
    for k in taps[1:]:
        expr = f"i64_xor({expr}, {term(k)})"
    return (f"export fn update(x: i64) -> i64:\n"
            f"    return i64_and({expr}, {(1<<w)-1})\n\n"
            "export fn main() -> i64:\n    return 0\n")


def run():
    seed = 2026111407
    report = {
        "campaign": "S3_V12_FIXED_SEED_HELD_OUT_NATIVE_CASES",
        "seed": seed,
        "first_run_without_candidate_tuning": True,
        "independent_blind_replication": False,
        "scope": "three previously unused widths and five-tap cyclic GF2 maps",
        "gcc_reference": "independent C sparse multiplication; real S3 native x86",
        "cases": [],
    }
    with tempfile.TemporaryDirectory(prefix="s3_v12_holdout_") as td:
        harness = Path(td)/"compare_s3_native_v12"
        subprocess.run(
            ["gcc", "-O3", "-std=c11", "-Wall", "-Wextra", "-Werror",
             str(HERE/"compare_s3_native_v12.c"), "-o", str(harness), "-ldl"],
            check=True, capture_output=True, timeout=60,
        )
        for w in (9, 23, 29):
            rng = random.Random(seed + w)
            taps = tuple(sorted(rng.sample(range(w), 5)))
            src = source_for_taps(w, taps)
            ir, _ = compile_source(
                src, optimization=OptimizationLevel.O1, predictive_exact=False,
            ).require_ordinary_artifacts()
            cert = certify_gf2_ir(ir, "update", w)
            with (
                compile_certified_gf2_dynamic(
                    ir, cert, algorithm="generic", enable_experimental=True,
                ) as generic,
                compile_certified_gf2_dynamic(
                    ir, cert, algorithm="auto", enable_experimental=True,
                    codegen_variant="v11_baseline",
                ) as v11,
                compile_certified_gf2_dynamic(
                    ir, cert, algorithm="auto", enable_experimental=True,
                    codegen_variant="v12_sparse",
                ) as v12,
            ):
                assert v11.manifest.selected_algorithm == "GF2_CYCLIC_POLYNOMIAL"
                assert v12.manifest.selected_algorithm == v11.manifest.selected_algorithm
                so_files = [str(Path(k._temp.name)/"dynamic.so")
                            for k in (generic, v11, v12)]
                samples = []
                for n in (37, 10_001, 1_000_003):
                    raw = subprocess.check_output(
                        [str(harness), *so_files, str(w), str(cert.columns[0]),
                         str(n), "9", "1467813"], text=True, timeout=90,
                    )
                    sample = json.loads(raw)
                    assert sample["parity"]
                    samples.append(sample)
                    print(
                        f"HOLDOUT W={w} taps={taps} N={n} "
                        f"V11_NS={sample['median_ns']['s3_v11']:.1f} "
                        f"V12_NS={sample['median_ns']['s3_v12']:.1f} "
                        f"V11/V12={1/sample['v12_over_v11']:.2f} "
                        f"V12/GCC={sample['v12_over_gcc_sparse']:.2f}",
                        flush=True,
                    )
                report["cases"].append({
                    "width": w,
                    "taps": taps,
                    "polynomial": cert.columns[0],
                    "source_ir_sha256": cert.ir_sha256,
                    "certificate_sha256": cert.certificate_sha256,
                    "nonzero_at_n1m": bool(certified_gf2_fast_forward(
                        ir, cert, 1, 1_000_003,
                    )),
                    "samples": samples,
                })
    target = HERE/"results_holdout_native_v12.json"
    target.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("RESULT_FILE="+str(target), flush=True)


if __name__ == "__main__":
    run()
