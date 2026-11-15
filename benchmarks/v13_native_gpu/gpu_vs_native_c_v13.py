#!/usr/bin/env python3
"""Physical RX580 S3 GPU vs independently compiled native Windows C Conway.

Runs on Windows in an isolated Python environment. C reference is compiled
with Zig's native Windows C frontend at -O3. GPU is actual S3->WGSL->Vulkan.
All GPU input transfer, dispatch, output readback and runtime allocations
are included in total; cold WGSL/C compilation is separately recorded.
No production GPU auto-dispatch is enabled or scientifically justified here.
"""
from __future__ import annotations
import ctypes
import json
from pathlib import Path
import statistics
import subprocess
import sys
from time import perf_counter_ns

import numpy as np

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))
from bootstrap.s3.gpu import GpuRuntime,compile_s3_to_wgsl

def cpu_numpy(grid,iterations):
    current=grid.copy()
    for _ in range(iterations):
        nbrs=(
            current[:-2,:-2]+current[:-2,1:-1]+current[:-2,2:]
            +current[1:-1,:-2]+current[1:-1,2:]
            +current[2:,:-2]+current[2:,1:-1]+current[2:,2:]
        )
        next_grid=np.zeros_like(current)
        next_grid[1:-1,1:-1]=(
            (nbrs==3)|((nbrs==2)&(current[1:-1,1:-1]==1))
        ).astype(np.int32)
        current=next_grid
    return current

def make_native_dll():
    dll=HERE/"conway_native_cpu_v13.dll"
    # Reuse the DLL produced by the first cold Zig build when present.
    # Cold build duration is unknown if the earlier invocation timed out
    # before returning, and MUST NOT be reported as measured.
    c_source=HERE/"conway_native_cpu.c"
    reuse=(dll.is_file() and dll.stat().st_size > 4096 and
           dll.stat().st_mtime_ns >= c_source.stat().st_mtime_ns)
    start=perf_counter_ns()
    if not reuse:
        command=[
            sys.executable,"-m","ziglang","cc","-O3","-shared",
            str(HERE/"conway_native_cpu.c"),"-o",str(dll),
        ]
        proc=subprocess.run(command,capture_output=True,text=True,timeout=300)
        if proc.returncode!=0:
            raise RuntimeError("NATIVE_C_COMPILE_FAIL: "+(proc.stderr or proc.stdout)[-1800:])
    compile_ms=None if reuse else (perf_counter_ns()-start)/1e6
    lib=ctypes.CDLL(str(dll))
    p=ctypes.POINTER(ctypes.c_int32)
    fn=lib.conway_native
    fn.argtypes=[p,p,ctypes.c_int32,ctypes.c_int32,ctypes.c_int32]
    fn.restype=ctypes.c_int
    return fn,compile_ms,dll

def execute_cpu(fn,initial,steps):
    out=np.empty_like(initial)
    p=ctypes.POINTER(ctypes.c_int32)
    code=fn(initial.ctypes.data_as(p),out.ctypes.data_as(p),
            initial.shape[1],initial.shape[0],steps)
    if code!=0:
        raise RuntimeError(f"NATIVE_C_RETURNED_{code}")
    return out

