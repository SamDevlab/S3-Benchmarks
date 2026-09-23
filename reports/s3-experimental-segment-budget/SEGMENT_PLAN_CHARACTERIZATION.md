# Deterministic Segment Plan Characterization

The planner consumes validated S3 Assembly function/block/instruction
structure. It never slices emitted x86 text, never crosses a basic-block
boundary, and terminates segments at calls or control transfers. Fast-path
eligibility uses the predeclared minimum logical weight of two and the current
budget domain. Weight-one and otherwise ineligible segments retain scalar
per-instruction accounting. The complete per-function plans are preserved in
the campaign raw evidence's `segment-plans.json`.

| workload | opt | logical instructions | segments | fast segments | scalar sites | mean weight | median | max | call barriers | control barriers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RMSD | O0 | 113 | 22 | 17 | 5 | 5.14 | 4 | 34 | 1 | 21 |
| RMSD | O1 | 113 | 22 | 17 | 5 | 5.14 | 4 | 34 | 1 | 21 |
| XSBench | O0 | 521 | 35 | 27 | 8 | 14.89 | 4 | 258 | 1 | 34 |
| XSBench | O1 | 520 | 34 | 27 | 7 | 15.29 | 3 | 258 | 1 | 33 |
| JSMN | O0 | 2,475 | 386 | 298 | 88 | 6.41 | 5 | 783 | 39 | 347 |
| JSMN | O1 | 2,427 | 356 | 298 | 58 | 6.82 | 5 | 781 | 39 | 317 |

JSMN's much larger number of fast segments coincides with the largest P2
`.text` growth (about 58.3-58.5%). This is a descriptive structural
correlation, not a separately isolated timing cause. Dynamic accounting-event
counts were not measured.
