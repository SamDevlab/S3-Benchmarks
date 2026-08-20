# M1.81-M1.90 Benchmark Candidate Corpus

This corpus is pinned to the merged M1.81-M1.90 S3 line and is separate from the historical M1.71-M1.80 baseline.

## Provenance

- previous canonical S3 main: `cd6804f72757d6936ca1ec6c20d5badf55d1aac4`
- reviewed/tested PR #183 head: `8742010f7c7a7956733dd35fabb6a6ef731d0b0b`
- canonical merged main: `a9e430551f2ee77aa2ef229daf9e967333e83e2c`
- historical M1.81-M1.90 benchmark campaign commit: `fbf53a0eb8cf39ed0245438b6b47dfde63658b20`

The tested PR head and the merge commit are different provenance facts. The merge commit must not be presented as the historical tested SHA.

The existing `BENCHMARK_APPLICABILITY.md` in merged S3 explicitly says post-review hardening requires focused correctness/smoke reruns before historical characterization is attributed to the newer source head. Therefore the old campaign is retained as evidence, but the new corpus requires a clean rerun against the canonical merged baseline.

## Corpus files

- [`../../references/upstreams-m181-m190.json`](../../references/upstreams-m181-m190.json) — immutable upstream/reference pins and S3 provenance.
- [`../../benchmarks/m181_m190/corpus.json`](../../benchmarks/m181_m190/corpus.json) — machine-readable workload definitions and promotion state.
- [`../../benchmarks/m181_m190`](../../benchmarks/m181_m190/README.md) — existing executable campaign harness inherited from the pre-merge campaign.

## Candidate 1 — M1.81 resumable async IR

Current harness: `async_task`.

Required canonical-baseline gate:

- suspended → resumed → completed state progression;
- exact final value;
- bounded poll count;
- deterministic repeated execution;
- cancellation/drop correctness remains a prerequisite before timing.

Reference: `rust-lang/rust`.

## Candidate 2 — M1.81/M1.82 await chain + move-only Future

Current harness: `await_chain`.

Expand the gate to include:

- multiple async functions;
- move-only `Future<T>` ownership transfer;
- double-consume/double-poll misuse rejection where applicable;
- deterministic async generic specialization identity;
- module-boundary async dispatch.

Reference: `rust-lang/rust`.

## Candidate 3 — M1.83 bounded multithread executor and channels

Current harnesses: `executor`, `channels`.

Channels remain parameterized at capacities `1`, `8`, and `64`.

Canonical-baseline correctness must cover:

- atomic capacity admission;
- no more than one active poll owner per task;
- deferred wake without lost wakeups;
- serialized cancellation;
- FIFO/count/checksum/close-state channel contracts;
- capacity reuse after task completion.

Reference: `tokio-rs/tokio`.

## Candidate 4 — M1.84 bounded async filesystem/process I/O

Current harness: `process_io`.

Expand from the current successful child-process case to:

- stdout and stderr streaming limits;
- timeout → kill → reap;
- output overflow → kill → reap;
- deterministic exit status;
- bounded filesystem read/write fixtures;
- cleanup after partial failure.

References: `tokio-rs/tokio`, `libuv/libuv`.

## Candidate 5 — M1.85 HTTP/1.1 loopback

Current harness: `http_loopback`.

Promote only after the final hardened contracts are exercised:

- ASCII request-boundary validation;
- one monotonic global deadline covering the entire request;
- Content-Length/body bounds;
- malformed framing rejection;
- deterministic connection cleanup;
- localhost fixture only.

References: `hyperium/hyper`, Tokio/Mio.

## Candidate 6 — M1.85 HTTPS/TLS local fixture

Current harness: `tls_policy` only.

This is **not yet a real handshake benchmark**. Add a local CA/certificate fixture and verify:

- successful trusted hostname-matching handshake;
- hostname mismatch rejection;
- untrusted certificate rejection;
- certificate + hostname verification cannot be disabled;
- deadline and cleanup behavior.

Reference: `rustls/rustls`.

No public internet may be required.

## Candidate 7 — M1.86 HTTPS content-addressed registry

Current harness: `registry_cache`.

Expand to cover the final hardened implementation:

- HTTPS-only transport;
- canonical lowercase registry-origin identity;
- malformed alias rejection;
- digest verification before cache admission;
- verified cache hit;
- corrupted cache/object rejection;
- bounded local registry fixture.

References: `rust-lang/cargo`, `astral-sh/uv`, rustls.

## Candidate 8 — M1.87 Ed25519 verification

Current harness: `signature`.

The production crypto boundary is the optional vetted `cryptography` provider. The gate must never add a home-grown crypto fallback.

Required cases:

- valid signature PASS;
- tampered payload FAIL;
- wrong key FAIL;
- malformed signature FAIL;
- missing provider → explicit DEFERRED, never a fabricated PASS.

Reference: `pyca/cryptography`.

## Candidate 9 — M1.88 Linux AArch64

Current harness: `aarch64_structure`.

The final M1.88 corpus must add the post-review typed AAPCS64 cases:

- integer parameters/results;
- `f64` parameters/results/constants/moves;
- mixed integer/floating signatures;
- object/link-plan structural validity;
- artifact hash binding;
- native executable hash, target/toolchain identity, exit code and scalar result when a real Linux AArch64 environment is available.

Reference: `llvm/llvm-project`.

Structural PASS is not native execution PASS.

## Candidate 10 — M1.89 macOS ARM64

No dedicated current harness exists yet; this is a required corpus addition.

Validate:

- macOS ARM64 target identity;
- typed ABI contracts;
- Mach-O object/link-plan structure;
- deterministic structural artifact;
- native result evidence only on a real compatible macOS ARM64 environment.

Reference: `llvm/llvm-project`.

## Candidate 11 — M1.90 release-candidate certification

Current harness `reproducibility` is a useful precursor, but the final M1.90 gate must target the release-candidate matrix rather than only the older toolchain bundler.

Required observable contracts:

- repeated builds are byte-identical;
- exact manifest membership;
- canonical paths and duplicate rejection;
- bounded file count and uncompressed bytes;
- strict manifest schema;
- mandatory Apache-2.0 material bound into verification;
- checksum and size verification;
- corruption fails closed;
- certification records distinguish structural, provider-deferred, and native-execution evidence.

References: Cargo and uv as package/distribution engineering references.

## Promotion order

1. repin and rerun the existing correctness harness on `a9e430551f2ee77aa2ef229daf9e967333e83e2c`;
2. add post-review regression vectors for HTTP, registry, typed AArch64 and RC verification;
3. add real local HTTPS certificate fixtures;
4. run Ed25519 provider cases in an environment with `cryptography`;
5. add macOS ARM64 structural coverage;
6. collect native Linux AArch64/macOS ARM64 execution evidence only on matching hosts;
7. introduce comparative timing only after equivalent pinned reference executables exist.

`CORRECTNESS BEFORE PERFORMANCE` remains mandatory. Historical characterization must not be silently republished as measurements of the canonical merged baseline.
