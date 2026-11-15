"""Check real dynamic stencil native evidence, independent of speed gains."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
import statistics

from source_v17 import source

HERE=Path(__file__).resolve().parent


def read(filename):
    return json.loads((HERE/filename).read_text("utf-8"))


def sessions():
    return [
        read(f"results_dynamic_v17_s{x}.json")
        for x in ("1","2","3")
    ]


def test_all_s3_native_sessions_share_source_and_reference_parity():
    digest=sha256(source().encode()).hexdigest()
    for number,report in enumerate(sessions(),1):
        assert report["session"]==f"s{number}"
        assert report["decision"]=="GO_EXPERIMENTAL_NOT_PRODUCTION"
        assert report["same_assembly_ir"] is True
        assert report["source_sha256"]==digest
        assert report["experimental_v17_default"] is False
        assert report["hp03_enabled"] is False
        assert report["c_role"]=="INDEPENDENT_CORRECTNESS_ORACLE_AND_TIMING_DRIVER"
        assert report["asm_hashes"]["baseline"]!=report["asm_hashes"]["v17"]
        assert report["benchmark"]["rounds"]==9
        assert len(report["benchmark"]["cases"])==21
        assert all(
            row["parity"] and row["baseline_ns"]>0
            and row["v17_ns"]>0
            for row in report["benchmark"]["cases"]
        )


def test_proof_records_verify_guard_edge_and_six_middle_indices():
    for report in sessions():
        for name in ("dynamic_neighbor","dynamic_stencil"):
            info=report["proofs"][name]
            assert info["proven_interior_loads"]==6
            assert info["candidate_checked_loads"]==2
            assert info["hp03_skip"] is False
            assert len(info["witnesses"])==6
            for w in info["witnesses"]:
                assert 0<=w["lower_site"]<w["eliminated_site"]
                assert 0<=w["upper_site"]<w["eliminated_site"]
                assert w["guarded_width_register"]==2
                assert w["guarded_true_edge"][0]=="entry"
                assert w["lower_dynamic"]==[0,0]
                assert w["upper_dynamic"]==[2,2]
                a,b=w["target_dynamic"]
                assert a in (0,1,2) and b in (0,1,2)
                # For width >= 3: 0 < a*width+b < 2*width+2
                assert 0<3*a+b<8
                assert 0<=a<=2
        assert report["proofs"]["dynamic_neighbor"][
            "rejected_blocks_without_dominating_guard"
        ]>=1


def test_static_native_backend_emission_reduced_guard_branches_not_real_pmu():
    report=sessions()[0]
    old=report["static_disassembly"]["baseline"]
    new=report["static_disassembly"]["v17"]
    assert old["static_not_pmu"] and new["static_not_pmu"]
    for name in ("dynamic_neighbor","dynamic_stencil"):
        original=old["hot"][name]
        candidate=new["hot"][name]
        assert candidate["static_instructions"]<original["static_instructions"]
        assert candidate["static_conditional_branches"]<original["static_conditional_branches"]
        assert candidate["static_calls"]==original["static_calls"]==0
    assert (
        old["hot"]["dynamic_stencil"]["static_conditional_branches"]
        -new["hot"]["dynamic_stencil"]["static_conditional_branches"]
    )==12


def test_summary_includes_every_session_and_unfavorable_observation():
    data=sessions()
    report=read("summary_v17.json")
    assert report["same_host_separate_process_sessions"]==3
    assert report["independent_physical_computers"]==1
    assert report["rounds_per_case_session"]==9
    assert report["total_case_session_ratios"]==63
    assert len(report["cases"])==21
    observed=[row["speedup"] for item in data
              for row in item["benchmark"]["cases"]]
    wins=sum(r>1 for r in observed)
    losses=sum(r<1 for r in observed)
    assert report["positive_ratio_observations"]==wins
    assert report["regression_observations"]==losses
    assert len(report["negative_observations"])==losses
    assert abs(
        report["median_of_all_case_session_ratios"]
        -statistics.median(observed)
    )<1e-5
    for i,case in enumerate(report["cases"]):
        ratios=[entry["benchmark"]["cases"][i]["speedup"] for entry in data]
        assert case["by_session"]==ratios
        assert case["all_correct"]


def test_hp03_trial_parity_but_no_general_compatibility_claim():
    report=read("results_dynamic_v17_s1_hp03.json")
    assert report["hp03_enabled"] is True
    assert report["experimental_v17_default"] is False
    assert report["decision"]=="GO_EXPERIMENTAL_NOT_PRODUCTION"
    assert len(report["benchmark"]["cases"])==21
    assert all(row["parity"] for row in report["benchmark"]["cases"])
    assert all(
        report["proofs"][name]["proven_interior_loads"]==6
        for name in ("dynamic_neighbor","dynamic_stencil")
    )
