#!/usr/bin/env python3
"""V11 real physical GPU S3 multi-step residency vs independent NumPy CPU.

Bounded W=64/128, 50 Conway generations using ping/pong buffers that
stay on the RX580 between dispatches; no unsafe buffer override.
Measures total transfer/dispatch/readback against CPU vectorized steps.
"""
from __future__ import annotations

import json
from pathlib import Path
import statistics
import sys
from time import perf_counter_ns

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))

import numpy as np
from bootstrap.s3.gpu import GpuRuntime, compile_s3_to_wgsl


def cpu_conway(initial: np.ndarray,steps: int)->np.ndarray:
    grid=initial.copy()
    for _ in range(steps):
        n=(
            grid[:-2,:-2] + grid[:-2,1:-1] + grid[:-2,2:]
            +grid[1:-1,:-2] + grid[1:-1,2:]
            +grid[2:,:-2] + grid[2:,1:-1] +grid[2:,2:]
        )
        out=np.zeros_like(grid)
        out[1:-1,1:-1]=np.logical_or(
            n==3, np.logical_and(n==2,grid[1:-1,1:-1]==1)
        ).astype(np.int32)
        grid=out
    return grid


def run():
    rt=GpuRuntime(require_physical=True)
    if not rt.device_info.is_physical or rt.device_info.backend not in ("Vulkan","D3D12"):
        raise RuntimeError("physical GPU required")
    src=(S3_ROOT/"examples"/"gpu_v3"/"conway_gpu.s3").read_text(encoding="utf-8")
    t0=perf_counter_ns()
    kernel=compile_s3_to_wgsl(
        src,"conway_gpu",allow_narrowing=True,workgroup_size=(8,8,1),
    )
    lowering_ms=(perf_counter_ns()-t0)/1e6
    rows=[]
    for w in (64,128):
        h=w
        steps=50
        rng=np.random.default_rng(1105+w)
        initial=np.zeros((h,w),dtype=np.int32)
        initial[1:-1,1:-1]=rng.integers(0,2,(h-2,w-2),dtype=np.int32)
        reference=cpu_conway(initial,steps)
        buf_zero=np.zeros_like(initial)
        cpu_samples=[]
        for _ in range(7):
            t0=perf_counter_ns()
            assert np.array_equal(cpu_conway(initial,steps),reference)
            cpu_samples.append((perf_counter_ns()-t0)/1e6)
        gpu_samples=[]
        dispatch_samples=[]
        for i in range(7):
            result=rt.execute_pingpong(
                kernel,"grid_in","grid_out",
                {"grid_in":initial.ravel(),"grid_out":buf_zero.ravel()},
                {"w":w,"h":h},
                steps=steps,workgroups=((w+7)//8,(h+7)//8,1),
            )
            got=np.frombuffer(result.outputs["final"],dtype=np.int32).reshape((h,w))
            np.testing.assert_array_equal(got,reference)
            if not result.gpu_is_physical or not result.dispatch_success or not result.readback_success:
                raise AssertionError("not a valid physical GPU dispatch/readback")
            gpu_samples.append(result.total_s*1000)
            dispatch_samples.append(result.dispatch_s*1000)
        rows.append({
            "width":w,"height":h,"steps":steps,
            "per_buffer_bytes":int(initial.nbytes),
            "s3_gpu_conway_correct":True,"gpu_physical":True,
            "gpu_total_ms_median":round(statistics.median(gpu_samples),4),
            "gpu_dispatch_ms_median":round(statistics.median(dispatch_samples),4),
            "cpu_numpy_total_ms_median":round(statistics.median(cpu_samples),4),
            "gpu_over_cpu_total_ratio":round(statistics.median(gpu_samples)/
                                               statistics.median(cpu_samples),4),
            "gpu_rounds":7,"cpu_rounds":7,
        })
        print("PHYSICAL_GPU_CONWAY",w,"x",h,"steps",steps,
              "GPU_MS",rows[-1]["gpu_total_ms_median"],
              "CPU_NUMPY_MS",rows[-1]["cpu_numpy_total_ms_median"],
              "PARITY_PASS",flush=True)
    report={
        "status":"REAL_S3_WGSL_PHYSICAL_GPU_RESIDENT_PINGPONG_PARITY",
        "device":vars(rt.device_info),
        "s3_wgsl_lowering_ms":round(lowering_ms,4),
        "cases":rows,
        "novel_gpu_algorithm":False,
        "production_dispatch_auto_enabled":False,
        "limits":[
            "One physical Windows RX580 GPU, 7 timed rounds and one local CPU.",
            "N=50 generations, two resident pingpong buffers of <=65536 bytes each.",
            "Total GPU includes shader dispatch/transfer/readback, unlike purely resident kernel microbenchmark.",
            "NumPy CPU uses a vectorized slicing reference, not tuned native C or AVX2.",
            "These results do not authorize unsafe-buffer override, GPU production promotion or a universal speedup claim.",
        ],
    }
    out=HERE/"results_gpu_resident_conway_v11.json"
    out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("OUTPUT="+str(out),flush=True)


if __name__=="__main__":
    run()
