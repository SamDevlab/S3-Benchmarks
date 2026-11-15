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


def test_v12_both_overlay_runs_pass_with_exact_collect_counts():
    data=load("v12_coexistence_20261115.json")
    assert data["decision"]=="GO_EXPERIMENTAL_COMPATIBLE_SUBSET"
    assert data["file_level_conflicts"]==0
    assert data["no_original_branch_modified"]
    assert data["no_merge_no_remote_push_no_actions"]
    rows=data["tests"]
    assert len(rows)==2
    assert [r["number_collected"] for r in rows]==[93,159]
    assert [r["collect_files"] for r in rows]==[9,15]
    assert data["total_overlay_tests_passed"]==252
    assert all(r["exit_code"]==0 and r["collect_exit_code"]==0
               and not r["timed_out"] for r in rows)
    assert all((ROOT/r["log"]).exists() and
               (ROOT/r["collect_log"]).exists() for r in rows)
    assert any("physical RX580" in claim for claim in data["not_proved"])


def test_v12_local_review_branches_record_no_upstream_push():
    ref=load("v12_overlay_local_refs_20261115.json")
    assert set(ref)=={"S3-V12-Combined","S3-V18-Combined"}
    for entry in ref.values():
        assert entry["local_only"] is True
        assert len(entry["changed_files"])==9
        assert entry["overlay_head"]!=entry["base"]
    assert ref["S3-V12-Combined"]["base"].startswith("02f0a3f7")
    assert ref["S3-V18-Combined"]["base"].startswith("1a323a03")


def test_release_triage_classifies_each_pr_without_claiming_release():
    release=load("release_triage_matrix_20261115.json")
    decisions=load("pr_decisions_20261115.json")
    assert release["campaign"]=="S3_CORE_V11_V18_RELEASE_TRIAGE_WITH_V12A"
    assert release["test_exit_code"]==release["collection_exit_code"]==0
    assert release["observed_success"]
    assert release["inherited_tests_still_open"]
    assert release["no_actions_no_merge_no_deploy"]
    assert decisions["outcome"]=="TRIAGE_COMPLETE_NO_RELEASE_APPROVAL"
    assert decisions["all_still_draft"]
    assert decisions["all_blocked_for_merge"]
    assert decisions["merges"]==0 and decisions["deployments"]==0
    assert decisions["github_actions_used"] is False
    assert len(decisions["decisions"])==27
    assert len({
       (item["repo"],item["number"]) for item in decisions["decisions"]
    })==27
    assert set(x["decision"] for x in decisions["decisions"]) <= {
       "GO_EXPERIMENTAL_ONLY","GO_EXPERIMENTAL_COMPATIBLE_SUBSET",
       "NO_GO_GLOBAL_DEFAULT",
    }
    assert all(x["blocked_for_merge"] for x in decisions["decisions"])
    assert sum(release["counts_by_stage"].values())+release["cross_family_tests"]==release["collected_total"]
    assert release["collected_total"]==227
    assert release["counts_by_stage"]["V18"]==13
    assert release["counts_by_stage"]["V12-A"]==34


def test_quality_fix_runs_formerly_excluded_tests_and_native_simd():
    quality=load("quality_gate_20261115.json")
    assert quality["campaign"]=="S3_CORE_QUALITY_V18_NO_LEGACY_DESELECTIONS_20261115"
    assert quality["passed"]
    assert quality["legacy_exclusions"]==[]
    assert len(quality["legacy_tests_restored"])==2
    assert quality["github_actions_used"] is False
    assert quality["merge_or_deploy"] is False
    assert quality["core_collection"]["tests_collected"]==248
    assert quality["vector_collection"]["tests_collected"]==14
    for key in ("core_test_result","core_collection",
                "vector_test_result","vector_collection"):
        result=quality[key]
        assert result["exit_code"]==0 and (ROOT/result["log"]).exists()
    assert "--deselect" not in quality["core_test_result"]["command"]


def test_v12a_v18_local_post_quality_has_no_hidden_exclusions():
    combined=load("post_quality_v18_v12a_20261115.json")
    assert combined["campaign"]=="S3_CORE_POST_QUALITY_V12A_V18_SELECTED_FULL_LOCAL"
    assert combined["all_selected_pass"]
    assert combined["tests_collected"]==229
    assert combined["test_exit_code"]==combined["collection_exit_code"]==0
    assert combined["deselected_tests"]==[]
    assert len(combined["previously_deselected_tests"])==2
    assert not combined["github_actions_used"]
    assert not combined["merged_to_main"]
    assert not combined["production_changes"]
    assert all((ROOT/path).exists() for path in combined["logs"])
