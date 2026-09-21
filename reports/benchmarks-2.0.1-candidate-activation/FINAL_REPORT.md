# S3 Benchmarks 2.0.1 Candidate Activation

## Campaign identity

```text
CAMPAIGN=S3_BENCHMARKS_2_0_1_CANDIDATE_ACTIVATION
BASE_PR=15
BASE_HEAD=2891ae5a2a8ee558267aeaa54c7cbc42156e2373
BRANCH=feat/benchmarks-2.0.1-candidate-activation
PR=16
PR_STATE=DRAFT_OPEN
PR_MERGED=NO
FUNCTIONAL_HEAD=39551020fb52b4b9f7f712fc52216520029d439a
FINAL_HEAD=39551020fb52b4b9f7f712fc52216520029d439a
PR_URL=https://github.com/SamDevlab/S3-Benchmarks/pull/16
REMOTE_SYNC=YES
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
S3_SOURCE_CHANGED=NO
SOURCE_CHANGED_AFTER_FINAL_GATES=NO
```

## Blocker falsification

The prior evidence contained seven `NOT_SUPPORTED_YET` workload families.
This campaign produced concrete independent S3 adapters for all 16 first-wave
workload identities, each at `tiny` and `small` deterministic sizes.

```text
PREVIOUS_NOT_SUPPORTED_COUNT=7
FALSIFIED_BLOCKERS=parallel-execution for sequential PRK nstream; multidimensional-data for flat-storage workloads; bounded-array-workload-driver for the internal BabelStream-compatible subset; whole-program-batch-composition for the S3 RMSD batch adapter; corpus-audit as a language capability
TRUE_BLOCKERS=NONE_AFTER_NATIVE_CANARY_REQUALIFICATION
ADAPTER_GAPS=TSVC s341 conditional indexed packing; external upstream driver conventions
DRIVER_GAPS=full upstream BabelStream/CLI protocol; external benchmark driver conventions
LAYOUT_ADAPTATIONS=flat f64_vector for transpose, RMSD matrix, PolyBench and PLB2 matrix shapes
WORKLOADS_PROMOTED_TO_CORRECTNESS_PASS=RMSD_BATCH,RMSD_MATRIX,BABELSTREAM_COPY,BABELSTREAM_SCALE,BABELSTREAM_ADD,BABELSTREAM_TRIAD,BABELSTREAM_DOT,PRK_NSTREAM,PRK_TRANSPOSE,POLYBENCH_ATAX,POLYBENCH_MVT,POLYBENCH_GEMM,POLYBENCH_2MM,POLYBENCH_JACOBI_1D,PLB2_MATMUL,TSVC-independent representative adapter coverage
WORKLOADS_PROMOTED_TO_NATIVE_PASS=RMSD_BATCH,RMSD_MATRIX,BABELSTREAM_COPY,BABELSTREAM_SCALE,BABELSTREAM_ADD,BABELSTREAM_TRIAD,BABELSTREAM_DOT,PRK_NSTREAM,PRK_TRANSPOSE,POLYBENCH_ATAX,POLYBENCH_MVT,POLYBENCH_GEMM,POLYBENCH_2MM,POLYBENCH_JACOBI_1D,PLB2_MATMUL,TSVC-independent representative adapter coverage
```

The hosted matrix is independently checked and recorded as `32/32
CORRECTNESS_PASS`. `PRK_NSTREAM_REQUIRES_PARALLEL_EXECUTION=NO`: the adapter
preserves the upstream sequential kernel shape and uses dynamic one-dimensional
storage plus arithmetic. `PRK_STENCIL` and `PRK_DGEMM` were not required for
this first wave and were not claimed as activated.

The first native Linux x86-64 attempt used the exact S3 candidate and reached
the same decimal-f64 output boundary for every case. The allowed integer
correctness-canary protocol then requalified the same workloads without
changing S3:

```text
NATIVE_CASES=32
NATIVE_PASS=32
NATIVE_FAIL=0
NATIVE_BLOCKED=0
NATIVE_EXECUTION=PASS
NATIVE_OBSERVABLE=CANARY
```

The initial output limitation was a protocol gap, not a language failure, and
was falsified by the permitted integer canary. The final raw transcript is
`native-activation-linux-x86_64.json`; its SHA-256 is
`978f02e152fffb1ddde36e666a1bc6f1c8b89249963b9700db49a20cc2d33d0d`.
No native speedup claim is made.

## TSVC audit

The upstream TSVC source was inspected at
`badf9adb2974867ac0937718d85a44dec6dec95a`, where 138 named loops were
enumerated. Eighteen representative shapes were classified in
`references/tsvc-loop-audit-v2.1.json`. No upstream source was copied into
this repository.

```text
TSVC_CORPUS_AUDIT=BENCHMARK_PREPARATION_INCOMPLETE_NOT_LANGUAGE_BLOCKER
TSVC_SUPPORTED_NOW=REPRESENTATIVE_SHAPES_ONLY
TSVC_IMPLEMENTED=NO
```

## Safety and provenance

```text
TRUE_LANGUAGE_BLOCKERS=NONE
TRUE_RUNTIME_BLOCKERS=NONE
TRUE_BACKEND_BLOCKERS=NONE_AFTER_NATIVE_CANARY_REQUALIFICATION
HARNESS_GAPS=NONE_FOR_INTERNAL_CORRECTNESS_MATRIX
ENVIRONMENT_GAPS=NONE_FOR_HOSTED_OR_LINUX_ATTEMPT
LICENSE_AUDIT=upstream pins recorded; license metadata remains separate from workload usability; no code vendored
VENDORED_CODE=NONE
PERFORMANCE_RESULTS_VALID=NO_NEW_PERFORMANCE_RESULTS
```

Generated S3 sources are deterministic artifacts under `generated/`, and
`activation-results.json` records each source SHA-256. The report contains no
timing and makes no official upstream score claim.

## Validation and next decision

```text
FULL_SUITE=18 passed, 1 skipped, 0 failed, exit 0
FULL_SUITE_SHA=36c1baf2465fe04c8034f5e50a5922030c35c376fa5da01d3eabba0dce831c0c
COMPILEALL=PASS
DIFF_CHECK=PASS
UPDATED_COVERAGE_REPORT=references/tsvc-loop-audit-v2.1.json; reports/benchmarks-2.0.1-candidate-activation/capability-coverage-v2.1.md
BLOCKER_FALSIFICATION_REPORT=reports/benchmarks-2.0.1-candidate-activation/BLOCKER_FALSIFICATION.md
FINAL_REPORT=reports/benchmarks-2.0.1-candidate-activation/FINAL_REPORT.md
NEXT_PATH=Path A
NEXT_CAMPAIGN=S3_BENCHMARKS_2_1_NATIVE_MEASUREMENT
EXTERNAL_PRS_OPENED=NO
READY_FOR_MERGE=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

No merge, tag, release, or shutdown action is part of this campaign.
