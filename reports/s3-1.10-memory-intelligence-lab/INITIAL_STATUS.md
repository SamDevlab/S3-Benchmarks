# S3-Benchmarks 1.10 Lab Checkpoint

```text
BENCH_CAMPAIGN_BASE=b11526443b9f2ac50f2ffdd3c4a6c1d0a2471152
BENCH_CAMPAIGN_TREE=0b4f917abc036ce268e85c2230434f2598170cf4
BENCH_BRANCH=research/s3-1.10-memory-intelligence-lab
S3_CONTROL_SHA=e27dff1e712e50271df9f860669cd714e28f4ce7
S3_CONTROL_TREE=3e5ddfc7283d8a226505c1cc6680fecf789e147b
```

The lab starts from merged `main`, not from the #27 feature branch. The
existing 1.9 executor is an independent pinned-checkout/build/correctness
path qualified for one S3 SHA. The 1.10 serial matrix extension has now
replayed exact 1.5–1.9 SHAs under one checked protocol; 1.10 itself remains
unreplayed pending a frozen S3 candidate SHA.

Inherited 1.9 timing classification is
`CHARACTERIZATION_ONLY`; `NATIVE_SPEEDUP_CLAIM=NO`; PMU is unavailable by
policy. It is budget-mode characterization, not evidence for a memory
transformation. The recorded independent native result is retained at
`reports/s3-1.9-native-observatory-lab/experiments/EXP-S3-19-NATIVE-OBS-001.json`
with SHA-256
`897fade8e52d459bf505c89d52a3f307196757d0ea1ea99e993914e968a9e721`.

## 1.10 lab scope

- Keep the lab independent: exact S3 SHA checkout, fresh build, correctness
  before measurement, and independently extracted object metrics.
- The serial multi-SHA orchestrator reuses the audited one-SHA contract only
  for revisions that contain its required benchmark entry point and schema;
  historical fixture/protocol compatibility remains a per-SHA question.
- Record historical entries as `REPLAYED`, `NOT_REPLAYABLE`,
  `REQUIRES_ADAPTER`, or `INCOMPATIBLE_PROTOCOL`; never silently patch old
  compiler sources. The 1.5–1.9 replay ledger is
  `evidence/historical-replay-v1/EXP-S3-110-HIST-001.json`.
- Do not rerun timing until a candidate transformation has nonzero eligible
  sites, correctness passes, and the matched measurement protocol is frozen.
- `execute_matrix` applies the qualified single-SHA protocol serially to
  explicit unique full SHAs. Every revision gets a fresh detached checkout and
  separate evidence directory; failures remain per-SHA failures. The five
  historical runs passed all workloads and the raw result hashes match the
  matrix. No 1.10 timing or transformation promotion claim is made.
- `HISTORICAL_REPLAY_AND_PR_DOSSIER.md` records the exact replay and the
  read-only recommendations for Bench PRs #15, #23, and #24.

```text
MULTI_SHA_EXECUTOR=IMPLEMENTED_TESTED_AND_REPLAYED_5_SHAS
HISTORICAL_REPLAY=1.5_THROUGH_1.9_REPLAYED_1.10_PENDING_FROZEN_SHA
TIMING_RERUN=YES_HISTORICAL_REPLAY_ONLY
NATIVE_SPEEDUP_CLAIM=NO
```
