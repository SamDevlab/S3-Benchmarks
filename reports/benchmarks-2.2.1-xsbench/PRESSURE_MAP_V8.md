# Pressure Map V8

## Classification

```text
INLINE_WARMUP_BUDGET_CONFOUNDER=CONFIRMED
MEASUREMENT_WINDOW=AVAILABLE
FFI_REPRODUCIBILITY=PASS
PERFORMANCE_PRESSURE=WORKLOAD_LOCAL
CAUSALITY=NOT_ESTABLISHED
S3_CAUSAL_EXPERIMENT_READY=NO
```

The WARMUPS=0 calibration and the controlled A/B proof show that full-K
inline warmups consume the finite S3 instruction budget before the measured
section. Separating five warmup samples into fresh processes restores a valid
K=750000 window while preserving the 100 ms control threshold.

The E/F pair is reproducible for all four variants. It establishes a limited,
workload-local timing gap under the stated protocol: the S3 variants are much
slower than the GCC and Clang controls for this medium XSBench-compatible
lookup fixture. It does not establish a compiler mechanism, a general S3
performance claim, or causality. Hardware counters remain unavailable under
host policy, and the prior A/B variance is not reproduced by the controlled
E/F pair.

No S3 source was changed. No S3 optimization is proposed from this evidence.
The next causal experiment remains deferred until a structural, falsifiable
mechanism is identified independently of this measurement correction.
