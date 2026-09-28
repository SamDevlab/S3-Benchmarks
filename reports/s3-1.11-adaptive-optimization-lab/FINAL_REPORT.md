# S3-Benchmarks 1.11 Lab Final Report

## Lineage and Scope

```text
BENCH_CAMPAIGN_BASE=b3ecb9b2269b583cba0706fd7ed13956a9641512
BENCH_CAMPAIGN_TREE=06316635dfc1830d3ec3955803acb0d168b77a7e
S3_CONTROL_SHA=832b1cc04fe1f6174e482eb3a245e08af3d53211
S3_CONTROL_TREE=dc1138890655169088f9371ce32a9050cfc3af8d
TARGET=Linux x86-64 for native replay evidence
RESULT_SCHEMA=1.0.0
TIMING_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
```

The lab independently executed the pinned control, replayed the exact
candidate artifacts, validated reference outputs and hashes, and independently
re-extracted native structure for the hot-fallthrough prototype. It did not
independently recompile that research transformation and did not time the
hot-fallthrough artifacts.

## Validation and Evidence

```text
BENCH_FOCUSED_TESTS=8 passed, 1 skipped on Windows
BENCH_FULL_WINDOWS_SUITE=41 passed, 1 skipped, exit 0
BENCH_FULL_LINUX_SUITE=42 passed, exit 0
BENCH_COMPILEALL=PASS on Windows
HOT_FALLTHROUGH_REPLAY=PASS correctness and native metrics
```

The corrected Linux full suite used the S3 frozen clone on `PYTHONPATH` for
the Bench native-artifact tests. Its transcript is
`evidence/validation/FULL-LINUX-BENCH-SUITE-20260928-PYTHONPATH.txt`; the
initial collection-only failure caused by missing `PYTHONPATH` is retained in
`FULL-LINUX-BENCH-SUITE-20260928.txt` and is not counted as a test failure.

The hot-fallthrough replay report is
`evidence/EXP-S3-111-HOT-FALLTHROUGH-REPLAY-001.json` with SHA-256
`053c3dd3d0f2ad92ed6af6a2511885c5b4f83f4b3b66765f2d968ec102df4076`. It
validated exact baseline/candidate output equality against the pinned energy
reference and independently matched native metrics: one fewer branch and
machine instruction, two fewer `.text` bytes, with memory references, stack
references, frame size, and ELF size unchanged.

The existing candidate replay dossier documents independent correctness
replays for the three value-transform candidate sets and the workload-specific
interleaved point-cloud timing confirmation. That timing remains a
characterization signal; it is not a general speedup claim or promotion.

## Capability and Limits

```text
INDEPENDENT_CONTROL_REPLAY=PASS
INDEPENDENT_CANDIDATE_CORRECTNESS_REPLAY=PASS
INDEPENDENT_HOT_FALLTHROUGH_STRUCTURE_REPLAY=PASS
INDEPENDENT_HOT_FALLTHROUGH_TIMING=NOT_MEASURED
MULTI_SHA_EXECUTOR=PINNED_SINGLE_SHA_ONLY
HISTORICAL_CROSS_VERSION_REPLAY=NOT_RUN
PRODUCTION_DEFAULT_CHANGED=NO
RELEASE_OR_TAG_CREATED=NO
HISTORICAL_PRS_15_23_24=OPEN_DRAFT_UNTOUCHED
```

The independent lab reproduced correctness and structure for exact candidate
artifacts, but it did not provide a second hot-fallthrough timing run, a
multi-version timing protocol, or historical 1.5–1.9 replays. These remain
evidence debt, not implied passes.

## Publication

```text
BENCH_BRANCH=research/s3-1.11-adaptive-optimization-lab
BENCH_PR_BASE=main
BENCH_PR_STATE=NOT_YET_PUBLISHED
STOP_HUMAN_GATE=REVIEW_S3_1_11
```
