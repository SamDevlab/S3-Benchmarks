# S3 Exact Segment Budget Experiment

## Decision

```text
EXPERIMENTAL_SEGMENT_BUDGET_DECISION=STRONG_SUCCESS
BUDGET_LINE_CONTINUES=HARDENING_ONLY
NO_FURTHER_BUDGET_ARCHITECTURES=YES
S3_PRODUCTION_CHANGE_READY=NO
```

P2 passed the S3 E0/correctness gates and recovered at least 92.1% of the
measured removable budget excess in every workload/optimization cell. All six
cells exceed the predeclared 50% strong-recovery threshold. This qualifies the
exact-segment experiment for hardening only; it does not authorize enabling it
by default or promoting it to production.

## Provenance

| item | identity |
|---|---|
| S3 control | `e07d0b5464bf472b2ca18993f3e196a234ff0fc5` |
| S3 tested source freeze | `1a76e341098b54a639fec22eecea362cc243c46f` |
| S3 publication/report head | `8f6b8afdf780cfc413a722d1885bf3107803f71a` (documentation-only after tests) |
| benchmark base | `8fc0aba50ca48d3f7171bdf49395df3cd880626a` |
| benchmark source freeze | `84347c9c400839c739241728f8e90f4a1273c33f` |
| S3 PR | #310, OPEN, Draft, unmerged |
| prior benchmark PR | #23 remains OPEN, Draft, unmerged |

The original dirty Windows S3 checkout was not used. The experiment and
control were clean isolated Linux worktrees at their exact pinned SHAs.

## Gate Results

- S3 focused exact-budget/native-safety group: exit 0 on Linux x86-64 with
  `S3_NATIVE_REQUIRED=1`.
- S3 `compileall`: PASS; `git diff --check`: PASS.
- Exactly one S3 full suite at the tested source SHA: 4,373 passed, 1 skipped,
  0 failed, exit 0. Transcript SHA-256:
  `1b92f9a4009b7e8f50b91e5ab47fdba1a699acfc6ecdbb1a9af3a27a7f455d4e`.
- Benchmark focused validation tests: 14 passed on Windows and 14 passed on
  Linux. Benchmark `compileall` and `git diff --check`: PASS.
- Exactly one benchmark full suite at its source freeze: 97 passed, 1 skipped,
  0 failed, exit 0, Linux x86-64 / Python 3.14.4.
- Candidate and control default-mode P0 Assembly matched byte-for-byte for all
  six measured cells. P0 and P2 reused the same compiled `AssemblyProgram`;
  the only configuration difference was `instruction_budget_mode`.
- Correctness passed for P0, P1, P2 and PNEG across RMSD, XSBench, and JSMN at
  O0/O1. All timed samples passed; all six cells passed independent-session
  reproducibility.

## Protocol

The fixed work was RMSD K=2,000,000; XSBench K=750,000; JSMN K=1,250,000.
Each of the six workload/optimization cells used five external warmups, zero
inline warmups, two independent fresh-process sessions, 30 balanced
repetitions per session, CPU affinity 0, and `CLOCK_MONOTONIC_RAW`. The reported
`T` is the arithmetic mean of the two session medians. The predeclared maximum
relative session-median delta was 25%; every observed cell/variant was below
3.1%.

## Causal Results

Times below are seconds per fixed-K invocation. Recovery uses the declared
no-budget PNEG diagnostic as a lower bound:

```text
P2 recovered excess = (T(P0) - T(P2)) / (T(P0) - T(PNEG))
P2 incremental over P1 = (T(P1) - T(P2)) / (T(P0) - T(PNEG))
```

Values above 100% mean P2 measured faster than PNEG in that cell; they are not
clamped. PNEG is unsafe/no-budget and is never a candidate.

| workload | opt | P0 | P1 | P2 | PNEG | P2 excess recovered | incremental over P1 | P2/PNEG |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| RMSD | O0 | 13.3973 | 13.5905 | 5.0085 | 5.3747 | 104.56% | 106.97% | 0.9319 |
| RMSD | O1 | 13.4296 | 13.5822 | 5.1351 | 5.3637 | 102.84% | 104.73% | 0.9574 |
| XSBench | O0 | 14.3397 | 14.6145 | 6.4396 | 6.1951 | 97.00% | 100.37% | 1.0395 |
| XSBench | O1 | 13.8169 | 14.0201 | 6.7578 | 6.6120 | 97.98% | 100.80% | 1.0221 |
| JSMN | O0 | 24.3932 | 23.6617 | 12.0788 | 11.0285 | 92.14% | 86.67% | 1.0952 |
| JSMN | O1 | 23.8875 | 23.4578 | 11.7446 | 10.8874 | 93.41% | 90.10% | 1.0787 |

The effect is cross-workload and strong. P2 materially outperformed P1 in all
six cells. Relative to the unsafe PNEG lower bound, P2 was faster in RMSD,
about 2.2-3.9% slower in XSBench, and about 7.9-9.5% slower in JSMN.

## Code Size and Segment Plan

Exact slow-path duplication increased P2 `.text` size by 39.17% for RMSD,
53.35-53.57% for XSBench, and 58.27-58.54% for JSMN. Static native
instruction counts rose from 3,983 to 5,304 (RMSD), 12,812 to 19,629/19,633
(XSBench), and 50,743/50,063 to 80,984/79,991 (JSMN O0/O1).

The planner is deterministic, Assembly-structure based, block-local, and emits
no heuristic slices of x86 text. JSMN has 298 fast segments among 386 O0 / 356
O1 segments, with median logical weight 5. XSBench has 27 fast segments among
35 / 34, and RMSD has 17 among 22. The exact slow sequence is present beside
each eligible fast sequence; this explains the measured static code growth.
Whether that duplication is the dominant cause of the remaining runtime gap
against PNEG is not independently isolated and is not claimed as a
microarchitectural result.

## Residual Triage

The directly observed remaining cost is P2's per-segment guard/precharge plus
the code-size cost of the duplicated exact slow path. This is the only
residual with a direct structural match in the candidate and its generated
artifacts. The data does not establish a new dominant bounds, register, stack,
runtime-helper, or instruction-selection cause.

PR #190 was inspected read-only. Its V2.1 attribution reported compact-EA
instruction/move reductions without load/store or stack reductions; scalar
replacement removed one load and one store; region-aware spill,
rematerialization, and live-range splitting were neutral in that study. Those
mechanisms do not directly explain P2's per-segment fast/slow duplication.
No PR #190 mechanism was enabled or changed.

## Selected Next Step

Proceed only to `S3_EXPERIMENT_SEGMENT_BUDGET_HARDENING`: investigate whether
the existing P2 exact slow path can be outlined/shared to reduce the observed
`.text` growth while preserving E0, deterministic segment identity, call
ordering, diagnostics, and default P0 byte identity. This report does not
implement that work, add P3/P4/P5, or authorize a production switch.

## Publication Boundaries

```text
BENCHMARK_READY_FOR_MERGE=NO
S3_READY_FOR_MERGE=NO
MERGE=NO
TAG=NO
RELEASE=NO
QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE
AUTO_SHUTDOWN=FORBIDDEN
KEEP_HOST_RUNNING=YES
KEEP_VM_RUNNING=YES
KEEP_VIRTUALBOX_RUNNING=YES
```

Raw evidence is in `raw/segment-budget-20260923-134844-191043748/` (121 files,
81,496,216 bytes), with the SHA-256 list at
`raw/segment-budget-20260923-134844-191043748.sha256`. The result JSON beside
this report records the full per-session and per-variant evidence.
