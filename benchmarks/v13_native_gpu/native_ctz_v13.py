#!/usr/bin/env python3
"""V13 same-host real S3 native V12-vs-V13 and independent GCC controls.

Reuses the V12 C harness: its 's3_v11' slot is V12 and its 's3_v12'
slot is V13, with explicit remapping of field names. Do not mistake
C GCC O3 as codegen-matched optimization level for S3 O1.
"""
from __future__ import annotations
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))
from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.gf2_ir_certificate import certify_gf2_ir,certified_gf2_fast_forward
from bootstrap.s3.gf2_dynamic_native import compile_certified_gf2_dynamic

CASES=[
    ("rule90",8,(1,7)),("rule90",32,(1,31)),
    ("invertible",16,(0,1,3)),("invertible",31,(0,1,3)),
    ("five_tap_holdout",9,(0,2,3,5,7)),
    ("five_tap_holdout",23,(1,11,12,16,21)),
    ("five_tap_holdout",29,(11,14,19,25,27)),
]
HORIZONS=(1,64,4096,1000003)

def source_for(width,taps):
    def rot(k):
        if k==0:return "x"
        return f"i64_or(i64_shl(x, {k}), i64_shr(x, {width-k}))"
    expr=rot(taps[0])
    for off in taps[1:]:
        expr=f"i64_xor({expr}, {rot(off)})"
    return (f"export fn update(x: i64) -> i64:\n"
            f"    return i64_and({expr}, {(1<<width)-1})\n\n"
            "export fn main() -> i64:\n    return 0\n")

def assembly_stats(shared):
    output=subprocess.check_output(
        ["objdump","-d","-Mintel",str(shared)],
        text=True,errors="replace",timeout=35,
    )
    symbol=None
    symbols={}
    for line in output.splitlines():
        match=re.match(r"^[0-9a-f]+ <([^>]+)>:$",line.strip())
        if match:
            symbol=match.group(1)
            symbols.setdefault(symbol,[])
        elif symbol is not None and re.match(r"^\s*[0-9a-f]+:\s+",line):
            parts=line.split("\t")
            if len(parts)>2:
                opcode=parts[-1].strip().split(" ",1)[0]
                symbols[symbol].append(opcode)
    target={k:v for k,v in symbols.items() if
        any(s in k for s in ("gf2_","certified_step_dynamic"))}
    counts={k:{"instructions":len(v),
               "branches":sum(i.startswith("j") for i in v),
               "calls":sum(i.startswith("call") for i in v),
               "bsf":sum(i.startswith("bsf") for i in v),
               "idiv":sum(i.startswith("idiv") for i in v),
               "mov":sum(i.startswith("mov") for i in v)}
            for k,v in target.items()}
    return {"hot_symbols":counts,
            "hot_instructions_including_helpers":sum(v["instructions"] for v in counts.values()),
            "whole_shared_object_instructions":sum(len(v) for v in symbols.values()),
            "scope":"static disassembly, not retired/dynamic PMU instructions",
            "shared_object_bytes":shared.stat().st_size}

def run(quick=False):
    cases=CASES[:2] if quick else CASES
    horizons=(1,1000003) if quick else HORIZONS
    report={
        "campaign":"S3_V13_CTZ_NATIVE_CODEGEN_AND_ASSEMBLY",
        "status":"ONE_HOST_EXPERIMENTAL_NO_PRODUCTION",
        "source_of_truth":"S3 source IR and certificate",
        "s3_compiler":"O1, S3 native x86-64 assembly",
        "s3_gcc_role":"assembler/linker only",
        "c_references":"GCC O3 full scan and GCC O3 sparse C; not matched optimization level",
        "measurements_include_compilation":False,
        "cpu_pmu_available":False,
        "rounds":9,"cases":[],
    }
    with tempfile.TemporaryDirectory(prefix="s3_v13_native_") as td:
        bench=Path(td)/"bench_v12_v13"
        subprocess.run([
            "gcc","-O3","-std=c11","-Wall","-Wextra","-Werror",
            str(HERE.parent/"v12_core"/"compare_s3_native_v12.c"),
            "-o",str(bench),"-ldl"
        ],check=True,capture_output=True,timeout=60)
        for family,width,taps in cases:
            ir,_=compile_source(
                source_for(width,taps),
                optimization=OptimizationLevel.O1,predictive_exact=False,
            ).require_ordinary_artifacts()
            cert=certify_gf2_ir(ir,"update",width)
            with (
                compile_certified_gf2_dynamic(
                    ir,cert,enable_experimental=True,algorithm="generic") as generic,
                compile_certified_gf2_dynamic(
                    ir,cert,enable_experimental=True,algorithm="auto",
                    codegen_variant="v12_sparse") as v12,
                compile_certified_gf2_dynamic(
                    ir,cert,enable_experimental=True,algorithm="auto",
                    codegen_variant="v13_ctz") as v13,
            ):
                assert v13.manifest.codegen_variant=="v13_ctz"
                libs=[Path(x._temp.name)/"dynamic.so" for x in (generic,v12,v13)]
                row={
                    "family":family,"width":width,"taps":taps,
                    "polynomial":cert.columns[0],
                    "certificate_sha256":cert.certificate_sha256,
                    "source_ir_sha256":cert.ir_sha256,
                    "assembly":{
                        n:assembly_stats(path)
                        for n,path in zip(("s3_generic","s3_v12","s3_v13"),libs)
                    },
                    "build_ms":{
                        n:obj.manifest.compile_cold_end_to_end_ms
                        for n,obj in zip(("s3_generic","s3_v12","s3_v13"),
                                         (generic,v12,v13))
                    },
                    "nonzero_1m":bool(certified_gf2_fast_forward(ir,cert,1,1000003)),
                    "samples":[],
                }
                for n in horizons:
                    stdout=subprocess.check_output([
                        str(bench),*(str(x) for x in libs),
                        str(width),str(cert.columns[0]),str(n),"9","1467813"
                    ],text=True,timeout=90)
                    raw=json.loads(stdout)
                    assert raw["parity"] and raw["checks"]==64
                    val=raw["median_ns"]
                    values={
                        "s3_generic":val["s3_generic"],
                        "s3_v12":val["s3_v11"],
                        "s3_v13":val["s3_v12"],
                        "gcc_fullscan":val["gcc_matched_scan"],
                        "gcc_sparse":val["gcc_sparse"],
                    }
                    assert all(v>0 for v in values.values())
                    item={"N":n,"median_ns":values,
                          "v13_speedup_over_v12":values["s3_v12"]/values["s3_v13"],
                          "v13_slowdown_vs_gcc_sparse":values["s3_v13"]/values["gcc_sparse"],
                          "parity":True}
                    row["samples"].append(item)
                    print(f"{family} W{width} N{n}: V12={values['s3_v12']:.1f}ns "
                          f"V13={values['s3_v13']:.1f}ns "
                          f"gain={item['v13_speedup_over_v12']:.2f}x "
                          f"C={values['gcc_sparse']:.1f}ns",flush=True)
                report["cases"].append(row)
    out=HERE/("results_native_v13_quick.json" if quick else "results_native_v13.json")
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("RESULT_FILE="+str(out),flush=True)

if __name__=="__main__":
    run("--quick" in sys.argv)
