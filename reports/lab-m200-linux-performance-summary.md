# S3 M2.00 Linux Native Performance Summary

## Provenance

- Baseline S3: `a9e430551f2ee77aa2ef229daf9e967333e83e2c`
- Candidate S3: `a651e9b3551f218af1c27bb908e0692880afc4da`
- Benchmark harness: `c13f159bb19f13cac9e83e523b6e392baae71738`
- Environment: Linux x86-64 in a VirtualBox VM, 3 vCPUs
- Python: 3.13.15
- GCC: Ubuntu 15.2.0; binutils 2.46

## Correctness And Protocol

Both baseline and candidate passed `--verify-only` and the full JSMN benchmark run. All 6 expected fixtures completed, with 0 blocked fixtures and exit 0 for both runs. The existing harness protocol was preserved: 5 warmups, 30 repetitions, 10,000 parses per sample, and process startup amortized rather than subtracted.

`NATIVE_COMPARATIVE_VALID=YES`: the VM, CPU, vCPU count, GCC, Python, benchmark SHA, fixtures, loop counts, flags, and protocol were held constant between runs. No T4 or new full campaign was executed for this publication analysis.

## Raw Performance

The values below are geometric means of the six per-fixture median `ns/parse` values emitted by the harness.

| Variant | Baseline | Candidate | Raw delta |
|---|---:|---:|---:|
| C-GCC-O0 | 188.338719 | 267.604214 | +42.091607% |
| C-GCC-O2 | 128.360434 | 192.120657 | +49.672801% |
| C-GCC-O3 | 121.809940 | 180.175825 | +47.906844% |
| S3-O0-NATIVE | 6183.138581 | 7540.585243 | +21.954007% |
| S3-O1-NATIVE | 6055.660584 | 7288.678663 | +20.361413% |

The raw direction is `REGRESSED`. However, the C-O2 control also moved by `+49.672801%`; therefore the raw wall-time change cannot be attributed entirely to S3. Relative to C-O2, S3-O0 changed from `48.170128x` to `39.249217x`, and S3-O1 changed from `47.177003x` to `37.938027x`. Normalized ratios improved by `18.519594%` and `19.583644%`, respectively. The final interpretation is `PERFORMANCE_DIRECTION=REGRESSED`, `REGRESSION_CONFIDENCE=LIKELY_REGRESSION`, with causal attribution `INCONCLUSIVE_DUE_TO_C_CONTROL_DRIFT`.

## Distribution And Fixtures

Each row below uses 30 raw samples per variant. The range and standard deviation are retained in the immutable JSON reports; the delta is candidate versus baseline median.

| Fixture | C-O2 delta | S3-O0 delta | S3-O1 delta |
|---|---:|---:|---:|
| tiny_01_empty_obj | +32.251335% | +13.938319% | +19.635114% |
| tiny_02_empty_arr | +105.626406% | +27.934178% | +23.234433% |
| tiny_03_pair | +44.632640% | +25.905992% | +22.030325% |
| tiny_04_arr | +52.031169% | +20.438402% | +21.110204% |
| tiny_05_string | +43.389430% | +25.538364% | +22.381391% |
| tiny_06_bool_null | +31.117990% | +18.558364% | +14.016851% |

All six S3 fixture deltas are positive, so the direction is uniform. Magnitude varies by input, with `tiny_02_empty_arr` worst and no single S3 outlier sufficient to explain the result. This is `UNIFORM` direction, `INPUT_DEPENDENT` magnitude, and not outlier-driven.

## Structural Comparison

The reports show no structural expansion between baseline and candidate:

| Variant | Instructions | Stack ops | Assembly lines | Branches | Loads/stores | ELF bytes | .text bytes |
|---|---:|---:|---:|---:|---:|---:|---:|
| S3-O0 baseline -> candidate | 50092 -> 50092 | 7491 -> 7491 | 71676 -> 71676 | 12914 -> 12914 | 24997 -> 24997 | 1162800 -> 1162800 | 1147822 -> 1147822 |
| S3-O1 baseline -> candidate | 49414 -> 49414 | 7560 -> 7560 | 70698 -> 70698 | 12694 -> 12694 | 24745 -> 24745 | 1146240 -> 1146240 | 1131729 -> 1131729 |

Therefore the evidence does not show `MORE_CODE`, `MORE_STACK_TRAFFIC`, `MORE_BRANCHES`, or `LARGER_TEXT`. The timing difference is not localized by these counters.

## Source Localization

The source diff contains 99 files and 20,948 insertions. The following are plausible candidates only; diff inspection is not causal proof.

| Change | First commit | Possible effect | Evidence | Confidence |
|---|---|---|---|---|
| Redundant native self-move analysis | `a06baa8` | Codegen candidate accounting; later path no longer rewrites Assembly | All reported structural counters are identical | Low |
| Logical self-move preservation and x86 initialization guard | `7b99ebb` | Extra initialized-register checking on logical TMOV | Touches x86 emitter; both O0 and O1 move similarly, but counters are unchanged | Low |
| Captured frame store preservation | `b59de94` | Preserved frame stores/reloads after disabling global DSE in observable paths | Optimizer explicitly protects memory observability; no counter expansion | Low |
| Loopback HTTP backpressure | `4be50ff` | No expected effect on JSMN native workload | HTTP-only implementation and tests | High, no effect |
| Release stability gate | `aa14b36` | No expected effect on JSMN hot path | Release validation and packaging code | High, no effect |

## Future Optimization Targets

1. Measure and reduce redundant initialized-register checks in the x86 emitter while preserving logical self-move safety.
2. Recover safe store/reload elimination in captured-frame paths without violating memory observability.
3. Use paired or interleaved C controls before attributing future native timing changes to compiler code.

Each item requires a future production change before implementation. No target was implemented here.

## Status

- `CORRECTNESS=PASS`
- `NATIVE_COMPARATIVE=YES`
- `PERFORMANCE=REGRESSED`
- `PYTHON_3_13=PASS`
- `PYTHON_3_14=COMPATIBILITY_OR_ENVIRONMENT_ISSUE`
- `TEST_HARNESS_COST` remains separate from `COMPILER_NATIVE_PERFORMANCE`.
- `S3_CHANGE=NO`
- `BENCHMARK_CHANGE=NO`
- `T4_RUNS=0`
- `MERGE=NO`
- `M2.01_STARTED=NO`
