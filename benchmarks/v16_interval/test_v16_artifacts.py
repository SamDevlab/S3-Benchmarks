"""V16 recorded evidence, reproducibility and honest performance boundaries."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
import statistics

from stencil_source_v16 import WIDTHS,whole_source,kernel_name,offsets

HERE=Path(__file__).resolve().parent


def artifact(name):
    return json.loads((HERE/name).read_text("utf-8"))


def records():
    return [artifact(f"results_interval_v16_{s}.json") for s in ("s1","s2","s3")]


def test_all_three_sessions_share_identical_provenance_and_parity():
    data=records()
    digest=sha256(whole_source().encode("utf-8")).hexdigest()
    for session,entry in enumerate(data,1):
        assert entry["session"]==f"s{session}"
        assert entry["decision"]=="GO_EXPERIMENTAL_NOT_COMPILER_DEFAULT"
        assert entry["original_s3_source_sha256"]==digest
        assert entry["same_s3_assembly_program_ir"]
        assert entry["experimental_flag_default_off"] is True
        assert entry["gcc_role_for_s3"]=="ASSEMBLE_LINK"
        assert "INDEPENDENT_ORACLE" in entry["c_role"]
        assert not entry["hp03_enabled"]
        assert not entry["assembly_output_equal"]
        assert entry["benchmark"]["rounds"]==9
        assert len(entry["benchmark"]["cases"])==len(WIDTHS)*3
        assert all(
            row["parity"] and row["neighbors"]==8 and
            row["baseline_ns"]>0 and row["v16_ns"]>0
            for row in entry["benchmark"]["cases"]
        )


def test_stencil_real_interval_proofs_are_bounded_and_not_name_based():
    data=records()
    for record in data:
        assert set(record["proof"])=={
            kernel_name(w) for w in WIDTHS
        }
        for w in WIDTHS:
            proof=record["proof"][kernel_name(w)]
            assert proof["proven_interior_loads"]==6
            assert proof["checked_endpoint_loads"]==2
            assert proof["skipped_due_to_hp03"] is False
            assert proof["max_span"]==64
            assert len(proof["proof_witnesses"])==6
            for site in proof["proof_witnesses"]:
                assert site["lower_checked_instruction"]<site["load_instruction"]
                assert site["upper_checked_instruction"]<site["load_instruction"]
                assert (0<=site["lower_offset"]<site["target_offset"]<
                        site["upper_offset"]<=64)
                assert site["upper_offset"]-site["lower_offset"]<=64
            assert record["slice_load_sites"][kernel_name(w)]==8
            assert offsets(w)==(
                0,1,2,w,w+2,2*w,2*w+1,2*w+2
            )


def test_actual_static_disassembly_less_bounds_code_without_pmu_claims():
    record=records()[1]
    asm=record["static_disassembly"]
    assert asm["baseline"]["not_dynamic_pmu"]
    assert asm["v16"]["not_dynamic_pmu"]
    for w in WIDTHS:
        name=kernel_name(w)
        a=asm["baseline"]["hot_functions"][name]
        b=asm["v16"]["hot_functions"][name]
        assert b["static_instructions"]<a["static_instructions"]
        assert b["static_conditional_branches"]<a["static_conditional_branches"]
        assert a["static_conditional_branches"]-b["static_conditional_branches"]==12
        assert a["static_calls"]==b["static_calls"]==0


def test_performance_ratios_are_consistent_but_never_a_ci_speed_gate():
    data=records()
    cases=[
        row
        for record in data for row in record["benchmark"]["cases"]
    ]
    assert len(cases)==27
    for row in cases:
        ratio=row["baseline_ns"]/row["v16_ns"]
        assert abs(ratio-row["speedup"])<0.001
        assert ratio>0
    # There is deliberately no minimum speedup threshold here:
    # host variation must not fail functional CI or claim a universal win.


def test_hp03_ablation_remains_independent_and_experimental():
    hp=artifact("results_interval_v16_s1_hp03.json")
    assert hp["hp03_enabled"] is True
    assert hp["experimental_flag_default_off"]
    assert hp["decision"]=="GO_EXPERIMENTAL_NOT_COMPILER_DEFAULT"
    assert hp["benchmark"]["rounds"]==9
    assert all(row["parity"] for row in hp["benchmark"]["cases"])
    # This particular source did not produce an HP03 versioned fast
    # path: V16's own local interval checker still applies.
    assert all(
        s["proven_interior_loads"]==6 and not s["skipped_due_to_hp03"]
        for s in hp["proof"].values()
    )


def test_aggregate_summary_matches_recorded_sessions():
    summary=artifact("summary_v16.json")
    data=records()
    assert summary["sessions"]==3
    assert summary["physical_machines"]==1
    assert summary["observed_total_rows"]==27
    assert len(summary["stencil_cases"])==9
    all_ratios=[
        row["speedup"]
        for item in data for row in item["benchmark"]["cases"]
    ]
    assert abs(
        summary["median_of_all_27_per_session_speedup_ratios"]
        -statistics.median(all_ratios)
    )<0.00001
    for i,case in enumerate(summary["stencil_cases"]):
        ratios=[
            entry["benchmark"]["cases"][i]["speedup"]
            for entry in data
        ]
        assert (case["width"],case["height"])==(
            data[0]["benchmark"]["cases"][i]["width"],
            data[0]["benchmark"]["cases"][i]["height"],
        )
        assert abs(case["median_session_speedup"]-statistics.median(ratios))<0.00001
        assert case["all_independent_c_parity"]
