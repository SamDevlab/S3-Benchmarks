# Instruction-Budget Safety Contract

## Scope

This contract governs benchmark-side prototypes for S3's pinned x86-64
instruction-budget implementation. The S3 checkout is read-only. A prototype
is a diagnostic artifact and is not a compiler or runtime change.

## Current oracle (P0)

The oracle is the current global count-up sequence emitted before every
logical S3 Assembly instruction:

```text
if instruction_count >= max_instructions: fail
instruction_count += 1
execute one logical instruction
```

The state is process-persistent for a loaded native artifact. Fused native
lowering does not merge logical accounting: a fused `TCMP`/`TBR3` pair has
logical weight two.

## Safety tiers

### E0: exact current semantics

For every valid program and budget, baseline success and candidate success are
identical. Successful observable results and side effects are identical. On
exhaustion, the candidate reaches the same logical boundary, failure category,
function, block, opcode, and available source context, and executes no later
logical instruction. Repeated calls through the same loaded shared object and
standalone execution retain the same global finite-budget lifetime.

Only E0 is eligible for timing selection or an isolated S3 implementation
experiment.

### E1: conservative bounded semantics

The candidate may fail earlier but never executes more logical instructions
than the budget permits. It is labeled `CONSERVATIVE_NOT_EXACT` and is not a
drop-in replacement.

### E2: bounded lag

The candidate may execute budget plus a positive delta. It is
`NOT_SAFE_EQUIVALENT` and is not eligible for performance promotion.

## P1 proof obligations

`GLOBAL_COUNTDOWN_EXACT` starts each artifact with `remaining = B` and emits
the unsigned sequence:

```asm
sub qword ptr [rip + __s3_instruction_remaining], 1
jb  original_failure_site
```

For `B=0`, the subtraction underflows and sets carry, so `jb` fails before
execution. For `B=1`, it produces zero without carry and executes exactly one
instruction. The domain is `0..2^64-1`; the maximum value also decrements
without carry. The transformed storage is initialized once in `.data`, which
preserves the loaded-artifact lifetime of the current global counter.

The rewriter is fail-closed: it requires every budget site to be complete,
requires one consistent limit, replaces exactly one storage declaration, and
rejects residual counter references or unknown layouts. It records input and
output hashes, expected/transformed site counts, and unexpected mutations.

## P2 policy

`CALL_AWARE_SEGMENT_PRECHARGE_EXACT` remains design-only unless an explicit
logical-Assembly segment map proves boundaries around S3 calls, reentrant
execution, unknown transfers, and fused logical weights. Heuristic native-text
slicing is prohibited. Until that proof exists P2 is
`BLOCKED_BY_EXACTNESS_PROOF`, not a failed exact candidate.

## Required evidence

The differential corpus must cover straight-line, conditional, loop, nested
and repeated S3 calls, early return, fused logical instructions, side effects
around the boundary, exact-budget success, and one-before-completion failure.
Native boundary checks must include small limits, the signed-immediate
boundary, the campaign limit, repeated FFI calls, and standalone execution.
Correctness precedes timing; timing is eligible only after `SAFETY_TIER=E0`
and `SAFETY_EQUIVALENCE=PASS`.
