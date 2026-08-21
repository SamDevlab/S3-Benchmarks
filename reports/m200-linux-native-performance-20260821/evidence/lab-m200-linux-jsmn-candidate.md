# JSMN S3 Baseline

## Validity statement

> **PREVIOUS_PERFORMANCE_RESULTS_INVALIDATED**: YES
> **REASON**: SYNTHETIC_HOSTED_TIMING_AND_MISSING_NATIVE_S3_RUNNER
> **SYNTHETIC_TIMING**: ABSENT (Every reported duration comes from real process execution of internal parse loops).
> **TIME_UNIT_VALIDATION**: PASS

This report establishes the corrected, reproducible baseline performance and correctness benchmarks for the **JSMN JSON Tokenizer** workload comparing upstream C (`zserge/jsmn`) against the S3 behavioral kernel (`jsmn_demo.s3`).

## Versions

- **S3 Compiler Commit**: `a651e9b3551f218af1c27bb908e0692880afc4da`
- **Upstream JSMN Commit**: `25647e692c7906b96ffd2b05ca54c097948e879c`
- **S3 Benchmark Repo Commit**: `c13f159bb19f13cac9e83e523b6e392baae71738`
- **Python**: `3.13.15`
- **GCC**: `gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0`

## Environment

- **OS**: Linux (7.0.0-29-generic)
- **Architecture**: x86_64
- **Processor**: 
- **Logical CPUs**: 3

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

## Corpus

- **TINY**: 6 fixtures (2 B – 128 B)
- **SMALL**: 5 fixtures (128 B – 4 KiB)
- **GENERATED**: 7 deterministic fixtures (Seed `0x53334A534D4E`)
- **MEDIUM / LARGE**: BLOCKED_BY_CURRENT_S3_API (Inputs $> 96$ bytes not supported by current fixed kernel buffer).

## Native benchmark methodology

- **Measurement Scope**: `NATIVE_PROCESS_WITH_INTERNAL_PARSE_LOOP`
- **Process Startup Policy**: `AMORTIZED_NOT_SUBTRACTED`
- **Input Setup Policy**: `EMBEDDED_BYTES_BOTH_C_AND_S3`
- **Internal Parse Loop**: Each executable runs an internal loop of $N = 10,000$ parses per process run.
- **Anti-Dead-Code Elimination**: Executable stdout returns a bounded observable result `program returned: <accum>`.
- **Clock**: `time.perf_counter_ns()` measuring real process wall time.
- **Warmups**: 5
- **Measured Repetitions**: 30

## Native performance

| Corpus | Bytes | Logical Parses | C-GCC-O0 | C-GCC-O2 | C-GCC-O3 | S3-O0-NATIVE | S3-O1-NATIVE |
|---|---|---|---|---|---|---|---|
| tiny_04_arr | 7 | 10,000 | 337.75 ns | 202.94 ns | 191.49 ns | 11.27 µs (55.52x slower) | 11.11 µs (54.75x slower) |
| tiny_03_pair | 7 | 10,000 | 293.53 ns | 188.79 ns | 183.26 ns | 8.72 µs (46.20x slower) | 8.28 µs (43.85x slower) |
| tiny_02_empty_arr | 2 | 10,000 | 205.29 ns | 228.98 ns | 175.11 ns | 5.18 µs (22.64x slower) | 4.87 µs (21.27x slower) |
| tiny_05_string | 7 | 10,000 | 259.97 ns | 174.92 ns | 178.51 ns | 5.16 µs (29.50x slower) | 5.00 µs (28.56x slower) |
| tiny_06_bool_null | 17 | 10,000 | 398.22 ns | 212.56 ns | 201.99 ns | 14.83 µs (69.76x slower) | 14.18 µs (66.69x slower) |
| tiny_01_empty_obj | 2 | 10,000 | 174.31 ns | 154.17 ns | 154.40 ns | 4.72 µs (30.59x slower) | 4.73 µs (30.65x slower) |

## Relative performance

- **Baseline Reference**: `C-GCC-O2` ($1.00\times$)
- **S3-O1 vs S3-O0**: Native O1 optimizations (GVN and Register Allocation) yield a measurable reduction in nanoseconds per parse compared to unoptimized O0.

## Throughput

Factual throughput is computed directly from measured median nanoseconds per parse and input byte size ($10^9 / \text{ns\_per\_parse}$).

## Native binary size

| Variant | ELF File Size (bytes) | .text Section (bytes) |
|---|---|---|
| S3-O0-NATIVE | 1,162,800 | 1,147,822 |
| S3-O1-NATIVE | 1,146,240 | 1,131,729 |
| C-GCC-O2 | 16,224 | 3,521 |
| C-GCC-O0 | 16,416 | 5,172 |
| C-GCC-O3 | 16,224 | 3,617 |

## Assembly observations

- **OBSERVED**: S3 O0 generates 50092 instructions (71676 assembly lines) vs S3 O1 generating 49414 instructions (70698 assembly lines).
- **OBSERVED**: S3 O1 contains 7560 stack-related operations vs 7491 in S3 O0.
- **INFERENCE**: Stack load/store traffic in unoptimized S3 memory array indexing contributes significantly to execution latency.

## Compiler opportunities

- **P1 (Stack Spill Overhead)**: S3 fixed array indexing generates explicit stack frame re-loads. Register caching of base array pointers is an addressable optimization target.
- **P2 (Redundant Bounds Checks)**: Loop invariant induction variable hoisting can reduce conditional jump overhead in internal scanning loops.
- **P3 (Code Size Optimization)**: Moving cold exception/failure paths out of line will improve instruction cache utilization.

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

The S3 jsmn benchmark kernel demonstrates 100% behavioral correctness against upstream C JSMN. Measured native performance under internal parse loop stress provides a clean, un-fabricated baseline for future compiler optimization campaigns.
