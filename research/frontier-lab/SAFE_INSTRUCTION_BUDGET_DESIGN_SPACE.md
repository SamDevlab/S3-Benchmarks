# Safe Instruction-Budget Design Space

This is a research constraint document, not a selected implementation.

## Observed cross-workload requirements

- The current budget instrumentation produced a reproducible material timing
  effect in three distinct workload classes: regular numerical RMSD, the
  irregular XSBench positive control, and control-flow/parsing JSMN.
- The experiment used the same fail-closed assembly rewriter and preserved
  correctness before timing for every selected workload.
- A design must preserve an explicit bounded-execution contract while avoiding
  silent changes to the observable result, ABI, or workload semantics.
- Any candidate must remain inspectable and fail closed when its structural
  rewrite does not match the complete expected instrumentation pattern.

## New constraints

- The evidence establishes research readiness, not production readiness.
- The tracked RMSD batch manifest still lacks whole-program composition; the
  regular result is from the existing direct FFI pilot and must not be
  presented as batch compiler closure.
- JSMN timing is matched native `PROCESS_E2E`, not pure kernel time.
- Dynamic logical-instruction counts are unavailable. Static site counts are
  descriptive and cannot be used to derive dynamic cost.
- Frame, bounds, initialization, register-pressure, and helper-cost changes
  remain unmeasured in this lane.

## Decision status

No budget design winner is selected. The next authorized research question is
whether bounded-mode prototypes can lower overhead across all three classes
without weakening safety, correctness, or reproducibility.
# 2.2.4 Safe architecture prototypes

The 2.2.4 campaign tests a single bounded replacement candidate, P1
`GLOBAL_COUNTDOWN_EXACT`, against P0's current global count-up oracle. P1 is
implemented only as a fail-closed transformation of generated x86-64 assembly:
the original failure labels and logical site count are preserved, while the
counter is initialized as a uint64 remaining budget and decremented with
`sub/jb`. PNEG remains a no-budget lower bound and is never a safe candidate.

P2 `CALL_AWARE_SEGMENT_PRECHARGE_EXACT` is intentionally not implemented until
logical S3 Assembly boundaries can be mapped to native segments without
heuristics. Its absence is an exactness proof blocker, not permission to use a
conservative or approximate timing candidate.

The campaign records native boundary equivalence before real workload timing
for RMSD, XSBench, and JSMN at the existing K values and both O0/O1 levels.
Final classifications and recovery values are written only after the bounded
protocol completes.

## 2.2.4 final decision

P1 is **safe but not selected for promotion**. The 21-case native boundary
differential and the 12-case structural corpus both passed E0. All three
workloads also passed correctness in P0, PNEG, P1, GCC, and Clang variants at
O0/O1. The timing gate did not pass: P1 recovered 8.37% of the removable
RMSD-O0 excess, -0.49% at RMSD-O1, -0.62%/-1.01% at XSBench O0/O1, and
4.40%/2.33% at JSMN O0/O1. These results establish a safe exact prototype,
not a material lower-overhead architecture.

The next decision must use a new causal prototype and the same E0 contract;
P1 must not be activated as a production backend. P2 remains blocked because
no explicit logical-Assembly-to-native segment map was proven. The no-budget
PNEG build remains only a lower-bound diagnostic.
