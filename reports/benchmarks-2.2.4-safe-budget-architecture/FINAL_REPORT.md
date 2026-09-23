# S3 Benchmarks 2.2.4 — Safe Instruction-Budget Architecture

## 1. Decision

P1 is an exact, safety-qualified benchmark prototype, but it is not selected
for production promotion because the cross-workload material-performance gate
did not pass. No S3 compiler or runtime change was made.

## 2. Campaign lineage

Base branch: `research/benchmarks-2.2.3-budget-generalization`.
Base HEAD: `e8463adc7284e2120dd1c205f92e6a901b813891`.
Campaign branch: `research/benchmarks-2.2.4-safe-budget-architecture`.
Final benchmark HEAD: `12e5e1b23c2b454aab975363575616ffe24ef39a`.

## 3. S3 source pin

The S3 checkout used for all artifacts was pinned to
`e07d0b5464bf472b2ca18993f3e196a234ff0fc5`. `S3_SOURCE_CHANGED=NO`.

## 4. Host

The native evidence was collected on Linux x86-64, AMD Ryzen 5 3400G,
kernel `7.0.0-31-generic`, CPU affinity 0. The current host fingerprint is
`9a3f305bd7d750ac2a6e86903c7487575d629e222bedd22dc70634519ec50b56`.

## 5. P0 oracle

P0 is the current global count-up sequence: check before each logical S3
Assembly instruction, fail when `count >= max`, increment before execution,
and preserve the global process-persistent state for a loaded artifact.

## 6. PNEG lower bound

PNEG removes the budget checks only for diagnosis. It has safety tier NONE and
is not a candidate implementation.

## 7. P1 definition

P1 is `GLOBAL_COUNTDOWN_EXACT`. It replaces each complete count-up site with
`sub qword ptr [rip + __s3_instruction_remaining], 1` followed by `jb` to the
original failure label. The remaining counter is initialized as a uint64 in
`.data`.

## 8. P2 definition

P2 is `CALL_AWARE_SEGMENT_PRECHARGE_EXACT`. It was not implemented because no
explicit logical-Assembly-to-native segment map was proven. Heuristic text
slicing is prohibited.

## 9. Safety contract

E0 requires identical success, observable effects, failure boundary, failure
category, function, block, opcode, source context, repeated-call lifetime,
and standalone behavior. Only E0 is eligible for promotion.

## 10. Static transform

The transform is fail-closed. It requires every expected site, one consistent
limit, one original storage symbol, and a recognized wide or immediate x86-64
layout. Partial, unknown, inconsistent, or residual count-up layouts fail.

## 11. Native boundary differential

P1 matched P0 in 21/21 native boundary cases across limits 0, 1, 2, 3,
`0x7fffffff`, `0x80000000`, and `10000000000`, with one, two, and three
repeated calls. The output, return code, diagnostic boundary, and failure
context matched.

## 12. Structural safety corpus

The 12-case corpus passed. It covered straight-line code, branches, loops,
nested S3 calls, multiple calls, early return, fused logical weight two,
side effects on both sides of a boundary, repeated FFI calls, exact success,
and one-before-completion.

## 13. Correctness matrix

RMSD, XSBench, and JSMN all passed correctness for P0, PNEG, P1, GCC, and
Clang variants at O0/O1. Each workload used the declared K value and each
variant returned the expected observable result.

## 14. RMSD workload

K=`2,000,000`. P1 recovered 8.37% of the removable O0 budget excess and
`-0.49%` at O1. P1 remained about 2.52x above the no-budget lower bound.

## 15. XSBench workload

K=`750,000`. P1 recovered `-0.62%` at O0 and `-1.01%` at O1. P1 remained
about 2.31x/2.09x above the no-budget lower bound at O0/O1.

## 16. JSMN workload

K=`1,250,000`. P1 recovered 4.40% at O0 and 2.33% at O1. P1 remained about
2.15x/2.20x above the no-budget lower bound at O0/O1.

## 17. Timing protocol

The final characterization used five external warmups, 30 repetitions, two
sessions, a fresh process per sample, balanced interleaving, CPU 0, and
`CLOCK_MONOTONIC_RAW`.

## 18. Reproducibility

All 3 workloads, 8 variants, and both sessions completed with 30 PASS samples
per variant. Cross-session median deltas are preserved in
`SAFE_BUDGET_ARCHITECTURE_RESULT.json`; RMSD varied by roughly 5.2–8.9%,
XSBench by 3.5–7.9%, and JSMN by less than 0.6%. No unprovided numerical
threshold is claimed as a pass criterion.

## 19. Performance decision

The exact safety gate passed, but the cross-workload material recovery gate
failed. The evidence does not justify selecting P1 as a lower-overhead
architecture.

## 20. Candidate classification

`SAFE_EXACT_BUT_NOT_PERFORMANCE_MATERIAL`.

## 21. P1 promotion status

P1 is not selected and is not implementation-ready for production. It remains
a reusable safety-qualified research transformation.

## 22. P2 status

P2 is blocked by the absence of an explicit logical-to-native segment map. No
approximate or conservative substitute was introduced.

## 23. Counter visibility

The pinned S3 audit found no public counter ABI and no other runtime readers;
the failure handler is terminal. These facts support the P1 safety argument
but do not establish performance materiality.

## 24. S3 immutability

No S3 production/compiler file was changed. All transformations are benchmark
side and diagnostic-only.

## 25. Artifact provenance

The final raw directory is
`raw/safe-budget-20260922-225407-074374170`. The final characterization
transcript is `raw/campaign-20260922-225406-retry2.txt`.

## 26. Failed harness attempts

The earlier transcripts are retained. The first failed in JSMN because of an
old artifact-field assumption; the second exposed the reciprocal artifact
contract. Both failures were harness-only and occurred before a final result.

## 27. Harness correction

The runner now accepts either artifact contract explicitly and fails closed on
an unsupported object. The correction was committed as
`12e5e1b23c2b454aab975363575616ffe24ef39a`.

## 28. Full suite

The selected full-suite gate ran once on the frozen benchmark HEAD in the
Windows checkout: `83 passed, 1 skipped, 0 failed`, exit 0. Transcript:
`raw/full-suite-local-20260923-035234.txt`.

## 29. Guest suite note

The guest invocation was preserved as an environment result: its system
Python had no `pytest`, so it exited 1 before collection. No dependency was
installed and no result was misrepresented as a Linux suite pass.

## 30. Additional validation

The focused benchmark tests passed `31 passed`. Python compilation of the
changed runner and safe-budget transformer passed. `git diff --check` passed.

## 31. Pressure map and hypotheses

`PRESSURE_MAP_V12.md` and `.json` record the remaining representation,
helper/call, frame/initialization, register-pressure, and instruction-selection
pressures. H8 is classified `CONFIRMED_SAFE_NOT_MATERIAL`; H9 remains
`BLOCKED_BY_EXACTNESS_PROOF`.

## 32. Release boundary

This campaign is research-only. No production change, merge, tag, release, or
shutdown is authorized. The only next step is a separately reviewed causal
prototype that preserves E0 and supplies evidence beyond P1.
