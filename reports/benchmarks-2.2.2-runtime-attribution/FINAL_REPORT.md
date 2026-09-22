# S3-Benchmarks 2.2.2 Runtime Cost Attribution and Frontier Lab

## Decision

This benchmark-only campaign completed the Linux causal experiment for the
instruction-budget hypothesis without modifying S3. The diagnostic artifact
was natively correct, independent G/H sessions were reproducible, and removing
only instruction-budget accounting reduced the measured XSBench baseline time
by 56.7777% at O0 and 52.6631% at O1. H2 is therefore confirmed for this
workload, host, artifact, and protocol. The remaining no-budget gap is still
45.61x/48.23x versus GCC and 58.56x/61.92x versus Clang.

The conditional frame experiment was also completed after the residual exceeded
the declared 5x trigger. Removing only the three frame-accounting sites passed
correctness, but made the timed artifact slower in both independent I/J
sessions. Frame attribution is therefore **NOT_CONFIRMED**; the result does not
justify a frame-cost claim or a subsequent H4/H5 experiment in this campaign.

`QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE` because the no-budget and no-frame
artifacts are diagnostic safety-envelope variants, not official S3 production
artifacts. `S3_PRODUCTION_CHANGE_READY=NO`.

## Native Resume

- branch: `research/benchmarks-2.2.2-runtime-attribution-frontier-lab`
- benchmark HEAD at the start: `44015b7fc0ef6ecdf93ceeb421c25191e41c87c5`
- workload: `scientific.xsbench.compatible_lookup.medium`
- `K=750000`; inline warmups `0`; five external warmups; 30 fresh-process
  repetitions per variant; balanced interleaving; CPU 0; `CLOCK_MONOTONIC_RAW`
- raw evidence: `raw/native-resume-20260922-074209/`
- no new full suite was run; inherited benchmark suite evidence remains
  `59 passed, 1 skipped, 0 failed`

## VirtualBox / s3-vm Recovery

The existing registered Ubuntu VM was already running and reachable through the
existing `s3-vm` SSH alias. No VM configuration or power operation was used.

- `VIRTUALBOX_ACTIVE=YES`
- `S3_VM_FOUND=YES`
- `S3_VM_STATE=RUNNING`
- `LINUX_ENVIRONMENT_RECOVERY=SAME_S3_VM`
- `KEEP_HOST_RUNNING=YES`
- `KEEP_VM_RUNNING=YES`

## Host Identity

The native guest was Linux x86-64 with Python 3.14.4, GCC 15.2.0, Clang
21.1.8, binutils 2.46, three logical CPUs, and `perf` 7.0.14. The new guest
fingerprint is:

`9f6c7cbbdbbc2d056ffc306f76a1dcd9df194e15167cb037542da54e97b59393`

This differs from the earlier E/F fingerprint
`cae6d65e71c97a0b0bbc1d83697faf67958777f50b7f6fc922e5de4b175abade`, so
`HOST_CHANGED=YES`. The selected K remained valid because the fastest control
was at least 100 ms in preflight; `K_RECALIBRATED=NO`.

## Native Artifact Build

The pinned S3 assembly was reproduced byte-identically. The Linux rebuilds of
the baseline shared objects are semantically usable and correct, but their
hashes differ from the frozen objects because the host/toolchain changed:
`BASELINE_SO_REPRODUCTION=SEMANTIC_REBUILD_TOOLCHAIN_DRIFT`.

The diagnostic rewriter removed exactly 521 O0 and 520 O1 instruction-budget
sites, with zero unexpected mutations. The frame rewriter removed exactly three
entry/exit accounting pairs per optimization level, preserving prologues,
returns, and failure-report blocks. Both rewrites are benchmark-side and
diagnostic-only; no S3 source or safety implementation was changed.

## ELF Metrics

| artifact | ELF bytes | `.text` bytes |
|---|---:|---:|
| S3 O0 baseline | 279240 | 72420 |
| S3 O1 baseline | 279240 | 72725 |
| S3 O0 no-budget | 262856 | 56781 |
| S3 O1 no-budget | 262856 | 57116 |
| GCC O2 | 15488 | not recorded in the preserved ELF transcript |
| Clang O2 | 15240 | not recorded in the preserved ELF transcript |

The missing control `.text` values are reported as unavailable rather than
inferred. Full artifact hashes and the exact preserved ELF transcript are in
the raw run directory.

## Diagnostic Correctness

All six base variants passed TINY, SMALL, and MEDIUM against the independent
oracle: 18/18 observations. The frame no-budget/no-frame variants passed all
six additional TINY/SMALL/MEDIUM checks. Observable results were unchanged.

