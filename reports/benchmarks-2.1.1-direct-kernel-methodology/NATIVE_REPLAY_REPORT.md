# S3 Benchmarks 2.1.1 Native Replay

## Provenance

```text
CAMPAIGN=S3_BENCHMARKS_2_1_1_NATIVE_REPLAY
BENCHMARK_HEAD=8b0bd1d2f4f4e693ab6effa7659e011cf82ecf8c
EXECUTION_REPLAY_HEAD=8b0bd1d2f4f4e693ab6effa7659e011cf82ecf8c
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
HOST=Linux x86_64
MACHINE_FINGERPRINT_SHA256=9f6c7cbbdbbc2d056ffc306f76a1dcd9df194e15167cb037542da54e97b59393
VARIANTS=S3_O0,S3_O1,GCC_O2,CLANG_O2
S3_SOURCE_CHANGED=NO
```

The pinned S3 checkout was read-only. The benchmark source fixed the repeated-
work oracle before this replay; the S3 source itself was not modified.

## Protocol

The existing `METHOD_C_IN_PROCESS_AMORTIZATION` harness was used. Each pilot
allocates and initializes its flat data once, then runs the same useful kernel
body for K iterations in one native executable. Timing is external
`PROCESS_E2E`; it includes executable startup and runtime initialization. It
is an empirical incremental-cost characterization, not hardware kernel time.

Safety probes ran at K=1 and K=10 for every pilot and variant. The projected
guard accepted the common levels K=1, 10, 100, 1000 for all four pilots. Each
level used five warmups and thirty interleaved samples, with a 2.0 second hard
per-sample timeout. Run A and independent Run B used the same machine
fingerprint. All raw sample arrays and build records are preserved under:

`raw/native-replay-20260921-final/`

All raw timing arrays, probe records, source fixtures and SHA-256 build
manifests are preserved. Derived native payloads (executables, objects and
assembly text) were omitted from the published snapshot after hashing so the
review branch does not carry hundreds of megabytes of reproducible binaries.
This does not remove or alter any timing sample.

`perf` was unavailable by policy/permission, so no performance-counter claim
is made.

## Gates

```text
NATIVE_PILOT_CORRECTNESS=PASS
MATCHED_GCC_CLANG_REFERENCE=PASS
BUILD_DETERMINISM=PASS
RUN_A=PASS
RUN_B=PASS
SAME_MACHINE=PASS
SAME_MACHINE_SLOPE_REPRODUCIBILITY=FAIL
JACOBI_NATIVE_CORRECTNESS=NATIVE_CORRECTNESS_OPEN
NATIVE_SPEEDUP_CLAIM=NO
```

The four pilots produced canary-correct native executables for S3 O0/O1 and
the available GCC/Clang references. Build determinism matched source, assembly,
object, and executable SHA-256 values on duplicate builds. The A/B machine
identity matched, but the fitted process-E2E slopes
were not reproducible within the declared 25% limit for several short
reference variants. This is a measurement-resolution/startup-envelope issue
for the current protocol, not evidence of a native speedup or a compiler bug.

Jacobi was intentionally kept as a separate correctness triage. Its hosted
small/medium O0/O1 checks were exercised, while native O0/O1 canaries remained
open; no Jacobi timing was collected.

## Decision

```text
NATIVE_REPLAY=COMPLETE_WITH_REPRODUCIBILITY_GAP
PRESSURE_MAP=OBSERVED_STARTUP_ENVELOPE
NEXT_PATH=METHODOLOGY_REFINEMENT_FOR_PROCESS_E2E_SLOPE_STABILITY
EXPAND_CORPUS=NO
S3_CAUSAL_EXPERIMENT=NO
PR=18
MERGE=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

The next step is to refine the controlled native measurement protocol so its
incremental slopes are resolvable and reproducible before expanding the corpus
or making any causal performance claim.
