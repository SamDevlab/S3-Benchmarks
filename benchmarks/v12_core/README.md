# S3 V12: real native codegen and independent GCC references

**Status:** GO_EXPERIMENTAL / NO-GO for production compiler or GPU dispatch.

This suite **does not use C to compile the S3 mathematical kernel**.
S3 creates x86-64 assembly, GCC only assembles/links it, and the
C harness uses `dlopen` to execute the resulting libraries. The C/GCC
reference implementations are compiled independently with O3.

## Reproducing

From the S3-Benchmarks repository, with the sibling S3 directory at
the same parent (as in `V12-Core-Lab/S3` and `V12-Core-Lab/S3-Benchmarks`):

```sh
python3 benchmarks/v12_core/run_auto_native_v12.py --quick
python3 benchmarks/v12_core/run_auto_native_v12.py
python3 benchmarks/v12_core/run_holdout_native_v12.py
python3 -m pytest -q benchmarks/v12_core/test_v12_core_results.py
```

Requires Linux x86-64, Python 3.12+, GCC, `objdump`, S3 compiler and
its dependencies. The benchmark intentionally does not enable
production optimizations or GPU code generation.

- **Three actual S3 implementations:** generic matrix, V11 full cyclic
  scan, V12 opt-in sparse cyclic scan, from one source-IR certificate.
- **Two C controls:** full-scan algorithm-matched reference and
  sparse set-bit specialist. Their optimization levels differ from S3.
- Fixed alternating rounds, 64 correctness checks per case against
  independent C, with bounded direct-step cross-checks, checksum sink.
- Full corpus: 8 source families/width combinations × 4 horizons = 32.
- Fixed-seed *held-out* corpus: 3 previously unused widths
  (9/23/29) × 3 horizons = 9. First run used no post-hoc candidate
  tuning, but this is **not** independent blinded replication.
- Timings are **native execution only**, not the cost of proof,
  compilation, memory transfer or end-user application throughput.
  Cold compile times are retained separately in JSON.
- Static `objdump` counts include ELF scaffolding and aren't
  dynamic instruction counts. Machine/session frequency control
  and PMU hardware counter analysis remain open work.

## Results

At N=1,000,003, V12/V11 speedups were between 2.41× and 11.33× for
the eight development cases, and between 1.52× and 2.13× for the three
held-out 5-tap cases (single machine/session). GCC sparse specialist
remained faster in all measurements, especially for small kernels.

**Important caveat:** cyclic Rule 90 at W=8/16/32 satisfies
`A^(W/2)=0` over GF(2), so the previous 1,000,000-generation benchmark
is partly degenerate. Nonzero-state rotations and odd-width,
five-tap mappings were added to prevent an accidental Rule 90-only
speed claim. Most data are still noise-sensitive microbenchmarks.

The V12 GPU planner has its own negative-confidence tests in the S3
repository. Physical RX580 tests were carried out in V11 and are not
a new experimental GPU measurement for this V12 suite.

No merge, production changes, Compact changes or DOOM changes are
permitted by this result alone.
