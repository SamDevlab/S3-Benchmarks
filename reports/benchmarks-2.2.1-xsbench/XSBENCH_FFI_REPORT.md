# XSBench Direct FFI Report

## Result

```text
FFI_CORRECTNESS=PASS (12/12)
RUN_A=PASS
RUN_B=PASS
SAME_ARTIFACT_A_B=PASS
SAME_BINARY_ACROSS_K=PASS
SYNTHETIC_TIMING=ABSENT
FFI_REPRODUCIBILITY=FAIL
XSBENCH_STATUS=REPRODUCIBILITY_OPEN
NEXT_PATH=MEASUREMENT_ENVIRONMENT_INVESTIGATION
```

The timing completed for all tiers and variants, but the existing 25 percent
Run A/B reproducibility rule was not met by every control sample. This is a
measurement-environment limitation, not a correctness, provenance, ABI, or
capability failure. No speedup or slowdown claim is promoted.

## Direct observations

Values below are factual medians from the preserved raw reports. They are
contextual observations only; the first number is Run A ns/lookup and the
second is Run B ns/lookup.

| Tier | S3 FFI O0 | S3 FFI O1 | GCC O2 | Clang O2 |
|---|---:|---:|---:|---:|
| TINY | 3051.83 / 2898.99 | 3049.09 / 2848.08 | 34.86 / 28.43 | 29.42 / 24.04 |
| SMALL | 2673.49 / 2555.08 | 2611.66 / 2457.34 | 30.50 / 23.46 | 27.08 / 18.49 |
| MEDIUM | 2549.45 / 2636.68 | 2406.81 / 2602.98 | 24.04 / 27.16 | 20.16 / 22.30 |

The SMALL Clang control differs by 31.74 percent under the prescribed
median comparison, which is the observed failing reproducibility condition.
The raw samples, calibration, Run A, Run B, correctness, and compiled
artifacts are preserved under:

```text
reports/benchmarks-2.2.1-xsbench/raw/xsbench-qualification-20260921-224913-802102762/
```

The full structured result is `XSBENCH_FFI_RESULT.json`.

## Perf policy

`perf` is installed, but the requested hardware event set is unavailable on
the guest (`perf_event_paranoid=4`, no supported events). Therefore:

```text
PERF_BINARY_AVAILABLE=YES
PERF_PERMISSION=DENIED_OR_UNSUPPORTED_BY_HOST_POLICY
CYCLES_PER_LOOKUP=UNAVAILABLE
INSTRUCTIONS_PER_LOOKUP=UNAVAILABLE
CACHE_MISS_RATE=UNAVAILABLE
BRANCH_MISS_RATE=UNAVAILABLE
```
