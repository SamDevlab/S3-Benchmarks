# XSBench Direct FFI Measurement Method

The existing Phase A direct-kernel protocol was reused without creating a new
FFI protocol. It uses `dlopen`, `dlsym`, a function pointer, the common C
driver, `CLOCK_MONOTONIC_RAW`, fixed runtime `K`, five warmups, 30 repetitions,
balanced interleaving, raw samples, artifact hashes, and Run A/Run B.

Setup outside the timed region includes library loading, symbol lookup,
allocation, fixture initialization, and warmups. The timed region contains
only `K` calls to the exported batch lookup. It contains no allocation, I/O,
JSON, filesystem, Python, or fixture generation.

```text
TIMING_SCOPE=KERNEL_PLUS_MATCHED_FFI_BOUNDARY
WARMUPS=5
REPETITIONS=30
K_FINAL_TINY=1000000
K_FINAL_SMALL=100000
K_FINAL_MEDIUM=100000
SAME_BINARY_ACROSS_K=PASS
SAME_ARTIFACT_A_B=PASS
SYNTHETIC_TIMING=ABSENT
```

The C references use the same fixture, search, interpolation, accumulation,
lookup count, and matched `dlopen`/`dlsym` call model. They are GCC O2 and
Clang O2 single-thread references, without OpenMP, LTO, or fast-math.
