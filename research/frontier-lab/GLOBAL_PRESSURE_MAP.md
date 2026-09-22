# Global Pressure Map V11

This map records evidence availability, not inferred causes. Only the
instruction-budget column received a new causal intervention in 2.2.3.

| workload | instruction_budget | frame | bounds | initialization | indexing | stack | register_pressure | calls | runtime_helpers | status |
|---|---|---|---|---|---|---|---|---|---|---|
| RMSD | CONFIRMED_CAUSAL | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_STATIC_ONLY | NOT_MEASURED | existing direct FFI pilot; 2.2.3 causal budget evidence |
| BabelStream | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | existing direct-kernel evidence |
| PRK NStream | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | preselection blocked by no common measurement window |
| PolyBench GEMM | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | existing direct-kernel evidence |
| XSBench | CONFIRMED_CAUSAL | WEAKENED | OBSERVED_ONLY | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | H2 causal; H3 not confirmed |
| JSMN | CONFIRMED_CAUSAL | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | native PROCESS_E2E budget attribution |
| plb2 | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | candidate |
| TSVC | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | candidate |

No cell is promoted to causal without a controlled transformation, correctness
gate, reproducible timing, and provenance. Dynamic logical-instruction counts
remain unavailable; no cost-per-logical-instruction claim is made.
