# S3 Language External Benchmarks

This repository (**`SamDevlab/S3-Benchmarks`**) is an independent, reproducible, and technically rigorous benchmark suite for evaluating real-world workloads compiled with the S3 programming language compiler (`SamDevlab/S3`).

## Fundamental Rule

> **CORRECTNESS BEFORE PERFORMANCE.**
> No performance result is valid unless the reference implementation and S3 produce 100% semantically equivalent observable behavior under the campaign's explicit equivalence contract.

## Executable Workloads

- [`benchmarks/jsmn`](benchmarks/jsmn/README.md): upstream C `zserge/jsmn` vs S3 behavioral port kernel.
- [`benchmarks/m181_m190`](benchmarks/m181_m190/README.md): executable post-M1.80 correctness-first campaign; timing remains characterization-only unless an equivalent pinned native reference exists.
- [`benchmarks/m199`](benchmarks/m199/README.md): M1.99 schema-v2 correctness and hosted characterization with hard Git provenance pins.

## Candidate Benchmark Corpus

The repository tracks immutable upstream references and bounded candidate campaigns. A reference entry is not itself a benchmark result.

Existing post-M1.80 material:

- [`references/upstreams-m171-m180.json`](references/upstreams-m171-m180.json): immutable upstream pins and milestone mapping.
- [`candidates/m171-m180`](candidates/m171-m180/README.md): async/runtime, reactor/networking, TLS, AArch64, package-resolution/reproducibility, and provider-pipeline candidates.

New real-world / M2.x material:

- [`references/upstreams-realworld-v1.json`](references/upstreams-realworld-v1.json): immutable snapshot for `llama.cpp`, `simdjson`, `zstd`, SQLite's GitHub mirror, `llhttp`, and MoneyPrinterTurbo.
- [`candidates/realworld-v1`](candidates/realworld-v1/README.md): bounded JSON, compression, SQLite, HTTP-parser, LLM-client, LLM-inference, and real-world application campaigns.
- [`laboratory`](laboratory/README.md): evidence-to-score bridge for the S3 Laboratory. Benchmarks produce evidence; the laboratory applies a versioned rubric and never manufactures benchmark results.

The real-world corpus is deliberately staged. `llama.cpp` may be pinned now as an LLM inference reference while S3-native comparative inference remains deferred until the S3 workload is genuinely equivalent and runs natively under a controlled protocol.

## Evidence Classes

Benchmark outputs must identify their class explicitly:

1. `CORRECTNESS` — deterministic observable equivalence or a structural contract.
2. `INTEGRATION` — bounded application pipeline behavior.
3. `CHARACTERIZATION_ONLY` — timing or resource observations that are not comparative performance evidence.
4. `NATIVE_COMPARATIVE` — equivalent native workloads, same controlled environment/toolchain policy, correctness gate passed first.
5. `DEFERRED` — a required environment/capability is unavailable; never relabel as PASS.

Only `NATIVE_COMPARATIVE` evidence may support a speedup/slowdown claim.

## Execution

```bash
# Differential correctness check for the currently promoted suite
python tools/runner.py --verify-only

# Benchmark smoke test
python tools/runner.py --smoke

# Full statistical benchmark suite for promoted workloads
python tools/runner.py --full
```

The generic runner still executes only workloads that have been explicitly promoted into its executable registry. Candidate corpus entries must not be presented as benchmark results until their correctness/structural-equivalence harnesses exist.

## CI Integration

GitHub Actions workflow `.github/workflows/tests.yml` enforces automated verification on every push and PR for the currently executable suite.