## Run G / Run H

Both sessions completed with 30 official samples for each of six variants,
plus five discarded external warmups per variant. Every official sample passed
the correctness check. The combined medians are:

| variant | median ns |
|---|---:|
| S3 O0 baseline | 14325439969.5 |
| S3 O0 no-budget | 6191784662.5 |
| S3 O1 baseline | 13832552419.5 |
| S3 O1 no-budget | 6547907311.0 |
| GCC O2 | 135752878.5 |
| Clang O2 | 105742938.5 |

## G/H Reproducibility

All six variants passed the declared 25% median-delta criterion. The maximum
delta was `0.0537918232` for Clang O2. Therefore
`G_H_REPRODUCIBILITY=PASS`.

## Instruction Budget Causal Attribution

H2 is `CONFIRMED_CAUSAL` within the declared scope. The diagnostic rewrite
removed the following fraction of baseline elapsed time:

| level | ratio baseline/diagnostic | absolute cost ns | baseline share |
|---|---:|---:|---:|
| O0 | 2.3136205069 | 8133655307.0 | 0.5677769984 |
| O1 | 2.1125150010 | 7284645108.5 | 0.5266305804 |

The corresponding excess-time fractions removed relative to controls were:

- O0 vs GCC `0.5732089267`; O0 vs Clang `0.5719991987`
- O1 vs GCC `0.5318501659`; O1 vs Clang `0.5306874200`

These are workload-local causal measurements, not a production speedup claim.

## Residual Gap

The no-budget residual remained:

- O0: `45.6107062400x` vs GCC and `58.5550652397x` vs Clang
- O1: `48.2340218738x` vs GCC and `61.9228801836x` vs Clang

Because the maximum relevant residual exceeded 5x, the declared H3 condition
was met.

## Conditional Frame Attribution

Independent I/J sessions used the same host, K, affinity, clock, warmup policy,
and fresh-process protocol. Both no-budget/no-frame variants were correct and
I/J reproducibility passed. However, removing frame accounting increased the
median runtime:

- O0 no-budget/no-frame: `14915428362.0 ns` vs no-budget `6451890176.0 ns`
- O1 no-budget/no-frame: `14378020467.5 ns` vs no-budget `6939367312.0 ns`

The resulting ratios (`0.4325648596` and `0.4826371841`) are not a positive
frame-cost attribution. `FRAME_SHARE_OF_RESIDUAL=NOT_VALID` and
`FRAME_ATTRIBUTION=NOT_CONFIRMED`. No H4/H5 implementation or additional
causal intervention was started.

## Pressure Map V10

`PRESSURE_MAP_V10.md` and `.json` promote only instruction-budget accounting to
`CONFIRMED_CAUSAL` for XSBench. Frame bookkeeping remains `WEAKENED`/not
confirmed by this intervention; initialization, bounds, indexing, stack,
register pressure, calls, helpers, and code size remain unmeasured or observed
only. No result is generalized to other workloads.

## Safe Budget Design Space

`SAFE_INSTRUCTION_BUDGET_DESIGN_SPACE.md` records future research options and
their required safety invariants. It does not select a winner and does not
authorize a production S3 change.

## Frontier Lab Update

H1 remains confirmed, H2 is confirmed causally for the declared XSBench
protocol, H3 is not confirmed, H4/H5 remain open, and H6 remains weakened.
The evidence score moves from 61/100 to an honest 77/100 (+16): correctness,
methodology, reliability, and portability gained direct native evidence, while
workload breadth and external validation did not.

## S3 PR #190 Relationship

PR #190 is still OPEN, DRAFT, and CONFLICTING. Its register/memory policy
families are a `POSSIBLE_MATCH` to the still-unmeasured residual code-structure
space, not a causal match and not an activation decision. No S3 policy was
enabled.

## Next Campaign

The next evidence target is
`S3_BENCHMARKS_2_2_3_MULTI_WORKLOAD_BUDGET_CAUSAL_VALIDATION`: replicate the
budget attribution across regular numerical, irregular, and control-flow
workloads before considering any S3 production change. `O21` safe budget design
review and `O22` checked-vs-benchmark mode study remain deferred research.

## Publication State

- `S3_SOURCE_CHANGED=NO`
- `S3_PRODUCTION_CHANGE_READY=NO`
- `QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE`
- PR #21 remains OPEN/DRAFT and is not merged.
- no tag, release, shutdown, reboot, or VM power action was performed.
