#!/usr/bin/env python3
"""Real S3 native x86-64 CPU Conway, Linux ELF under WSL.

One S3 source function updates all interior cells, no C loop math.
Caller uses two 64-bit arrays and passes pointer+length for each slice,
then invokes native S3 once per generation. Identical binary Conway
rule/boundaries as the S3 GPU shader on Windows. Record WSL/Windows
runtime boundary honestly; no claim of same-OS or production readiness.
"""
from __future__ import annotations
import argparse
import array
import ctypes
import hashlib
import json
from pathlib import Path
import random
import statistics
import struct
import subprocess
import sys
import tempfile
import time

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))
from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.backends.x86_64 import X8664Backend

def compile_native(root:Path, *, peephole:bool=False, budget_mode:str="loop-hybrid"):
    text=(HERE/"conway_s3_cpu.s3").read_text("utf-8")
    product=compile_source(text,optimization=OptimizationLevel.O1,predictive_exact=False)
    _,program=product.require_ordinary_artifacts()
    t=time.perf_counter()
    asm=X8664Backend.scientific(
        max_instructions=50_000_000,
        instruction_budget_mode=budget_mode,
        experimental_asm_peephole_v14=peephole,
    )._generate_ffi(program)
    build_asm_s=time.perf_counter()-t
    assembly=root/"conway_s3_native.s"
    library=root/"conway_s3_native.so"
    assembly.write_text(asm,encoding="utf-8")
    t=time.perf_counter()
    subprocess.run(
        ["gcc","-shared","-fPIC","-O2",str(assembly),"-o",str(library)],
        check=True,capture_output=True,text=True,timeout=90,
    )
    link_s=time.perf_counter()-t
    dl=ctypes.CDLL(str(library))
    fun=dl.conway_step
    fun.argtypes=[
        ctypes.POINTER(ctypes.c_int64),ctypes.c_int64,
        ctypes.POINTER(ctypes.c_int64),ctypes.c_int64,
        ctypes.c_int64,ctypes.c_int64,
    ]
    fun.restype=ctypes.c_int64
    return fun,{"experimental_peephole_v14":peephole,
                "instruction_budget_mode":budget_mode,
                "s3_native_compiler_asm_ms":round(build_asm_s*1000,3),
                "s3_native_elf_link_ms":round(link_s*1000,3),
                "s3_generated_assembly_sha256":hashlib.sha256(asm.encode()).hexdigest(),
                "s3_elf_file_bytes":library.stat().st_size,
                "s3_source_sha256":hashlib.sha256(text.encode()).hexdigest()}

def reference(g:list[int],w:int,h:int,steps:int):
    a=list(g)
    for _ in range(steps):
        b=[0]*(w*h)
        for y in range(1,h-1):
            for x in range(1,w-1):
                idx=y*w+x
                n=(a[idx-w-1]+a[idx-w]+a[idx-w+1]+a[idx-1]+a[idx+1]
                   +a[idx+w-1]+a[idx+w]+a[idx+w+1])
                b[idx]=int(n==3 or (n==2 and a[idx]!=0))
        a=b
    return a

def native_run(fun,initial:list[int],w:int,h:int,steps:int):
    n=w*h
    a=(ctypes.c_int64*n)(*initial)
    b=(ctypes.c_int64*n)()
    ans=0
    for _ in range(steps):
        ans=fun(a,n,b,n,w,h)
        if ans!=0:
            raise RuntimeError(f"S3_NATIVE_CPU_BAD_RETURN_{ans}")
        a,b=b,a
    return [int(v) for v in a]

def checksum(g:list[int]):
    blob=b"".join(struct.pack("<i",v) for v in g)
    return hashlib.sha256(blob).hexdigest()

