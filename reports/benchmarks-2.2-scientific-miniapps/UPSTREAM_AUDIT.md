# Scientific Workload Upstream Audit

## RMSD

The external reference identity retained for the RMSD campaign is:

```text
REFERENCE=charnley.rmsd
REFERENCE_SHA=1ad8ecee48d95ab43b49bd9f2fe4f8f07d9106bd
```

The Phase B correctness oracle is the small independent RMSD implementation
under `benchmarks/scientific/rmsd/reference.py`. No unresolved upstream source
was copied into this repository, and the result does not claim upstream
performance equivalence.

## Deferred Workloads

XSBench, miniBUDE, and miniMD were audited as candidate workload families but
were not promoted into executable Phase B claims. Their provenance, license,
input-contract, and adapter requirements need an immutable review before any
source is vendored or any correctness result is published.

```text
XSBench=AUDIT_ONLY
miniBUDE=AUDIT_ONLY
miniMD=READINESS_AUDIT_DEFERRED
SOURCE_VENDORED=NO
```
