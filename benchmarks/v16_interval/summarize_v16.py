#!/usr/bin/env python3
"""Aggregate three actual same-host S3 x86-64 A/B stencil sessions."""
from __future__ import annotations
import json
from pathlib import Path
import statistics

HERE=Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE/name).read_text("utf-8"))


def run():
    sessions=[read(f"results_interval_v16_s{i}.json") for i in (1,2,3)]
    hp03=read("results_interval_v16_s1_hp03.json")
    signature={session["original_s3_source_sha256"] for session in sessions}
    assert len(signature)==1
    assert all(session["benchmark"]["rounds"]==9 for session in sessions)
    outputs=[]
    wins=0
    regressions=[]
    ratios=[]
    for case_index in range(9):
        cases=[session["benchmark"]["cases"][case_index] for session in sessions]
        dimension={(c["width"],c["height"]) for c in cases}
        assert len(dimension)==1
        assert all(c["parity"] for c in cases)
        width,height=next(iter(dimension))
        gains=[c["speedup"] for c in cases]
        ratios.extend(gains)
        wins+=sum(r>1 for r in gains)
        regressions.extend([
            {"session":f"s{j+1}","width":width,"height":height,
             "speedup":round(value,6)}
            for j,value in enumerate(gains) if value<1
        ])
        output={
            "width":width,"height":height,
            "median_session_speedup":round(statistics.median(gains),6),
            "min_session_speedup":round(min(gains),6),
            "max_session_speedup":round(max(gains),6),
            "session_speedups":gains,
            "session_baseline_ns":[c["baseline_ns"] for c in cases],
            "session_v16_ns":[c["v16_ns"] for c in cases],
            "all_independent_c_parity":True,
        }
        outputs.append(output)
        print(
            f"W{width} H{height} median={output['median_session_speedup']:.3f}x "
            f"range={min(gains):.3f}..{max(gains):.3f}x",
            flush=True,
        )
    report={
        "campaign":"S3_V16_2D_EIGHT_NEIGHBOR_INTERVAL_NATIVE_SUMMARY",
        "sessions":3,"physical_machines":1,"rounds_per_session_per_case":9,
        "different_operating_systems_compared":False,
        "same_s3_ir":True,
        "experimental_flag_default_off":True,
        "baseline_v15_branch":"exp/s3-v15-slice-bounds-reuse",
        "observed_gain_rows":wins,
        "observed_regression_rows":len(regressions),
        "observed_total_rows":len(ratios),
        "median_of_all_27_per_session_speedup_ratios":
            round(statistics.median(ratios),6),
        "negative_rows":regressions,
        "hp03_one_session":True,
        "hp03_fast_versioned_candidates_verified":False,
        "hp03_note":"This particular source did not produce an HP03 fast-versioned loop; no general coexistence qualification.",
        "stencil_cases":outputs,
        "interpretation":"Exploratory same-host evidence; ratios are not statistical confidence bounds and should not enable compiler defaults.",
    }
    dest=HERE/"summary_v16.json"
    dest.write_text(json.dumps(report,indent=2),"utf-8")
    print(f"WINS={wins}/{len(ratios)} MEDIAN={report['median_of_all_27_per_session_speedup_ratios']:.3f}x",flush=True)
    print("RESULT_FILE="+str(dest),flush=True)


if __name__=="__main__":
    run()
