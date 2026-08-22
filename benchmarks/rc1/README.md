# RC1 longitudinal benchmark contracts

`benchmarks.rc1.workloads` defines the pinned P2-P18 workload contracts and
the deterministic contract probe used by the RC1 campaign. The probe verifies
that the declared input, oracle, and timing boundary are stable. It does not
compile S3, run native code, or create a timing claim.

A workload remains `EXPERIMENTAL_WORKLOAD` until its correctness oracle,
provenance, raw results, repeatability, and measurement boundary are all
executed and reviewed. The RC1 campaign therefore keeps P2-P18 out of the
aggregate scoreboard while still making the missing capability explicit.

The unattended orchestration entry point and its gate policy are documented in
[`AUTOMATION.md`](AUTOMATION.md). Use `python -m benchmarks.rc1.automation
--mode correctness-only` for a bounded correctness run or
`--mode preflight-only` to classify the host without timing S3.
