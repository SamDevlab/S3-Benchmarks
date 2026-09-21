# S3 Benchmarks 2.1 Native Measurement

## Status

- `CAMPAIGN`: `S3_BENCHMARKS_2_1_NATIVE_MEASUREMENT`
- `FUNCTIONAL_HEAD`: `7894ea5`
- `MEASUREMENT_HEAD_IN_RAW_ENVELOPE`: `70e95bfe963bf7b49175d5eeb978ff5a9404d5f0`
- `S3_SHA`: `e07d0b5464bf472b2ca18993f3e196a234ff0fc5`
- `MEASUREMENT_RUN`: `native-v1-20260921-02`
- `MEASURED_SIZE_POINTS`: `30`
- `MEASURED_VARIANT_SERIES`: `60`
- `NATIVE_QUALIFICATION`: `30/31 planned points`; one medium point was excluded before timing.

## Eligibility and skips

The measured corpus reused the 2.0.1 source/oracle generators. Each point first passed hosted O0/O1 oracle checks and a separate native canary gate. `numerical.polybench.jacobi_1d medium` passed hosted execution but failed the exact native canary in both O0 and O1 (`program returned: 0`), so it was recorded as `NATIVE_NOT_QUALIFIED` and not timed. The canary was not relaxed.

Skipped by policy: JSMN legacy adapter was not migrated to protocol v2; TSVC remains capability-shape evidence only; PRK stencil and dgemm were not activated.

## Measurement protocol

- timing scope: `PROCESS_E2E`
- separate measurement executable from the correctness phase
- one useful workload per process sample (`ITERATIONS_PER_SAMPLE=1`)
- one integer anti-DCE canary after the workload
- setup occurs before the workload in each process
- warmups: `5`; repetitions: `30`
- variants are interleaved deterministically O0/O1
- raw samples, median, mean, p95, stddev, MAD and CV are retained
- no `-ffast-math` or `-Ofast`
- no Python oracle or correctness comparison is in the timed process path

`KERNEL_TIME=NOT_AVAILABLE`: the current generated programs do not expose a safe setup-outside-loop kernel entry point, so no E2E subtraction or inferred kernel number is reported. The 200--1000 ms calibration target was not reached for these short process-E2E workloads and is marked as such.

## Host and provenance

- machine fingerprint: `9f6c7cbbdbbc2d056ffc306f76a1dcd9df194e15167cb037542da54e97b59393`
- CPU: `AMD Ryzen 5 3400G with Radeon Vega Graphics`
- RAM: `8432068 kB`
- kernel: `7.0.0-31-generic`
- architecture: `x86_64`
- affinity: `[0, 1, 2]`
- SMT: `0`
- governor: `['UNAVAILABLE']`
- turbo: `UNAVAILABLE`
- environment noisy: `False`
- perf: `NO` (`DENIED_OR_UNAVAILABLE`)

S3 and benchmark repository identities were checked fail-closed before compilation:

```text
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
BENCHMARK_REPO_SHA=70e95bfe963bf7b49175d5eeb978ff5a9404d5f0
```

## Results

The table below is a per-workload characterization. It is not an aggregate score and is not a claim of native kernel speedup.

