# S3 M2.00 Progress Snapshot v1

This campaign measures how the current M2.00-era S3 candidate is behaving without treating slow certification tests as performance failures.

## Immutable comparison boundary

```text
BASELINE_S3_SHA=a9e430551f2ee77aa2ef229daf9e967333e83e2c
CANDIDATE_S3_SHA=a651e9b3551f218af1c27bb908e0692880afc4da
EXECUTABLE_BENCHMARK_SHA=c13f159bb19f13cac9e83e523b6e392baae71738
```

`BASELINE_S3_SHA` is the canonical M1.81-M1.90 merge boundary. `CANDIDATE_S3_SHA` is the immutable source HEAD used by the post-reboot M2.00 certification work before documentation-only updates. The benchmark harness is pinned independently so later laboratory documentation changes cannot silently alter executable methodology.

## Purpose

Answer four separate questions:

1. Does current S3 still satisfy the executable compatibility/correctness workloads introduced for M1.81-M1.90?
2. How does native JSMN performance/code size compare with the M1.90 baseline under the same benchmark harness and host?
3. What does the M1.99 optimization characterization report for the current candidate?
4. Which laboratory dimensions improved, regressed, or simply gained coverage?

This campaign is **not** a replacement for T4 and must not inherit T4 timeout conclusions as benchmark failures.

## Host discipline

Run baseline and candidate on the same machine, same OS session when practical, same compiler/toolchain, same power mode, and serially. Do not run the two variants concurrently.

Record host metadata from the benchmark reports. A large host/environment change invalidates direct performance comparison until repeated under a common environment.

## Phase 1 — JSMN differential correctness and native comparison

Use clean detached S3 worktrees for each SHA and the same detached benchmark worktree at `EXECUTABLE_BENCHMARK_SHA`.

For the baseline:

```powershell
$env:S3_REPO = '<clean-worktree-at-a9e430551f2ee77aa2ef229daf9e967333e83e2c>'
python tools/runner.py --verify-only
python tools/runner.py --full --output-json reports/lab-m200-jsmn-baseline.json --output-markdown reports/lab-m200-jsmn-baseline.md
```

For the candidate:

```powershell
$env:S3_REPO = '<clean-worktree-at-a651e9b3551f218af1c27bb908e0692880afc4da>'
python tools/runner.py --verify-only
python tools/runner.py --full --output-json reports/lab-m200-jsmn-candidate.json --output-markdown reports/lab-m200-jsmn-candidate.md
```

Compare only if both differential correctness gates pass and both runs have valid native S3/C results.

Report at minimum:

- C-GCC-O2 median ns/parse;
- S3-O0 median ns/parse;
- S3-O1 median ns/parse;
- S3-O1 vs C-O2 ratio;
- S3-O1 vs S3-O0 ratio;
- S3-O1 ELF and `.text` bytes;
- fixture completion/blocking;
- environment identity.

## Phase 2 — current compatibility/capability snapshot

Against the candidate only:

```powershell
$env:S3_REPO = '<clean-worktree-at-a651e9b3551f218af1c27bb908e0692880afc4da>'
$env:S3_COMMIT = 'a651e9b3551f218af1c27bb908e0692880afc4da'
python -m benchmarks.m181_m190.correctness --json
python -m benchmarks.m181_m190.benchmark --smoke
```

The smoke timing remains `CHARACTERIZATION_ONLY`; it contributes capability/performance observations but no native comparative speedup claim.

## Phase 3 — M1.99 characterization

Run the existing M1.99 campaign only on the candidate under its exact provenance requirements. Preserve its current classification contract: hosted timing is `CHARACTERIZATION_ONLY` and native speedup remains `NO` unless a valid equivalent native comparative path is actually executed.

Do not relabel previous M1.99 evidence. This snapshot produces new evidence tied to the exact candidate and benchmark SHA used here.

## Laboratory interpretation

After the run, update a new scorecard/snapshot rather than rewriting historical scorecards.

Separate:

```text
CORRECTNESS
NATIVE_CODEGEN
PERFORMANCE
RUNTIME_ASYNC
NETWORK_TLS
PACKAGES_SECURITY
PORTABILITY
REPRODUCIBILITY
REAL_WORLD
TEST_HARNESS_COST
```

Stable expensive certification tests belong under `TEST_HARNESS_COST` unless benchmark or production evidence shows an implementation performance regression.

## Future cadence

This snapshot becomes the reference point for later implementation blocks. Future work should use the staged policy:

```text
focused correctness
-> affected subsystem
-> targeted benchmark delta
-> cross-subsystem validation
-> periodic broad snapshot
```

Do not rerun the broad benchmark suite after every small implementation change. Preserve baseline/candidate SHAs and analyze deltas in bounded stages.
