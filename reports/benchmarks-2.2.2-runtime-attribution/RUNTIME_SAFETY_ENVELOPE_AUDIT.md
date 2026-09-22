# Runtime Safety Envelope Audit

Campaign: `S3_BENCHMARKS_2_2_2_1_LINUX_NATIVE_RESUME_CAUSAL_CLOSURE`

This is a benchmark-side audit of assembly generated from pinned S3 source
`e07d0b5464bf472b2ca18993f3e196a234ff0fc5`. No S3 source, compiler, runtime,
ABI, or safety implementation was changed.

## Transformation boundaries

The instruction diagnostic removes only the exact four-line accounting block at
the pinned `10000000000` limit. The frame diagnostic removes only the exact
three entry/exit accounting pairs at the pinned frame limit of 1024. Bounds,
initialization, indexing, calls, ABI setup, arithmetic, control flow, prologue,
return path, and failure-report blocks remain in the diagnostic artifacts.

Both transforms are fail-closed and benchmark-side. They are not production
artifacts and do not establish a safe optimized runtime mode.

## Static counts

| metric | O0 baseline | O0 no-budget | O1 baseline | O1 no-budget |
|---|---:|---:|---:|---:|
| ELF bytes | 279240 | 262856 | 279240 | 262856 |
| `.text` bytes | 72420 | 56781 | 72725 | 57116 |
| instruction-budget sites | 521 | 0 | 520 | 0 |
| frame-limit sites | 3 | 3 | 3 | 3 |

The instruction-budget rewrite removed 2084 O0 and 2080 O1 static
instructions, exactly four per recognized site. The frame rewrite removed three
entry accounting groups and three exit accounting groups per level, while
preserving function prologues and returns. `UNEXPECTED_MUTATIONS=0` for both
rewriters.

Static counts are not dynamic execution counts. Loops and calls can amplify
the execution of any remaining checks.

## Native correctness and timing

The no-budget variants passed the independent TINY/SMALL/MEDIUM oracle. The
G/H protocol passed for all six base variants. The frame no-budget/no-frame
variants also passed correctness and I/J reproducibility, but removing frame
accounting increased runtime at both O0 and O1. Consequently frame causality is
not confirmed and no frame share is reported.

## Provenance

Raw evidence is preserved under:

`reports/benchmarks-2.2.2-runtime-attribution/raw/native-resume-20260922-074209/`

The environment changed relative to the earlier E/F fingerprint, so the
baseline shared objects are classified as a semantic rebuild with toolchain
drift rather than byte-identical frozen reproductions.
