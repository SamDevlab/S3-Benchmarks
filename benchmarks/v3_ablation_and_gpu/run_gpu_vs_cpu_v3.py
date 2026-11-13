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

from bootstrap.s3.gpu import GpuRuntime, compile_s3_to_wgsl  # noqa: E402


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


def _bench_axpy(rt: GpuRuntime, out_dict: dict) -> None:
    src = (S3_ROOT / "examples" / "gpu_v3" / "axpy_gpu.s3").read_text(encoding="utf-8")
    sizes = [1024, 16384, 65536, 1048576]
    wg_sizes = [64, 128, 256]
    rows = []
    for wg in wg_sizes:
        k = compile_s3_to_wgsl(src, "axpy_gpu", allow_narrowing=True, workgroup_size=(wg, 1, 1))
        for n in sizes:
            x = np.linspace(0.0, 1.0, n, dtype=np.float32)
            y = np.linspace(1.0, 2.0, n, dtype=np.float32)
            ref = 2.5 * x + y
            # Cold
            cold = rt.execute(k, {"x": x, "y": y.copy()}, {"alpha": 2.5, "n": n}, workgroups=(math.ceil(n / wg), 1, 1))
            y_gpu = np.frombuffer(cold.outputs["y"], dtype=np.float32)
            max_diff = float(np.max(np.abs(y_gpu - ref)))
            # Warm GPU (5 trials)
            gpu_h2d, gpu_kd2h, gpu_tot = [], [], []
            for _ in range(5):
                r = rt.execute(k, {"x": x, "y": y.copy()}, {"alpha": 2.5, "n": n}, workgroups=(math.ceil(n / wg), 1, 1))
                gpu_h2d.append(r.h2d_s * 1000.0)
                gpu_kd2h.append(r.kernel_and_d2h_s * 1000.0)
                gpu_tot.append(r.total_s * 1000.0)
            # CPU NumPy (C-vectorized baseline)
            cpu_times = []
            for _ in range(7):
                yc = y.copy()
                t0 = time.perf_counter()
                _ = 2.5 * x + yc
                cpu_times.append((time.perf_counter() - t0) * 1000.0)
            cpu_ms = statistics.median(cpu_times)
            gpu_ms = statistics.median(gpu_tot)
            row = {
                "kernel": "axpy_gpu",
                "n": n,
                "wg": wg,
                "cold_pipeline_ms": round(cold.pipeline_s * 1000.0, 3),
                "warm_h2d_ms": round(statistics.median(gpu_h2d), 3),
                "warm_kd2h_ms": round(statistics.median(gpu_kd2h), 3),
                "warm_total_ms": round(gpu_ms, 3),
                "cpu_numpy_ms": round(cpu_ms, 4),
                "speedup_end_to_end": round(cpu_ms / gpu_ms, 3) if gpu_ms > 0 else 0.0,
                "max_diff": max_diff,
            }
            rows.append(row)
            print(
                f"AXPY n={n:7d} wg={wg:3d} | cpu={cpu_ms:.3f}ms | gpu_tot={gpu_ms:.3f}ms "
                f"(h2d={row['warm_h2d_ms']:.3f} kd2h={row['warm_kd2h_ms']:.3f}) | diff={max_diff:.2e}",
                flush=True,
            )
    out_dict["axpy"] = rows


