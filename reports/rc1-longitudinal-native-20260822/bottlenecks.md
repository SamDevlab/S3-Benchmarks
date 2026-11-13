# RC1 bottleneck assessment

## B1 — P1 JSMN

- Observation: RC1 S3-O1 remains 43.89x slower than the same-run C-O2 geomean
- Likely layer: native lowering/runtime representation
- Evidence: HIGH
- Hypothesis: instruction and memory traffic expansion dominate the external gap
- Next experiment: promote P7-P9 paired native kernels and collect raw samples plus perf if permitted

## B2 — P1 JSMN

- Observation: S3-O1 assembly has 49,414 instructions, 24,745 loads/stores, and 7,560 stack operations
- Likely layer: code generation and frame materialization
- Evidence: MEDIUM
- Hypothesis: value and memory-state materialization remain broad
- Next experiment: structural P8/P9 kernels with per-function metric attribution

## B3 — P1 JSMN

- Observation: O1/O0 geomean ratio is 0.9449x on RC1
- Likely layer: optimization coverage
- Evidence: MEDIUM
- Hypothesis: current optimizer reduces runtime on this workload but does not close the representation gap
- Next experiment: separate optimizer passes with paired native structural deltas

## B4 — P1 JSMN

- Observation: C-O2 control range is above the 5% predeclared threshold
- Likely layer: measurement environment
- Evidence: HIGH
- Hypothesis: host/control variability prevents a confident H4-H5 runtime classification
- Next experiment: one bounded paired campaign after controlled cooldown

## B5 — P2-P18

- Observation: no promoted workload beyond P1 has a native timing result in this campaign
- Likely layer: benchmark coverage
- Evidence: HIGH
- Hypothesis: the next bottleneck is evidence coverage before optimization claims
- Next experiment: promote P7, P8, and P9 one at a time with correctness-first native harnesses
