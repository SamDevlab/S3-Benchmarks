#!/usr/bin/env python3
"""V18: aggregate all results, including regressions and code-size costs."""
from __future__ import annotations
import json
from pathlib import Path
import statistics

HERE=Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE/name).read_text("utf-8"))


def run():
    sessions=[read(f"results_autoguard_v18_s{i}.json") for i in (1,2,3)]
    hp03=read("results_autoguard_v18_s1_hp03.json")
    preliminary=read("results_autoguard_v18_whole_function_preliminary_s1.json")
    assert len({r["source_sha256"] for r in (*sessions,hp03,preliminary)})==1
    assert all(len(r["benchmark"]["cases"])==21 for r in sessions)
    all_ratios=[]
    negative=[]
    summaries=[]
    for i in range(21):
        cases=[r["benchmark"]["cases"][i] for r in sessions]
        shape={(c["width"],c["height"]) for c in cases}
        assert len(shape)==1
        assert all(c["parity"] for c in cases)
        width,height=next(iter(shape))
        ratios=[row["speedup"] for row in cases]
        all_ratios.extend(ratios)
        negative.extend(
            {"session":f"s{j+1}","width":width,"height":height,
             "speedup":round(value,6)}
            for j,value in enumerate(ratios) if value<1
        )
        summaries.append({
            "width":width,"height":height,
            "median_session_speedup":round(statistics.median(ratios),6),
            "min_session_speedup":round(min(ratios),6),
            "max_session_speedup":round(max(ratios),6),
            "all_independent_reference_parity":True,
            "by_session":ratios,
        })
        print(f"W{width} H{height} median={statistics.median(ratios):.3f}x "
              f"range={min(ratios):.3f}..{max(ratios):.3f}x",flush=True)
    a=sessions[0]["assembly_bytes"]["baseline"]
    b=sessions[0]["assembly_bytes"]["v18"]
    old=preliminary["assembly_bytes"]["v18"]
    result={
        "campaign":"S3_V18_COMPILER_AUTOGUARD_SELECTIVE_LOOP_SUMMARY",
        "decision":"GO_EXPERIMENTAL_NOT_PRODUCTION",
        "physical_machines":1,
        "process_sessions":3,
        "rounds_per_case_session":9,
        "total_case_session_ratios":len(all_ratios),
        "favorable_observations":sum(rate>1 for rate in all_ratios),
        "regression_observations":len(negative),
        "median_of_all_ratios":round(statistics.median(all_ratios),6),
        "negative_observations":negative,
        "cases":summaries,
        "source_sha256":sessions[0]["source_sha256"],
        "baseline_assembly_bytes":a,
        "initial_whole_function_assembly_bytes":old,
        "final_selective_loop_assembly_bytes":b,
        "initial_whole_function_vs_baseline_percent":round((old/a-1)*100,3),
        "selective_loop_vs_baseline_percent":round((b/a-1)*100,3),
        "selective_loop_vs_whole_function_percent":round((b/old-1)*100,3),
        "hp03_one_session_parity":all(r["parity"] for r in hp03["benchmark"]["cases"]),
        "hp03_is_multi_host_qualification":False,
        "limitations":[
            "Only one WSL Linux x86-64 machine. Timings sensitive to host load.",
            "V18 clones outer loop rather than whole function when safe; still larger than baseline.",
            "No real CPU PMU or production auto-enable based on these numbers.",
            "Initial whole-function baseline preserved for negative design evidence.",
        ],
    }
    output=HERE/"summary_v18.json"
    output.write_text(json.dumps(result,indent=2),"utf-8")
    print(
        f"V18 SUMMARY WINS={result['favorable_observations']}/{len(all_ratios)} "
        f"NEGATIVE={len(negative)} MEDIAN={result['median_of_all_ratios']:.3f}x "
        f"CODE_DELTA={result['selective_loop_vs_baseline_percent']:.1f}%",
        flush=True,
    )
    print("RESULT_FILE="+str(output),flush=True)


if __name__=="__main__":
    run()
