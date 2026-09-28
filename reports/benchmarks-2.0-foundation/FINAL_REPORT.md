# S3 Evidence Lab 2.0 Foundation

## Provenance

```text
CAMPAIGN=S3_BENCHMARKS_2_0_EVIDENCE_LAB
REPOSITORY=SamDevlab/S3-Benchmarks
START_MAIN_SHA=e5f3236f868d5522e1e0e92e245a51c7b3e91064
FUNCTIONAL_HEAD=8f0d0ed36f21319bb1552fc122b475c92a3500a2
FINAL_TESTED_SOURCE_HEAD=8f0d0ed36f21319bb1552fc122b475c92a3500a2
S3_CANDIDATE_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
S3_SOURCE_CHANGED=NO
REGISTRY_DIGEST=b05c980a1275d4433de51f728f530d1a947f2198ee041191c5ac63c962d67cbf
```

The campaign started from the audited `origin/main` and created one branch,
`feat/benchmarks-2.0-evidence-lab`. No compiler, OS, Biolab, or S3 source was
modified. The final documentation commit is intentionally separate from the
functional commit so the tested source identity remains explicit.

## Architecture and compatibility

```text
HARNESS_REUSE_AUDIT=PASS
GENERIC_HARNESS=PASS
OLD_JSMN_ARCHITECTURE=PRESERVED_AS_COMPATIBILITY_ADAPTER
JSMN_REGRESSION=NONE_OBSERVED
JSMN_RUNNER_COMPATIBILITY=PASS
RESULT_SCHEMA_V2=PASS
UPSTREAM_REGISTRY_V2=PASS
```

The generic protocol contains workload, correctness, measurement, statistics,
provenance, result, and registry contracts. It preserves raw samples, warmup
exclusion, deterministic interleaving, MAD, CV, work-unit metrics, and explicit
unavailable metrics. Synthetic timing is rejected. The legacy JSMN runner still
supports `--verify-only` and the new explicit `--workload jsmn` alias.

## Upstream registry

```text
UPSTREAMS_PINNED=6 immediate references
LICENSE_AUDIT=PARTIAL; plb2 and rmsd resolved; four upstreams report NOASSERTION and require legal review before vendoring
VENDORED_CODE=NONE
```

All six immediate entries use full immutable commit SHAs. No repository branch
name is used as benchmark identity. Fifteen medium/future candidates are
registered separately without pretending they are pinned or executable.

## Workload matrix

| Workload | Status | Native | Measurement | First missing capability |
|---|---|---|---|---|
| `realworld.jsmn` | `CORRECTNESS_PASS` | not run here | not run | none observed |
| `scientific.rmsd.single` | `CORRECTNESS_PASS` | not run here | not run | none for single-vector slice |
| `scientific.rmsd.batch` | `NOT_SUPPORTED_YET` | no | no | whole-program-batch-composition |
| `scientific.rmsd.matrix` | `NOT_SUPPORTED_YET` | no | no | multidimensional-data |
| `memory.babelstream.initial` | `NOT_SUPPORTED_YET` | no | no | bounded-array-workload-driver |
| `hpc.prk.initial` | `NOT_SUPPORTED_YET` | no | no | parallel-execution |
| `numerical.polybench.initial` | `NOT_SUPPORTED_YET` | no | no | multidimensional-data |
| `language.plb2.matmul` | `NOT_SUPPORTED_YET` | no | no | multidimensional-data |
| `compiler.tsvc.initial` | `NOT_SUPPORTED_YET` | no | no | corpus-audit |

RMSD uses an independent Python oracle and the pinned S3 candidate source. The
hosted gate passed in both O0 and O1 with `sqrt(14/3) = 2.160246899469287`.
The S3 checkout was verified fail-closed at the exact functional SHA. No
benchmark timing was produced, so no performance claim is made.

```text
RMSD_SINGLE=CORRECTNESS_PASS
RMSD_BATCH=NOT_SUPPORTED_YET
RMSD_MATRIX=NOT_SUPPORTED_YET
BABELSTREAM_COPY=NOT_SUPPORTED_YET
BABELSTREAM_SCALE=NOT_SUPPORTED_YET
BABELSTREAM_ADD=NOT_SUPPORTED_YET
BABELSTREAM_TRIAD=NOT_SUPPORTED_YET
BABELSTREAM_DOT=NOT_SUPPORTED_YET
PRK_NSTREAM=NOT_SUPPORTED_YET
PRK_TRANSPOSE=NOT_SUPPORTED_YET
PRK_STENCIL=NOT_SUPPORTED_YET
PRK_DGEMM=NOT_SUPPORTED_YET
POLYBENCH_ATAX=NOT_SUPPORTED_YET
POLYBENCH_MVT=NOT_SUPPORTED_YET
POLYBENCH_GEMM=NOT_SUPPORTED_YET
POLYBENCH_2MM=NOT_SUPPORTED_YET
POLYBENCH_JACOBI_1D=NOT_SUPPORTED_YET
POLYBENCH_ADDITIONAL=DEFERRED
PLB2_MATMUL=NOT_SUPPORTED_YET
TSVC_AUDITED_COUNT=0
TSVC_SUPPORTED_NOW=0
TSVC_INITIAL_IMPLEMENTED=0
```

