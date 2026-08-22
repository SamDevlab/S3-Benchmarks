# Native Artifact Isolation and Determinism

## Scope

This report covers the benchmark-infrastructure correction at
`cad045f29250bf34f63f86a09c0b8fba26bebea0`. The S3 repository was not
modified. No performance timing, T4 run, or M2.01 work was performed.

## Validation

- Focused infrastructure tests: `8 passed`
- Relevant Python compilation: `PASS`
- `git diff --check`: `PASS`
- Artifact manifests: `PASS`
- Cross-run writable path reuse: `NO`
- Cross-variant writable path reuse: `NO`
- Cross-S3-SHA writable path reuse: `NO`
- Provenance checks: exact S3 and benchmark HEADs required before native work

Each run has its own run-id root containing the input, generated source,
assembly, object, executable, manifest, metadata, and transcript. Completed
manifests are write-once and summaries resolve only the explicitly selected
run-id.

## Candidate Smoke

Pins:

```text
S3_SHA=a651e9b3551f218af1c27bb908e0692880afc4da
BENCHMARK_SHA=cad045f29250bf34f63f86a09c0b8fba26bebea0
FIXTURE=tiny_04_arr
OPTIMIZATION=S3-O1
```

Hosted and native correctness passed in all three runs. Artifact manifests
and per-file hashes were verified for every run, but assembly determinism
failed:

| Run | Assembly SHA256 | Executable SHA256 | Instructions | Stack ops | Branches | Loads/stores |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| candidate-v2-1 | `78519f7c0e4a39694144546e1af7f7a6d86d2884c4430cea849ddf174563dd4d` | `e0766ff3a99f1519ebc076d297d7130ce177cc90e0e3f746cc68456456999aad` | 48784 | 7440 | 12524 | 24445 |
| candidate-v2-2 | `b22a56a1ac0fcc32af16d5585b1e87781636a3fbced196b901dd90b8f7dfca96` | `16e81ae25d9f86ee8f840067c44040c462bcfeadfaa8d77aa273d9edd94fd69e` | 46716 | 8644 | 11945 | 23489 |
| candidate-v2-3 | `78519f7c0e4a39694144546e1af7f7a6d86d2884c4430cea849ddf174563dd4d` | `e0766ff3a99f1519ebc076d297d7130ce177cc90e0e3f746cc68456456999aad` | 48784 | 7440 | 12524 | 24445 |

Result:

```text
DETERMINISM_SMOKE=FAIL
CORRECTNESS_REPRODUCIBILITY=PASS_FOR_CANDIDATE
PERFORMANCE_CAMPAIGN_ELIGIBLE=NO
```

The differing assembly is an unresolved compiler/backend determinism issue;
this benchmark-infrastructure change does not reinterpret it as performance
evidence.

## Baseline Observation

The optional baseline smoke was started only after the first candidate smoke
passed. On benchmark infrastructure commit `200b6661d362e6ea82ec8247520116290c553bc7`,
baseline run 1 reproduced an uninitialized captured-memory cell (`start`, token
0); runs 2 and 3 completed. The run-1 transcript was preserved and the smoke
was stopped after the reproduction was observed; runs 2 and 3 had already
completed by then. The later diagnostic-context-only commit
is why that historical run-1 message contains unspecified provenance fields;
the current harness records the exact S3 SHA and run-id for future failures.

```text
BASELINE_DETERMINISM_SMOKE=FAIL
RUN8_NONE_REPRODUCED=YES_FOR_BASELINE_OBSERVATION
```

## Promotion Decision

```text
PERFORMANCE_EVIDENCE_VALID =
  CORRECTNESS_PASS +
  ARTIFACT_PROVENANCE_PASS +
  RUN_ISOLATION_PASS +
  ASSEMBLY_DETERMINISM_PASS
```

The first three terms pass for the candidate smoke, but assembly determinism
does not. No comparative timing or native speedup claim is valid.

```text
S3_CHANGE=NO
BENCHMARK_INFRA_CHANGE=YES
FULL_PERFORMANCE_RUNS=0
T4_RUNS=0
MERGE=NO
M2.01_STARTED=NO
```
