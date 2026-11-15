# S3 V17 — Actual native dynamic-width 2D stencil A/B

**Research only. Default compiler behavior is unchanged.**

## Reproduction

Checkout matching S3 V17 + S3-Benchmarks V17
branches in sibling directories on a Linux x86-64
host or WSL. Requires GCC, objdump, Python and pytest.

```sh
python3 benchmarks/v17_dynamic/run_dynamic_v17.py --session s1
python3 benchmarks/v17_dynamic/run_dynamic_v17.py --session s2
python3 benchmarks/v17_dynamic/run_dynamic_v17.py --session s3
python3 benchmarks/v17_dynamic/run_dynamic_v17.py --session s1 --hp03
python3 benchmarks/v17_dynamic/summarize_v17.py
python3 -m pytest -q benchmarks/v17_dynamic/test_v17_artifacts.py
```

`source_v17.py` contains two real S3 programs:
`dynamic_neighbor` and `dynamic_stencil`. Both
use a runtime `width: i64` and an explicit
source guard `width >= 3`. The first has a
fully equivalent slow fallback with every original
index check preserved. The second iterates
interior 2D cells using `y` and `x` induction
variables and computes base indexes from them.

S3 compiles exactly the same O1 source and IR to
native x86-64 Assembly with the opt-in V17 interval
proof OFF and ON. GCC **only assembles/links the
S3-generated machine code**. The C harness
`native_dynamic_ab_v17.c` provides independent
oracle outputs plus a low-overhead timer which
calls both actual S3-exported native functions.
No C implementation of the stencil is used inside
the timed region.

The proof recognizes a dominating original
source guard, two earlier checked endpoint
TSLOADs, and six middle indices of the form
`base+a*width+b`. All arithmetic, actual loads,
overflow traps and fallback paths remain.
Every proof witness includes guard true-edge,
instruction indices and symbolic offsets.
The accompanying JSON includes the S3 source
SHA-256 and compiler flag provenance.

## Recorded hardware results

Single machine, Linux/WSL x86-64, three distinct
process sessions, 9 rotating measurements per
workload/session. 7 widths (3,5,8,16,31,48,64),
3 heights (64,256,1024): **63 paired ratios**.

**Median of the 63 ratios = 1.120x**, with
**58 favorable cases and five regressions**.
All 63 native outputs matched the independent
C oracle. The separate HP03-on trial retained
native parity, but some cases regressed.

Machine-generated `summary_v17.json` contains
all 21 per-shape median-of-session comparisons,
the actual unfavorable rows, session aggregates
and source identity. Do not mistake the 63 results
for independent physical machines or a statistical
confidence interval.

The S3 native static `dynamic_stencil` function
declined from 544 to 519 static instructions
and 169 to 157 static conditional branches.
**These are static objdump counts, not CPU PMU
retired instructions.** Cold build times are
separately recorded and not included in the
per-call native execution timing.

## Qualification / known limits

This is not general automatic guard insertion:
the source must already provide a guard and a
fallback. The false branch is not optimized.
Current interval proofs are limited to a single
straight-line slice-load block, exact pointer/
length and local affine indices with a non-mutated
runtime width. It does not claim multi-host
replication, a new Big-O algorithm, physical
GPU acceleration, green GitHub Actions or
production readiness. V17 is disabled by default.
