# XSBench-Compatible Lookup Contract

This document defines the qualified subset. It is not a claim to reproduce
the complete XSBench application or its official figure of merit.

```text
UPSTREAM=ANL-CESAR/XSBench
UPSTREAM_SHA=ba08e5221af6106252b866e50ea123c69d31a4e2
WORKLOAD_NAME=XSBENCH_COMPATIBLE_LOOKUP_KERNEL
WORK_UNIT=XS_LOOKUP
NUMERIC_TYPE=f64
```

## Algorithm

For each lookup, the fixture selects a material and nuclide record, searches
the sorted energy grid with the upstream binary-search invariant, obtains the
two bounding points, linearly interpolates the five microscopic channels, and
accumulates the concentration-weighted macroscopic result. The observable is
the deterministic sum of the five output channels over the exact lookup tier.

The binary search is unchanged in meaning. A small benchmark-local helper is
used so the native lowering sees the same search as a callable unit; this is
not a replacement algorithm.

## Flat representation

The deterministic adapter uses parallel flat arrays encoded in one bounded
metadata slice plus a flat f64 data slice. Metadata contains the material and
nuclide mapping, energy ticks, offsets, and the lookup count. The layout is
explicit and identical for the S3 and C reference drivers; no multidimensional
array or upstream application data generator is introduced.

## Fixtures

| Tier | Lookups | Purpose | Oracle |
|---|---:|---|---:|
| TINY | 1 | hand-verifiable boundary | 117.52 |
| SMALL | 4 | focused search/interpolation matrix | 1212.472 |
| MEDIUM | 8 | representative deterministic pattern | 2444.096 |

There is no LARGE fixture in this campaign. Initialization, data generation,
parallel execution, device transfer, and alternative optimized kernels are
excluded.

## Oracle and comparison policy

The Python oracle in `benchmarks/scientific/xsbench/contract.py` is
independent of the S3 implementation. Exact fixture values are compared with
the predeclared floating-point tolerance in the focused tests. Native and
FFI results use the same scientific values, not an unrelated integer canary.
