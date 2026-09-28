# S3 1.11 Independent Control Replay

## Provenance and protocol

```text
S3_REPOSITORY=https://github.com/SamDevlab/S3.git
S3_CONTROL_SHA=832b1cc04fe1f6174e482eb3a245e08af3d53211
S3_CONTROL_TREE=dc1138890655169088f9371ce32a9050cfc3af8d
S3_CHECKOUT_CLEAN=YES
BENCH_EXECUTOR_REPOSITORY=https://github.com/SamDevlab/S3-Benchmarks.git
BENCH_EXECUTOR_SHA=b3ecb9b2269b583cba0706fd7ed13956a9641512
BENCH_EXECUTOR_TREE=06316635dfc1830d3ec3955803acb0d168b77a7e
BENCH_EXECUTOR_SHA256=66e8b351d90f15a62ac4aba3ce4129dc62e1aa4439c93d50d3f32c4ff1325002
TARGET=Linux x86_64; Python 3.14.4; kernel 7.0.0-31-generic
RUN=2026-09-27 20:44:58.366400 -03:00 to 20:45:12.661719 -03:00
ELAPSED_SECONDS=14.29528
PROTOCOL=3 warmups; 21 samples; 1000 iterations/sample
TIMING_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
```

The independent executor cloned and checked out the exact S3 commit detached,
validated that checkout as clean, re-hashed the compiler source files, and
accepted `PASS_ALL_BUILDS` for all three workload builds. This is independent
execution and correctness evidence; it does not import the compiler-side
research transformation.

## Cross-check against the compiler-side control

The baseline native output hashes exactly match the separately captured S3
control for all workloads. Object metrics also match. Timing is close but
not directly interpreted as a paired comparison because the runs were
separate and non-interleaved:

| Workload | S3 control median ns/call | Bench replay median ns/call | Replay delta | Exact output hash match |
| --- | ---: | ---: | ---: | --- |
| Energy | 16,946.866 | 17,814.818 | +5.12% | YES |
| Point cloud | 13,502.947 | 13,996.794 | +3.66% | YES |
| Raster | 11,494.410 | 11,868.525 | +3.25% | YES |

These small separately observed median shifts are not a causal result and do
not establish a regression or speedup. An interleaved protocol would be
required for direct timing attribution. Hardware counters remain
`UNAVAILABLE_BY_POLICY`; no permission or security setting was changed.

## Preserved evidence

Under `evidence/control-832b/`:

```text
native-workload-benchmark-v1.json
  compiler-side control copy; SHA-256 4b8eabb4f542c93a0bfde3b3736bd8fe26cecea9c1521d636297908ab92556e

independent-replay/native-workload-benchmark-v1.json
  independent raw replay; SHA-256 f763b525e51bb852399b1da54165fc0e7c6bbb709108b5673a276aa75ce4c5a9

independent-replay/executor-result-v1.json
  validated executor result; SHA-256 cb6336617a33e44f9515b11b350bcb52e70854fa77ab7a65ce689a541fae7e58

independent-replay/executor-stdout.txt
  compact command result; SHA-256 f03a9629a039d46caf638a68aa2b50c660ee513777bc2b6e955311720cd0aa78
```

Generated `.s`/`.so` artifacts remain outside the repository in the Linux
temporary output directory. The replay was read-only with respect to both
remote repositories. Historical PRs #15, #23 and #24 remain untouched.

```text
INDEPENDENT_CONTROL_REPLAY=PASS
WORKLOADS=3/3 PASS_ALL_BUILDS
OUTPUT_HASHES_MATCH_S3_CONTROL=YES
TIMING_REPLICATION=NON_INTERLEAVED_CHARACTERIZATION_ONLY
PRODUCTION_DEFAULT_CHANGED=NO
RELEASE_OR_TAG_CREATED=NO
```
