# Scientific Mini-Apps Phase B Report

## Provenance

```text
BENCHMARK_HEAD=aacee293056cd3422bf25bd9c9a9834c67bb6f71
S3_HEAD=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
PLATFORM=Linux x86_64
S3_SOURCE_CHANGED=NO
```

## Result

The deterministic RMSD expansion completed with five profiles:

```text
scientific.rmsd.small
scientific.rmsd.medium
scientific.rmsd.large
scientific.rmsd.batch_large
scientific.rmsd.matrix_large
```

All profiles matched the independent oracle in hosted O0 and O1 execution.
All profiles also passed the native x86-64 integer canary generated from the
same workload shape. The exact per-profile values, source hashes, and native
observations are in `SCIENTIFIC_MINIAPPS_RESULT.json`.

```text
RMSD_EXPANSION=PASS
SCIENTIFIC_HOSTED_CORRECTNESS=PASS
SCIENTIFIC_NATIVE_CORRECTNESS=PASS
PHASE_B_GATE=PASS
TIMING=NOT_RUN
SYNTHETIC_TIMING=ABSENT
```

This is a correctness and representability result. It makes no native speedup
claim and does not promote a compiler optimization.
