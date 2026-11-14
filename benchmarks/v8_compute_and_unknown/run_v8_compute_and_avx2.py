#!/usr/bin/env python3
"""S3 V8 Compute, AVX2/F64, Cellular Automata & GPU Honesty Suite.

Evaluates:
1. S3 Compute 7-stage lifecycle (`conway_step`, `stencil5point_step`) across:
   - Default (`per-instruction` budget, standard cost model)
   - V7 (`loop-hybrid` + `selective_hp_cost_model`)
   - V8 (`exact-segment` + `selective_hp_cost_model`)
   - GCC -O3 handwritten C11 reference oracle
2. Scientific Numerics / AVX2 & F64:
   - Strict IEEE-754 (`FP_REASSOCIATION_DEFAULT=FALSE`) vs opt-in AVX2/FMA
   - Poisson 2D CG/Jacobi (32x32, 64x64) and F64 vector kernels (`vec_dot`, `vec_axpy`, `vec_scale`, `vec_triad`)
   - Parity and speed comparison vs GCC -O3 strict and GCC -O3 AVX2/FMA
3. Cellular Automata (`GF(2)` Rule 90 fast-forward & Hashlife V3 structured vs chaotic abstention)
4. GPU Qualification honesty (`GPU_BACKEND_STATUS = NOT_IMPLEMENTED_CPU_FALLBACK_ONLY`)
"""

from __future__ import annotations

from array import array
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

BENCH_DIR = Path(__file__).resolve().parent
BENCH_ROOT = BENCH_DIR.parents[1]
S3_ROOT = BENCH_ROOT.parent / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))
sys.path.insert(0, str(BENCH_ROOT / "benchmarks" / "v7_compute_ca_gpu"))
sys.path.insert(0, str(BENCH_ROOT / "benchmarks" / "v7_gcc_reproducibility"))

from run_v7_compute_ca_gpu import (  # noqa: E402
    _measure_gcc_stencil_baseline,
    _measure_seven_stages,
)
from run_v7_poisson_avx2 import (  # noqa: E402
    run_benchmark as run_poisson_avx2_benchmark,
)
from bootstrap.s3.gpu.runtime import execute_with_cpu_fallback  # noqa: E402
from bootstrap.s3.predictive_gf2_s3 import get_s3_gf2_library  # noqa: E402
from bootstrap.s3.predictive_hashlife_v2 import (  # noqa: E402
    HashlifeV3Engine,
    run_hashlife_v3_finite_grid,
)
from bootstrap.s3.predictive_native import get_native_predictive_library  # noqa: E402


