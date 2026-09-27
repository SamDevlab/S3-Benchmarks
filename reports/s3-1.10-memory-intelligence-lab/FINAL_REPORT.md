# S3-Benchmarks 1.10 Memory Intelligence Lab — Final Report

## Outcome

The lab completed the independent Linux replay of the frozen S3 1.10 source
and joined it to the separately executed historical 1.5–1.9 compatibility
matrix. This is a research and characterization result. It does not promote a
compiler transformation, change a default, establish a general performance
claim, or authorize release activity.

```text
CAMPAIGN=S3_1_10_MEMORY_INTELLIGENCE_VALUE_LOCALITY_VERIFIED_TRANSFORMATIONS_AND_COMPILER_SCIENCE_EXPANSION
BENCH_BASE=b11526443b9f2ac50f2ffdd3c4a6c1d0a2471152
BENCH_BRANCH=research/s3-1.10-memory-intelligence-lab
BENCH_TESTED_HEAD=3d0619f8c6423849477fa1f69d39c5beadf41a64
S3_CONTROL_SHA=e27dff1e712e50271df9f860669cd714e28f4ce7
S3_REPLAY_SHA=856bf0cd60c3da6ba701adec73c7858d063739a7
S3_REPLAY_TREE=5d7c179ac9df64fad99b7ec140f69571c48b866f
BENCHMARK_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
TRANSFORMATION_PROMOTION=NO
```

The Bench branch is based on merged `main` after PR #27, not on a historical
research branch. The 1.10 S3 compiler source was checked out at its exact
commit in a clean worktree and independently built and exercised by the Bench
executor.

## Replay Evidence

The 1.5–1.9 historical group and the single-SHA 1.10 replay were executed as
separate serial groups, not interleaved. All six S3 revisions passed the
three-workload correctness matrix. The combined compatibility index checks
the pinned source identities, protocol, host/toolchain data, raw evidence,
artifact coverage, and output hashes. Because the groups were not
interleaved, cross-version timing deltas are not supported.

```text
CROSS_VERSION_COVERAGE=1.5_TO_1.10
HISTORICAL_GROUP=1.5_TO_1.9
CURRENT_GROUP=1.10_SINGLE_SHA
EXECUTION_ORDER=SERIAL_GROUPS_NOT_INTERLEAVED
DIRECT_CROSS_VERSION_TIMING_DELTA_SUPPORTED=NO
INDEX_SHA256=f25d0165d8a3be2f1fa04793cb5107b19f9235af1b0ab5b3441c49908a3fd38b
RAW_1_10_EVIDENCE_SHA256=d6b8b68704db7317db9ff9978e7082a694d17b01fe1593074f62af03e553fc79
EXECUTOR_SHA256=66e8b351d90f15a62ac4aba3ce4129dc62e1aa4439c93d50d3f32c4ff1325002
```

The 1.10 replay ran on Linux x86-64, kernel `7.0.0-31-generic`, Python
`3.14.4`, an AMD Ryzen 5 3400G, and GCC `15.2.0`. Each of the energy,
point-cloud, and raster workloads reported `PASS_ALL_BUILDS`; native output
hashes match across the builds recorded in the raw result.

## Native Characterization

The timing protocol used 3 warmups, 21 samples of 1,000 same-process scalar
C-ABI calls, paired ordering, and 10,000 bootstrap resamples. Input/setup/build
were excluded; ctypes dispatch was included equally. The table gives the
measured median nanoseconds per call from the raw artifact. These are
host-specific characterization values, not a cross-version comparison.

| Workload | S3 O1 per-instruction | Compact-EA request | Exact-segment | Loop-hybrid | Correctness |
| --- | ---: | ---: | ---: | ---: | --- |
| Energy aggregation | 16,742.308 | 16,716.151 | 14,815.865 | 14,698.390 | PASS_ALL_BUILDS |
| Point-cloud summary | 13,846.137 | 13,257.459 | 12,281.018 | 12,338.485 | PASS_ALL_BUILDS |
| Raster statistics | 11,231.421 | 11,273.149 | 10,482.026 | 10,672.632 | PASS_ALL_BUILDS |

Compact-EA applied zero sites in all three workloads and therefore did not
exercise its intended rewrite. Paired classifications in the raw JSON report
exact-segment as `MATERIAL_IMPROVEMENT` against per-instruction for all three
workloads; loop-hybrid is `MATERIAL_IMPROVEMENT` for energy and point-cloud,
and `INCONCLUSIVE` for raster. These classifications are limited to this
protocol and candidate. They do not establish that instruction-budget mode
alone caused the observed differences or justify changing defaults.

Hardware performance counters were unavailable by policy
(`perf_event_paranoid=4`). No PMU-level or microarchitectural attribution is
made. The exact samples, confidence intervals, compiler flags, native object
metrics, static IR counts, fallbacks, and output identities remain in
`evidence/replay-1.10-candidate-v1/.../native-workload-benchmark-v1.json`.

## Validation

Focused index/executor tests passed (`11 passed`) before publication of the
final replay index. `python -m compileall tools tests` and `git diff --check`
passed. The required complete Linux test suite was run once against the exact
Bench source/evidence HEAD shown below:

```text
FULL_SUITE_HEAD=3d0619f8c6423849477fa1f69d39c5beadf41a64
FULL_SUITE_START=2026-09-27T22:29:03.528920589+00:00
FULL_SUITE_END=2026-09-27T22:29:07.980056746+00:00
FULL_SUITE_TERMINAL=YES
FULL_SUITE_RESULT=33 passed
FULL_SUITE_EXIT=0
SOURCE_OR_TEST_LOGIC_CHANGED_AFTER_SUITE=NO
```

The transcript and status are preserved on the Linux guest at
`/tmp/s3-bench-final-3d0619f/qualification-20260927/full-suite.log` and
`full-suite-status.txt`. This report is a documentation-only change after
that gate; it does not require another full suite.

## Evidence Retention and Boundaries

The committed 1.10 evidence bundle contains curated structured JSON, launch
and status records, and the compatibility index. The evidence subtree has 14
files totaling 660,186 bytes. Full generated native build artifacts were
retained outside the repository under `%TEMP%` on Windows and `/tmp` on the
Linux guest; they were not deleted. Historical reports and PR #15, #23, and
#24 were preserved and not modified by this campaign.

```text
BENCHMARKS_1_10_REPLAY=PASS
BENCHMARKS_FULL_SUITE=PASS
BENCHMARK_TIMING_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
PRODUCTION_DEFAULT_CHANGED=NO
HISTORICAL_PRS_MODIFIED=NO
RELEASE_OR_TAG_CREATED=NO
```

The corresponding compiler campaign report is in the S3 repository at
`reports/s3-1.10-memory-intelligence-value-locality/FINAL_REPORT.md`. The two
repositories are independently reviewable; neither is a stacked dependency
for the other.

```text
BENCH_PR=28
BENCH_PR_BASE=main
BENCH_PR_STATE=DRAFT
S3_PR=324
S3_PR_BASE=main
S3_PR_STATE=DRAFT
MERGE=NOT_AUTHORIZED
RELEASE=NOT_AUTHORIZED
TAG=NOT_AUTHORIZED
PYPI=NOT_AUTHORIZED
S3_1_11_STARTED=NO
```

Review requests: [S3-Benchmarks #28](https://github.com/SamDevlab/S3-Benchmarks/pull/28)
and [S3 #324](https://github.com/SamDevlab/S3/pull/324).
