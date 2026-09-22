# Safe Instruction-Budget Design Space

This document is research planning only. It follows the XSBench H2 result and
does not authorize a production S3 change or select a winner.

| design | bounded execution | runaway detection | nested calls / loops | verification burden | open experiment |
|---|---|---|---|---|---|
| A. current global per-instruction counter | yes | direct | direct | low, existing | measure baseline semantics |
| B. register-resident decrementing counter | must prove spill/reload safety | direct if preserved | ABI-sensitive | high | native correctness and signal paths |
| C. basic-block charging | yes if block cost is conservative | block boundary | calls and loops need exact accounting | medium | compare worst-case bounds |
| D. weighted basic-block charging | yes only with sound weights | block boundary | nested control flow | high | validate conservative weights |
| E. loop-chunk charging | yes with loop bound policy | chunk boundary | nested loops and breaks | high | prove loop accounting |
| F. function-level charging | coarse bound only | call/return boundary | recursion and callbacks | medium | establish lower-bound safety |
| G. periodic checkpoint accounting | interval-dependent | checkpoint latency | nested calls may exceed interval | high | bound detection latency |
| H. hybrid static/dynamic budget | potentially yes | mixed | all dynamic escape paths | very high | formal accounting model |
| I. checked native mode | yes | explicit checked path | preserve all safety checks | medium | mode contract and differential tests |
| J. optimized bounded native mode | only after proof | explicit | all safety paths | very high | multi-workload qualification |

Every future design must preserve `BOUNDED_EXECUTION`,
`RUNAWAY_DETECTION`, `DETERMINISTIC_BUDGET_FAILURE`, `NESTED_CALL_ACCOUNTING`,
`LOOP_ACCOUNTING`, and `ERROR_REPORTING`. Removing protection permanently is
not a valid design.

Required next evidence is multi-workload causal replication, not immediate S3
implementation. No design is selected by this document.
