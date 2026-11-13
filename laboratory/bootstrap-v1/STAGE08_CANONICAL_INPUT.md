# Stage08 canonical source as input (prepared, inactive)

Stage08 proves that the exact current `selfhost/compiler/s3c_stage1.s3` can be represented by the semantic candidate without modifying that canonical source.

The Benchmark-side validator takes a supplied canonical source file and recomputes its SHA256 and byte count. A checkpoint cannot relabel a different source as the canonical Stage1 input.

Required evidence:

```text
CANONICAL_SOURCE_AS_INPUT=PASS
CANONICAL_SOURCE_V2_CONFORMANCE=PASS
CANONICAL_SOURCE_DETERMINISM=PASS
NATIVE_PROVENANCE=PASS
S1=PASS
S2=PASS
S3=PASS
S4=PASS
S5=PASS
Z_MASK=31
CANONICAL_SOURCE_MUTATED=NO
```

A Stage08 PASS only makes Stage09 a candidate next step. It does not authorize canonical mutation. The live control plane must be re-read and must explicitly set `canonical_stage1_mutation_authorized=true` before Stage09 can proceed.
