# Frontier Lab State

Date: 2026-09-23

- Lane A: instruction-budget attribution is causally confirmed for the pinned
  XSBench positive control, the existing RMSD FFI pilot, and the JSMN native
  parser path.
- Lane B: multi-workload replication closed H7 as `CONFIRMED_GENERAL` across
  three workload classes. O09 is complete.
- S3 experimental baseline: `e07d0b5464bf472b2ca18993f3e196a234ff0fc5`.
  The isolated exact-segment candidate is frozen at
  `1a76e341098b54a639fec22eecea362cc243c46f`; its report-only evidence is
  published in S3 PR #310, without changing the tested source.
- P2 exact segment accounting passed the bounded E0, correctness, and
  reproducibility gates, with strong material recovery in all six workload /
  optimization cells. H9 exact mapping is no longer blocked; H10 is confirmed
  and H11 is confirmed material.
- Production optimization: none. S3 PR #310 remains open Draft and unmerged;
  the default remains per-instruction accounting.
- O21: COMPLETE_SAFE_NOT_PROMOTED. P1 remains safe but non-material; P2 is an
  experimental candidate for hardening only, not production promotion.
- Evidence score remains 89/100 (delta 0 for this campaign); qualified
  performance index remains NOT_AVAILABLE.
- The sole next action is `S3_EXPERIMENT_SEGMENT_BUDGET_HARDENING`, focused on
  outlining/sharing the existing exact slow path while preserving E0 and
  default-mode byte identity. No further budget architecture search is
  authorized.

The current evidence is bounded to the declared Linux x86-64 protocols. Host,
VM, and VirtualBox remain running by policy; no power action is authorized.
