# Real-world Benchmark Candidates v1

These are **candidate campaigns**, not published benchmark results.

Reference pins: [`references/upstreams-realworld-v1.json`](../../references/upstreams-realworld-v1.json).

The candidate program is designed to answer two different questions without conflating them:

1. **Can S3 implement the workload correctly and reproducibly?**
2. **If both sides are truly equivalent and native, how does performance compare?**

The first question must be answered before the second is even eligible.

## Promotion stages

Every candidate moves through the same explicit stages:

- **A — CORRECTNESS REFERENCE:** deterministic fixtures and observable equivalence contract.
- **B — INTEGRATION:** the bounded S3 workload exercises the intended runtime/compiler surface.
- **C — CHARACTERIZATION_ONLY:** local timing/resource observations may be recorded, but no comparative claim is allowed.
- **D — NATIVE EQUIVALENCE:** both S3 and reference execute equivalent native workloads in a controlled environment.
- **E — NATIVE_COMPARATIVE:** correctness is green, toolchain/environment policy is satisfied, and speedup/slowdown claims become eligible.

A stage may remain `DEFERRED_BY_ENVIRONMENT` without being relabeled as PASS or FAIL.

## Candidate A — large JSON parsing (`simdjson`)

Reference: `simdjson/simdjson`.

Bounded workload:

- pinned local JSON fixtures: flat, nested, arrays, strings/escapes, numeric boundaries and malformed inputs;
- identical accepted/rejected corpus;
- observable result is canonical digest/counts, not implementation internals;
- no public network.

Correctness gates:

- canonical parsed-value digest matches;
- malformed-input verdicts match the explicit campaign contract;
- bounded memory/input-size policy is enforced;
- S3 O0/O1 and native output agree before reference timing.

Future metrics after native equivalence:

- documents/s and bytes/s;
- median/p95 latency per fixture class;
- peak RSS;
- native code size/instruction count where meaningful.

## Candidate B — compression/streaming (`zstd`)

Reference: `facebook/zstd`.

Bounded workload:

- deterministic text/binary fixture set;
- compress and decompress at one explicitly pinned level/configuration;
- streaming chunks with bounded capacities;
- checksum and original-byte equality are correctness gates.

Do not compare different compression levels, dictionaries, CPU features or window sizes under one headline number.

Future metrics:

- compression MB/s;
- decompression MB/s;
- compressed size;
- peak memory;
- streaming backpressure behavior.

## Candidate C — local database application shape (SQLite)

Reference: `sqlite/sqlite` GitHub mirror for design only.

Before executable comparative promotion, pin an explicit SQLite release/Fossil source identity.

Bounded workload:

- create one local temporary database;
- deterministic schema;
- fixed insert batch;
- indexed and non-indexed reads;
- deterministic transaction/rollback case;
- close/reopen durability check;
- no external services.

Initial S3 value is **application integration**, even before it has an equivalent embedded SQL engine. A wrapper around SQLite must not be advertised as S3-vs-SQLite compiler performance.

## Candidate D — HTTP parser/framing (`llhttp`)

Reference: `nodejs/llhttp`.

Bounded workload:

- deterministic HTTP/1.1 request and response corpus;
- header limits;
- Content-Length framing;
- malformed lines and injected-header cases;
- parser stop/error offsets where they are part of the explicit equivalence contract.

This campaign is separate from socket/TLS timing. Parser throughput must not include network variance.

## Candidate E — LLM client / agent pipeline

Reference shape: local OpenAI-compatible protocol; application inspiration may include MoneyPrinterTurbo, but no external provider is a correctness oracle.

This candidate is immediately useful for S3's current runtime capabilities.

Pipeline:

1. parse deterministic local config;
2. connect to a local fixture server;
3. send a bounded JSON request;
4. parse streaming SSE/token chunks;
5. enforce backpressure, timeout and cancellation;
6. write a deterministic result/cache file;
7. optionally invoke one bounded local process.

Correctness requires a deterministic local mock. No API key, paid service or public internet is allowed.

Metrics in characterization stage may include:

- time to first local mock chunk;
- chunk throughput;
- peak buffered bytes;
- cancellation latency;
- output digest;
- resource cleanup.

This tests S3 as an **LLM application/runtime language**, not as an inference engine.

## Candidate F — local LLM inference (`llama.cpp`)

Reference: `ggml-org/llama.cpp`.

Initial status: `REFERENCE_ONLY`; native comparative inference is deferred.

Executable campaign prerequisites:

- a small redistribution-compatible GGUF model or generated fixture with an immutable SHA-256;
- CPU-only mode initially;
- one thread initially, then an explicitly separate threaded campaign;
- deterministic/greedy generation settings;
- pinned prompt corpus;
- no network/model download during correctness or timing;
- tokenization/output contract defined before timing.

Correctness evidence must record:

- model digest;
- prompt digest;
- token IDs or another stable token-level oracle;
- generated token count;
- termination reason;
- S3/reference build and commit identities.

Potential native metrics after true equivalence:

- model-load time;
- prompt tokens/s;
- generation tokens/s;
- time to first token;
- peak RSS;
- binary/code size where meaningful.

A S3 wrapper that merely calls `llama.cpp` is an integration benchmark, **not** S3-native inference performance.

## Candidate G — real-world provider pipeline (MoneyPrinterTurbo shape)

Reference shape: `harry0703/MoneyPrinterTurbo`.

Do not port the whole application. Extract a small deterministic provider/config/network/output workflow. It is useful as a cross-subsystem workload after the LLM-client candidate is stable.

## S3 Laboratory integration

Each promoted benchmark should emit enough machine-readable provenance for the S3 Laboratory to consume it without guessing:

- S3 commit;
- benchmark-repository commit;
- upstream commit/data/model digest;
- workload id and schema;
- correctness status;
- evidence classification;
- environment/toolchain identity;
- timing class;
- native comparative validity;
- raw result digest where available.

The benchmark does not assign a vanity grade. The laboratory applies a versioned rubric from [`laboratory/`](../../laboratory/) and reports **score**, **coverage** and **confidence** separately.

## Recommended promotion order

1. HTTP parser/framing;
2. large JSON parsing;
3. LLM client / agent pipeline;
4. compression/streaming;
5. local database application shape;
6. real-world provider pipeline;
7. local LLM inference once native compute capabilities and a model fixture are ready.

Do not promote all candidates at once. Every promotion requires its own correctness contract and narrow review.
