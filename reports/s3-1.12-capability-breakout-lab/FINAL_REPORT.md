# S3 1.12 Capability Breakout Lab - Final Report

## Provenance

```text
BENCH_CAMPAIGN_BASE=d425aaca241549bae797d88d08fd7832ad221255
BENCH_FUNCTIONAL_SOURCE_FREEZE=751c7a15d54bc9a8662f66f970af3726db994d16
BENCH_FUNCTIONAL_SOURCE_TREE=8e13593ec910fa20d8b3a336fb3cab6b87105d3d
S3_CONTROL=a1ecc29908dfb42480376961927fd6c50552ecf3
S3_CANDIDATE_SOURCE=c89daae65aca69be775a395e971f3223ae3a21ce
```

The S3 candidate source used by the matrix is the functional source freeze; subsequent S3 commits changed tests only.

## New Lab Capability

The pinned candidate-matrix runner independently checks out exact source revisions/configurations, builds BASE and CANDIDATE variants, verifies correctness, captures native artifacts and structural metrics, and performs interleaved paired timing. Its tests cover runner dispatch, isolated outputs, provenance, and fail-closed behavior. It replaces one-off candidate-specific harness code with a config-driven BASE/A/B/A+B-capable lab path.

```text
CANDIDATE_MATRIX_RUNNER=PASS
INDEPENDENT_CANDIDATE_BUILD=PASS
INDEPENDENT_CORRECTNESS=PASS
INDEPENDENT_TIMING=CHARACTERIZATION_ONLY
BENCH_LINUX_FULL_SUITE=54 passed, 0 failed, exit 0
```

The Bench tests require the S3 checkout on `PYTHONPATH` for shared compiler integration tests. The first collection attempt omitted this external dependency and stopped before running tests. The successful run set `S3_REPO` and `PYTHONPATH` to the S3 campaign checkout. No Bench source change was needed.

## Experiment

```text
EXPERIMENT_ID=EXP-S3-112-CANDIDATE-MATRIX-001
SPEC=candidate-matrix-001.spec.json
RESULT=candidate-matrix-001.result.json
SPEC_SHA256=ee41ff5ee335b8a92217915a3b8349fecb6549d775ccb69b9e03a2af62a6417d
RESULT_SHA256=de29bccd734d6f5c06fa80392e863b624958d79a89912b70ca9bd5f24fbffcf9
TARGET=Linux x86-64
VARIANTS=BASE,CANDIDATE
WORKLOADS=energy.pv-timeseries-aggregation.v1,engineering.point-cloud-summary.v1,geospatial.raster-window-statistics.v1
TIMING_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
```

Protocol: O1, baseline native policy, per-instruction budget, 5 warmups, 15 interleaved samples, 1000 iterations per sample, 5000 bootstrap resamples, seed 11212. The timed region is same-process scalar C ABI execution; compilation/setup are excluded and ctypes dispatch is included equally.

All three workloads passed reference correctness and exact BASE/CANDIDATE output equality. Inspection found zero eligible same-color TMOV sites in these workload AssemblyPrograms. Each BASE/CANDIDATE binary hash and every reported native structural metric was identical:

| Workload | `.text` bytes | Static instructions | Memory refs | Stack refs | Median BASE/CANDIDATE ratio | 95% paired interval | Result |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Energy aggregation | 36,304 | 2,754 | 953 | 907 | 1.03560 | [0.96503, 1.18491] | INCONCLUSIVE |
| Point-cloud summary | 58,112 | 4,732 | 1,601 | 1,536 | 0.98293 | [0.94007, 1.14706] | INCONCLUSIVE |
| Raster window statistics | 68,491 | 5,666 | 1,898 | 1,821 | 1.00516 | [0.92253, 1.14830] | INCONCLUSIVE |

The ratios are `baseline / candidate`; all intervals include 1 and no runtime-speedup claim is made. Since the three workloads contain no eligible sites, this experiment establishes no general runtime effect for TMOV elision. Native correctness for the transformation itself is covered separately by the S3 compiler regression.

## Final Classification

```text
NEW_LAB_EXECUTION_CAPABILITIES=1 (pinned config-driven candidate matrix)
ONE_OFF_SCRIPTS_ADDED=0
REPORT_ONLY_CHANGE=NO
ABLATION_RUNNER=SUPPORTED_BY_VARIANT_SPEC
INDEPENDENT_CANDIDATE_BUILD=PASS
INDEPENDENT_CORRECTNESS=PASS
INDEPENDENT_TIMING=INCONCLUSIVE
```

Raw binaries and temporary build trees are not committed. Full result JSON and its spec are preserved here; transient execution logs remain outside the repository under `/tmp/s3-1.12-matrix-evidence-003`.
