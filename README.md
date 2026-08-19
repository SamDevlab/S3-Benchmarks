# S3 Language External Benchmarks

This repository (**`SamDevlab/S3-Benchmarks`**) is an independent, reproducible, and technically rigorous benchmark suite for evaluating real-world workloads compiled with the S3 programming language compiler (`SamDevlab/S3`).

## Fundamental Rule

> **CORRECTNESS BEFORE PERFORMANCE.**
> No performance result is valid unless the reference implementation and S3 produce 100% semantically equivalent observable behavior under the campaign's explicit equivalence contract.

## Executable Workloads

- [`benchmarks/jsmn`](benchmarks/jsmn/README.md): Upstream C `zserge/jsmn` vs S3 behavioral port kernel.

## Candidate Benchmark Corpus

The repository now tracks a pinned external reference corpus for the post-M1.80 benchmark program:

- [`references/upstreams-m171-m180.json`](references/upstreams-m171-m180.json): immutable upstream pins and milestone mapping.
- [`references/README.md`](references/README.md): policy for promoting external projects into reproducible S3 benchmark campaigns.
- [`candidates/m171-m180`](candidates/m171-m180/README.md): bounded candidate campaigns for async/runtime, reactor/networking, TLS, AArch64, package resolution/reproducibility, and a real-world provider pipeline.

The current references are Rust, Tokio, Mio, rustls, libuv, LLVM, Cargo, and uv. MoneyPrinterTurbo is tracked only as a future real-world workload shape; it is not treated as a compiler oracle and is not vendored into this repository.

## Execution

```bash
# Differential correctness check
python tools/runner.py --verify-only

# Benchmark smoke test
python tools/runner.py --smoke

# Full statistical benchmark suite
python tools/runner.py --full
```

The commands above currently execute the JSMN campaign only. Candidate campaigns must not be presented as benchmark results until their own correctness/structural-equivalence harnesses exist.

## CI Integration

GitHub Actions workflow `.github/workflows/tests.yml` enforces automated verification on every push and PR for the currently executable suite.
