#!/usr/bin/env python3
"""Read-only pinned S3 core PR inventory and dependency map.

Source: authenticated gh pr list snapshots, captured on the connected PC.
This script never calls GitHub Actions, merges PRs, or edits sources.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
from datetime import date

ROOT=Path(__file__).resolve().parent
REPOS={
    "S3": ("prs_s3_open.json",tuple(range(408,417))),
    "S3-Benchmarks": ("prs_benchmarks_open.json",tuple(range(53,62))),
    "Relat-rio": ("prs_relatorio_open.json",tuple(range(69,78))),
}
STUDIES={
    "V11": {"S3":[408],"S3-Benchmarks":[53],"Relat-rio":[69]},
    "V12": {"S3":[409,410],"S3-Benchmarks":[54,55],"Relat-rio":[70,71]},
    "V13": {"S3":[411],"S3-Benchmarks":[56],"Relat-rio":[72]},
    "V14": {"S3":[412],"S3-Benchmarks":[57],"Relat-rio":[73]},
    "V15": {"S3":[413],"S3-Benchmarks":[58],"Relat-rio":[74]},
    "V16": {"S3":[414],"S3-Benchmarks":[59],"Relat-rio":[75]},
    "V17": {"S3":[415],"S3-Benchmarks":[60],"Relat-rio":[76]},
    "V18": {"S3":[416],"S3-Benchmarks":[61],"Relat-rio":[77]},
}
DECISIONS={
    "V11":"REVIEW_EXPERIMENTAL",
    "V12":"SPLIT_BRANCH_REVIEW_REQUIRED",
    "V13":"REVIEW_EXPERIMENTAL",
    "V14":"NO_GO_FOR_DEFAULT_GLOBAL_ENABLE",
    "V15":"GO_EXPERIMENTAL_ONLY",
    "V16":"GO_EXPERIMENTAL_ONLY",
    "V17":"GO_EXPERIMENTAL_ONLY",
    "V18":"GO_EXPERIMENTAL_WITH_CODE_SIZE_REGRESSIONS",
}


def git(path:Path,*args:str)->str:
    return subprocess.check_output(
        ["git","-C",str(path),*args],
        text=True,encoding="utf-8",errors="replace",timeout=20,
    ).strip()


def load_open(filename:str):
    items=json.loads((ROOT/filename).read_text(encoding="utf-8-sig"))
    assert isinstance(items,list)
    ids=[item["number"] for item in items]
    assert len(set(ids))==len(ids),"duplicated PR number"
    return items


def collect():
    repo_data={}
    for name,(filename,range_ids) in REPOS.items():
        data=load_open(filename)
        by_num={row["number"]:row for row in data}
        chosen=[by_num[num] for num in range_ids if num in by_num]
        missing=sorted(set(range_ids)-set(by_num))
        by_head={row["headRefName"]:row["number"] for row in data}
        inventory=[]
        for pr in chosen:
            parent=by_head.get(pr["baseRefName"])
            inventory.append({
                **pr,
                "parent_open_pr":parent,
                "stacked_on_open_pr":parent is not None,
                "integration_status":"REVIEW_ONLY",
            })
        repo_data[name]={
            "all_open_prs":len(data),
            "selected_prs":inventory,
            "not_open_from_expected_ids":missing,
            "branch_forks":[
                {"number":p["number"],"base":p["baseRefName"]}
                for p in inventory if name=="S3" and p["number"] in (409,410)
            ],
        }
    # Windows Git owns these worktrees. WSL Git cannot resolve the
    # Windows-absolute .git pointers. Git refs are captured via Windows
    # Git and pinned as an explicit JSON evidence snapshot instead.
    refs=json.loads((ROOT/"git_refs_20261115.json").read_text("utf-8-sig"))
    baseline={
        **refs,
        "main_is_not_a_modern_performance_reference":True,
        "branch_is_not_production_release":True,
    }
    fork=json.loads((ROOT/"v12_fork_20261115.json").read_text("utf-8-sig"))
    assert fork["pr409"]["base"]==fork["pr410"]["base"]
    assert set(fork["pr409"]["files"]).isdisjoint(fork["pr410"]["files"])
    return {
        "campaign":"S3_CORE_CONSOLIDATION_20261115",
        "snapshot_date":"2026-11-15",
        "source":"Authenticated GitHub CLI PR list; local git HEAD and branch",
        "decision":"INVENTORY_ONLY_NO_MERGE_NO_DEFAULT_ENABLE",
        "repos":repo_data,
        "studies":STUDIES,
        "initial_screening":DECISIONS,
        "baseline":baseline,
        "v12_fork":fork,
        "release_gate":[
            "Do not merge a child while parent stack is unreviewed.",
            "Pick a single V12 branch line; avoid double-applying sibling work.",
            "Test semantics, signed i64 overflow, bounds/trap parity.",
            "Preserve exact per-instruction logical budget and error output.",
            "Measure compiler and native CPU performance on matched workloads.",
            "Check machine-code growth; V18 is not default-ready.",
            "All checks execute locally through WSL/Remote Desktop Commander.",
            "No GitHub Actions runner dependency or paid CI.",
        ],
    }


def write():
    result=collect()
    (ROOT/"pr_stack_20261115.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",
    )
    lines=[
        "# S3 Core Consolidation — PR dependency map",
        "",
        "Evidence date: 2026-11-15. Source: saved authenticated GitHub CLI snapshots.",
        "",
        "**This is an inventory, not approval to merge any PR.**",
        "",
        "## Key finding",
        "",
        "- S3 `main` is an old historical base, not a qualified current CPU-performance baseline.",
        f"- Historical main: `{result['baseline']['historical_main_sha'][:12]}`.",
        f"- Candidate stack V18: `{result['baseline']['candidate_v18_sha'][:12]}`.",
        f"- Main…V18 commit counts (left/right): `{result['baseline']['main_to_v18_commits']}`.",
        "- V12 has sibling candidate branches on the V11 base. Review their overlap before integration.",
        "- PR #409 touches 9 files; PR #410 touches 8, with **zero shared file paths** in the GitHub PR diff. This is NOT semantic compatibility proof.",
        "- V14–V18 are opt-in studies; neither their standalone correctness nor their speedups justify a global enable.",
        "",
        "## S3 dependency chain (observed PR targets)",
        "",
        "| Stage | S3 | S3-Benchmarks | Relat-rio | Screening |",
        "|---|---|---|---|---|",
    ]
    for phase,per_repo in STUDIES.items():
        cells=[]
        for name in REPOS:
            selected={p["number"]:p for p in result["repos"][name]["selected_prs"]}
            cells.append(", ".join(
                f"[#{n}]({selected[n]['url']})" if n in selected else f"#{n} (NOT OPEN)"
                for n in per_repo.get(name,())
            ))
        lines.append(
            f"| {phase} | {cells[0]} | {cells[1]} | {cells[2]} | {DECISIONS[phase]} |"
        )
    lines+=["","## Explicit PR-to-PR base edges","","| Repo | PR | Parent PR, if open | Base branch | Draft |","|---|---|---|---|---|"]
    for name,rec in result["repos"].items():
        for item in rec["selected_prs"]:
            parent=("#"+str(item["parent_open_pr"])
                    if item["parent_open_pr"] else "not in open snapshot")
            lines.append(
                f"| {name} | [#{item['number']}]({item['url']}) | {parent} | "
                f"`{item['baseRefName']}` | {item['isDraft']} |"
            )
    lines += [
        "",
        "## Gates",
        "",
        "1. Establish two pinned baselines: historic `main` for regression history and V18 as a *candidate*, not as an approved release.",
        "2. Reproduce the known legacy test failures independently; never hide untested failures in a green label.",
        "3. Evaluate dependencies oldest-first; audit the V12 split, then V13…V18.",
        "4. Classify each PR as GO_EXPERIMENTAL, READY_FOR_INTEGRATION, NO_GO, or BLOCKED with a supporting artifact.",
        "5. No global default enablement for V14–V18. V18 has code size and native timing regressions.",
        "6. Use local WSL + Remote Desktop Commander. No paid runners or GitHub Actions gating.",
        "7. No automatic merge, deploy, or reopening Compact/DOOM.",
        "",
        "## Operational WIP",
        "",
        "Kanban canonical branch: `feat/native-kanban-flow-v1-20261111`, PR #38 in Relat-rio.",
        "Agent WIP maximum 2, one per owner. Existing non-S3 priorities are not silently overwritten.",
        "All development/research tasks must have done_when, stop_when, next_action and dated review.",
        "",
    ]
    (ROOT/"DEPENDENCIES_20261115.md").write_text("\n".join(lines),encoding="utf-8")
    for name,item in result["repos"].items():
        print(f"{name}: {item['all_open_prs']} open; "
              f"{len(item['selected_prs'])} selected; "
              f"missing expected={item['not_open_from_expected_ids']}",flush=True)
    print("MAIN_TO_V18",result["baseline"]["main_to_v18_commits"],flush=True)
    print("OUTPUT=pr_stack_20261115.json, DEPENDENCIES_20261115.md",flush=True)


if __name__=="__main__":
    write()
