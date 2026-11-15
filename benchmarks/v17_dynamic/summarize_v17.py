#!/usr/bin/env python3
"""Faithfully summarize all measured native dynamic-width S3 trials."""
from __future__ import annotations
import json
from pathlib import Path
import statistics

HERE=Path(__file__).resolve().parent

def read(name):
    return json.loads((HERE/name).read_text("utf-8"))


def run():
    sessions=[read(f"results_dynamic_v17_s{i}.json") for i in (1,2,3)]
    hp03=read("results_dynamic_v17_s1_hp03.json")
    assert {s["source_sha256"] for s in sessions}=={hp03["source_sha256"]}
    assert all(len(s["benchmark"]["cases"])==21 for s in sessions)
    ratios=[]
    cases=[]
    negative=[]
    for index in range(21):
        group=[s["benchmark"]["cases"][index] for s in sessions]
        dims={(row["width"],row["height"]) for row in group}
        assert len(dims)==1
        width,height=next(iter(dims))
        assert all(row["parity"] for row in group)
        rates=[row["speedup"] for row in group]
        ratios.extend(rates)
        for i,value in enumerate(rates):
            if value<1:
                negative.append({
                    "session":f"s{i+1}","width":width,
                    "height":height,"speedup":round(value,6),
                })
        cases.append({
            "width":width,"height":height,
            "all_correct":True,
            "median_session_speedup":round(statistics.median(rates),6),
            "min_session_speedup":round(min(rates),6),
            "max_session_speedup":round(max(rates),6),
            "by_session":rates,
        })
        print(f"DYNAMIC {width}x{height}: "
              f"median={statistics.median(rates):.3f}x "
              f"range={min(rates):.3f}..{max(rates):.3f}x",
              flush=True)
    result={
        "campaign":"S3_V17_DYNAMIC_WIDTH_NATIVE_AB_AGGREGATE",
        "same_host_separate_process_sessions":3,
        "independent_physical_computers":1,
        "rounds_per_case_session":9,
        "total_case_session_ratios":len(ratios),
        "positive_ratio_observations":sum(rate>1 for rate in ratios),
        "regression_observations":len(negative),
        "median_of_all_case_session_ratios":round(statistics.median(ratios),6),
        "source_sha256":sessions[0]["source_sha256"],
        "negative_observations":negative,
        "cases":cases,
        "hp03_one_session":{
            "all_parity":all(c["parity"] for c in hp03["benchmark"]["cases"]),
            "observations":len(hp03["benchmark"]["cases"]),
            "note":"One same-host HP03-on A/B only; no generalized compatibility qualification.",
        },
        "decision":"GO_EXPERIMENTAL_NOT_PRODUCTION",
        "limitations":[
            "Single physical machine and OS (WSL Linux), no CPU PMU.",
            "A proof of legal optimization under explicit user-source guard, not automatic compiler guard synthesis.",
            "Outlier/regression rows preserved, timing is not a CI correctness gate.",
            "C implementation used solely as independent oracle and timer driver.",
        ],
    }
    output=HERE/"summary_v17.json"
    output.write_text(json.dumps(result,indent=2),"utf-8")
    print(f"V17_SUMMARY gain={result['median_of_all_case_session_ratios']:.3f}x "
          f"wins={result['positive_ratio_observations']}/{len(ratios)} "
          f"regressions={len(negative)}",flush=True)
    print("RESULT_FILE="+str(output),flush=True)


if __name__=="__main__":
    run()
