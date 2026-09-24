# Exact Segment Budget Causal Matrix

**Sources:** S3 control `e07d0b5464bf472b2ca18993f3e196a234ff0fc5`; S3
experiment `1a76e341098b54a639fec22eecea362cc243c46f`; benchmark runner
`84347c9c400839c739241728f8e90f4a1273c33f`.

All variants passed expected-output correctness in all workload/optimization
cells. P0/P2 share the same compiled Assembly object and differ only by budget
mode. P0's candidate assembly matched the pinned control. Sessions are paired
by a balanced deterministic schedule, with 30 repetitions in each of two
independent sessions. `T` is the arithmetic mean of their medians.

| workload | opt | K | T(P0) s | T(P1) s | T(P2) s | T(PNEG) s | P2 recovered | P2 over P1 | max session delta |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RMSD | O0 | 2,000,000 | 13.3973 | 13.5905 | 5.0085 | 5.3747 | 104.56% | 106.97% | 3.08% |
| RMSD | O1 | 2,000,000 | 13.4296 | 13.5822 | 5.1351 | 5.3637 | 102.84% | 104.73% | 1.93% |
| XSBench | O0 | 750,000 | 14.3397 | 14.6145 | 6.4396 | 6.1951 | 97.00% | 100.37% | 1.12% |
| XSBench | O1 | 750,000 | 13.8169 | 14.0201 | 6.7578 | 6.6120 | 97.98% | 100.80% | 0.89% |
| JSMN | O0 | 1,250,000 | 24.3932 | 23.6617 | 12.0788 | 11.0285 | 92.14% | 86.67% | 1.61% |
| JSMN | O1 | 1,250,000 | 23.8875 | 23.4578 | 11.7446 | 10.8874 | 93.41% | 90.10% | 1.57% |

P2 recovered more than the 50% strong-recovery threshold in every cell. A
recovery above 100% is retained (not capped): it means the measured P2 median
was below the PNEG diagnostic median. PNEG has no safety guarantee and is only
a lower-bound comparator.

`correctness=PASS`, `all_timed_samples_pass=true`, and
`reproducibility=PASS`; per-variant session medians and all raw samples are in
`EXPERIMENTAL_SEGMENT_BUDGET_RESULT.json` and the run's JSONL files.
