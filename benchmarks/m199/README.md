# M1.99 self-move benchmark

This campaign compares the same validated AssemblyProgram with the
`TMOV rN, rN` elimination pass disabled and enabled. The workload covers
redundant and non-redundant moves, a call, mutable memory, and control flow.

The Windows host cannot execute the generated Linux x86-64 native artifact.
The campaign therefore certifies semantic equivalence and records hosted
emulator characterization without making a native speedup claim.
