# S3-Benchmarks 2.2.3 Final Report

## 1. Executive Summary

The current per-instruction budget mechanism produced a reproducible material
timing cost in three tested workload classes. RMSD, XSBench, and JSMN all
passed correctness and paired-session reproducibility gates, with O0/O1 budget
shares between 51.77733252% and 61.97746370%. The result is
`SYSTEMIC_STRONG` for the tested classes. It is diagnostic evidence, not a
production speed claim.

## 2. Starting Evidence

The campaign started from benchmark HEAD
`f2b4acb510b5f0e6a9e04287d3061194094d1417`, with PR #21 open and Draft. The
prior XSBench H2 result was already causal. PR #21's prior native blocker was
resolved before this campaign.

## 3. PR21 Reconciliation

PR #21's body was reconciled to state that the previous native blocker was
resolved, the same `s3-vm` was recovered, G/H and I/J were complete, H2 was
confirmed, H3 was not confirmed, and the evidence score was 77. PR #21
remains Draft, open, unmerged, and not ready for merge.

## 4. Research Question

Does current per-instruction budget accounting consume a material fraction of
native execution time across different S3 workload classes?

## 5. Workload Selection

The regular numerical workload is `scientific.rmsd.batch`, selected as the
existing direct FFI pilot. The tracked whole-program batch manifest remains
`NOT_SUPPORTED_YET`; that distinction is preserved. XSBench medium is the
irregular positive control. JSMN is the control-flow/parsing workload. PRK
NStream was retained as a blocked preselection attempt because no valid common
100 ms window was found before the frozen 10B instruction limit.

## 6. Reuse Audit

All selected workloads reuse the fail-closed
`remove_instruction_budget_instrumentation` rewriter. Budget sites are
derived from each generated artifact; XSBench's historical 521/520 counts are
not used as expectations for other workloads. Focused rewriter tests passed,
including unknown and partial-pattern rejection.

## 7. Environment

Native evidence came from the running Linux x86-64 `s3-vm` guest (`Ubuntuserve`):
kernel `7.0.0-31-generic`, Python `3.14.4`, GCC `15.2.0`, Clang `21.1.8`,
CPU affinity 0, `/usr/bin/perf` present, and `CLOCK_MONOTONIC_RAW`. Current
host fingerprint is
`9a3f305bd7d750ac2a6e86903c7487575d629e222bedd22dc70634519ec50b56`.
It differs from the prior fingerprint, so `HOST_CHANGED=YES`; no forced
equality is claimed. The host and VM remain running.

## 8. Artifact Matrix

Each selected workload used S3 O0 baseline, S3 O0 no-budget, S3 O1 baseline,
S3 O1 no-budget, GCC O2, and Clang O2. SHA-256 artifact records are retained
in the per-workload JSON results and raw evidence. No frame diagnostic was
run.

## 9. Static Budget-Site Analysis

Derived S3 budget sites were RMSD O0/O1 `113/113`, XSBench `521/520`, and JSMN
`2475/2427`. RMSD S3 O0 baseline/diagnostic static instruction counts were
3983/3531; JSMN counts were 50743/40843. These are static counts only. The
XSBench historical positive-control report does not provide a comparable
static instruction pair in this campaign result.

## 10. Correctness

All six variants passed the appropriate independent correctness gates for
RMSD and JSMN. XSBench retained its prior positive-control correctness and
native evidence. No failed or missing sample was converted to zero.

## 11. Calibration

RMSD used `K=2,000,000`; XSBench used its pinned positive-control `K=750,000`;
JSMN used `K=1,250,000`. Each selected workload met the fastest-control
threshold of at least 100 ms while passing all six correctness variants.
JSMN used the existing 35-byte `small_01_flat.json` fixture because the medium
fixture exceeds the frozen S3 input capacity 96; S3 was not changed.

## 12. Regular Numerical Results

RMSD O0 budget ratio/share were `2.5218501865x` and `60.34657390%`.
O1 ratio/share were `2.6300191866x` and `61.97746370%`. Both independent
sessions reproduced the result within the declared 25% gate.

## 13. XSBench Positive Control

XSBench O0 ratio/share were `2.3136205069x` and `56.77769984%`.
O1 ratio/share were `2.1125150010x` and `52.66305804%`. The expected
no-budget-faster direction remained true, and the prior full positive-control
evidence is retained.

## 14. Control-Flow Results

JSMN O0 ratio/share were `2.0737135713x` and `51.77733252%`. O1 ratio/share
were `2.1857747331x` and `54.24963127%`. Its timing scope is matched native
`PROCESS_E2E` parser execution, not pure kernel time. The status/token/checksum
oracle passed for all variants.

## 15. Reproducibility

