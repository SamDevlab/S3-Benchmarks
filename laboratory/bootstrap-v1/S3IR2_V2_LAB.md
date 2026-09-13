# S3IR2 v2 laboratory operating guide

This guide documents the independent S3-Benchmarks consumer for Stage1 semantic-lowering evidence.

## Authority boundary

The S3 repository owns semantic truth.

- `SamDevlab/S3/tools/verify_stage1_semantic_conformance_v2.py` is the strict semantic conformance authority.
- This laboratory validates stream structure, exact-byte determinism, native artifact provenance, campaign completeness, and regressions.
- A completeness bit or a structurally valid stream never promotes a semantic lane by itself.
- This laboratory never authorizes canonical Stage1 mutation, SELF_EMIT, Stage2, Stage3, T4, or performance claims.

## Evidence lifecycle

For one fixture, S3 should preserve the exact producer inputs/artifacts:

```text
candidate-source.s3
candidate-binary
source.s3
candidate.s3ir2
native-metadata.json
native-provenance.json
conformance.json
repeat-2.s3ir2
repeat-2-native-metadata.json
repeat-2-native-provenance.json
repeat-3.s3ir2                  # strongly recommended
repeat-3-native-metadata.json
repeat-3-native-provenance.json
```

### 1. Native provenance for every run

`native-metadata.json` follows `s3.stage1.native-semantic-evidence.v1` and declares:

```text
candidate_git_sha
candidate_source_sha256 / candidate_source_bytes
candidate_binary_sha256 / candidate_binary_bytes
fixture_source_sha256 / fixture_source_bytes
stream_sha256 / stream_bytes
platform.os = linux
platform.arch = x86_64
build.status = PASS
build.exit_code = 0
run.status = PASS
run.exit_code = <integer>
control_revision
```

`tools/render_s3ir2_v2_native_metadata.py` can compute the hashes/byte counts from the exact files. Its output is still only metadata.

Run `tools/validate_s3ir2_v2_native_provenance.py` with the actual candidate source, binary, fixture, and stream. The validator recalculates hashes and byte sizes; metadata alone is insufficient. Preserve the resulting `native-provenance.json`.

Repeat runs use the same process and get their own provenance report.

### 2. Repeat binding

`tools/ingest_s3ir2_v2_evidence_set.py` does not accept repeated bytes as determinism evidence by themselves.

For every repeat stream, supply one repeat native-provenance report. The evidence set requires all runs to resolve to the same:

```text
candidate_git_sha
candidate source SHA-256
candidate binary SHA-256
fixture source SHA-256
```

Each repeat provenance must also reference the SHA-256 of its own repeat stream.

Therefore copying the primary stream into a repeat file without a separately validated native run cannot satisfy the native evidence gate.

### 3. Strict S3 semantic conformance

Run the authoritative S3 verifier against `source.s3` and the primary `candidate.s3ir2`, and preserve its `conformance.json`.

S3-Benchmarks never substitutes its own structural parser for that semantic proof.

### 4. Evidence-set ingestion

The evidence-set ingestor consumes the primary source/stream/conformance/provenance plus matching repeat stream/provenance pairs and produces:

```text
ingest.json
native-binding.json
determinism.json
scorecard.json
triage.json         # when conformance is not PASS
evidence-manifest.json
```

The evidence-set manifest is the unit consumed by campaign aggregation and immutable checkpoint recording.

A final evidence-set `qualification_gate=PASS` requires all of:

```text
structural S3IR2 validation = PASS
primary native provenance = PASS
all repeat native provenance = PASS
all runs bound to the same candidate source/binary/fixture = PASS
strict S3 semantic conformance = PASS
deterministic repeated stream bytes = PASS
```

## Incremental Codex stages vs campaign evidence

The live Codex control plane owns incremental gates such as Stage 03 Pass1 bindings. The campaign aggregator is not a replacement for those live implementation gates.

Stage 03 may legitimately report `S1=PARTIAL_EXPECTED` while constants/results are still unimplemented. A final retrospective campaign only becomes `PASS_EVIDENCE_SET` after the later full candidate can rerun those mapped cases with native provenance and strict semantic conformance PASS.

## Stage map

`laboratory/bootstrap-v1/s3ir2-v2-stage-map.json` maps the deterministic bootstrap corpus to semantic concerns:

- Stage 03: function ownership, parameters, locals, source bindings;
- Stage 04: constants/results and instruction def/use;
- Stage 05: calls, ordered arguments/results, arrays/indexing, seventh-parameter fail-closed probe;
- Stage 06: RETURN/JUMP/BRANCH3 and loop/control-flow edges;
- Stage 07: deterministic canonical serialization and full strict conformance.

## Multi-fixture campaign

Use `tools/aggregate_s3ir2_v2_campaign.py` with `CASE_ID=PATH` evidence manifests.

A stage is `PASS_EVIDENCE_SET` only when every required case is present and has:

```text
structural_status = PASS
native_provenance_status = PASS
semantic_conformance_status = PASS
```

Stage 07 additionally requires `determinism_status=PASS` for every required case.

`FULL_V2_FIXTURE_CAMPAIGN=PASS` requires every mapped stage to be `PASS_EVIDENCE_SET`.

The campaign report remains laboratory evidence only; it is not a bootstrap promotion command.

## Immutable checkpoints

Use `tools/record_s3ir2_v2_checkpoint.py` to bind one evidence manifest to exact candidate Git SHA, candidate source SHA-256, case ID, and stage ID. The recorder refuses to overwrite an existing checkpoint path.

## Regression comparison

`tools/compare_s3ir2_v2_campaigns.py` fails its regression gate when a previously passing structural, native provenance, semantic conformance, Stage 07 determinism, or stage evidence status ceases to pass.

## Failure workflow

When strict conformance fails:

1. keep the exact candidate source/binary, fixture source, stream, native provenance, and conformance JSON;
2. run structural ingest;
3. classify likely S1/S2/S3/S4/S5 ownership with `tools/classify_s3ir2_v2_failure.py`;
4. preserve hashes/files with `tools/capture_s3ir2_v2_failure_bundle.py`;
5. when useful, minimize with `tools/minimize_s3_failure.py` and an external predicate command;
6. add the minimized reproducer only after confirming it fails for the same semantic reason.

The minimizer never invokes a shell and does not understand S3 syntax. Invalid reductions simply stop satisfying the supplied predicate.

## Determinism

For one exact fixture and one exact native candidate binary, independent native runs should emit byte-identical semantic streams. Exact-byte equality is necessary for S5 but is not semantic proof by itself.

## Performance boundary

No tool in this S3IR2 v2 laboratory grants a performance claim. Resource measurements remain characterization-only until the separate host-eligibility and comparative-performance gates are satisfied.
