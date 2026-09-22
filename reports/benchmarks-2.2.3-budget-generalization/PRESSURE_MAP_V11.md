# Global Pressure Map V11

This map records evidence availability. Only the instruction-budget column is
newly causal in this campaign. `OBSERVED_ONLY` and `OBSERVED_STATIC_ONLY` are
not causal attribution claims.

| Workload | Instruction budget | Frame | Bounds | Initialization | Indexing | Stack | Register pressure | Calls | Runtime helpers |
|---|---|---|---|---|---|---|---|---|---|
| `scientific.rmsd.batch` | CONFIRMED_CAUSAL | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_STATIC_ONLY | NOT_MEASURED |
| `scientific.xsbench.compatible_lookup.medium` | CONFIRMED_CAUSAL | WEAKENED | OBSERVED_ONLY | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED |
| `realworld.jsmn` | CONFIRMED_CAUSAL | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | OBSERVED_ONLY | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED | NOT_MEASURED |

No frame, bounds, register-allocation, or runtime-helper experiment was run
in this campaign. Dynamic logical instruction counts are unavailable, so no
cost-per-logical-instruction claim is made.
