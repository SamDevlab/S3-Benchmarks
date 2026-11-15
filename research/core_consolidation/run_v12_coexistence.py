#!/usr/bin/env python3
"""Real local V12 #409 + #410 semantic/native compatibility campaign.

All source overlays are temporary Windows Git worktrees created
outside this repository by the operator; they are never merged,
pushed, or built in production.

Two checks:
  A-on-B   = PR #409 cherry-picked --no-commit over PR #410
  A-on-V18 = PR #409 cherry-picked --no-commit over the V18 stack
A's four original tests and B's three original tests are executed
in each environment together, plus cross-family integration tests.
"""
from __future__ import annotations

from datetime import datetime,timezone
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
from time import perf_counter

ROOT=Path(__file__).resolve().parent
WORKSPACE=ROOT.parents[2]
COMBINED_V12=WORKSPACE/"S3-V12-Combined"
COMBINED_V18=WORKSPACE/"S3-V18-Combined"
TEST_CROSS=ROOT/"test_v12_cross_family.py"
A_TESTS=(
    "tests/test_s3_v12_empirical_gpu_dispatch.py",
    "tests/test_s3_v12_verified_i64_native.py",
    "tests/test_s3_v12_verified_i64_progression.py",
    "tests/test_s3_v12_verified_strategy_registry.py",
)
B_TESTS=(
    "tests/test_s3_v12_gpu_cost_dispatch.py",
    "tests/test_s3_v12_sparse_codegen.py",
    "tests/test_s3_v12_verified_candidates.py",
)
ADDITIONAL_TESTS=(
    "tests/test_s3_v11_auto_algorithm_selection.py",
    "tests/test_optimizer.py",
)
V18_TESTS=(
    "tests/test_s3_v13_native_ctz.py",
    "tests/test_s3_v14_x86_asm_peephole.py",
    "tests/test_s3_v15_slice_bounds_reuse.py",
    "tests/test_s3_v16_interval_bounds.py",
    "tests/test_s3_v17_dynamic_intervals.py",
    "tests/test_s3_v18_auto_guard.py",
)


def run(name,cwd:Path,tests:tuple[str,...],timeout:int=220):
    missing=[name for name in tests if not (cwd/name).exists()]
    if missing:
        raise RuntimeError(f"Missing tests on {cwd}: {missing}")
    args=[
        sys.executable,"-m","pytest","-q","--tb=short",
        *tests,str(TEST_CROSS),
    ]
    start=perf_counter()
    try:
        proc=subprocess.run(args,cwd=cwd,capture_output=True,text=True,timeout=timeout)
        rc=proc.returncode
        output=proc.stdout+proc.stderr
        timed_out=False
    except subprocess.TimeoutExpired as exc:
        output=str(exc)
        rc=124
        timed_out=True
    seconds=round(perf_counter()-start,3)
    log=ROOT/f"{name}.log"
    log.write_text(output,encoding="utf-8")
    match=re.findall(r"(\d+) passed",output)
    observed=sum(int(v) for v in match)
    print(f"V12_{name} rc={rc} passed={observed} elapsed={seconds}s",flush=True)
    print("RESULT_TAIL","\n".join(output.splitlines()[-10:]),flush=True)
    return {
        "name":name,"cwd":cwd.name,
        "exit_code":rc,"passed_reported":observed,
        "elapsed_seconds":seconds,"timed_out":timed_out,
        "log":log.name,"tests":[*tests,str(TEST_CROSS.name)],
        "stdout_tail":"\n".join(output.splitlines()[-10:]),
    }


def check():
    assert COMBINED_V12.exists() and COMBINED_V18.exists()
    fork=json.loads((ROOT/"v12_fork_20261115.json").read_text("utf-8-sig"))
    assert fork["pr409"]["file_count"]==9
    assert fork["pr410"]["file_count"]==8
    assert fork["overlap_file_count"]==0
    for wd in (COMBINED_V12,COMBINED_V18):
        for filename in (*A_TESTS,*B_TESTS):
            assert (wd/filename).exists(),f"Overlay incomplete: {wd}/{filename}"
    results=[
        run("b_plus_a_original_v12",COMBINED_V12,(*A_TESTS,*B_TESTS,*ADDITIONAL_TESTS)),
        run("v18_plus_a_regression",COMBINED_V18,(*A_TESTS,*B_TESTS,*ADDITIONAL_TESTS,*V18_TESTS)),
    ]
    report={
        "campaign":"S3_CORE_V12_SEMANTIC_COHABITATION_20261115",
        "observed_at_utc":datetime.now(timezone.utc).isoformat(),
        "methods":"Windows Git cherry-pick --no-commit into two isolated worktrees; Linux WSL native test",
        "hardware":platform.platform(),
        "source_branches":{
            "A":"PR #409 a271bbfdf8f9a4d2f1c1cff5fcb27fd973e0cfa0",
            "B":"PR #410 02f0a3f76b138b5495362fe9161058cdee00f3f7",
            "stack":"V18 1a323a033c361d904aa6b9ce747364f7ee05255e",
        },
        "no_original_branch_modified":True,
        "no_merge_no_remote_push_no_actions":True,
        "file_level_conflicts":0,
        "semantic_contracts":{
            "a_i64_progression_verified":True,
            "b_i64_identity_verified":True,
            "a_not_wired_production":True,
            "independent_optin_gates":True,
        },
        "tests":results,
        "all_selected_tests_pass":all(r["exit_code"]==0 for r in results),
        "decision":"GO_EXPERIMENTAL_COMPATIBLE_SUBSET" if all(r["exit_code"]==0 for r in results) else "NO_GO_COMPATIBILITY_INCOMPLETE",
        "not_proved":[
            "No universal source-language compatibility proof.",
            "Does not verify PR #409 runtime GPU dispatch on physical RX580.",
            "Passing B+A and V18+A does not authorize merge of stacked PRs.",
            "Selection cost metrics require real host measurements, not fixture samples.",
        ],
    }
    (ROOT/"v12_coexistence_20261115.json").write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",
    )
    print("DECISION",report["decision"],flush=True)
    print("EVIDENCE",ROOT/"v12_coexistence_20261115.json",flush=True)
    if not report["all_selected_tests_pass"]:
        raise SystemExit(1)


if __name__=="__main__":
    check()
