#!/usr/bin/env python3
"""Parse pytest's custom quiet collection into pinned factual test counts."""
from __future__ import annotations
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
REPORT=ROOT/"baseline_20261115.json"
MAIN=ROOT.parents[2]/"S3-main-baseline"
PATTERN=re.compile(r"^tests/[^:\n]+:\s*(\d+)\s*$",re.MULTILINE)

def main():
    report=json.loads(REPORT.read_text("utf-8"))
    collected=(ROOT/"logs"/"candidate_collect_only.log").read_text("utf-8")
    counts=[int(n) for n in PATTERN.findall(collected)]
    if len(counts)<10:
        raise RuntimeError("Candidate collection unexpected; refuse fabricated count")
    report["candidate_collection"]["number_in_summary"]=sum(counts)
    report["candidate_collection"]["collected_files"]=len(counts)
    assert report["candidate_collection"]["exit_code"]==0

    cmd=[sys.executable,"-m","pytest","--collect-only","-q",
         "tests/test_compiler.py","tests/test_optimizer.py",
         "tests/test_native_x86_64.py"]
    p=subprocess.run(cmd,cwd=MAIN,capture_output=True,text=True,timeout=90)
    (ROOT/"logs"/"historical_main_collect_only.log").write_text(
        p.stdout+"\n"+p.stderr,encoding="utf-8",
    )
    hist=[int(n) for n in PATTERN.findall(p.stdout)]
    report["historical_collection"]={
        "exit_code":p.returncode,
        "number_collected":sum(hist) if hist else None,
        "files":len(hist),
        "log":"logs/historical_main_collect_only.log",
    }
    assert p.returncode==0 and hist
    assert report["candidate_collection"]["number_in_summary"]>=200
    assert report["all_mandatory_gates_passed"] is True
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n","utf-8")
    print("V18_SELECTED_TESTS",sum(counts),"FILES",len(counts))
    print("HISTORICAL_MAIN_SMOKE",sum(hist),"FILES",len(hist))
    print("ARTIFACT_VALIDATORS",sum(
        r["passed_reported"] for r in report["results"]
        if r["job"].startswith("benchmark_artifacts_")
    ))
    print("MANDATORY_LOCAL_GATES",report["mandatory_gates"])
    print("BASELINE",REPORT)


if __name__=="__main__":
    main()
