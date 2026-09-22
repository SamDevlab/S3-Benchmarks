# Runtime Safety Envelope Audit

Campaign: `S3_BENCHMARKS_2_2_2_RUNTIME_COST_ATTRIBUTION_FRONTIER_LAB_V1`

## Scope

This is a benchmark-side audit of the frozen S3 assembly generated from
`e07d0b5464bf472b2ca18993f3e196a234ff0fc5`. No S3 source, compiler, runtime,
ABI, or instruction-limit implementation was changed.

The input assembly was regenerated from a clean archive of the pinned S3
commit and matched the frozen O0/O1 assembly byte-for-byte. The native shared
objects were not rebuilt in this Windows session because the configured Linux
guest (`s3-vm`, `127.0.0.1:2222`) was unavailable.

## Observed safety mechanisms

- instruction budget: exact `movabs` + counter compare + failure branch + counter increment;
- frame budget: entry counter and limit checks;
- bounds/reference/initialization checks: retained and not transformed;
- calls, ABI setup, stack layout, and arithmetic: retained and not transformed.

## Static counts

| metric | O0 baseline | O0 diagnostic | O1 baseline | O1 diagnostic |
|---|---:|---:|---:|---:|
| assembly lines | 17938 | 15854 | 17934 | 15854 |
| instructions | 12812 | 10728 | 12812 | 10732 |
| logical instruction sites | 10716 | 10716 | 10720 | 10720 |
| instruction-budget sites | 521 | 0 | 520 | 0 |
| frame-limit sites | 3 | 3 | 3 | 3 |
| static branches | 3031 | 2510 | 3028 | 2508 |
| static calls | 56 | 56 | 56 | 56 |
| stack operations (approx.) | 1978 | 1978 | 2062 | 2062 |
| memory loads (approx.) | 4811 | 3769 | 4892 | 3852 |
| memory stores (approx.) | 1964 | 1443 | 2047 | 1527 |

The load/store columns are static memory-operand approximations, not dynamic
hardware counts. `.text` size for the diagnostic object is unavailable until
the assembly is built on Linux. Frozen baseline shared-object size is 279280
bytes for both S3 O0 and O1; GCC O2 is 15520 bytes and Clang O2 is 15272
bytes in the prior frozen artifact set.

## Diagnostic transformation contract

The benchmark-side rewriter removes only complete four-line sites with the
exact pinned limit `10000000000`. O0 removed 521/521 sites and O1 removed
520/520 sites. The reports contain input/output assembly hashes and record
`unexpected_mutations=0`. Partial, unknown, or mixed layouts fail closed.

No diagnostic shared object was produced in this session. Therefore this
report does not claim diagnostic correctness, native equivalence, or causal
timing.

## Evidence paths

- regenerated assembly: `reports/benchmarks-2.2.2-runtime-attribution/raw/baseline-reproduction/`;
- transformed assembly and static audits: `reports/benchmarks-2.2.2-runtime-attribution/raw/diagnostic-assembly/`;
- rewriter: `tools/runtime_attribution.py`;
- rewriter tests: `tests/test_runtime_attribution.py`.
