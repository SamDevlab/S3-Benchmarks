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
