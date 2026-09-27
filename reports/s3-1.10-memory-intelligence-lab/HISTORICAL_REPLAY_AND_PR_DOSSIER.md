# S3-Benchmarks 1.10 Historical Replay and PR Dossier

## EXP-S3-110-HIST-001

Five exact historical S3 commits were independently checked out, built, and
validated serially on the Linux x86-64 guest using the 1.9 executor contract.
Each version passed all three workload correctness gates. The executor
verified clean checkouts, compiler source hashes, and inventories of 31
native artifacts per revision. The five raw result JSONs and compact matrix
are retained under `evidence/historical-replay-v1/`; native binaries are not
retained, but every generated artifact has a recorded byte count and SHA-256
in the matrix.

| S3 line | Exact source SHA | Source tree | Raw result SHA-256 | Bytes |
| --- | --- | --- | --- | ---: |
| 1.5 | `c924148c6d95948778351c7dd1362259caff670c` | `b54be6f1dc9de47a788f26468c5eb30f7266a646` | `292bccad36eab55eccf2dea2528b02b0a382388211e450c7f98f223f677cd2fe` | 71,638 |
| 1.6 | `cb88a8036af1bcdc026db193590cb961bee4737d` | `a8b1cd6ee25b38f98532155aa123556ae8885f62` | `0ad514a9451e18f652098653e5d53d137d9bd68bf010790d0514e2e75426eaf1` | 71,595 |
| 1.7 | `39dfbb5d19ecefc7df78da7dc8d3ea8e31d81df4` | `b7e0e77be6984f031491c9085743173c52ff4b4a` | `e7c26ea14b012fa7bd8a639fa463d63f60e94819a35c9cc07bd60eac08ebc13f` | 71,597 |
| 1.8 | `b8f446a5ea2b24b948a263cb955f426c5d0f48ce` | `ee71518080df40ff98c28fa07f7f9f8301d7943a` | `a749a4e26cb18a1953c1965c2a9fc7ed30d6f47fea4ccbfb221c6c1d66883f8d` | 71,596 |
| 1.9 | `211b1aecec756be42516322429720018f54001e7` | `08289d214832e856d46e14ef941239649e9f4063` | `550e7ca33a45159ede49086595cf51525c0acf02a2c807e01de0673db05406df` | 71,559 |

The common protocol hash is
`91ccec27588c1a4e5993c3b894fcf74d99c0de30eb9892bfc260f685413acf67`;
the host, toolchain, workload set, dataset hashes, sample protocol, and all
three baseline O1 output hashes match across the five revisions. All runs
used 3 warmups, 21 samples, and 1,000 iterations per sample. The raw result
hashes match the executor matrix's pinned values.

### Baseline O1 characterization

Values are medians in ns/call; `.text` bytes and machine instruction counts
are static metrics from the common extraction fields. Timing rows are
descriptive only: matrix execution was grouped serially by ascending SHA,
without cross-version interleaving. Therefore the index sets
`direct_cross_version_timing_delta_supported=false` and makes no causal
speedup claim. Static object counts use the same extraction protocol. The
1.5 benchmark script differs from 1.6–1.9 only in its handling of two legacy
budget counter symbol names; the reported `.text` and static instruction
fields are unaffected.

| S3 line | Workload | Median ns/call | `.text` bytes | Static instructions |
| --- | --- | ---: | ---: | ---: |
| 1.5 | energy | 43,471.585 | 40,970 | 3,048 |
| 1.5 | point cloud | 34,414.684 | 65,774 | 5,233 |
| 1.5 | raster | 28,039.393 | 78,460 | 6,311 |
| 1.6 | energy | 43,246.280 | 40,970 | 3,048 |
| 1.6 | point cloud | 37,670.200 | 65,774 | 5,233 |
| 1.6 | raster | 28,989.777 | 78,460 | 6,311 |
| 1.7 | energy | 18,469.099 | 36,304 | 2,754 |
| 1.7 | point cloud | 14,264.300 | 58,112 | 4,732 |
| 1.7 | raster | 11,786.882 | 68,491 | 5,666 |
| 1.8 | energy | 17,647.827 | 36,304 | 2,754 |
| 1.8 | point cloud | 13,950.703 | 58,112 | 4,732 |
| 1.8 | raster | 11,860.500 | 68,491 | 5,666 |
| 1.9 | energy | 17,809.520 | 36,304 | 2,754 |
| 1.9 | point cloud | 15,389.616 | 58,112 | 4,732 |
| 1.9 | raster | 12,081.788 | 68,491 | 5,666 |

The static evidence shows a step between the 1.6 and 1.7 pins: `.text` and
static instruction counts fall in all three kernels. The observed timing
medians also differ, but the grouped one-pass replay cannot establish that
the code change caused the timing difference. Replicated/interleaved runs
would be needed for that inference. S3 1.10 is not included because its
functional candidate has not yet been frozen to a commit SHA.

## Historical Bench PR recommendations

States below were read from GitHub on 2026-09-27. No PR was edited, rebased,
closed, marked ready, or merged.

| PR | Current scope/state | Superseded vs. still unique | Recommendation |
| --- | --- | --- | --- |
| [#15](https://github.com/SamDevlab/S3-Benchmarks/pull/15) | Draft, open, base `main`; Benchmarks 2.0 Evidence Lab foundation. | The later 1.9 executor supplies a more recent pinned-SHA native checkout/build/correctness path. PR #15 still uniquely contributes protocol-v2 measurement/provenance/registry/result contracts, workload manifests, and the independent RMSD correctness adapter. Its broader candidate registry does not mean those candidates are executable. | `KEEP_OPEN_WITH_REASON`: retain as the foundational protocol/RMSD proposal; consider integrating after reviewing overlap with the 1.9 and 1.10 lab contracts. Do not merge automatically. |
| [#23](https://github.com/SamDevlab/S3-Benchmarks/pull/23) | Draft, open, base `research/benchmarks-2.2.3-budget-generalization`; benchmark-side exact global countdown experiment. | Its P1 safety result remains a useful exact-budget experiment, but the cross-workload material-recovery gate failed and P2 was not implemented due absent exact segment mapping. It is not a memory/value-locality facility. | `KEEP_OPEN_WITH_REASON`: preserve as a non-production research record; do not promote or merge into main while performance selection failed and the base is another research branch. |
| [#24](https://github.com/SamDevlab/S3-Benchmarks/pull/24) | Draft, open, base `research/benchmarks-2.2.3-budget-generalization`; independent Linux x86-64 exact-segment validation. | Its six RMSD/XSBench/JSMN O0/O1 correctness/performance cells are distinct validation evidence; it also carries prerequisite commits in its history. It depends on the same budget research line as #23 and does not extend the memory lab. | `KEEP_OPEN_WITH_REASON`: preserve the independent validation evidence; resolve the prerequisite/base-branch relationship and promotion decision deliberately, without rebasing or merging as part of 1.10. |

These are evidence-based recommendations only. This campaign has made no
change to PR #15, #23, or #24.
