#!/usr/bin/env python3
"""V12 non-GF2 exact checked-i64 progression to genuine S3 x86-64.

Algorithm-matched C reference, original S3 N-step runtime, and
proof-gated S3-native closed form. Honest cold compile and per-call
Python proof cost reported separately. No automatic default promotion.
"""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
import statistics
import subprocess
import sys
import tempfile
from time import perf_counter_ns

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))

from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.backends.x86_64 import X8664Backend
from bootstrap.s3.verified_i64_progression import certify_i64_progression_ir
from bootstrap.s3.verified_i64_native import compile_certified_i64_native


SOURCE="""export fn update(x: i64) -> i64:
    return x + 7

export fn main() -> i64:
    return 0
"""


def main():
    t0=perf_counter_ns()
    original=compile_source(SOURCE,optimization=OptimizationLevel.O0,predictive_exact=False)
    ir,asm=original.require_ordinary_artifacts()
    ir_compile_ms=(perf_counter_ns()-t0)/1e6
    t0=perf_counter_ns()
    cert=certify_i64_progression_ir(ir,"update")
    proof_ms=(perf_counter_ns()-t0)/1e6
    assert cert.delta==7
    with tempfile.TemporaryDirectory(prefix="s3_v12_i64_bench_") as td:
        root=Path(td)
        orig_asm=X8664Backend.scientific(max_instructions=1_000_000)._generate_ffi(asm)
        (root/"original.s").write_text(orig_asm,encoding="utf-8")
        original_so=root/"original.so"
        subprocess.run(
            ["gcc","-shared","-fPIC","-O2",str(root/"original.s"),"-o",str(original_so)],
            check=True,capture_output=True,text=True,timeout=120,
        )
        harness=root/"harness"
        subprocess.run(
            ["gcc","-O3","-std=c11","-Wall","-Wextra",
             str(HERE/"compare_i64_progression_v12.c"),"-o",str(harness),"-ldl"],
            check=True,capture_output=True,text=True,timeout=120,
        )
        with compile_certified_i64_native(ir,cert,enable_experimental=True) as optimized:
            optimized_so=Path(optimized._temp.name)/"native.so"
            rows=[]
            for n in (0,1,100,10_000,1_000_000):
                proc=subprocess.run(
                    [str(harness),str(original_so),str(optimized_so),"7",
                     str(n),"9","103"],
                    check=True,capture_output=True,text=True,timeout=120,
                )
                row=json.loads(proc.stdout.strip())
                assert row["parity"]
                rows.append(row)
                print("I64_S3_NATIVE_PROGRESSION",n,
                      "ORIGINAL_NS",row["median_ns"]["original_s3_n_steps"],
                      "S3_CLOSED_NS",row["median_ns"]["verified_native_s3_formula"],
                      "GCC_CLOSED_NS",row["median_ns"]["independent_gcc_formula"],
                      flush=True)
            checked=[]
            for i in range(31):
                t=perf_counter_ns()
                result=optimized.run(100+i,1_000_000)
                checked.append(perf_counter_ns()-t)
                assert result==100+i+7_000_000
            report={
                "campaign":"S3_V12_VERIFIED_CHECKED_I64_NATIVE_PROGRESSIONS",
                "status":"EXPERIMENTAL_S3_NATIVE_VERIFIED_NON_GF2_ALGORITHM",
                "algorithm_family":"MONOTONIC_SIGNED_I64_ARITHMETIC_PROGRESSION",
                "source_ir_proof":True,"blackbox_inference_used":False,
                "s3_native_backend_used":True,"gcc_role":"ASSEMBLER_LINKER_AND_INDEPENDENT_C_REFERENCE",
                "automatic_production_promotion":False,
                "source_ir_sha256":cert.ir_sha256,
                "certificate_sha256":cert.certificate_sha256,
                "delta":cert.delta,
                "original_compile_ms":round(ir_compile_ms,5),
                "certificate_proof_ms":round(proof_ms,5),
                "specialized_cold_build_ms":optimized.manifest.cold_build_ms,
                "native_smoke_checks":optimized.manifest.smoke_checks,
                "protected_python_api_median_ns":statistics.median(checked),
                "original_s3_assembly_sha256":sha256(orig_asm.encode()).hexdigest(),
                "native_shortcut_assembly_sha256":optimized.manifest.assembly_sha256,
                "samples":rows,
                "limitations":[
                    "Original i64 N-step S3 vs verified single-formula S3 changes O(N) to O(1) for this known progression; not a new algorithm.",
                    "Both native S3 symbols used direct C ABI benchmark without Python proof-check overhead; protected API reported separately.",
                    "No general checked-i64 affine optimization, only monotone same-sign progression and explicit overflow guards.",
                    "N=1e6 timing is not end-to-end cold-build amortized; cold/proof costs reported separately.",
                    "Single host, nine rotating native rounds, unusually small GCC formula times sensitive to noise.",
                ],
            }
    out=HERE/"i64_progression_results_v12.json"
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("OUTPUT",out)


if __name__=="__main__":
    main()
