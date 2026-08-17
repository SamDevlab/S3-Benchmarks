# S3 Language External Benchmarks

This repository (**`SamDevlab/S3-Benchmarks`**) is an independent, reproducible, and technically rigorous benchmark suite for evaluating real-world workloads compiled with the S3 programming language compiler (`SamDevlab/S3`).

## Fundamental Rule

> **CORRECTNESS BEFORE PERFORMANCE.**
> No performance result is valid unless C and S3 produce 100% semantically equivalent output, status codes, and token attributes.

## Workloads

- [`benchmarks/jsmn`](benchmarks/jsmn/README.md): Upstream C `zserge/jsmn` vs S3 behavioral port kernel.

## S3 Compiler Checkout

The benchmark runner does not use machine-specific fallback paths. It resolves the S3 compiler checkout in this order:

1. `S3_REPO`, when explicitly set;
2. `./s3-compiler`, relative to the root of this repository.

The path must point to the root of a valid `SamDevlab/S3` checkout containing `bootstrap/s3`. If neither location is valid, the runner exits with an explicit setup error instead of silently selecting another checkout.

For a checkout matching the compiler revision currently pinned by CI:

```bash
git clone https://github.com/SamDevlab/S3.git s3-compiler
git -C s3-compiler checkout 85541b782571c80d4857d013d1fb25b4997c1eb9
```

Alternatively, point to an existing checkout explicitly.

Linux/macOS:

```bash
export S3_REPO=/path/to/S3
```

PowerShell:

```powershell
$env:S3_REPO = "C:\path\to\S3"
```

GitHub Actions performs a pinned S3 checkout under `./s3-compiler` and passes that same location through `S3_REPO`, so CI never depends on a developer workstation path.

## Execution

```bash
# Differential correctness check
python tools/runner.py --verify-only

# Benchmark smoke test
python tools/runner.py --smoke

# Full statistical benchmark suite
python tools/runner.py --full
```

## CI Integration

GitHub Actions workflow `.github/workflows/tests.yml` enforces automated verification on every push and PR.
