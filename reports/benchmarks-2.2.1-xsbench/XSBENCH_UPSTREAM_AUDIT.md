# XSBench Upstream Audit

## Identity and license

```text
UPSTREAM=ANL-CESAR/XSBench
UPSTREAM_SHA=ba08e5221af6106252b866e50ea123c69d31a4e2
LICENSE=MIT-like permissive Argonne license
UPSTREAM_CODE_VENDORED=NO
```

The pinned `LICENSE` file contains the Argonne copyright notice and a
permissive warranty disclaimer. No upstream source is vendored in this
repository.

## Baseline consulted

The audit covered `README.md`, `LICENSE`, and the baseline sources under
`openmp-threading/`, including the grid initialization, material setup, and
lookup path. The represented kernel is the serial semantic core of
`calculate_macro_xs`: material and nuclide accumulation, per-nuclide binary
search in sorted energy grids, and linear interpolation of the five
cross-section channels.

The upstream application also contains data generation, OpenMP execution,
alternative hash/grid modes, and other variants. Those are outside this
qualification and are not claimed here.

## Reuse audit

| Requirement | Classification |
|---|---|
| f64 arithmetic and interpolation | REUSE_DIRECTLY |
| i64 indices and counts | REUSE_DIRECTLY |
| loops, conditionals, nested control | REUSE_DIRECTLY |
| flat indexed data and borrowed slices | ADAPT_EXISTING_CONTRACT |
| binary search | ADAPT_EXISTING_CONTRACT; algorithm preserved |
| function calls | REUSE_DIRECTLY |
| struct-like records | ADAPT_EXISTING_CONTRACT; explicit flat metadata |
| native FFI boundary | REUSE_EXISTING_FFI |
| sqrt/exp/pow | not required by this XSBench lookup subset |

No true language, runtime, backend, provenance, license, or ABI blocker was
found. The benchmark source factors the search helper to preserve the same
algorithm in the native integrated workload; it does not replace binary
search with a linear, hash, or precomputed lookup.

## Factual campaign identity

```text
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
S3_SOURCE_CHANGED=NO
BENCHMARK_FUNCTIONAL_HEAD=edbce77725e1193e602d93258431e4fae85d6694
```
