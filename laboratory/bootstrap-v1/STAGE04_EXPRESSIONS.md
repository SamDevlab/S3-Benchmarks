# Stage04 expression qualification

This document is the S3-Benchmarks-side companion to the live Codex control-plane Stage 04.

It is read-only laboratory infrastructure. It does not mutate or authorize mutation of `SamDevlab/S3`.

## Live route

The authoritative live state remains the S3 control branch. The current observed route is control revision 5:

```text
active_stage=04_EXPRESSIONS_S1_S2
canonical_stage1_mutation_authorized=false
self_emit_authorized=false
stage2_authorized=false
stage3_authorized=false
t4_authorized=false
```

The current Codex work is legitimate parser/lowering repair. A syntax/indentation error or duplicated `match` branch is classified as:

```text
EXPR_PARSER_SYNTAX=BLOCKED
```

until repaired. It is not sufficient evidence to call S1 or S2 semantically FAIL because their focused native conformance may not have run yet.

## Current operator scope

The normative S3 0.6 precedence ladder is:

```text
postfix/call/index/member
unary: - ~
additive: + -
tritwise min: &
tritwise max: |
ternary compare: <=>
relational: == != < <= > >=
```

Current S3 AST/IR does not define arithmetic multiplication, division, or remainder. Stage04 must not add them speculatively.

Subtraction has an additional architectural rule: it lowers as `INVERT` followed by `ADD`; there is no native subtraction opcode.

A repository-backed precedence source is:

```s3
mut res: trit = 1 <=> 2 < 3
```

with expected association `(1 <=> 2) < 3`.

The Stage04 checkpoint must report multiply/divide/remainder as `FAIL_CLOSED` or `NOT_APPLICABLE`, never as a newly implemented PASS capability.

## Gate model

Stage04 is where the candidate moves from binding metadata into semantic expression dataflow:

```text
source expression
  -> logical values
  -> instruction results
  -> ordered operand edges
  -> exactly-one result definition
```

Use:

- `stage04-checkpoint-template.json`
- `stage04-expression-gate-contract.json`
- `tools/evaluate_stage04_expression_checkpoint.py`

Technical Stage04 fields must become PASS:

```text
expr_parser_syntax
integer_literal_lowering
negative_wide_literal_lowering
identifier_lookup
lexical_shadowing
unary_negate
unary_invert
supported_binary_operators
binary_precedence
comparison_lowering
local_initialization
assignment_reassignment
instruction_result_ids
ordered_operand_edges
single_result_definition
candidate_stage0_check
focused_native_v2_conformance
s1_typed_values
s2_def_use
```

`stage03_evidence_backfill` is tracked separately as historical evidence debt. Valid honest values are:

```text
PASS
PARTIAL
NOT_RECORDED
NOT_REOBSERVED
```

A non-PASS backfill value is reported in `nonblocking_evidence_debt`; it does not by itself invalidate a technically complete Stage04 candidate. This matches the live control-plane rule that missing historical evidence must not be fabricated.

Mandatory Stage04 invariants remain:

```text
canonical_source_mutated=false
self_emit_authorized=false
stage2_authorized=false
z_mask < 31
```

`Z 31` during Stage04 is invalid because S3/S4/S5 are incomplete.

## Incremental comparison

`tools/compare_stage04_expression_checkpoints.py` distinguishes:

- `IMPROVEMENT`: a previously non-PASS gate becomes PASS;
- `REGRESSION`: a previously PASS gate is re-observed as non-PASS;
- `NOT_REOBSERVED`: a previous PASS gate was simply not rerun.

Discovering the next syntax/parser error after repairing the previous one is not automatically a semantic regression.

## Pinned Stage04 fixtures

The deterministic corpus now contains focused inputs for:

```text
wide_literal_positive
wide_literal_negative
unary_negate_tryte
unary_invert_tryte
subtraction_lowering
tritwise_and
tritwise_or
relational_equal
relational_precedence_v06
mixed_expression_precedence
mutable_reassignment_example
local_identity
```

These fixtures cover the supported operator families without inventing `*`, `/`, or `%` arithmetic.

Important source provenance:

- operator set and precedence: normative `SamDevlab/S3/spec/language.md`;
- relational precedence: S3 V0.6 relational parser tests;
- mutable reassignment: S3 mutable-value example;
- shadowing semantics: S3 reference semantic tests prove distinct inner/outer symbol origins.

`lexical_shadowing` remains an explicit focused-fixture planning gap because the repository-backed test also exercises references. Do not silently simplify that test and call it pinned without independent qualification.

## Fixture coverage audit

`tools/audit_stage04_fixture_coverage.py` treats:

- `PINNED` as an applicable capability with deterministic corpus input;
- `FIXTURE_NOT_YET_PINNED` as an explicit planning gap;
- `NOT_APPLICABLE_BY_LANGUAGE_CONTRACT` as valid and excluded from fixture requirements.

Therefore unsupported multiply/divide/remainder no longer appears as an invalid capability merely because it intentionally has no fixture.

`tools/check_s3ir2_stage_map_contract.py` additionally rejects:

- stage-map references to nonexistent corpus cases;
- duplicate required cases;
- Stage04 fixtures containing spaced arithmetic `*`, `/`, or `%` tokens.

These are static planning/contract checks, not compiler PASS evidence.

## Retrospective campaign

A later fully capable candidate must rerun all mapped Stage04 cases with:

```text
structural_status=PASS
native_provenance_status=PASS
semantic_conformance_status=PASS
```

Final S5/campaign qualification additionally requires independently proven repeated native streams with deterministic bytes.

Stage04 incremental implementation status and final retrospective evidence remain deliberately separate concepts.

## Handoff to Stage05

The Benchmark evaluator may report:

```text
STAGE04_GATE=PASS
NEXT_STAGE_CANDIDATE=05_CALLS_ARRAYS_S3
```

This is advisory laboratory evidence only. Actual transition and authorization still belong to the live S3 control plane.
