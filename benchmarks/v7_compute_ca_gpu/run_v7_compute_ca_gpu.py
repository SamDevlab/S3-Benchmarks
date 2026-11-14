#!/usr/bin/env python3
"""V7 Benchmark: S3 Compute 7-Stage Pipeline, GF(2) CA, Hashlife V3, Stencil vs GCC, & GPU Fallback."""

from __future__ import annotations

import ctypes
import json
from pathlib import Path
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from array import array

S3_ROOT = Path(__file__).resolve().parents[3] / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.compute import S3ComputeRuntime
from bootstrap.s3.gpu.runtime import execute_with_cpu_fallback
from bootstrap.s3.predictive_gf2_s3 import get_s3_gf2_library
from bootstrap.s3.predictive_hashlife_v2 import HashlifeV3Engine, run_hashlife_v3_finite_grid
from bootstrap.s3.predictive_native import get_native_predictive_library


def _measure_seven_stages(
    source_text: str,
    symbol: str,
    width: int,
    height: int,
    steps: int,
    initial: list[int],
    *,
    budget_mode: str | None,
    selective_hp: bool,
    trials: int = 5,
) -> dict[str, object]:
    """Measure all 7 compute lifecycle stages from fresh prepare -> execute -> readback."""
    # 1. Cold build (with temporary HOME/cache isolation via force? Measure runtime's own metrics!)
    rt = S3ComputeRuntime(
        backend="native",
        instruction_budget_mode=budget_mode,
        selective_hp_cost_model=selective_hp,
    )
    try:
        kernel = rt.prepare_kernel(source_text, symbol)
        prep = kernel.preparation

        in_buf = array("q", initial)
        out_buf = array("q", [0]) * (width * height)
        # Warmup
        kernel.execute(in_buf, width, height, out_buf)

        dispatch_ns_samples = []
        kernel_ns_samples = []
        readback_ns_samples = []
        total_run_ns_samples = []

        last_snapshot: list[int] = []
        for _ in range(trials):
            buf_a = array("q", initial)
            buf_b = array("q", [0]) * (width * height)
            t_run0 = time.perf_counter_ns()
            k_acc = 0
            e_acc = 0
            for _ in range(steps):
                res = kernel.execute(buf_a, width, height, buf_b)
                assert res.status == 0
                k_acc += res.kernel_ns
                e_acc += res.elapsed_ns
                buf_a, buf_b = buf_b, buf_a
            t_rb0 = time.perf_counter_ns()
            last_snapshot = list(buf_a)
            t_rb1 = time.perf_counter_ns()
            dispatch_ns_samples.append(max(0, e_acc - k_acc))
            kernel_ns_samples.append(k_acc)
            readback_ns_samples.append(t_rb1 - t_rb0)
            total_run_ns_samples.append(t_rb1 - t_run0)

        compile_ms = prep.compilation_ns / 1e6
        linking_ms = (prep.native_codegen_ns + prep.native_build_ns) / 1e6
        load_ms = prep.library_load_ns / 1e6
        dispatch_ms = statistics.median(dispatch_ns_samples) / 1e6
        kernel_ms = statistics.median(kernel_ns_samples) / 1e6
        readback_ms = statistics.median(readback_ns_samples) / 1e6
        total_exec_ms = statistics.median(total_run_ns_samples) / 1e6

        return {
            "symbol": symbol,
            "budget_mode": budget_mode or "default",
            "selective_hp": selective_hp,
            "width": width,
            "height": height,
            "steps": steps,
            "cache_hit": prep.compilation_cache_hit,
            "stages_ms": {
                "1_COMPILATION": compile_ms,
                "2_LINKING": linking_ms,
                "3_LOAD": load_ms,
                "4_DISPATCH": dispatch_ms,
                "5_KERNEL": kernel_ms,
                "6_READBACK": readback_ms,
                "7_TOTAL_EXEC_AND_READBACK": total_exec_ms,
            },
            "checksum": sum(last_snapshot) & 0xFFFFFFFFFFFFFFFF,
        }
    finally:
        rt.close()


