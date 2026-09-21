# S3 Benchmarks 2.1.2 Fixed-Work Native Stability

```text
CAMPAIGN=S3_BENCHMARKS_2_1_2_FIXED_WORK_NATIVE_STABILITY
BENCHMARK_HEAD=e1399fde430f6cbd739c13b110fda1cc1b126ca9
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
MACHINE_FINGERPRINT=9f6c7cbbdbbc2d056ffc306f76a1dcd9df194e15167cb037542da54e97b59393
METHODOLOGY=FIXED_WORK_AMPLIFIED_PROCESS
DIRECT_KERNEL_TIME=NOT_AVAILABLE
CALLABLE_KERNEL_ABI=NO
CROSS_K_SLOPE_STATUS=HISTORICAL_ONLY
NATIVE_CORRECTNESS=PASS
MATCHED_FLAT_REFERENCE=PASS
FROZEN_BINARY_A_B=NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW
BUILD_DETERMINISM=NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW
SAME_MACHINE_REPRODUCTION=NOT_RUN_NO_COMMON_FIXED_WORK_WINDOW
PERF_DIAGNOSTICS=UNAVAILABLE_PERMISSION
JACOBI_NATIVE_CORRECTNESS=HARNESS_GAP
JACOBI_PERFORMANCE_MEASURED=NO
PRESSURE_MAP_V3=NOT_ACTIONABLE_NO_COMMON_FIXED_WORK_WINDOW
S3_CAUSAL_EXPERIMENT_READY=NO
NEXT_PATH=MEASUREMENT_ENVIRONMENT_INVESTIGATION
STATUS=NO_COMMON_FIXED_WORK_WINDOW
PR=18
MERGE=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

The primary comparison uses one selected `K_FINAL` per workload, the same
across S3 O0, S3 O1, GCC O2 and Clang O2. Calibration is discarded as timing
evidence. Calibration found no common `K_FINAL` satisfying the bounded target across all four variants for every workload, so no official fixed binary or Run A/B was started; this is a protocol closure, not a timing result.

The historical cross-K slope evidence remains preserved in the 2.1.1 report
and is classified `HISTORICAL_ONLY`. It is not used as the primary result here.

Raw JSON, frozen manifests, build hashes, calibration decisions and all sample
arrays are under `reports/benchmarks-2.1.2-fixed-work-native-stability/raw/fixed-work-native-20260921-135552`. Derived executables, objects and
assembly payloads may be removed after hashing; their SHA-256 values remain in
the frozen manifest.
