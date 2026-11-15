# V18 — Compiler-synthesized safe guard and native fast/slow stencil loops

Experimental S3 x86-64 native A/B. **No source `width>=3`
guard is present in the test program.** S3 creates the guard and
two loop variants under an explicit opt-in; the original loop
remains the exact fallback. The existing V17 affine checked
interval analysis certifies exactly six redundant bounds tests.

## Reproduce

Checkout matching V18 S3 + S3-Benchmarks branches in sibling
directories, on Linux x86-64/WSL with GCC, objdump,
Python 3.12+ and pytest:

```sh
python3 benchmarks/v18_autoguard/run_autoguard_v18.py --session s1
python3 benchmarks/v18_autoguard/run_autoguard_v18.py --session s2
python3 benchmarks/v18_autoguard/run_autoguard_v18.py --session s3
python3 benchmarks/v18_autoguard/run_autoguard_v18.py --session s1 --hp03
python3 benchmarks/v18_autoguard/summarize_v18.py
python3 -m pytest -q benchmarks/v18_autoguard/test_v18_artifacts.py
```

The harness times actual S3-generated native ELF libraries
using an independent C correctness oracle and rotating C
timed caller. GCC only assembles/links S3 output.

Three same-host sessions, nine rounds per workload, 21 shapes
(7 runtime widths x 3 heights). The final selective-loop
candidate recorded **57/63 faster measurements, six regressions,
and median speedup 1.070x**. All oracle parity checks passed.

### Code growth, including the rejected first design

The initial full-function clone produced 203,450 B of S3
generated Assembly versus baseline 125,953 B (+61.53%).
`results_autoguard_v18_whole_function_preliminary_s1.json`
preserves this negative-control candidate.

The final outer-loop-only clone generates 140,302 B
(+11.39% over baseline, -31.04% versus preliminary).
This does not mean machine instructions are 11% larger:
the native static `auto_stencil` function grows
517 -> 918 disassembled instructions, as both hot and
cold loop versions are retained. Static counts are NOT
dynamic PMU retired instructions.

The original S3 source used is in `source_v18.py`.
A matching standalone S3 fixture is committed in the
S3 repository's tests. The benchmark JSON records
source SHA-256, exact per-load audit witnesses,
compile/link timings, static Assembly stats,
independent C parity, all favorable and unfavorable
measurements, and source/feature provenance.

Single machine; no population-level performance
confidence, no GPU result and no release/merge.
Instruction-budget preservation across all native
budget modes is tested in the companion S3 PR.
