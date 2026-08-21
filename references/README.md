# External Reference Corpus

This directory records external projects used to design and review future S3 benchmark campaigns.

## Policy

- **CORRECTNESS BEFORE PERFORMANCE** remains the repository-wide rule.
- Every external reference used by a campaign must be pinned to an immutable commit SHA.
- Reference repositories are **not** benchmark results and are **not** automatically copied or vendored into this repository.
- A performance comparison is valid only after S3 and the chosen oracle/reference implementation have an explicitly defined equivalent workload and pass the differential correctness gate.
- Network/TLS/LLM-client correctness must use local fixtures or loopback services by default; public internet access and paid APIs must not be required.
- Large projects may be used as architecture or workload references without attempting a full-language port.
- Models, databases and other large data artifacts require their own immutable digest before they can participate in executable evidence.
- `DEFERRED`, `STRUCTURAL_ONLY`, and `CHARACTERIZATION_ONLY` are evidence classes, not failures and not PASS aliases.

## Current post-M1.80 corpus

See [`upstreams-m171-m180.json`](upstreams-m171-m180.json).

The pinned research set includes Rust, Tokio, Mio, rustls, libuv, LLVM, Cargo and uv for async/runtime, networking/TLS, native backend, package identity and reproducibility work.

## Real-world corpus v1

See [`upstreams-realworld-v1.json`](upstreams-realworld-v1.json).

The new pinned snapshot expands coverage in six directions:

- `ggml-org/llama.cpp` — future CPU-only LLM inference reference; initially reference/integration only, with native comparative inference deferred until S3 has an equivalent workload.
- `simdjson/simdjson` — JSON parsing, branch behavior, buffer traversal and future native throughput comparison.
- `facebook/zstd` — streaming compression/decompression, checksums, bounded buffers and memory-intensive loops.
- `sqlite/sqlite` — local storage/query workload shape using the GitHub mirror; executable comparative provenance must be rebound to an explicit SQLite release/Fossil source identity before promotion.
- `nodejs/llhttp` — HTTP parsing/framing reference for bounded request/response parser workloads.
- `harry0703/MoneyPrinterTurbo` — real-world provider/config/network pipeline shape only; not a compiler oracle.

No project above is vendored by this manifest. The immutable SHA records only the reference snapshot reviewed for candidate design.

## Promotion into an executable benchmark

A candidate moves into `benchmarks/` only when all of these exist:

1. a bounded workload definition;
2. immutable upstream, S3 and benchmark-repository commit pins;
3. deterministic fixtures and, where relevant, immutable data/model digests;
4. an independent oracle or explicit equivalence contract;
5. differential correctness checks before timing;
6. a timing methodology that uses real execution rather than synthetic timings;
7. explicit environment/toolchain metadata;
8. machine-readable and Markdown reports;
9. an evidence classification (`CORRECTNESS`, `INTEGRATION`, `CHARACTERIZATION_ONLY`, `NATIVE_COMPARATIVE`, or `DEFERRED`);
10. a rule forbidding speedup claims unless native comparative validity is explicitly proven.

The S3 Laboratory may consume these benchmark artifacts, but scoring logic belongs under [`laboratory/`](../laboratory/), not inside workload runners.
