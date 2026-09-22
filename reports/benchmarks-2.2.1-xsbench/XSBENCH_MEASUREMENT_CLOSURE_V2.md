# XSBench Measurement Closure V2

## Result

```text
COMMON_100MS_WINDOW=PASS
SELECTED_K=750000
WARMUP_SAMPLES=5
INLINE_DRIVER_WARMUPS=0
RUN_E=PASS
RUN_F=PASS
REPETITIONS=30
BALANCED_INTERLEAVING=PASS
FFI_REPRODUCIBILITY=PASS
NATIVE_SPEEDUP_CLAIM=NO
STATUS=QUALIFIED
```

Run E and Run F were independent sessions on the same machine and exact
artifact set. Each run performed five independent warmup samples per variant,
then 30 fresh-process official samples per variant. Warmup timings were not
included in the official statistics.

| Variant | E median ns | F median ns | delta | E CV | F CV |
|---|---:|---:|---:|---:|---:|
| S3_FFI_O0 | 14184990214.5 | 14243536650.0 | 0.411038613% | 0.0147481476 | 0.0330807859 |
| S3_FFI_O1 | 13756193245.0 | 13766528564.0 | 0.075075710% | 0.0116232252 | 0.0394754303 |
| GCC_O2 | 130760943.0 | 131211545.5 | 0.343416807% | 0.0846012183 | 0.1014145048 |
| CLANG_O2 | 104982871.0 | 106478338.0 | 1.404480036% | 0.1347571377 | 0.1743804054 |

All four deltas satisfy the established 25% rule. Full min/max/p95/MAD
statistics are preserved in `run_e.json` and `run_f.json`.

## Limited performance observation

Using Run E medians only, the ratios are:

```text
S3_O0_TO_GCC_RATIO=108.480329746
S3_O0_TO_CLANG_RATIO=135.117187017
S3_O1_TO_GCC_RATIO=105.201086268
S3_O1_TO_CLANG_RATIO=131.032740046
```

These are limited to `scientific.xsbench.compatible_lookup.medium`, this
machine, these frozen artifacts, and this timing boundary
(`KERNEL_PLUS_MATCHED_FFI_BOUNDARY`). They are not general S3 claims and do
not establish a compiler cause.

## Provenance

```text
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
BENCHMARK_FUNCTIONAL_HEAD=edbce77725e1193e602d93258431e4fae85d6694
PREVIOUS_BENCHMARK_HEAD=6508a542a033b417aceedd78f34b017198576650
CLOSURE_HEAD_BEFORE_THIS_CAMPAIGN=dae4cc85870b890b40981e3cbd480937798d91bb
ORIGINAL_AB_FINGERPRINT=cae6d65e71c97a0b0bbc1d83697faf67958777f50b7f6fc922e5de4b175abade
OFFICIAL_E_F_FINGERPRINT=cae6d65e71c97a0b0bbc1d83697faf67958777f50b7f6fc922e5de4b175abade
LEGACY_CLOSURE_HELPER_FINGERPRINT=97838760b4a5698e35ab5314930224216d3f936837c54a870789bc9b732a5b69
FINGERPRINT_RECONCILIATION=FINGERPRINT_SCHEMA_CHANGED
SAME_PHYSICAL_MACHINE_FOR_E_F=YES
```

The `9783...` value came from the earlier ad-hoc recalibration helper, which
used a different CPU identity schema. The official E/F helper uses the same
`/proc/cpuinfo`-based schema as A/B and produces the same `cae6...` identity.

## Perf and gates

```text
PERF_BINARY_AVAILABLE=YES
PERF_COMMAND_EXECUTABLE=YES
PERF_HARDWARE_EVENTS_AVAILABLE=NO
PERF_COUNTER_MEASUREMENT=UNAVAILABLE
PERF_PERMISSION=DENIED_OR_UNSUPPORTED_BY_HOST_POLICY
HOSTED_CORRECTNESS=PASS
NATIVE_CORRECTNESS=PASS
FULL_SUITE=INHERITED_52_PASSED_1_SKIPPED
FULL_SUITE_RERUN=NO_SOURCE_CHANGE
S3_SOURCE_CHANGED=NO
S3_CAUSAL_EXPERIMENT_READY=NO
PR_MERGED=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

Raw evidence is under:

```text
reports/benchmarks-2.2.1-xsbench/raw/xsbench-measurement-closure-v2-20260922-warmup0-official/
```
