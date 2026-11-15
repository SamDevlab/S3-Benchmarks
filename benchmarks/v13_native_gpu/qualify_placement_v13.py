#!/usr/bin/env python3
"""Feed three actual Windows RX580/C sessions into S3's V12 fail-closed planner.

No GPU work is dispatched here; the original three files each contain
physical S3 WGSL Vulkan dispatch/readback with independent native-C parity.
These are short consecutive sessions on one host, not independent machines
or a production-grade statistical validation.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]/"S3"
sys.path.insert(0,str(ROOT))
from bootstrap.s3.gpu import compile_s3_to_wgsl
from bootstrap.s3.gpu.eligibility import GpuEligibilityReport
from bootstrap.s3.gpu.cost_dispatch_v12 import (
    WorkloadFootprint,PhysicalCalibration,qualify_device_placement,
)

def run():
    paths=[
        HERE/"results_gpu_vs_native_c_v13.json",
        HERE/"results_gpu_vs_native_c_v13_s2.json",
        HERE/"results_gpu_vs_native_c_v13_s3.json",
    ]
    sessions=[json.loads(f.read_text("utf-8")) for f in paths]
    src=(ROOT/"examples"/"gpu_v3"/"conway_gpu.s3").read_text("utf-8")
    kernel=compile_s3_to_wgsl(
        src,"conway_gpu",allow_narrowing=True,workgroup_size=(8,8,1),
    )
    info=sessions[0]["device"]
    assert all(
        s["device"]==info and
        s["sessions"]==1 and
        s["rounds_per_case"]==7 and
        s["automatic_production_gpu_dispatch"] is False and
        s["windows_cpu_native_c_comparison"] is True
        for s in sessions
    )
    assert info["is_physical"] and info["backend"]=="Vulkan"
    availability=GpuEligibilityReport(
        eligible=True,function_name="conway_gpu",
        reason="S3 WGSL lowering succeeded and actual GPU parity recorded",
        narrowing_contract=kernel.narrowing_contract,
        slice_params=(),scalar_params=(),
    )
    results=[]
    for index in range(len(sessions[0]["cases"])):
        first=sessions[0]["cases"][index]
        workload=WorkloadFootprint(
            kernel_hash=kernel.gpu_kernel_hash,
            device_id=f"{info['name']}|{info['driver']}|{info['backend']}",
            width=first["width"],height=first["height"],
            iterations=first["steps"],
            upload_bytes=first["buffer_bytes"],
            readback_bytes=first["buffer_bytes"],
            resident=True,precision_contract=kernel.narrowing_contract,
        )
        points=[]
        for i,session in enumerate(sessions):
            row=session["cases"][index]
            assert (
                row["width"]==workload.width and
                row["height"]==workload.height and
                row["steps"]==workload.iterations and
                row["buffer_bytes"]==workload.upload_bytes and
                row["physical_gpu_parity"] and row["native_c_parity"]
            )
            points.append(PhysicalCalibration(
                footprint=workload,session_id=f"physical-run-{i+1}",
                round_count=session["rounds_per_case"],
                physical_gpu=session["device"]["is_physical"],
                parity_passed=True,cpu_comparator="native_c",
                cpu_total_ms=row["native_c_total_ms"],
                gpu_total_ms=row["gpu_total_ms"],
            ))
        decision=qualify_device_placement(
            availability,workload,tuple(points),
            enable_experimental=True,minimum_independent_sessions=3,
            required_speedup=1.25,
        )
        assert decision.selected=="CPU"
        assert decision.automatic_production_dispatch is False
        results.append({
            "width":workload.width,"height":workload.height,
            "iterations":workload.iterations,
            "decision":decision.selected,"reason":decision.reason,
            "accepted_sessions":decision.accepted_sessions,
            "worst_gpu_ms":decision.worst_gpu_ms,
            "best_cpu_ms":decision.best_cpu_ms,
            "session_ratios_gpu_over_native_c":[
                p.gpu_total_ms/p.cpu_total_ms for p in points
            ],
        })
        print(f"PLACEMENT W{workload.width} STEPS{workload.iterations}: "
              f"{decision.selected} {decision.reason} sessions={decision.accepted_sessions}",
              flush=True)
    report={
        "campaign":"S3_V13_ACTUAL_HARDWARE_CPU_GPU_SELECTION",
        "status":"EXPERIMENTAL_CORRECT_CPU_PLACEMENT_NOT_PRODUCTION",
        "physical_gpu":True,"cpu_reference":"native Windows C -O3",
        "same_host_distinct_process_sessions":3,
        "independent_machines":1,
        "gpu_kernel_hash":kernel.gpu_kernel_hash,
        "original_s3_source_hash":kernel.s3_source_hash,
        "precision_contract":kernel.narrowing_contract,
        "automatic_production_dispatch":False,
        "cases":results,
    }
    path=HERE/"results_placement_v13.json"
    path.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print("RESULT_FILE="+str(path),flush=True)

if __name__=="__main__":
    run()
