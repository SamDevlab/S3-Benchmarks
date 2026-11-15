#!/usr/bin/env python3
"""Real non-GF2 S3 native x86 A/B for opt-in flag-neutral asm peephole.

Five actual native workloads from three S3 functions, 9 alternating
rounds with independent C oracle. GCC only assembles/links S3 outputs.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(ROOT))
from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.backends.x86_64 import X8664Backend
from bootstrap.s3.backends.x86_64.asm_peephole_v14 import optimize_s3_asm_v14

SRC="""export fn sum_squares(n: i64) -> i64:
    mut sum: i64 = 0
    mut i: i64 = 0
    while i < n:
        sum = sum + i * i
        i = i + 1
    return sum

export fn factorial(n: i64) -> i64:
    mut out: i64 = 1
    mut i: i64 = 1
    while i <= n:
        out = out * i
        i = i + 1
    return out

export fn count_bits(n: i64) -> i64:
    mut count: i64 = 0
    mut x: i64 = n
    while x > 0:
        x = i64_and(x, x - 1)
        count = count + 1
    return count

fn main() -> i64:
    return 0
"""

def hot_stats(so:Path):
    output=subprocess.check_output(
        ["objdump","-d","-Mintel",str(so)],text=True,timeout=40,
        errors="replace",
    )
    blocks={}
    current=None
    for line in output.splitlines():
        h=re.match(r"^([0-9a-f]+) <([^>]+)>:$",line)
        if h:
            current=h.group(2)
            blocks[current]=0
        elif current and re.match(r"^\s*[0-9a-f]+:\s+[0-9a-f]",line):
            blocks[current]+=1
    return {
        "bytes":so.stat().st_size,
        "hot_static_instructions":{
            name:blocks.get(name,0)
            for name in ("sum_squares","factorial","count_bits")
        },
        "scope":"static disassembly, not PMU retired instruction count",
    }

def run(session_id: str="s1"):
    if session_id not in ("s1","s2","s3"):
        raise ValueError("INVALID_BOUNDED_SESSION_ID")
    t=time.perf_counter_ns()
    program=compile_source(
        SRC,optimization=OptimizationLevel.O1,
        predictive_exact=False,
    ).require_ordinary_artifacts()[1]
    source_compile_ms=(time.perf_counter_ns()-t)/1e6
    baseline=X8664Backend.scientific(
        max_instructions=25_000_000,
        experimental_asm_peephole_v14=False,
    )._generate_ffi(program)
    optimized=X8664Backend.scientific(
        max_instructions=25_000_000,
        experimental_asm_peephole_v14=True,
    )._generate_ffi(program)
    expected,stats=optimize_s3_asm_v14(baseline)
    assert optimized==expected
    with tempfile.TemporaryDirectory(prefix="s3_v14_general_") as tmp:
        td=Path(tmp)
        dlls=[]
        for name,asm in (("baseline",baseline),("experimental",optimized)):
            inp=td/(name+".s")
            out=td/(name+".so")
            inp.write_text(asm,encoding="utf-8")
            subprocess.run(
                ["gcc","-shared","-fPIC","-O2",str(inp),"-o",str(out)],
                check=True,capture_output=True,timeout=90,
            )
            dlls.append(out)
        executable=td/"compare"
        subprocess.run([
            "gcc","-O3","-std=c11","-Wall","-Wextra","-Werror",
            str(HERE/"general_native_v14.c"),"-o",str(executable),"-ldl",
        ],check=True,capture_output=True,text=True,timeout=90)
        benchmark=json.loads(subprocess.check_output(
            [str(executable),str(dlls[0]),str(dlls[1]),"9"],
            text=True,timeout=90,
        ))
        assert all(c["parity"] for c in benchmark["cases"])
        profiles={
            name:hot_stats(so)
            for name,so in zip(("baseline","experimental"),dlls)
        }
    report={
        "campaign":"S3_V14_GENERIC_X86_PEEPHOLE_NATIVE_AB",
        "status":"EXPERIMENTAL_ONLY_NOT_PROMOTED",
        "session_id":session_id,
        "control":"same S3 IR, backend opt-in only, real x86 FFI, GCC as linker",
        "native_s3_source_sha256":hashlib.sha256(SRC.encode()).hexdigest(),
        "source_compile_ms":round(source_compile_ms,3),
        "asm_peephole_stats":{
            "dropped_self_moves":stats.dropped_self_moves,
            "dropped_identity_lea":stats.dropped_identity_lea,
            "dropped_fallthrough_jumps":stats.dropped_fallthrough_jumps,
        },
        "asm_source_bytes_baseline":len(baseline),
        "asm_source_bytes_experimental":len(optimized),
        "native_profiles":profiles,
        "bench":benchmark,
        "limits":[
            "S3 generic backend opt-in peephole is behavior-preserving but small.",
            "This is one WSL host session with 9 alternating rounds.",
            "No PMU counters; static disassembly is not dynamic instruction count.",
            "Speed changes smaller than measurement noise are not a GO decision.",
        ],
    }
    out=HERE/("results_general_native_v14.json" if session_id=="s1"
              else f"results_general_native_v14_{session_id}.json")
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("PEEPHOLE="+json.dumps(report["asm_peephole_stats"]),flush=True)
    for c in benchmark["cases"]:
        print(f"NATIVE_GENERIC {c['name']} baseline={c['baseline_ns']:.2f}ns "
              f"opt={c['experimental_ns']:.2f}ns "
              f"speedup={c['speedup']:.3f}x",flush=True)
    print("RESULT_FILE="+str(out),flush=True)

if __name__=="__main__":
    run(sys.argv[1] if len(sys.argv)>1 else "s1")
