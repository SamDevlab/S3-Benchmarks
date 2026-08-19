# S3 Language External Benchmarks

This repository (**`SamDevlab/S3-Benchmarks`**) is an independent, reproducible, and technically rigorous benchmark suite for evaluating real-world workloads compiled with the S3 programming language compiler (`SamDevlab/S3`).

## Fundamental Rule

> **CORRECTNESS BEFORE PERFORMANCE.**
> No performance result is valid unless the reference implementation and S3 produce 100% semantically equivalent observable behavior under the campaign's explicit equivalence contract.

## Executable Workloads

- [`benchmarks/jsmn`](benchmarks/jsmn/README.md): Upstream C `zserge/jsmn` vs S3 behavioral port kernel. Differential correctness + native performance campaign.
- [`benchmarks/async_runtime`](benchmarks/async_runtime/README.md): M1.71-M1.76 async-runtime behavioral correctness preflight. Performance intentionally deferred.
- [`benchmarks/network_loopback`](benchmarks/network_loopback/README.md): M1.73/M1.74 reactor + deterministic local network correctness preflight. No public internet and no network performance claims yet.
- [`benchmarks/tls_local`](benchmarks/tls_local/README.md): M1.75 local TLS state-machine correctness preflight with certificate/hostname validation locked on. No public internet and no TLS performance claims yet.
- [`benchmarks/aarch64`](benchmarks/aarch64/README.md): M1.77/M1.78 Linux AArch64 + macOS ARM64 structural conformance preflight. LLVM is pinned as an architecture/codegen reference, but comparative code quality and execution timing remain explicitly invalid/deferred.
- [`benchmarks/package_repro`](benchmarks/package_repro/README.md): M1.56/M1.79/M1.80 package resolver, content-addressed cache, archive-safety, and reproducible toolchain-bundle correctness preflight. Cargo and uv are pinned references only; resolver performance remains deferred.
- [`benchmarks/provider_pipeline`](benchmarks/provider_pipeline/README.md): MoneyPrinterTurbo-inspired application integration preflight using S3 OS services + async network + async TLS against deterministic local fixtures. No real providers, secrets, public internet, or performance claims.

## Candidate Benchmark Corpus

The repository tracks a pinned external reference corpus for the post-M1.80 benchmark program:

- [`references/upstreams-m171-m180.json`](references/upstreams-m171-m180.json): immutable upstream pins and milestone mapping.
- [`references/README.md`](references/README.md): policy for promoting external projects into reproducible S3 benchmark campaigns.
- [`candidates/m171-m180`](candidates/m171-m180/README.md): bounded candidate campaigns and promotion state.

The current references are Rust, Tokio, Mio, rustls, libuv, LLVM, Cargo, uv, and MoneyPrinterTurbo. MoneyPrinterTurbo is used only as an application-architecture/workload-shape reference; its code is not vendored and its external provider integrations are not executed.

## Execution

```bash
# JSMN differential correctness check
python tools/runner.py --verify-only

# M1.71-M1.76 async-runtime correctness
S3_CURRENT_REPO=/path/to/S3 python tools/async_runtime_runner.py --verify-only

# M1.73/M1.74 reactor + local network correctness
S3_CURRENT_REPO=/path/to/S3 python tools/network_loopback_runner.py --verify-only

# M1.75 local TLS correctness
S3_CURRENT_REPO=/path/to/S3 python tools/tls_local_runner.py --verify-only

# M1.77/M1.78 ARM64 structural conformance
S3_CURRENT_REPO=/path/to/S3 python tools/aarch64_runner.py --verify-only

# M1.56/M1.79/M1.80 package/cache/reproducibility correctness
S3_CURRENT_REPO=/path/to/S3 python tools/package_repro_runner.py --verify-only

# MoneyPrinterTurbo-inspired local provider pipeline integration correctness
S3_CURRENT_REPO=/path/to/S3 python tools/provider_pipeline_runner.py --verify-only

# JSMN benchmark smoke test
python tools/runner.py --smoke

# JSMN full statistical benchmark suite
python tools/runner.py --full
```

The M1.71-M1.80 async/network/TLS/ARM64/package/provider-pipeline workloads currently emit **correctness, structural, or integration evidence only**. Their runners enforce the pinned S3 baseline `cd6804f72757d6936ca1ec6c20d5badf55d1aac4`.

The provider-pipeline gate also verifies the MoneyPrinterTurbo reference pin `d4c0e45da4ac0889af77f7307f52f9d5d4f74942`. Its first version uses Python JSON parsing inside the benchmark harness and reports that limitation explicitly; it must not be treated as evidence of a production S3 JSON runtime.

## CI Integration

GitHub Actions workflow `.github/workflows/tests.yml` keeps the historical JSMN S3 pin separate from the M1.71-M1.80 correctness baseline. This prevents a newer compiler from silently rewriting historical benchmark provenance while allowing the newer gates to be verified independently.
