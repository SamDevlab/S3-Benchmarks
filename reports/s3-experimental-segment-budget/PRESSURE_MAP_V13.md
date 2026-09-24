# Pressure Map V13

This update adds one controlled S3 exact-segment budget experiment. It does
not infer causes for untested pressure dimensions.

| workload | P0 instruction budget | P1 global countdown | P2 exact segment | frame | bounds/index | register/stack | helpers | status |
|---|---|---|---|---|---|---|---|---|
| RMSD | SYSTEMIC_CAUSAL | SAFE_NOT_MATERIAL | STRONG_MATERIAL_RECOVERY | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | P2 faster than PNEG at O0/O1 |
| XSBench | SYSTEMIC_CAUSAL | SAFE_NOT_MATERIAL | STRONG_MATERIAL_RECOVERY | WEAKENED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | P2 recovers 97.0-98.0%; 2.2-3.9% slower than PNEG |
| JSMN | SYSTEMIC_CAUSAL | SAFE_NOT_MATERIAL | STRONG_MATERIAL_RECOVERY | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | P2 recovers 92.1-93.4%; 7.9-9.5% slower than PNEG |
| BabelStream | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | no candidate run |
| PRK NStream | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | no candidate run |
| PolyBench GEMM | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | no candidate run |

`P0` remains the safe default. `P1` is not promoted. P2 is a research
candidate for hardening only. Dynamic instruction/accounting-event counts are
unavailable; static code size is not a substitute.
