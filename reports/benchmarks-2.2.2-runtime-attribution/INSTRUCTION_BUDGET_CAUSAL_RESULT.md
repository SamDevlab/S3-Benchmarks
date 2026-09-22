# Instruction-Budget Causal Result

## Decision

`INSTRUCTION_BUDGET_CAUSALITY=UNDER_TEST`

The controlled assembly transformation is structurally valid, but the
causal experiment is not complete. The Linux build, TINY/SMALL/MEDIUM native
correctness, and independent Run G/Run H timing sessions could not run because
the configured Linux guest was unreachable. Existing E/F timings are
historical evidence and are not reused as causal measurements.

## Hypothesis

`NATIVE_INSTRUCTION_BUDGET_INSTRUMENTATION` is a primary causal candidate for
the observed XSBench runtime pressure. It is not yet a proven cause.

## Controlled transformation

Input: the exact pinned O0/O1 S3 assembly. Output: the same text with only
complete instruction-budget accounting blocks removed. Frame checks, bounds,
initialization, calls, ABI, arithmetic, control flow, and memory layout are
untouched. The transformation is deterministic, pattern-specific, auditable,
and fail-closed.

## Gates

| gate | result |
|---|---|
| pinned assembly reproduction | PASS |
| rewriter focused tests | PASS, 7 passed |
| static transformation audit | PASS, O0 521 sites and O1 520 sites removed |
| unexpected assembly mutations | PASS, 0 |
| diagnostic native build | NOT_RUN, Linux guest unavailable |
| diagnostic correctness | NOT_RUN |
| Run G | NOT_RUN |
| Run H | NOT_RUN |
| G/H reproducibility | NOT_RUN |

## Why no causal number is reported

The required protocol compares fresh G/H sessions for baseline and diagnostic
variants at `K=750000`, with five external warmups, zero inline warmups, 30
fresh-process repetitions, CPU 0 affinity, `CLOCK_MONOTONIC_RAW`, and balanced
interleaving. No part of that protocol was substituted with old E/F samples.

`INSTRUCTION_BUDGET_COST_RATIO_O0=NOT_AVAILABLE`
`INSTRUCTION_BUDGET_COST_RATIO_O1=NOT_AVAILABLE`

The residual gap and excess-time attribution are consequently
`NOT_INTERPRETABLE`. Frame attribution is deferred until the first causal
experiment has a valid diagnostic timing result.

## Safety interpretation

Even if a future G/H run shows a large timing change, it will establish the
cost of this safety envelope under this workload and protocol. It will not
justify a production speed claim or removal of bounded-execution protection.
