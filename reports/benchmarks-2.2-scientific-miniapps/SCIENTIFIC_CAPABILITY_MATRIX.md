# Scientific Capability Matrix

The matrix below records only capabilities exercised by the bounded Phase B
protocol. It does not promote timing or compiler optimization conclusions.

| Workload family | Correctness status | Hosted O0/O1 | Linux native canary | Timing | Promotion |
| --- | --- | --- | --- | --- | --- |
| RMSD single | PASS | PASS | PASS | NOT_RUN | Phase B |
| RMSD batch | PASS | PASS | PASS | NOT_RUN | Phase B |
| RMSD matrix | PASS | PASS | PASS | NOT_RUN | Phase B |
| XSBench | AUDIT_ONLY | NOT_RUN | NOT_RUN | NOT_RUN | Deferred provenance review |
| miniBUDE | AUDIT_ONLY | NOT_RUN | NOT_RUN | NOT_RUN | Deferred provenance review |
| miniMD | READINESS_AUDIT_DEFERRED | NOT_RUN | NOT_RUN | NOT_RUN | Deferred |

The RMSD expansion contains `SMALL`, `MEDIUM`, `LARGE`, `BATCH_LARGE`, and
`MATRIX_LARGE` deterministic profiles. Every promoted profile uses a flat
`f64_vector` layout and an explicit index mapping.
