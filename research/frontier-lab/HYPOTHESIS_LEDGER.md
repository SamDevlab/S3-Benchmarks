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
| H8 | an exact global-countdown budget can preserve current instruction-limit semantics with lower native overhead | CONFIRMED_SAFE_NOT_MATERIAL | P1 passed E0 native boundary equivalence and all workload correctness gates, but recovered only 8.37% at RMSD O0, -0.49% at RMSD O1, -0.62%/-1.01% at XSBench O0/O1, and 4.40%/2.33% at JSMN O0/O1; no cross-workload material-performance gate |
| H9 | call-aware segment precharge with an exact slow path can preserve current budget semantics while amortizing accounting | CONFIRMED_EXACT_MAPPING | deterministic Assembly-structure segment plan, call/control barriers, and exact scalar slow path validated in S3 candidate `1a76e341`; E0 equivalence passed |
| H10 | the S3 emitter can construct exact logical-instruction segments directly from Assembly structure without benchmark-side heuristic reconstruction | CONFIRMED | S3 emitter planner operated on validated Assembly structure; P0/P2 reused one compiled program and only budget mode differed |
| H11 | amortizing instruction-budget accounting over exact logical segments materially reduces systemic budget cost while preserving E0 | CONFIRMED_MATERIAL | all six RMSD/XSBench/JSMN O0/O1 cells recovered at least 92.1% of measured removable excess; correctness and independent-session reproducibility passed |

H6 is less plausible as the explanation for the measured 100x-scale local
gap, but it is not claimed falsified by this campaign.

Scope: H2 remains confirmed for the pinned XSBench medium workload. H7 is
confirmed for the three declared workload classes under the 2.2.3 protocol:
`scientific.rmsd.batch` through the existing direct FFI pilot,
`scientific.xsbench.compatible_lookup.medium`, and `realworld.jsmn`. The P0/P1
causal baseline remains bounded to S3 source
`e07d0b5464bf472b2ca18993f3e196a234ff0fc5`. The P2 experiment is separately
bounded to candidate `1a76e341098b54a639fec22eecea362cc243c46f`, the recovered
Linux x86-64 guest, the recorded fixed-work fresh-process sessions, and the
published raw evidence. These results are not a universal overhead claim and
do not authorize production enablement.
