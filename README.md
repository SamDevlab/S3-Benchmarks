# S3 Language External Benchmarks

This repository (**`SamDevlab/S3-Benchmarks`**) is an independent, reproducible, and technically rigorous benchmark suite for evaluating real-world workloads compiled with the S3 programming language compiler (`SamDevlab/S3`).

## Fundamental Rule

> **CORRECTNESS BEFORE PERFORMANCE.**
> No performance result is valid unless the reference implementation and S3 produce 100% semantically equivalent observable behavior under the campaign's explicit equivalence contract.

## Executable Workloads

- [`benchmarks/jsmn`](benchmarks/jsmn/README.md): Upstream C `zserge/jsmn` vs S3 behavioral port kernel. Differential correctness + native performance campaign.
- [`benchmarks/async_runtime`](benchmarks/async_runtime/README.md): M1.71-M1.76 async-runtime behavioral correctness preflight. **Performance is intentionally deferred** until an equivalent native S3 workload exists.

## Candidate Benchmark Corpus

The repository tracks a pinned external reference corpus for the post-M1.80 benchmark program:

- [`references/upstreams-m171-m180.json`](references/upstreams-m171-m180.json): immutable upstream pins and milestone mapping.
- [`references/README.md`](references/README.md): policy for promoting external projects into reproducible S3 benchmark campaigns.
- [`candidates/m171-m180`](candidates/m171-m180/README.md): bounded candidate campaigns for async/runtime, reactor/networking, TLS, AArch64, package resolution/reproducibility, and a real-world provider pipeline.

The current references are Rust, Tokio, Mio, rustls, libuv, LLVM, Cargo, and uv. MoneyPrinterTurbo is tracked only as a future real-world workload shape; it is not treated as a compiler oracle and is not vendored into this repository.

## Execution

```bash
# JSMN differential correctness check
python tools/runner.py --verify-only

# Async-runtime correctness preflight (requires current S3 checkout)
S3_CURRENT_REPO=/path/to/S3 python tools/async_runtime_runner.py --verify-only

# JSMN benchmark smoke test
python tools/runner.py --smoke

# JSMN full statistical benchmark suite
python tools/runner.py --full
```

The async-runtime workload currently emits correctness evidence only. It must not be presented as an async performance benchmark until the native-equivalence gate described in its README is satisfied.

## CI Integration

GitHub Actions workflow `.github/workflows/tests.yml` keeps the historical JSMN S3 pin separate from the current async-runtime S3 pin. This prevents a new compiler baseline from silently rewriting historical benchmark provenance while still verifying the new correctness workload on every push and PR.
