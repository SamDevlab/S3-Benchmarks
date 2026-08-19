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

## Promotion order

Recommended order:

1. async executor/channels;
2. reactor/loopback networking;
3. TLS local handshake;
4. real-world provider pipeline.

Do not promote all four at once. Each candidate becomes executable only after its differential correctness contract is complete.
