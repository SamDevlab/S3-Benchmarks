# S3 Language External Benchmarks

This repository (**`SamDevlab/S3-Benchmarks`**) is an independent, reproducible, correctness-first benchmark suite for evaluating real-world workloads against the S3 programming language compiler (`SamDevlab/S3`).

## Fundamental Rule

> **CORRECTNESS BEFORE PERFORMANCE.**
> No performance result is valid unless S3 and the selected reference implementation have an explicitly equivalent observable workload and pass the campaign correctness gate first.

## Executable Workloads

- [`benchmarks/jsmn`](benchmarks/jsmn/README.md): upstream C `zserge/jsmn` vs S3 behavioral/native benchmark campaign.
- [`benchmarks/m181_m190`](benchmarks/m181_m190/README.md): M1.81-M1.90 correctness/characterization harness for async, channels, executor, process I/O, HTTP, registry/cache, reproducibility, TLS policy, Ed25519 and AArch64 structure.

## Immutable Benchmark Corpora

### M1.71-M1.80

- [`references/upstreams-m171-m180.json`](references/upstreams-m171-m180.json)
- [`candidates/m171-m180`](candidates/m171-m180/README.md)

The historical M1.71-M1.80 corpus keeps its original S3 provenance and must not be silently repinned to later compiler commits.

### M1.81-M1.90

Canonical merged S3 baseline:

`a9e430551f2ee77aa2ef229daf9e967333e83e2c`

Reviewed/tested PR #183 head:

`8742010f7c7a7956733dd35fabb6a6ef731d0b0b`

Corpus files:

- [`references/upstreams-m181-m190.json`](references/upstreams-m181-m190.json): immutable upstream pins plus tested-head/merge provenance.
- [`benchmarks/m181_m190/corpus.json`](benchmarks/m181_m190/corpus.json): machine-readable workload and evidence-status matrix.
- [`candidates/m181-m190`](candidates/m181-m190/README.md): required reruns/expansions for each M1.81-M1.90 capability.

The historical executable campaign commit `fbf53a0eb8cf39ed0245438b6b47dfde63658b20` remains preserved as historical evidence. Because the merged S3 benchmark-applicability report records post-review hardening after earlier characterization, the canonical merge requires fresh correctness/smoke execution before old measurements can be attributed to it.

## Reference Projects

The corpora pin only the projects relevant to each capability. The current union includes Rust, Tokio, Mio, libuv, Hyper, rustls, Cargo, uv, `pyca/cryptography`, LLVM, and the earlier MoneyPrinterTurbo workload reference.

Reference code is not automatically vendored or treated as a benchmark result. A pinned SHA defines what was studied or compared; it does not imply that the reference executable was built or run.

## Execution

```bash
# Historical JSMN differential correctness
python tools/runner.py --verify-only

# M1.81-M1.90 correctness against an explicit S3 checkout
S3_REPO=/path/to/S3 S3_COMMIT=a9e430551f2ee77aa2ef229daf9e967333e83e2c \
  python -m benchmarks.m181_m190.correctness --json

# M1.81-M1.90 smoke characterization only
S3_REPO=/path/to/S3 S3_COMMIT=a9e430551f2ee77aa2ef229daf9e967333e83e2c \
  python -m benchmarks.m181_m190.benchmark --smoke
```

Until a matching reference executable and equivalent workload exist, M1.81-M1.90 timing is **characterization only**, not comparative performance evidence.

## Evidence Rules

- public internet is not a correctness fixture;
- secrets/API keys are not required by benchmark correctness;
- missing optional Ed25519 provider is `DEFERRED`, not PASS;
- structural ARM64 validation is not native execution certification;
- tested SHA, measured SHA and canonical merge SHA are recorded separately;
- newer milestones receive new corpus pins rather than rewriting older results.
