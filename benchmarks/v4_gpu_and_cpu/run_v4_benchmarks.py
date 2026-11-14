#!/usr/bin/env python3
"""S3 V4 GPU Performance & Integrity Benchmark (MatMul V1 vs V2 Tiled, Stencil 1..100 steps, Signal/HighLife)."""

from __future__ import annotations

import json
import math
import os
import statistics
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

S3_ROOT = Path(__file__).resolve().parents[3] / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.gpu import (  # noqa: E402
    GpuResidentSession,
    GpuRuntime,
    build_tiled_matmul_kernel,
    compile_s3_to_wgsl,
)


def _atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise


def bench_matmul_v1_vs_v2(rt: GpuRuntime) -> list[dict]:
    mm_v1_src = (S3_ROOT / "examples" / "gpu_v3" / "matmul_gpu.s3").read_text(encoding="utf-8")
    k_v1 = compile_s3_to_wgsl(mm_v1_src, "matmul_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    k_v2 = build_tiled_matmul_kernel(16)
    rng = np.random.default_rng(2026)
    rows = []
    for side in [32, 64, 128, 256, 512]:
        a = rng.standard_normal((side, side), dtype=np.float32)
        b = rng.standard_normal((side, side), dtype=np.float32)
        c = np.zeros((side, side), dtype=np.float32)
        ref = a @ b

        # V1
        r1 = rt.execute(k_v1, {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()}, {"m": side, "n": side, "k_dim": side}, workgroups=(math.ceil(side / 8), math.ceil(side / 8), 1))
        c1 = np.frombuffer(r1.outputs["c"], dtype=np.float32).reshape(side, side)
        diff1 = np.abs(c1 - ref)
        v1_times = [
            rt.execute(k_v1, {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()}, {"m": side, "n": side, "k_dim": side}, workgroups=(math.ceil(side / 8), math.ceil(side / 8), 1))
            for _ in range(3)
        ]

        # V2 Tiled (end-to-end AND resident dispatch-only)
        r2 = rt.execute(k_v2, {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()}, {"m": side, "n": side, "k_dim": side}, workgroups=(math.ceil(side / 16), math.ceil(side / 16), 1))
        c2 = np.frombuffer(r2.outputs["c"], dtype=np.float32).reshape(side, side)
        diff2 = np.abs(c2 - ref)
        v2_times = [
            rt.execute(k_v2, {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()}, {"m": side, "n": side, "k_dim": side}, workgroups=(math.ceil(side / 16), math.ceil(side / 16), 1))
            for _ in range(3)
        ]

        sess = GpuResidentSession(rt, k_v2, {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()}, {"m": side, "n": side, "k_dim": side})
        try:
            _ = sess.dispatch((math.ceil(side / 16), math.ceil(side / 16), 1))
            res_disp = [sess.dispatch((math.ceil(side / 16), math.ceil(side / 16), 1)) * 1000.0 for _ in range(5)]
        finally:
            sess.close()

        cpu_times = []
        for _ in range(5):
            t0 = time.perf_counter()
            _ = a @ b
            cpu_times.append((time.perf_counter() - t0) * 1000.0)

        row = {
            "size": f"{side}x{side}",
            "v1_total_ms": round(statistics.median([x.total_s * 1000.0 for x in v1_times]), 3),
            "v1_dispatch_ms": round(statistics.median([x.dispatch_s * 1000.0 for x in v1_times]), 3),
            "v1_max_diff": float(np.max(diff1)),
            "v2_tiled_total_ms": round(statistics.median([x.total_s * 1000.0 for x in v2_times]), 3),
            "v2_tiled_dispatch_ms": round(statistics.median([x.dispatch_s * 1000.0 for x in v2_times]), 3),
            "v2_resident_dispatch_ms": round(statistics.median(res_disp), 3),
            "v2_max_diff": float(np.max(diff2)),
            "v2_bad_gt_1e2": int(np.sum(diff2 > 1e-2)),
            "cpu_numpy_blas_ms": round(statistics.median(cpu_times), 4),
        }
        rows.append(row)
        print(
            f"MATMUL {side:3d}x{side:3d} | V1={row['v1_total_ms']:.3f}ms | V2={row['v2_tiled_total_ms']:.3f}ms "
            f"(resident_disp={row['v2_resident_dispatch_ms']:.3f}ms) | BLAS={row['cpu_numpy_blas_ms']:.3f}ms | bad={row['v2_bad_gt_1e2']}",
            flush=True,
        )
    return rows


def bench_stencil_steps(rt: GpuRuntime) -> list[dict]:
    src = (S3_ROOT / "examples" / "gpu_v3" / "stencil2d_gpu.s3").read_text(encoding="utf-8")
    k = compile_s3_to_wgsl(src, "stencil2d_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    side = 512
    s_in = np.zeros((side, side), dtype=np.float32)
    s_in[side // 2, side // 2] = 100.0
    rows = []
    for steps in [1, 10, 50, 100]:
        r = rt.execute_pingpong(
            k, "u_in", "u_out",
            {"u_in": s_in.ravel(), "u_out": s_in.copy().ravel()},
            {"w": side, "h": side, "c": 0.1},
            steps=steps,
            workgroups=(side // 8, side // 8, 1),
        )
        t0 = time.perf_counter()
        a, b = s_in.copy(), s_in.copy()
        for _ in range(steps):
            b[1:-1, 1:-1] = a[1:-1, 1:-1] + 0.1 * (
                a[1:-1, :-2] + a[1:-1, 2:] + a[:-2, 1:-1] + a[2:, 1:-1] - 4.0 * a[1:-1, 1:-1]
            )
            a, b = b, a
        cpu_ms = (time.perf_counter() - t0) * 1000.0
        gpu_ms = r.total_s * 1000.0
        g_arr = np.frombuffer(r.outputs["final"], dtype=np.float32).reshape(side, side)
        diff = float(np.max(np.abs(g_arr - a)))
        row = {
            "size": "512x512",
            "steps": steps,
            "gpu_total_ms": round(gpu_ms, 3),
            "cpu_numpy_ms": round(cpu_ms, 3),
            "speedup_vs_numpy": round(cpu_ms / gpu_ms, 3),
            "max_diff": diff,
        }
        rows.append(row)
        print(f"STENCIL 512x512 x{steps:3d} | cpu={cpu_ms:.2f}ms | gpu={gpu_ms:.2f}ms | speedup={row['speedup_vs_numpy']:.2f}x | diff={diff:.2e}", flush=True)
    return rows


def main() -> int:
    rt = GpuRuntime(require_physical=True)
    out_path = Path(__file__).resolve().parent / "results_v4_gpu.json"
    payload = {
        "device": {"name": rt.device_info.name, "backend": rt.device_info.backend, "driver": rt.device_info.driver},
        "matmul_v1_vs_v2": bench_matmul_v1_vs_v2(rt),
        "stencil_multi_step": bench_stencil_steps(rt),
    }
    _atomic_write_json(out_path, payload)
    print(f"Saved: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

