#!/usr/bin/env python3
"""Real S3 GPU Vulkan outputs/fixtures to compare against S3-native CPU on WSL.

No C CPU reference used as the comparison column; same initial binary
Conway grids and exact output digest are later used by S3 native x86.
Different OS runtime (Windows GPU vs WSL Linux CPU) is explicitly retained.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import statistics
import sys
import time

import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(ROOT))
from bootstrap.s3.gpu import GpuRuntime,compile_s3_to_wgsl

def cpu_numpy(grid,steps):
    current=grid.copy()
    for _ in range(steps):
        nbrs=(current[:-2,:-2]+current[:-2,1:-1]+current[:-2,2:]
              +current[1:-1,:-2]+current[1:-1,2:]
              +current[2:,:-2]+current[2:,1:-1]+current[2:,2:])
        out=np.zeros_like(current)
        out[1:-1,1:-1]=(
            (nbrs==3)|((nbrs==2)&(current[1:-1,1:-1]==1))
        ).astype(np.int32)
        current=out
    return current

def run():
    assert sys.platform=="win32", "WINDOWS_PHYSICAL_VULKAN_REQUIRED"
    rt=GpuRuntime(require_physical=True,preferred_backend="Vulkan")
    assert rt.device_info.is_physical and rt.device_info.backend=="Vulkan"
    source=(ROOT/"examples"/"gpu_v3"/"conway_gpu.s3").read_text("utf-8")
    begin=time.perf_counter()
    kernel=compile_s3_to_wgsl(
        source,"conway_gpu",allow_narrowing=True,
        workgroup_size=(8,8,1),
    )
    lowering_ms=round((time.perf_counter()-begin)*1000,4)
    fixtures=HERE/"fixtures"
    fixtures.mkdir(parents=True,exist_ok=True)
    report={
        "campaign":"S3_V14_S3_PHYSICAL_GPU_FIXTURES_FOR_NATIVE_CPU",
        "status":"ACTUAL_PHYSICAL_GPU_SAME_HOST_DIFFERENT_OS_CPU",
        "device":vars(rt.device_info),
        "gpu_source_hash":kernel.s3_source_hash,
        "gpu_wgsl_hash":kernel.gpu_kernel_hash,
        "precision":kernel.narrowing_contract,
        "lowering_ms":lowering_ms,
        "engine":"S3 source -> WGSL -> physical Vulkan RX580 on Windows",
        "sessions":1,"rounds":7,"warmups":2,
        "production_dispatch_enabled":False,
        "cases":[],
    }
    for width,steps in ((64,50),(128,10),(128,50)):
        rng=np.random.default_rng(13000+width+steps)
        grid=np.zeros((width,width),dtype=np.int32)
        grid[1:-1,1:-1]=rng.integers(
            0,2,size=(width-2,width-2),dtype=np.int32,
        )
        grid=np.ascontiguousarray(grid)
        baseline=cpu_numpy(grid,steps)
        expected_hash=hashlib.sha256(baseline.tobytes()).hexdigest()
        zero=np.zeros_like(grid)
        results=[]
        for i in range(9):
            execution=rt.execute_pingpong(
                kernel,"grid_in","grid_out",
                {"grid_in":grid.ravel(),"grid_out":zero.ravel()},
                {"w":width,"h":width},steps=steps,
                workgroups=((width+7)//8,(width+7)//8,1),
            )
            assert execution.gpu_is_physical
            assert execution.readback_success and execution.dispatch_success
            raw=execution.outputs["final"]
            actual=np.frombuffer(raw,dtype=np.int32).reshape(width,width)
            np.testing.assert_array_equal(actual,baseline)
            assert hashlib.sha256(actual.tobytes()).hexdigest()==expected_hash
            if i>=2:
                results.append({
                    "total_ms":execution.total_s*1000,
                    "h2d_ms":execution.h2d_s*1000,
                    "dispatch_ms":execution.dispatch_s*1000,
                    "d2h_ms":execution.d2h_s*1000,
                    "pipeline_ms":execution.pipeline_s*1000,
                })
        stem=f"conway_{width}x{width}_g{steps}"
        (fixtures/f"{stem}_input_i32le.bin").write_bytes(grid.tobytes())
        (fixtures/f"{stem}_gpu_output_sha256.txt").write_text(
            expected_hash+"\n",encoding="ascii",
        )
        record={
            "width":width,"height":width,"steps":steps,
            "initial_input_sha256":hashlib.sha256(grid.tobytes()).hexdigest(),
            "final_output_sha256":expected_hash,
            "gpu_physical":True,"readback_verified":True,
            "numpy_reference_exact":True,
            "samples":results,
            "median_gpu_total_ms":round(
                statistics.median(x["total_ms"] for x in results),4
            ),
            "median_gpu_dispatch_ms":round(
                statistics.median(x["dispatch_ms"] for x in results),4
            ),
        }
        report["cases"].append(record)
        print(f"S3_GPU_PHYSICAL W={width} steps={steps} "
              f"median={record['median_gpu_total_ms']:.3f}ms "
              f"sha256={expected_hash[:16]} PARITY=PASS",flush=True)
    destination=HERE/"results_s3_physical_gpu_v14.json"
    destination.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("RESULT_FILE="+str(destination),flush=True)

if __name__=="__main__":
    run()
