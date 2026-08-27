# S3 Bootstrap Laboratory v1

This laboratory tracks the vertical self-hosting path of `SamDevlab/S3`.
It is deliberately independent from compiler development branches: the lab
consumes pinned evidence and never mutates the S3 source repository.

## Priority

The current research priority is vertical closure:

```text
Stage0 reference
    -> Stage1 semantic IR closure
    -> general emitter
    -> Stage1 self-emit
    -> Stage2
    -> Stage3
    -> Stage1/Stage2/Stage3 equivalence
```

Real-world performance, accelerator, quantum, embedded and additional optimizer
research remain valuable, but they are not allowed to manufacture progress in
this chain.

## Five semantic surfaces

Bootstrap v1 normalizes the general-emitter prerequisites into five surfaces:

1. `typed_values`
2. `instruction_def_use`
3. `call_dataflow`
4. `complete_terminators`
5. `canonical_serialization`

Historical S3 reports may describe more granular lanes. The laboratory stores
those reports as provenance, but promotion depends on the emitter-facing five
surfaces rather than a permanently fixed historical lane count.

## Evidence states

The contract intentionally distinguishes:

- `PASS` / `FAIL`
- `BLOCKED`
- `NOT_STARTED` / `NOT_CREATED` / `NOT_AUTHORIZED`
- `DEFERRED`
- `CHARACTERIZATION_ONLY`
- `INCONCLUSIVE_ENVIRONMENT`

A blocked or unavailable stage is valid evidence. It is not a test failure and
must never be rewritten as PASS.

## Resource characterization

The lab records, when available:

- peak RSS;
- compile wall time;
- compiler/artifact bytes;
- assembly bytes;
- semantic values;
- instructions;
- blocks;
- calls.

Resource measurements are `CHARACTERIZATION_ONLY` until correctness and semantic
equivalence are established. Host/reference IR measurements may influence
architecture selection, but may not be copied directly into fixed Stage1 array
sizes without a Stage1-specific representation proof.

## Validator

```bash
python tools/check_bootstrap_laboratory.py path/to/snapshot.json
```

The validator fails closed when, for example:

- Stage2 appears before Stage1 self-emission and semantic-IR closure;
- Stage3 appears before Stage2 correctness;
- full self-hosting is claimed without Stage1/2/3 equivalence;
- performance is marked valid while correctness, workload equivalence,
  environment stability, or provenance locks are missing;
- resource metrics contain invalid negative measurements.

## Snapshot provenance

Every executable snapshot must pin both repositories:

```text
S3_COMMIT=<exact 40-char commit>
BENCHMARK_COMMIT=<exact 40-char commit>
SOURCE_LOCK_VALID=true
BENCHMARK_LOCK_VALID=true
```

Do not attribute historical benchmark results to a new S3 source line without a
new run or an explicit evidence-reuse contract that proves applicability.

## Current integration boundary

At the 2026-08-26 checkpoint, active S3 compiler work is occurring in PR #268.
This laboratory branch is intentionally separate from that PR and does not
modify `selfhost/compiler/s3c_stage1.s3`, its local reports, or its Linux guest.
The lab is ready to consume Stage1/Stage2/Stage3 evidence when those artifacts
become authorized.