def load_fixture(width,steps):
    folder=HERE/"fixtures"
    f=folder/f"conway_{width}x{width}_g{steps}_input_i32le.bin"
    expected=folder/f"conway_{width}x{width}_g{steps}_gpu_output_sha256.txt"
    if f.is_file() and expected.is_file():
        blob=f.read_bytes()
        if len(blob)!=width*width*4:
            raise ValueError("INVALID_FIXTURE_BYTES")
        grid=[x[0] for x in struct.iter_unpack("<i",blob)]
        return grid,expected.read_text("ascii").strip(),True
    rng=random.Random(15002026+width+steps)
    grid=[0]*(width*width)
    for y in range(1,width-1):
        for x in range(1,width-1):
            grid[y*width+x]=rng.randrange(2)
    return grid,None,False

def run(smoke:bool=False, *, peephole:bool=False, budget_mode:str="loop-hybrid"):
    cases=((16,2),) if smoke else ((64,50),(128,10),(128,50))
    report={
        "campaign":"S3_V14_NATIVE_CPU_VS_S3_GPU_IDENTICAL_CONWAY",
        "engine":"S3 source -> native ELF x86-64, Linux WSL host",
        "status":"EXPERIMENTAL_HOSTED_FFI_NOT_SAME_OS_AS_WINDOWS_GPU",
        "ffi_boundary":"one exported S3 native call per generation, no native C math",
        "rounds":7,"warmups":2,
        "pmu_instructions_measured":False,
        "cases":[],
        "limitations":[
            "Native S3 CPU runs inside WSL Linux; GPU S3 runs on physical Windows Vulkan; this is same physical host but different runtime OS.",
            "CPU wall includes Python<->ctypes call per generation, but native per-step computation is from S3, not C.",
            "GPU and native CPU both exclude cold compile time from step latency; compile separately recorded.",
            "Per-run S3 CPU includes creating input/output i64 arrays; GPU operates i32 after explicit narrowing of 0/1.",
            "Not production dispatch calibration and no cross-machine replication.",
        ],
    }
    with tempfile.TemporaryDirectory(prefix="s3_v14_conway_") as temp:
        fun,build=compile_native(Path(temp),peephole=peephole,budget_mode=budget_mode)
        report["build"]=build
        for w,steps in cases:
            initial,gpu_expected,fixture=load_fixture(w,steps)
            ref=reference(initial,w,w,steps)
            expected=checksum(ref)
            if gpu_expected is not None:
                assert expected==gpu_expected,(w,steps,expected,gpu_expected)
            for _ in range(2):
                got=native_run(fun,initial,w,w,steps)
                assert got==ref,(w,steps)
            samples=[]
            for _ in range(7):
                start=time.perf_counter_ns()
                got=native_run(fun,initial,w,w,steps)
                duration=(time.perf_counter_ns()-start)/1e6
                assert got==ref
                samples.append(duration)
            record={
                "width":w,"height":w,"steps":steps,
                "fixture_from_physical_gpu":fixture,
                "source_input_sha256":checksum(initial),
                "final_output_sha256":expected,
                "native_s3_parity":True,
                "gpu_digest_agrees":gpu_expected is None or gpu_expected==expected,
                "median_native_s3_cpu_ms":round(statistics.median(samples),4),
                "all_samples_native_s3_cpu_ms":samples,
            }
            report["cases"].append(record)
            print(f"S3_NATIVE_CPU W={w} steps={steps} "
                  f"median={record['median_native_s3_cpu_ms']:.3f}ms "
                  f"correct=PASS shared_fixture={fixture}",flush=True)
    if smoke:
        output=HERE/"results_native_s3_cpu_smoke_v14.json"
    elif budget_mode=="loop-hybrid" and not peephole:
        output=HERE/"results_native_s3_cpu_v14.json"
    else:
        suffix=budget_mode.replace("-","_")+("_peephole" if peephole else "")
        output=HERE/f"results_native_s3_cpu_v14_{suffix}.json"
    output.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("RESULT_FILE="+str(output),flush=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--smoke",action="store_true")
    parser.add_argument("--peephole",action="store_true")
    parser.add_argument("--budget-mode",choices=("loop-hybrid","exact-segment","per-instruction"),default="loop-hybrid")
    opt=parser.parse_args()
    run(opt.smoke,peephole=opt.peephole,budget_mode=opt.budget_mode)
