# Native Measurement Pressure Map

Run `native-v1-20260921-02` on machine `9f6c7cbbdbbc2d056ffc306f76a1dcd9df194e15167cb037542da54e97b59393`.

The map is characterization evidence, not a compiler optimization decision. All timing rows are `PROCESS_E2E`; `KERNEL_TIME=NOT_AVAILABLE`.

| Pressure | Evidence | Families | Workload points | Causality |
|---|---|---:|---:|---|
| PROCESS_E2E_STARTUP_AND_RUNTIME_INITIALIZATION | MULTI_FAMILY | 5 | 30 | UNKNOWN |
| STATIC_CODE_AND_STACK_OPERATION_DENSITY | MULTI_FAMILY | 5 | 30 | UNKNOWN |
| MEASUREMENT_VARIABILITY | MULTI_FAMILY | 5 | 30 | UNKNOWN |
| MEMORY_BANDWIDTH_CACHE_LOCALITY_DYNAMIC_COUNTERS | UNAVAILABLE | 0 | 0 | UNKNOWN |

## Interpretation limits

- E2E startup/runtime cost is observed by construction, but it is not separated from useful work.
- Static assembly counters are descriptive and do not establish dynamic causality.
- `perf` was unavailable by host permission; cycles, instructions, branches, cache references/misses and IPC are not reported.
- There is no official BabelStream claim: these are the named compatible kernel subset.
