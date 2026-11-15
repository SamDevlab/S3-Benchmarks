#!/usr/bin/env python3
"""V10.3 independent C harness vs genuine dynamic S3 x86-64 kernel.

Build once per WIDTH, then execute N={...} with the SAME S3 shared library.
The strongest known cyclic polynomial reference is included. Reports cold
certification/build costs, raw native timing, and checked Python API latency
separately. No S3 compiler modifications or production promotion.
"""
from __future__ import annotations

import json
from pathlib import Path
import statistics
import subprocess
import sys
import tempfile
from time import perf_counter_ns

HERE = Path(__file__).resolve().parent
S3_ROOT = HERE.parents[2] / "S3"
sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.pipeline import OptimizationLevel, compile_source
from bootstrap.s3.gf2_ir_certificate import certify_gf2_ir, certified_gf2_fast_forward
from bootstrap.s3.gf2_dynamic_native import compile_certified_gf2_dynamic

N_VALUES = (0, 1, 10, 100, 1000, 10000, 100000, 1000000)
WIDTHS = (8, 16)


def original_s3(width):
    return f"""export fn update(x: i64) -> i64:
    mut left: i64 = i64_or(i64_shl(x, 1), i64_shr(x, {width-1}))
    mut right: i64 = i64_or(i64_shl(x, {width-1}), i64_shr(x, 1))
    return i64_and(i64_xor(left, right), {(1<<width)-1})

export fn main() -> i64:
    return 0
"""


def run():
    report = {
        "campaign": "S3_V10_3_GF2_DYNAMIC_N_NATIVE_VS_SPECIALIST",
        "status": "EXPERIMENTAL_NATIVE_BENCHMARK_ONLY",
        "source": str(HERE / "native_gf2_dynamic_harness.c"),
        "methods": {
            "S3": "S3-generated x86-64 dynamic GF2 matrix powering (raw native symbol)",
            "SPECIALIST": "Independent GCC -O3 cyclic polynomial repeated squaring",
            "MATCHED_GENERIC_C": "Independent GCC -O3 same GF2 matrix column squaring algorithm as S3",
            "ITERATIVE": "Independent GCC -O3 direct Rule 90 recurrence",
            "CHECKED_API": "Python public S3 dynamic wrapper verifies original IR proof per call; measured separately",
        },
        "known_algorithm_novelty": "NONE_CLAIMED",
        "s3_native_assembly": True,
        "s3_compiler_default_changed": False,
        "assumptions": "Fixed width W=8 or 16; runtime dynamic N>=0 i64; GF2 linear circulant Rule90",
        "caveats": [
            "One CPU/WSL host and one measurement session; nine alternating rounds, high sensitivity for short kernels.",
            "Native kernel raw timing intentionally bypasses proof gate; public checked API has additional cost.",
            "Warm kernel latency excludes compilation and discovery/proof overhead, reported separately.",
            "C specialized cyclic polynomial algorithm is stronger than a naive direct loop reference.",
            "IR checker proof and tested machine behavior are not a full formal verified compiler.",
        ],
        "cases": [],
    }
    with tempfile.TemporaryDirectory(prefix="s3_v10_dyn_bench_") as temp:
        executable = Path(temp) / "native_gf2_dynamic_bench"
        subprocess.run(
            ["gcc", "-O3", "-std=c11", "-Wall", "-Wextra",
             str(HERE / "native_gf2_dynamic_harness.c"), "-o", str(executable), "-ldl"],
            check=True, capture_output=True, text=True, timeout=60,
        )
        for width in WIDTHS:
            source = original_s3(width)
            start=perf_counter_ns()
            compiled=compile_source(
                source, optimization=OptimizationLevel.O1,
                predictive_exact=False,
            )
            ir,_=compiled.require_ordinary_artifacts()
            after_ir=(perf_counter_ns()-start)/1e6
            start=perf_counter_ns()
            certificate=certify_gf2_ir(ir,"update",width)
            certify_ms=(perf_counter_ns()-start)/1e6
            with compile_certified_gf2_dynamic(ir,certificate,enable_experimental=True) as kernel:
                shared_object=Path(kernel._temp.name)/"dynamic.so"
                assert shared_object.exists()
                samples=[]
                checked_times={}
                for n in N_VALUES:
                    completed=subprocess.run(
                        [str(executable),str(shared_object),str(width),str(n),"9","3039184"],
                        check=True, capture_output=True, text=True, timeout=90,
                    )
                    item=json.loads(completed.stdout.strip())
                    assert item["parity"]
                    item["s3_vs_c_specialist_ratio"] = round(
                        item["median_ns"]["s3_dynamic_native_raw"]/
                        item["median_ns"]["cyclic_specialist_c"], 4)
                    item["s3_vs_c_direct_speedup"] = round(
                        item["median_ns"]["iterative_c"]/
                        item["median_ns"]["s3_dynamic_native_raw"], 4)
                    item["s3_vs_matched_generic_c_ratio"] = round(
                        item["median_ns"]["s3_dynamic_native_raw"]/
                        item["median_ns"]["generic_matrix_c"], 4)
                    samples.append(item)
                    if n in (0,100,1000000):
                        measured=[]
                        for i in range(31):
                            state=(17+i*73)&((1<<width)-1)
                            t=perf_counter_ns()
                            x=kernel.run(state,n)
                            measured.append(perf_counter_ns()-t)
                            assert x==certified_gf2_fast_forward(ir,certificate,state,n)
                        checked_times[str(n)] = statistics.median(measured)
                case={
                    "width":width,
                    "same_s3_shared_object_for_all_N":True,
                    "certificate_method":certificate.certification_method,
                    "certificate_ir_sha256":certificate.ir_sha256,
                    "source_ir_compilation_ms":round(after_ir,4),
                    "certificate_derivation_ms":round(certify_ms,4),
                    "dynamic_native_build_and_smoke_ms":kernel.manifest.compile_cold_end_to_end_ms,
                    "native_smoke_checks":kernel.manifest.native_smoke_checks,
                    "native_generated_source_sha256":kernel.manifest.generated_s3_sha256,
                    "native_assembly_sha256":kernel.manifest.emitted_assembly_sha256,
                    "native_binary_sha256":kernel.manifest.native_shared_object_sha256,
                    "checked_python_public_api_ns":checked_times,
                    "samples":samples,
                }
                report["cases"].append(case)
                last=samples[-1]
                print("WIDTH",width,"SAME_SO_ALL_N",case["same_s3_shared_object_for_all_N"],
                      "BUILD_MS",case["dynamic_native_build_and_smoke_ms"],
                      "N1M_NATIVE_NS",last["median_ns"]["s3_dynamic_native_raw"],
                      "N1M_SPECIALIST_NS",last["median_ns"]["cyclic_specialist_c"],
                      "N1M_GENERIC_GCC_NS",last["median_ns"]["generic_matrix_c"],
                      "S3_SPECIALIST_RATIO",last["s3_vs_c_specialist_ratio"],
                      "S3_GENERIC_GCC_RATIO",last["s3_vs_matched_generic_c_ratio"],flush=True)
    out=HERE/"native_gf2_dynamic_results_v10_3.json"
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("OUTPUT",out)


if __name__ == "__main__":
    run()