def _bench_stencil2d(rt: GpuRuntime, out_dict: dict) -> None:
    src = (S3_ROOT / "examples" / "gpu_v3" / "stencil2d_gpu.s3").read_text(encoding="utf-8")
    k = compile_s3_to_wgsl(src, "stencil2d_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    rows = []
    for side in [64, 128, 256, 512]:
        u_in = np.zeros((side, side), dtype=np.float32)
        u_in[side // 2, side // 2] = 100.0
        u_out = u_in.copy()
        cold = rt.execute(
            k,
            {"u_in": u_in.ravel(), "u_out": u_out.ravel()},
            {"w": side, "h": side, "c": 0.1},
            workgroups=(math.ceil(side / 8), math.ceil(side / 8), 1),
        )
        u_gpu = np.frombuffer(cold.outputs["u_out"], dtype=np.float32).reshape(side, side)
        u_ref = u_in.copy()
        u_ref[1:-1, 1:-1] = u_in[1:-1, 1:-1] + 0.1 * (
            u_in[1:-1, :-2] + u_in[1:-1, 2:] + u_in[:-2, 1:-1] + u_in[2:, 1:-1] - 4.0 * u_in[1:-1, 1:-1]
        )
        max_diff = float(np.max(np.abs(u_gpu - u_ref)))

        gpu_tot, gpu_kd2h = [], []
        for _ in range(5):
            r = rt.execute(
                k,
                {"u_in": u_in.ravel(), "u_out": u_out.ravel()},
                {"w": side, "h": side, "c": 0.1},
                workgroups=(math.ceil(side / 8), math.ceil(side / 8), 1),
            )
            gpu_tot.append(r.total_s * 1000.0)
            gpu_kd2h.append(r.kernel_and_d2h_s * 1000.0)

        cpu_times = []
        for _ in range(7):
            t0 = time.perf_counter()
            tmp = u_in.copy()
            tmp[1:-1, 1:-1] = u_in[1:-1, 1:-1] + 0.1 * (
                u_in[1:-1, :-2] + u_in[1:-1, 2:] + u_in[:-2, 1:-1] + u_in[2:, 1:-1] - 4.0 * u_in[1:-1, 1:-1]
            )
            cpu_times.append((time.perf_counter() - t0) * 1000.0)

        cpu_ms = statistics.median(cpu_times)
        gpu_ms = statistics.median(gpu_tot)
        row = {
            "kernel": "stencil2d_gpu",
            "size": f"{side}x{side}",
            "elements": side * side,
            "warm_kd2h_ms": round(statistics.median(gpu_kd2h), 3),
            "warm_total_ms": round(gpu_ms, 3),
            "cpu_numpy_ms": round(cpu_ms, 4),
            "speedup_end_to_end": round(cpu_ms / gpu_ms, 3) if gpu_ms > 0 else 0.0,
            "max_diff": max_diff,
        }
        rows.append(row)
        print(
            f"STENCIL2D {side:3d}x{side:3d} | cpu_np={cpu_ms:.3f}ms | gpu_tot={gpu_ms:.3f}ms | speedup={row['speedup_end_to_end']:.2f}x | diff={max_diff:.2e}",
            flush=True,
        )
    out_dict["stencil2d"] = rows


def _bench_matmul(rt: GpuRuntime, out_dict: dict) -> None:
    src = (S3_ROOT / "examples" / "gpu_v3" / "matmul_gpu.s3").read_text(encoding="utf-8")
    k = compile_s3_to_wgsl(src, "matmul_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    rows = []
    rng = np.random.default_rng(7)
    for side in [64, 128, 256, 512]:
        a = rng.standard_normal((side, side), dtype=np.float32)
        b = rng.standard_normal((side, side), dtype=np.float32)
        c = np.zeros((side, side), dtype=np.float32)
        ref = a @ b
        cold = rt.execute(
            k,
            {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()},
            {"m": side, "n": side, "k_dim": side},
            workgroups=(math.ceil(side / 8), math.ceil(side / 8), 1),
        )
        c_gpu = np.frombuffer(cold.outputs["c"], dtype=np.float32).reshape(side, side)
        max_diff = float(np.max(np.abs(c_gpu - ref)))

        gpu_tot, gpu_kd2h = [], []
        for _ in range(5):
            r = rt.execute(
                k,
                {"a": a.ravel(), "b": b.ravel(), "c": c.ravel()},
                {"m": side, "n": side, "k_dim": side},
                workgroups=(math.ceil(side / 8), math.ceil(side / 8), 1),
            )
            gpu_tot.append(r.total_s * 1000.0)
            gpu_kd2h.append(r.kernel_and_d2h_s * 1000.0)

        cpu_times = []
        for _ in range(5):
            t0 = time.perf_counter()
            _ = a @ b
            cpu_times.append((time.perf_counter() - t0) * 1000.0)

        cpu_ms = statistics.median(cpu_times)
        gpu_ms = statistics.median(gpu_tot)
        row = {
            "kernel": "matmul_gpu",
            "size": f"{side}x{side}",
            "warm_kd2h_ms": round(statistics.median(gpu_kd2h), 3),
            "warm_total_ms": round(gpu_ms, 3),
            "cpu_numpy_blas_ms": round(cpu_ms, 4),
            "speedup_vs_blas": round(cpu_ms / gpu_ms, 3) if gpu_ms > 0 else 0.0,
            "max_diff": max_diff,
        }
        rows.append(row)
        print(
            f"MATMUL {side:3d}x{side:3d} | cpu_blas={cpu_ms:.3f}ms | gpu_tot={gpu_ms:.3f}ms | ratio={row['speedup_vs_blas']:.2f}x | diff={max_diff:.2e}",
            flush=True,
        )
    out_dict["matmul"] = rows


def _bench_wave_and_sobel(rt: GpuRuntime, out_dict: dict) -> None:
    wave_src = (S3_ROOT / "examples" / "gpu_v3" / "wave_2d_gpu.s3").read_text(encoding="utf-8")
    wave_k = compile_s3_to_wgsl(wave_src, "wave2d_step", allow_narrowing=True, workgroup_size=(8, 8, 1))
    sobel_src = (S3_ROOT / "examples" / "gpu_v3" / "image_sobel_gpu.s3").read_text(encoding="utf-8")
    sobel_k = compile_s3_to_wgsl(sobel_src, "sobel_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    conway_src = (S3_ROOT / "examples" / "gpu_v3" / "conway_gpu.s3").read_text(encoding="utf-8")
    conway_k = compile_s3_to_wgsl(conway_src, "conway_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))
    part_src = (S3_ROOT / "examples" / "gpu_v3" / "particles_2d_gpu.s3").read_text(encoding="utf-8")
    part_k = compile_s3_to_wgsl(part_src, "particles_2d_gpu", allow_narrowing=True, workgroup_size=(64, 1, 1))
    stencil_src = (S3_ROOT / "examples" / "gpu_v3" / "stencil2d_gpu.s3").read_text(encoding="utf-8")
    stencil_k = compile_s3_to_wgsl(stencil_src, "stencil2d_gpu", allow_narrowing=True, workgroup_size=(8, 8, 1))

    side = 256
    u_curr = np.zeros((side, side), dtype=np.float32)
    u_curr[128, 128] = 10.0
    u_prev = np.zeros((side, side), dtype=np.float32)
    u_next = np.zeros((side, side), dtype=np.float32)
    rw = rt.execute(
        wave_k,
        {"u_curr": u_curr.ravel(), "u_prev": u_prev.ravel(), "u_next": u_next.ravel()},
        {"w": side, "h": side, "c2": 0.2},
        workgroups=(side // 8, side // 8, 1),
    )
    rs = rt.execute(
        sobel_k,
        {"img_in": u_curr.ravel(), "img_out": u_next.ravel()},
        {"w": side, "h": side},
        workgroups=(side // 8, side // 8, 1),
    )

    # Multi-step Resident Ping-Pong: Stencil 2D 512x512 x 50 steps (GPU resident vs NumPy CPU)
    pp_side, steps = 512, 50
    s_in = np.zeros((pp_side, pp_side), dtype=np.float32)
    s_in[pp_side // 2, pp_side // 2] = 100.0
    s_out = s_in.copy()
    r_pp = rt.execute_pingpong(
        stencil_k,
        "u_in",
        "u_out",
        {"u_in": s_in.ravel(), "u_out": s_out.ravel()},
        {"w": pp_side, "h": pp_side, "c": 0.1},
        steps=steps,
        workgroups=(pp_side // 8, pp_side // 8, 1),
    )
    t_cpu0 = time.perf_counter()
    a, b = s_in.copy(), s_in.copy()
    for _ in range(steps):
        b[1:-1, 1:-1] = a[1:-1, 1:-1] + 0.1 * (
            a[1:-1, :-2] + a[1:-1, 2:] + a[:-2, 1:-1] + a[2:, 1:-1] - 4.0 * a[1:-1, 1:-1]
        )
        a, b = b, a
    cpu_pp_ms = (time.perf_counter() - t_cpu0) * 1000.0
    gpu_pp_ms = r_pp.total_s * 1000.0
    pp_gpu_arr = np.frombuffer(r_pp.outputs["final"], dtype=np.float32).reshape(pp_side, pp_side)
    pp_diff = float(np.max(np.abs(pp_gpu_arr - a)))

    # Conway 512x512 x 50 steps resident ping-pong
    rng = np.random.default_rng(123)
    c_in = rng.integers(0, 2, size=(pp_side, pp_side), dtype=np.int32)
    c_out = np.zeros_like(c_in)
    r_conway_pp = rt.execute_pingpong(
        conway_k,
        "grid_in",
        "grid_out",
        {"grid_in": c_in.ravel(), "grid_out": c_out.ravel()},
        {"w": pp_side, "h": pp_side},
        steps=steps,
        workgroups=(pp_side // 8, pp_side // 8, 1),
    )

    # Particle Lab 2D: 65,536 particles single-step GPU vs Python/NumPy
    n_part = 65536
    px = rng.uniform(1.0, 99.0, size=n_part).astype(np.float32)
    py = rng.uniform(1.0, 99.0, size=n_part).astype(np.float32)
    vx = rng.uniform(-5.0, 5.0, size=n_part).astype(np.float32)
    vy = rng.uniform(-5.0, 5.0, size=n_part).astype(np.float32)
    r_part = rt.execute(
        part_k,
        {"px": px.copy(), "py": py.copy(), "vx": vx.copy(), "vy": vy.copy()},
        {"n": n_part, "dt": 0.016, "gx": 0.0, "gy": -9.8, "box_w": 100.0, "box_h": 100.0},
        workgroups=(math.ceil(n_part / 64), 1, 1),
    )

    out_dict["scientific_labs"] = [
        {"kernel": "wave2d_step", "size": "256x256", "total_ms": round(rw.total_s * 1000.0, 3), "s3_hash": rw.s3_source_hash[:12], "wgsl_hash": rw.gpu_kernel_hash[:12]},
        {"kernel": "sobel_gpu", "size": "256x256", "total_ms": round(rs.total_s * 1000.0, 3), "s3_hash": rs.s3_source_hash[:12], "wgsl_hash": rs.gpu_kernel_hash[:12]},
        {"kernel": "stencil2d_pingpong_50steps", "size": "512x512", "gpu_total_ms": round(gpu_pp_ms, 3), "cpu_numpy_ms": round(cpu_pp_ms, 3), "speedup_vs_numpy": round(cpu_pp_ms / gpu_pp_ms, 3), "max_diff": pp_diff},
        {"kernel": "conway_pingpong_50steps", "size": "512x512", "gpu_total_ms": round(r_conway_pp.total_s * 1000.0, 3)},
        {"kernel": "particles_2d_gpu", "size": f"{n_part}", "gpu_total_ms": round(r_part.total_s * 1000.0, 3)},
    ]
    print(
        f"PINGPONG STENCIL 512x512 x50 | cpu_np={cpu_pp_ms:.2f}ms | gpu={gpu_pp_ms:.2f}ms | speedup={cpu_pp_ms/gpu_pp_ms:.2f}x | diff={pp_diff:.2e}",
        flush=True,
    )
    print(
        f"CONWAY 512x512 x50={r_conway_pp.total_s*1000:.2f}ms | PARTICLES 65536={r_part.total_s*1000:.2f}ms",
        flush=True,
    )


def main() -> int:
    rt = GpuRuntime(require_physical=True)
    out_path = Path(__file__).resolve().parent / "results_gpu_vs_cpu_v3.json"
    payload = {
        "device": {
            "name": rt.device_info.name,
            "vendor": rt.device_info.vendor,
            "driver": rt.device_info.driver,
            "backend": rt.device_info.backend,
            "is_physical": rt.device_info.is_physical,
        }
    }
    _bench_axpy(rt, payload)
    _atomic_write_json(out_path, payload)
    _bench_stencil2d(rt, payload)
    _atomic_write_json(out_path, payload)
    _bench_matmul(rt, payload)
    _atomic_write_json(out_path, payload)
    _bench_wave_and_sobel(rt, payload)
    _atomic_write_json(out_path, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
