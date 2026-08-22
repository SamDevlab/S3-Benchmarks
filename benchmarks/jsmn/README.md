# JSMN Workload Benchmark

This directory contains the comparative benchmark suite for **JSMN JSON Tokenizer**.

## Subdirectories

- `upstream/`: Upstream C reference (`zserge/jsmn`, pinned commit `25647e692c7906b96ffd2b05ca54c097948e879c`).
- `s3/`: S3 behavioral kernel (`jsmn_demo.s3`, pinned commit `85541b782571c80d4857d013d1fb25b4997c1eb9`).
- `corpus/`: Immutable representative JSON inputs (`tiny/`, `small/`, `medium/`, `large/`, `generated/`).
- `harness/`: Differential correctness, statistical timing, and benchmarking modules.
- `results/`: Output benchmark results.

## Execution

```bash
S3_REPO=/absolute/path/to/S3 \
S3_COMMIT=<full-s3-sha> \
BENCHMARK_REPO_COMMIT=<full-benchmark-sha> \
python tools/runner.py --smoke --run-id=<unique-run-id>
```

Every invocation receives a unique writable run root under `.artifacts/<run-id>`
(or `--artifact-root`). Generated C/S3 sources, assembly, objects,
executables, manifests, and reports are resolved only from that run root.
Completed run roots are never overwritten, and the runner fails closed when
either repository HEAD differs from its requested SHA. The tracked corpus and
all other static benchmark sources are read-only inputs.

## Evidence promotion policy

`PERFORMANCE_EVIDENCE_VALID` requires all of the following before timing can
be promoted to comparative evidence:

```text
CORRECTNESS_PASS
ARTIFACT_PROVENANCE_PASS
RUN_ISOLATION_PASS
ASSEMBLY_DETERMINISM_PASS
```

Stable expensive tests are independent of this policy. A native binary may
retain a weaker determinism contract when linker metadata prevents byte
identity; assembly bytes, `.text` bytes, structural metrics, and observable
execution must then be recorded explicitly.
