"""Guard rails for S3 Core baseline/inventory: no accidental GO claims."""
from __future__ import annotations
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT/name).read_text("utf-8-sig"))


def test_pr_snapshot_has_exactly_scoped_27_target_prs():
    inv=load("pr_stack_20261115.json")
    assert inv["campaign"]=="S3_CORE_CONSOLIDATION_20261115"
    assert set(inv["repos"])=={"S3","S3-Benchmarks","Relat-rio"}
    assert sum(len(r["selected_prs"]) for r in inv["repos"].values())==27
    for repo,data in inv["repos"].items():
        assert data["not_open_from_expected_ids"]==[]
        assert data["all_open_prs"]>=len(data["selected_prs"])
        assert all(p["isDraft"] and p["state"]=="OPEN" for p in data["selected_prs"])
    a={p["number"]:p for p in inv["repos"]["S3"]["selected_prs"]}
    assert a[409]["baseRefName"]==a[410]["baseRefName"]
    assert a[416]["baseRefName"]==a[415]["headRefName"]
    assert inv["baseline"]["main_to_v18_commits"].split()==["0","663"]
    assert inv["decision"]=="INVENTORY_ONLY_NO_MERGE_NO_DEFAULT_ENABLE"


def test_local_baseline_uses_distinct_main_and_v18_no_hidden_failures():
    report=load("baseline_20261115.json")
    assert report["all_mandatory_gates_passed"]
    assert all(report["mandatory_gates"].values())
    assert report["github_actions"]=="NOT_USED_NO_REMOTE_CI_ASSERTIONS"
    assert report["release_approval"]=="NO_MERGE_NO_DEPLOY_EXPERIMENTAL_ONLY"
    assert report["comparison_contract"].startswith("Historical main and V18")
    assert report["candidate_collection"]["number_in_summary"]==246
    assert report["historical_collection"]["number_collected"]==61
    assert report["historical_main_smoke_exit_code"]==0
    assert len(report["inherited_deselected_selectors"])==2
    results={r["job"]:r for r in report["results"]}
    assert results["candidate_v10_v18_regression"]["exit_code"]==0
    assert results["historic_main_available_smoke"]["exit_code"]==0
    for i in (1,2):
        t=results[f"inherited_failure_probe_{i}"]
        assert t["exit_code"]==1 and t["job"].startswith("inherited_failure")
        assert (ROOT/t["log"]).exists()
    for name in ("v15","v16","v17","v18"):
        row=results[f"benchmark_artifacts_{name}"]
        assert row["exit_code"]==0
        assert row["passed_reported"]>0
        assert (ROOT/row["log"]).exists()


def test_baseline_source_has_no_secret_or_release_claim():
    dependency=(ROOT/"DEPENDENCIES_20261115.md").read_text("utf-8")
    assert "V12 has sibling" in dependency
    assert "No automatic merge" in dependency
    report=load("pr_stack_20261115.json")
    assert report["initial_screening"]["V18"]=="GO_EXPERIMENTAL_WITH_CODE_SIZE_REGRESSIONS"
    assert not report["baseline"]["branch_is_not_production_release"] is False


def test_evidence_collection_log_count_matches_selected_test_total():
    report=load("baseline_20261115.json")
    collected=(ROOT/"logs"/"candidate_collect_only.log").read_text("utf-8")
    numbers=[
        int(x) for x in re.findall(r"^tests/[^:\n]+:\s*(\d+)\s*$",
                                   collected,re.MULTILINE)
    ]
    assert sum(numbers)==report["candidate_collection"]["number_in_summary"]
    assert len(numbers)==report["candidate_collection"]["collected_files"]
    assert "unexpected keyword argument 'predictive_exact'" in (
        ROOT/"logs"/"inherited_failure_probe_1.log"
    ).read_text("utf-8")


def test_v12_parallel_prs_disjoint_files_but_not_automatically_compatible():
    record=load("v12_fork_20261115.json")
    assert record["pr409"]["number"]==409
    assert record["pr410"]["number"]==410
    assert record["pr409"]["base"]==record["pr410"]["base"]
    a=set(record["pr409"]["files"])
    b=set(record["pr410"]["files"])
    assert len(a)==9 and len(b)==8
    assert a.isdisjoint(b)
    assert record["overlap_file_count"]==0
    assert record["decision"]=="REVIEW_REQUIRED_DO_NOT_MERGE_SIBLINGS_AUTOMATICALLY"
    assert load("pr_stack_20261115.json")["v12_fork"]["overlap_file_count"]==0
