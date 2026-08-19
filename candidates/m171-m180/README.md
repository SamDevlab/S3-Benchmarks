# M1.71-M1.80 Benchmark Candidates

The current S3 baseline is `SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`.

## Candidate A — async executor and channels

**Correctness preflight: PROMOTED** → [`benchmarks/async_runtime`](../../benchmarks/async_runtime/README.md)

Primary references: `rust-lang/rust`, `tokio-rs/tokio`.

Performance remains deferred until a native S3 workload with equivalent observable semantics exists.

## Candidate B — reactor and loopback networking

**Correctness preflight: PROMOTED** → [`benchmarks/network_loopback`](../../benchmarks/network_loopback/README.md)

Primary references: `tokio-rs/mio`, `libuv/libuv`.

The promoted preflight verifies deterministic reactor and provider-neutral local-network semantics without public internet. Native socket/reactor performance remains deferred.

## Candidate C — TLS local handshake

**Correctness preflight: PROMOTED** → [`benchmarks/tls_local`](../../benchmarks/tls_local/README.md)

Primary reference: `rustls/rustls`.

The promoted preflight validates the provider-neutral TLS state machine and secure defaults. It does not claim native TLS, trust-store, or external-chain execution certification.

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

**Structural correctness preflight: PROMOTED** → [`benchmarks/aarch64`](../../benchmarks/aarch64/README.md)

Primary reference: `llvm/llvm-project` pinned at `b562ef546e46face7172d174e1a5f5454c470eee`.

The promoted gate currently validates only the contracts actually modeled by S3 M1.77/M1.78:

- target registration;
- AAPCS64 scalar integer argument locations;
- scalar return in `x0`;
- deterministic structural return assembly;
- ELF64 AArch64 identity;
- Mach-O ARM64 executable-header identity;
- execution-certification deferment;
- fail-closed invalid inputs.

The gate explicitly records the following as unmodeled rather than inferring support:

- floating-point ABI classification;
- explicit 16-byte stack-alignment proof;
- aggregate argument/return and `sret`;
- ELF sections/relocations;
- Mach-O load commands/sections/relocations;
- machine-code encoding;
- native link/execution.

Therefore LLVM remains a pinned architecture/codegen reference only. Comparative instruction-count/code-size claims and execution timing are invalid until S3 has equivalent native object generation and execution paths.

## Candidate F — package resolver, cache and reproducibility

**Status: NEXT CANDIDATE**

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

1. validate the four promoted M1.71-M1.78 correctness/structural preflights;
2. package resolver/cache/reproducibility;
3. real-world provider pipeline;
4. native performance/code-quality only where an equivalent S3 native path exists.

No hosted Python timing or structural-only output should be presented as native S3 performance.