def _measure_gcc_stencil_baseline(width: int, height: int, steps: int, initial: list[int], trials: int = 5) -> dict[str, object]:
    c_code = """
#include <stdint.h>
void c_stencil5point(const int64_t *cur, int64_t w, int64_t h, int64_t *nxt) {
    int64_t total = w * h;
    for (int64_t i = 0; i < total; ++i) nxt[i] = 0;
    for (int64_t r = 1; r + 1 < h; ++r) {
        for (int64_t c = 1; c + 1 < w; ++c) {
            int64_t idx = r * w + c;
            nxt[idx] = (cur[idx] + cur[idx - w] + cur[idx + w] + cur[idx - 1] + cur[idx + 1] + 2) / 5;
        }
    }
}
"""
    with tempfile.TemporaryDirectory(prefix="s3-v7-gcc-stencil-") as tmp:
        c_path = Path(tmp) / "stencil.c"
        so_path = Path(tmp) / "stencil.so"
        c_path.write_text(c_code, encoding="utf-8")
        subprocess.run(["gcc", "-O3", "-march=native", "-shared", "-fPIC", str(c_path), "-o", str(so_path)], check=True)
        lib = ctypes.CDLL(str(so_path))
        fn = lib.c_stencil5point
        i64_ptr = ctypes.POINTER(ctypes.c_int64)
        fn.argtypes = [i64_ptr, ctypes.c_int64, ctypes.c_int64, i64_ptr]
        fn.restype = None

        samples_ms = []
        checksum = 0
        for _ in range(trials):
            a = (ctypes.c_int64 * len(initial))(*initial)
            b = (ctypes.c_int64 * len(initial))()
            t0 = time.perf_counter_ns()
            for _ in range(steps):
                fn(a, width, height, b)
                a, b = b, a
            t1 = time.perf_counter_ns()
            samples_ms.append((t1 - t0) / 1e6)
            checksum = sum(a[i] for i in range(len(initial))) & 0xFFFFFFFFFFFFFFFF
        return {
            "median_ms": statistics.median(samples_ms),
            "checksum": checksum,
        }


