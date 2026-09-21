# Jacobi Correctness Triage

```text
JACOBI_NATIVE_CORRECTNESS=HARNESS_GAP
JACOBI_PERFORMANCE_MEASURED=NO
```

Hosted small and medium O0/O1 checks remain recorded. The native adapter
currently reports an explicit `HARNESS_GAP` for the Jacobi pilot because the
fixed-work pilot builder does not expose that workload in the native replay
generator. This is not classified as an S3 native failure and no Jacobi timing
was collected.
