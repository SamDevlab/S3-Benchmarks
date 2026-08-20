# M1.99 self-move benchmark

This campaign compares the same parsed AssemblyProgram and workload. OFF uses
the original AssemblyProgram; ON uses
`eliminate_redundant_noop_moves(original)`. The workload covers redundant and
non-redundant moves, a call, mutable memory, and control flow.

The Windows host cannot execute the generated Linux x86-64 native artifact.
Timing is hosted Emulator execution. Native x86 generation is a supplementary
structural probe only, so the campaign makes no native speedup claim.

The benchmark resolves the local Git HEAD of both the tested S3 checkout and
this benchmark repository and fails closed if either differs from its pinned
evidence SHA.
