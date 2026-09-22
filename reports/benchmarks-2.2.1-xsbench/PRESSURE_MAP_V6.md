# Pressure Map V6

```text
STATUS=CORRECTNESS_CLOSED_TIMING_REPRODUCIBILITY_OPEN
CAUSAL_EXPERIMENT_READY=NO
NATIVE_SPEEDUP_CLAIM=NO
```

## XSBench observations

The qualified subset exercises irregular indexed memory access, binary search,
bounds-sensitive branching, flat data layout, f64 interpolation, and nested
accumulation. These are structural workload pressures, not causal compiler
findings. The direct FFI timing is not reproducible under the prescribed
Run A/B rule, so it cannot promote a performance pressure or optimization
candidate.

| Pressure | Evidence | Strength | Causality |
|---|---|---|---|
| irregular memory access | explicit flat indexed fixture | SINGLE_WORKLOAD | UNKNOWN |
| indexing and bounds | binary-search and metadata contract | SINGLE_WORKLOAD | UNKNOWN |
| branching | search and interpolation control | SINGLE_WORKLOAD | UNKNOWN |
| cache locality | no supported perf counters | UNAVAILABLE | UNKNOWN |
| runtime helpers | no isolated causal measurement | NOT_MEASURED | UNKNOWN |
| numeric interpolation | hosted/native parity | SINGLE_WORKLOAD | CORRELATED |
| code size/assembly | artifacts preserved, no causal test | NOT_MEASURED | UNKNOWN |

Existing Phase B families (RMSD single/batch/matrix) provide correctness
coverage for regular scientific vector and nested-loop shapes. They do not,
together with this timing-open XSBench run, satisfy the evidence bar for a
causal S3 optimization experiment. No candidate is promoted.

```text
PERSISTENT_S3_PRESSURES=NOT_ESTABLISHED
S3_CAUSAL_EXPERIMENT_READY=NO
S3_CAUSAL_EXPERIMENT_CANDIDATES=NONE
PERF_COUNTERS=UNAVAILABLE_BY_HOST_POLICY
```
