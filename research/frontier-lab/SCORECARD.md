# Evidence Scorecard V1

Scoring is criterion-based and does not reward diagnostic speed.

| dimension | max | score | basis |
|---|---:|---:|---|
| correctness evidence | 15 | 15 | XSBench baseline, diagnostic, and frame diagnostic native gates passed against the independent oracle |
| measurement methodology | 15 | 15 | balanced fresh-process G/H and I/J protocols, warmups isolated, monotonic raw clock, fixed affinity |
| workload coverage | 15 | 15 | Three workload classes have correctness-gated, reproducible budget causality: RMSD, XSBench, and JSMN |
| performance evidence | 15 | 14 | Per-workload O0/O1 causal shares and paired sessions are complete; no production speed claim and no dynamic instruction count |
| resource efficiency | 10 | 6 | bounded fixtures and deterministic artifacts |
| portability | 10 | 7 | Linux x86-64 native evidence and guest provenance are complete; no cross-platform closure |
| reliability | 10 | 9 | fail-closed instruction/frame rewriters, focused tests, independent reproducibility, preserved raw evidence |
| external validation | 5 | 3 | RMSD and JSMN upstream pins, controls, and semantics are recorded; tracked RMSD batch composition remains deferred |
| provenance | 5 | 5 | pinned S3, benchmark heads, hashes, raw reports |
| **TOTAL** | **100** | **89** | evidence score, not performance score |

`EVIDENCE_SCORE_BEFORE=77`, `EVIDENCE_SCORE_AFTER=89`, and
`EVIDENCE_SCORE_DELTA=12`. Workload breadth is bounded to three tested
classes; no performance index was created. `QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE`.
