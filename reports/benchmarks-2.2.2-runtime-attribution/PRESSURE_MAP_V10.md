# Pressure Map V10

Status values describe evidence for the scoped XSBench experiment. They are
not production optimization priorities and do not generalize to other
workloads.

| pressure | XSBench state | evidence | scope decision |
|---|---|---|---|
| instruction-budget instrumentation | CONFIRMED_CAUSAL | exact removal of 521 O0 / 520 O1 sites; native correctness; reproducible G/H; 52.6631%-56.7777% baseline share removed | primary causal candidate for this workload |
| frame budget | WEAKENED | exact I/J intervention passed correctness but increased runtime; causal share invalid | not confirmed; no follow-up in this campaign |
| initialization metadata | OBSERVED | present in generated assembly; no controlled split | open |
| bounds | NOT_MEASURED | intentionally retained | open |
| indexing | OBSERVED | irregular lookup workload; no controlled split | open |
| stack | OBSERVED | not removed by either diagnostic | open |
| register pressure | NOT_MEASURED | no controlled emitter differential | open |
| calls | OBSERVED | retained in diagnostic | open |
| runtime helpers | OBSERVED | retained in diagnostic | open |
| code size | OBSERVED | ELF sizes recorded; not a runtime attribution | descriptive only |

## Interpretation

H2 is causal only for `scientific.xsbench.compatible_lookup.medium`, pinned S3
source `e07d0b5464bf472b2ca18993f3e196a234ff0fc5`, the recovered Linux guest,
and the declared G/H protocol. The no-budget residual remains large, but the
frame intervention did not explain it. The remaining code-structure pressures
are not distinguished by this campaign.

`QUALIFIED_PERFORMANCE_INDEX=NOT_AVAILABLE` and
`S3_PRODUCTION_CHANGE_READY=NO`. Other workloads remain `NOT_MEASURED`.
