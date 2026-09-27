# S3-Benchmarks 1.8 Research Questions and Baseline

## Provenance

- Lab campaign base: `2ca7b7802c630fec655e7826462e319fb773014c` (merge of PR #25).
- S3 campaign base: `f1342592aef1be7cc9fe0d390e0f3c6fc266af5a` (merge of PR #321).
- S3 1.7 source candidate: `39dfbb5d19ecefc7df78da7dc8d3ea8e31d81df4`.
- Inherited independent experiment: `EXP-S3-17-LOWERING-002`.

## Evidence-Lab Questions

| ID | Question | Status | Qualification rule |
| --- | --- | --- | --- |
| RQ-L1 | Can artifacts be attributed across source, IR, Assembly and native regions without inventing lineage? | OPEN | Preserve unknown ranges and report coverage. |
| RQ-L2 | Which structural metrics predict measured runtime for the continuity kernels? | OPEN | Paired, same-host, same-workload evidence; no universal model claim. |
| RQ-L3 | Does the S3 1.6 PER optimization change exact/hybrid historical comparisons? | OPEN | Re-run only with validated comparable historical protocol; otherwise classify unavailable. |
| RQ-L4 | Can compiler experiments and hypotheses be replicated across versions? | OPEN | Pinned SHAs, dataset, harness, toolchain, and raw samples. |
| RQ-L5 | Can an automated experiment engine safely perform ablations? | NOT_STARTED | First establish correctness, provenance, and reproducibility invariants. |

## Inherited 1.7 Observation

`EXP-S3-17-LOWERING-002` compared the 1.7 source candidate against its pinned
control on the continuity workloads. Correctness passed. Static instruction,
memory-operand and branch counts were unchanged. Paired medians changed by
about 1.6% for energy, 1.3% for point cloud, and 2.1% for raster in the
slower direction; none crossed the 5% materiality threshold, so the result
does not establish a regression or speedup.

The marker-elision proof admitted no reads in the three hot reference-bearing
functions. The result is therefore `NO_EFFECT_OBSERVED_WITHIN_PROTOCOL` for
those workloads and that candidate, not a general result about register-init
checks.

## Evidence Policy

- No synthetic dynamic counters are inferred from static Assembly or machine
  instruction counts.
- Preserve original 1.7 records; 1.8 recharacterizations receive new experiment
  IDs and immutable raw output paths.
- Control and candidate must pin both repositories, workload data, compiler,
  and measurement settings.
- Results without directly comparable historical protocol remain
  `NOT_COMPARABLE`, not backfilled with invented measurements.
