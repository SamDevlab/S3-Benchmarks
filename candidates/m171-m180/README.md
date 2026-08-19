# M1.71-M1.80 Benchmark Candidates

The current S3 baseline is `SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`.

## Candidate A — async executor and channels

**Correctness preflight: PROMOTED** → [`benchmarks/async_runtime`](../../benchmarks/async_runtime/README.md)

Primary references: `rust-lang/rust`, `tokio-rs/tokio`.

Performance remains deferred until a native S3 workload with equivalent observable semantics exists.

Future timing kernels:

- create and complete N cooperative tasks;
- bounded channel ping-pong with capacities 1, 8, and 64;
- chained await depth;
- generated code size where native comparison is meaningful.

## Candidate B — reactor and loopback networking

**Correctness preflight: PROMOTED** → [`benchmarks/network_loopback`](../../benchmarks/network_loopback/README.md)

Primary references: `tokio-rs/mio`, `libuv/libuv`.

The promoted preflight verifies deterministic reactor and provider-neutral local-network semantics without public internet. Native socket/reactor performance remains deferred.

Future native kernels:

- localhost TCP connect/accept/read/write;
- UDP loopback send/receive;
- readiness re-arm after WouldBlock;
- fixed-size payload throughput;
- resource cleanup after cancellation/peer close.

## Candidate C — TLS local handshake

**Correctness preflight: PROMOTED** → [`benchmarks/tls_local`](../../benchmarks/tls_local/README.md)

Primary reference: `rustls/rustls`.

The promoted preflight validates the provider-neutral TLS state machine and secure defaults. It does not claim native TLS, trust-store, or external-chain execution certification.

Future native kernels:

- local trusted certificate handshake;
- repeated handshake/session setup;
- fixed-size encrypted echo;
- hostname mismatch and untrusted-certificate rejection gates;
- cancellation during handshake and cleanup.

Certificate and hostname verification must remain enabled.

## Candidate D — real-world provider pipeline

**Status: PLANNED**

Application reference: `harry0703/MoneyPrinterTurbo`.

Do **not** port the full application. Extract a compact workload that exercises the same engineering shape:

1. parse deterministic configuration;
2. select a provider from a declarative registry;
3. issue a local HTTP/TLS request to a fixture server;
4. parse the response;
5. write a deterministic result file;
6. optionally invoke one bounded local process where S3 process APIs support it.

This candidate should follow the lower-level runtime/network/TLS gates.

## Candidate E — AArch64 backend structure and code quality

**Status: NEXT STRUCTURAL CANDIDATE**

Primary reference: `llvm/llvm-project`.

This is not a claim that S3 and LLVM have equivalent optimizer scope. The comparison must use bounded kernels with equivalent semantics.

Candidate checks:

- AArch64 function-call ABI fixtures;
- integer and floating argument/return placement;
- aggregate/sret layout;
- stack alignment;
- ELF structural validity for Linux AArch64;
- Mach-O structural validity for macOS ARM64;
- instruction count and code size for tiny arithmetic/control-flow kernels.

Execution timing is valid only on a real matching target environment. Structural checks must be reported separately from execution certification.

## Candidate F — package resolver, cache and reproducibility

**Status: PLANNED**

Primary references: `rust-lang/cargo`, `astral-sh/uv`.

Candidate workloads:

- resolve a deterministic local dependency graph;
- identical multi-parent dependency identity;
- conflicting identity rejection;
- lockfile regeneration determinism;
- warm-cache vs cold-cache local fixture resolution;
- offline cache hit;
- checksum mismatch rejection;
- bounded archive extraction/path traversal rejection;
- repeat toolchain/package bundle hash comparison.

Do not use live public registries for correctness. Use a local fixture registry/content store.

## Promotion order from here

1. validate the three promoted correctness preflights;
2. AArch64 structural/code-quality campaign;
3. package resolver/cache/reproducibility;
4. real-world provider pipeline;
5. native performance only where an equivalent S3 execution path exists.

No hosted Python timing should be presented as native S3 performance.