def run(session_id: str = "s1"):
    if session_id not in ("s1", "s2", "s3"):
        raise ValueError("ONLY_BOUNDED_V13_SESSION_IDS")
    if sys.platform!="win32":
        raise RuntimeError("V13 physical GPU measurement requires native Windows")
    cpu_fn,c_compile_ms,dll=make_native_dll()
    rt=GpuRuntime(require_physical=True,preferred_backend="Vulkan")
    if not rt.device_info.is_physical or rt.device_info.backend!="Vulkan":
        raise RuntimeError("PHYSICAL_VULKAN_GPU_REQUIRED")
    s3_source=(S3_ROOT/"examples"/"gpu_v3"/"conway_gpu.s3").read_text("utf-8")
    start=perf_counter_ns()
    kernel=compile_s3_to_wgsl(
        s3_source,"conway_gpu",allow_narrowing=True,
        workgroup_size=(8,8,1),
    )
    wgsl_compile_ms=(perf_counter_ns()-start)/1e6
    report={
        "campaign":"S3_V13_PHYSICAL_GPU_VS_NATIVE_WINDOWS_C",
        "status":"EXPLORATORY_ONE_HOST_SESSION_NOT_DISPATCH_QUALIFIED",
        "device":vars(rt.device_info),
        "native_c_compiler":"zig cc -O3 on Windows (independent C source)",
        "s3_gpu_compiler":"S3 source to WGSL to physical Vulkan RX580",
        "c_compile_cold_ms":None if c_compile_ms is None else round(c_compile_ms,4),
        "native_c_dll_reused_after_cold_compilation_timeout":c_compile_ms is None,
        "s3_wgsl_lowering_ms":round(wgsl_compile_ms,4),
        "gpu_to_s3_native_cpu_comparison":False,
        "windows_cpu_native_c_comparison":True,
        "sessions":1,"session_id":session_id,"rounds_per_case":7,
        "automatic_production_gpu_dispatch":False,
        "cases":[],
        "limitations":[
            "GPU total includes upload/dispatch/readback while native C includes per-call host buffer allocations and copy; no CUDA/ROCm or cross-machine claims",
            "S3 GPU uses i32 cell narrowing explicitly; C uses int32, cells are 0/1 and exact in this workload",
            "GPU runtime pipeline cache and driver timing are implementation-specific",
            "One GPU/CPU session is insufficient for automatic cost-model promotion",
            "C is a separately compiled optimized CPU baseline, not S3 native CPU",
        ],
    }
    for width,steps in ((64,50),(128,10),(128,50)):
        height=width
        rng=np.random.default_rng(13000+width+steps)
        grid=np.zeros((height,width),dtype=np.int32)
        grid[1:-1,1:-1]=rng.integers(
            0,2,size=(height-2,width-2),dtype=np.int32
        )
        grid=np.ascontiguousarray(grid)
        zero=np.zeros_like(grid)
        reference=cpu_numpy(grid,steps)
        np.testing.assert_array_equal(execute_cpu(cpu_fn,grid,steps),reference)
        native_times=[]
        numpy_times=[]
        gpu_total=[]
        gpu_dispatch=[]
        gpu_upload=[]
        gpu_readback=[]
        gpu_pipeline=[]
        for warmup in range(2):
            assert np.array_equal(execute_cpu(cpu_fn,grid,steps),reference)
            result=rt.execute_pingpong(
                kernel,"grid_in","grid_out",
                {"grid_in":grid.ravel(),"grid_out":zero.ravel()},
                {"w":width,"h":height},steps=steps,
                workgroups=((width+7)//8,(height+7)//8,1)
            )
            got=np.frombuffer(result.outputs["final"],dtype=np.int32).reshape((height,width))
            np.testing.assert_array_equal(got,reference)
        for round_index in range(7):
            # Alternate CPU vs GPU order each round without coupling sinks.
            def do_cpu():
                before=perf_counter_ns()
                actual=execute_cpu(cpu_fn,grid,steps)
                elapsed=(perf_counter_ns()-before)/1e6
                np.testing.assert_array_equal(actual,reference)
                native_times.append(elapsed)
            def do_gpu():
                result=rt.execute_pingpong(
                    kernel,"grid_in","grid_out",
                    {"grid_in":grid.ravel(),"grid_out":zero.ravel()},
                    {"w":width,"h":height},steps=steps,
                    workgroups=((width+7)//8,(height+7)//8,1)
                )
                actual=np.frombuffer(
                    result.outputs["final"],dtype=np.int32
                ).reshape((height,width))
                np.testing.assert_array_equal(actual,reference)
                assert result.gpu_is_physical and result.dispatch_success
                assert result.readback_success
                gpu_total.append(result.total_s*1000)
                gpu_dispatch.append(result.dispatch_s*1000)
                gpu_upload.append(result.h2d_s*1000)
                gpu_readback.append(result.d2h_s*1000)
                gpu_pipeline.append(result.pipeline_s*1000)
            if round_index%2:
                do_gpu();do_cpu()
            else:
                do_cpu();do_gpu()
            before=perf_counter_ns()
            np.testing.assert_array_equal(cpu_numpy(grid,steps),reference)
            numpy_times.append((perf_counter_ns()-before)/1e6)
        med=lambda xs:round(statistics.median(xs),4)
        row={
            "width":width,"height":height,"steps":steps,
            "buffer_bytes":int(grid.nbytes),
            "physical_gpu_parity":True,"native_c_parity":True,
            "gpu_total_ms":med(gpu_total),
            "gpu_dispatch_ms":med(gpu_dispatch),
            "gpu_h2d_ms":med(gpu_upload),
            "gpu_d2h_ms":med(gpu_readback),
            "gpu_pipeline_ms":med(gpu_pipeline),
            "native_c_total_ms":med(native_times),
            "numpy_cpu_total_ms":med(numpy_times),
            "gpu_over_native_c_total":med(gpu_total)/med(native_times),
            "gpu_over_numpy_total":med(gpu_total)/med(numpy_times),
            "all_samples_ms":{
                "gpu_total":gpu_total,
                "native_c_total":native_times,
                "numpy_cpu_total":numpy_times,
            },
        }
        report["cases"].append(row)
        print(f"PHYSICAL_GPU width={width} steps={steps} "
              f"gpu={row['gpu_total_ms']:.3f}ms "
              f"native_C={row['native_c_total_ms']:.3f}ms "
              f"numpy={row['numpy_cpu_total_ms']:.3f}ms PARITY=PASS",flush=True)
    destination=HERE/("results_gpu_vs_native_c_v13.json" if session_id=="s1"
                       else f"results_gpu_vs_native_c_v13_{session_id}.json")
    destination.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(f"RESULT_FILE={destination}",flush=True)

if __name__=="__main__":
    run(sys.argv[1] if len(sys.argv)>1 else "s1")
