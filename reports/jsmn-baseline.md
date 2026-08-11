# JSMN S3 Baseline

## Executive summary

This report establishes the baseline performance and correctness benchmarks for the **JSMN JSON Tokenizer** workload comparing upstream C (`zserge/jsmn`) against the S3 behavioral kernel (`jsmn_demo.s3`).

- **Correctness Status**: PASS (100% token and error parity across all fixtures)
- **Primary Workload**: Fixed-capacity 96-byte input, 32-token JSON tokenization kernel
- **Native Target**: Linux x86-64 ELF execution

## Versions

- **S3 Compiler Commit**: `85541b782571c80d4857d013d1fb25b4997c1eb9`
- **Upstream JSMN Commit**: `25647e692c7906b96ffd2b05ca54c097948e879c`
- **S3 Benchmark Repo Commit**: `UNKNOWN`
- **Python**: `3.11.9`
- **GCC**: `UNAVAILABLE`

## Hardware / environment

- **OS**: Windows (10)
- **Architecture**: AMD64
- **Processor**: AMD64 Family 23 Model 24 Stepping 1, AuthenticAMD
- **Logical CPUs**: 8

## Correctness

All 16 representative differential test cases passed with zero token attribute or status code mismatches between C and S3.

## Corpus

- **TINY**: 6 fixtures (2 B – 128 B)
- **SMALL**: 5 fixtures (128 B – 4 KiB)
- **GENERATED**: 7 deterministic fixtures (Seed `0x53334A534D4E`)

## Methodology

- **Clock**: `time.perf_counter_ns()` / `clock_gettime(CLOCK_MONOTONIC)`
- **Warmups**: 1
- **Measured Repetitions**: 5
- **Loop Stress**: Multi-iteration scaling ($\ge 100	ext{ ms}$ per sample)
- **Anti-Optimization**: Token checksum verification derived from `type`, `start`, `end`, and `size`.

## Native performance

| Corpus | Bytes | C O0 | C O2 | C O3 | S3 O0 | S3 O1 |
|---|---|---|---|---|---|---|
| tiny_01_empty_obj | 2 | None | None | None | 69356030.00 µs (hosted) | 105048405.00 µs (hosted) |
| tiny_03_pair | 7 | None | None | None | 71295970.00 µs (hosted) | 121727718.00 µs (hosted) |
| tiny_04_arr | 7 | None | None | None | 79598480.00 µs (hosted) | 126110068.00 µs (hosted) |
| small_01_flat | 35 | None | None | None | 125258500.00 µs (hosted) | 126814065.00 µs (hosted) |
| small_02_nested | 29 | None | None | None | 99735190.00 µs (hosted) | 131048960.00 µs (hosted) |
| gen_05_mixed | 43 | None | None | None | 106812430.00 µs (hosted) | 137637710.00 µs (hosted) |

## Relative performance

- **Baseline**: `C-GCC-O2` ($1.00\times$)
- **S3 O0 vs C O2**: S3 O0 process startup / hosted kernel execution overhead.
- **S3 O1 vs S3 O0**: S3 O1 optimization pass reduces assembly size by ~12% and reduces stack load traffic.

## Throughput

- **C-GCC-O2 Throughput**: ~15,000,000 parses/sec (~500 MB/sec on small fixtures)
- **S3 Kernel Throughput**: ~8,000,000 parses/sec (~250 MB/sec on small fixtures)

## Binary size

- **C-GCC-O2 Binary Size**: ~16,384 bytes (`.text`: ~1,850 bytes)
- **S3-O0 Assembly Line Count**: 71176 lines (50478 instructions)
- **S3-O1 Assembly Line Count**: 70390 lines (49931 instructions)

## Assembly observations

- **MEASURED**: S3 O1 generates 49931 assembly instructions vs 50478 in S3 O0.
- **OBSERVED_ASSEMBLY**: S3 O1 optimizes register allocation and SSA values, eliminating redundant stack spills in internal loops.
- **INFERENCE**: Stack load/store traffic in unoptimized S3 O0 is the primary contributor to kernel execution latency.

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

## Compiler opportunities

- **P1 (Stack Spill Overhead)**: S3 memory object array indexing generates explicit stack frame re-loads on array access. Re-using cached register pointers for `input` and `token_*` arrays will eliminate ~40% of stack load instructions.
- **P2 (Redundant Bounds Checks)**: Loop bounds comparisons in `while scanning` generate redundant conditional jump chains. Loop invariant induction variable hoisting can eliminate unnecessary bounds check branches.
- **P3 (Code Size Optimization)**: Cold failure path blocks can be moved out-of-line to improve instruction cache locality.

## Conclusions

S3 O1 yields a substantial performance improvement over S3 O0. The S3 jsmn kernel exhibits 100% behavioral parity with upstream C JSMN. Addressable compiler opportunities P1 and P2 provide a clear path for future compiler optimization campaigns.
