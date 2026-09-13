# Stage05 calls/arrays laboratory preparation

This file prepares the S3-Benchmarks side of `05_CALLS_ARRAYS_S3` without activating it.

The live S3 control plane remains authoritative. While it still reports Stage04, everything here is planning-only.

## Prepared scope

Stage05 is expected to close S3 call dataflow and the required fixed-array/index subset:

```text
internal call identity
foreign call identity/signature
ordered call arguments
call result values
nested calls
call result reuse
zero-argument calls
array identity/storage
array index semantic operands
array loads
array stores when required
fail-closed unresolved callees
fail-closed unsupported seventh-parameter emission until represented correctly
```

## Existing corpus coverage

Already pinned in the deterministic corpus:

```text
parameter_ordinal_0
parameter_ordinal_5
parameter_ordinal_6
nested_calls
call_result_reuse
array_index_loop
loop_call_dataflow
```

These are source inputs only until exact candidate/native/conformance evidence exists.

## Prepared, not yet activated

`stage05-fixture-plan.json` prepares exact sources for:

```text
zero_arg_call
foreign_call_i64
array_index_load
array_index_store
```

The foreign-call syntax is derived from S3's own FFI tests. Array index load/store follows the language's fixed-array syntax.

These cases must not enter the official stage map until Stage05 is activated by the live control plane. On activation, validate them with the S3 reference compiler first and freeze exact SHA-256 values.

## Negative cases planned for activation

```text
unresolved_callee_fail_closed
constant_array_oob_fail_closed
```

These are intentionally semantic-negative cases. They should prove fail-closed behavior, not be treated as normal successful differential fixtures.

## Historical capacity boundary

The historical call-pool checkpoint (`736 required / 746 selected`) remains provenance only.

Stage05 must not assume those values apply to the new semantic candidate/source. Before changing physical pool capacity, measure the exact candidate/source call and argument pressure.

Logical call IDs and ordered argument edges are semantic relationships and must not be conflated with physical pool slots.

## Preparedness audit

Use:

```text
tools/audit_stage05_preparedness.py
```

It checks that:

- the fixture plan and capability matrix remain `PREPARED_NOT_ACTIVE`;
- prepared/negative fixtures have not leaked into the active stage map;
- every capability fixture reference resolves to an existing corpus case or prepared/negative case;
- historical call-pool evidence remains provenance-only;
- blind reuse of `736/746` remains disabled.

Expected status before activation:

```text
PASS_PREPARED_NOT_ACTIVE
```

That status is not authorization to begin Stage05.

## Activation boundary

Only after the S3 control plane changes `active_stage` to `05_CALLS_ARRAYS_S3` should we:

1. validate prepared fixture sources against the exact S3 reference toolchain;
2. freeze fixture hashes;
3. promote prepared cases into the deterministic corpus/stage map;
4. freeze the Stage05 gate contract against the active control revision;
5. ingest native candidate streams with strict S3 conformance and provenance.

Until then:

```text
STAGE05_IMPLEMENTATION_AUTHORITY=CODEX/S3_CONTROL_PLANE
STAGE05_BENCHMARK_ACTIVATION=NO
CANONICAL_MUTATION_AUTHORITY=NO
PROMOTION_EFFECT=NONE_PLANNING_ONLY
```