| Workload | Size | Work units | O0 median ns | O1 median ns | O1/O0 | O1 ns/work | O1 CV |
|---|---|---:|---:|---:|---:|---:|---:|
| `hpc.prk.nstream` | `medium` | 31 | 538337 | 511168 | 0.950 | 16489.3 | 0.312 |
| `hpc.prk.nstream` | `small` | 7 | 490933 | 560492 | 1.142 | 80070.2 | 0.308 |
| `hpc.prk.transpose` | `medium` | 192 | 738784 | 628090 | 0.850 | 3271.3 | 0.275 |
| `hpc.prk.transpose` | `small` | 12 | 965756 | 1000055 | 1.036 | 83337.9 | 0.197 |
| `language.plb2.matmul` | `medium` | 1536 | 858937 | 1013374 | 1.180 | 659.7 | 0.237 |
| `language.plb2.matmul` | `small` | 24 | 586636 | 719729 | 1.227 | 29988.7 | 0.325 |
| `memory.babelstream.add` | `medium` | 31 | 652600 | 758868 | 1.163 | 24479.6 | 0.354 |
| `memory.babelstream.add` | `small` | 7 | 551812 | 498682 | 0.904 | 71240.4 | 0.365 |
| `memory.babelstream.copy` | `medium` | 31 | 495402 | 519302 | 1.048 | 16751.7 | 0.400 |
| `memory.babelstream.copy` | `small` | 7 | 481123 | 551292 | 1.146 | 78755.9 | 0.393 |
| `memory.babelstream.dot` | `medium` | 31 | 518617 | 579646 | 1.118 | 18698.3 | 0.291 |
| `memory.babelstream.dot` | `small` | 7 | 605586 | 483402 | 0.798 | 69057.5 | 0.587 |
| `memory.babelstream.scale` | `medium` | 31 | 511802 | 515598 | 1.007 | 16632.2 | 0.388 |
| `memory.babelstream.scale` | `small` | 7 | 535677 | 566046 | 1.057 | 80863.8 | 0.344 |
| `memory.babelstream.triad` | `medium` | 31 | 695410 | 506092 | 0.728 | 16325.6 | 0.354 |
| `memory.babelstream.triad` | `small` | 7 | 508880 | 486368 | 0.956 | 69481.1 | 0.436 |
| `numerical.polybench.2mm` | `medium` | 3072 | 1432134 | 1399386 | 0.977 | 455.5 | 0.249 |
| `numerical.polybench.2mm` | `small` | 48 | 730109 | 579222 | 0.793 | 12067.1 | 0.292 |
| `numerical.polybench.atax` | `medium` | 192 | 736593 | 664365 | 0.902 | 3460.2 | 0.268 |
| `numerical.polybench.atax` | `small` | 12 | 1338700 | 1312315 | 0.980 | 109359.6 | 0.366 |
| `numerical.polybench.gemm` | `medium` | 1536 | 917222 | 1086327 | 1.184 | 707.2 | 0.293 |
| `numerical.polybench.gemm` | `small` | 24 | 693044 | 593096 | 0.856 | 24712.3 | 0.336 |
| `numerical.polybench.jacobi_1d` | `small` | 5 | 581771 | 536637 | 0.922 | 107327.4 | 0.344 |
| `numerical.polybench.mvt` | `medium` | 192 | 891165 | 1120518 | 1.257 | 5836.0 | 2.413 |
| `numerical.polybench.mvt` | `small` | 12 | 906136 | 839083 | 0.926 | 69923.6 | 0.244 |
| `scientific.rmsd.batch` | `medium` | 48 | 530528 | 595714 | 1.123 | 12410.7 | 0.290 |
| `scientific.rmsd.batch` | `small` | 9 | 511082 | 548796 | 1.074 | 60977.4 | 0.482 |
| `scientific.rmsd.matrix` | `medium` | 48 | 783303 | 573051 | 0.732 | 11938.6 | 0.317 |
| `scientific.rmsd.matrix` | `small` | 27 | 564126 | 575710 | 1.021 | 21322.6 | 0.320 |
| `scientific.rmsd.single` | `medium` | 31 | 536676 | 507532 | 0.946 | 16372.0 | 0.465 |


## Structural evidence

Assembly analysis reused `tools/assembly_analyzer.py`. It records instruction, call-site, load/store, branch, conditional-branch, stack-operation, binary-size and `.text` metrics for each S3 O0/O1 artifact. Runtime-helper counts, dynamic bounds checks, dynamic stack traffic, cycles, instructions, cache counters and IPC are unavailable under this protocol.

## Pressure decision

`PRESSURE_MAP.md` and `PRESSURE_MAP.json` record three multi-family hypotheses with `CAUSALITY=UNKNOWN`: process startup/runtime initialization, static code/stack-operation density, and measurement variability. Since direct kernel evidence and dynamic counters are unavailable, the campaign selects **PATH C: improve benchmark methodology first**. No S3 optimization should be started from this data.

## Reproducibility

- raw result envelope: `baselines/native-v1/native-v1-20260921-02/measurement-results.json`
- raw transcript: `scratch/native-measurement-20260921-02.txt`
- artifact index: `baselines/native-v1/native-v1-20260921-02/artifact-index.json`
- same-machine reproduction: `NOT_RUN`
- build determinism: `NOT_MEASURED`
- full suite at functional head `7894ea5`: `21 passed, 1 skipped, 0 failed`, exit `0`.
- full-suite transcript hash: `NOT_RECORDED_BY_RUNNER`; the terminal result was captured in this task output and was not rerun to manufacture a transcript.

## Decision

```text
NEXT_PATH=PATH_C
NEXT_CAMPAIGN=direct-kernel-and-flat-reference-methodology
S3_SOURCE_CHANGED=NO
EXTERNAL_PRS_OPENED=NO
READY_FOR_MERGE=NO
```
