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

## Evidence pipeline

The parallel laboratory workflow is intentionally read-only with respect to S3:

```text
S3 Stage1 evidence
    -> import_s3_bootstrap_evidence.py
    -> bootstrap snapshot
    -> check_bootstrap_laboratory.py

bootstrap corpus
    -> Stage0/reference
    -> optional Stage1
    -> run_bootstrap_differential.py
    -> summarize_bootstrap_semantic_coverage.py

candidate command
    -> measure_bootstrap_resource_envelope.py
    -> check_bootstrap_determinism.py

Stage1/Stage2/Stage3 artifacts + observations
    -> compare_bootstrap_stages.py
```

A case-level differential PASS never promotes an IR surface by itself. IR closure
continues to require explicit Stage1 semantic evidence.

## Evidence import

```bash
python tools/import_s3_bootstrap_evidence.py \
  --s3-repo /path/to/S3 \
  --benchmark-repo . \
  --expected-s3-commit <40-char-sha> \
  --output .artifacts/current-bootstrap.json

python tools/check_bootstrap_laboratory.py .artifacts/current-bootstrap.json
```

The importer consumes `reports/selfhost/stage1/semantic-ir-requirements.json` and
maps explicit `semantic_relationships` into the five surfaces. Host/reference IR
counts remain provenance only and are never copied into Stage1 resource metrics.

## Differential campaign

Generate the deterministic corpus:

```bash
python tools/generate_bootstrap_fuzz_corpus.py --output .artifacts/bootstrap-corpus
```

Run reference only while Stage1 is unavailable:

```bash
python tools/run_bootstrap_differential.py \
  .artifacts/bootstrap-corpus/manifest.json \
  --reference-command "python -m bootstrap.s3.cli run {source}" \
  --output .artifacts/differential.json
```

When a Stage1 executable exists, add `--stage1-command`. The known
`S3_STAGE1_EMITTER_BLOCKED` marker is classified as `STAGE1_BLOCKED`; an
unrecognized Stage1 error, timeout, reference failure, or semantic mismatch is a
hard campaign failure.

Create the case-level semantic coverage report with:

```bash
python tools/summarize_bootstrap_semantic_coverage.py \
  --snapshot .artifacts/current-bootstrap.json \
  --differential .artifacts/differential.json \
  --output .artifacts/semantic-coverage.json
```

## Resource characterization

The lab records, when available:

- peak RSS;
- compile wall time;
- user/system CPU time;
- compiler/artifact bytes;
- assembly bytes;
- semantic values;
- instructions;
- blocks;
- calls.

Example:

```bash
python tools/measure_bootstrap_resource_envelope.py \
  --command "<compiler command>" \
  --artifact path/to/output \
  --output .artifacts/resource-envelope.json
```

Resource measurements are `CHARACTERIZATION_ONLY` until correctness and semantic
equivalence are established. Host/reference IR measurements may influence
architecture selection, but may not be copied directly into fixed Stage1 array
sizes without a Stage1-specific representation proof.

## Determinism and future Stage2/Stage3 comparison

```bash
python tools/check_bootstrap_determinism.py source.s3 \
  --command "<compiler> {source} -o {output}" \
  --repeats 3 \
  --output .artifacts/determinism.json
```

The stage comparator keeps byte reproducibility separate from semantic
observations:

```bash
python tools/compare_bootstrap_stages.py \
  --stage1-artifact stage1.bin \
  --stage2-artifact stage2.bin \
  --stage3-artifact stage3.bin \
  --stage1-observation stage1.obs \
  --stage2-observation stage2.obs \
  --stage3-observation stage3.obs \
  --output .artifacts/stage-equivalence.json
```

Missing Stage2/Stage3 artifacts remain `NOT_AVAILABLE`; they are never treated as
zero-sized, equal, or PASS.

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
