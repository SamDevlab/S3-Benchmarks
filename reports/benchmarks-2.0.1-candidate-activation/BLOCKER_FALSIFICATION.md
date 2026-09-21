# Candidate Activation and Blocker Falsification

## Scope

This campaign activates faithful, independently generated S3 workload
adapters for the 2.0.1 candidate. It does not add timing claims, modify the
S3 source repository, vendor upstream benchmark code, or claim native
qualification when the runtime cannot expose the result protocol.

## Hosted result

The bounded hosted matrix contains 16 workload identities at two deterministic
sizes, for 32 observations total. Every observation is checked against an
independent Python oracle and passed. Generated source files are retained in
`generated/`, with their SHA-256 values recorded by `activation-results.json`.

## Native result

The same 32 cases were attempted on Linux x86-64 using the exact S3 candidate.
All 32 were blocked before a result could be observed because the standalone
runtime does not yet provide decimal `f64` output for a native entry function.
This is a genuine backend/output-protocol blocker, not a falsified pass and
not a language-capability failure. No performance result is valid from this
run.

## TSVC relationship

The TSVC audit is pinned to upstream commit
`badf9adb2974867ac0937718d85a44dec6dec95a`. Eighteen representative loop
shapes were classified without copying upstream source. The audit is a
coverage map for future independent adapters, not an implementation claim.

## Policy result

- `NATIVE_QUALIFICATION`: blocked by backend output protocol
- `BENCHMARK_TIMING`: not run
- `PERFORMANCE_RESULTS_VALID`: `NO_NEW_PERFORMANCE_RESULTS`
- `VENDORED_CODE`: none
- `MERGE`: not performed
- `TAG`: not performed
- `RELEASE`: not performed
