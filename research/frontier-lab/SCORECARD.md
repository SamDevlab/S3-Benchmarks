# Evidence Scorecard V1

Scoring is criterion-based and does not reward diagnostic speed.

| dimension | max | score | basis |
|---|---:|---:|---|
| correctness evidence | 15 | 15 | XSBench baseline, diagnostic, and frame diagnostic native gates passed against the independent oracle |
| measurement methodology | 15 | 15 | balanced fresh-process G/H and I/J protocols, warmups isolated, monotonic raw clock, fixed affinity |
| workload coverage | 15 | 7 | XSBench plus prior bounded miniapps, not broad closure |
| performance evidence | 15 | 12 | H2 causal G/H attribution is complete; H3 was tested but not confirmed; no production speed claim |
| resource efficiency | 10 | 6 | bounded fixtures and deterministic artifacts |
| portability | 10 | 7 | Linux x86-64 native evidence and guest provenance are complete; no cross-platform closure |
| reliability | 10 | 9 | fail-closed instruction/frame rewriters, focused tests, independent reproducibility, preserved raw evidence |
| external validation | 5 | 2 | upstream pins and radar; no new external pilot |
| provenance | 5 | 5 | pinned S3, benchmark heads, hashes, raw reports |
| **TOTAL** | **100** | **77** | evidence score, not performance score |

`EVIDENCE_SCORE_BEFORE=61`, `EVIDENCE_SCORE_AFTER=77`, and
`EVIDENCE_SCORE_DELTA=16`. Workload breadth and external validation were not
inflated. `QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE`.
