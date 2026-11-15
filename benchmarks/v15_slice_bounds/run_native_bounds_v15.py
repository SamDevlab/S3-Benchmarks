#!/usr/bin/env python3
"""V15 CPU slice-bounds proof A/B, real native x86 generated from S3.

Default comparison holds HP03 disabled so a separate loop-bounds
optimizer cannot hide the benefit. --hp03 verifies interaction with
the existing guarded loop-versioning pass. No codegen defaults change.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))
from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.backends.x86_64 import X8664Backend
from bootstrap.s3.backends.x86_64.slice_bounds_reuse_v15 import (
    reuse_proven_slice_load_bounds_v15,
)

SOURCE="""export fn loop_dup(xs: &[i64], count: i64) -> i64:
    mut i: i64 = 0
    mut total: i64 = 0
    while i < count:
        total = total + xs[i] + xs[i]
        i = i + 1
    return total

export fn sum_three(xs: &[i64], count: i64) -> i64:
    mut i: i64 = 0
    mut total: i64 = 0
    while i < count:
        total = total + xs[i] + xs[i] + xs[i]
        i = i + 1
    return total

fn main() -> i64:
    return 0
"""

def hot_asm_stats(shared:Path)->dict:
    output=subprocess.check_output(
        ["objdump","-d","-Mintel",str(shared)],
        text=True,timeout=45,errors="replace",
    )
    block={}
    symbol=None
    for line in output.splitlines():
        header=re.match(r"^[0-9a-f]+ <([^>]+)>:$",line)
        if header:
            symbol=header.group(1)
            block.setdefault(symbol,[])
        elif symbol and re.match(r"^\s*[0-9a-f]+:\s+[0-9a-f]",line):
            parts=line.split("\t")
            if len(parts)>2:
                block[symbol].append(parts[-1].strip().split(" ",1)[0])
    return {
        "shared_library_bytes":shared.stat().st_size,
        "hot_functions":{
            f:{
                "static_instructions":len(block.get(f,())),
                "static_conditional_jumps":sum(
                    op.startswith("j") and op!="jmp"
                    for op in block.get(f,())
                ),
                "static_calls":sum(op.startswith("call") for op in block.get(f,())),
            } for f in ("loop_dup","sum_three")
        },
        "static_counts_not_dynamic_pmu":True,
    }

def run(session:str,hp03:bool):
    assert session in {"s1","s2","s3"}
    t=time.perf_counter_ns()
    program=compile_source(
        SOURCE,optimization=OptimizationLevel.O1,
        predictive_exact=False,
    ).require_ordinary_artifacts()[1]
    compile_ms=(time.perf_counter_ns()-t)/1e6
    def backend(enabled:bool)->X8664Backend:
        return X8664Backend(
            register_allocation=True,
            max_instructions=50_000_000,
            instruction_budget_mode="loop-hybrid",
            enable_hp03=hp03,
            enable_hp02=True,
            experimental_slice_bounds_reuse_v15=enabled,
        )
    base=backend(False)
    optimized=backend(True)
    transformed,_=base._apply_hp_passes(program)
    local_proofs={
        fn.name:reuse_proven_slice_load_bounds_v15(fn)[1].to_dict()
        for fn in transformed.functions if not fn.external and fn.name!="main"
    }
    start=time.perf_counter_ns()
    baseline_asm=base._generate_ffi(program)
    baseline_emit_ms=(time.perf_counter_ns()-start)/1e6
    start=time.perf_counter_ns()
    v15_asm=optimized._generate_ffi(program)
    v15_emit_ms=(time.perf_counter_ns()-start)/1e6
    if not hp03:
        assert baseline_asm!=v15_asm
    same_assembly=(baseline_asm==v15_asm)
    with tempfile.TemporaryDirectory(prefix="s3_v15_slice_ab_") as td:
        root=Path(td)
        profiles={}
        libs=[]
        for name,asm in (("baseline",baseline_asm),("v15",v15_asm)):
            src=root/f"{name}.s"
            lib=root/f"{name}.so"
            src.write_text(asm,"utf-8")
            subprocess.run(
                ["gcc","-shared","-fPIC","-O2",str(src),"-o",str(lib)],
                check=True,capture_output=True,text=True,timeout=60,
            )
            libs.append(lib)
            profiles[name]=hot_asm_stats(lib)
        binary=root/"compare"
        subprocess.run(
            ["gcc","-O3","-std=c11","-Wall","-Wextra","-Werror",
             str(HERE/"native_bounds_ab_v15.c"),"-o",str(binary),"-ldl"],
            check=True,capture_output=True,text=True,timeout=60,
        )
        sample=json.loads(subprocess.check_output([
            str(binary),str(libs[0]),str(libs[1]),"9",
            "1" if hp03 else "0",
        ],text=True,timeout=120))
        assert sample["rounds"]==9
        assert len(sample["cases"])==6
        assert all(row["parity"] and row["baseline_ns"]>0 and row["v15_ns"]>0
                   for row in sample["cases"])
    result={
        "campaign":"S3_V15_LOCAL_SLICE_BOUNDS_PROOF_NATIVE_AB",
        "status":"EXPERIMENTAL_NO_GLOBAL_PROMOTION",
        "session_id":session,
        "same_s3_assembly_program_ir":True,
        "source_sha256":hashlib.sha256(SOURCE.encode("utf-8")).hexdigest(),
        "s3_compiler_level":"O1",
        "gcc_role_for_s3":"ASSEMBLE_AND_LINK_ONLY",
        "hp03_loop_versioning_enabled":hp03,
        "hp02_scalar_promotion_enabled":True,
        "native_budget_mode":"loop-hybrid",
        "experimental_v15_default":False,
        "optimization_stats":local_proofs,
        "identical_native_assembly_after_optin":same_assembly,
        "compile_to_assembly_ms":{
            "source_compile_ms":round(compile_ms,3),
            "baseline_emitter_ms":round(baseline_emit_ms,3),
            "v15_emitter_ms":round(v15_emit_ms,3),
        },
        "static_disassembly":profiles,
        "results":sample,
        "limits":[
            "One host, 9 alternating rounds. Submicrosecond runtimes may be noisy.",
            "The independent C code is a correctness oracle and timing harness only.",
            "Resulting S3 machine code is not formally verified; native differential tests compare outputs and invalid bounds traps.",
            "Preexisting HP03 fast-path checks are not used as a local proof witness.",
            "No CPU PMU or production dispatch claims.",
        ],
    }
    suffix=f"_{session}"+("_hp03" if hp03 else "")
    out=HERE/f"results_native_bounds_v15{suffix}.json"
    out.write_text(json.dumps(result,indent=2),"utf-8")
    for row in sample["cases"]:
        print(f"V15 HP03={hp03} SESSION={session} {row['kernel']} n={row['length']} "
              f"baseline={row['baseline_ns']:.2f}ns "
              f"opt={row['v15_ns']:.2f}ns gain={row['speedup']:.3f}x",
              flush=True)
    print(f"RESULT_FILE={out}",flush=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--session",choices=("s1","s2","s3"),default="s1")
    parser.add_argument("--hp03",action="store_true")
    args=parser.parse_args()
    run(args.session,args.hp03)
