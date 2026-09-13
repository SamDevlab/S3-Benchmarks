# Stage07 S3IR2 v2 serialization qualification (prepared, inactive)

This is S3-Benchmarks-side planning for the live S3 control-plane stage `07_SERIALIZATION_S5`.

It does not activate Stage07, mutate canonical Stage1, or authorize SELF_EMIT/Stage2.

## Frozen record family

```text
F/B/V/M/I/O/R/C/A/T/Z
```

Only `Z 31` represents complete S1-S5 coverage.

If any S1-S4 dependency is unresolved, the candidate must emit a lower completeness mask or fail closed. The Benchmark must never infer semantic correctness from `Z 31` alone.

## Required evidence

Each focused fixture must provide:

- parseable S3IR2 v2 stream;
- internal v2 verifier PASS;
- strict S3 semantic conformance PASS;
- exact `Z 31` completeness;
- at least three native executions of the same fixture;
- byte-identical streams across repeats;
- independent native provenance for every repeat;
- preserved stream SHA256 and conformance JSON.

A copied stream file is not a repeated native execution.

## Prepared representative mix

The plan spans literals, unary/binary dataflow, reassignment, parameters, nested calls, call-result reuse, while, BRANCH3/match and arrays/indexing. It deliberately reuses the Stage03-06 corpus rather than growing a new performance-like corpus during bootstrap closure.

## Exit gate

```text
S1=PASS
S2=PASS
S3=PASS
S4=PASS
S5_CANONICAL_SERIALIZATION=PASS
RECORD_FAMILY_COVERAGE=PASS
CANONICAL_RECORD_ORDER=PASS
STRICT_PARSEABILITY=PASS
FOCUSED_V2_CONFORMANCE=PASS
DETERMINISTIC_REPEAT=PASS
NATIVE_PROVENANCE_FOR_EACH_REPEAT=PASS
Z_MASK=31
```

A Stage07 laboratory PASS is still only advisory evidence. Stage08 transition and any later canonical/self-hosting authorization belong to the live control plane.
