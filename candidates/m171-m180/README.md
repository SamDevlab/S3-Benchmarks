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

**Status: NEXT APPLICATION CANDIDATE**

Application reference: `harry0703/MoneyPrinterTurbo`.

Do **not** port the full application. Extract a compact workload that exercises the same engineering shape:

1. parse deterministic configuration;
2. select a provider from a declarative registry;
3. issue a local HTTP/TLS request to a fixture server;
4. parse the response;
5. write a deterministic result file;
6. optionally invoke one bounded local process where S3 process APIs support it.

This candidate should reuse the already-promoted async/network/TLS/package correctness gates rather than duplicating them.

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

**Correctness preflight: PROMOTED** → [`benchmarks/package_repro`](../../benchmarks/package_repro/README.md)

Primary references: `rust-lang/cargo`, `astral-sh/uv`.

The promoted gate uses local deterministic fixtures and verifies:

- package lock mapping-order determinism;
- identical multi-parent dependency identity;
- reachable identity conflict rejection;
- unreachable conflict isolation;
- stable lock SHA-256;
- exact content-addressed registry locks;
- offline cache reuse after registry-object removal;
- checksum verification on cache hits;
- deterministic install paths;
- archive traversal and duplicate canonical path rejection;
- bounded member extraction;
- byte-identical toolchain bundles across input order;
- deterministic manifest/ZIP metadata;
- corruption and machine-path rejection;
- registry publishing and remote release remain unavailable.

Cargo and uv remain pinned design/reference projects only. This preflight does not execute public registries or claim resolver performance equivalence.

## Promotion order from here

1. validate the five promoted M1.71-M1.80 correctness/structural preflights;
2. real-world provider pipeline inspired by MoneyPrinterTurbo;
3. native performance/code-quality only where an equivalent S3 native path exists;
4. add a separate immutable M1.81-M1.90 benchmark pin only after that roadmap is merged and reviewed.

No hosted Python timing or structural-only output should be presented as native S3 performance.
