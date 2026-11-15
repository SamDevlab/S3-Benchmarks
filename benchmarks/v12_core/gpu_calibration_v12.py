#!/usr/bin/env python3
"""V12 physical GPU/CPU exact-workload cost calibration (no dispatch changes).

Collect seven REAL timing samples each for a S3-WGSL GPU-resident Conway
pipeline and NumPy vectorized CPU. Verify full cell parity each sample.
Feed these actual measurements into S3 V12's fail-closed empirical route
planner, which never overrides the existing GPU safety qualification.
"""
from __future__ import annotations

from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import platform
import sys
from time import perf_counter_ns

HERE=Path(__file__).resolve().parent
S3_ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(S3_ROOT))

import numpy as np
from bootstrap.s3.gpu import GpuRuntime, compile_s3_to_wgsl
from bootstrap.s3.gpu.empirical_dispatch import (
    GpuEmpiricalCalibration, choose_empirical_gpu_route,
)


def cpu_reference(initial,steps):
    grid=initial.copy()
    for _ in range(steps):
        n=(grid[:-2,:-2]+grid[:-2,1:-1]+grid[:-2,2:]
           +grid[1:-1,:-2]+grid[1:-1,2:]
           +grid[2:,:-2]+grid[2:,1:-1]+grid[2:,2:])
        after=np.zeros_like(grid)
        after[1:-1,1:-1]=((n==3)|((n==2)&(grid[1:-1,1:-1]==1))).astype(np.int32)
        grid=after
    return grid


def main():
    rt=GpuRuntime(require_physical=True)
    assert rt.device_info.is_physical and rt.device_info.backend=="Vulkan"
    source=(S3_ROOT/"examples/gpu_v3/conway_gpu.s3").read_text(encoding="utf-8")
    h=sha256(source.encode()).hexdigest()
    host=platform.node()+"|"+platform.system()+"|"+rt.device_info.driver
    kernel=compile_s3_to_wgsl(
        source,"conway_gpu",allow_narrowing=True,workgroup_size=(8,8,1),
    )
    cases=[]
    for width in (64,128):
        steps=50
        rng=np.random.default_rng(1200+width)
        start=np.zeros((width,width),dtype=np.int32)
        start[1:-1,1:-1]=rng.integers(0,2,(width-2,width-2),dtype=np.int32)
        ref=cpu_reference(start,steps)
        cpu_ms=[]
        gpu_ms=[]
        dispatch_ms=[]
        for k in range(7):
            t0=perf_counter_ns()
            cpu=cpu_reference(start,steps)
            cpu_ms.append((perf_counter_ns()-t0)/1e6)
            np.testing.assert_array_equal(cpu,ref)
            res=rt.execute_pingpong(
                kernel,"grid_in","grid_out",
                {"grid_in":start.ravel(),"grid_out":np.zeros_like(start).ravel()},
                {"w":width,"h":width},steps=steps,
                workgroups=((width+7)//8,(width+7)//8,1),
            )
            gpu=np.frombuffer(res.outputs["final"],dtype=np.int32).reshape(width,width)
            np.testing.assert_array_equal(gpu,ref)
            assert res.gpu_is_physical and res.dispatch_success and res.readback_success
            gpu_ms.append(res.total_s*1000)
            dispatch_ms.append(res.dispatch_s*1000)
        evidence=GpuEmpiricalCalibration(
            s3_kernel_sha256=h,host_fingerprint=host,
            device_name=rt.device_info.name,workload_kind="conway",
            width=width,height=width,steps=steps,element_bytes=4,
            num_buffers=2,precision="i32_exact",
            resident_between_steps=True,
            cpu_total_ms_samples=tuple(cpu_ms),
            gpu_total_ms_samples=tuple(gpu_ms),
            s3_gpu_result_parity=True,physical_gpu_used=True,readback_verified=True,
        )
        recommended=choose_empirical_gpu_route(
            rt.device_info,host_fingerprint=host,s3_kernel_sha256=h,
            workload_kind="conway",width=width,height=width,steps=steps,
            precision="i32_exact",resident_between_steps=True,evidence=evidence,
            required_speedup=1.2,
        )
        assert recommended.target in ("cpu","gpu")
        cases.append({
            "workload":f"S3 Conway {width}x{width} x {steps}",
            "evidence":asdict(evidence),
            "route":{
                "target":recommended.target,"reason":recommended.reason,
                "cpu_median_ms":recommended.cpu_median_ms,
                "gpu_median_ms":recommended.gpu_median_ms,
                "gpu_over_cpu_ratio":recommended.measured_ratio,
                "safety_qualified":recommended.contract.gpu_workload_qualified,
                "automatic_production_dispatch_enabled":False,
            },
            "gpu_dispatch_samples_ms":dispatch_ms,
            "exact_cell_parity":True,
            "gpu_real_physical":True,
            "safe_per_buffer_bytes":int(start.nbytes),
        })
        print("V12_CALIBRATION",width,"GPU_TARGET",recommended.target,
              "GPU_MS",round(recommended.gpu_median_ms or 0,3),
              "CPU_MS",round(recommended.cpu_median_ms or 0,3),
              "PARITY_PASS",flush=True)
    report={
        "campaign":"S3_V12_GPU_EXACT_WORKLOAD_COST_CALIBRATION",
        "device":asdict(rt.device_info),
        "production_dispatch_changed":False,
        "samples_are_raw_not_synthesized":True,
        "cases":cases,
        "limitations":[
            "Single physical RX580/Vulkan and single local session; repeat before calibrating other hardware.",
            "These measurements qualify only the exact program, width, steps, precision, and host.",
            "CPU reference is vectorized NumPy not a tuned native C implementation.",
            "GPU total includes H2D/dispatch/D2H; no unsafe buffer override.",
        ],
    }
    file=HERE/"gpu_calibration_v12.json"
    file.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("OUTPUT",file)


if __name__=="__main__":
    main()
