#!/usr/bin/env python3
"""Preserve completed V18 evidence; correct only historical smoke selector."""
from __future__ import annotations
from datetime import datetime,timezone
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from run_local_baseline import (S3_MAIN,S3_V18,ROOT as DATA,invoke,
                                DSELECTIONS,CANDIDATE_GROUPS)

def run():
    path=ROOT/"baseline_20261115.json"
    report=json.loads(path.read_text("utf-8"))
    old=next(x for x in report["results"]
             if x["job"]=="historic_main_shared_smoke")
    assert old["exit_code"]==4
    assert "file or directory not found" in (
        ROOT/old["log"]).read_text("utf-8")
    # No previous successful job is rerun or overwritten.
    smoke=invoke(
        "historic_main_available_smoke",S3_MAIN,
        [sys.executable,"-m","pytest","-q","--tb=short",
         "tests/test_compiler.py","tests/test_optimizer.py",
         "tests/test_native_x86_64.py"],180,
    )
    report["results"].append(smoke)
    report["historical_main_smoke_status"]="DIAGNOSTIC_ONLY_NOT_EQUIVALENT_TO_V18"
    report["historical_main_smoke_repaired_selector"]=True
    report["historical_main_smoke_exit_code"]=smoke["exit_code"]

    # Collection count is performed separately; the repository's
    # pytest configuration deliberately prints no summary for -q.
    args=[sys.executable,"-m","pytest","--collect-only","-q"]
    for file in CANDIDATE_GROUPS:
        if "*" in file:
            args.extend(str(p.relative_to(S3_V18)) for p in sorted(S3_V18.glob(file)))
        else:
            args.append(file)
    for selector in DSELECTIONS:
        args.extend(("--deselect",selector))
    collection=subprocess.run(
        args,cwd=S3_V18,capture_output=True,text=True,timeout=90,
    )
    (ROOT/"logs"/"candidate_collect_only.log").write_text(
        collection.stdout+"\n"+collection.stderr,encoding="utf-8",
    )
    match=re.findall(
        r"(\d+) tests? (?:collected|selected)",collection.stdout,
        flags=re.IGNORECASE,
    )
    report["candidate_collection"]={
        "exit_code":collection.returncode,
        "number_in_summary":int(match[-1]) if match else None,
        "log":"logs/candidate_collect_only.log",
        "summary_tail":"\n".join(collection.stdout.splitlines()[-8:]),
    }
    report["historical_correction_utc"]=datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n","utf-8")
    print("HIST_MAIN",smoke["exit_code"],smoke["output_tail"],flush=True)
    print("CANDIDATE_COLLECT",report["candidate_collection"],flush=True)
    print("OVERALL_MANDATORY",report["all_mandatory_gates_passed"],flush=True)


if __name__=="__main__":
    run()
