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
FUNCTIONAL_HEAD=1ceb99b0876b53a99740fd4ce2793652cd707d13
FINAL_HEAD=f44fec82414e5ca3f911770699cd1a07e1850dda
PR_URL=https://github.com/SamDevlab/S3-Benchmarks/pull/16
REMOTE_SYNC=YES
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
S3_SOURCE_CHANGED=NO
```

## Blocker falsification

The prior evidence contained seven `NOT_SUPPORTED_YET` workload families.
This campaign produced concrete independent S3 adapters for all 16 first-wave
workload identities, each at `tiny` and `small` deterministic sizes.

```text
PREVIOUS_NOT_SUPPORTED_COUNT=7
FALSIFIED_BLOCKERS=parallel-execution for sequential PRK nstream; multidimensional-data for flat-storage workloads; bounded-array-workload-driver for the internal BabelStream-compatible subset; whole-program-batch-composition for the S3 RMSD batch adapter; corpus-audit as a language capability
TRUE_BLOCKERS=standalone native decimal-f64 output protocol
ADAPTER_GAPS=TSVC s341 conditional indexed packing; external upstream driver conventions
DRIVER_GAPS=full upstream BabelStream/CLI protocol; external benchmark driver conventions
LAYOUT_ADAPTATIONS=flat f64_vector for transpose, RMSD matrix, PolyBench and PLB2 matrix shapes
WORKLOADS_PROMOTED_TO_CORRECTNESS_PASS=RMSD_BATCH,RMSD_MATRIX,BABELSTREAM_COPY,BABELSTREAM_SCALE,BABELSTREAM_ADD,BABELSTREAM_TRIAD,BABELSTREAM_DOT,PRK_NSTREAM,PRK_TRANSPOSE,POLYBENCH_ATAX,POLYBENCH_MVT,POLYBENCH_GEMM,POLYBENCH_2MM,POLYBENCH_JACOBI_1D,PLB2_MATMUL,TSVC-independent representative adapter coverage
WORKLOADS_PROMOTED_TO_NATIVE_PASS=NONE
```

The hosted matrix is independently checked and recorded as `32/32
CORRECTNESS_PASS`. `PRK_NSTREAM_REQUIRES_PARALLEL_EXECUTION=NO`: the adapter
preserves the upstream sequential kernel shape and uses dynamic one-dimensional
storage plus arithmetic. `PRK_STENCIL` and `PRK_DGEMM` were not required for
this first wave and were not claimed as activated.

The native Linux x86-64 attempt used the exact S3 candidate and reached the
same native output boundary for every case:

```text
NATIVE_CASES=32
NATIVE_PASS=0
NATIVE_FAIL=0
NATIVE_BLOCKED=32
NATIVE_BLOCKER=TRUE_BACKEND_CAPABILITY_BLOCKER
NATIVE_ERROR=NativeBackendError: native entry function 'main' cannot return f64 until the standalone runtime provides decimal float output
```

This is a real backend/output-protocol blocker, not a language-capability
failure. No native correctness or speedup claim is made. The raw transcript
is `native-activation-linux-x86_64.json`; its SHA-256 is
`3ee07223cdf66f2d2fe6085ecbb097a94569c75b7992d3fa54781e2c83bb49ae`.

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
TRUE_BACKEND_BLOCKERS=standalone native decimal-f64 output protocol
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
FULL_SUITE_SHA=5745b1e2497908d1e9d0249d7b056a33a71401dfde70df1d46ec608370b0d3c6
COMPILEALL=PASS
DIFF_CHECK=PASS
UPDATED_COVERAGE_REPORT=references/tsvc-loop-audit-v2.1.json; reports/benchmarks-2.0.1-candidate-activation/capability-coverage-v2.1.md
BLOCKER_FALSIFICATION_REPORT=reports/benchmarks-2.0.1-candidate-activation/BLOCKER_FALSIFICATION.md
FINAL_REPORT=reports/benchmarks-2.0.1-candidate-activation/FINAL_REPORT.md
NEXT_PATH=Path B
NEXT_CAMPAIGN=S3_CAPABILITY_CAMPAIGN_FOR_NATIVE_DECIMAL_F64_OUTPUT
EXTERNAL_PRS_OPENED=NO
READY_FOR_MERGE=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO
```

No merge, tag, release, or shutdown action is part of this campaign.
