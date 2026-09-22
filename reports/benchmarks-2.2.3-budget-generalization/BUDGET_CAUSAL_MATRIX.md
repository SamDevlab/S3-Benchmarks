# Budget Causal Matrix

Campaign: `S3_BENCHMARKS_2_2_3_MULTI_WORKLOAD_BUDGET_CAUSAL_VALIDATION`

The percentages below are reported per workload. They are not averaged and
are not a universal overhead estimate.

| Workload | Class | K | O0 share | O1 share | Reproducible | Causality |
|---|---|---:|---:|---:|---|---|
| `scientific.rmsd.batch` | regular numeric | 2,000,000 | 60.34657390% | 61.97746370% | PASS | CONFIRMED_CAUSAL |
| `scientific.xsbench.compatible_lookup.medium` | irregular scientific | 750,000 | 56.77769984% | 52.66305804% | PASS | CONFIRMED_CAUSAL |
| `realworld.jsmn` | control-flow / parsing | 1,250,000 | 51.77733252% | 54.24963127% | PASS | CONFIRMED_CAUSAL |

`MATERIAL_SHARE_THRESHOLD=0.10` and the descriptive large-effect threshold is
`0.25`. All three selected classes exceed the materiality threshold in both
S3 optimization levels. The observed share range is descriptive only; no
cross-workload average or geomean is used.

Source provenance and raw sessions are recorded in
`BUDGET_GENERALIZATION_RESULT.json` and under `raw/regular/`,
`raw/xsbench/` where historical positive-control material exists, and
`raw/control-flow/jsmn-small-window-official-20260922/`.