RMSD and JSMN each have two independent official sessions, five external
warmups, 30 fresh-process repetitions per variant/session, balanced
interleaving, CPU-0 affinity, and raw samples. XSBench retains its prior
positive-control reproducibility PASS.

## 16. Per-Workload Causal Attribution

RMSD: `CONFIRMED_CAUSAL`. XSBench: `CONFIRMED_CAUSAL`. JSMN:
`CONFIRMED_CAUSAL`. Each isolated rewrite removed at least the predeclared
10% material share in both S3 optimization levels.

## 17. Cross-Workload Generalization

With XSBench as the positive control and both additional classes materially
causal, `BUDGET_PRESSURE_GENERALIZATION=SYSTEMIC_STRONG` and
`H7=CONFIRMED_GENERAL`. The claim is bounded to the three tested classes and
their declared protocols; it is not a universal percentage.

## 18. Dynamic Instruction Evidence

Dynamic logical-instruction counts are `NOT_AVAILABLE`. Consequently,
`BUDGET_COST_PER_LOGICAL_INSTRUCTION=NOT_MEASURED`. Static site counts are not
substituted for dynamic counts.

## 19. Residual Performance

Residual no-budget-to-GCC/Clang values are recorded per workload in
`BUDGET_GENERALIZATION_RESULT.json`. They are not pursued here; this campaign
does not begin H4 bounds/indexing or H5 register-policy attribution.

## 20. Pressure Map V11

`PRESSURE_MAP_V11.md` and `.json` record causal budget cells and preserve
unmeasured/observational states for frame, bounds, initialization, indexing,
stack, registers, calls, and runtime helpers.

## 21. Frontier Lab Update

The Frontier Lab now records H7 as `CONFIRMED_GENERAL`, O09 as complete, and
O21 safe budget design review as the next research action. No S3 production
source changed.

## 22. Evidence Score

Using the unchanged rubric, the score is 89/100: correctness 15/15,
methodology 15/15, workload coverage 15/15, performance evidence 14/15,
resource efficiency 6/10, portability 7/10, reliability 9/10, external
validation 3/5, provenance 5/5. This is `77 -> 89`, a delta of 12; it is not
a performance score.

## 23. Safe Budget Design Implications

Design research is warranted, but no design winner is selected. A future
bounded-mode prototype must preserve correctness, explicit safety semantics,
fail-closed validation, ABI behavior, and reproducibility across all three
classes. The constraints are recorded in
`research/frontier-lab/SAFE_INSTRUCTION_BUDGET_DESIGN_SPACE.md`.

## 24. PR190 Relationship

PR #190 remains read-only and was not activated. No experimental codegen or
register policy mechanism contaminated this causal budget campaign.

## 25. Limitations

RMSD evidence is from an existing direct FFI pilot rather than tracked
whole-program batch composition. JSMN uses PROCESS_E2E timing and a small
fixture constrained by the current S3 capacity. The host fingerprint changed
from the previous campaign. No cross-platform closure, dynamic instruction
count, frame attribution, bounds attribution, or register-pressure experiment
is claimed.

## 26. Next Campaign

`S3_BENCHMARKS_2_2_4_SAFE_BUDGET_ARCHITECTURE_EXPERIMENT_DESIGN` should ask
which safe lower-overhead bounded-mode prototypes preserve behavior and reduce
the confirmed cost across all three tested classes. It remains research-first;
no production patch is authorized by this report.

## 27. Publication State

This branch is intended for one Draft PR based on the 2.2.2 campaign branch.
`READY_FOR_MERGE=NO`, `MERGE=NO`, `TAG=NO`, `RELEASE=NO`. S3 remains read-only
at `e07d0b5464bf472b2ca18993f3e196a234ff0fc5`. No shutdown, reboot, or VM
power action is permitted.

## Status

The full benchmark-suite gate is run once at source freeze and is recorded in
the final machine-readable status below. Report-only updates after that gate
do not require a rerun.

## Final Machine-Readable Status

