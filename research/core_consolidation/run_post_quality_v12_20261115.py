#!/usr/bin/env python3
"""Post-fix V18 + V12-A cross-family regression WITHOUT deselections.

This is the local-only overlay 5340c39e built on V18 1a323a03,
V12-A a271bbfd and quality fix 356b323c. No merge to original branches.
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
WORKTREE=ROOT.parents[2]/"S3-V18-Combined"
from run_full_stack_20261115 import TESTS,CROSS,KNOWN

def execute(label,command):
    start=perf_counter()
    result=subprocess.run(
        command,cwd=WORKTREE,capture_output=True,text=True,timeout=180,
    )
    output=result.stdout+result.stderr
    (ROOT/f"{label}.log").write_text(output,encoding="utf-8")
    print(label,"exit_code",result.returncode,
          "seconds",round(perf_counter()-start,2),
          "\n".join(output.splitlines()[-7:]),flush=True)
    return result.returncode,output,round(perf_counter()-start,3)

def main():
    selector=tuple(n for group in TESTS.values() for n in group)
    assert len(set(selector))==len(selector)
    assert (WORKTREE/"tests"/"test_s3_v12_verified_strategy_registry.py").is_file()
    assert (WORKTREE/"tests"/"test_s3_v18_auto_guard.py").is_file()
    for item in KNOWN:
        assert (WORKTREE/item.split("::")[0]).is_file()
    cmd=[sys.executable,"-m","pytest","-q","--tb=short",*selector,str(CROSS)]
    assert "--deselect" not in cmd
    code,output,seconds=execute("post_quality_v18_v12a_tests",cmd)
    gather=[sys.executable,"-m","pytest","--collect-only","-q",*selector,str(CROSS)]
    ccode,clog,csecs=execute("post_quality_v18_v12a_collect",gather)
    counts=[int(n) for n in re.findall(
        r"^tests/.+\.py:\s*(\d+)\s*$",clog,re.MULTILINE
    )]
    external=[int(n) for n in re.findall(r"^:\s*(\d+)\s*$",clog,re.MULTILINE)]
    assert len(counts)==len(selector) and len(external)==1,(counts,external)
    total=sum(counts)+sum(external)
    verified=code==ccode==0 and total==229
    report={
        "campaign":"S3_CORE_POST_QUALITY_V12A_V18_SELECTED_FULL_LOCAL",
        "utc":datetime.now(timezone.utc).isoformat(),
        "source":"S3-V18-Combined local-only overlay",
        "combined_head":"5340c39e96aa90d9fd1cc94592e6059107098893",
        "v18_parent":"1a323a033c361d904aa6b9ce747364f7ee05255e",
        "v12a_commit":"a271bbfdf8f9a4d2f1c1cff5fcb27fd973e0cfa0",
        "quality_commit":"356b323c3677f46fee69f1c535bb7f349b2fe35c",
        "runner":platform.platform(),
        "tests_collected":total,
        "test_exit_code":code,
        "collection_exit_code":ccode,
        "test_runtime_seconds":seconds,
        "collection_runtime_seconds":csecs,
        "logs":["post_quality_v18_v12a_tests.log","post_quality_v18_v12a_collect.log"],
        "previously_deselected_tests":list(KNOWN),
        "deselected_tests":[],
        "all_selected_pass":verified,
        "github_actions_used":False,
        "merged_to_main":False,
        "production_changes":False,
        "scope_limit":"Selected V11–V18 and foundation suite plus V12-A research; not entire repository or physical GPU.",
    }
    (ROOT/"post_quality_v18_v12a_20261115.json").write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+"\n","utf-8",
    )
    print("POST_QUALITY_TESTS",total,"PASS",verified,flush=True)
    if not verified:raise SystemExit(1)

if __name__=="__main__":main()
