#!/usr/bin/env python3
"""Real S3 native x86-64 A/B: dynamic-width guard dominance proof.

GCC only assembles/links S3-generated Assembly. A separate independent
C executable checks mathematical parity and times the actual S3
functions, with rotating baseline/experimental rounds.
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
from bootstrap.s3.backends.x86_64.dynamic_interval_v17 import (
    prove_dynamic_intervals_v17,
)
from source_v17 import source,sha256_hex


def disassemble_hot(lib:Path):
    output=subprocess.check_output(
        ["objdump","-d","-Mintel",str(lib)],
        text=True,errors="replace",timeout=60,
    )
    blocks={}
    name=None
    for line in output.splitlines():
        found=re.match(r"^[a-f0-9]+ <([^>]+)>:$",line)
        if found:
            name=found.group(1)
            blocks[name]=[]
        elif name and re.match(r"^\s*[a-f0-9]+:\s+[a-f0-9]",line):
            fields=line.split("\t")
            if len(fields)>2:
                blocks[name].append(fields[-1].strip().split(" ",1)[0])
    return {
        "library_bytes":lib.stat().st_size,
        "hot":{
            name:{
                "static_instructions":len(blocks.get(name,())),
                "static_conditional_branches":sum(
                    ins.startswith("j") and ins!="jmp"
                    for ins in blocks.get(name,())
                ),
                "static_calls":sum(
                    ins.startswith("call")
                    for ins in blocks.get(name,())
                ),
            }
            for name in ("dynamic_neighbor","dynamic_stencil")
        },
        "static_not_pmu":True,
    }


def run(session:str, hp03:bool=False):
    if session not in ("s1","s2","s3"):
        raise ValueError("INVALID_SESSION_ID")
    text=source()
    t=perf_counter_ns()
    program=compile_source(
        text,optimization=OptimizationLevel.O1,
        predictive_exact=False,
    ).require_ordinary_artifacts()[1]
    frontend_ms=(perf_counter_ns()-t)/1e6
    def backend(enabled:bool):
        return X8664Backend(
            register_allocation=True,
            enable_hp03=hp03,
            enable_hp02=True,
            max_instructions=100_000_000,
            instruction_budget_mode="loop-hybrid",
            experimental_dynamic_interval_v17=enabled,
        )
    base=backend(False)
    opt=backend(True)
    prepared,_=base._apply_hp_passes(program)
    proofs={
        fn.name:prove_dynamic_intervals_v17(fn)[1].to_dict()
        for fn in prepared.functions
        if fn.name in ("dynamic_neighbor","dynamic_stencil")
    }
    for name in ("dynamic_neighbor","dynamic_stencil"):
        assert proofs[name]["proven_interior_loads"]==6,proofs[name]
        assert len(proofs[name]["witnesses"])==6
    assert proofs["dynamic_neighbor"]["rejected_blocks_without_dominating_guard"]>=1
    t=perf_counter_ns()
    baseline=base._generate_ffi(program)
    base_emit_ms=(perf_counter_ns()-t)/1e6
    t=perf_counter_ns()
    experimental=opt._generate_ffi(program)
    opt_emit_ms=(perf_counter_ns()-t)/1e6
    assert baseline!=experimental

    with tempfile.TemporaryDirectory(prefix="s3_v17_dynamic_") as temporary:
        root=Path(temporary)
        native=[]
        stats={}
        link_ms={}
        for name,assembly in (("baseline",baseline),("v17",experimental)):
            asm_path=root/f"{name}.s"
            library=root/f"{name}.so"
            asm_path.write_text(assembly,"utf-8")
            t=perf_counter_ns()
            subprocess.run(
                ["gcc","-shared","-fPIC","-O2",str(asm_path),"-o",str(library)],
                check=True,capture_output=True,text=True,timeout=120,
            )
            link_ms[name]=(perf_counter_ns()-t)/1e6
            native.append(library)
            stats[name]=disassemble_hot(library)
        runner=root/"native_bench"
        subprocess.run([
            "gcc","-O3","-std=c11","-Wall","-Wextra","-Werror",
            str(HERE/"native_dynamic_ab_v17.c"),"-o",str(runner),"-ldl"
        ],check=True,capture_output=True,text=True,timeout=75)
        observations=json.loads(subprocess.check_output(
            [str(runner),str(native[0]),str(native[1]),"9"],
            text=True,timeout=180,
        ))
        assert observations["rounds"]==9
        assert len(observations["cases"])==21
        assert all(row["parity"] for row in observations["cases"])
        assert all(row["baseline_ns"]>0 and row["v17_ns"]>0
                   for row in observations["cases"])
    report={
        "campaign":"S3_V17_DYNAMIC_WIDTH_STENCIL_NATIVE_AB",
        "decision":"GO_EXPERIMENTAL_NOT_PRODUCTION",
        "session":session,
        "host_os":platform.system(),
        "host_arch":platform.machine(),
        "same_assembly_ir":True,
        "source_sha256":hashlib.sha256(text.encode()).hexdigest(),
        "backend_baseline":"S3 x86 native O1 with V17 OFF",
        "backend_candidate":"S3 x86 native O1 with V17 ON",
        "experimental_v17_default":False,
        "hp03_enabled":hp03,
        "frontend_ms":round(frontend_ms,3),
        "native_codegen_ms":{
            "baseline":round(base_emit_ms,3),
            "v17":round(opt_emit_ms,3),
        },
        "gcc_assemble_link_ms":{
            k:round(v,3) for k,v in link_ms.items()
        },
        "c_role":"INDEPENDENT_CORRECTNESS_ORACLE_AND_TIMING_DRIVER",
        "provenance":"Same generated S3 source and IR; only opt-in V17 feature differs",
        "proofs":proofs,
        "asm_hashes":{
            "baseline":hashlib.sha256(baseline.encode()).hexdigest(),
            "v17":hashlib.sha256(experimental.encode()).hexdigest(),
        },
        "static_disassembly":stats,
        "benchmark":observations,
        "limits":[
            "One physical host running WSL Linux x86-64; no PMU counters.",
            "Source contains explicit width>=3 true-path guard and fallback.",
            "No compiler-generated guard/versioned loop has been claimed.",
            "All S3 index arithmetic and i64 overflow traps remain.",
            "GCC assembles/links S3 assembly; it does not implement S3 math.",
            "Short microbenchmarks and timing noise prohibit universal speed claims.",
        ],
    }
    suffix="_hp03" if hp03 else ""
    filename=HERE/f"results_dynamic_v17_{session}{suffix}.json"
    filename.write_text(json.dumps(report,indent=2),"utf-8")
    print("PROOFS="+json.dumps({name:{"proven":p["proven_interior_loads"],"rejected_blocks":p["rejected_blocks_without_dominating_guard"]} for name,p in proofs.items()}),flush=True)
    for row in observations["cases"]:
        print(
            f"V17 session={session} hp03={hp03} "
            f"{row['width']}x{row['height']}: "
            f"baseline={row['baseline_ns']:.1f}ns "
            f"v17={row['v17_ns']:.1f}ns "
            f"speedup={row['speedup']:.3f}x",
            flush=True,
        )
    print(f"RESULT_FILE={filename}",flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--session",choices=("s1","s2","s3"),default="s1")
    parser.add_argument("--hp03",action="store_true")
    args=parser.parse_args()
    run(args.session,args.hp03)
