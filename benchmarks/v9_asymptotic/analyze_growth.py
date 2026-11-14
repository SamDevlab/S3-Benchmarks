#!/usr/bin/env python3
"""V9 Big-O empirical scaling audit. Timing is evidence, NEVER an asymptotic proof.

Read V8/V9 dual-backend results; separate fixed-word algorithmic hypotheses from
empirical effective exponents and explicitly flag near-noise and sparse samples.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = BASE / "v8_dual_backend" / "results_v8_dual_backend.json"
MODE_LABELS = {
    "A": "S3 native loop",
    "B": "S3 native predictive (original)",
    "G": "S3 native predictive (cleaned)",
    "C": "GCC C conventional loop",
    "D": "GCC C handwritten formula",
    "E": "GCC C auto-emitted from S3 IR",
    "F": "GCC C auto-emitted conventional IR",
}
ITERATIVE = frozenset(("A", "C", "F"))
HYPOTHESIS = {
    "sum_quasi_parity": "O(1)",
    "sum_i2": "O(1)",
    "triangular_cubic": "O(1)",
    "coupled_exchange": "O(1)",
    "lcg_mod": "O(log N)",
    "fib_mod": "O(log N)",
}
WARNINGS = [
    "Big O CANNOT be inferred or formally proved from runtime measurements alone.",
    "All complexity hypotheses assume unit-cost fixed-width integer arithmetic and valid in-domain N.",
    "With finite i64 inputs, these are idealized algorithm families, not a literal N -> infinity claim.",
    "For arbitrary-precision inputs, bit complexity must also account for operand widths and multiplication.",
    "A measured effective exponent is not an asymptotic proof, especially with 3 data points.",
    "Constant-time or logarithmic kernels can be dominated by invocation overhead in this range.",
    "C handwritten formulas (D) can have different checked-overflow semantics from S3/GCC auto code (E).",
    "Only comparable inputs, correctness status, CPU, compiler flags and measurement scopes may be compared.",
    "Predictive fast-path O(1)/O(log N) estimates are CONDITIONAL; a guarded fallback can remain O(N).",
    "Global worst-case complexity across all valid inputs has NOT been established.",
]


def fit_loglog(points: list[dict]) -> float | None:
    if len(points) < 2:
        return None
    xx = [math.log(row["N"]) for row in points]
    yy = [math.log(row["median_ns"]) for row in points]
    mx = statistics.fmean(xx)
    my = statistics.fmean(yy)
    denominator = sum((x - mx) ** 2 for x in xx)
    return sum((x - mx) * (y - my) for x, y in zip(xx, yy)) / denominator if denominator else None


def caveats(rows: list[dict], high_slope: float | None) -> list[str]:
    out = []
    if len(rows) < 5:
        out.append("SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION")
    if any(not r["above_noise_floor"] for r in rows):
        out.append("TIMING_CLOSE_TO_NOISE_FLOOR")
    if rows[-1]["median_ns"] < 100.0:
        out.append("VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE")
    if high_slope is not None and 0.07 < high_slope < 0.35:
        out.append("SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG")
    if rows[-1]["N"] / rows[0]["N"] < 100:
        out.append("INPUT_RANGE_TOO_NARROW")
    return out


def parse_input(path: Path, coll: dict) -> dict:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if "results" not in data:
        raise ValueError(f"{path}: expected results[]")
    accepted, rejected = 0, 0
    for row in data["results"]:
        fn = row.get("function") or row.get("workload")
        n = row.get("T")
        if fn not in HYPOTHESIS or not isinstance(n, int) or n <= 0:
            rejected += 1
            continue
        for mode, record in row["modes"].items():
            if mode not in MODE_LABELS:
                continue
            if isinstance(record, dict) and "median_ns" in record:
                ns = float(record["median_ns"])
            else:
                continue
            if not math.isfinite(ns) or ns <= 0:
                rejected += 1
                continue
            ok = row.get("correctness", {}).get(MODE_LABELS[mode])
            # V8 correctness keys use full names, so also use result's source name.
            if ok is None:
                ok = row.get("correctness", {}).get(record.get("name"))
            if ok is False:
                rejected += 1
                continue
            coll[(fn, mode, n)] = {
                "N": n,
                "median_ns": ns,
                "above_noise_floor": bool(record.get("above_noise_floor", True)),
                "source": str(path),
            }
            accepted += 1
    return {"file": str(path), "accepted": accepted, "skipped": rejected, "environment": data.get("environment", {})}


def analyze(paths: list[Path]) -> dict:
    coll: dict = {}
    sources = [parse_input(p, coll) for p in paths]
    groups = defaultdict(list)
    for (fn, mode, _), record in coll.items():
        groups[(fn, mode)].append(record)
    out = []
    for (fn, mode), points in sorted(groups.items()):
        points.sort(key=lambda a: a["N"])
        slope = fit_loglog(points)
        last3 = points[-min(3, len(points)):]
        high_slope = fit_loglog(last3)
        predicted = "O(N)" if mode in ITERATIVE else HYPOTHESIS[fn]
        first, last = points[0], points[-1]
        out.append({
            "function": fn,
            "mode": mode,
            "mode_description": MODE_LABELS[mode],
            "algorithmic_hypothesis_not_proof": predicted,
            "complexity_scope": "ITERATIVE_REFERENCE" if mode in ITERATIVE else "CONDITIONAL_OPTIMIZED_FAST_PATH_NOT_WORST_CASE_PROOF",
            "observed_loglog_slope_all": round(slope, 4) if slope is not None else None,
            "observed_loglog_slope_high_window": round(high_slope, 4) if high_slope is not None else None,
            "N_first": first["N"],
            "N_last": last["N"],
            "N_factor": round(last["N"] / first["N"], 2),
            "runtime_growth_factor": round(last["median_ns"] / first["median_ns"], 4),
            "sample_count": len(points),
            "flags": caveats(points, high_slope),
            "samples": points,
        })
    return {
        "status": "EMPIRICAL_SCALING_AUDIT_ONLY",
        "complexity_certification": "NOT_PROVED",
        "sources": sources,
        "warnings": WARNINGS,
        "rows": out,
    }


def markdown(data: dict) -> str:
    lines = [
        "# S3 V9 — Empirical Big-O Scaling Audit",
        "",
        "**Classification: empirical observations, NOT mathematical proof of Big O.**",
        "",
        "## Results",
        "",
        "| Function | Backend | Hypothesis* | N range | Runtime growth | Effective p, all | Effective p, high | Caution |",
        "|---|---|---|---|---:|---:|---:|---|",
    ]
    for row in data["rows"]:
        fs = ", ".join(row["flags"]) or "—"
        fmt = lambda x: "n/a" if x is None else f"{x:.3f}"
        lines.append(
            f"| {row['function']} | {row['mode']} | {row['algorithmic_hypothesis_not_proof']} | "
            f"{row['N_first']}–{row['N_last']} ({row['sample_count']} points) | "
            f"{row['runtime_growth_factor']:.2f}× | {fmt(row['observed_loglog_slope_all'])} | "
            f"{fmt(row['observed_loglog_slope_high_window'])} | {fs} |"
        )
    lines += [
        "",
        "*Algorithmic hypotheses come from the known loop vs closed-form/matrix-exponentiation structure, "
        "NOT from time fitting. The A/C/F family uses an N-step loop; B/D/E/G use a closed form "
        "for polynomial/quasi-polynomial functions and logarithmic repeated squaring for modular LCG/Fibonacci.*",
        "",
        "The observed p is a log-log slope (d log time / d log N), not a proof.",
        "For finite n, constant call overhead, caches, loop setup and noise can dominate.",
        "",
        "## Interpretation guide",
        "",
        "- An O(N) loop typically tends toward p≈1 when the measured cost is dominated by the loop.",
        "- A closed-form O(1) kernel tends toward p≈0 in a fixed-word model.",
        "- O(log N) may also have p near 0 over limited inputs; distinguish via source-level structure and broader sweeps.",
        "- O(N²) tends toward p≈2 only when n² work dominates, which is not established by this suite.",
        "- For a numeric value N represented in L bits, O(log N)=O(L), O(N)=O(2^L); "
        "unbounded integer arithmetic has additional bit complexity.",
        "",
        "## Caveats",
        "",
    ]
    lines.extend("- " + w for w in data["warnings"])
    lines += [
        "",
        "## Required follow-up to establish complexity",
        "",
        "1. Derive recurrence or operation-count model from the IR and source.",
        "2. Verify domain, checked overflow and fallback paths.",
        "3. Count core operations dynamically and compare with theoretical bounds.",
        "4. Measure new logarithmically spaced N values across a wider valid input domain.",
        "5. For O(1) claims, ensure code does not fall back to a loop for some valid inputs.",
        "6. Independently confirm equivalence for checked-i64 semantics.",
        "7. Compare algorithmic complexity separately from compiler/backend constant factors.",
        "",
        "## Sources",
        "",
    ]
    for s in data["sources"]:
        lines.append(f"- {s['file']} — accepted {s['accepted']}; skipped {s['skipped']}")
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, action="append", help="V8/V9 JSON (later files override matching points)")
    ap.add_argument("--output", type=Path, default=Path(__file__).with_name("scaling_v9.json"))
    ap.add_argument("--markdown", type=Path, default=Path(__file__).with_name("SCALING_V9.md"))
    args = ap.parse_args()
    result = analyze(args.input or [DEFAULT_INPUT])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    args.markdown.write_text(markdown(result), encoding="utf-8")
    for r in result["rows"]:
        print(f"{r['function']:20s} {r['mode']} N={r['N_first']}-{r['N_last']} "
              f"growth={r['runtime_growth_factor']:>10.2f}x p={r['observed_loglog_slope_all']!s:>7} "
              f"theory={r['algorithmic_hypothesis_not_proof']:>8} flags={','.join(r['flags'])}")
    print(f"WROTE {args.output} and {args.markdown}; BIG_O_PROVED=NO")


if __name__ == "__main__":
    main()
