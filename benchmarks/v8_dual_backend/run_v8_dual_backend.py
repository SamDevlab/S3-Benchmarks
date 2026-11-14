#!/usr/bin/env python3
"""S3 V8 dual-backend experiment: S3 discovers/verifies once, two backends compile it.

Modes (per eligible function):
  A  S3_CONVENTIONAL_NATIVE        S3 x86-64 backend on the optimised, non-transformed IR
  B  S3_PREDICTIVE_NATIVE          S3 x86-64 backend on the verified transformed IR
  C  GCC_CONVENTIONAL_C            hand-written C11 loop (V7 reference source), gcc -O3
  D  GCC_MANUAL_MATHEMATICAL       hand-written C closed form (V7 reference, __int128), gcc -O3
  E  GCC_S3_AUTOMATIC_MATHEMATICAL C emitted from the SAME transformed IR as B, gcc -O3
  F  GCC_S3_IR_CONVENTIONAL        (extra) C emitted from the SAME IR as A, gcc -O3
     -> A vs F isolates pure backend/codegen quality (same IR, no math);
     -> B vs E isolates backend quality for the *same verified transformation*.

NOTE on D: the V7 manual reference uses __int128 intermediates and wraps/UB on
overflow instead of trapping, so D and E do not share an overflow policy.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import pathlib
import platform
import random
import resource
import statistics
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
WORKSPACE = HERE.parents[2]
S3_ROOT = WORKSPACE / "S3"
sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3 import OptimizationLevel  # noqa: E402
from bootstrap.s3.backends.x86_64 import (  # noqa: E402
    InstructionBudgetMode,
    NativeToolchain,
    generate_ffi_assembly,
)
from bootstrap.s3.c_backend import emit_c_module, manifest_json  # noqa: E402
from bootstrap.s3.codegen import generate_assembly  # noqa: E402
from bootstrap.s3.ir_cleanup import simplify_lowered_ir  # noqa: E402
from bootstrap.s3.lowering import lower  # noqa: E402
from bootstrap.s3.optimizer import optimize_ir  # noqa: E402
from bootstrap.s3.parser import parse  # noqa: E402
from bootstrap.s3.predictive_discovery import discover_ir_patterns  # noqa: E402
from bootstrap.s3.predictive_native_lowering import (  # noqa: E402
    apply_predictive_native_lowering,
    clear_all_predictive_caches,
)
from bootstrap.s3.predictive_verifier import hash_ir_function, hash_source  # noqa: E402
from bootstrap.s3.semantic import analyze  # noqa: E402

GCC_FLAGS = ["-O3", "-fPIC", "-shared"]
MAX_INSTR = 50_000_000

# name -> (argc_mode, extra args)
WORKLOADS = {
    "sum_quasi_parity": (1, []),
    "sum_i2": (1, []),
    "triangular_cubic": (3, [13, -7]),
    "coupled_exchange": (3, [10, -3]),
    "lcg_mod": (3, [7, 1000000007]),
    "fib_mod": (2, [1000000007]),
}
MODES = ["A", "B", "G", "C", "D", "E", "F"]
MODE_NAMES = {
    "A": "S3_CONVENTIONAL_NATIVE",
    "B": "S3_PREDICTIVE_NATIVE",
    "G": "S3_PREDICTIVE_NATIVE_CLEANED_EXACT",
    "C": "GCC_CONVENTIONAL_C",
    "D": "GCC_MANUAL_MATHEMATICAL",
    "E": "GCC_S3_AUTOMATIC_MATHEMATICAL",
    "F": "GCC_S3_IR_CONVENTIONAL (extra)",
}


def _load_v7_refs():
    p = WORKSPACE / "S3-Benchmarks" / "benchmarks" / "v7_native_predictive" / "run_v7_native_predictive.py"
    spec = importlib.util.spec_from_file_location("v7ref", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.C11_CONVENTIONAL_SRC, mod.C11_MATH_ACCEL_SRC


def _ms(t0: float) -> float:
    return round((time.perf_counter() - t0) * 1000.0, 3)


def _gcc(src: pathlib.Path, out: pathlib.Path, extra=()) -> float:
    t0 = time.perf_counter()
    r = subprocess.run(["gcc", *GCC_FLAGS, *extra, "-o", str(out), str(src)], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"gcc failed for {src}:\n{r.stderr[:3000]}")
    return _ms(t0)


def build_artifacts(work: pathlib.Path, src: str) -> dict:
    """Run the full dual-backend pipeline once and return stage timings + artifact paths."""
    stages: dict[str, float] = {}
    clear_all_predictive_caches()
    t = time.perf_counter()
    ast = parse(src)
    sem = analyze(ast)
    ir0 = lower(ast, sem)
    ir_opt = optimize_ir(ir0, OptimizationLevel.O1, allow_fp_reassociation=False)
    stages["FRONTEND_IR_OPT_MS"] = _ms(t)

    t = time.perf_counter()
    discover_ir_patterns(ir_opt, run_empirical_probes=False, allow_quasi_polynomial_parity=True)
    stages["DISCOVERY_ONLY_MS"] = _ms(t)

    t = time.perf_counter()
    low_nocheck = apply_predictive_native_lowering(
        ir_opt, source_text=src, use_cache=False, verify_with_checker=False, allow_quasi_polynomial_parity=True
    )
    stages["DISCOVERY_PLUS_CERT_LOWERING_MS"] = _ms(t)
    t = time.perf_counter()
    low = apply_predictive_native_lowering(
        ir_opt, source_text=src, use_cache=False, verify_with_checker=True, allow_quasi_polynomial_parity=True
    )
    total_checked = (time.perf_counter() - t) * 1000.0
    stages["PROOF_CHECK_MS_ESTIMATE"] = round(max(0.0, total_checked - stages["DISCOVERY_PLUS_CERT_LOWERING_MS"]), 3)
    del low_nocheck

    # --- S3 x86-64 backend (A and B) ---------------------------------------
    tc = NativeToolchain.detect()
    arts: dict[str, pathlib.Path] = {}
    t = time.perf_counter()
    cleaned_module, cleanup_stats = simplify_lowered_ir(low.module)
    stages["IR_CLEANUP_MS"] = _ms(t)
    stages["IR_CLEANUP_STATS"] = cleanup_stats.to_dict()
    for mode, module, extra_kw in (
        ("A", ir_opt, {}),
        ("B", low.module, {}),
        (
            "G",
            cleaned_module,
            {
                "instruction_budget_mode": InstructionBudgetMode.EXACT_SEGMENT,
                "selective_hp_cost_model": True,
            },
        ),
    ):
        t = time.perf_counter()
        asm = generate_ffi_assembly(generate_assembly(module), max_instructions=MAX_INSTR, **extra_kw)
        stages[f"S3_CODEGEN_{mode}_MS"] = _ms(t)
        t = time.perf_counter()
        arts[mode] = tc.build_shared(asm, work / f"mode_{mode}.so")
        stages[f"S3_ASM_LINK_{mode}_MS"] = _ms(t)
        (work / f"mode_{mode}.s").write_text(asm if isinstance(asm, str) else str(asm))

    # --- C emitter (E from transformed IR, F from conventional IR) ----------
    prov = {
        "SOURCE_SHA256": hash_source(src),
        "COMPILER_FLAGS": {
            "PREDICTIVE_EXACT_DEFAULT": False,
            "FP_REASSOCIATION_DEFAULT": False,
            "S3C_NG_DEFAULT": False,
            "EXPERIMENTAL_LICM_DEFAULT": False,
            "SCIENTIFIC_INSTRUCTION_BUDGET": MAX_INSTR,
            "ALLOW_QUASI_POLYNOMIAL_PARITY": True,
            "IR_CLEANUP_MODE": "G_OPT_IN_EXACT_SEGMENT",
        },
        "CERTIFICATES": [
            {
                "PROOF_CERTIFICATE_ID": v.updated_certificate.certificate_id,
                "TRANSFORMATION_ID": v.updated_certificate.transformation_id,
                "SOURCE_IR_HASH": v.updated_certificate.source_ir_sha,
                "TARGET_IR_HASH": v.updated_certificate.target_ir_sha,
                "ARITHMETIC_DOMAIN": v.updated_certificate.arithmetic_domain,
                "CORRECTNESS_CLASS": v.updated_certificate.correctness_class,
                "VERIFICATION_STATUS": v.checker_result,
                "CHECKER_VERSION": v.updated_certificate.checker_version,
                "ACCEPTED": v.accepted,
            }
            for v in low.verdicts
        ],
        "LOWERED_FUNCTIONS": list(low.lowered_functions),
        "SKIPPED_PREDICTIVE_FUNCTIONS": dict(low.skipped_functions),
        "TRANSFORMED_IR_HASHES": {f.name: hash_ir_function(f) for f in low.module.functions},
        "SOURCE_IR_HASHES": {f.name: hash_ir_function(f) for f in ir_opt.functions},
        "S3_COMPILER_COMMIT": subprocess.check_output(["git", "-C", str(S3_ROOT), "rev-parse", "HEAD"], text=True).strip(),
        "GCC_VERSION": subprocess.check_output(["gcc", "--version"], text=True).splitlines()[0],
        "GCC_FLAGS": GCC_FLAGS,
        "BACKEND_VERSION": "s3-c-emitter-v8.0",
        "CORRECTNESS_STATUS": "PENDING_DIFFERENTIAL_VALIDATION",
    }
    art_dir = HERE / "artifacts"
    art_dir.mkdir(parents=True, exist_ok=True)
    for mode, module in (("E", low.module), ("F", ir_opt)):
        t = time.perf_counter()
        res = emit_c_module(module, provenance={**prov, "MODE": mode})
        stages[f"C_TRANSLATION_{mode}_MS"] = _ms(t)
        c_path = work / f"generated_optimized_{mode}.c"
        c_path.write_text(res.c_source)
        (work / f"generated_optimized_{mode}.h").write_text(res.c_header)
        (work / f"translation_manifest_{mode}.json").write_text(manifest_json(res.manifest))
        stages[f"GCC_COMPILE_{mode}_MS"] = _gcc(c_path, work / f"mode_{mode}.so", extra=["-w"])
        arts[mode] = work / f"mode_{mode}.so"
        if mode == "E":
            opt_c = art_dir / "generated_optimized.c"
            opt_h = art_dir / "generated_optimized.h"
            opt_so = art_dir / "generated_optimized.so"
            opt_elf = art_dir / "generated_optimized.elf"
            opt_c.write_text(res.c_source)
            opt_h.write_text(res.c_header)
            opt_so.write_bytes(arts["E"].read_bytes())
            # Compile standalone ELF via separate translation units (no LTO inlining).
            obj_c = work / "generated_optimized.o"
            obj_m = work / "elf_main_v8.o"
            t_elf = time.perf_counter()
            subprocess.run(["gcc", "-O3", "-c", "-w", str(opt_c), "-o", str(obj_c)], check=True)
            subprocess.run(["gcc", "-O2", "-c", "-I", str(art_dir), str(HERE / "elf_main_v8.c"), "-o", str(obj_m)], check=True)
            subprocess.run(["gcc", "-o", str(opt_elf), str(obj_c), str(obj_m)], check=True)
            stages["GCC_BUILD_ELF_MS"] = _ms(t_elf)
            e_manifest = dict(res.manifest)
            e_manifest["C_SHARED_OBJECT_SHA256"] = hashlib.sha256(opt_so.read_bytes()).hexdigest()
            e_manifest["ELF_EXECUTABLE_SHA256"] = hashlib.sha256(opt_elf.read_bytes()).hexdigest()
            e_manifest["ELF_BUILD_FLAGS"] = ["gcc -O3 -c (module)", "gcc -O2 -c (harness, separate TU)"]
            (art_dir / "translation_manifest.json").write_text(manifest_json(e_manifest))
            arts["E_ELF"] = opt_elf
            arts["E_MANIFEST"] = art_dir / "translation_manifest.json"
        if res.skipped_functions and mode == "E":
            stages["E_SKIPPED_FUNCTIONS"] = {k: v for k, v in res.skipped_functions.items()}

    # --- hand-written C references (C, D) -----------------------------------
    c_src, d_src = _load_v7_refs()
    for mode, text in (("C", c_src), ("D", d_src)):
        p = work / f"manual_{mode}.c"
        p.write_text(text)
        stages[f"GCC_COMPILE_{mode}_MS"] = _gcc(p, work / f"mode_{mode}.so")
        arts[mode] = work / f"mode_{mode}.so"

    # noop baseline and driver
    _gcc(HERE / "noop.c", work / "noop.so")
    subprocess.run(["gcc", "-O2", "-o", str(work / "driver"), str(HERE / "bench_driver_v8.c"), "-ldl"], check=True)
    stages["PEAK_RSS_KB_BUILD_PROCESS"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return {
        "stages": stages,
        "arts": arts,
        "prov": prov,
        "ir_opt": ir_opt,
        "low": low,
        "work": work,
    }


def run_driver(work: pathlib.Path, so: pathlib.Path, fn: str, mode: int, T: int, extra, batch=None, nbatches=0) -> dict:
    cmd = [str(work / "driver")]
    if batch is None:
        cmd += ["verify", str(so), fn, str(mode), str(T)]
    else:
        cmd += ["bench", str(so), fn, str(mode), str(T), str(batch), str(nbatches)]
    cmd += [str(x) for x in extra]
    return json.loads(subprocess.check_output(cmd, text=True))


def calibrate_batch(work, so, fn, mode, T, extra, target_ms=2.0) -> int:
    r = run_driver(work, so, fn, mode, T, extra, batch=8, nbatches=3)
    per_ns = max(statistics.median(r["per_call_ns"]), 1.0)
    return int(max(8, min(5_000_000, target_ms * 1e6 / per_ns)))


def boot_ci(xs, iters=2000, seed=1234):
    rng = random.Random(seed)
    meds = sorted(statistics.median(rng.choices(xs, k=len(xs))) for _ in range(iters))
    return meds[int(0.025 * iters)], meds[int(0.975 * iters) - 1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=7)
    ap.add_argument("--batches", type=int, default=15)
    ap.add_argument("--T", type=int, nargs="+", default=[1000, 10000, 1000000])
    ap.add_argument("--out", default=str(HERE / "results_v8_dual_backend.json"))
    ap.add_argument("--functions", nargs="+", default=list(WORKLOADS))
    args = ap.parse_args()

    src = (HERE / "corpus_v8.s3").read_text()
    work = pathlib.Path(tempfile.mkdtemp(prefix="s3v8_"))
    built = build_artifacts(work, src)
    arts, stages = built["arts"], built["stages"]

    env = {
        "cpu": next((l.split(":", 1)[1].strip() for l in open("/proc/cpuinfo") if l.startswith("model name")), "?"),
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "gcc": built["prov"]["GCC_VERSION"],
        "gcc_flags": GCC_FLAGS,
        "s3_commit": built["prov"]["S3_COMPILER_COMMIT"],
        "rounds": args.rounds,
        "batches_per_round": args.batches,
        "inputs": "T + (i & 15) cycled at run time; xor-folded into volatile sink",
    }
    clock = json.loads(subprocess.check_output([str(work / "driver"), "clock"], text=True))

    # Independent differential verification against mathematical formulas & ELF
    def _ref_py(fn_name: str, args: list[int]) -> int:
        n = args[0]
        if fn_name == "sum_quasi_parity":
            return 5 + sum(((i * i + 3 * i + 1) // 2) for i in range(max(0, n)))
        if fn_name == "sum_i2":
            return sum(i * i for i in range(max(0, n)))
        if fn_name == "triangular_cubic":
            _, s2, s1 = args
            for i in range(max(0, n)):
                s1 += i * i
                s2 += s1
            return s2
        if fn_name == "coupled_exchange":
            _, x, y = args
            total = 0
            for i in range(max(0, n)):
                flux = x - y + i
                x -= flux
                y += flux
                total += x + y
            return total
        if fn_name == "lcg_mod":
            _, x0, m = args
            x = x0
            for _ in range(max(0, n)):
                nxt = 3 * x + 5
                q = (abs(nxt) // abs(m)) * (-1 if (nxt < 0) ^ (m < 0) else 1)
                x = nxt - q * m
            return x
        if fn_name == "fib_mod":
            _, m = args
            a, b = 0, 1
            for _ in range(max(0, n)):
                s = a + b
                q = (abs(s) // abs(m)) * (-1 if (s < 0) ^ (m < 0) else 1)
                a, b = b, s - q * m
            return a
        raise KeyError(fn_name)

    indep_checks: dict[str, bool] = {}
    elf_path = arts["E_ELF"]
    for fn_name, (argc_mode, extra_args) in WORKLOADS.items():
        all_ok = True
        for tv in (-2, 0, 1, 17, 250):
            call_args = [tv, *extra_args] if argc_mode > 1 else [tv]
            expected = _ref_py(fn_name, call_args)
            got_elf = int(subprocess.check_output([str(elf_path), "call", fn_name, *[str(x) for x in call_args]], text=True).strip())
            if got_elf != expected:
                all_ok = False
                break
        indep_checks[fn_name] = all_ok
    trap_check = subprocess.run([str(elf_path), "call", "lcg_mod", "5", "3", "0"], capture_output=True)
    indep_checks["lcg_mod_div0_traps"] = trap_check.returncode != 0
    ovf_check = subprocess.run([str(elf_path), "call", "triangular_cubic", "1000000", str((1 << 63) - 1), "1"], capture_output=True)
    indep_checks["triangular_cubic_overflow_traps"] = ovf_check.returncode != 0

    direct_rounds = [
        json.loads(subprocess.check_output([str(elf_path), "bench-direct", "10000", "200000"], text=True))
        for _ in range(args.rounds)
    ]
    direct_summary = {
        k: round(statistics.median(r[k] for r in direct_rounds), 4)
        for k in ("noop_direct_ns", "sum_quasi_parity_direct_ns", "sum_i2_direct_ns", "triangular_cubic_direct_ns")
    }

    results = []
    for fn in args.functions:
        mode, extra = WORKLOADS[fn]
        for T in args.T:
            if fn == "triangular_cubic" and T > 10000:
                continue
            row: dict = {"function": fn, "T": T, "extra_args": extra, "modes": {}}
            # correctness: identical checksums across all implementations that are in-domain
            checks = {m: run_driver(work, arts[m], fn, mode, T, extra) for m in MODES}
            ref = checks["A"]
            row["correctness"] = {MODE_NAMES[m]: (checks[m] == ref) for m in MODES}
            row["checksum_reference_mode_A"] = ref
            noop_fn = f"noop{mode}"
            noop_batch = calibrate_batch(work, work / "noop.so", noop_fn, mode, T, extra)
            batches = {}
            for m in MODES:
                batches[m] = calibrate_batch(work, arts[m], fn, mode, T, extra)
            samples = {m: [] for m in MODES}
            noop_samples: list[float] = []
            for rnd in range(args.rounds):
                order = MODES[rnd % len(MODES):] + MODES[: rnd % len(MODES)]  # rotate
                r = run_driver(work, work / "noop.so", noop_fn, mode, T, extra, batch=noop_batch, nbatches=args.batches)
                noop_samples.append(statistics.median(r["per_call_ns"]))
                for m in order:
                    r = run_driver(work, arts[m], fn, mode, T, extra, batch=batches[m], nbatches=args.batches)
                    samples[m].append(statistics.median(r["per_call_ns"]))
            noop_med = statistics.median(noop_samples)
            for m in MODES:
                xs = samples[m]
                lo, hi = boot_ci(xs)
                row["modes"][m] = {
                    "name": MODE_NAMES[m],
                    "median_ns": round(statistics.median(xs), 4),
                    "mean_ns": round(statistics.fmean(xs), 4),
                    "stdev_ns": round(statistics.pstdev(xs), 4),
                    "min_ns": round(min(xs), 4),
                    "max_ns": round(max(xs), 4),
                    "ci95_ns": [round(lo, 4), round(hi, 4)],
                    "batch_calls": batches[m],
                    "round_medians_ns": [round(x, 4) for x in xs],
                    "above_noise_floor": statistics.median(xs) > 3.0 * max(noop_med, clock["back_to_back_median_ns"] / max(batches[m], 1)),
                }
            row["call_overhead_noop_median_ns"] = round(noop_med, 4)
            row["call_overhead_noop_round_medians_ns"] = [round(x, 4) for x in noop_samples]
            results.append(row)
            print(fn, T, {m: row["modes"][m]["median_ns"] for m in MODES}, "noop", row["call_overhead_noop_median_ns"], flush=True)

    all_verified = all(indep_checks.values()) and all(all(r["correctness"].values()) for r in results)
    final_status = "VERIFIED_DIFFERENTIAL_PARITY" if all_verified else "FAILED_VALIDATION"
    built["prov"]["CORRECTNESS_STATUS"] = final_status
    manifest_path = arts["E_MANIFEST"]
    mdata = json.loads(manifest_path.read_text())
    mdata["CORRECTNESS_STATUS"] = final_status
    manifest_path.write_text(json.dumps(mdata, indent=2))

    out = {
        "environment": env,
        "clock": clock,
        "stage_timings_ms": stages,
        "artifact_dir": str(work),
        "independent_differential_checks": indep_checks,
        "direct_vs_ffi_overhead_ns": direct_summary,
        "provenance": {k: v for k, v in built["prov"].items() if k != "TRANSFORMED_IR_HASHES" and k != "SOURCE_IR_HASHES"},
        "transformed_ir_hashes": built["prov"]["TRANSFORMED_IR_HASHES"],
        "source_ir_hashes": built["prov"]["SOURCE_IR_HASHES"],
        "artifact_sizes_bytes": {MODE_NAMES[m]: arts[m].stat().st_size for m in MODES}
        | {"ELF_EXECUTABLE": arts["E_ELF"].stat().st_size},
        "results": results,
    }
    pathlib.Path(args.out).write_text(json.dumps(out, indent=2, default=str))
    print("wrote", args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
