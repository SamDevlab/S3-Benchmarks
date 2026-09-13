# RC1 Linux clean-checkout activation

## Decision

`FINAL_STATUS=FAIL_CLOSED_UNSTABLE_ENVIRONMENT`

The fresh Linux benchmark checkout was created without touching the historical
dirty checkout and was fixed detached at the executable source lock
`ee1af3071aac5479e721f96f1f33b729310c9202`. The post-lock delta to PR head
`73915bb2304e569ca0db766db9a6a8a38dd96701` is
`REPORTS_DOCS_METADATA_ONLY`; the source lock is valid.

The one authorized preflight completed with 5 blocks and 50 raw samples. Its
control drift was `6.583860468970637%`, above the 5% threshold. The runner
therefore stopped fail-closed. No timing smoke, correctness workload, weekly
run, H0-H5 run, M2.30 comparison, retry, or benchmark merge was executed.

## Checkouts and provenance

The old checkout was preserved read-only at
`/home/vboxuser/s3-rc1-longitudinal-native-v2-20260822/benchmark`, at
`6ae9e1f8bcff79557c02eb20c786e70d42eeda1d`, with its two historical
untracked report directories unchanged. It was not reset, cleaned, changed, or
deleted.

The new checkout is
`/home/vboxuser/s3-bench-runs/rc1-automation-source-ee1af307`, detached,
clean, and at the exact source lock. The read-only RC1 S3 checkout remained
clean at `9b39c7070d7bfa23d709c2128eb0b0bbef164177`; tag
`v1.0.0-rc1` resolves to that same commit. S3 was not mutated.

## Validation

- SSH connection, non-interactive operation, stdout/stderr capture, exit-code
  propagation, and timeout propagation passed; the bounded timeout returned
  `124`. No secret was persisted.
- Required imports and CLI discovery for automation, P1, P7/P9, and statistics
  passed.
- Linux native toolchain was ready: x86-64, Python 3.14.4, GCC/CC 15.2.0,
  binutils 2.46, kernel 7.0.0-29-generic.
- The future weekly command was syntax/configuration validated only and was not
  executed.

Raw preflight evidence is retained under the run directory
`linux-clean-preflight-20260822-145649/`, including `preflight.json`,
`samples.json`, `samples.csv`, `summary.json`, and `machine-status.json`.

`AUTOMATION_WIRING=PASS`, `LINUX_EXECUTOR_READY=YES_PRESTAGED_CHECKOUTS_ONLY`,
`LINUX_PERFORMANCE_RUNNER_READY=NO`, `WEEKLY_RUN_ELIGIBLE=NO`, and
`TIMING_SMOKE_PROMOTED=NO`.

The next action is a future automated preflight on a stable Linux host. This
campaign does not retry the unstable preflight.

## Safety ledger

`S3_PRODUCTION_CHANGE=NO`

`S3_TEST_CHANGE=NO`

`S3_RUNNER_CHANGE=NO`

`T4_RUNS=0`

`FULL_SUITE_RUNS=0`

`BENCHMARK_MERGE=NO`

`FORCE_PUSH=NO`

`SHUTDOWN=NO`

`REBOOT=NO`
