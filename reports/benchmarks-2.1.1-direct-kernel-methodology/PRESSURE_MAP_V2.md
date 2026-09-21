# Pressure Map V2

This report separates measurement confounders from S3 runtime bottlenecks.

| Pressure | Classification | Evidence |
| --- | --- | --- |
| Process startup/runtime initialization | OBSERVED_STARTUP_ENVELOPE | Run A/B native PROCESS_E2E K-scaling with setup outside the repeated region. |
| Static code/stack operation density | OBSERVED_NOT_CAUSAL | S3/GCC/Clang matched flat references; no hardware counter claim is made. |
| Measurement variability | OPEN | Independent Run A/B slope comparison on one machine fingerprint. |

The hosted pilot gate is retained as a prior correctness record. The native
pilot result is in `NATIVE_REPLAY_RESULT.json`; every raw sample remains under
`raw/native-replay-20260921/`. The controlled run completed, but A/B slope
reproducibility did not pass for several short-reference variants and Jacobi
native correctness remains open. No direct native speedup or kernel-time claim
is made; the next path is methodology refinement before corpus expansion or a
causal experiment.
