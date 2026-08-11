# JSMN Workload Benchmark

This directory contains the comparative benchmark suite for **JSMN JSON Tokenizer**.

## Subdirectories

- `upstream/`: Upstream C reference (`zserge/jsmn`, pinned commit `25647e692c7906b96ffd2b05ca54c097948e879c`).
- `s3/`: S3 behavioral kernel (`jsmn_demo.s3`, pinned commit `85541b782571c80d4857d013d1fb25b4997c1eb9`).
- `corpus/`: Representative JSON fixtures (`tiny/`, `small/`, `medium/`, `large/`, `generated/`).
- `harness/`: Differential correctness, statistical timing, and benchmarking modules.
- `results/`: Output benchmark results.

## Execution

```bash
python tools/runner.py --smoke
```
