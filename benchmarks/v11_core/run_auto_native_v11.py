#!/usr/bin/env python3
"""V11 native S3 automatic algorithm selection, identical source and proof.

Compiles 2 S3 x86-64 kernels with the same source-derived cert: generic
matrix and automatic exact circulant-specialized polynomial. The C11 harness
independently validates against direct Rule90 & known polynomial reference.
All results exploratory, no S3 defaults or production changed.
"""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))

from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.gf2_ir_certificate import certify_gf2_ir
from bootstrap.s3.gf2_algorithm_selection import select_certified_gf2_algorithm
from bootstrap.s3.gf2_dynamic_native import compile_certified_gf2_dynamic

WIDTHS=(8,16,32)
HORIZONS=(1,16,1000,1000000)
ROUNDS=9


def original_s3(w:int)->str:
    return f"""export fn update(x: i64) -> i64:
    mut left: i64 = i64_or(i64_shl(x, 1), i64_shr(x, {w-1}))
    mut right: i64 = i64_or(i64_shl(x, {w-1}), i64_shr(x, 1))
    return i64_and(i64_xor(left, right), {(1<<w)-1})

export fn main() -> i64:
    return 0
"""


def run():
    result={
        "campaign":"S3_V11_CORE_AUTOMATIC_GF2_ALGORITHM_SELECTION",
        "scientific_status":"EXPERIMENTAL_SOURCE_IR_CERTIFIED_AUTO_REPRESENTATION_CHOICE",
        "novel_algorithm_claim":False,
        "automatic_production_compiler_pass":False,
        "gpu_benchmark_included":False,
        "s3_backend":"S3 x86-64 assembly, GCC assembler/linker only",
        "c_reference":"GCC -O3 independent cyclic polynomial and direct N-step Rule90",
        "machine_session":"single Windows/WSL host; nine alternating rounds",
        "cases":[],
        "limitations":[
            "Only a restricted, structurally certified GF2 family, not a general automatic S3 algorithm discoverer.",
            "C cyclic specialist is known, not an S3 mathematical novelty.",
            "Raw native timings exclude Python proof checks; cold builds recorded.",
            "Submicrosecond references are susceptible to clock and optimizer noise.",
            "No claim of asymptotically better algorithm vs specialist; check W-scaling separately.",
        ]
    }
    with tempfile.TemporaryDirectory(prefix="s3_v11_auto_") as td:
        harness=Path(td)/"compare_s3_native_auto"
        subprocess.run(
            ["gcc","-O3","-std=c11","-Wall","-Wextra",str(HERE/"compare_s3_native_auto.c"),
             "-o",str(harness),"-ldl"],
            check=True,capture_output=True,text=True,timeout=60,
        )
        for w in WIDTHS:
            c=compile_source(original_s3(w),optimization=OptimizationLevel.O1,predictive_exact=False)
            ir,_=c.require_ordinary_artifacts()
            cert=certify_gf2_ir(ir,"update",w)
            auto=select_certified_gf2_algorithm(ir,cert,requested="auto")
            assert auto.selected=="GF2_CYCLIC_POLYNOMIAL"
            with (
                compile_certified_gf2_dynamic(ir,cert,enable_experimental=True,algorithm="generic") as generic,
                compile_certified_gf2_dynamic(ir,cert,enable_experimental=True,algorithm="auto") as selected,
            ):
                assert generic.manifest.selected_algorithm=="GF2_GENERIC_MATRIX"
                assert selected.manifest.selected_algorithm=="GF2_CYCLIC_POLYNOMIAL"
                gso=Path(generic._temp.name)/"dynamic.so"
                aso=Path(selected._temp.name)/"dynamic.so"
                samples=[]
                for n in HORIZONS:
                    out=subprocess.run(
                        [str(harness),str(gso),str(aso),str(w),str(n),str(ROUNDS),"1467813"],
                        check=True,capture_output=True,text=True,timeout=90,
                    )
                    row=json.loads(out.stdout.strip())
                    assert row["parity"]
                    samples.append(row)
                case={
                    "width":w,
                    "source_ir_sha256":cert.ir_sha256,
                    "proof_cert_sha256":cert.certificate_sha256,
                    "selection":auto.to_dict(),
                    "generic_native_build_ms":generic.manifest.compile_cold_end_to_end_ms,
                    "auto_native_build_ms":selected.manifest.compile_cold_end_to_end_ms,
                    "generic_native_smoke_checks":generic.manifest.native_smoke_checks,
                    "auto_native_smoke_checks":selected.manifest.native_smoke_checks,
                    "same_s3_binary_per_N_for_each_selected_algorithm":True,
                    "samples":samples,
                }
                result["cases"].append(case)
                last=samples[-1]
                print(f"W={w} N={last['N']} generic={last['median_ns']['s3_generic']:.1f}ns "
                      f"auto={last['median_ns']['s3_auto_selected']:.1f}ns "
                      f"gcc_specialist={last['median_ns']['gcc_cyclic_specialist']:.1f}ns "
                      f"auto/generic={last['auto_over_generic']:.3f}",flush=True)
    out=HERE/"results_auto_native_v11.json"
    out.write_text(json.dumps(result,indent=2),encoding="utf-8")
    print("RESULT_FILE="+str(out))


if __name__=="__main__":
    run()
