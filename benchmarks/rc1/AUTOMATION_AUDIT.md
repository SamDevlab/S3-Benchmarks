# RC1 Automation Audit

## Reusable components

- `tools/artifacts.py` for exact Git provenance, run-scoped paths, write-once
  manifests, and file hashes.
- `tools/p1_stability.py` for paired P1 native artifacts and raw samples.
- `tools/p7_p9_native.py` for correctness-first P7/P8/P9 native workloads.
- `benchmarks.rc1.statistics` for deterministic summaries and bootstrap CI.
- `tools.assembly_analyzer` for structural artifact metrics.

## Components added

- `benchmarks.rc1.automation` as the single non-interactive mode dispatcher.
- Immutable C control preflight with block-level drift classification.
- Safe host identity and deterministic environment hash.
- Run manifest, environment diagnostics, raw sample schema, append-only trend
  history, and fail-closed regression classification.
- Cheap correctness-only entry points and scheduler-ready shell/PowerShell
  wrappers.

## Duplicated or unsafe behavior addressed

- Timing is no longer reachable from a correctness-only path.
- P1/P7/P8/P9 orchestration is centralized instead of requiring callers to
  compose independent timing commands.
- Control instability is classified before any S3 timing command is started.
- Missing native toolchains are reported as `NOT_RUN_PLATFORM`, not as a
  compiler correctness failure.
- Run evidence is never overwritten; promoted history is append-only.

## Deliberate boundaries

- Existing historical V1/V2 reports remain immutable.
- The current VM's remote checkout is not silently changed by the runner.
- Scheduler registration, credentials, process killing, shutdown, and reboot
  remain outside the repository.
