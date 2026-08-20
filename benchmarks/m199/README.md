# M1.99 self-move benchmark

This schema-v2 campaign compares the same parsed `AssemblyProgram` and
workload. OFF uses the original `AssemblyProgram`; ON uses
`eliminate_redundant_noop_moves(original)`. The corrected helper preserves the
Assembly program, so the hosted emulator is timed for characterization only.

Correctness controls run before timing and include initialized self-moves,
uninitialized self-moves, and the instruction-limit boundary. The timing
protocol uses five warmups, thirty measured repetitions, and deterministic
alternating OFF/ON order. Each result records median, minimum, maximum, IQR,
and raw samples.

Timing is hosted Emulator execution. Native x86 generation is a supplementary
structural probe only; no native speedup claim is made. A native comparative
result is valid only when a supported Linux x86-64 toolchain and equivalent
controlled execution are actually available.

The benchmark resolves the local Git HEAD of both the tested S3 checkout and
this benchmark repository and fails closed if either differs from its pinned
evidence SHA. The M1.99 baseline is derived from the unique Git commit that
introduced `bootstrap/s3/codegen_optimization.py` and its immediate parent.
