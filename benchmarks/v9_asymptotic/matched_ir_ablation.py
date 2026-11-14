#!/usr/bin/env python3
"""S3 V9 opt-in ablation: native S3 and GCC compile the same mathematical IR.

Key correction to V8: Mode E GCC compiles *uncleaned* predictive IR, whereas
Mode G S3 compiles *cleaned* IR; E/G are not a literal equal-IR comparison.

Here we rebuild them and additionally benchmark GCC cleaned (H) and S3 cleaned
with normal instruction budgeting (J). This is experimental, NOT an equivalence
proof over all S3 programs, nor a full independent source-to-C verification.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import statistics
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
V8 = HERE.parent / "v8_dual_backend"
sys.path.insert(0, str(V8))
import run_v8_dual_backend as v8

from bootstrap.s3.c_backend import emit_c_module, check_c_obligations
from bootstrap.s3.ir_cleanup import simplify_lowered_ir
from bootstrap.s3.predictive_verifier import hash_ir_function
from bootstrap.s3.backends.x86_64 import generate_ffi_assembly
from bootstrap.s3.codegen import generate_assembly

NAMES = {
    "B": "S3_UNCLEANED_DEFAULT",
    "E": "GCC_UNCLEANED",
    "G": "S3_CLEANED_EXACT",
    "H": "GCC_CLEANED",
    "J": "S3_CLEANED_DEFAULT",
}
COMPARE = {"uncleaned": ["B", "E"], "cleaned": ["J", "H"], "cleaned_exact_budget": ["G", "H"]}


def compile_extra(work, built):
    arts = built["arts"]
    low = built["low"]
    # Both backends MUST use these exact shared IRModule objects, no
    # backend-specific mathematical transform in this script.
    cleaned, cleanup_stats = simplify_lowered_ir(low.module)
    if not cleanup_stats.to_dict():
        raise RuntimeError("cleanup stats missing")
    uncleaned_hashes = {f.name: hash_ir_function(f) for f in low.module.functions}
    cleaned_hashes = {f.name: hash_ir_function(f) for f in cleaned.functions}
    native_backend = v8.NativeToolchain.detect()
    result = emit_c_module(cleaned, provenance={
        "IR_SOURCE": "exact same IR as S3 G/J",
        "MATHEMATICAL_FORMULAS_HARDCODED_IN_C_EMITTER": False,
        "CLEANUP_APPLIED": True,
    })
    obligations = check_c_obligations(result.c_source, cleaned, result.exported_functions, c_header=result.c_header)
    if not obligations["ok"]:
        raise RuntimeError("C output structural obligations FAIL: " + str(obligations["problems"]))
    if result.skipped_functions:
        raise RuntimeError("C backend skipped functions: " + str(result.skipped_functions))
    cpath = work / "v9_mode_H.c"
    cpath.write_text(result.c_source, encoding="utf-8")
    arts["H"] = work / "mode_H.so"
    v8._gcc(cpath, arts["H"], extra=["-w"])

    # J is the native S3 backend with the same cleaned IR as H, without
    # G's exact-segment and selective cost-model flags.
    asm_j = generate_ffi_assembly(generate_assembly(cleaned), max_instructions=v8.MAX_INSTR)
    arts["J"] = native_backend.build_shared(asm_j, work / "mode_J.so")

    for mode in NAMES:
        if not arts[mode].is_file():
            raise RuntimeError(f"missing artifact {mode}")

    # Explicit provenance for the modules actually handed to each backend.
    hashes_by_mode = {
        "B": uncleaned_hashes,
        "E": uncleaned_hashes,
        "G": cleaned_hashes,
        "J": cleaned_hashes,
        "H": cleaned_hashes,
    }
    equal_ir_pairs = {
        "B_E": hashes_by_mode["B"] == hashes_by_mode["E"],
        "J_H": hashes_by_mode["J"] == hashes_by_mode["H"],
        "G_H": hashes_by_mode["G"] == hashes_by_mode["H"],
    }
    if not all(equal_ir_pairs.values()):
        raise AssertionError("IR provenance mismatch: " + str(equal_ir_pairs))
    return {
        "artifacts": arts,
        "cleanup": cleanup_stats.to_dict(),
        "structural_C_obligations": obligations["obligations"],
        "hashes_uncleaned": uncleaned_hashes,
        "hashes_cleaned": cleaned_hashes,
        "hashes_by_mode": hashes_by_mode,
        "equal_ir_pairs": equal_ir_pairs,
        "c_source_sha256": hashlib.sha256(result.c_source.encode()).hexdigest(),
    }


def measure(args):
    src = (V8 / "corpus_v8.s3").read_text(encoding="utf-8-sig")
    import tempfile
    with tempfile.TemporaryDirectory(prefix="s3_v9_matched_") as td:
        work = pathlib.Path(td)
        built = v8.build_artifacts(work, src)
        extras = compile_extra(work, built)
        arts = extras["artifacts"]
        status = []
        summary = []
        for fn in args.functions:
            argc_mode, extra_args = v8.WORKLOADS[fn]
            for n in args.N:
                modes = list(NAMES)
                refs = {m: v8.run_driver(work, arts[m], fn, argc_mode, n, extra_args) for m in modes}
                reference = refs["B"]
                matches = {m: (refs[m] == reference) for m in modes}
                if not all(matches.values()):
                    raise AssertionError(f"parity FAIL for {fn} N={n}: {matches!r}")

                batches = {
                    m: v8.calibrate_batch(work, arts[m], fn, argc_mode, n, extra_args, target_ms=1.0)
                    for m in modes
                }
                samples = {m: [] for m in modes}
                for round_idx in range(args.rounds):
                    # Rotate, avoiding a favored fixed ordering.
                    order = modes[round_idx % len(modes):] + modes[:round_idx % len(modes)]
                    for m in order:
                        record = v8.run_driver(
                            work, arts[m], fn, argc_mode, n, extra_args,
                            batch=batches[m], nbatches=args.batches
                        )
                        samples[m].append(statistics.median(record["per_call_ns"]))
                medians = {m: round(statistics.median(values), 4) for m, values in samples.items()}
                row = {
                    "function": fn,
                    "N": n,
                    "input_variation": "N + (i & 15)",
                    "medians_ns": medians,
                    "samples_round_medians_ns": samples,
                    "all_cross_backend_checksums_match": True,
                    "ratios": {
                        "gcc_vs_s3_matched_uncleaned_B_over_E": round(medians["B"] / medians["E"], 4),
                        "gcc_vs_s3_matched_cleaned_J_over_H": round(medians["J"] / medians["H"], 4),
                        "gcc_vs_s3_matched_cleaned_exact_G_over_H": round(medians["G"] / medians["H"], 4),
                        "gcc_cleanup_gain_E_over_H": round(medians["E"] / medians["H"], 4),
                        "s3_cleanup_and_budget_gain_B_over_G": round(medians["B"] / medians["G"], 4),
                    },
                }
                summary.append(row)
                status.append(f"{fn} N={n} B={medians['B']} J={medians['J']} G={medians['G']} E={medians['E']} H={medians['H']}")
        output = {
            "status": "EXPLORATORY_MATCHED_IR_BENCHMARK",
            "complexity_proof": False,
            "semantic_equivalence_proof": False,
            "emitter_verification": "STRUCTURAL_C_OBLIGATIONS_PLUS_DIFFERENTIAL_CHECKSUM",
            "source_commit": subprocess.check_output(["git", "-C", str(v8.S3_ROOT), "rev-parse", "HEAD"], text=True).strip(),
            "naming": NAMES,
            "same_ir_pairing": COMPARE,
            "compiler_runtime_flags_note": "Native G uses exact-segment/selective model; native J uses normal defaults. GCC E/H use -O3. IR equality is claimed only within matching pairs.",
            "all_ir_hashes_after_cleanup": extras["hashes_cleaned"],
            "all_ir_hashes_before_cleanup": extras["hashes_uncleaned"],
            "ir_hashes_by_mode": extras["hashes_by_mode"],
            "equal_ir_pairs_verified": extras["equal_ir_pairs"],
            "structural_C_obligations": extras["structural_C_obligations"],
            "cleaned_c_source_sha256": extras["c_source_sha256"],
            "cleaned_ir_stats": extras["cleanup"],
            "rounds": args.rounds,
            "batches": args.batches,
            "results": summary,
            "caveats": [
                "No universal equivalence proof. Per-function random/adversarial testing is future work.",
                "Sub-microsecond measurement is noisy; repeat in independent clean sessions.",
                "Mathematical transformation and IR cleanup are separate stages.",
                "C manual closed forms may not preserve checked-i64 traps.",
            ],
        }
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(output, indent=2), encoding="utf-8")
        for msg in status:
            print(msg, flush=True)
        print("STATUS=EXPLORATORY_MATCHED_IR; OUTPUT=" + str(args.out), flush=True)
        return output


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--functions", nargs="+", choices=sorted(v8.WORKLOADS), default=["sum_quasi_parity", "lcg_mod", "fib_mod"])
    ap.add_argument("--N", nargs="+", type=int, default=[1000, 10000, 100000])
    ap.add_argument("--rounds", type=int, default=5)
    ap.add_argument("--batches", type=int, default=5)
    ap.add_argument("--out", type=pathlib.Path, default=HERE / "matched_ir_ablation_v9.json")
    args = ap.parse_args()
    if min(args.N) <= 0 or args.rounds < 1 or args.batches < 1:
        ap.error("positive N, rounds and batches required")
    measure(args)


if __name__ == "__main__":
    main()
