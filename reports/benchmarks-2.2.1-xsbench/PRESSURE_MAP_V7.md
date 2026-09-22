# Pressure Map V7

## Status

```text
PRESSURE_MAP_VERSION=V7
STATUS=MEASUREMENT_WINDOW_UNAVAILABLE
CAUSALITY=NOT_ESTABLISHED
```

The closure evidence does not establish a performance cause. The bounded
calibration instead exposes a protocol incompatibility in the frozen medium
artifacts:

1. At K=450000, the fastest control reaches 109.088227 ms, but both S3
   variants terminate at the fixed 10,000,000,000-instruction runtime limit.
2. At K=400000, both control variants pass and the S3 variants still hit the
   same deterministic instruction limit; the fastest control is only
   87.444239 ms.
3. At K=200000, the S3 variants complete, but the fastest control is only
   46.860272 ms.

The prior A/B failure remains an environment-variability observation from the
original protocol. It is not combined with this deterministic measurement
window failure, and no C/D reproducibility claim is made.

## Pressure classification

```text
PRIMARY_OBSERVED_PRESSURE=FROZEN_S3_RUNTIME_INSTRUCTION_BUDGET_AND_SCALING
SECONDARY_OBSERVED_PRESSURE=CONTROL_WINDOW_INCOMPATIBILITY
ENVIRONMENT_VARIABILITY=NOT_RETESTED_BY_VALID_C_D_PAIR
PERF_COUNTERS=UNAVAILABLE_BY_HOST_POLICY
NATIVE_SPEEDUP_CLAIM=NO
CAUSAL_EXPERIMENT_READY=NO
```

The next experiment must choose a protocol that preserves comparable work and
the frozen-artifact policy while making the instruction budget and timing
window jointly feasible. It must not silently treat failed S3 samples as
zero, relax the 100 ms threshold, increase the instruction limit, or promote
the failed K=500000 Run C as a timing result.
