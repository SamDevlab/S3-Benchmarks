# Stage06 control-flow qualification (prepared, inactive)

This is S3-Benchmarks-side planning for the live S3 control-plane stage `06_CONTROL_FLOW_S4`.

It does not activate Stage06 and does not mutate or authorize mutation of `SamDevlab/S3`.

## Required semantics

The frozen control-plane contract requires explicit semantic terminators:

- `RETURN`: one return value ID where applicable and no branch targets;
- `JUMP`: one numeric destination, with the remaining target lanes absent/`-1`;
- `BRANCH3`: one condition value ID plus numeric negative/zero/positive targets in that exact order.

Every qualified non-external block must end in exactly one complete terminator.

## Existing corpus coverage

Prepared coverage reuses existing deterministic inputs:

- direct return: `wide_literal_positive`, `local_identity`;
- while/back-edge: `while_counter`;
- three-way branch: `match_three_way`;
- call dataflow under control flow: `loop_call_dataflow`;
- array dataflow under control flow: `array_index_loop`.

Nested control flow and break/continue are not expanded speculatively. They should be pinned only if exact canonical-source usage proves they are required by the Stage1 self-hosting subset.

## Exit gate

Stage06 is evidence-ready only if:

```text
S1=PASS
S2=PASS
S3=PASS
S4_COMPLETE_TERMINATORS=PASS
RETURN_TERMINATOR=PASS
JUMP_TERMINATOR=PASS
BRANCH3_TERMINATOR=PASS
BRANCH3_TARGET_ORDER=PASS
BLOCK_TERMINATOR_COVERAGE=PASS
CANDIDATE_STAGE0_CHECK=PASS
FOCUSED_NATIVE_V2_CONFORMANCE=PASS
```

During Stage06, `Z 31` is forbidden because S5 has not closed. The prepared gate requires `z_mask < 31`.

The Benchmark gate is advisory evidence only. Transition to Stage07 remains controlled by the live S3 control branch.
