# Direct Kernel Methodology 2.1.1

Final native replay provenance: `BENCHMARK_EXECUTION_HEAD=8b0bd1d2f4f4e693ab6effa7659e011cf82ecf8c`,
`S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5`, with raw evidence under
`raw/native-replay-20260921-final/`.

The benchmark repository remains pinned to the S3 candidate and does not modify
the S3 compiler. The audit selected `METHOD_C_IN_PROCESS_AMORTIZATION` because the
pinned source has no internal timer or exported callable kernel ABI. The native
replay therefore measures complete native executable process time, not a
hardware-kernel timer.

## Boundaries

Each pilot allocates and initializes flat arrays once, then executes the same
kernel body for `K` iterations inside one process. A final observable prevents
dead-code elimination. The external wall clock measures the resulting process
envelope; any fitted slope is labeled `EMPIRICAL_SLOPE`, not physical kernel
time.

K levels requested: `1, 10, 100, 1000`. The native replay
first probes K=1 and K=10 for every pilot and variant, then selects common
deterministic levels under a projected `1.8`
second guard. The exact selected levels and skipped levels are in the raw JSON.

The C references use `gcc -O2` or `clang -O2` when available, without BLAS,
`-ffast-math`, or `-Ofast`. Their flat layouts and loop order are explicit in
the generated sources. The Linux x86-64 native replay is **available**.
S3, GCC and Clang use the same useful-work contract and correctness canary.
Native speedup is not claimed: fitted slopes are empirical PROCESS_E2E
incremental costs and include process startup/runtime initialization.

Run A and independent Run B use the same machine fingerprint, five warmups,
thirty interleaved samples per K, and a two-second hard sample timeout. Build
determinism compares source, assembly where applicable, object and executable
SHA-256 values. Jacobi is a separate correctness triage and is not timed until
its native canary is valid.
