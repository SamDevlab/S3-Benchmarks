# M1.71-M1.80 Benchmark Candidates

These are **candidate campaigns**, not published benchmark results.

The current S3 baseline is `SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`.

## Candidate A — async executor and channels

Primary references: `rust-lang/rust`, `tokio-rs/tokio`.

Bounded workload ideas:

- create and complete N trivial cooperative tasks;
- chained await depth with equivalent observable result;
- timer wake scheduling with a deterministic/fake clock for correctness;
- bounded channel ping-pong with capacities 1, 8, and 64;
- cancellation/drop correctness before timing.

Metrics after correctness passes:

- ns/task completion;
- ns/channel message;
- generated code size where native comparison is meaningful;
- allocations or frame counts when the runtime exposes stable counters.

## Candidate B — reactor and loopback networking

Primary references: `tokio-rs/mio`, `libuv/libuv`.

Bounded workload ideas:

- localhost TCP connect/accept/read/write;
- UDP loopback send/receive;
- readiness re-arm after WouldBlock;
- fixed-size payload throughput;
- resource cleanup after cancellation/peer-close.

Public internet must not be required.

## Candidate C — TLS local handshake

Primary reference: `rustls/rustls`.

Bounded workload ideas:

- local trusted certificate handshake;
- repeated handshake/session setup;
- fixed-size encrypted echo;
- hostname mismatch and untrusted-certificate rejection as correctness gates;
- cancellation during handshake and cleanup.

Certificate and hostname verification must remain enabled. A benchmark that disables verification is invalid.

## Candidate D — real-world provider pipeline

Application reference: `harry0703/MoneyPrinterTurbo`.

Do **not** port the full application. Extract a compact workload that exercises the same engineering shape:

1. parse deterministic configuration;
2. select a provider from a declarative registry;
3. issue a local HTTP/TLS request to a fixture server;
4. parse the response;
5. write a deterministic result file;
6. optionally invoke one bounded local process where S3 process APIs support it.

This candidate is valuable as an integration benchmark after the lower-level async/network/TLS campaigns are stable.

## Candidate E — AArch64 backend structure and code quality

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

## Promotion order

Recommended order:

1. async executor/channels;
2. reactor/loopback networking;
3. TLS local handshake;
4. AArch64 structural/code-quality campaign;
5. package resolver/cache/reproducibility;
6. real-world provider pipeline.

Do not promote all candidates at once. Each candidate becomes executable only after its differential correctness or structural-equivalence contract is complete.
