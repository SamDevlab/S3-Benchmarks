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

**Integration correctness preflight: PROMOTED** → [`benchmarks/provider_pipeline`](../../benchmarks/provider_pipeline/README.md)

Application reference: `harry0703/MoneyPrinterTurbo` pinned at `d4c0e45da4ac0889af77f7307f52f9d5d4f74942`.

The promoted V1 workload extracts only the useful application shape rather than porting the full project:

1. deterministic config file read through S3 OS services;
2. stable provider-ID lookup in a benchmark-local declarative registry;
3. default/explicit model resolution;
4. deterministic local DNS and async network connect;
5. async TLS handshake/read/write with certificate and hostname validation required;
6. deterministic HTTP-like request envelope;
7. local fixture provider response;
8. response parse;
9. deterministic result-file write/readback through S3 OS services;
10. cleanup after success and after a late output-path failure.

The gate additionally proves that an unknown provider fails before network activity starts and that `../` output escape is rejected.

### Explicit V1 limitation

JSON parsing/serialization is provided by the Python benchmark harness because the pinned M1.71-M1.80 S3 baseline does not expose a general JSON runtime for this workload. The report labels this as:

`python_benchmark_harness_not_s3_runtime_feature`

Therefore this candidate is an integration/workload-shape gate, not evidence that S3 already has a production JSON library.

No real AI provider, API key, public internet, or MoneyPrinterTurbo runtime is used.

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

## Promotion state

All six M1.71-M1.80 candidates are now represented by bounded executable correctness/structural/integration preflights:

1. async runtime;
2. reactor/network;
3. TLS;
4. provider application pipeline;
5. AArch64 structure;
6. package/cache/reproducibility.

The next benchmark-program step should **not** silently repin these workloads to code under active M1.81-M1.90 development. Add a separate immutable M1.81-M1.90 reference/baseline only after that roadmap is merged and reviewed.

Native performance/code-quality comparisons remain allowed only where an equivalent native S3 execution path and an explicit correctness/equivalence contract exist. No hosted Python timing or structural-only output should be presented as native S3 performance.
