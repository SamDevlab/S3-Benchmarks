# S3IR2 v2 laboratory operating guide

This guide documents the independent S3-Benchmarks consumer for Stage1 semantic-lowering evidence.

## Authority boundary

The S3 repository owns semantic truth.

- `SamDevlab/S3/tools/verify_stage1_semantic_conformance_v2.py` is the strict semantic conformance authority.
- This laboratory validates stream structure, exact-byte determinism, provenance, campaign completeness, and regressions.
- A completeness bit or a structurally valid stream never promotes a semantic lane by itself.
- This laboratory never authorizes canonical Stage1 mutation, SELF_EMIT, Stage2, Stage3, T4, or performance claims.

## Evidence lifecycle

For one fixture, S3 should produce:

```text
source.s3
candidate.s3ir2
conformance.json
repeat-2.s3ir2      # recommended; required for S5 qualification
repeat-3.s3ir2      # recommended; required for stronger determinism evidence
```

`tools/ingest_s3ir2_v2_evidence_set.py` converts that set into:

```text
ingest.json
determinism.json    # when repeats are supplied
scorecard.json
triage.json         # when conformance is not PASS
evidence-manifest.json
```

The evidence-set manifest is the unit consumed by campaign aggregation and immutable checkpoint recording.

## Incremental Codex stages vs campaign evidence

The live Codex control plane owns incremental gates such as Stage 03 Pass1 bindings. The campaign aggregator is not a replacement for those live implementation gates.

In particular, Stage 03 may legitimately report `S1=PARTIAL_EXPECTED` while constants/results are still unimplemented. A final retrospective campaign only becomes `PASS_EVIDENCE_SET` after the later full candidate can rerun those mapped Stage 03 cases with strict semantic conformance PASS.

This separation prevents a partial stream from being promoted merely because the current development slice behaved as expected.

## Stage map

`laboratory/bootstrap-v1/s3ir2-v2-stage-map.json` maps the deterministic bootstrap corpus to semantic concerns:

- Stage 03: function ownership, parameters, locals, source bindings;
- Stage 04: constants/results and instruction def/use;
- Stage 05: calls, ordered arguments/results, arrays/indexing, seventh-parameter fail-closed probe;
- Stage 06: RETURN/JUMP/BRANCH3 and loop/control-flow edges;
- Stage 07: deterministic canonical serialization and full strict conformance.

## Multi-fixture campaign

Use `tools/aggregate_s3ir2_v2_campaign.py` with `CASE_ID=PATH` evidence manifests.

A stage is `PASS_EVIDENCE_SET` only when every required case is present, structurally valid, and has strict S3 conformance PASS. Stage 07 additionally requires determinism PASS for every required case.

`FULL_V2_FIXTURE_CAMPAIGN=PASS` requires every mapped stage to be `PASS_EVIDENCE_SET`.

The campaign report is still laboratory evidence only; it is not a bootstrap promotion command.

## Immutable checkpoints

Use `tools/record_s3ir2_v2_checkpoint.py` to bind one evidence manifest to:

- exact candidate Git SHA;
- exact candidate source SHA-256;
- case ID;
- stage ID.

The recorder refuses to overwrite an existing checkpoint path. A later candidate must receive a new checkpoint rather than replacing earlier evidence.

## Regression comparison

Use `tools/compare_s3ir2_v2_campaigns.py` to compare a newer candidate campaign with an older baseline.

The regression gate fails when a previously passing:

- structural status;
- semantic conformance status;
- Stage 07 determinism status;
- stage evidence set

ceases to pass.

Improvements are reported separately from regressions.

## Failure workflow

When strict conformance fails:

1. keep the exact source, stream, and conformance JSON;
2. run structural ingest;
3. run `tools/classify_s3ir2_v2_failure.py` to estimate S1/S2/S3/S4/S5 ownership;
4. use `tools/capture_s3ir2_v2_failure_bundle.py` to preserve hashes and files;
5. when useful, use `tools/minimize_s3_failure.py` with an external predicate command that reproduces the failure;
6. add the minimized reproducer as a permanent regression only after confirming it still fails for the same semantic reason.

The minimizer never invokes a shell and does not understand S3 syntax. Invalid reductions simply stop satisfying the supplied predicate and are discarded.

## Determinism

S5 is stronger than semantic equivalence alone.

For one exact source and candidate artifact, repeated semantic streams should be byte-identical. `tools/check_s3ir2_v2_determinism.py` reports exact SHA-256 equality across repetitions.

Deterministic output is not, by itself, proof of semantic correctness; both determinism and strict S3 semantic conformance are required.

## Performance boundary

No tool in this S3IR2 v2 laboratory grants a performance claim. Resource measurements remain characterization-only until the separate host-eligibility and comparative-performance gates are satisfied.
