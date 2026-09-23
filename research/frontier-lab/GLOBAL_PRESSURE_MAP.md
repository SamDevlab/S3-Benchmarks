# Global Pressure Map V13

This map records evidence availability, not inferred causes. The P2 column
records the independently replayed exact-segment experiment; the other
dimensions remain unpromoted absent a controlled intervention.

| workload | instruction_budget | exact_segment_P2 | frame | bounds | initialization | indexing | stack | register_pressure | calls | runtime_helpers | status |
|---|---|---|---|---|---|---|---|---|---|---|
| RMSD | P0_SYSTEMIC_CAUSAL | STRONG_MATERIAL_E0 | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_STATIC_ONLY | NOT_MEASURED | existing direct FFI pilot; P2 six-cell replay |
| BabelStream | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | existing direct-kernel evidence |
| PRK NStream | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | preselection blocked by no common measurement window |
| PolyBench GEMM | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | existing direct-kernel evidence |
| XSBench | P0_SYSTEMIC_CAUSAL | STRONG_MATERIAL_E0 | WEAKENED | OBSERVED_ONLY | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | H2 causal; H3 not confirmed; P2 six-cell replay |
| JSMN | P0_SYSTEMIC_CAUSAL | STRONG_MATERIAL_E0 | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | native PROCESS_E2E; P2 six-cell replay |
| plb2 | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | candidate |
| TSVC | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | NOT_AUDITED | candidate |

No cell is promoted to causal without a controlled transformation, correctness
gate, reproducible timing, and provenance. Dynamic logical-instruction counts
remain unavailable; no cost-per-logical-instruction claim is made. P2 results
are experimental and qualify hardening only; current production remains P0.
For the P2 cells, the minimum recovered P0-to-PNEG excess was 92.14% (JSMN
O0); all six cells exceeded the predeclared 50% strong threshold.
