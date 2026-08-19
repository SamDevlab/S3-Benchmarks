# External Reference Corpus

This directory records external projects used to design and review future S3 benchmark campaigns.

## Policy

- **CORRECTNESS BEFORE PERFORMANCE** remains the repository-wide rule.
- Every external reference used by a campaign must be pinned to an immutable commit SHA.
- Reference repositories are **not** benchmark results and are **not** automatically copied or vendored into this repository.
- A performance comparison is valid only after S3 and the chosen oracle/reference implementation have an explicitly defined equivalent workload and pass the differential correctness gate.
- Network/TLS benchmarks must use local fixtures or loopback services by default; public internet access must not be required for correctness.
- Large projects may be used as architecture or workload references without attempting a full-language port.

## Current M1.71-M1.80 corpus

See [`upstreams-m171-m180.json`](upstreams-m171-m180.json).

The current pinned research set is intentionally scoped to the capabilities now present in S3:

- `rust-lang/rust` — async lowering, ownership across suspension, future/drop semantics.
- `tokio-rs/tokio` — task lifecycle, executor behavior, timers, channels, async networking.
- `tokio-rs/mio` — readiness/reactor and nonblocking I/O behavior.
- `rustls/rustls` — nonblocking TLS state machine and secure validation behavior.
- `libuv/libuv` — cross-platform event-loop and resource-lifecycle reference.
- `llvm/llvm-project` — AArch64 ABI, ELF/Mach-O and native backend structural reference.
- `rust-lang/cargo` — package identity, registry, lockfile, checksum and offline-cache reference.
- `astral-sh/uv` — modern resolver, cache and reproducible package/distribution workflow reference.
- `harry0703/MoneyPrinterTurbo` — real-world application workload-shape reference for provider registry, config/service layering, local network/TLS integration and deterministic output flow.

MoneyPrinterTurbo is **not** a compiler oracle and is not ported wholesale. The bounded integration candidate has been promoted to [`benchmarks/provider_pipeline`](../benchmarks/provider_pipeline/README.md). That gate uses local fixtures only, does not execute MoneyPrinterTurbo itself, does not call real AI providers, and explicitly marks Python-harness JSON parsing as outside the current S3 runtime feature set.

## Promotion into an executable benchmark

A candidate should move into `benchmarks/` only when all of these exist:

1. a bounded workload definition;
2. immutable upstream and S3 commit pins;
3. deterministic fixtures;
4. an oracle or equivalence contract;
5. differential correctness checks;
6. a timing methodology that does not use synthetic timing;
7. machine-readable and Markdown reports.

For correctness-only or structural preflights where performance is intentionally deferred, item 6 is satisfied by explicitly reporting that timing is invalid/deferred rather than fabricating comparative numbers.
