"""V18 evidence integrity: correctness, generated guards, costs, negative cases.

Speedups are measurements, NEVER correctness/CI gates.
"""
from __future__ import annotations
import json
from pathlib import Path
import statistics

from source_v18 import sha256_hex

HERE=Path(__file__).resolve().parent


def artifact(filename):
    return json.loads((HERE/filename).read_text("utf-8"))


def sessions():
    return [artifact(f"results_autoguard_v18_s{i}.json") for i in (1,2,3)]


def test_real_native_sessions_preserve_source_and_oracle():
    digest=sha256_hex()
    for number,run in enumerate(sessions(),1):
        assert run["session"]==f"s{number}"
        assert run["decision"]=="GO_EXPERIMENTAL_NOT_PRODUCTION"
        assert run["source_sha256"]==digest
        assert run["same_assembly_ir"]
        assert run["compiler_generated_guard"]
        assert run["compiler_slow_fallback_original_cfg"]
        assert run["original_source_contains_user_width_guard"] is False
        assert run["experimental_v18_default"] is False
        assert run["c_role"]=="INDEPENDENT_CORRECTNESS_ORACLE_AND_TIMING_DRIVER"
        assert run["gcc_role"]=="ASSEMBLY_LINK_ONLY"
        assert run["asm_hashes"]["baseline"]!=run["asm_hashes"]["v18"]
        assert run["benchmark"]["rounds"]==9
        assert len(run["benchmark"]["cases"])==21
        assert all(
            x["parity"] and x["baseline_ns"]>0 and x["v18_ns"]>0
            for x in run["benchmark"]["cases"]
        )


def test_loop_guard_and_original_fallback_are_auditable():
    for run in sessions():
        assert set(run["proofs"])=={"auto_neighbor","auto_stencil"}
        loop=run["proofs"]["auto_stencil"]
        assert loop["generated_guard"]
        assert loop["cloned_fast_blocks"]==7
        assert loop["retained_slow_blocks"]==11
        assert loop["eliminated_fast_bounds"]==6
        assert loop["fallback_bounds_eliminated"]==0
        assert loop["guarded_width_register"]==2
        assert len(loop["witness_records"])==6
        assert run["proofs"]["auto_neighbor"]["cloned_fast_blocks"]==1
        for witness in loop["witness_records"]:
            assert witness["block"].endswith("__v18_autoguard_fast")
            assert witness["guarded_true_edge"][0].startswith("__v18_autoguard_")
            assert witness["lower_site"]<witness["eliminated_site"]
            assert witness["upper_site"]<witness["eliminated_site"]
            assert witness["lower_dynamic"]==[0,0]
            assert witness["upper_dynamic"]==[2,2]
            c,k=witness["target_dynamic"]
            assert 0<3*c+k<8


def test_assembly_size_and_static_disassembly_costs_are_not_hidden():
    for run in sessions():
        size=run["assembly_bytes"]
        assert size["v18"]>size["baseline"]
        assert run["native_static_profile"]["v18"]["static_not_cpu_pmu"]
        assert run["native_static_profile"]["baseline"]["static_not_cpu_pmu"]
        a=run["native_static_profile"]["baseline"]["hot"]["auto_stencil"]
        b=run["native_static_profile"]["v18"]["hot"]["auto_stencil"]
        assert b["static_instructions"]>a["static_instructions"]
        assert b["static_conditional_branches"]>a["static_conditional_branches"]
        assert a["static_calls"]==b["static_calls"]==0


def test_summary_tracks_all_positive_and_negative_observations():
    data=sessions()
    summary=artifact("summary_v18.json")
    assert summary["process_sessions"]==3
    assert summary["physical_machines"]==1
    assert summary["rounds_per_case_session"]==9
    assert summary["total_case_session_ratios"]==63
    assert len(summary["cases"])==21
    ratios=[r["speedup"] for trial in data
            for r in trial["benchmark"]["cases"]]
    assert summary["favorable_observations"]==sum(x>1 for x in ratios)
    assert summary["regression_observations"]==sum(x<1 for x in ratios)
    assert len(summary["negative_observations"])==sum(x<1 for x in ratios)
    assert abs(summary["median_of_all_ratios"]-statistics.median(ratios))<1e-5
    for i,case in enumerate(summary["cases"]):
        rows=[trial["benchmark"]["cases"][i] for trial in data]
        assert (case["width"],case["height"])==(rows[0]["width"],rows[0]["height"])
        assert case["by_session"]==[r["speedup"] for r in rows]
        assert case["all_independent_reference_parity"]


def test_preliminary_whole_function_rejected_design_preserved():
    summary=artifact("summary_v18.json")
    earlier=artifact("results_autoguard_v18_whole_function_preliminary_s1.json")
    assert earlier["source_sha256"]==summary["source_sha256"]
    assert earlier["proofs"]["auto_stencil"]["cloned_fast_blocks"]==11
    assert earlier["proofs"]["auto_stencil"]["eliminated_fast_bounds"]==6
    assert summary["initial_whole_function_assembly_bytes"]==(
        earlier["assembly_bytes"]["v18"]
    )
    assert summary["final_selective_loop_assembly_bytes"]==(
        sessions()[0]["assembly_bytes"]["v18"]
    )
    assert summary["final_selective_loop_assembly_bytes"]<(
        summary["initial_whole_function_assembly_bytes"]
    )
    assert summary["baseline_assembly_bytes"]==(
        earlier["assembly_bytes"]["baseline"]
    )


def test_hp03_parity_is_not_global_production_qualification():
    entry=artifact("results_autoguard_v18_s1_hp03.json")
    assert entry["hp03_enabled"]
    assert entry["decision"]=="GO_EXPERIMENTAL_NOT_PRODUCTION"
    assert all(c["parity"] for c in entry["benchmark"]["cases"])
    assert entry["proofs"]["auto_stencil"]["generated_guard"]
    assert entry["proofs"]["auto_stencil"]["fallback_bounds_eliminated"]==0
    assert artifact("summary_v18.json")["hp03_is_multi_host_qualification"] is False
