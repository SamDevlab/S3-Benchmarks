# S3 Benchmark Handoff

## Closed Evidence

The external benchmark branch now contains two bounded evidence layers:

1. Phase A direct FFI reuse with four workload families and reproducible
   correctness/timing artifacts.
2. Phase B deterministic RMSD expansion with hosted O0/O1 agreement and Linux
   x86-64 native canaries.

The Phase B result is pinned to benchmark HEAD
`aacee293056cd3422bf25bd9c9a9834c67bb6f71` and S3 HEAD
`e07d0b5464bf472b2ca18993f3e196a234ff0fc5`.

## Gaps

- Phase B intentionally collected no timing and contains no synthetic timing.
- XSBench, miniBUDE, and miniMD remain unpromoted pending provenance, license,
  input, oracle, and adapter review.
- `perf` counters remain unavailable under the Phase A host policy.
- No compiler optimization cause is established by this evidence.

## Recommended Next Experiments

1. Qualify one deferred workload end to end with immutable provenance and an
   independent oracle.
2. Add a matched native correctness matrix for that workload before any
   timing protocol.
3. Only after correctness closure, design a separate timing experiment with
   an explicit boundary and supported counters.

```text
S3_SOURCE_CHANGED=NO
PHASE_B_GATE=PASS
TIMING_CLAIMS=NONE
EXTERNAL_PR=NONE
```
