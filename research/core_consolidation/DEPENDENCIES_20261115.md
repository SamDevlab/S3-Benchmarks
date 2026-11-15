# S3 Core Consolidation — PR dependency map

Evidence date: 2026-11-15. Source: saved authenticated GitHub CLI snapshots.

**This is an inventory, not approval to merge any PR.**

## Key finding

- S3 `main` is an old historical base, not a qualified current CPU-performance baseline.
- Historical main: `9b39c7070d7b`.
- Candidate stack V18: `1a323a033c36`.
- Main…V18 commit counts (left/right): `0	663`.
- V12 has sibling candidate branches on the V11 base. Review their overlap before integration.
- PR #409 touches 9 files; PR #410 touches 8, with **zero shared file paths** in the GitHub PR diff. This is NOT semantic compatibility proof.
- V14–V18 are opt-in studies; neither their standalone correctness nor their speedups justify a global enable.

## S3 dependency chain (observed PR targets)

| Stage | S3 | S3-Benchmarks | Relat-rio | Screening |
|---|---|---|---|---|
| V11 | [#408](https://github.com/SamDevlab/S3/pull/408) | [#53](https://github.com/SamDevlab/S3-Benchmarks/pull/53) | [#69](https://github.com/SamDevlab/Relat-rio/pull/69) | REVIEW_EXPERIMENTAL |
| V12 | [#409](https://github.com/SamDevlab/S3/pull/409), [#410](https://github.com/SamDevlab/S3/pull/410) | [#54](https://github.com/SamDevlab/S3-Benchmarks/pull/54), [#55](https://github.com/SamDevlab/S3-Benchmarks/pull/55) | [#70](https://github.com/SamDevlab/Relat-rio/pull/70), [#71](https://github.com/SamDevlab/Relat-rio/pull/71) | SPLIT_BRANCH_REVIEW_REQUIRED |
| V13 | [#411](https://github.com/SamDevlab/S3/pull/411) | [#56](https://github.com/SamDevlab/S3-Benchmarks/pull/56) | [#72](https://github.com/SamDevlab/Relat-rio/pull/72) | REVIEW_EXPERIMENTAL |
| V14 | [#412](https://github.com/SamDevlab/S3/pull/412) | [#57](https://github.com/SamDevlab/S3-Benchmarks/pull/57) | [#73](https://github.com/SamDevlab/Relat-rio/pull/73) | NO_GO_FOR_DEFAULT_GLOBAL_ENABLE |
| V15 | [#413](https://github.com/SamDevlab/S3/pull/413) | [#58](https://github.com/SamDevlab/S3-Benchmarks/pull/58) | [#74](https://github.com/SamDevlab/Relat-rio/pull/74) | GO_EXPERIMENTAL_ONLY |
| V16 | [#414](https://github.com/SamDevlab/S3/pull/414) | [#59](https://github.com/SamDevlab/S3-Benchmarks/pull/59) | [#75](https://github.com/SamDevlab/Relat-rio/pull/75) | GO_EXPERIMENTAL_ONLY |
| V17 | [#415](https://github.com/SamDevlab/S3/pull/415) | [#60](https://github.com/SamDevlab/S3-Benchmarks/pull/60) | [#76](https://github.com/SamDevlab/Relat-rio/pull/76) | GO_EXPERIMENTAL_ONLY |
| V18 | [#416](https://github.com/SamDevlab/S3/pull/416) | [#61](https://github.com/SamDevlab/S3-Benchmarks/pull/61) | [#77](https://github.com/SamDevlab/Relat-rio/pull/77) | GO_EXPERIMENTAL_WITH_CODE_SIZE_REGRESSIONS |

## Explicit PR-to-PR base edges

| Repo | PR | Parent PR, if open | Base branch | Draft |
|---|---|---|---|---|
| S3 | [#408](https://github.com/SamDevlab/S3/pull/408) | #407 | `exp/s3-v10-gf2-source-certificates` | True |
| S3 | [#409](https://github.com/SamDevlab/S3/pull/409) | #408 | `exp/s3-v11-core-auto-strategy` | True |
| S3 | [#410](https://github.com/SamDevlab/S3/pull/410) | #408 | `exp/s3-v11-core-auto-strategy` | True |
| S3 | [#411](https://github.com/SamDevlab/S3/pull/411) | #410 | `exp/s3-v12-core-native` | True |
| S3 | [#412](https://github.com/SamDevlab/S3/pull/412) | #411 | `exp/s3-v13-native-assembly` | True |
| S3 | [#413](https://github.com/SamDevlab/S3/pull/413) | #412 | `exp/s3-v14-core-x86-peephole` | True |
| S3 | [#414](https://github.com/SamDevlab/S3/pull/414) | #413 | `exp/s3-v15-slice-bounds-reuse` | True |
| S3 | [#415](https://github.com/SamDevlab/S3/pull/415) | #414 | `exp/s3-v16-interval-bounds` | True |
| S3 | [#416](https://github.com/SamDevlab/S3/pull/416) | #415 | `exp/s3-v17-dynamic-interval` | True |
| S3-Benchmarks | [#53](https://github.com/SamDevlab/S3-Benchmarks/pull/53) | #52 | `exp/s3-v10-algorithm-discovery` | True |
| S3-Benchmarks | [#54](https://github.com/SamDevlab/S3-Benchmarks/pull/54) | #53 | `exp/s3-v11-core-gpu` | True |
| S3-Benchmarks | [#55](https://github.com/SamDevlab/S3-Benchmarks/pull/55) | #53 | `exp/s3-v11-core-gpu` | True |
| S3-Benchmarks | [#56](https://github.com/SamDevlab/S3-Benchmarks/pull/56) | #55 | `exp/s3-v12-core-benchmarks` | True |
| S3-Benchmarks | [#57](https://github.com/SamDevlab/S3-Benchmarks/pull/57) | #56 | `exp/s3-v13-native-gpu-benchmarks` | True |
| S3-Benchmarks | [#58](https://github.com/SamDevlab/S3-Benchmarks/pull/58) | #57 | `exp/s3-v14-native-s3-vs-gpu` | True |
| S3-Benchmarks | [#59](https://github.com/SamDevlab/S3-Benchmarks/pull/59) | #58 | `exp/s3-v15-native-slice-bench` | True |
| S3-Benchmarks | [#60](https://github.com/SamDevlab/S3-Benchmarks/pull/60) | #59 | `exp/s3-v16-stencil-interval-bench` | True |
| S3-Benchmarks | [#61](https://github.com/SamDevlab/S3-Benchmarks/pull/61) | #60 | `exp/s3-v17-dynamic-stencil` | True |
| Relat-rio | [#69](https://github.com/SamDevlab/Relat-rio/pull/69) | #68 | `exp/s3-v10-algorithm-discovery-research` | True |
| Relat-rio | [#70](https://github.com/SamDevlab/Relat-rio/pull/70) | #69 | `exp/s3-v11-core-research` | True |
| Relat-rio | [#71](https://github.com/SamDevlab/Relat-rio/pull/71) | #69 | `exp/s3-v11-core-research` | True |
| Relat-rio | [#72](https://github.com/SamDevlab/Relat-rio/pull/72) | #71 | `exp/s3-v12-core-research` | True |
| Relat-rio | [#73](https://github.com/SamDevlab/Relat-rio/pull/73) | #72 | `exp/s3-v13-native-gpu-research` | True |
| Relat-rio | [#74](https://github.com/SamDevlab/Relat-rio/pull/74) | #73 | `exp/s3-v14-core-research` | True |
| Relat-rio | [#75](https://github.com/SamDevlab/Relat-rio/pull/75) | #74 | `exp/s3-v15-research` | True |
| Relat-rio | [#76](https://github.com/SamDevlab/Relat-rio/pull/76) | #75 | `exp/s3-v16-interval-research` | True |
| Relat-rio | [#77](https://github.com/SamDevlab/Relat-rio/pull/77) | #76 | `exp/s3-v17-dynamic-interval-research` | True |

## Gates

1. Establish two pinned baselines: historic `main` for regression history and V18 as a *candidate*, not as an approved release.
2. Reproduce the known legacy test failures independently; never hide untested failures in a green label.
3. Evaluate dependencies oldest-first; audit the V12 split, then V13…V18.
4. Classify each PR as GO_EXPERIMENTAL, READY_FOR_INTEGRATION, NO_GO, or BLOCKED with a supporting artifact.
5. No global default enablement for V14–V18. V18 has code size and native timing regressions.
6. Use local WSL + Remote Desktop Commander. No paid runners or GitHub Actions gating.
7. No automatic merge, deploy, or reopening Compact/DOOM.

## Operational WIP

Kanban canonical branch: `feat/native-kanban-flow-v1-20261111`, PR #38 in Relat-rio.
Agent WIP maximum 2, one per owner. Existing non-S3 priorities are not silently overwritten.
All development/research tasks must have done_when, stop_when, next_action and dated review.
