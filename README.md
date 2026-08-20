# S3 Language External Benchmarks

This repository (**`SamDevlab/S3-Benchmarks`**) is an independent, reproducible, and technically rigorous benchmark suite for evaluating real-world workloads compiled with the S3 programming language compiler (`SamDevlab/S3`).

## Fundamental Rule

> **CORRECTNESS BEFORE PERFORMANCE.**
> No performance result is valid unless C and S3 produce 100% semantically equivalent output, status codes, and token attributes.

## Workloads

- [`benchmarks/jsmn`](benchmarks/jsmn/README.md): Upstream C `zserge/jsmn` vs S3 behavioral port kernel.
- [`benchmarks/experimental_provider`](benchmarks/experimental_provider/README.md): non-normative external-provider bridge for deterministic CPU/GPU/FFI experiments. It is isolated from official baselines and CI performance gates.

## Execution

```bash
# Differential correctness check
python tools/runner.py --verify-only

# Benchmark smoke test
python tools/runner.py --smoke

# Full statistical benchmark suite
python tools/runner.py --full
```

Experimental provider bridge:

```bash
python tools/experimental_provider_runner.py --list
python tools/experimental_provider_runner.py --verify-only
```

## CI Integration

GitHub Actions workflow `.github/workflows/tests.yml` enforces automated verification on every push and PR.

The experimental external-provider bridge is intentionally **not** part of the normative CI performance gate. Its bundled provider is only a protocol fixture.
