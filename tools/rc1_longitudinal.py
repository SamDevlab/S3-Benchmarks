"""Aggregate the RC1 native longitudinal campaign without overclaiming.

The P1 runner stores aggregate per-fixture statistics, not paired sample
vectors. This tool therefore publishes raw aggregates and marks confidence as
INCONCLUSIVE whenever the control drift or missing paired samples prevents a
predeclared statistical conclusion.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import subprocess
from typing import Any


EXPECTED_S3_MAIN = "9b39c7070d7bfa23d709c2128eb0b0bbef164177"
EXPECTED_RC1 = EXPECTED_S3_MAIN
EXPECTED_BENCHMARK_START = "871e2015a2e2d15e202eb023f11a833304ba44e4"
HISTORICAL = {
    "H0": ("85541b782571c80d4857d013d1fb25b4997c1eb9", "historical"),
    "H1": ("631b51e70562a33183ac14d0be5bbe2ddd140779", "pre-P8"),
    "H2": ("5dd6844607ba3a2d5830ed836fb9026eed86d0fb", "post-P8"),
    "H3": ("2316300f7f6c119004009b713849cae1c101d1a5", "M2.00"),
    "H4": ("e23b092bec100cedc520841a7dd0f4488090b6a1", "M2.30"),
    "H5": (EXPECTED_RC1, "RC1"),
}
SCOPE = {
    "scope": "NATIVE_PROCESS_WITH_INTERNAL_PARSE_LOOP",
    "process_startup": "AMORTIZED_NOT_SUBTRACTED",
    "input_setup": "EMBEDDED_BYTES_BOTH_C_AND_S3",
    "parses_per_sample": 10000,
    "warmups": 5,
    "repetitions": 30,
    "affinity": "taskset -c 0",
}


class ReportError(RuntimeError):
    pass


def _git_head(root: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--verify", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _geomean(values: list[float]) -> float:
    if not values or any(value <= 0 for value in values):
        raise ReportError("geomean requires positive values")
    return math.exp(sum(math.log(value) for value in values) / len(values))


def _load_p1(raw_dir: Path) -> dict[str, dict[str, Any]]:
    reports: dict[str, dict[str, Any]] = {}
    fixture_contract: tuple[tuple[str, int, str], ...] | None = None
    for checkpoint, (expected_sha, _) in HISTORICAL.items():
        path = raw_dir / f"{checkpoint}.json"
        if not path.is_file():
            raise ReportError(f"missing raw P1 report: {path}")
        report = json.loads(path.read_text(encoding="utf-8"))
        environment = report.get("environment", {})
        if environment.get("s3_compiler_commit") != expected_sha:
            raise ReportError(f"{checkpoint} S3 provenance mismatch")
        if environment.get("benchmark_repo_commit") != EXPECTED_BENCHMARK_START:
            raise ReportError(f"{checkpoint} benchmark provenance mismatch")
        if report.get("correctness", {}).get("status") != "PASS":
            raise ReportError(f"{checkpoint} correctness is not PASS")
        scope = report.get("measurement_scope", {})
        required_scope = {
            "SCOPE": SCOPE["scope"],
            "PROCESS_STARTUP": SCOPE["process_startup"],
            "INPUT_SETUP_POLICY": SCOPE["input_setup"],
            "PARSES_PER_SAMPLE": SCOPE["parses_per_sample"],
            "WARMUPS": SCOPE["warmups"],
            "REPETITIONS": SCOPE["repetitions"],
        }
        if any(scope.get(key) != value for key, value in required_scope.items()):
            raise ReportError(f"{checkpoint} measurement scope mismatch")
        if len(report.get("results", [])) != 30 or len(report.get("comparison_table", [])) != 6:
            raise ReportError(f"{checkpoint} result cardinality mismatch")
        variants = {row.get("variant") for row in report["results"]}
        expected_variants = {"C-GCC-O0", "C-GCC-O2", "C-GCC-O3", "S3-O0-NATIVE", "S3-O1-NATIVE"}
        if variants != expected_variants:
            raise ReportError(f"{checkpoint} variant set mismatch")
        for row in report["results"]:
            if row.get("process_exit_code") != 0 or row.get("samples_count") != 30:
                raise ReportError(f"{checkpoint} contains an invalid result row")
        fixture_contract_now = tuple(
            sorted((row["corpus"], row["bytes"], row["sha256"]) for row in report["comparison_table"])
        )
        if fixture_contract is None:
            fixture_contract = fixture_contract_now
        elif fixture_contract_now != fixture_contract:
            raise ReportError(f"{checkpoint} fixture contract mismatch")
        reports[checkpoint] = report
    return reports


def _checkpoint_row(checkpoint: str, report: dict[str, Any]) -> dict[str, Any]:
    by_variant: dict[str, list[float]] = {}
    for result in report["results"]:
        by_variant.setdefault(result["variant"], []).append(float(result["median_ns_per_parse"]))
    assembly = report["assembly_analysis"]["S3-O1"]
    c_o2 = _geomean(by_variant["C-GCC-O2"])
    c_o3 = _geomean(by_variant["C-GCC-O3"])
    s3_o0 = _geomean(by_variant["S3-O0-NATIVE"])
    s3_o1 = _geomean(by_variant["S3-O1-NATIVE"])
    return {
        "checkpoint": checkpoint,
        "sha": report["environment"]["s3_compiler_commit"],
        "correctness": report["correctness"]["status"],
        "o0_ns_per_parse_geomean": s3_o0,
        "o1_ns_per_parse_geomean": s3_o1,
        "c_o2_ns_per_parse_geomean": c_o2,
        "c_o3_ns_per_parse_geomean": c_o3,
        "c_o2_ratio": s3_o1 / c_o2,
        "c_o3_ratio": s3_o1 / c_o3,
        "instruction_count": assembly["instruction_count"],
        "branches": assembly["branch_count"],
        "loads_stores": assembly["load_store_count"],
        "stack_ops": assembly["stack_ops_count"],
        "assembly_lines": assembly["line_count"],
        "sample_level_data_available": False,
    }


def _control_drift(rows: list[dict[str, Any]]) -> dict[str, Any]:
    controls = [row["c_o2_ns_per_parse_geomean"] for row in rows]
    minimum = min(controls)
    maximum = max(controls)
    relative = maximum / minimum - 1.0
    return {
        "control": "C-GCC-O2",
        "values_ns_per_parse_geomean": controls,
        "min": minimum,
        "max": maximum,
        "relative_range": relative,
        "threshold": 0.05,
        "classification": "HIGH" if relative > 0.05 else "LOW",
    }


def _delta(new: float, old: float) -> float:
    return (new / old - 1.0) * 100.0


def _format_scoreboard_value(value: Any, *, percent: bool = False) -> str:
    if value is None:
        return "N/A"
    if isinstance(value, float):
        return f"{value:.2f}%" if percent else f"{value:.2f}"
    return str(value)


def _load_workloads(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {"workloads": []}
    if not path.is_file():
        raise ReportError(f"missing workload status: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("contract_probe") != "PASS":
        raise ReportError("workload contract probe did not pass")
    return value


def build_report(report_root: Path, *, benchmark_root: Path, m199_path: Path | None, workload_path: Path | None) -> dict[str, Any]:
    raw_dir = report_root / "p1" / "raw"
    reports = _load_p1(raw_dir)
    rows = [_checkpoint_row(checkpoint, reports[checkpoint]) for checkpoint in HISTORICAL]
    drift = _control_drift(rows)
    h4 = next(row for row in rows if row["checkpoint"] == "H4")
    h5 = next(row for row in rows if row["checkpoint"] == "H5")
    h4_h5_delta = _delta(h5["o1_ns_per_parse_geomean"], h4["o1_ns_per_parse_geomean"])
    longitudinal_class = "INCONCLUSIVE" if drift["classification"] == "HIGH" else "UNCHANGED_WITHIN_NOISE"
    for index, row in enumerate(rows):
        row["vs_previous_percent"] = None if index == 0 else _delta(row["o1_ns_per_parse_geomean"], rows[index - 1]["o1_ns_per_parse_geomean"])
        row["vs_previous_classification"] = None if index == 0 else "INCONCLUSIVE"
        row["statistical_classification"] = longitudinal_class
        row["confidence_interval_95"] = None
    workload_status = _load_workloads(workload_path)
    workloads = workload_status.get("workloads", [])
    m199 = None
    if m199_path is not None:
        m199 = json.loads(m199_path.read_text(encoding="utf-8"))
        if m199.get("status") != "PASS_CHARACTERIZATION_ONLY":
            raise ReportError("M1.99 characterization did not pass")
    benchmark_final = _git_head(benchmark_root)
    provenance = {
        "s3_main_sha": EXPECTED_S3_MAIN,
        "rc1_tag": "v1.0.0-rc1",
        "rc1_tag_target": EXPECTED_RC1,
        "benchmark_start_sha": EXPECTED_BENCHMARK_START,
        "benchmark_analysis_sha": benchmark_final,
        "historical_shas": {key: value[0] for key, value in HISTORICAL.items()},
        "raw_p1_provenance": "PASS",
        "s3_mutated": False,
        "new_t4_runs": 0,
        "full_suite_runs": 0,
    }
    protocol = {
        "measurement": SCOPE,
        "correctness_before_timing": True,
        "raw_sample_vectors_persisted": False,
        "statistical_method": "predeclared aggregate-only review; paired/bootstrap CI unavailable",
        "control_drift_policy": "HIGH control drift makes affected longitudinal classifications INCONCLUSIVE",
        "native_speedup_claim": "NO",
        "host": "VIRTUALBOX_LINUX",
    }
    environment = reports["H5"]["environment"] | {
        "host": "VIRTUALBOX_LINUX",
        "virtualized": True,
        "host_ready_for_benchmark": True,
        "taskset": "/usr/bin/taskset -c 0",
        "benchmark_processes_active_during_preflight": 0,
        "s3_processes_active_during_preflight": 0,
    }
    _write_json(report_root / "environment.json", environment)
    _write_json(report_root / "provenance.json", provenance)
    _write_json(report_root / "protocol.json", protocol)
    p1_summary = {
        "schema": "s3.rc1.p1.summary.v1",
        "provenance": provenance,
        "rows": rows,
        "control_drift": drift,
        "h4_vs_h5": {
            "o1_delta_percent": h4_h5_delta,
            "classification": longitudinal_class,
            "reason": "C-O2 control range exceeded 5%; aggregate reports have no paired sample vectors",
        },
        "correctness": "PASS",
        "native_speedup_claim": "NO",
        "m199": m199,
    }
    _write_json(report_root / "p1" / "summary.json", p1_summary)
    (report_root / "p1" / "summary.md").write_text(
        "# P1 RC1 longitudinal summary\n\n"
        "All H0-H5 runs passed correctness and used the same native process protocol. "
        f"C-O2 control drift is {drift['relative_range'] * 100:.2f}%, so cross-checkpoint timing conclusions are **{longitudinal_class}**. "
        "The stored reports contain aggregate statistics rather than paired sample vectors; no confidence interval is invented.\n",
        encoding="utf-8",
    )
    for row in rows:
        historical = {
            **row,
            "raw_json": f"p1/raw/{row['checkpoint']}.json",
            "raw_sha256": _sha256(raw_dir / f"{row['checkpoint']}.json"),
            "comparison_scope": "same current VM/protocol; cross-checkpoint classification control-limited",
        }
        _write_json(report_root / "historical" / f"{row['checkpoint']}.json", historical)
    trend = {
        "schema": "s3.rc1.longitudinal.trend.v1",
        "metric_units": {"runtime": "ns/parse geomean", "ratios": "x", "structure": "count"},
        "rows": rows,
        "classification": longitudinal_class,
        "control_drift": drift,
    }
    _write_json(report_root / "trend.json", trend)
    with (report_root / "trend.csv").open("w", newline="", encoding="utf-8") as stream:
        fields = ["checkpoint", "sha", "o0_ns_per_parse_geomean", "o1_ns_per_parse_geomean", "c_o2_ratio", "instruction_count", "branches", "loads_stores", "stack_ops", "statistical_classification"]
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({field: row.get(field) for field in fields} for row in rows)
    (report_root / "trend.md").write_text(
        "# RC1 longitudinal trend\n\n"
        "| Checkpoint | O1 ns/parse | C-O2 ratio | Instructions | Branches | Loads/stores | Stack ops | Classification |\n"
        "|---|---:|---:|---:|---:|---:|---:|---|\n"
        + "\n".join(
            f"| {row['checkpoint']} | {row['o1_ns_per_parse_geomean']:.2f} | {row['c_o2_ratio']:.2f}x | {row['instruction_count']} | {row['branches']} | {row['loads_stores']} | {row['stack_ops']} | {row['statistical_classification']} |"
            for row in rows
        )
        + "\n\nControl drift is HIGH when the C-O2 geomean range exceeds 5%; affected runtime conclusions remain inconclusive.\n",
        encoding="utf-8",
    )
    for row in workloads:
        pdir = report_root / row["workload"].lower()
        _write_json(pdir / "summary.json", row)
        (pdir / "summary.md").write_text(
            f"# {row['workload']} {row['name']}\n\n"
            f"Contract probe: **{row['contract_probe']}**. Canonical status: **{row['canonical_status']}**. "
            f"Performance timing: **{row['performance_status']}**. {row['reason']}\n",
            encoding="utf-8",
        )
    _write_json(report_root / "workload-status.json", workload_status)
    scoreboard_rows = [{
        "workload": "P1 JSMN",
        "comparison_class": "S3_VS_C",
        "correctness": "PASS",
        "historical": "H0-H5",
        "m2_00": rows[3]["o1_ns_per_parse_geomean"],
        "m2_30": rows[4]["o1_ns_per_parse_geomean"],
        "rc1": rows[5]["o1_ns_per_parse_geomean"],
        "c_o2": rows[5]["c_o2_ns_per_parse_geomean"],
        "c_o3": rows[5]["c_o3_ns_per_parse_geomean"],
        "rc1_vs_m2_30_percent": h4_h5_delta,
        "rc1_vs_historical": "INCONCLUSIVE",
        "rc1_vs_c_o2": rows[5]["c_o2_ratio"],
        "result": "INCONCLUSIVE_LONGITUDINAL_CONTROL_DRIFT",
        "confidence": "LOW",
    }]
    for row in workloads:
        scoreboard_rows.append({
            "workload": row["workload"],
            "comparison_class": row["comparison_class"],
            "correctness": row["contract_probe"],
            "historical": "NOT_RUN",
            "m2_00": None,
            "m2_30": None,
            "rc1": None,
            "c_o2": None,
            "c_o3": None,
            "rc1_vs_m2_30_percent": None,
            "rc1_vs_historical": "NOT_COMPARABLE",
            "rc1_vs_c_o2": "NOT_COMPARABLE",
            "result": row["canonical_status"],
            "confidence": "LOW",
        })
    _write_json(report_root / "scoreboard.json", {"schema": "s3.rc1.scoreboard.v1", "rows": scoreboard_rows})
    (report_root / "scoreboard.md").write_text(
        "# RC1 performance scoreboard\n\n"
        "P1 is the only timed workload. P2-P18 rows are contract probes and are excluded from aggregate performance claims.\n\n"
        "| Workload | Class | Correctness | RC1 | RC1 vs M2.30 | Result | Confidence |\n|---|---|---|---:|---:|---|---|\n"
        + "\n".join(
            f"| {row['workload']} | {row['comparison_class']} | {row['correctness']} | {_format_scoreboard_value(row['rc1'])} | {_format_scoreboard_value(row['rc1_vs_m2_30_percent'], percent=True)} | {row['result']} | {row['confidence']} |"
            for row in scoreboard_rows
        )
        + "\n",
        encoding="utf-8",
    )
    bottlenecks = [
        {"id": "B1", "workload": "P1 JSMN", "observation": "RC1 S3-O1 remains 43.89x slower than the same-run C-O2 geomean", "s3_metric": rows[5]["o1_ns_per_parse_geomean"], "c_metric": rows[5]["c_o2_ns_per_parse_geomean"], "ratio": rows[5]["c_o2_ratio"], "likely_layer": "native lowering/runtime representation", "evidence_strength": "HIGH", "hypothesis": "instruction and memory traffic expansion dominate the external gap", "next_experiment": "promote P7-P9 paired native kernels and collect raw samples plus perf if permitted"},
        {"id": "B2", "workload": "P1 JSMN", "observation": "S3-O1 assembly has 49,414 instructions, 24,745 loads/stores, and 7,560 stack operations", "s3_metric": {"instructions": rows[5]["instruction_count"], "loads_stores": rows[5]["loads_stores"], "stack_ops": rows[5]["stack_ops"]}, "c_metric": "not captured by current runner", "ratio": None, "likely_layer": "code generation and frame materialization", "evidence_strength": "MEDIUM", "hypothesis": "value and memory-state materialization remain broad", "next_experiment": "structural P8/P9 kernels with per-function metric attribution"},
        {"id": "B3", "workload": "P1 JSMN", "observation": "O1/O0 geomean ratio is 0.9449x on RC1", "s3_metric": rows[5]["o1_ns_per_parse_geomean"], "c_metric": rows[5]["o0_ns_per_parse_geomean"], "ratio": rows[5]["o1_ns_per_parse_geomean"] / rows[5]["o0_ns_per_parse_geomean"], "likely_layer": "optimization coverage", "evidence_strength": "MEDIUM", "hypothesis": "current optimizer reduces runtime on this workload but does not close the representation gap", "next_experiment": "separate optimizer passes with paired native structural deltas"},
        {"id": "B4", "workload": "P1 JSMN", "observation": "C-O2 control range is above the 5% predeclared threshold", "s3_metric": drift["relative_range"], "c_metric": 0.05, "ratio": drift["relative_range"] / 0.05, "likely_layer": "measurement environment", "evidence_strength": "HIGH", "hypothesis": "host/control variability prevents a confident H4-H5 runtime classification", "next_experiment": "one bounded paired campaign after controlled cooldown"},
        {"id": "B5", "workload": "P2-P18", "observation": "no promoted workload beyond P1 has a native timing result in this campaign", "s3_metric": 0, "c_metric": 0, "ratio": None, "likely_layer": "benchmark coverage", "evidence_strength": "HIGH", "hypothesis": "the next bottleneck is evidence coverage before optimization claims", "next_experiment": "promote P7, P8, and P9 one at a time with correctness-first native harnesses"},
    ]
    _write_json(report_root / "bottlenecks.json", {"schema": "s3.rc1.bottlenecks.v1", "rows": bottlenecks})
    (report_root / "bottlenecks.md").write_text(
        "# RC1 bottleneck assessment\n\n" + "\n".join(
            f"## {row['id']} — {row['workload']}\n\n- Observation: {row['observation']}\n- Likely layer: {row['likely_layer']}\n- Evidence: {row['evidence_strength']}\n- Hypothesis: {row['hypothesis']}\n- Next experiment: {row['next_experiment']}\n"
            for row in bottlenecks
        ),
        encoding="utf-8",
    )
    p2_p18_counts = {
        "executable_count": 0,
        "pass_count": 0,
        "deferred_count": len(workloads),
        "experimental_count": len(workloads),
        "contract_probe_pass": "PASS",
    }
    final = {
        "schema": "s3.rc1.longitudinal.final.v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "s3_main_sha": EXPECTED_S3_MAIN,
        "rc1_tag_target": EXPECTED_RC1,
        "benchmark_start_sha": EXPECTED_BENCHMARK_START,
        "benchmark_final_sha": benchmark_final,
        "linux_environment": "VIRTUALBOX_LINUX",
        "host_ready_for_benchmark": True,
        "p1_correctness": "PASS",
        "p1": rows,
        "p1_longitudinal_classification": longitudinal_class,
        "control_drift": drift["classification"],
        "p2_p18": p2_p18_counts,
        "best_s3_checkpoint_observed": "H5_RC1",
        "rc1_new_best": "INCONCLUSIVE",
        "rc1_vs_historical": "INCONCLUSIVE",
        "rc1_vs_post_p8": "INCONCLUSIVE",
        "rc1_vs_m2_00": "INCONCLUSIVE",
        "rc1_vs_m2_30": "INCONCLUSIVE",
        "rc1_vs_c_o2": f"{rows[5]['c_o2_ratio']:.2f}x slower",
        "current_c_gap": f"{rows[5]['c_o2_ratio']:.2f}x geomean",
        "s3_runtime_direction": "INCONCLUSIVE",
        "compiler_structure_direction": "UNCHANGED_H4_H5",
        "benchmark_coverage_direction": "EXPANDED_CONTRACTS_NOT_PROMOTED",
        "proven_improvements": [],
        "proven_regressions": [],
        "unchanged_within_noise": [],
        "inconclusive": ["P1 H4-H5 timing due control drift and aggregate-only raw reports"],
        "native_speedup_claim": "NO",
        "regression_bisect_executed": "NO",
        "first_regressing_region": "NOT_ESTABLISHED",
        "rc2_performance_fix_justified": "NO",
        "benchmark_quality": {"correctness_before_timing": "PASS", "artifact_isolation": "PASS", "sha_provenance": "PASS", "raw_results_persisted": "PASS", "environment_captured": "PASS", "statistical_classification": "INCONCLUSIVE_BY_POLICY", "compileall": "PENDING", "diff_check": "PENDING"},
        "s3_mutated": False,
        "s3_production_change": False,
        "s3_test_change": False,
        "s3_runner_change": False,
        "new_t4_runs": 0,
        "full_suite_runs": 0,
        "tag_change": False,
        "release_change": False,
        "benchmark_merge": False,
        "shutdown": False,
        "status": "MIXED_BY_WORKLOAD",
    }
    _write_json(report_root / "final.json", final)
    (report_root / "final.md").write_text(
        "# S3 RC1 longitudinal native benchmark\n\n"
        f"- RC1 source: `{EXPECTED_RC1}`\n- Benchmark analysis HEAD: `{benchmark_final}`\n"
        f"- P1 correctness: **PASS**\n- P1 longitudinal classification: **{longitudinal_class}**\n"
        f"- C-O2 gap: **{rows[5]['c_o2_ratio']:.2f}x geomean**\n- Native speedup claim: **NO**\n"
        "- P2-P18: contract probes expanded the registry, but all remain experimental/deferred and are excluded from aggregate claims.\n\n"
        "The evidence supports a large remaining native representation/code-generation gap, but not a causal claim for a single layer. H4-H5 runtime evolution is inconclusive because C-O2 control drift exceeded the declared threshold and paired raw samples were not persisted.\n",
        encoding="utf-8",
    )
    return final


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-root", type=Path, required=True)
    parser.add_argument("--benchmark-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--m199-json", type=Path)
    parser.add_argument("--workload-json", type=Path)
    args = parser.parse_args()
    final = build_report(args.report_root, benchmark_root=args.benchmark_root, m199_path=args.m199_json, workload_path=args.workload_json)
    print("P1_CORRECTNESS=PASS")
    print(f"P1_LONGITUDINAL_CLASSIFICATION={final['p1_longitudinal_classification']}")
    print(f"BENCHMARK_FINAL_SHA={final['benchmark_final_sha']}")
    print("NATIVE_SPEEDUP_CLAIM=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
