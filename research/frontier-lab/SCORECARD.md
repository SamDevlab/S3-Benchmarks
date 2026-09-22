# Evidence Scorecard V1

Scoring is criterion-based and does not reward diagnostic speed.

| dimension | max | score | basis |
|---|---:|---:|---|
| correctness evidence | 15 | 11 | XSBench hosted/native historical gates and independent oracle; diagnostic native gate pending |
| measurement methodology | 15 | 12 | balanced E/F protocol and warmup isolation; G/H pending |
| workload coverage | 15 | 7 | XSBench plus prior bounded miniapps, not broad closure |
| performance evidence | 15 | 7 | reproducible local E/F observation, no causal attribution yet |
| resource efficiency | 10 | 6 | bounded fixtures and deterministic artifacts |
| portability | 10 | 4 | Linux native evidence exists historically; current diagnostic host unavailable |
| reliability | 10 | 7 | fail-closed rewriter and preserved raw evidence |
| external validation | 5 | 2 | upstream pins and radar; no new external pilot |
| provenance | 5 | 5 | pinned S3, benchmark heads, hashes, raw reports |
| **TOTAL** | **100** | **61** | evidence score, not performance score |

`EVIDENCE_SCORE_BEFORE` was not recalculated under this rubric in the prior
campaign, so no score delta is claimed. `QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE`.
