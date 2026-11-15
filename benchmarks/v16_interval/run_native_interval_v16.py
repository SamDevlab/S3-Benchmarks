#!/usr/bin/env python3
"""Real S3 source -> native x86 interval proof A/B for 2D eight-neighbor stencil.

The independent C reference computes only parity and times actual exported
S3 ELF functions. Same IR/program, only V16 flag differs. All CPU data
are one WSL x86-64 host; never assert production/general superiority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile
from time import perf_counter_ns

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))
from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.backends.x86_64 import X8664Backend
from bootstrap.s3.backends.x86_64.slice_interval_v16 import (
    prove_slice_intervals_v16,
)
from bootstrap.s3.assembly import AssemblyOpcode
from stencil_source_v16 import WIDTHS,kernel_name,whole_source


def hot_disassembly(path:Path)->dict:
    raw=subprocess.check_output(
        ["objdump","-d","-Mintel",str(path)],
        text=True,errors="replace",timeout=45,
    )
    symbols={}
    current=None
    for line in raw.splitlines():
        match=re.match(r"^[a-f0-9]+ <([^>]+)>:$",line)
        if match:
            current=match.group(1)
            symbols[current]=[]
        elif current is not None and re.match(r"^\s*[0-9a-f]+:\s+[a-f0-9]",line):
            parts=line.split("\t")
            if len(parts)>2:
                symbols[current].append(parts[-1].strip().split(" ",1)[0])
    return {
        "shared_elf_bytes":path.stat().st_size,
        "hot_functions":{
            kernel_name(width):{
                "static_instructions":len(symbols.get(kernel_name(width),[])),
                "static_conditional_branches":sum(
                    ins.startswith("j") and ins!="jmp"
                    for ins in symbols.get(kernel_name(width),[])
                ),
                "static_calls":sum(
                    ins.startswith("call")
                    for ins in symbols.get(kernel_name(width),[])
                ),
            }
            for width in WIDTHS
        },
        "not_dynamic_pmu":True,
    }


def run(session:str,hp03:bool):
    if session not in {"s1","s2","s3"}:
        raise ValueError("INVALID_SESSION")
    source=whole_source()
    before=perf_counter_ns()
    program=compile_source(
        source,optimization=OptimizationLevel.O1,
        predictive_exact=False,
    ).require_ordinary_artifacts()[1]
    s3_frontend_ms=(perf_counter_ns()-before)/1e6

    def create_backend(enabled:bool)->X8664Backend:
        return X8664Backend(
            register_allocation=True,
            enable_hp02=True,
            enable_hp03=hp03,
            max_instructions=50_000_000,
            instruction_budget_mode="loop-hybrid",
            experimental_slice_interval_v16=enabled,
        )
    original=create_backend(False)
    optimized=create_backend(True)
    prepared,_=original._apply_hp_passes(program)
    proof_stats={
        f.name:prove_slice_intervals_v16(f)[1].to_dict()
        for f in prepared.functions
        if not f.external and f.name!="main"
    }
    assertions={
        f.name:sum(1 for b in f.blocks for ins in b.instructions
                   if ins.opcode is AssemblyOpcode.TSLOAD)
        for f in prepared.functions if f.name!="main"
    }
    for width in WIDTHS:
        if not proof_stats[kernel_name(width)]["skipped_due_to_hp03"]:
            assert proof_stats[kernel_name(width)]["proven_interior_loads"]==6
        assert assertions[kernel_name(width)]>=8

    start=perf_counter_ns()
    asm_base=original._generate_ffi(program)
    base_compile_ms=(perf_counter_ns()-start)/1e6
    start=perf_counter_ns()
    asm_candidate=optimized._generate_ffi(program)
    v16_compile_ms=(perf_counter_ns()-start)/1e6

    with tempfile.TemporaryDirectory(prefix="s3_v16_interval_") as td:
        root=Path(td)
        libs=[]
        asm_profiles={}
        linker_ms={}
        for name,text in (("baseline",asm_base),("v16",asm_candidate)):
            source_path=root/f"{name}.s"
            lib_path=root/f"{name}.so"
            source_path.write_text(text,encoding="utf-8")
            start=perf_counter_ns()
            subprocess.run(
                ["gcc","-shared","-fPIC","-O2",
                 str(source_path),"-o",str(lib_path)],
                check=True,capture_output=True,text=True,timeout=80,
            )
            linker_ms[name]=(perf_counter_ns()-start)/1e6
            asm_profiles[name]=hot_disassembly(lib_path)
            libs.append(lib_path)
        exe=root/"stencil_bench"
        subprocess.run(
            ["gcc","-std=c11","-O3","-Wall","-Wextra","-Werror",
             str(HERE/"stencil_native_ab_v16.c"),"-o",str(exe),"-ldl"],
            check=True,capture_output=True,text=True,timeout=60,
        )
        raw=subprocess.check_output(
            [str(exe),str(libs[0]),str(libs[1]),"9"],
            text=True,timeout=120,
        )
        metrics=json.loads(raw)
        assert len(metrics["cases"])==9
        assert metrics["rounds"]==9
        assert all(x["parity"] and x["baseline_ns"]>0 and x["v16_ns"]>0
                   for x in metrics["cases"])
    report={
        "campaign":"S3_V16_2D_EIGHT_NEIGHBOR_INTERVAL_PROOF_NATIVE_AB",
        "decision":"GO_EXPERIMENTAL_NOT_COMPILER_DEFAULT",
        "session":session,
        "platform":platform.system()+"-"+platform.machine(),
        "same_s3_assembly_program_ir":True,
        "original_s3_source_sha256":hashlib.sha256(source.encode()).hexdigest(),
        "hp03_enabled":hp03,
        "hp02_enabled":True,
        "native_budget_mode":"loop-hybrid",
        "experimental_flag_default_off":True,
        "c_role":"INDEPENDENT_ORACLE_AND_NATIVE_TIME_HARNESS_ONLY",
        "gcc_role_for_s3":"ASSEMBLE_LINK",
        "assembly_output_equal":asm_base==asm_candidate,
        "proof":proof_stats,
        "slice_load_sites":assertions,
        "cold_compile_ms":{
            "frontend":round(s3_frontend_ms,3),
            "baseline_native_codegen":round(base_compile_ms,3),
            "v16_native_codegen":round(v16_compile_ms,3),
            "gcc_baseline":round(linker_ms["baseline"],3),
            "gcc_v16":round(linker_ms["v16"],3),
        },
        "static_disassembly":asm_profiles,
        "benchmark":metrics,
        "limitations":[
            "One Linux WSL x86-64 machine, 9 rotating rounds per configuration.",
            "The two source variants use the same S3 IR. Only V16 bounds proof is toggled.",
            "Native arithmetic, i64 overflow traps, allocation and reads remain active.",
            "C is a correctness oracle and timed caller, not a substitute native kernel.",
            "Static disassembly is not a PMU retired instruction measurement.",
            "HP03 compatibility is analyzed separately and no production defaults are changed.",
        ],
    }
    suffix=("_hp03" if hp03 else "")
    output=HERE/f"results_interval_v16_{session}{suffix}.json"
    output.write_text(json.dumps(report,indent=2),"utf-8")
    print("PROOF="+json.dumps(proof_stats),flush=True)
    for case in metrics["cases"]:
        print(f"V16 session={session} hp03={hp03} "
              f"width={case['width']} height={case['height']} "
              f"baseline_ns={case['baseline_ns']:.1f} "
              f"v16_ns={case['v16_ns']:.1f} "
              f"speedup={case['speedup']:.3f}x",flush=True)
    print(f"RESULT_FILE={output}",flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--session",choices=("s1","s2","s3"),default="s1")
    parser.add_argument("--hp03",action="store_true")
    args=parser.parse_args()
    run(args.session,args.hp03)
