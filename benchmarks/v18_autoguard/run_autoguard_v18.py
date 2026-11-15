#!/usr/bin/env python3
"""V18 compiled-guard dynamic stencil: actual native x86-64 baseline A/B.

The exact same source and IR are compiled with V18 OFF/ON.
Only GCC assembler/linker processes the S3-generated x86 ELF.
C provides independent arithmetic oracle and clocked native caller.
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
from bootstrap.s3.backends.x86_64.auto_guard_v18 import (
    version_stencil_with_auto_guard_v18,
)
from source_v18 import source,sha256_hex


def native_static_profile(lib:Path)->dict:
    raw=subprocess.check_output([
        "objdump","-d","-Mintel",str(lib)
    ],text=True,errors="replace",timeout=60)
    instructions={}
    symbol=None
    for line in raw.splitlines():
        candidate=re.match(r"^[0-9a-f]+ <([^>]+)>:$",line)
        if candidate:
            symbol=candidate.group(1)
            instructions[symbol]=[]
        elif symbol and re.match(r"^\s*[0-9a-f]+:\s+[0-9a-f]",line):
            cols=line.split("\t")
            if len(cols)>2:
                instructions[symbol].append(cols[-1].strip().split(" ",1)[0])
    return {
        "library_bytes":lib.stat().st_size,
        "hot":{
            name:{
                "static_instructions":len(instructions.get(name,())),
                "static_conditional_branches":sum(
                    op.startswith("j") and op!="jmp"
                    for op in instructions.get(name,())
                ),
                "static_calls":sum(
                    op.startswith("call")
                    for op in instructions.get(name,())
                ),
            }for name in ("auto_neighbor","auto_stencil")
        },
        "static_not_cpu_pmu":True,
    }


def run(session:str,hp03:bool):
    if session not in ("s1","s2","s3"):
        raise ValueError("INVALID_SESSION")
    s3_source=source()
    start=perf_counter_ns()
    program=compile_source(
        s3_source,optimization=OptimizationLevel.O1,
        predictive_exact=False,
    ).require_ordinary_artifacts()[1]
    frontend_ms=(perf_counter_ns()-start)/1e6

    def config(enabled:bool):
        return X8664Backend(
            register_allocation=True,
            enable_hp02=True,
            enable_hp03=hp03,
            max_instructions=100_000_000,
            instruction_budget_mode="loop-hybrid",
            experimental_auto_guard_v18=enabled,
        )

    original=config(False)
    candidate=config(True)
    hp_program,_=original._apply_hp_passes(program)
    proofs={
        fn.name:version_stencil_with_auto_guard_v18(fn)[1].to_dict()
        for fn in hp_program.functions
        if fn.name in ("auto_neighbor","auto_stencil")
    }
    for name in ("auto_neighbor","auto_stencil"):
        assert proofs[name]["generated_guard"] is True,proofs[name]
        assert proofs[name]["eliminated_fast_bounds"]==6
        assert proofs[name]["fallback_bounds_eliminated"]==0
        assert len(proofs[name]["witness_records"])==6

    start=perf_counter_ns()
    baseline=original._generate_ffi(program)
    compile_base_ms=(perf_counter_ns()-start)/1e6
    start=perf_counter_ns()
    optimized=candidate._generate_ffi(program)
    compile_opt_ms=(perf_counter_ns()-start)/1e6
    assert baseline!=optimized

    with tempfile.TemporaryDirectory(prefix="s3_v18_autoguard_") as td:
        root=Path(td)
        builds=[]
        profiles={}
        gcc_ms={}
        for name,assembly in (("baseline",baseline),("v18",optimized)):
            assembly_path=root/f"{name}.s"
            library=root/f"{name}.so"
            assembly_path.write_text(assembly,"utf-8")
            start=perf_counter_ns()
            subprocess.run([
                "gcc","-shared","-fPIC","-O2",str(assembly_path),
                "-o",str(library),
            ],check=True,capture_output=True,text=True,timeout=90)
            gcc_ms[name]=(perf_counter_ns()-start)/1e6
            builds.append(library)
            profiles[name]=native_static_profile(library)
        driver=root/"ab"
        subprocess.run([
            "gcc","-O3","-std=c11","-Wall","-Wextra","-Werror",
            str(HERE/"native_autoguard_ab_v18.c"),"-o",str(driver),"-ldl",
        ],check=True,capture_output=True,text=True,timeout=60)
        metrics=json.loads(subprocess.check_output(
            [str(driver),str(builds[0]),str(builds[1]),"9"],
            text=True,timeout=180,
        ))
        assert len(metrics["cases"])==21
        assert metrics["rounds"]==9
        assert all(
            r["parity"] and r["baseline_ns"]>0 and r["v18_ns"]>0
            for r in metrics["cases"]
        )

    report={
        "campaign":"S3_V18_COMPILER_GENERATED_GUARD_FAST_SLOW_NATIVE_AB",
        "decision":"GO_EXPERIMENTAL_NOT_PRODUCTION",
        "session":session,
        "host_os":platform.system(),
        "host_arch":platform.machine(),
        "same_assembly_ir":True,
        "source_sha256":sha256_hex(),
        "original_source_contains_user_width_guard":False,
        "compiler_generated_guard":True,
        "compiler_slow_fallback_original_cfg":True,
        "experimental_v18_default":False,
        "hp03_enabled":hp03,
        "c_role":"INDEPENDENT_CORRECTNESS_ORACLE_AND_TIMING_DRIVER",
        "gcc_role":"ASSEMBLY_LINK_ONLY",
        "backend_baseline":"S3 O1 native x86 V18 OFF",
        "backend_candidate":"S3 O1 native x86 V18 ON",
        "proofs":proofs,
        "cold_compile_ms":{
            "frontend":round(frontend_ms,3),
            "baseline_native_codegen":round(compile_base_ms,3),
            "v18_native_codegen":round(compile_opt_ms,3),
            "gcc_baseline":round(gcc_ms["baseline"],3),
            "gcc_v18":round(gcc_ms["v18"],3),
        },
        "assembly_bytes":{
            "baseline":len(baseline.encode("utf-8")),
            "v18":len(optimized.encode("utf-8")),
        },
        "asm_hashes":{
            "baseline":hashlib.sha256(baseline.encode()).hexdigest(),
            "v18":hashlib.sha256(optimized.encode()).hexdigest(),
        },
        "native_static_profile":profiles,
        "benchmark":metrics,
        "limitations":[
            "One physical host with WSL x86-64. Three process sessions do not mean three machines.",
            "GCC only assembles and links S3-produced code, it does not implement the stencil.",
            "Original slow CFG retained in compiler IR. Auto guard is cheap nontrapping >=3.",
            "V18 duplicates whole CFG, not just loop; code size may increase considerably.",
            "No universal speed gain, green GitHub CI or production dispatch claim.",
        ],
    }
    suffix="_hp03" if hp03 else ""
    output=HERE/f"results_autoguard_v18_{session}{suffix}.json"
    output.write_text(json.dumps(report,indent=2),"utf-8")
    for row in metrics["cases"]:
        print(f"V18 session={session} hp03={hp03} "
              f"{row['width']}x{row['height']} "
              f"baseline_ns={row['baseline_ns']:.1f} "
              f"v18_ns={row['v18_ns']:.1f} "
              f"speedup={row['speedup']:.3f}x",flush=True)
    print(f"ASSEMBLY_BASE={report['assembly_bytes']['baseline']} "
          f"V18={report['assembly_bytes']['v18']}",flush=True)
    print(f"RESULT_FILE={output}",flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--session",choices=("s1","s2","s3"),default="s1")
    parser.add_argument("--hp03",action="store_true")
    args=parser.parse_args()
    run(args.session,args.hp03)
