# Stage04 expression qualification

This document is the S3-Benchmarks-side companion to the live Codex control-plane Stage 04.

It is read-only laboratory infrastructure. It does not mutate or authorize mutation of `SamDevlab/S3`.

## Live route

The live control plane is currently expected to be at control revision 4 with:

```text
active_stage=04_EXPRESSIONS_S1_S2
canonical_stage1_mutation_authorized=false
self_emit_authorized=false
stage2_authorized=false
stage3_authorized=false
t4_authorized=false
```

The laboratory does not treat this file as control authority; the authoritative live control state remains the S3 control branch.

## Why Stage04 is tracked separately

Stage04 is the first slice where the candidate moves from binding metadata into actual semantic expression dataflow:

```text
source expression
  -> logical values
  -> instruction results
  -> ordered operand edges
  -> exactly-one result definition
```

A parser becoming syntactically valid is necessary but not sufficient. Likewise, one successful literal fixture is not S1/S2 closure.

## Machine-readable checkpoint

Use:

- `stage04-checkpoint-template.json`
- `stage04-expression-gate-contract.json`
- `tools/evaluate_stage04_expression_checkpoint.py`

The normalized checkpoint records candidate identity plus these subgates:

```text
stage03_evidence_backfill
expr_parser_syntax
integer_literal_lowering
negative_wide_literal_lowering
identifier_lookup
lexical_shadowing
unary_lowering
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

The gate remains BLOCKED if any required field is not explicit PASS.

The following invariants are also mandatory during Stage04:

```text
canonical_source_mutated=false
self_emit_authorized=false
stage2_authorized=false
z_mask < 31
```

`Z 31` during Stage04 is an error because S3/S4/S5 are not yet closed.

## Incremental comparison

`tools/compare_stage04_expression_checkpoints.py` compares two normalized Stage04 checkpoints.

It deliberately distinguishes:

- `IMPROVEMENT`: a previously non-PASS gate becomes PASS;
- `REGRESSION`: a previously PASS gate is re-observed as non-PASS;
- `NOT_REOBSERVED`: a previous PASS gate was not rerun in the new candidate.

This distinction is useful while the parser is being repaired incrementally. Discovering the next parser error after fixing the previous one is not automatically a semantic regression.

## Pinned fixtures

The deterministic bootstrap corpus currently includes focused Stage04 inputs for:

- `wide_literal_positive`
- `wide_literal_negative`
- `relational_precedence_v06`
- `mutable_reassignment_example`
- `local_identity`

`relational_precedence_v06` is copied from the V0.6 source used by `SamDevlab/S3/tests/test_s3_relational_parser.py`.

`mutable_reassignment_example` is copied from `SamDevlab/S3/examples/mutable_value.s3`.

These source inputs are planning/corpus evidence only. They become compiler evidence only after execution against an exact candidate with native provenance and strict S3 semantic conformance.

## Current focused-fixture gaps

`stage04-capability-matrix.json` intentionally keeps gaps visible.

At the current planning state:

- precedence: pinned;
- comparison: pinned;
- reassignment: pinned;
- unary negation: partially pinned through the negative-wide-literal case;
- generic unary coverage: still incomplete;
- lexical shadowing: repository semantics prove shadowing exists, but a minimal Stage04-only fixture is not yet pinned.

Do not convert these planning gaps into compiler failures. Do not convert them into PASS either.

## Fixture coverage audit

Use `tools/audit_stage04_fixture_coverage.py`.

The expected current state is `INCOMPLETE_FIXTURE_COVERAGE` while generic unary and focused lexical-shadowing coverage remain incomplete.

This is not a Stage04 implementation failure; it is a test-corpus completeness signal.

## Stage04 retrospective campaign

The broader `s3ir2-v2-stage-map.json` now requires these Stage04 cases:

```text
wide_literal_positive
wide_literal_negative
relational_precedence_v06
mutable_reassignment_example
local_identity
```

A later fully capable candidate must rerun them with:

```text
structural_status=PASS
native_provenance_status=PASS
semantic_conformance_status=PASS
```

Stage04 incremental progress and final retrospective evidence are deliberately separate concepts.

## Handoff to Stage05

The Benchmark evaluator may report:

```text
STAGE04_GATE=PASS
NEXT_STAGE_CANDIDATE=05_CALLS_ARRAYS_S3
```

This is advisory laboratory evidence only. Actual transition/authorization still belongs to the live S3 control plane.
