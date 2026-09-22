# Pressure Map V9

Status values are evidence states, not optimization priorities. Structural
observation is not causal evidence.

| pressure | XSBench state | evidence |
|---|---|---|
| instruction-budget instrumentation | OBSERVED / UNDER_TEST | 521 O0 and 520 O1 exact static sites |
| frame budget | OBSERVED | 3 static frame-limit sites in O0/O1 |
| bounds | NOT_MEASURED | intentionally not removed |
| initialization metadata | OBSERVED | present in generated assembly; no causal split |
| indexing | OBSERVED | irregular lookup/index workload; no causal split |
| stack traffic | OBSERVED | static approximation unchanged by rewrite |
| register pressure | NOT_MEASURED | no native differential available |
| calls | OBSERVED | 56 static calls in baseline and diagnostic assembly |
| runtime helpers | OBSERVED | helper symbols retained |
| code size | OBSERVED | frozen S3 object is 279280 bytes; diagnostic object unavailable |

The only causal label allowed in this revision is
`UNDER_TEST`; no pressure is promoted to `CAUSAL_EXPERIMENT_PASS`.