## Future corpus

```text
EMBENCH_REGISTERED=YES
COREMARK_REGISTERED=YES
COREMARK_PRO_REGISTERED=YES
XSBENCH_REGISTERED=YES
MINIBUDE_REGISTERED=YES
MINIMD_REGISTERED=YES
GAPBS_REGISTERED=YES
PBBS_REGISTERED=YES
LLVM_TEST_SUITE_REGISTERED=YES
HPCG_REGISTERED=YES
NPB_REGISTERED=YES
RAJAPERF_REGISTERED=YES
```

These are candidate records only. They have no executable benchmark result or
invented upstream pin in this campaign.

## Measurement readiness

```text
WALL_TIME_METRICS=AVAILABLE_IN_PROTOCOL; NOT_MEASURED
CPU_TIME_METRICS=DEFERRED
PEAK_RSS_METRICS=AVAILABLE_OPTIONAL; NOT_MEASURED
PAGE_FAULT_METRICS=DEFERRED
PERF_COUNTERS=OPTIONAL; NOT_AVAILABLE
BINARY_SIZE_METRICS=SUPPORTED; NOT_MEASURED
ASSEMBLY_METRICS=REUSED_FOR_JSMN; NOT_RUN_FOR_NEW_WORKLOADS
COMPILER_METRICS=DEFERRED
ENERGY_METRICS=SCHEMA_ONLY; NOT_MEASURED
RAW_SAMPLES=SUPPORTED_SCHEMA; NO_TIMED_SAMPLES_PRODUCED
INTERLEAVED_MEASUREMENT=SUPPORTED_PROTOCOL; NOT_EXECUTED
WORK_UNIT_METRICS=SUPPORTED
REPRODUCIBILITY_LEVEL=SINGLE_RUN_FOR_TEST_EVIDENCE; NO_PERFORMANCE_REPRODUCTION
LINUX_X86_64_NATIVE=NOT_RUN_IN_THIS_FOUNDATION_CAMPAIGN
PERFORMANCE_RESULTS_VALID=NO_NEW_PERFORMANCE_RESULTS
SYNTHETIC_TIMING=ABSENT
```

The Windows host was used for contract and correctness validation only. Native
performance remains unclaimed until a controlled Linux x86-64 run produces raw
samples, environment metadata, artifacts, and provenance under the v2 schema.

## Capability coverage

```text
CAPABILITY_COVERAGE_MATRIX=PASS
MISSING_CAPABILITY_REPORT=PASS
TOP_BLOCKING_CAPABILITIES_BY_WORKLOAD_COUNT=multidimensional-data:3; bounded-array-workload-driver:1; corpus-audit:1; parallel-execution:1; whole-program-batch-composition:1
```

The coverage matrix is descriptive, not a score and not an automatic compiler
roadmap. Capability gaps are recorded without modifying S3.

## Validation

```text
FOCUSED_TESTS=16 passed
COMPILEALL=PASS
REGISTRY_VALIDATION=PASS
DIFF_CHECK=PASS
FULL_TEST_SUITE=PASS
FULL_TEST_SUITE_EXIT=0
FULL_TEST_SUITE_SHA=1648440c08ea699815dcd8b5d97073cfd109ccef5487a1d4413e8dfaa09f988a
FULL_TEST_SUITE_TRANSCRIPT=reports/benchmarks-2.0-foundation/final-full-suite-20260920.txt
```

An earlier discovery attempt was invalid because a temporary S3 clone under
`scratch/` was collected recursively. `pytest.ini` now excludes scratch and
artifact directories; the final valid suite above ran against the intended
repository tests only.

## Externalization and disposition

```text
PRK_UPSTREAM_CONTRIBUTION=NOT_STARTED
PLB2_UPSTREAM_CONTRIBUTION=NOT_STARTED
LANGARENA_INTEGRATION=NOT_STARTED
PROGRAMMING_LANGUAGE_BENCHMARKS_INTEGRATION=NOT_STARTED
EXTERNAL_PRS_OPENED=NO
S3_BENCHMARKS_2_0=FOUNDATION_OPERATIONAL
READY_FOR_MERGE=NO
PR_MERGED=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

This campaign establishes the evidence-lab foundation and a correctness-only
RMSD vertical slice. It deliberately does not claim Level D native measurement
or Level E multi-family operational status.
