# Pressure Map V12

## Scope

This map records the 2.2.4 benchmark-only safe instruction-budget
prototype. The pinned S3 checkout is read-only at
`e07d0b5464bf472b2ca18993f3e196a234ff0fc5`.

## Closed evidence

- P0 is the current global count-up oracle.
- P1 `GLOBAL_COUNTDOWN_EXACT` passed the E0 native boundary differential:
  21/21 cases, including zero, one, 32-bit boundary values, a large value,
  repeated calls, and standalone execution.
- The structural corpus passed 12/12 cases, including fused logical weight
  two and exact failure-site preservation.
- RMSD, XSBench, and JSMN passed correctness for P0, PNEG, P1, GCC, and
  Clang variants at O0/O1.

## Remaining pressures

The timing result does not show a material cross-workload recovery. P1
recovers 8.37% at RMSD O0 and 4.40% at JSMN O0, while the other O0/O1
measurements are approximately neutral or slightly regressed. P1 therefore
does not close the native overhead pressure and is not promoted.

The no-budget PNEG build remains a lower-bound diagnostic only. P2
`CALL_AWARE_SEGMENT_PRECHARGE_EXACT` remains blocked until an explicit
logical-S3-Assembly-to-native segment map is proven. No heuristic slicing is
accepted as an exact implementation.

## Next research boundary

The next safe experiment must explain the residual work between P1 and PNEG
without weakening E0. Candidate causes remain representation staging, helper
and call overhead, frame or initialization traffic, register pressure, and
native instruction selection. This map does not authorize production changes.
