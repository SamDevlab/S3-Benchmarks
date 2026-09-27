# S3-Benchmarks 1.9 Lab Checkpoint

## Provenance

The lab campaign starts from `main` at
`e5ff385d26ea6ec89d13cf1955bfa5438e56a266`. Its branch is
`research/s3-1.9-native-observatory-lab`. The corresponding S3 compiler
campaign starts from `211b1aecec756be42516322429720018f54001e7`, tree
`08289d214832e856d46e14ef941239649e9f4063`.

This document is an initial status, not a final qualification. Historical
campaigns and their PRs remain separate; no merge, tag, release, or default
policy change is performed here.

## Portability correction

The existing S3 1.8 evidence snapshot validator pinned JSON artifacts by
canonical LF content, but compared that canonical digest against a raw file
byte count. On a Windows checkout with `core.autocrlf=true`, the nine pinned
JSON files were materialized with CRLF. Their canonical hashes were correct,
but raw on-disk lengths differed from the manifest. The validator now derives
both digest and byte count from the same CRLF-to-LF canonical byte sequence.
It does not rewrite source artifacts or change their semantic content.

Focused `tests/test_s3_18_compiler_science_lab.py` results after the correction:

- Windows: 7 passed.
- Linux x86-64 VM: 7 passed.
- Before the correction, Windows showed 5 passed and 2 failures from the
  newline-sensitive byte count; Linux remained the canonical artifact format.

The first focused rerun exposed this portability issue; the correction was
narrowly limited to snapshot hashing/counting and its assertion. A full lab
suite has not been run at this checkpoint.

## Native evidence boundary

The S3 1.8 run and the S3 1.9 Observatory are distinct evidence producers.
The Observatory compiles a pinned source workload into an ELF relocatable
object and attributes machine instructions where a generated Assembly origin
is available. Its machine-instruction totals cover the entire `.text`; older
workload `binary_metrics.static_machine_instructions` may describe only the
exported workload function. Those fields must not be compared until the
accounting domains are explicitly reconciled.

Timing evidence remains characterization-only. PMU access was unavailable in
the Linux VM (`perf_event_paranoid=4`), and no actual dynamic spill or hardware
event claim is supported. This lab checkpoint does not promote EXACT, HYBRID,
or any experimental optimization as a default.

## Initial next bounded work (historical checkpoint)

1. Freeze the cross-repository result/provenance contract.
2. Add a lab-owned executor that checks out an exact S3 commit and validates
   correctness before timing.
3. Make artifact accounting domains explicit (whole `.text`, exported
   function, and S3-Assembly-origin mapped region).
4. Replicate only selected inconclusive timing cells after the executor and
   protocol are validated.

This was the plan at the initial status checkpoint. The lab-owned executor was
subsequently implemented and exercised; the matched 21-sample replication
below is the current evidence. Energy remains inconclusive across runs, so no
additional timing run or default promotion is inferred here.

## Executor smoke: EXP-S3-19-NATIVE-OBS-001

The lab-owned `tools/s3_19_executor.py` was exercised end-to-end on the Linux
x86-64 VM. It cloned the public S3 remote, checked out the exact pinned
`211b1aecec756be42516322429720018f54001e7` commit detached, verified tree
`08289d214832e856d46e14ef941239649e9f4063`, confirmed the clone was clean, and
independently recomputed all five compiler-source hashes emitted by the S3
runner. The raw runner then reported `PASS_ALL_BUILDS` for all three workloads.

This was a pipeline smoke, not a useful timing study: 1 warmup, 3 samples, and
10 iterations per sample. Its timing class is `CHARACTERIZATION_ONLY`, and the
wrapper explicitly sets `native_speedup_claim=false`. No performance
conclusion is drawn from the noisy three-sample ratios. The run produced and
SHA-256-pinned 15 assembly files and 16 shared objects; their inventory is in
`evidence/smoke-v1/executor-result-v1.json`. The raw result, stdout, and stderr
are preserved alongside it.

The lab worktree was dirty during execution because the new executor was
uncommitted; its measured HEAD/tree and executor SHA are recorded in the
wrapper. The clean detached S3 checkout and compiler inputs are separately
pinned. No binaries are committed in this report directory; the hashes allow
the temporary VM outputs to be checked if retained, and the exact pinned run
can be reproduced.

## Matched 21-sample replication

The executor was then used for one bounded independent replication with the
same Linux x86-64 host, exact S3 source commit/tree, datasets, compiler inputs,
optimization levels, budget modes, FFI path, 3 warmups, 21 samples, and 1,000
iterations per sample. Correctness passed before timing for all three
continuity workloads. The raw result is
`evidence/confirmation-v1/native-workload-benchmark-v1.json` (SHA-256
`897fade8e52d459bf505c89d52a3f307196757d0ea1ea99e993914e968a9e721`); the
executor wrapper is `evidence/confirmation-v1/executor-result-v1.json` (SHA-256
`362ae31e343230be83a2375b31a714da6814d4f1c6aeb1cca3c2463e03694bc6`). The
wrapper pins the exact raw-result SHA and independently verified compiler
source hashes. This is a replicated characterization, not promotion.

Paired results against PER were:

| Workload | EXACT_SEGMENT | LOOP_HYBRID | O0 vs O1 | Compact-EA |
| --- | --- | --- | --- | --- |
| point cloud | material improvement in both runs | material improvement in both runs | no material change | not applied |
| raster | material improvement in both runs | inconclusive in both runs | no material change | not applied |
| energy | first inconclusive, replication material; cross-run inconclusive | first inconclusive, replication material; cross-run inconclusive | no material change | not applied |

The original direct-run raw SHA-256 is
`6ddd6fb9a8fd6a3c656b6ac0970d1e5ba5f44e05cea59da8aaefd888cb15deaa`. Thus
EXACT_SEGMENT replicated for point cloud and raster; LOOP_HYBRID replicated
only for point cloud. Energy disagreement is retained as inconclusive rather
than averaged into a positive result. Compact-EA timing is not evidence for a
transformation because it fell back to baseline for these kernels. PER remains
the default. PMU counters were unavailable by policy, and no native-cycle,
hardware-instruction, spill, or causal speedup claim is made.