```text
CAMPAIGN=S3_BENCHMARKS_2_2_3_MULTI_WORKLOAD_BUDGET_CAUSAL_VALIDATION
PR21_BODY_RECONCILED=YES
BASE_HEAD=f2b4acb510b5f0e6a9e04287d3061194094d1417
SOURCE_FREEZE_HEAD=e3a056f95af9cf5fed27db34a4ece2e022c33717
BRANCH=research/benchmarks-2.2.3-budget-generalization
PR=22
PR_STATE=NOT_CREATED_YET
PR_DRAFT=NO
PR_MERGED=NO
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
S3_SOURCE_CHANGED=NO
VIRTUALBOX_ACTIVE=YES
S3_VM_STATE=RUNNING
HOST_FINGERPRINT=9a3f305bd7d750ac2a6e86903c7487575d629e222bedd22dc70634519ec50b56
HOST_CHANGED=YES
REGULAR_WORKLOAD=scientific.rmsd.batch
IRREGULAR_WORKLOAD=scientific.xsbench.compatible_lookup.medium
CONTROL_FLOW_WORKLOAD=realworld.jsmn
REGULAR_CORRECTNESS=PASS
IRREGULAR_CORRECTNESS=PASS
CONTROL_FLOW_CORRECTNESS=PASS
REGULAR_K=2000000
IRREGULAR_K=750000
CONTROL_FLOW_K=1250000
REGULAR_REPRODUCIBILITY=PASS
IRREGULAR_REPRODUCIBILITY=PASS
CONTROL_FLOW_REPRODUCIBILITY=PASS
REGULAR_BUDGET_SITES_O0=113
REGULAR_BUDGET_SITES_O1=113
IRREGULAR_BUDGET_SITES_O0=521
IRREGULAR_BUDGET_SITES_O1=520
CONTROL_FLOW_BUDGET_SITES_O0=2475
CONTROL_FLOW_BUDGET_SITES_O1=2427
REGULAR_BUDGET_COST_RATIO_O0=2.5218501865482588
REGULAR_BUDGET_COST_RATIO_O1=2.6300191865998777
REGULAR_BUDGET_SHARE_O0=0.6034657390299882
REGULAR_BUDGET_SHARE_O1=0.6197746369703057
IRREGULAR_BUDGET_COST_RATIO_O0=2.3136205069050235
IRREGULAR_BUDGET_COST_RATIO_O1=2.1125150009778446
IRREGULAR_BUDGET_SHARE_O0=0.5677769984249836
IRREGULAR_BUDGET_SHARE_O1=0.5266305803570066
CONTROL_FLOW_BUDGET_COST_RATIO_O0=2.073713571333792
CONTROL_FLOW_BUDGET_COST_RATIO_O1=2.1857747330514607
CONTROL_FLOW_BUDGET_SHARE_O0=0.517773325196107
CONTROL_FLOW_BUDGET_SHARE_O1=0.542496312690034
REGULAR_CAUSALITY=CONFIRMED_CAUSAL
IRREGULAR_CAUSALITY=CONFIRMED_CAUSAL
CONTROL_FLOW_CAUSALITY=CONFIRMED_CAUSAL
MATERIAL_SHARE_THRESHOLD=0.10
H1=CONFIRMED
H2=CONFIRMED_CAUSAL_XSBENCH
H3=NOT_CONFIRMED
H4=OPEN
H5=OPEN
H6=WEAKENED
H7=CONFIRMED_GENERAL
BUDGET_PRESSURE_GENERALIZATION=SYSTEMIC_STRONG
DYNAMIC_LOGICAL_INSTRUCTION_COUNTS=NOT_AVAILABLE
BUDGET_COST_PER_LOGICAL_INSTRUCTION=NOT_MEASURED
PRESSURE_MAP_V11=PASS
BUDGET_CAUSAL_MATRIX=PASS
EVIDENCE_SCORE_BEFORE=77
EVIDENCE_SCORE_AFTER=89
EVIDENCE_SCORE_DELTA=12
QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE
S3_BUDGET_DESIGN_RESEARCH_READY=YES
S3_PRODUCTION_CHANGE_READY=NO
PR190_RELATION=READ_ONLY_NOT_ACTIVATED
NEXT_CAMPAIGN=S3_BENCHMARKS_2_2_4_SAFE_BUDGET_ARCHITECTURE_EXPERIMENT_DESIGN
NEXT_RESEARCH_QUESTION=Which safe lower-overhead bounded-mode prototypes preserve correctness across all three tested classes?
FOCUSED_TESTS=28_PASSED
FULL_SUITE=69_PASSED_1_SKIPPED_0_FAILED_EXIT_0
FULL_SUITE_HEAD=e3a056f95af9cf5fed27db34a4ece2e022c33717
FULL_SUITE_START=2026-09-22T14:08:13.8997385-03:00
FULL_SUITE_END=2026-09-22T14:08:19.1252801-03:00
FULL_SUITE_TRANSCRIPT_SHA256=0BDE296F1734A0DB345FCBD1B12C250490653F464E8B7A2AA4DE83B0DA9A159C
COMPILEALL=PASS
EVIDENCE_LAB=PASS
DIFF_CHECK=PASS
SOURCE_CHANGED_AFTER_FINAL_GATES=NO
READY_FOR_MERGE=NO
MERGE=NO
TAG=NO
RELEASE=NO
AUTO_SHUTDOWN=FORBIDDEN
HOST_SHUTDOWN=NO
HOST_REBOOT=NO
VM_SHUTDOWN=NO
VM_REBOOT=NO
KEEP_HOST_RUNNING=YES
KEEP_VM_RUNNING=YES
```
