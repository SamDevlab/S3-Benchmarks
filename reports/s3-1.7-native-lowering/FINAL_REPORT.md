# S3 1.7 Native Lowering Evidence

## Scope

This report records the independent, Linux x86-64 characterization for
`EXP-S3-17-LOWERING-002`. The experiment asks whether the proof-gated native
register-initialization marker elision in S3 1.7 changes code shape or
same-process scalar FFI execution for the three pinned real-world workloads.
It does not claim performance against C or another compiler.

The control is `SamDevlab/S3` at
`4ddc7a64a4c395460181db0e8957f085d8bb12a9`. The candidate is
`SamDevlab/S3` at `39dfbb5d19ecefc7df78da7dc8d3ea8e31d81df4`. Both checkouts
were clean and exact at execution time. The control used a temporary,
two-file CLI/FFI adapter (`ff926c2a1a6b8e238272fe38e7c7183b0d05b6ab7b15169daa2b2689aaf4aa90`)
to expose the same optimization, syntax, and instruction-budget options as the
candidate. It changed no compiler backend sources.

## Protocol

Both builds used the public `ffi-build` command with `-O 1`,
`--source-syntax 0.6`, `--native-policy baseline`, and
`--max-instructions 1000000000`. The budget is pinned to the historical S3
control report at
`reports/s3-1.7-native-lowering-codegen-expansion/evidence/control-4ddc7a6/native-workload-benchmark-v1.json`
(SHA-256 `f1ba247af3e38b9bcc2559c6f298b0116ad345b2f55842758c87b09f119ab06e`).

The protocol used 3 warmups, 21 paired samples, 1,000 calls per sample, seed
1701, and 10,000 paired bootstrap resamples. Timing includes `ctypes`
dispatch equally and excludes setup and compilation. Reference correctness
was checked before timing. External fixture and dataset hashes are pinned in
the manifest.

Host: Linux x86-64, AMD Ryzen 5 3400G with Radeon Vega Graphics, kernel
`7.0.0-31-generic`, Python 3.13.15.

## Results

| Workload | Correctness / output equality | Static instructions control/candidate | Memory-operand instructions | Branches | Median ns/call control/candidate | Control/candidate ratio | 95% paired interval | Classification |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `energy.pv-timeseries-aggregation.v1` | PASS / equal | 2763 / 2763 | 953 / 953 | 789 / 789 | 19982.579 / 20296.314 | 0.98107 | [0.95671, 0.99785] | NO_MATERIAL_CHANGE_WITHIN_5_PERCENT |
| `engineering.point-cloud-summary.v1` | PASS / equal | 4746 / 4746 | 1601 / 1601 | 1367 / 1367 | 19065.913 / 19314.020 | 0.97417 | [0.94534, 1.00333] | INCONCLUSIVE |
| `geospatial.raster-window-statistics.v1` | PASS / equal | 5688 / 5688 | 1898 / 1898 | 1715 / 1715 | 13351.102 / 13637.392 | 0.97419 | [0.95977, 1.01872] | NO_MATERIAL_CHANGE_WITHIN_5_PERCENT |

Correctness passed for both binaries against the independent references, and
control and candidate outputs were equal for every workload. Static counts
were unchanged in this workload set. The observed candidate medians were
approximately 1.9% to 2.6% slower, but the predeclared 5% materiality gate
does not support a material-regression or speedup claim. One workload is
inconclusive; the other two are classified as no material change within the
threshold.

## Invalid Preliminary Run

`EXP-S3-17-LOWERING-001` is retained unchanged at
`results/EXP-S3-17-LOWERING-001.json` (SHA-256
`13881ae714af83cb56d1d1abba5b1b8a642494ecaf7c52aac6aa21687bb2dad5`). Its
manifest declared O1, but the then-current FFI helper rebuilt the program at
the default O0. Therefore that run is diagnostic only and is not evidence for
the O1 protocol. The defect was fixed in S3 commit
`39dfbb5d19ecefc7df78da7dc8d3ea8e31d81df4`; the corrected command and options
are recorded in `...002`.

The valid raw result is `results/EXP-S3-17-LOWERING-002.json` (SHA-256
`571275d03083baa600008916a3d9e7ee4b501b1cdfbfc99f32812963c89ee8cb`). The
record includes the exact build commands, source SHAs, adapter hash, host,
toolchain, outputs, structural metrics, paired samples, and classifications.

## Conclusion

For these three pinned workloads and this protocol, the experiment does not
show reduced static instruction, memory-operand, or branch counts and does
not establish a material runtime improvement. This is a bounded negative or
inconclusive result, not evidence that the transformation cannot help other
program shapes. No C-relative speedup claim is made.

## S3 Campaign Cross-Reference

- S3 repository: `SamDevlab/S3`
- S3 source freeze: `39dfbb5d19ecefc7df78da7dc8d3ea8e31d81df4`
- S3 campaign report:
  `reports/s3-1.7-native-lowering-codegen-expansion/FINAL_REPORT.md`
- S3 review PR: #321, Draft, base `main`:
  https://github.com/SamDevlab/S3/pull/321
- This report and experiment are published in S3-Benchmarks PR #25, Draft,
  base `main`.
