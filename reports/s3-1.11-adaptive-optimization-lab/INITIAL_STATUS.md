# S3-Benchmarks 1.11 Lab — Initial Status

```text
CAMPAIGN=S3_1_11_ADAPTIVE_OPTIMIZATION_REGISTER_MEMORY_CODESIGN_MACHINE_INTELLIGENCE_AND_EXPERIMENTAL_COMPUTE_FRONTIER
BENCH_CAMPAIGN_BASE=b3ecb9b2269b583cba0706fd7ed13956a9641512
BENCH_CAMPAIGN_TREE=06316635dfc1830d3ec3955803acb0d168b77a7e
S3_CONTROL_SHA=832b1cc04fe1f6174e482eb3a245e08af3d53211
S3_CONTROL_TREE=dc1138890655169088f9371ce32a9050cfc3af8d
BENCH_BRANCH=research/s3-1.11-adaptive-optimization-lab
BENCHMARK_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
```

The lab branch starts directly at the merged S3-Benchmarks `main` base. The
S3 1.11 source control is pinned to the merged #324 SHA above. The benchmark
repository remains an independent execution, correctness, and provenance
authority; its copied control JSON is reference evidence, not a claimed
independent replay.

## Initial evidence

The S3 baseline JSON has been copied to `evidence/control-832b/` for schema
and input identity review. It records three workload correctness results as
`PASS_ALL_BUILDS`, exact output hashes, Linux x86-64/Python 3.14.4/cc 15.2.0,
and `PMU=UNAVAILABLE_BY_POLICY`. The timing is characterization only.

The independent control replay is complete and documented in
`CONTROL_REPLAY.md`. It executed the pinned source with the integrated Bench
executor, validated all three workloads, and matched their output hashes to
the separately captured S3 control. The replay's medians are preserved as
non-interleaved characterization only, not as a paired performance claim.
Independent candidate correctness replay and one point-cloud interleaved
timing confirmation are documented in `CANDIDATE_REPLAY.md`. The latter is
workload-specific characterization only and does not promote the candidate.

```text
INDEPENDENT_CONTROL_REPLAY=PASS
INDEPENDENT_CANDIDATE_CORRECTNESS_REPLAY=PASS (3/3)
INDEPENDENT_CANDIDATE_TIMING_REPLICATION=PARTIAL (point-cloud only)
INDEPENDENT_CANDIDATE_REPLICATION=PARTIAL
HISTORICAL_PRS_15_23_24=OPEN_DRAFT_UNTOUCHED
PRODUCTION_DEFAULT_CHANGED=NO
RELEASE_OR_TAG_CREATED=NO
```
