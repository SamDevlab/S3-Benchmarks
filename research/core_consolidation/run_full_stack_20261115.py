#!/usr/bin/env python3
"""Local differential release triage of entire V11–V18 stack + isolated V12-A.

No GitHub Actions, PR merge, production change, or benchmark claims.
Tests operate on the *local-only* V18+#409 combined worktree.
"""
from __future__ import annotations
import json
from pathlib import Path
import os
import platform
import re
import subprocess
import sys
from time import perf_counter
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parent
S3=ROOT.parents[2]/"S3-V18-Combined"
TESTS={
"V11":("tests/test_s3_v11_auto_algorithm_selection.py",),
"V12-A":(
"tests/test_s3_v12_empirical_gpu_dispatch.py",
"tests/test_s3_v12_verified_i64_native.py",
"tests/test_s3_v12_verified_i64_progression.py",
"tests/test_s3_v12_verified_strategy_registry.py",
),
"V12-B":(
"tests/test_s3_v12_gpu_cost_dispatch.py",
"tests/test_s3_v12_sparse_codegen.py",
"tests/test_s3_v12_verified_candidates.py",
),
"V13":("tests/test_s3_v13_native_ctz.py",),
"V14":("tests/test_s3_v14_x86_asm_peephole.py",),
"V15":("tests/test_s3_v15_slice_bounds_reuse.py",),
"V16":("tests/test_s3_v16_interval_bounds.py",),
"V17":("tests/test_s3_v17_dynamic_intervals.py",),
"V18":("tests/test_s3_v18_auto_guard.py",),
"FOUNDATION":(
"tests/test_optimizer.py",
"tests/test_hp_v2_scalar_promotion.py",
"tests/test_compute_runtime.py",
"tests/test_ffi_capability.py",
"tests/test_native_x86_64.py",
),
}
CROSS=ROOT/"test_v12_cross_family.py"
KNOWN=(
"tests/test_ffi_capability.py::test_shared_library_compiles_with_requested_optimization_and_syntax_mode",
"tests/test_native_x86_64.py::test_native_backend_emits_every_current_opcode",
)

def execute(args,log,timeout=210):
    t=perf_counter()
    p=subprocess.run(
       args,cwd=S3,capture_output=True,text=True,timeout=timeout,
       env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"},
    )
    output=p.stdout+p.stderr
    (ROOT/log).write_text(output,encoding="utf-8")
    return p.returncode,round(perf_counter()-t,3),output

def main():
    assert S3.is_dir() and CROSS.is_file()
    selected=tuple(p for files in TESTS.values() for p in files)
    assert len(selected)==len(set(selected))
    assert all((S3/p).is_file() for p in selected)
    args=[sys.executable,"-m","pytest","-q","--tb=short",*selected,str(CROSS)]
    for dis in KNOWN: args.extend(("--deselect",dis))
    rc,secs,output=execute(args,"full_stack_v11_v18_with_v12a.log")
    print("RELEASE_SUITE",rc,secs,"\n".join(output.splitlines()[-8:]),flush=True)
    collect=[sys.executable,"-m","pytest","--collect-only","-q",*selected,str(CROSS)]
    for dis in KNOWN: collect.extend(("--deselect",dis))
    crc,csecs,clog=execute(collect,"full_stack_collect.log",60)
    assert crc==0,clog[-1200:]
    counts={}
    for row in clog.splitlines():
        m=re.fullmatch(r"(.+\.py):\s*(\d+)\s*",row.strip())
        if m:
            key=m.group(1)
            counts[key]=int(m.group(2))
    # The custom quiet collector renders our sole absolute external test
    # file as ': 4'; match that explicit record, never guess from % bars.
    external_counts=[
        int(match.group(1)) for row in clog.splitlines()
        if (match:=re.fullmatch(r":\s*(\d+)\s*",row.strip()))
    ]
    if len(external_counts)!=1:
        raise RuntimeError("Unexpected number of external pytest collections")
    counts[str(CROSS)]=external_counts[0]
    missing=[str(p) for p in selected if p not in counts]
    if missing: raise RuntimeError("Missing collected tests "+repr(missing))
    cross=[n for p,n in counts.items() if p.endswith("test_v12_cross_family.py")]
    if len(cross)!=1:raise RuntimeError("Missing cross-family count")
    total=sum(counts.values())
    manifest=json.loads((ROOT/"pr_stack_20261115.json").read_text("utf-8"))
    assert manifest["baseline"]["candidate_v18_sha"].startswith("1a323a03")
    report={
       "campaign":"S3_CORE_V11_V18_RELEASE_TRIAGE_WITH_V12A",
       "date_utc":datetime.now(timezone.utc).isoformat(),
       "local_runner":platform.platform(),
       "baseline":"V18 branch + local-only V12-A #409 compatibility overlay",
       "source_v18_base":manifest["baseline"]["candidate_v18_sha"],
       "source_v12a":"a271bbfdf8f9a4d2f1c1cff5fcb27fd973e0cfa0",
       "no_actions_no_merge_no_deploy":True,
       "release_claim":"NO_DEFAULT_NO_MERGE_ONLY_LOCAL_COMPATIBILITY",
       "test_command":args,
       "test_exit_code":rc,
       "test_runtime_seconds":secs,
       "collection_exit_code":crc,
       "collection_runtime_seconds":csecs,
       "collected_total":total,
       "counts_by_file":counts,
       "counts_by_stage":{
           stage:sum(counts[p] for p in paths)
           for stage,paths in TESTS.items()
       },
       "cross_family_tests":cross[0],
       "inherited_test_exclusions":KNOWN,
       "inherited_tests_still_open":True,
       "observed_success":rc==0 and total>=220,
       "limits":[
           "Scope is explicit test selection, not full repository pytest suite.",
           "Two known inherited failures were deselected and independently reproduced before.",
           "One WSL Linux host; no physical GPU RX580 test or multi-host native performance.",
           "IR source proof and native tests do not imply formal arbitrary-program equivalence.",
           "No release, production enablement or semantic merge approval.",
       ],
    }
    (ROOT/"release_triage_matrix_20261115.json").write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+"\n","utf-8"
    )
    print("RELEASE_TRIAGE_TESTS",total,flush=True)
    print("RELEASE_STAGE_COUNTS",report["counts_by_stage"],flush=True)
    print("RESULT",report["observed_success"],flush=True)
    if not report["observed_success"]:raise SystemExit(1)

if __name__=="__main__":main()
