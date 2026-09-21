# Candidate Activation and Blocker Falsification

## Scope

This campaign activates faithful, independently generated S3 workload
adapters for the 2.0.1 candidate. It does not add timing claims, modify the
S3 source repository, or vendor upstream benchmark code.

## Hosted result

The bounded hosted matrix contains 16 workload identities at two deterministic
sizes, for 32 observations total. Every observation is checked against an
independent Python oracle and passed. Generated source files are retained in
`generated/`, with their SHA-256 values recorded by `activation-results.json`.

## Native result

The first attempt used native decimal-`f64` output and recorded 32 protocol
blocks. The allowed integer correctness-canary protocol then compiled the
same 32 workloads on Linux x86-64 and produced `NATIVE_PASS=32` with
`NATIVE_OBSERVABLE=CANARY`. The canary returns `1` only when the calculated
workload result matches the independent Python oracle value. The initial raw
block transcript remains preserved separately for provenance; the final native
result is a pass, not a backend blocker.

## TSVC relationship

The TSVC audit is pinned to upstream commit
`badf9adb2974867ac0937718d85a44dec6dec95a`. Eighteen representative loop
shapes were classified without copying upstream source. The audit is a
coverage map for future independent adapters, not an implementation claim.

## Policy result

- `NATIVE_QUALIFICATION`: PASS via integer correctness canary
- `BENCHMARK_TIMING`: not run
- `PERFORMANCE_RESULTS_VALID`: `NO_NEW_PERFORMANCE_RESULTS`
- `VENDORED_CODE`: none
- `MERGE`: not performed
- `TAG`: not performed
- `RELEASE`: not performed
