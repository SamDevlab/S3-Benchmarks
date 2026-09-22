# Hypothesis Ledger

| ID | hypothesis | status | evidence |
|---|---|---|---|
| H1 | inline warmups consume finite instruction budget | CONFIRMED | prior controlled WARMUPS=0/1 proof |
| H2 | instruction-budget instrumentation materially contributes to XSBench gap | UNDER_TEST | exact diagnostic rewrite prepared; G/H pending |
| H3 | frame bookkeeping materially contributes to residual gap | OPEN | frame checks observed, not isolated |
| H4 | indexing/bounds dominate residual | OPEN | irregular workload shape only |
| H5 | register/memory code generation dominates residual | OPEN | no native differential yet |
| H6 | FFI boundary dominates the gap | WEAKENED | matched/amortized boundary in E/F protocol |

H6 is less plausible as the explanation for the measured 100x-scale local
gap, but it is not claimed falsified by this campaign.
