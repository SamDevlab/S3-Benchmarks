"""V8 Discovery V4 Dual-Backend Benchmark Addendum.

Measures newly discovered V4 functions (mod 6, 7, 9, 10, 12, 16, LCM mixed divisors
mod 6 & mod 15, loop-local scratch variables, and shifted quadratics) across:
  - A = S3_CONVENTIONAL_NATIVE
  - G = S3_PREDICTIVE_NATIVE_CLEANED_EXACT (simplify_lowered_ir + EXACT_SEGMENT)
  - E = GCC_O3_GENERATED_PREDICTIVE_C (emit_c_module on identical transformed S3 IR)
using the C harness bench_driver_v8 for sub-microsecond accuracy.
"""

from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path
import statistics
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
S3_ROOT = ROOT.parents[2] / "S3"
sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.backends.x86_64 import InstructionBudgetMode, NativeToolchain, generate_ffi_assembly
from bootstrap.s3.c_backend import check_c_obligations, emit_c_module
from bootstrap.s3.codegen import generate_assembly
from bootstrap.s3.ir_cleanup import simplify_lowered_ir
from bootstrap.s3.pipeline import OptimizationLevel, compile_source
from tests.test_s3_v8_discovery_v4 import V8_DISCOVERY_V4_SRC, _ref_oracle

V4_BENCH_FNS = (
    "quasi_m6",
    "quasi_m7",
    "quasi_m9",
    "quasi_m10",
    "quasi_m12",
    "quasi_m16",
    "quasi_lcm_6",
    "quasi_lcm_15_rem",
    "quasi_m6_with_locals",
    "quasi_m6_shifted",
)


def _ensure_driver(build_dir: Path) -> Path:
    drv = build_dir / "bench_driver_v8"
    if not drv.exists():
        subprocess.run(
            ["gcc", "-O3", str(ROOT / "bench_driver_v8.c"), "-o", str(drv), "-ldl", "-lm"],
            check=True,
        )
    return drv


def _run_driver(drv: Path, so: Path, fn: str, n: int, batch: int, reps: int = 9) -> dict:
    ver = json.loads(
        subprocess.check_output([str(drv), "verify", str(so), fn, "1", str(n)], text=True)
    )
    ben = json.loads(
        subprocess.check_output(
            [str(drv), "bench", str(so), fn, "1", str(n), str(batch), str(reps)], text=True
        )
    )
    return {
        "result": ver["first"],
        "verify": ver,
        "median_ns": statistics.median(ben["per_call_ns"]),
    }


def main() -> None:
    build = ROOT / "build_v4_disc"
    build.mkdir(exist_ok=True)
    drv = _ensure_driver(build)
    tc = NativeToolchain.detect()

    comp_a = compile_source(V8_DISCOVERY_V4_SRC, OptimizationLevel.O1, predictive_exact=False)
    comp_b = compile_source(V8_DISCOVERY_V4_SRC, OptimizationLevel.O1, predictive_exact=True)
    cleaned_ir, clean_stats = simplify_lowered_ir(comp_b.ir)
    comp_g = replace(comp_b, ir=cleaned_ir, assembly=generate_assembly(cleaned_ir))

    so_a = build / "mode_A_conv.so"
    so_g = build / "mode_G_pred_cleaned.so"
    so_e = build / "mode_E_gcc_pred.so"

    tc.build_shared(
        generate_ffi_assembly(comp_a.assembly, max_instructions=50_000_000),
        so_a,
    )
    tc.build_shared(
        generate_ffi_assembly(
            comp_g.assembly,
            max_instructions=50_000_000,
            instruction_budget_mode=InstructionBudgetMode.EXACT_SEGMENT,
            selective_hp_cost_model=True,
        ),
        so_g,
    )

    c_res = emit_c_module(comp_b.ir, functions=V4_BENCH_FNS)
    chk = check_c_obligations(c_res.c_source, comp_b.ir, c_res.exported_functions, c_header=c_res.c_header)
    assert chk["ok"], chk["problems"]
    c_file = build / "mode_E_pred.c"
    c_file.write_text(c_res.c_source, encoding="utf-8")
    subprocess.run(
        ["gcc", "-O3", "-march=x86-64-v3", "-shared", "-fPIC", "-Wall", "-Wextra", "-Werror", str(c_file), "-o", str(so_e)],
        check=True,
    )

    horizons = (1_000, 10_000, 1_000_000)
    results: dict = {
        "cleanup_stats": {
            "blocks_before": clean_stats.blocks_before,
            "blocks_after": clean_stats.blocks_after,
            "instructions_before": clean_stats.instructions_before,
            "instructions_after": clean_stats.instructions_after,
        },
        "c_obligations": chk["obligations"],
        "benchmarks": {},
    }

    for fn in V4_BENCH_FNS:
        fn_res = {}
        for n in horizons:
            ref = _ref_oracle(fn, n) if n <= 10_000 else None
            batch_a = 200 if n <= 1_000 else (20 if n <= 10_000 else 1)
            batch_fast = 2000
            ra = _run_driver(drv, so_a, fn, n, batch=batch_a)
            rg = _run_driver(drv, so_g, fn, n, batch=batch_fast)
            re = _run_driver(drv, so_e, fn, n, batch=batch_fast)
            assert ra["result"] == rg["result"] == re["result"], (fn, n, ra["result"], rg["result"], re["result"])
            if ref is not None:
                assert ra["result"] == ref, (fn, n, ra["result"], ref)
            fn_res[str(n)] = {
                "result": ra["result"],
                "A_S3_CONV_NS": round(ra["median_ns"], 2),
                "G_S3_PRED_CLEANED_NS": round(rg["median_ns"], 2),
                "E_GCC_O3_PRED_C_NS": round(re["median_ns"], 2),
                "speedup_G_vs_A": round(ra["median_ns"] / max(rg["median_ns"], 1e-6), 2),
                "speedup_E_vs_A": round(ra["median_ns"] / max(re["median_ns"], 1e-6), 2),
                "ratio_G_over_E": round(rg["median_ns"] / max(re["median_ns"], 1e-6), 2),
            }
        results["benchmarks"][fn] = fn_res

    out_path = ROOT / "results_v8_discovery_v4.json"
    out_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    for fn, d in results["benchmarks"].items():
        print(fn, "1000:", d["1000"], "1000000:", d["1000000"])


if __name__ == "__main__":
    main()
