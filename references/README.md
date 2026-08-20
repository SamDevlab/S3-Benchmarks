# External Reference Corpus

This directory records external projects used to design and review S3 benchmark campaigns.

## Policy

- **CORRECTNESS BEFORE PERFORMANCE** remains the repository-wide rule.
- Every external reference used by a campaign must be pinned to an immutable commit SHA.
- Reference repositories are **not** benchmark results and are **not** automatically copied or vendored into this repository.
- A performance comparison is valid only after S3 and the chosen oracle/reference implementation have an explicitly defined equivalent workload and pass the differential correctness gate.
- Network/TLS benchmarks must use local fixtures or loopback services by default; public internet access must not be required for correctness.
- Structural platform evidence must not be relabeled as native execution evidence.
- Tested source SHAs and canonical merge SHAs are separate provenance facts when they differ.

## M1.71-M1.80 corpus

See [`upstreams-m171-m180.json`](upstreams-m171-m180.json).

This historical corpus remains pinned to its original S3 baseline and is not repinned when later milestones merge.

Primary references include Rust, Tokio, Mio, rustls, libuv, LLVM, Cargo and uv. MoneyPrinterTurbo is tracked as a bounded real-world workload shape rather than a compiler oracle.

## M1.81-M1.90 corpus

See [`upstreams-m181-m190.json`](upstreams-m181-m190.json).

Canonical merged S3 baseline:

`a9e430551f2ee77aa2ef229daf9e967333e83e2c`

Reviewed/tested PR #183 head:

`8742010f7c7a7956733dd35fabb6a6ef731d0b0b`

The M1.81-M1.90 corpus adds/extends references for:

- Rust — resumable async IR, move-only futures and async generics;
- Tokio/Mio/libuv — bounded multithread executor, process I/O and networking;
- Hyper + rustls — HTTP/1.1 and secure HTTPS/TLS behavior;
- Cargo + uv — HTTPS registry/cache and reproducible package/distribution workflows;
- `pyca/cryptography` — vetted Ed25519 provider boundary;
- LLVM — typed AAPCS64, ELF/Mach-O and ARM64 object/link structure.

The historical executable campaign at `fbf53a0eb8cf39ed0245438b6b47dfde63658b20` is retained as evidence only. The merged S3 benchmark-applicability report says post-review hardening requires focused reruns before old characterization is attributed to the newer source line, so the canonical merge receives a new correctness run rather than an inherited PASS.

## Promotion into an executable benchmark

A candidate should be treated as publishable benchmark evidence only when all of these exist:

1. a bounded workload definition;
2. immutable upstream and S3 commit pins;
3. deterministic fixtures;
4. an oracle or equivalence contract;
5. differential correctness checks;
6. a timing methodology that does not use synthetic timing;
7. machine-readable and Markdown reports;
8. no unresolved provenance mismatch between tested code, merged code and measured code.
