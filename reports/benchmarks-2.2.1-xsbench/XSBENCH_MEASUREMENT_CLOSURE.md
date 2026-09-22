# XSBench Measurement Closure

## Decision

```text
CAMPAIGN=S3_BENCHMARKS_2_2_1_1_XSBENCH_MEASUREMENT_CLOSURE
WORKLOAD=scientific.xsbench.compatible_lookup.medium
WORK_UNIT=XS_LOOKUP
ARTIFACTS=FROZEN_AND_REUSED
CALIBRATION=NO_COMMON_STABLE_CONTROL_WINDOW
RUN_C=INCOMPLETE_AT_INVALID_K
RUN_D=NOT_RUN
FFI_REPRODUCIBILITY=OPEN
STATUS=CORRECTNESS_QUALIFIED_MEASUREMENT_WINDOW_UNAVAILABLE
READY_FOR_MERGE=NO
```

The prior A/B correctness and provenance evidence remains valid and is not
overwritten. The closure attempt did not produce a valid C/D comparison.

## Calibration finding

The first calibration selected K=500000 incorrectly. Its `slowest_s3_seconds`
calculation treated missing elapsed samples as zero, so the row was marked as
passing even though both S3 variants terminated with the frozen runtime's
10,000,000,000-instruction limit. That calibration and the resulting Run C
are preserved unchanged under:

```text
reports/benchmarks-2.2.1-xsbench/raw/xsbench-measurement-closure-20260921-221600/
```

The bounded recalibration required all four variants to finish with
`status=PASS`. It found:

| K | Fastest control (ms) | S3 outcome | Window |
|---:|---:|---|---|
| 250000 | 54.748923 | O0/O1 instruction limit | invalid |
| 300000 | 44.764624 | O0/O1 instruction limit | invalid |
| 400000 | 87.444239 | O0/O1 instruction limit | invalid |
| 450000 | 109.088227 | O0/O1 instruction limit | invalid |

Thus the control threshold first becomes true at K=450000, but the S3
artifacts are no longer executable at that K. K=200000 completed for S3 in
the original calibration, but its fastest control was only 46.860272 ms.
There is no K satisfying both protocol constraints with the frozen artifacts.

The S3 failure is deterministic runtime instruction-limit exhaustion, not an
environment-variability classification and not a correctness mismatch.

## Run C evidence

Run C used K=500000, five warmups, thirty planned repetitions, CPU 0, and the
frozen artifacts. `CLANG_O2` and `GCC_O2` completed 30 samples, with medians
105226549 ns and 133851229 ns respectively. Both S3 variants produced zero
valid samples because their calls terminated with the instruction-limit
error. The raw record is:

```text
reports/benchmarks-2.2.1-xsbench/raw/xsbench-measurement-closure-20260921-221600/run_c.json
```

Run D was correctly not started because the common measurement window was
invalid. No C/D delta, reproducibility pass, native speedup claim, or pressure
causality is promoted.

## Protocol and provenance

- benchmark functional head: `edbce77725e1193e602d93258431e4fae85d6694`
- benchmark branch head before this evidence: `6508a542a033b417aceedd78f34b017198576650`
- S3 source changed: `NO`
- frozen driver and four library hashes: recorded in both calibration artifact manifests
- exact benchmark machine fingerprint: `cae6d65e71c97a0b0bbc1d83697faf67958777f50b7f6fc922e5de4b175abade`
- timer: `CLOCK_MONOTONIC_RAW`, resolution `1 ns`
- CPU affinity: `0`
- `perf` binary: available
- `PERF_PERMISSION=DENIED_OR_UNSUPPORTED_BY_HOST_POLICY`
- full suite: inherited prior evidence `52 passed, 1 skipped`; no full suite was rerun

The temporary calibration helper used during the bounded investigation was
removed. No benchmark source, S3 source, or prior A/B raw evidence was
modified.

## Next path

The next measurement decision must address the incompatibility between the
control-duration threshold and the frozen S3 instruction budget. It must not
silently relax the threshold, increase the runtime instruction limit, or
replace the medium workload. Until that protocol question is resolved,
`READY_FOR_MERGE=NO`.
