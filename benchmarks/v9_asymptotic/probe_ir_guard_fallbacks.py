#!/usr/bin/env python3
"""Adversarial S3 IR guard/fallback probes. Does not modify S3 compiler."""
import json
from pathlib import Path

from ir_dynamic_operation_counts import modules_for_corpus, exec_with_count
from bootstrap.s3.ir_emulator import IRExecutionError

HERE = Path(__file__).resolve().parent


def main():
    modules, lowered, _ = modules_for_corpus()
    rows = []
    for n in (16, 64, 256, 1024):
        for label, x0, modulus in (
            ("eligible_positive", 7, 1_000_000_007),
            ("negative_seed", -1, 1_000_000_007),
            ("modulus_one", 7, 1),
            ("negative_modulus", 7, -1_000_000_007),
        ):
            inputs = (n, x0, modulus)
            data = {"N": n, "case": label, "arguments": inputs, "modes": {}}
            for name, module in modules.items():
                try:
                    val, count, elapsed = exec_with_count(module, "lcg_mod", inputs, 1000000)
                    data["modes"][name] = {"result": val, "ir_ops": count["executed_ir_opcodes"]}
                except Exception as exc:
                    data["modes"][name] = {"exception": type(exc).__name__, "message": str(exc)[:180]}
            baseline = data["modes"]["CONVENTIONAL_OPTIMIZED_IR"]
            predictive = data["modes"]["PREDICTIVE_CLEANED_IR"]
            if "result" in baseline and "result" in predictive:
                data["parity"] = baseline["result"] == predictive["result"]
                if not data["parity"]:
                    raise AssertionError(f"counterexample: {data}")
            else:
                data["parity"] = ("exception" in baseline) == ("exception" in predictive)
            data["ratio_conventional_over_cleaned"] = (
                round(baseline["ir_ops"]/predictive["ir_ops"], 3)
                if "ir_ops" in baseline and "ir_ops" in predictive else None
            )
            rows.append(data)
            print(label, n, "ref", baseline, "pred", predictive, "parity", data["parity"], flush=True)
    out = HERE / "ir_guard_fallback_probes_v9.json"
    out.write_text(json.dumps({
        "status": "BOUNDED_IR_ADVERSARIAL_PROBES_NOT_PROOF",
        "cases": rows,
        "limitations": [
            "Finite selected cases only, not a proof of complete semantics or worst case.",
            "Exceptions matched by occurrence, not exact trap semantics or messages.",
            "S3 IR emulator opcode counts are not native CPU instructions.",
        ],
    }, indent=2), encoding="utf-8")
    print(f"WROTE={out}")


if __name__ == "__main__":
    main()
