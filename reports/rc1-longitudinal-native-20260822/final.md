# S3 RC1 longitudinal native benchmark

## Scope

- S3 RC1: `9b39c7070d7bfa23d709c2128eb0b0bbef164177`
- M2.30: `e23b092bec100cedc520841a7dd0f4488090b6a1`
- Benchmark final HEAD: `6ae9e1f8bcff79557c02eb20c786e70d42eeda1d`
- P1 V2 measurement HEAD: `3716b0bea81776614b2f729f3079f32595186498`
- P7-P9 measurement HEAD: `6ae9e1f8bcff79557c02eb20c786e70d42eeda1d`
- Host: Linux x86-64 VirtualBox, affinity `taskset -c 0`
- S3 was read-only throughout. No S3 source, tests, tags, or releases changed.

## P1 measurement quality

Campaign V1 remains preserved as `INCONCLUSIVE_CONTROL_DRIFT_HIGH`.
Campaign V2 persisted individual vectors and passed correctness before timing.
The primary attempt had 30 samples per fixture/checkpoint and the bounded retry
also had 30. Control drift was `72.1146%` and `13.0953%`, respectively, both
above the declared `5%` gate. The retry therefore also classified as
`INCONCLUSIVE_ENVIRONMENT`; no further timing retry is authorized by policy.

The H4/M2.30 to H5/RC1 raw geomean delta was `+0.3703%`. The paired median was
`-0.0550%` with bootstrap 95% CI `[-0.4553%, +0.6191%]`, so the comparison is
inconclusive. RC1 versus same-run C-O2 was `48.1984x` by fixture-median
geomean. C-O3 was not timed in V2 and is recorded as unavailable rather than
borrowed from the non-comparable V1 protocol.

`SAMPLE_LEVEL_DATA_AVAILABLE=YES` and the retry vectors are in
`p1-v2/raw/samples.json` and `p1-v2/raw/samples.csv`. The shared C-O0/O2/O3
binary manifest is `p1-v2/control-manifest.json`.

## P7-P9 native workloads

All three workloads passed correctness before timing and persisted 30 samples
per variant, but each remained `EXPERIMENTAL` because C-O2 control drift was
`361.3685%` for P7, `640.6807%` for P8, and `77.3083%` for P9. These numbers
are evidence of an unstable measurement environment, not promoted performance
claims.

The structural evidence is still useful: RC1 P7/P8/P9 O1 instruction counts
were respectively 3043, 2583, and 3270 versus C-O2 counts 38, 18, and 40.
The x86 analyzer did not produce meaningful C load/store or stack counts for
these controls, so those ratios remain unavailable. P9's struct subkernel was
not measured and is explicitly not claimed.

## Conclusion

`P1=P1_V2_INCONCLUSIVE_ENVIRONMENT`, `P7=EXPERIMENTAL`, `P8=EXPERIMENTAL`,
and `P9=EXPERIMENTAL`. The primary remaining blocker is measurement-environment
control variance. A secondary structural hypothesis is S3 native code
expansion and memory-state materialization, supported by the P7-P9 structural
counts but not sufficient for an optimization or RC2 claim.

`M1.99=PASS_CHARACTERIZATION_ONLY`; it remains hosted Emulator evidence with no
native speedup claim. P2-P6 and P10-P18 remain contracts. No S3 T4, full suite,
merge, tag, release, shutdown, or S3 modification was performed.
