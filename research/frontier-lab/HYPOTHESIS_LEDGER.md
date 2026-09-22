# Hypothesis Ledger

| ID | hypothesis | status | evidence |
|---|---|---|---|
| H1 | inline warmups consume finite instruction budget | CONFIRMED | prior controlled WARMUPS=0/1 proof |
| H2 | instruction-budget instrumentation materially contributes to XSBench gap | CONFIRMED_CAUSAL | native diagnostic correctness; independent G/H; O0/O1 baseline share removed 0.5677769984/0.5266305804 |
| H3 | frame bookkeeping materially contributes to residual gap | NOT_CONFIRMED | exact I/J intervention passed correctness but increased runtime at both O0 and O1 |
| H4 | indexing/bounds dominate residual | OPEN | irregular workload shape only |
| H5 | register/memory code generation dominates residual | OPEN | no native differential yet |
| H6 | FFI boundary dominates the gap | WEAKENED | matched/amortized boundary in E/F protocol |
| H7 | instruction-budget instrumentation materially affects multiple distinct native workload classes | CONFIRMED_GENERAL | RMSD, XSBench, and JSMN each passed correctness, paired reproducibility, and material O0/O1 causal attribution |

H6 is less plausible as the explanation for the measured 100x-scale local
gap, but it is not claimed falsified by this campaign.

Scope: H2 remains confirmed for the pinned XSBench medium workload. H7 is
confirmed for the three declared workload classes under the 2.2.3 protocol:
`scientific.rmsd.batch` through the existing direct FFI pilot,
`scientific.xsbench.compatible_lookup.medium`, and `realworld.jsmn`. The
result remains bounded to S3 source
`e07d0b5464bf472b2ca18993f3e196a234ff0fc5`, the recovered Linux x86-64 guest,
and the recorded fresh-process sessions. It is not a universal overhead claim.
