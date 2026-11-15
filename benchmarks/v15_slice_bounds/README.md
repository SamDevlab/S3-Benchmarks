# S3 V15 — Native x86-64 exact slice-bound reuse

**Status: GO_EXPERIMENTAL only, never production/automatic.**

Real S3 compiler O1 emits ELF x86-64 assembly; GCC only assembles
and links it. The separate C harness uses `dlopen` to call S3 code
and an independent mathematical oracle to check 6 real configurations.

## Reproduction

From the `S3-Benchmarks` repository, with sibling `S3` checkout:

```sh
python3 benchmarks/v15_slice_bounds/run_native_bounds_v15.py --session s1
python3 benchmarks/v15_slice_bounds/run_native_bounds_v15.py --session s2
python3 benchmarks/v15_slice_bounds/run_native_bounds_v15.py --session s3
python3 benchmarks/v15_slice_bounds/run_native_bounds_v15.py --session s1 --hp03
python3 -m pytest -q benchmarks/v15_slice_bounds/test_v15_artifacts.py
```

Requires x86-64 Linux/WSL, S3 compiler dependencies, GCC, objdump,
Python 3.12+ and pytest.

Two S3 source kernels call the same indexed slice element twice or
three times in a counted loop. The A/B toggles only the V15 native
backend feature. HP03 loop versioning is disabled deliberately in
the principal A/B; it is enabled in a separate interaction test.
HP02 scalar promotion and LOOP_HYBRID instruction budgeting remain
the same in both variants. Three separate host sessions, nine
rotating timed rounds per session.

Isolated V15 medians of per-session speedup ratios:

| S3 function | 64 values | 1,024 values | 8,192 values |
|---|---:|---:|---:|
| loop_dup | 1.10x | 1.03x | 1.10x |
| sum_three | 1.24x | 1.39x | 1.40x |

The pass only eliminates repeat bounds checks: one for loop_dup,
two for sum_three. An earlier checked read must have completed.
The actual second/third memory loads remain, and no numeric
range inference or unsafe unchecked access is introduced.

**Negative result and correction retained:** HP03 has a separate
fast loop path with bounds proven already. The first V15 attempt
after HP03 unexpectedly changed slow loop layout and regressed a
case to 0.764x. `results_native_bounds_v15_s1_hp03_pre_guard.json`
preserves that measurement. The final V15 gate explicitly skips
HP03-versioned functions; `results_native_bounds_v15_s1_hp03.json`
proves the generated assembly is identical to HP03 alone.

The remaining timing variation with identical assembly reflects
host/microbenchmark noise. Never treat a benchmark ratio as a CI
correctness gate. Only source/IR proof invariants and reference
parity authorize an experimental candidate.

No new GPU benchmark is asserted; the physical AMD RX580 remains
the V14 hardware study. The original V14 tests and CI-budget
blocker are documented in their respective Draft PRs. Compact,
DOOM and production remain frozen.
