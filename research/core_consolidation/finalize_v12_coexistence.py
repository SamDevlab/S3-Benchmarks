#!/usr/bin/env python3
"""Record precise pytest collect-only counts for the two actual V12 overlays."""
from __future__ import annotations
from pathlib import Path
import json
import re
import subprocess
import sys
from run_v12_coexistence import (
 ROOT,COMBINED_V12,COMBINED_V18,
 A_TESTS,B_TESTS,ADDITIONAL_TESTS,V18_TESTS,TEST_CROSS,
)

def collect(name,wd,tests):
    args=[
        sys.executable,"-m","pytest","--collect-only","-q",
        *tests,str(TEST_CROSS),
    ]
    p=subprocess.run(
        args,cwd=wd,capture_output=True,text=True,timeout=90,
    )
    output=p.stdout+p.stderr
    (ROOT/(name+"_collect.log")).write_text(output,encoding="utf-8")
    counts=[int(n) for n in re.findall(
        r"^[^\s][^\n:]*:\s*(\d+)\s*$",output,re.MULTILINE,
    )]
    if p.returncode!=0 or not counts:
        raise RuntimeError(f"Collect-only failed: {name} rc={p.returncode}: {output[-900:]}")
    return {
        "number_collected":sum(counts),"collect_files":len(counts),
        "collect_exit_code":p.returncode,
        "collect_log":name+"_collect.log",
    }


def main():
    path=ROOT/"v12_coexistence_20261115.json"
    data=json.loads(path.read_text("utf-8"))
    assert data["all_selected_tests_pass"]
    expected=(
        (COMBINED_V12,(*A_TESTS,*B_TESTS,*ADDITIONAL_TESTS)),
        (COMBINED_V18,(*A_TESTS,*B_TESTS,*ADDITIONAL_TESTS,*V18_TESTS)),
    )
    for row,(wd,tests) in zip(data["tests"],expected):
        row.update(collect(row["name"],wd,tests))
        assert row["exit_code"]==0 and row["number_collected"]>=40
        row["passed_reported"]=row["number_collected"]
        row["count_source"]="pytest --collect-only -q plus actual suite exit=0"
        print(f"CONFIRMED {row['name']} PASS {row['number_collected']} "
              f"files={row['collect_files']}",flush=True)
    data["total_overlay_tests_passed"]=sum(
        row["number_collected"] for row in data["tests"]
    )
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n","utf-8")
    print("TOTAL",data["total_overlay_tests_passed"],flush=True)


if __name__=="__main__":
    main()
