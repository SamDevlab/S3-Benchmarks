# S3 V16 — auditably checked 2D stencil interval proof

S3 produces native x86-64 Assembly; GCC *only assembles and links*
the S3 output. A separate C harness independently checks the
8-neighbor row-major stencil sum and times the actual exported
S3 ELF functions (not Python loops).

## Reproduce

Checkout S3 V16 and S3-Benchmarks V16 as sibling directories.
Install Linux/WSL Python, pytest, GCC and objdump.

```sh
python3 benchmarks/v16_interval/run_native_interval_v16.py --session s1
python3 benchmarks/v16_interval/run_native_interval_v16.py --session s2
python3 benchmarks/v16_interval/run_native_interval_v16.py --session s3
python3 benchmarks/v16_interval/run_native_interval_v16.py --session s1 --hp03
python3 benchmarks/v16_interval/summarize_v16.py
python3 -m pytest -q benchmarks/v16_interval/test_v16_artifacts.py
```

The `stencil_source_v16.py` emits ordinary S3 source for three
eight-neighbor 2D stencils with constant row widths 8, 16 and 24.
The S3 generator builds signed-i64 index arithmetic and bounds
checks. V16 changes **only** whether the six interior TSLOAD
bounds comparisons are needed after the two earlier checked
extreme-offset loads. Every load and i64 overflow check remains.

Five JSON files plus the aggregate summary provide:
source SHA-256, per-site audit witness records (IR block,
instruction indexes and offsets), compiler settings,
cold assembly/link times, static objdump instruction/branch
counts, independent reference parity, three separate
same-host sessions with nine interleaved benchmark rounds each,
and a separate HP03-on ablation.

Final recorded 27 cases: 27/27 speedups, median gain 1.137x.
Earlier exploratory timing recorded regressions, so there is no
universal machine-performance claim and no CI runtime threshold.
This study used one WSL x86-64 host; CPU PMU was unavailable.
No production compiler defaults or CPU/GPU dispatch were changed.

The HP03-on ablation did not produce an HP03 versioned fast
loop on these kernels; this does not verify all HP03 interactions.
The V16 checker skips any function containing an already-proven
HP03 fast path.

Correctness and signed-overflow/trap tests are in the S3
companion PR under `tests/test_s3_v16_interval_bounds.py`.
All benchmark JSON tests validate source identity, proof
witness ordering and reference parity without treating a
positive speedup as a correctness requirement.
