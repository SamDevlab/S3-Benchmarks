# Pressure Map V2

This report separates measurement confounders from S3 runtime bottlenecks.

| Pressure | Classification | Evidence |
| --- | --- | --- |
| Process startup/runtime initialization | NATIVE_REPLAY_REPRODUCIBILITY_GAP | Run A/B native PROCESS_E2E K-scaling with setup outside the repeated region. |
| Static code/stack operation density | OBSERVED_NOT_CAUSAL | S3/GCC/Clang matched flat references; no hardware counter claim is made. |
| Measurement variability | OPEN | Independent Run A/B slope comparison on one machine fingerprint. |

The hosted pilot gate is retained as a prior correctness record. The native
pilot result is in `NATIVE_REPLAY_RESULT.json`; every raw sample remains under
`raw/native-replay-20260921-final/`. The independent Run A/B slopes did not
reproduce within the declared limit, so measurement variability remains open
and the next path is methodology refinement for process-E2E slope stability.
No direct native speedup or kernel-time claim is made, and the pressure map is
not by itself an optimization authorization.
