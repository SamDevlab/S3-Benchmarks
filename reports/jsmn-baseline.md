# JSMN S3 Baseline

## Validity statement

> **PREVIOUS_PERFORMANCE_RESULTS_INVALIDATED**: YES
> **REASON**: SYNTHETIC_HOSTED_TIMING_AND_MISSING_NATIVE_S3_RUNNER
> **SYNTHETIC_TIMING**: ABSENT
> **PERFORMANCE_DATA_AVAILABLE**: NO

This checked-in artifact records the correctness and assembly characterization available from the environment below. It does **not** contain a valid C-vs-S3 native performance comparison because the required native toolchain measurements were unavailable in this run. Linux CI artifacts are the authoritative source for native performance measurements when all required variants complete successfully.

## Versions

- **S3 Compiler Commit**: `85541b782571c80d4857d013d1fb25b4997c1eb9`
- **Upstream JSMN Commit**: `25647e692c7906b96ffd2b05ca54c097948e879c`
- **S3 Benchmark Repo Commit**: `77e61932967481e6d3a3522d869b4fe9c516790c`
- **Python**: `3.11.9`
- **GCC**: `UNAVAILABLE`

## Environment

- **OS**: Windows (10)
- **Architecture**: AMD64
- **Processor**: AMD64 Family 23 Model 24 Stepping 1, AuthenticAMD
- **Logical CPUs**: 8

## Correctness

All 16 representative differential test cases passed with zero token attribute or status code mismatches between C and S3 (`GATE_F_DIFFERENTIAL_CORRECTNESS: PASS`).

## Current S3 limitations

```text
JSMN_S3_DROP_IN_API=NO
JSMN_S3_INCREMENTAL_PARSER=NO
JSMN_S3_RUNTIME_TOKEN_CAPACITY=NO
JSMN_S3_LARGE_INPUT=NO
JSMN_S3_C_ABI=NO
JSMN_S3_NATIVE_KERNEL=YES
JSMN_S3_O0_NATIVE=YES
JSMN_S3_O1_NATIVE=YES
RA_SEPARATE_SWITCH=UNAVAILABLE
```

These capability flags describe the pinned S3 compiler commit used by this benchmark artifact, not newer S3 milestones.

## Corpus

- **TINY**: 6 fixtures (2 B – 128 B)
- **SMALL**: 5 fixtures (128 B – 4 KiB)
- **GENERATED**: 7 deterministic fixtures (Seed `0x53334A534D4E`)
- **MEDIUM / LARGE**: BLOCKED_BY_CURRENT_S3_API (inputs greater than 96 bytes are not supported by the pinned fixed-buffer kernel).

## Native benchmark methodology

When the required native toolchains are available, the suite uses:

- **Measurement Scope**: `NATIVE_PROCESS_WITH_INTERNAL_PARSE_LOOP`
- **Process Startup Policy**: `AMORTIZED_NOT_SUBTRACTED`
- **Internal Parse Loop**: each executable runs an internal loop of 1,000 parses per process run in this artifact configuration.
- **Clock**: `time.perf_counter_ns()` measuring real process wall time.
- **Warmups**: 1
- **Measured Repetitions**: 5

No native timing claim is made from this checked-in run because the comparative binaries were unavailable.

## Native performance

| Corpus | Bytes | Logical Parses | C-GCC-O0 | C-GCC-O2 | C-GCC-O3 | S3-O0-NATIVE | S3-O1-NATIVE |
|---|---|---|---|---|---|---|---|
| tiny_01_empty_obj | 2 | 1,000 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| tiny_03_pair | 7 | 1,000 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| tiny_04_arr | 7 | 1,000 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| small_01_flat | 35 | 1,000 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| small_02_nested | 29 | 1,000 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |
| gen_05_mixed | 43 | 1,000 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE |

## Relative performance

Comparative native performance is **UNAVAILABLE** in this artifact. No statement about S3 O0, S3 O1, or C relative speed is supported by these rows.

## Throughput

Throughput is **UNAVAILABLE** in this artifact because no comparative native timing rows were produced.

## Native binary size

| Variant | ELF File Size (bytes) | .text Section (bytes) |
|---|---|---|

No native binary-size comparison is available from this environment.

## Assembly observations

- **OBSERVED**: S3 O0 generates 52,307 instructions (73,746 assembly lines) vs S3 O1 generating 51,668 instructions (72,831 assembly lines).
- **OBSERVED**: S3 O1 contains 9,604 stack-related operations vs 9,677 in S3 O0.
- **NOT MEASURED HERE**: the runtime latency impact of those stack operations. They are an optimization candidate, not evidence of a measured bottleneck in this artifact.

## Compiler opportunities

- **P1 (Stack traffic)**: investigate whether register caching of frequently reused array/frame addresses reduces generated stack traffic.
- **P2 (Bounds checks)**: measure whether loop-invariant bounds-check elimination is legal and beneficial before promoting it as an optimization target.
- **P3 (Code size)**: evaluate cold-path outlining against native code-size and runtime measurements.

These are hypotheses derived from assembly characterization and require native measurements before performance claims are made.

## Limitations

```text
JSMN_S3_DROP_IN_API=NO
JSMN_S3_INCREMENTAL_PARSER=NO
JSMN_S3_RUNTIME_TOKEN_CAPACITY=NO
JSMN_S3_LARGE_INPUT=NO
JSMN_S3_C_ABI=NO
JSMN_S3_NATIVE_KERNEL=YES
JSMN_S3_O0_NATIVE=YES
JSMN_S3_O1_NATIVE=YES
RA_SEPARATE_SWITCH=UNAVAILABLE
```

## Conclusion

The pinned S3 JSMN kernel demonstrates behavioral correctness for the 16 differential cases covered by this run. This checked-in artifact does **not** establish a native performance baseline because its C and S3 timing rows are unavailable. Native performance conclusions must come from a run where the required comparative variants produce real timing data, such as the Linux CI benchmark artifacts.
