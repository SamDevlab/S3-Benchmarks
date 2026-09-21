# Direct Kernel Methodology 2.1.1

The benchmark repository remains pinned to the S3 candidate and does not modify
the S3 compiler. The audit selected `METHOD_C_IN_PROCESS_AMORTIZATION` because no
supported direct timer or callable S3 kernel ABI was found in the pinned source.

## Boundaries

Each pilot allocates and initializes flat arrays once, then executes the same
kernel body for `K` iterations inside one process. A final observable prevents
dead-code elimination. The external wall clock measures the resulting process
envelope; any fitted slope is labeled `EMPIRICAL_SLOPE`, not physical kernel
time.

K levels planned: `1, 10, 100, 1000`.

The C references use `gcc -O2` or `clang -O2` when available, without BLAS,
`-ffast-math`, or `-Ofast`. Their flat layouts and loop order are explicit in
the generated sources. The Linux x86-64 hosted replay is **available**. This is
not direct native S3 kernel execution: the pinned source exposes no callable
kernel ABI or internal timer, so no native speedup claim is made.

No naive empty-process subtraction is used. No S3 optimization was made.
