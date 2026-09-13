# Bootstrap Evidence Applicability

Evidence retained in an S3 commit is not automatically evidence for that commit's
current canonical Stage1 source.

Bootstrap Laboratory v1 distinguishes three identities:

1. the exact S3 Git commit containing the report;
2. the canonical Stage1 source SHA-256 described by the current semantic evidence;
3. the source SHA-256 on which a supplemental/native measurement was actually run.

A supplemental result may influence current qualification only when its measured
source is explicitly proven applicable to the current canonical source. Presence
of an old report in a newer Git commit is not enough.

## Current pinned example: S3 `0789ad2`

Current semantic Stage1 source:

```text
S3_COMMIT=0789ad2df5f200c6b35b67d591d10e016c1a557a
SEMANTIC_SOURCE_SHA256=ec6bef92782fe253f4b1c1390d90f95017670a3cbb65497eff9dba12a2e7623c
```

The retained call-pool closure report identifies its clean measured source as:

```text
CALL_POOL_MEASURED_SOURCE_SHA256=20fddbb73eee9ae09de911493f2f2da01ab582c7a6de879ea2e557946716a341
```

Therefore:

```text
SOURCE_APPLICABILITY=HISTORICAL_SOURCE_MISMATCH
PROMOTION_EFFECT=NONE_PROVENANCE_ONLY
```

The historical measurement remains useful provenance:

```text
required_capacity=736
selected_capacity=746
headroom=10
bank_sizes=[365,365,16]
pool_gate=PASS
remaining_blocker=GENERAL_EMITTER_CAPABILITY_GAP
```

Those values must **not** be silently relabelled as a fresh capacity proof for the
current `ec6bef...` source. A new current-source measurement is required before the
lab may mark the call-pool result as source-applicable.

## Applicability states

`MATCH`
: The supplemental measurement's canonical source hash equals the current semantic
  Stage1 source hash. This only proves source applicability; it does not itself
  promote any semantic IR surface.

`HISTORICAL_SOURCE_MISMATCH`
: The report is valid historical evidence but was measured on a different canonical
  source. It must not be reused as a current PASS without a separate evidence-reuse
  proof.

`UNKNOWN`
: One or both source hashes are unavailable. The result remains provenance only.

## Source lock

The read-only importer sets `provenance.source_lock_valid=true` only when both are
true:

```text
Git HEAD matches the requested S3 commit
AND
SHA256(selfhost/compiler/s3c_stage1.s3) matches semantic-ir-requirements.json
```

This prevents a current Git checkout with stale semantic evidence from appearing
source-locked.

## Non-promotion rule

Even when `SOURCE_APPLICABILITY=MATCH`, supplemental pool/capacity evidence has:

```text
promotion_effect=NONE_PROVENANCE_ONLY
```

The authoritative five semantic surfaces remain independently gated:

- `typed_values`
- `instruction_def_use`
- `call_dataflow`
- `complete_terminators`
- `canonical_serialization`

No capacity closure, host-oracle count, historical native run, or retained report
may promote those surfaces by itself.