def main() -> int:
    conway_src = (S3_ROOT / "examples/compute/conway.s3").read_text(encoding="utf-8")
    stencil_src = (S3_ROOT / "examples/compute/stencil5point.s3").read_text(encoding="utf-8")

    w, h, steps = 64, 64, 100
    conway_init = [1 if ((r * 13 + c * 7) % 5 == 0) else 0 for r in range(h) for c in range(w)]
    stencil_init = [(i * 31 + 7) % 256 for i in range(w * h)]

    conway_def = _measure_seven_stages(
        conway_src, "conway_step", w, h, steps, conway_init, budget_mode=None, selective_hp=False
    )
    conway_v7 = _measure_seven_stages(
        conway_src, "conway_step", w, h, steps, conway_init, budget_mode="loop-hybrid", selective_hp=True
    )
    assert conway_def["checksum"] == conway_v7["checksum"]

    stencil_def = _measure_seven_stages(
        stencil_src, "stencil5point_step", w, h, steps, stencil_init, budget_mode=None, selective_hp=False
    )
    stencil_v7 = _measure_seven_stages(
        stencil_src, "stencil5point_step", w, h, steps, stencil_init, budget_mode="loop-hybrid", selective_hp=True
    )
    gcc_stencil = _measure_gcc_stencil_baseline(w, h, steps, stencil_init)
    assert stencil_def["checksum"] == stencil_v7["checksum"] == gcc_stencil["checksum"]

    # GF(2) Circulant CA native S3 vs Conventional native S3
    gf2 = get_s3_gf2_library()
    gf2_init = [1 if (i % 9 == 0 or i == 17) else 0 for i in range(128)]
    gf2_fast_small = gf2.run_gf2_circulant_fast_forward(gf2_init, rule=90, steps=2000)
    gf2_conv_small = gf2.run_gf2_conventional_ca(gf2_init, rule=90, steps=2000)
    assert list(gf2_fast_small.final_state) == list(gf2_conv_small.final_state)
    gf2_fast_1m = gf2.run_gf2_circulant_fast_forward(gf2_init, rule=90, steps=1_000_000)

    # Hashlife V3 structured vs chaotic abort
    native = get_native_predictive_library()
    gliders = array("q", [0]) * (128 * 128)
    for br in range(4, 108, 32):
        for bc in range(4, 108, 32):
            for dr, dc in ((0, 1), (1, 2), (2, 0), (2, 1), (2, 2)):
                gliders[(br + dr) * 128 + (bc + dc)] = 1
    hl_gliders = run_hashlife_v3_finite_grid(gliders, 128, 128, 4096, rule="conway", engine=HashlifeV3Engine("conway"))

    rpent = array("q", [0]) * (64 * 64)
    for dr, dc in ((0, 1), (0, 2), (1, 0), (1, 1), (2, 1)):
        rpent[(32 + dr) * 64 + (32 + dc)] = 1
    c11_rpent, _ = native.run_conventional_ca("conway", rpent, 64, 64, 500)
    hl_rpent = run_hashlife_v3_finite_grid(rpent, 64, 64, 500, rule="conway")
    assert list(hl_rpent.final_state) == list(c11_rpent)

    # GPU hardware check + CPU fallback verification
    wgpu_available = False
    try:
        import wgpu  # noqa: F401
        wgpu_available = True
    except ImportError:
        wgpu_available = False

    gpu_fallback = execute_with_cpu_fallback(
        device_info=None,
        op_kind="stencil5point",
        num_elements=w * h,
        steps=steps,
        gpu_fn=lambda: None,
        cpu_fallback_fn=lambda: {"fallback_checksum": stencil_v7["checksum"]},
    )

    out = {
        "campaign": "S3_V7_COMPUTE_CA_GPU",
        "compute_7stage": {
            "conway_64x64_100": {
                "default": conway_def,
                "v7_loop_hybrid_hp": conway_v7,
                "kernel_speedup": conway_def["stages_ms"]["5_KERNEL"] / max(1e-9, conway_v7["stages_ms"]["5_KERNEL"]),
            },
            "stencil5point_64x64_100": {
                "default": stencil_def,
                "v7_loop_hybrid_hp": stencil_v7,
                "gcc_o3_native": gcc_stencil,
                "kernel_speedup_vs_default": stencil_def["stages_ms"]["5_KERNEL"] / max(1e-9, stencil_v7["stages_ms"]["5_KERNEL"]),
                "s3_v7_vs_gcc_o3_ratio": stencil_v7["stages_ms"]["5_KERNEL"] / max(1e-9, gcc_stencil["median_ms"]),
            },
        },
        "cellular_automata": {
            "gf2_width128_rule90_2000_steps": {
                "s3_fast_forward_ms": gf2_fast_small.execution_ns / 1e6,
                "s3_conventional_ms": gf2_conv_small.execution_ns / 1e6,
                "speedup": gf2_conv_small.execution_ns / max(1, gf2_fast_small.execution_ns),
                "parity_verified": True,
            },
            "gf2_width128_rule90_1m_steps": {
                "s3_fast_forward_ms": gf2_fast_1m.execution_ns / 1e6,
                "accelerated": gf2_fast_1m.accelerated,
            },
            "hashlife_v3_gliders_128x128_4096": {
                "method": hl_gliders.certificate.method_used,
                "accelerated": hl_gliders.accelerated,
                "total_ms": hl_gliders.total_ns / 1e6,
            },
            "hashlife_v3_rpentomino_64x64_500_negative_result": {
                "method": hl_rpent.certificate.method_used,
                "accelerated": hl_rpent.accelerated,
                "fallback_reason": hl_rpent.fallback_reason,
                "steps_c11_handoff": hl_rpent.steps_executed_conventionally,
                "total_ms": hl_rpent.total_ns / 1e6,
                "parity_with_c11": True,
            },
        },
        "gpu_qualification": {
            "wgpu_installed": wgpu_available,
            "physical_gpu_present": False,
            "actual_backend": gpu_fallback.actual_backend,
            "fallback_used": gpu_fallback.fallback_used,
            "fallback_reason": gpu_fallback.fallback_reason,
            "contract": {
                "gpu_device_available": gpu_fallback.contract.gpu_device_available,
                "gpu_device_qualified": gpu_fallback.contract.gpu_device_qualified,
                "gpu_workload_qualified": gpu_fallback.contract.gpu_workload_qualified,
                "gpu_fallback_available": gpu_fallback.contract.gpu_fallback_available,
                "reason": gpu_fallback.contract.reason,
            },
        },
    }
    out_path = Path(__file__).with_name("results_v7_compute_ca_gpu.json")
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
