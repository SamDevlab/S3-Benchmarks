# M2.38 External Real-World Performance Campaign

- Benchmark branch: `benchmark/m238-real-world-rc-20260822`
- Benchmark start SHA: `7875801a03f758158e0d0685709f02f8b8f3cd15`
- Benchmark source SHA at measurement: `7875801a03f758158e0d0685709f02f8b8f3cd15`
- S3 candidate SHA: `39aa289b3de16c3832ef331085265b0e458707a3`
- S3 canonical baseline: `e23b092bec100cedc520841a7dd0f4488090b6a1`
- Environment: Windows AMD64; Linux native toolchain unavailable
- Virtualized Linux comparison: not executed in this measurement
- Bare-metal validation: `NO`

## Workload Matrix

The benchmark repository exposes executable JSMN and M1.99 harnesses only.
The requested P2-P18 external workloads are not present as executable,
protocol-compatible workloads, so they are `DEFERRED`; no synthetic
replacement was run.

| Workload | Correctness | Performance classification | Evidence |
| --- | --- | --- | --- |
| P1 JSMN/native | `PASS` for six fixtures and 100% differential parity | `DEFERRED_BY_ENVIRONMENT` for native timing | `raw/p1-jsmn-smoke.json` |
| M1.99 hosted characterization | `PASS` | `CHARACTERIZATION_ONLY` | `raw/m199-hosted-characterization.json` |
| P2-P18 external corpus | `DEFERRED` | `DEFERRED` | no executable workload present |

The JSMN smoke run recorded `S3-O1` assembly structure but no native timing:
the host reported `gcc_version=UNAVAILABLE`, and all native binary metrics
were unavailable. This is not a native performance result.

The M1.99 protocol used the same parsed `AssemblyProgram` and workload:
`OFF = original AssemblyProgram`, `ON = eliminate_redundant_noop_moves(original)`.
Timing was hosted Emulator execution. Native x86 generation was a supplementary
structural probe only; no native speedup claim is made.

Observed hosted M1.99 medians, in nanoseconds per 25-loop sample, were:

| Case | OFF median | ON median |
| --- | ---: | ---: |
| with self moves | 4,734,800 | 4,628,700 |
| without self moves | 4,121,400 | 3,945,900 |

These values are characterization measurements on the Windows host and are
not a production-hardware or native-speedup claim.

## Provenance and Raw Evidence

- M1.99 benchmark repository self-check: `PASS`
- M1.99 raw transcript SHA-256: `19575e9023eef8087f74960e5899a33c76eb4c77b55c0a7d0a429d2399503c18`
- P1 JSMN report SHA-256: `63a0454a54dcded12a36be9a019ffd060368d73a4a7643a6b063a5351c2d00ec`
- Benchmark repository SHA was resolved locally and matched the pinned SHA.
- S3 candidate SHA was resolved locally and matched the pinned SHA.

## Result

`M2_38_PERFORMANCE=CHARACTERIZATION_ONLY`

`BENCHMARK_CORRECTNESS=PASS`

`BENCH_TIMING_CLASS=CHARACTERIZATION_ONLY`

`NATIVE_SPEEDUP_CLAIM=NO`
