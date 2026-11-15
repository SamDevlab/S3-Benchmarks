#!/usr/bin/env python3
"""S3 Core Consolidation: record locally reproduced test baselines.

No GitHub Actions, no network, no source modifications and no merge.
The historical main is NOT compared as a performance-equivalent backend.
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
S3_V18=ROOT.parents[3]/"V18-Autoguard-Lab"/"S3"
S3_MAIN=ROOT.parents[2]/"S3-main-baseline"
BENCH=ROOT.parents[1]
LOGS=ROOT/"logs"
DSELECTIONS=(
    "tests/test_ffi_capability.py::test_shared_library_compiles_with_requested_optimization_and_syntax_mode",
    "tests/test_native_x86_64.py::test_native_backend_emits_every_current_opcode",
)
CANDIDATE_GROUPS=(
    "tests/test_s3_v18_auto_guard.py",
    "tests/test_s3_v17_dynamic_intervals.py",
    "tests/test_s3_v16_interval_bounds.py",
    "tests/test_s3_v15_slice_bounds_reuse.py",
    "tests/test_s3_v14_x86_asm_peephole.py",
    "tests/test_s3_v13_native_ctz.py",
    "tests/test_s3_v12_*.py",
    "tests/test_s3_v11_auto_algorithm_selection.py",
    "tests/test_s3_v10_gf2_*.py",
    "tests/test_optimizer.py",
    "tests/test_hp_v2_scalar_promotion.py",
    "tests/test_compute_runtime.py",
    "tests/test_ffi_capability.py",
    "tests/test_native_x86_64.py",
)
ARTIFACT_SUITES=(
    "benchmarks/v18_autoguard/test_v18_artifacts.py",
    "benchmarks/v17_dynamic/test_v17_artifacts.py",
    "benchmarks/v16_interval/test_v16_artifacts.py",
    "benchmarks/v15_slice_bounds/test_v15_artifacts.py",
)


def invoke(name:str,cwd:Path,args:list[str],timeout:int=180):
    LOGS.mkdir(parents=True,exist_ok=True)
    t=perf_counter()
    try:
        process=subprocess.run(
            args,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
            text=True,errors="replace",timeout=timeout,
            env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"},
        )
        output=process.stdout
        code=process.returncode
        timeout_hit=False
    except subprocess.TimeoutExpired as ex:
        output=(ex.stdout or b"")
        if isinstance(output,bytes):
            output=output.decode(errors="replace")
        output+="\nTIMEOUT\n"
        code=124
        timeout_hit=True
    duration=round(perf_counter()-t,3)
    (LOGS/f"{name}.log").write_text(output,encoding="utf-8")
    passed=sum(int(n) for n in re.findall(r"(\d+) passed",output))
    failed=sum(int(n) for n in re.findall(r"(\d+) failed",output))
    report={
        "job":name,
        "cwd":"historic_main" if cwd==S3_MAIN else (
            "candidate_v18" if cwd==S3_V18 else "S3-Benchmarks"
        ),
        "command":args,
        "exit_code":code,
        "duration_seconds":duration,
        "passed_reported":passed,
        "failed_reported":failed,
        "timed_out":timeout_hit,
        "log":f"logs/{name}.log",
        "output_tail":"\n".join(output.splitlines()[-9:]),
    }
    print(f"TEST {name}: rc={code}, passed={passed}, failed={failed}, "
          f"duration={duration:.1f}s",flush=True)
    return report


def main():
    refs=json.loads((ROOT/"git_refs_20261115.json").read_text("utf-8-sig"))
    assert S3_V18.exists(),S3_V18
    assert S3_MAIN.exists(),S3_MAIN
    assert BENCH.exists(),BENCH
    created=datetime.now(timezone.utc).isoformat()
    results=[]
    results.append(invoke(
        "candidate_compiler_import_bytecode",S3_V18,
        [sys.executable,"-m","compileall","-q",
         "bootstrap/s3/backends/x86_64"],
        120,
    ))
    expanded=[]
    for item in CANDIDATE_GROUPS:
        if "*" in item:
            expanded.extend(str(x.relative_to(S3_V18)) for x in sorted(S3_V18.glob(item)))
        else:
            assert (S3_V18/item).exists(),item
            expanded.append(item)
    args=[sys.executable,"-m","pytest","-q","--tb=short",*expanded]
    for path in DSELECTIONS:
        args.extend(("--deselect",path))
    results.append(invoke("candidate_v10_v18_regression",S3_V18,args,240))
    for index,selector in enumerate(DSELECTIONS,1):
        results.append(invoke(
            f"inherited_failure_probe_{index}",S3_V18,
            [sys.executable,"-m","pytest","-q","--tb=short",selector],
            90,
        ))
    results.append(invoke(
        "historic_main_shared_smoke",S3_MAIN,
        [sys.executable,"-m","pytest","-q","--tb=short",
         "tests/test_optimizer.py","tests/test_compute_runtime.py",
         "tests/test_native_x86_64.py"],
        160,
    ))
    for index,filename in enumerate(ARTIFACT_SUITES,1):
        if (BENCH/filename).exists():
            results.append(invoke(
                f"benchmark_artifacts_v{19-index}",BENCH,
                [sys.executable,"-m","pytest","-q","--tb=short",filename],
                90,
            ))
    required={
        "candidate_bytecode":results[0]["exit_code"]==0,
        "candidate_core_regression":results[1]["exit_code"]==0,
        "artifact_validators":all(
            x["exit_code"]==0 for x in results
            if x["job"].startswith("benchmark_artifacts_")
        ),
    }
    report={
        "campaign":"S3_CORE_CONSOLIDATION_LOCAL_BASELINE_20261115",
        "recorded_utc":created,
        "runner":"Windows connected PC; WSL Linux x86-64; local Python",
        "platform":platform.platform(),
        "python":sys.version.split()[0],
        "cpu":platform.processor() or "NOT_RECORDED",
        "github_actions":"NOT_USED_NO_REMOTE_CI_ASSERTIONS",
        "source_shas":refs,
        "comparison_contract":"Historical main and V18 are different code bases. No direct speedup inferred.",
        "inherited_deselected_selectors":list(DSELECTIONS),
        "results":results,
        "mandatory_gates":required,
        "all_mandatory_gates_passed":all(required.values()),
        "known_inherited_failure_tests_are_not_counted_passed":True,
        "release_approval":"NO_MERGE_NO_DEPLOY_EXPERIMENTAL_ONLY",
    }
    (ROOT/"baseline_20261115.json").write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",
    )
    print("BASELINE_GATES",json.dumps(required),flush=True)
    print("REPORT="+str(ROOT/"baseline_20261115.json"),flush=True)
    if not report["all_mandatory_gates_passed"]:
        raise SystemExit(1)


if __name__=="__main__":
    main()