def main() -> int:
    conway_src = (S3_ROOT / "examples" / "compute" / "conway.s3").read_text(encoding="utf-8")
    stencil_src = (S3_ROOT / "examples" / "compute" / "stencil5point.s3").read_text(encoding="utf-8")

    w, h, steps = 64, 64, 100
    conway_init = [1 if ((r * 13 + c * 7) % 5 == 0) else 0 for r in range(h) for c in range(w)]
    stencil_init = [(i * 31 + 7) % 256 for i in range(w * h)]

    conway_def = _measure_seven_stages(
        conway_src, "conway_step", w, h, steps, conway_init,
        budget_mode=None, selective_hp=False,
    )
    conway_v7 = _measure_seven_stages(
        conway_src, "conway_step", w, h, steps, conway_init,
        budget_mode="loop-hybrid", selective_hp=True,
    )
    conway_v8 = _measure_seven_stages(
        conway_src, "conway_step", w, h, steps, conway_init,
        budget_mode="exact-segment", selective_hp=True,
    )
    assert conway_def["checksum"] == conway_v7["checksum"] == conway_v8["checksum"]

    stencil_def = _measure_seven_stages(
        stencil_src, "stencil5point_step", w, h, steps, stencil_init,
        budget_mode=None, selective_hp=False,
    )
    stencil_v7 = _measure_seven_stages(
        stencil_src, "stencil5point_step", w, h, steps, stencil_init,
        budget_mode="loop-hybrid", selective_hp=True,
    )
    stencil_v8 = _measure_seven_stages(
        stencil_src, "stencil5point_step", w, h, steps, stencil_init,
        budget_mode="exact-segment", selective_hp=True,
    )
    gcc_stencil = _measure_gcc_stencil_baseline(w, h, steps, stencil_init)
    assert (
        stencil_def["checksum"]
        == stencil_v7["checksum"]
        == stencil_v8["checksum"]
        == gcc_stencil["checksum"]
    )

    # Run Poisson 2D CG/Jacobi & AVX2 F64 Vector Suite (5 trials for fast reproducibility)
    poisson_tmp = BENCH_DIR / "_tmp_poisson_v8.json"
    poisson_res = run_poisson_avx2_benchmark(tag="v8_dual_backend", trials=5, out_path=poisson_tmp)
    if poisson_tmp.exists():
        poisson_tmp.unlink()

    # Cellular Automata GF(2) + Hashlife V3
    gf2 = get_s3_gf2_library()
    gf2_init = [1 if (i % 9 == 0 or i == 17) else 0 for i in range(128)]
    gf2_fast_small = gf2.run_gf2_circulant_fast_forward(gf2_init, rule=90, steps=2000)
    gf2_conv_small = gf2.run_gf2_conventional_ca(gf2_init, rule=90, steps=2000)
    assert list(gf2_fast_small.final_state) == list(gf2_conv_small.final_state)
    gf2_fast_1m = gf2.run_gf2_circulant_fast_forward(gf2_init, rule=90, steps=1_000_000)

    native_ca = get_native_predictive_library()
    rpent = array("q", [0]) * (64 * 64)
    for dr, dc in ((0, 1), (0, 2), (1, 0), (1, 1), (2, 1)):
        rpent[(32 + dr) * 64 + (32 + dc)] = 1
    c11_rpent, _ = native_ca.run_conventional_ca("conway", rpent, 64, 64, 500)
    hl_rpent = run_hashlife_v3_finite_grid(rpent, 64, 64, 500, rule="conway")
    assert list(hl_rpent.final_state) == list(c11_rpent)

    gliders = array("q", [0]) * (128 * 128)
    for br in range(4, 108, 32):
        for bc in range(4, 108, 32):
            for dr, dc in ((0, 1), (1, 2), (2, 0), (2, 1), (2, 2)):
                gliders[(br + dr) * 128 + (bc + dc)] = 1
    hl_gliders = run_hashlife_v3_finite_grid(
        gliders, 128, 128, 4096, rule="conway", engine=HashlifeV3Engine("conway")
    )

    gpu_fallback = execute_with_cpu_fallback(
        device_info=None,
        op_kind="stencil5point",
        num_elements=w * h,
        steps=steps,
        gpu_fn=lambda: None,
        cpu_fallback_fn=lambda: {"fallback_checksum": stencil_v8["checksum"]},
    )

    out = {
        "campaign": "S3_V8_MATHEMATICAL_COMPILER_FUSION",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "fp_reassociation_default": False,
        "gpu_backend_status": "NOT_IMPLEMENTED_CPU_FALLBACK_ONLY",
        "compute_7stage": {
            "conway_64x64_100": {
                "default": conway_def,
                "v7_loop_hybrid_hp": conway_v7,
                "v8_exact_segment_hp": conway_v8,
                "kernel_speedup_v8_vs_default": round(
                    conway_def["stages_ms"]["5_KERNEL"]
                    / max(1e-9, conway_v8["stages_ms"]["5_KERNEL"]),
                    3,
                ),
            },
            "stencil5point_64x64_100": {
                "default": stencil_def,
                "v7_loop_hybrid_hp": stencil_v7,
                "v8_exact_segment_hp": stencil_v8,
                "gcc_o3_native": gcc_stencil,
                "kernel_speedup_v8_vs_default": round(
                    stencil_def["stages_ms"]["5_KERNEL"]
                    / max(1e-9, stencil_v8["stages_ms"]["5_KERNEL"]),
                    3,
                ),
                "s3_v8_vs_gcc_o3_ratio": round(
                    stencil_v8["stages_ms"]["5_KERNEL"] / max(1e-9, gcc_stencil["median_ms"]),
                    3,
                ),
            },
        },
        "poisson_2d_cg_jacobi": [
            r for r in poisson_res["poisson_2d_cg_jacobi"] if r["grid"] in ("32x32", "64x64", "128x128")
        ],
        "vector_f64_kernels": [
            r for r in poisson_res["vector_f64_kernels"] if r["n"] in (4096, 65536)
        ],
        "cellular_automata": {
            "gf2_width128_rule90_2000_steps": {
                "s3_fast_forward_ms": round(gf2_fast_small.execution_ns / 1e6, 4),
                "s3_conventional_ms": round(gf2_conv_small.execution_ns / 1e6, 4),
                "speedup": round(
                    gf2_conv_small.execution_ns / max(1, gf2_fast_small.execution_ns), 2
                ),
                "parity_verified": True,
            },
            "gf2_width128_rule90_1m_steps": {
                "s3_fast_forward_ms": round(gf2_fast_1m.execution_ns / 1e6, 4),
                "accelerated": gf2_fast_1m.accelerated,
            },
            "hashlife_v3_gliders_128x128_4096": {
                "method": hl_gliders.certificate.method_used,
                "accelerated": hl_gliders.accelerated,
                "total_ms": round(hl_gliders.total_ns / 1e6, 4),
            },
            "hashlife_v3_rpentomino_64x64_500_negative_result": {
                "method": hl_rpent.certificate.method_used,
                "accelerated": hl_rpent.accelerated,
                "fallback_reason": hl_rpent.fallback_reason,
                "steps_c11_handoff": hl_rpent.steps_executed_conventionally,
                "total_ms": round(hl_rpent.total_ns / 1e6, 4),
                "parity_with_c11": True,
            },
        },
        "gpu_qualification": {
            "actual_backend": gpu_fallback.actual_backend,
            "fallback_used": gpu_fallback.fallback_used,
            "fallback_reason": gpu_fallback.fallback_reason,
        },
    }
    out_path = BENCH_DIR / "results_v8_compute_and_avx2.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "conway_v8_speedup": out["compute_7stage"]["conway_64x64_100"][
                    "kernel_speedup_v8_vs_default"
                ],
                "stencil_v8_speedup": out["compute_7stage"]["stencil5point_64x64_100"][
                    "kernel_speedup_v8_vs_default"
                ],
                "stencil_s3_v8_vs_gcc_o3": out["compute_7stage"]["stencil5point_64x64_100"][
                    "s3_v8_vs_gcc_o3_ratio"
                ],
                "gf2_speedup": out["cellular_automata"]["gf2_width128_rule90_2000_steps"][
                    "speedup"
                ],
                "gpu_backend_status": out["gpu_backend_status"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
