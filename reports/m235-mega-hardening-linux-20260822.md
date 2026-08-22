# M2.35 Mega-Hardening Linux Characterization

- S3 source HEAD: `6604b9d07c607579df9c5c0759d8f2a708ba72d1`
- Benchmark HEAD: `fd5f5b48f36a1c4805bfbc69590f220e70d65951`
- Protocol: M1.99 correctness and hosted characterization
- Correctness: `PASS`
- Timing class: `CHARACTERIZATION_ONLY`
- Native speedup claim: `NO`
- Raw transcript SHA-256: `b93ddf26b0d3f42fd352025835ddf73f24550672b581f1bbc870437395813c8a`

The current benchmark repository exposes the JSMN/M1.99 harness only. P1-P18
workloads were not present as executable, so no synthetic replacement was run.
Timing compares the original and transformed parsed AssemblyProgram in the
hosted Emulator. Native x86 generation remains a structural probe only.
