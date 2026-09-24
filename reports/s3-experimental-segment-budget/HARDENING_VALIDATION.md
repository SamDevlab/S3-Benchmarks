# Exact Segment Budget Hardening Validation

## Decision

`CURRENT_P2_RETAINED`. The single authorized P2H candidate passed correctness, reproducibility, P0 identity, segment-plan identity, and the predeclared runtime guard, but did not produce useful code-size or hot-layout recovery. No second hardening design is authorized. The budget-architecture search remains closed; next is a separate production-readiness review of existing P2.

## Frozen provenance and protocol

| Item | Value |
| --- | --- |
| Control S3 source | `e07d0b5464bf472b2ca18993f3e196a234ff0fc5` |
| P2 S3 source | `1a76e341098b54a639fec22eecea362cc243c46f` |
| P2H S3 source | `6f320242e3c1ebbb0d2ac5d6d85272ab375e5333` |
| Benchmark source | `c5b35775b62847bf2f535d61ea68db4a774bf838` |
| Benchmark base | `8fc0aba50ca48d3f7171bdf49395df3cd880626a` |
| Host fingerprint | `75237604ad5507b026b5e148a637c40db9f1f32d2ebd32e267f80afc1b207c89` |
| Host | Ubuntu 26.04 x86-64, AMD Ryzen 5 3400G, Python 3.14.4 |
| Timing | `CLOCK_MONOTONIC_RAW`, CPU affinity 0, 5 external warmups, 0 inline warmups, 30 fresh-process samples × 2 independent sessions, balanced interleaving |
| Workloads | RMSD K=2,000,000; XSBench K=750,000; JSMN K=1,250,000 |
| Run | `segment-budget-20260923-225935-431096547`; terminal output at 2026-09-24 03:53:38 UTC; elapsed approximately 4h54m |

P0/P2 were compiled independently from identical source and parsed workload; their only configuration difference was `instruction_budget_mode`. All correctness oracles passed for P0, P2, P2H, and PNEG in all three workloads. All six timing cells passed reproducibility. P0 byte identity passed. P2/P2H segment plans matched exactly, including counts: JSMN O0 386/298 fast/slow, O1 356/298; RMSD O0/O1 22/17; XSBench O0 35/27, O1 34/27. P2H retained at least 91.32% budget-excess recovery in every cell, above the frozen 50% minimum.

## Timings and hardening thresholds

Times below are arithmetic means of the two session medians, seconds per fixed workload execution. Added-text recovery is intentionally not clipped; negative values mean P2H grew relative to P2.

| Workload | Opt | P0 s | P2 s | P2H s | PNEG s | P2H/P2 | Added-text recovery | Budget-excess recovery |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| JSMN | O0 | 25.9243 | 13.1483 | 13.1682 | 12.0286 | 1.001516 | -0.1568% | 91.7987% |
| JSMN | O1 | 25.2481 | 12.8250 | 12.9235 | 11.7521 | 1.007682 | -0.1557% | 91.3202% |
| RMSD | O0 | 14.1407 | 5.2742 | 5.1269 | 5.5619 | 0.972085 | -0.3689% | 105.0707% |
| RMSD | O1 | 14.1858 | 5.0503 | 5.1180 | 5.5224 | 1.013410 | -0.3689% | 104.6673% |
| XSBench | O0 | 15.4606 | 6.9138 | 6.7961 | 6.7610 | 0.982988 | -0.1139% | 99.5955% |
| XSBench | O1 | 15.0930 | 7.4033 | 7.2517 | 7.0220 | 0.979516 | -0.1052% | 97.1546% |

All P2H/P2 ratios are within the predeclared 1.05 ceiling. That safety/performance result does not offset the absent structural win: all added-text and hot-text recovery values are negative, failing the predeclared 25% materiality threshold.

The hot-layout materiality threshold was also frozen at 25%; none of the six cells meets it. The previous hypothesis ledger remains unchanged: H1 `CONFIRMED`; H2 `CONFIRMED_CAUSAL_XSBENCH`; H3 `NOT_CONFIRMED`; H4/H5 `OPEN`; H6 `WEAKENED`; H7 `CONFIRMED_GENERAL`; H8 `CONFIRMED_SAFE_NOT_MATERIAL`; H9 `CONFIRMED_EXACT_MAPPING`; H10 `CONFIRMED`; H11 `CONFIRMED_MATERIAL`. H12 is `SAFE_NOT_STRUCTURALLY_MATERIAL`; H12A is `NOT_CONFIRMED`. Evidence Score remains 89/100 under the existing rubric. `QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE`.

