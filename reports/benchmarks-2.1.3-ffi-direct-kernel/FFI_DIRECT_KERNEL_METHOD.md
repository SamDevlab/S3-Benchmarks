# FFI Direct Kernel Method

The common C driver uses dlopen and dlsym for every variant. Allocation,
initialization, dynamic loading, warmups, and output serialization are outside
the clock_gettime(CLOCK_MONOTONIC_RAW) call loop. The metric is
KERNEL_PLUS_MATCHED_FFI_BOUNDARY, not pure kernel time.

The four workload families are BabelStream triad, PRK nstream, PolyBench GEMM,
and RMSD batch. Each has the same C ABI shape and was tested with
S3_FFI_O0, S3_FFI_O1, GCC_O2, and CLANG_O2. The O1 ELF export is resolved from
the actual symbol table; the S3 compatibility spelling is used only when the
generated artifact exposes the `s3_` prefix.

K is a runtime driver argument; libraries are built once and reused across all
calibration and official K values. Warmups are 5, repetitions are 30, and the
driver is pinned with `taskset -c 0`. No LTO, -Ofast, -ffast-math, or BLAS is
used.

The selected K values are 1,000,000 for triad and nstream, and 100,000 for
GEMM and RMSD. The latter two are marked `FALLBACK_BELOW_TARGET_MIN` because
the preferred 10 ms fastest-variant floor could not coexist with the 120 s
per-sample timeout for the S3 variants. Their timing remains real, bounded,
and reproducible; no synthetic timing or speed claim is introduced.

The official raw evidence is in
`raw/ffi-direct-kernel-20260921-192448-009785706/`. Phase A produced 16/16
correctness points, complete Run A and Run B, identical frozen artifacts, and
reproducible summaries for all four families.
