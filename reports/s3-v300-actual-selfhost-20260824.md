# S3 v3.00 external benchmark validation

This report is an external correctness record for the post-M3.00 actual
self-hosting certification. It does not replace the S3 certification gate.

## Provenance

- S3 certification commit: `b9c8fdd8b27802d3a10df20f7ae19c04e2895e62`
- Benchmark commit: `871e2015a2e2d15e202eb023f11a833304ba44e4`
- S3 source manifest: `aebc6f536c8bc44e861cd09f8bc5fceadf5ad26739763d7007179d48a465d4b4`
- Network access: `NO`

## Results

- Python reference `--verify-only`: `PASS`, exit `0`.
- Stage2 correctness: `BLOCKED_ARTIFACT_UNAVAILABLE`.
- Stage3 correctness: `BLOCKED_ARTIFACT_UNAVAILABLE`.
- Stage2/Stage3 equivalence: `NOT_APPLICABLE`.
- Smoke: `DEFERRED`.
- Full benchmark: `DEFERRED`.
- Performance validity: `NO`.
- Native speedup claim: `NO`.

The compiler adapter requires an explicit artifact path and matching SHA-256
for Stage2 and Stage3. Missing artifacts and mismatches fail closed; the
adapter does not fall back to the Python reference compiler.
