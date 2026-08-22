# LICM Determinism Campaign Evidence

Date: 2026-08-21

This report records the bounded evidence collected after the S3 LICM
determinism correction. It is documentation only; no benchmark harness,
workload, timing protocol, or raw artifact was changed.

## Provenance

```text
BENCHMARK_HEAD=5fa0285a16056f4f5c92d9d22a4de47373862a8e
S3_BASE_SHA=a651e9b3551f218af1c27bb908e0692880afc4da
S3_FIX_SHA=32feb550dcfe01e81eda6e2b4c6f8e1d475bda01
FIXTURE=tiny_04_arr
OPTIMIZATION=O1
TARGET=native-x86-64
PYTHON=3.13.15
```

The raw cross-seed artifacts and transcripts are retained on the Linux
validation host under:

```text
/home/vboxuser/s3-m200-licm-determinism-artifacts-20260821-v4
```

## Correctness And Reproducibility

The isolated harness completed nine fresh-process runs: `PYTHONHASHSEED=0, 1,
42`, three runs per seed. Every run passed correctness. The resulting
assembly, object, executable, source digest, and structural metrics were
identical across all runs.

```text
CROSS_SEED_RUNS=9
CORRECTNESS=9/9 PASS
ASSEMBLY_UNIQUE_DIGESTS=1
OBJECT_UNIQUE_DIGESTS=1
EXECUTABLE_UNIQUE_DIGESTS=1
STRUCTURAL_METRIC_UNIQUE_DIGESTS=1
ASSEMBLY_SHA256=78519f7c0e4a39694144546e1af7f7a6d86d2884c4430cea849ddf174563dd4d
INSTRUCTION_COUNT=48784
STACK_OPS=7440
BRANCH_COUNT=12524
LOAD_STORE_COUNT=24445
```

The harness manifests recorded the same S3 fix SHA and this benchmark HEAD on
all nine runs. The isolation and provenance gates therefore passed.

## Native Characterization

The bounded native campaign used the existing smoke protocol and the paired
order `A B B A` on one Linux x86-64 VM. `A` was the M1.90 S3 baseline and `B`
was the deterministic LICM fix. Each run passed correctness.

The evidence class is `CHARACTERIZATION_ONLY`, not a native speedup claim. The
control compiler moved materially between paired observations, and the
baseline S3-O1 observation also moved materially between A and A2. The S3-O1
normalized result is consequently inconclusive:

```text
S3_O1_A=12932.727 ns
S3_O1_B=12764.712 ns
S3_O1_B2=13040.933 ns
S3_O1_A2=14011.982 ns
CONTROL_C_O2_A=10573.266 ns
CONTROL_C_O2_A2=10392.308 ns
CONTROL_C_O2_B=11179.980 ns
CONTROL_C_O2_B2=11363.391 ns
EVIDENCE_CLASS=CHARACTERIZATION_ONLY
NORMALIZED_RESULT=INCONCLUSIVE
NATIVE_SPEEDUP_CLAIM=NO
```

The LICM correction did not change the measured O1 structural counters or
binary sizes. No optimization was selected or retained from this campaign.

## Laboratory Status

```text
CORRECTNESS=PASS
REPRODUCIBILITY=PASS
NATIVE_CODEGEN=PASS
PERFORMANCE=CHARACTERIZATION_ONLY_INCONCLUSIVE
INITIAL_20_PERCENT_REGRESSION=REJECTED
ABBA_PRE_ISOLATION=INCONCLUSIVE
POST_ISOLATION_PRE_LICM_FIX=INVALID_FOR_PERFORMANCE
POST_LICM_DETERMINISM=PASS
POST_OPTIMIZATION=NOT_RUN
```

The next performance study requires a longer paired protocol with stable
control observations and broader workloads. This record does not authorize a
merge, release, or a native performance claim.
