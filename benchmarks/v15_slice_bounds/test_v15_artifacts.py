"""V15 actual native output artifacts: correctness, proof scope, HP03 gate."""
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE/name).read_text("utf-8"))


def test_all_isolated_v15_ab_runs_keep_parity_and_control():
    records=[
        load(f"results_native_bounds_v15_{session}.json")
        for session in ("s1","s2","s3")
    ]
    fingerprints={r["source_sha256"] for r in records}
    assert len(fingerprints)==1
    for i,rec in enumerate(records):
        assert rec["session_id"]==("s1","s2","s3")[i]
        assert rec["status"]=="EXPERIMENTAL_NO_GLOBAL_PROMOTION"
        assert rec["gcc_role_for_s3"]=="ASSEMBLE_AND_LINK_ONLY"
        assert rec["experimental_v15_default"] is False
        assert rec["same_s3_assembly_program_ir"]
        assert rec["hp03_loop_versioning_enabled"] is False
        assert not rec.get("identical_native_assembly_after_optin",False)
        assert rec["optimization_stats"]["loop_dup"]["reused_checks"]==1
        assert rec["optimization_stats"]["sum_three"]["reused_checks"]==2
        assert rec["results"]["rounds"]==9
        assert len(rec["results"]["cases"])==6
        for case in rec["results"]["cases"]:
            assert case["parity"]
            assert case["baseline_ns"]>0 and case["v15_ns"]>0
            assert case["speedup"]>0


def test_native_static_code_has_fewer_branches_in_guarded_case():
    record=load("results_native_bounds_v15_s1.json")
    base=record["static_disassembly"]["baseline"]["hot_functions"]
    optimized=record["static_disassembly"]["v15"]["hot_functions"]
    for kernel in ("loop_dup","sum_three"):
        assert optimized[kernel]["static_instructions"]<base[kernel]["static_instructions"]
        assert optimized[kernel]["static_conditional_jumps"]<base[kernel]["static_conditional_jumps"]
        assert optimized[kernel]["static_calls"]==base[kernel]["static_calls"]==0
    assert record["static_disassembly"]["v15"]["static_counts_not_dynamic_pmu"]


def test_hp03_prior_regression_is_preserved_and_guard_is_conservative():
    old=load("results_native_bounds_v15_s1_hp03_pre_guard.json")
    safe=load("results_native_bounds_v15_s1_hp03.json")
    assert old["hp03_loop_versioning_enabled"]
    assert safe["hp03_loop_versioning_enabled"]
    assert old["source_sha256"]==safe["source_sha256"]
    assert old.get("identical_native_assembly_after_optin",False) is False
    assert safe["identical_native_assembly_after_optin"] is True
    for name in ("loop_dup","sum_three"):
        assert old["optimization_stats"][name]["reused_checks"]>0
        assert safe["optimization_stats"][name]["reused_checks"]==0
        assert safe["optimization_stats"][name]["skipped_due_to_existing_hp03_fast_path"]
    assert all(row["parity"] for row in old["results"]["cases"])
    assert all(row["parity"] for row in safe["results"]["cases"])


def test_speedups_are_never_a_binary_ci_gate_or_production_claim():
    records=[load(f"results_native_bounds_v15_{s}.json")
             for s in ("s1","s2","s3")]
    assert any(
        row["speedup"]<1 for rec in records for row in rec["results"]["cases"]
    )
    assert all(
        rec["status"]=="EXPERIMENTAL_NO_GLOBAL_PROMOTION"
        for rec in records
    )
