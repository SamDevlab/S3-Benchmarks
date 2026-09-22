# XSBench Warmup Budget Audit

## Decision

```text
CAMPAIGN=S3_BENCHMARKS_2_2_1_2_XSBENCH_WARMUP_BUDGET_ISOLATION
WORKLOAD=scientific.xsbench.compatible_lookup.medium
K_SELECTED=750000
INLINE_WARMUP_BUDGET_CONFOUNDER=CONFIRMED
COMMON_100MS_WINDOW=PASS
S3_SOURCE_CHANGED=NO
```

The frozen driver was tested without rebuilding the frozen artifacts. Every
calibration sample used a fresh process, CPU affinity 0, the same medium
workload, and `WARMUPS=0`. No missing sample was converted to zero.

| K | all four pass | fastest control (ms) | slowest S3 (s) | window |
|---:|:---:|---:|---:|:---:|
| 200000 | PASS | 27.879911 | 3.911466829 | FAIL |
| 250000 | PASS | 41.154412 | 5.159402579 | FAIL |
| 300000 | PASS | 46.765926 | 5.897921033 | FAIL |
| 400000 | PASS | 84.447822 | 8.334581266 | FAIL |
| 450000 | PASS | 72.291885 | 8.859569172 | FAIL |
| 500000 | PASS | 87.447159 | 9.839811930 | FAIL |
| 750000 | PASS | 113.569453 | 14.840859453 | PASS |

The earlier WARMUPS=5 failures at K=250000 through K=450000 were therefore
not an intrinsic inability of the frozen S3 artifacts to execute those K
values. They were caused, at least in part, by the inline warmup work consuming
the finite runtime instruction budget before the measured section.

## Controlled proof

At the selected K, using the frozen `S3_FFI_O0` artifact:

```text
CASE_A fresh process, WARMUPS=0: PASS
CASE_B fresh process, WARMUPS=1: INSTRUCTION_LIMIT
```

This is protocol evidence, not an S3 optimization result. The official
protocol consequently uses five independent warmup samples per variant with
`WARMUPS=0`, discards those times, and then runs the 30 official repetitions
in fresh processes with `WARMUPS=0`.

Raw calibration and proof evidence:

```text
reports/benchmarks-2.2.1-xsbench/raw/xsbench-measurement-closure-v2-20260922-warmup0/
reports/benchmarks-2.2.1-xsbench/raw/xsbench-measurement-closure-v2-20260922-warmup0-extended/
reports/benchmarks-2.2.1-xsbench/raw/xsbench-measurement-closure-v2-20260922-warmup0-official/warmup_budget_proof.json
```
