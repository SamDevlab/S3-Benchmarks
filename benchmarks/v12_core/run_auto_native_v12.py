#!/usr/bin/env python3
"""V12 guarded x86 native measurement: same certificate, distinct S3 codegen.

Preserves the V11 samples. Records standalone GCC matched/sparse references,
non-nilpotent GF2 programs, assembly instruction statistics, and cold builds.
Results are one-host exploratory measurements, not an automated production
dispatch policy or a proof of machine-code correctness.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
S3_ROOT = HERE.parents[2] / "S3"
sys.path.insert(0, str(S3_ROOT))
from bootstrap.s3.pipeline import compile_source, OptimizationLevel
from bootstrap.s3.gf2_ir_certificate import certify_gf2_ir, certified_gf2_fast_forward
from bootstrap.s3.gf2_dynamic_native import compile_certified_gf2_dynamic

ROUNDS = 9


def original_s3(w: int, family: str) -> str:
    mask = (1 << w) - 1
    def rot(k: int) -> str:
        return f"i64_or(i64_shl(x, {k}), i64_shr(x, {w-k}))"
    if family == "rule90":
        expr = f"i64_xor({rot(1)}, {rot(w-1)})"
    elif family == "invertible":
        expr = f"i64_xor(i64_xor(x, {rot(1)}), {rot(3)})"
    elif family == "rotation":
        expr = rot(1)
    else:
        raise ValueError(family)
    return (f"export fn update(x: i64) -> i64:\n"
            f"    return i64_and({expr}, {mask})\n\n"
            "export fn main() -> i64:\n    return 0\n")


def assembly_profile(shared: Path) -> dict:
    lines = subprocess.check_output(
        ["objdump", "-d", "-Mintel", str(shared)], text=True,
        timeout=30, errors="replace",
    ).splitlines()
    ins = [s for s in lines if re.match(r"^\s*[0-9a-f]+:\s+[0-9a-f]{2}", s)]
    asm = "\n".join(ins)
    instructions = [
        (re.search(r"\s([a-z][a-z0-9]*)\s", x).group(1)
         if re.search(r"\s([a-z][a-z0-9]*)\s", x) else "")
        for x in ins
    ]
    return {
        "total_disassembled_instructions_including_plt": len(ins),
        "static_branch_instructions": sum(op.startswith("j") for op in instructions),
        "static_call_instructions": sum(op == "call" for op in instructions),
        "assembly_lines": len(lines),
        "shared_library_bytes": shared.stat().st_size,
        "instruction_count_is_dynamic": False,
        "scope": "entire shared object (includes ELF scaffolding), not workload",
    }


def run(quick: bool):
    cases = ([("rule90", 8), ("invertible", 31)] if quick else
             [("rule90", 8), ("rule90", 16), ("rule90", 32),
              ("rotation", 8), ("rotation", 31),
              ("invertible", 8), ("invertible", 16), ("invertible", 31)])
    horizons = (1, 1_000_003) if quick else (1, 64, 4096, 1_000_003)
    result = {
        "campaign": "S3_V12_CORE_NATIVE_CODEGEN_QUALIFICATION",
        "scientific_status": "EXPERIMENTAL_NOT_PRODUCTION",
        "algorithmic_novelty": False,
        "s3_native_assembly": True,
        "gcc_role_for_s3": "ASSEMBLE_AND_LINK_ONLY",
        "compiler_levels": {"s3": "O1", "c_reference": "GCC -O3"},
        "measurement_scope": "native execution only; certificate validation and cold build separately recorded",
        "machine_session": "one Windows/WSL GCC x86-64 host",
        "rounds": ROUNDS,
        "cases": [],
        "limits": [
            "S3 O1 vs C GCC O3: comparison does not isolate only register allocation.",
            "Instruction counts describe disassembled shared libraries, not dynamic PMU counts.",
            "C algorithm-matched scan and C sparse reference separate algorithm/codegen factors.",
            "Rule90 on power-of-two widths is nilpotent in W/2 steps.",
            "Power-of-two cyclic GF2 operators have special periodicity; include W31 holdout.",
            "Submicrosecond GCC timings may be noisy: no universal GPU/CPU or codegen speed claims.",
        ],
    }
    with tempfile.TemporaryDirectory(prefix="s3_v12_core_bench_") as td:
        harness = Path(td) / "compare_s3_native_v12"
        subprocess.run(
            ["gcc", "-O3", "-std=c11", "-Wall", "-Wextra", "-Werror",
             str(HERE / "compare_s3_native_v12.c"), "-o", str(harness), "-ldl"],
            check=True, capture_output=True, text=True, timeout=45,
        )
        for family, width in cases:
            product = compile_source(
                original_s3(width, family), optimization=OptimizationLevel.O1,
                predictive_exact=False,
            )
            module, _ = product.require_ordinary_artifacts()
            cert = certify_gf2_ir(module, "update", width)
            with (
                compile_certified_gf2_dynamic(
                    module, cert, algorithm="generic", enable_experimental=True,
                ) as generic,
                compile_certified_gf2_dynamic(
                    module, cert, algorithm="auto", enable_experimental=True,
                    codegen_variant="v11_baseline",
                ) as v11,
                compile_certified_gf2_dynamic(
                    module, cert, algorithm="auto", enable_experimental=True,
                    codegen_variant="v12_sparse",
                ) as v12,
            ):
                assert v11.manifest.selected_algorithm == "GF2_CYCLIC_POLYNOMIAL"
                assert v12.manifest.selected_algorithm == v11.manifest.selected_algorithm
                libraries = [
                    Path(k._temp.name) / "dynamic.so" for k in (generic, v11, v12)
                ]
                row = {
                    "family": family,
                    "width": width,
                    "polynomial": cert.columns[0],
                    "source_ir_sha256": cert.ir_sha256,
                    "certificate_sha256": cert.certificate_sha256,
                    "nonzero_output_at_large_horizon": bool(
                        certified_gf2_fast_forward(module, cert, 1, 1_000_003)
                    ),
                    "assembly": {
                        name: assembly_profile(library)
                        for name, library in zip(("s3_generic", "s3_v11", "s3_v12"), libraries)
                    },
                    "cold_build_ms": {
                        name: kernel.manifest.compile_cold_end_to_end_ms
                        for name, kernel in zip(("s3_generic", "s3_v11", "s3_v12"), (generic, v11, v12))
                    },
                    "samples": [],
                }
                for horizon in horizons:
                    args = [str(harness)] + [str(f) for f in libraries] + [
                        str(width), str(cert.columns[0]), str(horizon),
                        str(ROUNDS), "1467813",
                    ]
                    sample = json.loads(subprocess.check_output(
                        args, text=True, timeout=90,
                    ).strip())
                    assert sample["parity"] and sample["checks"] == 64
                    row["samples"].append(sample)
                    print(
                        f"FAMILY={family} W={width} N={horizon} "
                        f"V11_NS={sample['median_ns']['s3_v11']:.2f} "
                        f"V12_NS={sample['median_ns']['s3_v12']:.2f} "
                        f"C_MATCH_NS={sample['median_ns']['gcc_matched_scan']:.2f} "
                        f"RATIO={sample['v12_over_v11']:.3f}",
                        flush=True,
                    )
                result["cases"].append(row)
    target = HERE / ("results_auto_native_v12_quick.json" if quick
                     else "results_auto_native_v12.json")
    target.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"RESULT_FILE={target}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true",
                        help="two-case W8/W31 correctness and measurement smoke")
    run(parser.parse_args().quick)
