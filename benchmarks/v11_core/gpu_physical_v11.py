#!/usr/bin/env python3
"""V11 actual S3->WGSL->Vulkan GPU execution on the physical Windows adapter.

Conservative buffer sizes; CPU NumPy comparison; records compiler+dispatch+
readback and accuracy separately. This probes *real* physical GPU dispatch,
not emulation or fallback, and does not change S3 production defaults.
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
from bootstrap.s3.gpu import (
    GpuRuntime, compile_s3_to_wgsl, discover_gpu_devices,
)
from bootstrap.s3.gpu.runtime import qualify_gpu_workload

SIZES=(1024,4096,16384)
ROUNDS=9


def median_ns(fn, rounds=30):
    vals=[]
    for _ in range(rounds):
        t0=perf_counter_ns()
        fn()
        vals.append(perf_counter_ns()-t0)
    return statistics.median(vals)


def run():
    devices=discover_gpu_devices()
    physical=[x for x in devices if x.is_physical]
    if not physical:
        raise RuntimeError("NO_GO_NO_PHYSICAL_GPU: refusing software emulation")
    rt=GpuRuntime(require_physical=True)
    if not rt.device_info.is_physical:
        raise RuntimeError("physical GPU selection failed")
    src=(S3_ROOT/"examples"/"gpu_v3"/"axpy_gpu.s3").read_text(encoding="utf-8")
    t0=perf_counter_ns()
    kernel=compile_s3_to_wgsl(src,"axpy_gpu",allow_narrowing=True,workgroup_size=(64,1,1))
    lowering_ms=(perf_counter_ns()-t0)/1e6
    cases=[]
    for n in SIZES:
        x=np.linspace(0.0,1.0,n,dtype=np.float32)
        y=np.linspace(1.0,2.0,n,dtype=np.float32)
        alpha=2.5
        expected=alpha*x+y
        # Explicitly permit f64 -> f32 because the RX580 shader path
        # uses GPU f32; parity is against a floating-point f32 CPU ref.
        gpu_samples=[]
        diagnostics=[]
        for i in range(ROUNDS):
            res=rt.execute(
                kernel,{"x":x,"y":y},{"alpha":alpha,"n":n},
                workgroups=((n+63)//64,1,1),
            )
            if not (res.gpu_is_physical and res.dispatch_success and res.readback_success):
                raise AssertionError("GPU physical, dispatch and readback must all be true")
            got=np.frombuffer(res.outputs["y"],dtype=np.float32)
            np.testing.assert_allclose(got,expected,rtol=1e-5,atol=1e-5)
            gpu_samples.append(res.total_s*1e6)  # microseconds
            diagnostics.append({
                "pipeline_us":res.pipeline_s*1e6,
                "h2d_us":res.h2d_s*1e6,
                "kernel_d2h_us":res.kernel_and_d2h_s*1e6,
                "total_us":res.total_s*1e6,
                "integrity":res.integrity_verified,
                "physical":res.gpu_is_physical,
            })
        cpu_us=median_ns(lambda: 2.5*x+y)/1000
        decision=qualify_gpu_workload(device_info=rt.device_info,op_kind="axpy",num_elements=n)
        cases.append({
            "N":n,"gpu_total_us_median":round(statistics.median(gpu_samples),4),
            "gpu_total_us_min":round(min(gpu_samples),4),
            "cpu_numpy_us_median":round(cpu_us,4),
            "gpu_over_cpu_total_ratio":round(statistics.median(gpu_samples)/cpu_us,4),
            "wgsl_f32_compiled_from_s3":True,
            "cpu_vs_gpu_f32_parity":True,
            "gpu_physical":True,
            "gpu_dispatch_success":True,
            "gpu_readback_success":True,
            "gpu_qualification":decision.to_dict(),
            "rounds":ROUNDS,"first_and_last_gpu_diagnostics":[diagnostics[0],diagnostics[-1]],
        })
        print("GPU",rt.device_info.name,"N",n,
              "gpu_total_us",cases[-1]["gpu_total_us_median"],
              "cpu_numpy_us",cases[-1]["cpu_numpy_us_median"],
              "phys",True,flush=True)
    report={
        "campaign":"S3_V11_PHYSICAL_GPU_DIAGNOSTIC",
        "status":"REAL_GPU_COMPILE_DISPATCH_READBACK_PARITY_PASS",
        "device":vars(rt.device_info),
        "all_discovered_gpu_devices":[vars(x) for x in devices],
        "f64_to_f32_narrowing_explicit":True,
        "s3_wgsl_lowering_ms":round(lowering_ms,4),
        "workload":"S3 AXPY f32, n<=16384, 64 threads per workgroup",
        "reference":"NumPy vectorized CPU f32, same input arrays",
        "cases":cases,
        "limitations":[
            "Single Windows host and RX580, 9 GPU rounds; not a cross-hardware benchmark.",
            "GPU total includes transfer, memory management and readback; CPU NumPy excludes corresponding copies.",
            "This makes GPU path slower for small transfers; no large-batch speedup claim.",
            "S3 f64 source lowered with allow_narrowing=True; GPU results validated at f32 precision.",
            "No GPU workload beyond provisional S3 buffer safety limits.",
            "This is not automatic GPU dispatch in S3 compiler; it exercises existing opt-in backend.",
        ],
    }
    output=HERE/"results_gpu_physical_v11.json"
    output.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("OUTPUT="+str(output),flush=True)


if __name__=="__main__":
    run()
