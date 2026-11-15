#!/usr/bin/env python3
"""Run candidate V18 quality gate with both formerly excluded tests ENABLED.

Uses isolated local quality worktree, never Actions or production.
An independent native SSE2/autovectorization execution group
exercises backend-generated vector ISA absent from source fixture.
"""
from __future__ import annotations
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
from time import perf_counter

ROOT=Path(__file__).resolve().parent
S3=ROOT.parents[2]/"S3-Quality"
from run_local_baseline import CANDIDATE_GROUPS,DSELECTIONS

SIMD_SUITES=(
    "tests/test_s3_v4_9_native_simd.py",
    "tests/test_s3_v5_0_autovectorize.py",
    "tests/test_s3_v4_8_licm_and_simd.py",
    "tests/test_s3_v3_compiler_and_simd.py",
)


def run(name,args,timeout=210):
    t=perf_counter()
    p=subprocess.run(args,cwd=S3,capture_output=True,text=True,timeout=timeout,
        env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"})
    text=p.stdout+p.stderr
    (ROOT/f"{name}.log").write_text(text,"utf-8")
    print(name,"rc",p.returncode,"wall",round(perf_counter()-t,3),
          "\n".join(text.splitlines()[-7:]),flush=True)
    return {
        "name":name,
        "exit_code":p.returncode,
        "elapsed_seconds":round(perf_counter()-t,3),
        "command":args,
        "log":f"{name}.log",
    }


def collect(name,selectors):
    entry=run(name,[sys.executable,"-m","pytest","--collect-only","-q",*selectors],90)
    data=(ROOT/entry["log"]).read_text("utf-8")
    counters={}
    for line in data.splitlines():
        m=re.fullmatch(r"(tests/.+\.py):\s*(\d+)\s*",line.strip())
        if m:
            counters[m.group(1)]=int(m.group(2))
    assert entry["exit_code"]==0 and counters and len(counters)==len(selectors),(
        name,entry,counters,len(selectors)
    )
    entry["tests_collected"]=sum(counters.values())
    entry["per_file"]=counters
    return entry


def main():
    assert S3.is_dir()
    selectors=[]
    for item in CANDIDATE_GROUPS:
        if "*" in item:
            selectors += [str(x.relative_to(S3)) for x in sorted(S3.glob(item))]
        else:
            selectors.append(item)
    assert len(selectors)==len(set(selectors))
    assert all((S3/item).is_file() for item in selectors)
    assert all((S3/selector.split("::")[0]).is_file() for selector in DSELECTIONS)
    assert len(SIMD_SUITES)==len(set(SIMD_SUITES))
    assert all((S3/name).is_file() for name in SIMD_SUITES)

    base=run("quality_v18_core_no_deselections",[
        sys.executable,"-m","pytest","-q","--tb=short",*selectors
    ],210)
    cnt=collect("quality_v18_core_collection",selectors)

    native=run("quality_v18_native_simd",[
        sys.executable,"-m","pytest","-q","--tb=short",*SIMD_SUITES,
    ],180)
    ncnt=collect("quality_v18_native_simd_collection",SIMD_SUITES)

    # Refuse pass unless both selectors really ran under core test collection.
    assert cnt["per_file"].get("tests/test_native_x86_64.py",0)>0
    assert cnt["per_file"].get("tests/test_ffi_capability.py",0)>0
    assert all("--deselect" not in str(arg) for arg in base["command"])
    report={
        "campaign":"S3_CORE_QUALITY_V18_NO_LEGACY_DESELECTIONS_20261115",
        "timestamp_utc":datetime.now(timezone.utc).isoformat(),
        "hardware":platform.platform(),
        "worktree":"S3-Quality based on V18 1a323a03",
        "scope":"Chosen V10-V18+foundation suite; 4 independent native SIMD groups",
        "github_actions_used":False,
        "merge_or_deploy":False,
        "legacy_exclusions":[],
        "legacy_tests_restored":list(DSELECTIONS),
        "core_test_result":base,
        "core_collection":cnt,
        "vector_test_result":native,
        "vector_collection":ncnt,
        "passed":base["exit_code"]==cnt["exit_code"]==native["exit_code"]==ncnt["exit_code"]==0,
        "limits":[
            "This is a selected regression corpus, not the entire repository test corpus.",
            "SIMD suite checks native x86-64 executable output; not GPU RX580.",
            "No automatic merge/default enablement even if local tests pass.",
        ],
    }
    (ROOT/"quality_gate_20261115.json").write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+"\n","utf-8",
    )
    print("QUALITY_TESTS",cnt["tests_collected"],"SIMD",ncnt["tests_collected"],
          "PASS",report["passed"],flush=True)
    if not report["passed"]:raise SystemExit(1)

if __name__=="__main__":main()
