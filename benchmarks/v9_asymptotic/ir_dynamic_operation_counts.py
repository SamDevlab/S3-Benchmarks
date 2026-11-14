#!/usr/bin/env python3
"""S3 V9 runtime IR opcode counters using the existing S3 observer interface.

This is REAL DYNAMIC S3 IR opcode counting, NOT native x86-64 instruction counting,
NOT compiler-level formal complexity proof and NOT a wall-clock benchmark.
The existing private S3 IR emulator provides an execution_observer hook to
_execute_function; we invoke it without modifying S3 source/runtime defaults.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import math
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
V8 = HERE.parent / "v8_dual_backend"
sys.path.insert(0, str(V8))
import run_v8_dual_backend as v8

from bootstrap.s3.host_services import HostExecutionContext
from bootstrap.s3.ir_cleanup import simplify_lowered_ir
from bootstrap.s3.ir_emulator import _execute_function
from bootstrap.s3.verifier import verify_ir
from reference_operation_counts import (
    Cost, MODULUS, sum_loop, lcg_loop, fib_loop
)

ARITHMETIC = frozenset(("ADD", "MULTIPLY", "DIVIDE", "NUMERIC_DIFFERENCE", "INVERT"))
CONTROL = frozenset(("JUMP", "BRANCH3", "RETURN"))
DATA = frozenset(("LOAD", "STORE", "MOVE", "CONST", "CONVERT"))


class IRInstructionCounter:
    def __init__(self, module, cap=1_000_000):
        self.index = {
            (f.name, b.name): tuple(ins.opcode.name for ins in b.instructions)
            for f in module.functions for b in f.blocks
        }
        self.cap = cap
        self.total = 0
        self.calls = 0
        self.histogram = Counter()
        self.by_function = Counter()
        self.by_block = Counter()

    def function_call(self, caller, function):
        self.calls += 1

    def instruction(self, function, block, index):
        self.total += 1
        if self.total > self.cap:
            raise RuntimeError("IR instruction budget reached during experimental profiling")
        name = self.index[(function.name, block)][index]
        self.histogram[name] += 1
        self.by_function[function.name] += 1
        self.by_block[function.name + "::" + block] += 1

    def function_return(self, caller, function, result):
        pass

    def stats(self):
        return {
            "executed_ir_opcodes": self.total,
            "function_calls": self.calls,
            "arithmetic_opcodes": sum(self.histogram.get(x, 0) for x in ARITHMETIC),
            "control_opcodes": sum(self.histogram.get(x, 0) for x in CONTROL),
            "data_opcodes": sum(self.histogram.get(x, 0) for x in DATA),
            "opcode_histogram": dict(sorted(self.histogram.items())),
            "per_function": dict(sorted(self.by_function.items())),
        }


def exec_with_count(module, name, args, limit):
    fns = {f.name: f for f in module.functions}
    fn = fns[name]
    observer = IRInstructionCounter(module, cap=limit)
    t0 = time.perf_counter()
    got = _execute_function(
        fns, fn, tuple(args), (),
        {s.id: s.value for s in module.static_strings},
        HostExecutionContext(), observer,
    )
    elapsed = (time.perf_counter() - t0) * 1000
    return got, observer.stats(), round(elapsed, 3)


def modules_for_corpus():
    text = (V8 / "corpus_v8.s3").read_text(encoding="utf-8-sig")
    ast = v8.parse(text)
    sem = v8.analyze(ast)
    ir0 = v8.lower(ast, sem)
    conventional = v8.optimize_ir(ir0, v8.OptimizationLevel.O1, allow_fp_reassociation=False)
    v8.clear_all_predictive_caches()
    low = v8.apply_predictive_native_lowering(
        conventional, source_text=text, use_cache=False, verify_with_checker=True,
        allow_quasi_polynomial_parity=True,
    )
    cleaned, cleanup = simplify_lowered_ir(low.module)
    lowered = set(low.lowered_functions)
    return {
        "CONVENTIONAL_OPTIMIZED_IR": conventional,
        "PREDICTIVE_LOWERED_IR": low.module,
        "PREDICTIVE_CLEANED_IR": cleaned,
    }, lowered, cleanup.to_dict()


def args_for(name, n):
    return [n, *v8.WORKLOADS[name][1]]


def reference(name, n):
    if name == "sum_quasi_parity":
        return sum_loop(n, Cost())
    if name == "lcg_mod":
        return lcg_loop(n, 7, MODULUS, Cost())
    if name == "fib_mod":
        return fib_loop(n, MODULUS, Cost())
    raise KeyError(name)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--N", nargs="+", type=int, default=[4, 16, 64, 256])
    p.add_argument("--functions", nargs="+", choices=["sum_quasi_parity", "lcg_mod", "fib_mod"],
                   default=["sum_quasi_parity", "lcg_mod", "fib_mod"])
    p.add_argument("--max-ir-operations", type=int, default=1_000_000)
    p.add_argument("--out", type=Path, default=HERE / "ir_dynamic_operations_v9.json")
    args = p.parse_args()
    if not args.N or any(n < 0 or n > 10_000 for n in args.N):
        p.error("N must be between 0 and 10000 (avoid huge Python IR-emulator runs)")
    all_modules, lowered_functions, cleanup_stats = modules_for_corpus()
    for name, mod in all_modules.items():
        verify_ir(mod)
    rows = []
    for name in args.functions:
        if name not in lowered_functions:
            raise RuntimeError(f"{name} wasn't transformed by the S3 predictive compiler")
        for n in args.N:
            expected = reference(name, n)
            observations = {}
            for mode, mod in all_modules.items():
                got, stats, elapsed = exec_with_count(mod, name, args_for(name, n), args.max_ir_operations)
                if got != expected:
                    raise AssertionError(f"IR result mismatch: {name} n={n} {mode} got {got} expected {expected}")
                observations[mode] = {
                    "result": got,
                    "counts": stats,
                    "interpreter_ms_not_benchmark": elapsed,
                }
            original = observations["CONVENTIONAL_OPTIMIZED_IR"]["counts"]["executed_ir_opcodes"]
            cleaned = observations["PREDICTIVE_CLEANED_IR"]["counts"]["executed_ir_opcodes"]
            rows.append({
                "function": name,
                "N": n,
                "expected": expected,
                "results_match_independent_reference": True,
                "ir_opcode_count_ratio_conventional_over_cleaned": round(original / cleaned, 4),
                "modes": observations,
            })
            print(f"{name:19s} N={n:>5} conventional_IR_ops={original:>8} "
                  f"predictive_cleaned_IR_ops={cleaned:>8} ratio={original/cleaned:>8.2f}x", flush=True)
    slopes = {}
    for fn in args.functions:
        points = [r for r in rows if r["function"] == fn and r["N"] > 0]
        if len(points) >= 2:
            x = [math.log(r["N"]) for r in points]
            xbar = sum(x)/len(x)
            slopes[fn] = {}
            for mode in all_modules:
                y = [math.log(r["modes"][mode]["counts"]["executed_ir_opcodes"]) for r in points]
                ybar = sum(y)/len(y)
                slopes[fn][mode] = round(sum((a-xbar)*(b-ybar) for a,b in zip(x,y)) /
                                         sum((a-xbar)**2 for a in x), 4)
    data = {
        "classification": "ACTUAL_S3_IR_DYNAMIC_OPCODE_COUNTS_FROM_EXISTING_EMULATOR_OBSERVER",
        "native_machine_instruction_count": "NOT_MEASURED",
        "formal_complexity_proof": False,
        "global_worst_case_complexity": "NOT_PROVED",
        "source_branch": "S3 V8 unchanged experimental compiler",
        "methods": ["CONVENTIONAL_OPTIMIZED_IR", "PREDICTIVE_LOWERED_IR", "PREDICTIVE_CLEANED_IR"],
        "lowered_functions": sorted(lowered_functions),
        "cleanup_stats": cleanup_stats,
        "ir_count_growth_loglog_slopes_empirical_not_proof": slopes,
        "rows": rows,
        "limitations": [
            "Counts executed S3 IR opcodes, not machine instructions, CPU cycles or external host operations.",
            "Only selected in-domain inputs are observed; error/fallback paths could have different complexity.",
            "Emulator interpreter time is diagnostic only and should not be reported as native speed.",
            "IR verifier checks structural correctness; no formal proof of complete fast-path/fallback complexity.",
            "Output size and input bit-cost are not included in this word-cost IR-opcode model.",
        ],
    }
    args.out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print("S3_IR_OPCODE_COUNT_STATUS=SUCCESS_FOR_OBSERVED_INPUTS; " +
          f"ROWS={len(rows)}; OUTPUT={args.out}; PROOF=NO")


if __name__ == "__main__":
    main()
