# Instruction-Budget Causal Result

## Decision

`INSTRUCTION_BUDGET_CAUSALITY=CONFIRMED_CAUSAL`

The exact benchmark-side rewrite removed only complete instruction-budget
accounting blocks from the pinned O0/O1 assembly. Native diagnostic correctness
passed for TINY, SMALL, and MEDIUM. Independent G/H sessions each completed 30
fresh-process official samples for all six variants, and every G/H median delta
was within the declared 25% criterion.

## Controlled protocol

- workload: `scientific.xsbench.compatible_lookup.medium`
- K: `750000`
- inline warmups: `0`
- external warmups: `5` per variant
- official repetitions: `30` per variant per session
- fresh process: yes
- balanced interleaving: yes
- CPU affinity: `0`
- clock: `CLOCK_MONOTONIC_RAW`
- sessions: G and H

## Result

| level | baseline median ns | diagnostic median ns | ratio | removed baseline share |
|---|---:|---:|---:|---:|
| O0 | 14325439969.5 | 6191784662.5 | 2.3136205069 | 0.5677769984 |
| O1 | 13832552419.5 | 6547907311.0 | 2.1125150010 | 0.5266305804 |

The no-budget residual remained 45.6107x/48.2340x against GCC and
58.5551x/61.9229x against Clang for O0/O1 respectively. The experiment proves
the material cost of this safety instrumentation under this workload and host;
it does not justify removing the protection or claiming production speedup.

## Gates

| gate | result |
|---|---|
| pinned assembly reproduction | PASS |
| instruction-budget rewriter audit | PASS, O0 521 and O1 520 sites |
| unexpected mutations | PASS, 0 |
| diagnostic native build | PASS |
| diagnostic native correctness | PASS, 18/18 base observations |
| Run G | PASS |
| Run H | PASS |
| G/H reproducibility | PASS, maximum delta 0.0537918232 |
| frame conditional gate | executed; attribution NOT_CONFIRMED |

The frame experiment is recorded separately and is not part of the H2 causal
number. Removing frame accounting made both diagnostic variants slower in I/J,
so `FRAME_SHARE_OF_RESIDUAL=NOT_VALID`.

## Scope

This is evidence for one XSBench workload, one pinned S3 source, one Linux
x86-64 guest fingerprint, and the declared protocol. Other workloads remain
`NOT_MEASURED`; `QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE` and
`S3_PRODUCTION_CHANGE_READY=NO`.