## Static structure

Each tuple is `total executable text bytes / hot .text bytes / cold executable text bytes / total native instructions / fast-path instructions / slow-path instructions`. P2H had zero detected cold executable bytes in every cell.

| Workload | Opt | P0 | P2 | P2H | PNEG |
| --- | --- | --- | --- | --- | --- |
| JSMN | O0 | 309721/309721/0/50743/50743/0 | 490209/490209/0/80984/57165/23819 | 490492/490492/0/80984/57129/23855 | 235343/235343/0/40843/40843/0 |
| JSMN | O1 | 306079/306079/0/50063/50063/0 | 485245/485245/0/79991/56416/23575 | 485524/485524/0/79991/56380/23611 | 233151/233151/0/40355/40355/0 |
| RMSD | O0 | 19413/19381/0/3983/3983/0 | 27004/26972/0/5304/4223/1081 | 27032/27000/0/5304/4222/1082 | 16017/15985/0/3531/3531/0 |
| RMSD | O1 | 19413/19381/0/3983/3983/0 | 27004/26972/0/5304/4223/1081 | 27032/27000/0/5304/4222/1082 | 16017/15985/0/3531/3531/0 |
| XSBench | O0 | 72468/72420/0/12812/12812/0 | 111102/111054/0/19629/14148/5481 | 111146/111098/0/19629/14147/5482 | 56829/56781/0/10728/10728/0 |
| XSBench | O1 | 72773/72725/0/12812/12812/0 | 111733/111685/0/19633/14148/5485 | 111774/111726/0/19633/14147/5486 | 57164/57116/0/10732/10732/0 |

P2H grew total executable text by 28 bytes for RMSD, 41–44 bytes for XSBench, and 279–283 bytes for JSMN. P2H and P2 static instruction totals are identical in all six cells; P2H shifts one instruction from slow to fast or vice versa by at most one. This run does not confirm cold placement or code-size compression.

## Final disposition and limitations

- E0, P0 byte identity, segment-plan identity, correctness, and timing reproducibility: PASS.
- Runtime non-regression (`P2H/P2 <= 1.05`): PASS in six of six cells.
- Retained budget recovery (`>= 0.50`): PASS in six of six cells.
- Added-text/hot-layout materiality (`>= 0.25`): FAIL in six of six cells; measured recoveries are negative.
- H12A: `NOT_CONFIRMED`; H12: `SAFE_NOT_STRUCTURALLY_MATERIAL`.
- Hardening outcome: `CURRENT_P2_RETAINED`; no candidate two and no new budget architecture.
- Full benchmark suite at c5: transcript summary `106 passed, 1 skipped in 1.48s`. The outer wrapper then failed while parsing an invalid shell `exit` expression, so a separate pytest exit code was not captured. This was not rerun. Transcript SHA-256: `55903d3cccb2355b2890d3c22ff01e5381f421a208645a86c6178d2ad6d1026a`.
- Raw evidence: 124 manifest entries, 88 MiB run directory plus manifest; manifest SHA-256 `3ca2fc0cf04b5579e2c0b24d3fc066e30e596cfcd356b58b99b842ab522a15a4`. Runner transcript SHA-256 `978b32d88d741b37ae97a9084af1a724708d868539479338ff284f1dd5db7388`. Consolidated runner result SHA-256 `ce7c91fa9adaf0604d0a49fd3ba87f078913c12fe2366751c15081d1673659f3`.
- S3 full suite at P2H source: 4,375 passed, 1 skipped, exit 0; full transcript and hash are recorded in the S3 hardening report.
- PR #310 remains OPEN/DRAFT/UNMERGED. Its latest CI at P2H SHA has three pre-step workflow failures (all jobs `steps=[]`, completed within approximately 3–5 seconds); cause remains unattributed and no rerun was made.
- This is not production promotion. `production_ready=false`; next campaign is `S3_EXACT_SEGMENT_BUDGET_PRODUCTION_READINESS_REVIEW`, covering default-mode selection, API, concurrency contract, CI, cross-platform scope, limits, compatibility, documentation/ADR, migration, release and rollback.

The machine-readable per-cell and per-artifact data is in `SEGMENT_BUDGET_HARDENING_RESULT.json`; the immutable raw directory and runner/suite transcripts are adjacent under `raw/`.
