# Global Pressure Map V1

This map records evidence availability, not inferred causes.

| workload | instrumentation | frame | FFI | bounds/indexing | memory/register | status |
|---|---|---|---|---|---|---|
| RMSD | NOT_MEASURED | NOT_MEASURED | OBSERVED | NOT_MEASURED | NOT_MEASURED | existing readiness/native foundation |
| BabelStream | NOT_MEASURED | NOT_MEASURED | OBSERVED | NOT_MEASURED | NOT_MEASURED | existing direct-kernel evidence |
| PRK NStream | NOT_MEASURED | NOT_MEASURED | OBSERVED | NOT_MEASURED | NOT_MEASURED | existing direct-kernel evidence |
| PolyBench GEMM | NOT_MEASURED | NOT_MEASURED | OBSERVED | NOT_MEASURED | NOT_MEASURED | existing direct-kernel evidence |
| XSBench | CONFIRMED_CAUSAL | WEAKENED | OBSERVED | OBSERVED | OPEN | H2 causal; H3 not confirmed; residual structure open |
| JSMN | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED | NOT_MEASURED | correctness corpus |
| plb2 | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | candidate |
| TSVC | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | candidate |

No cell is promoted to causal without a controlled transformation, correctness
gate, reproducible timing, and provenance.

The XSBench instruction-budget cell satisfies that rule under the scoped
Linux-native G/H protocol. The promotion does not generalize to RMSD,
BabelStream, PRK, PolyBench, JSMN, plb2, or TSVC; those cells remain
NOT_MEASURED or retain their prior observational status.
