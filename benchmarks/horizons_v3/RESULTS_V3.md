# S3 Scientific Horizons V3 — Benchmark & Compiler Bottleneck Report

- **Campaign:** `S3_SCIENTIFIC_HORIZONS_V3`
- **S3 Commit:** `46f286c2182e65eb2ae4c9953a5a8e18502bfb5a` (`feat/s3-scientific-experiments-v3`, PR #377 stacked on PR #376)
- **Environment:** `Linux-4.4.0-26100-Microsoft-x86_64-with-glibc2.39`, Python `3.12.3`, `gcc -shared -fPIC -O2` FFI wrapper
- **Methodology:** 3 warmups + 9 measured samples per profile (`O0 PER_INSTRUCTION`, `O1 PER_INSTRUCTION`, `O1 EXACT_SEGMENT`); peak RSS = `40,132 KiB`; `max_instructions = 500_000_000`.
- **Verification:** `pytest -v benchmarks/horizons_v3/test_horizons_v3.py` -> `1 passed`

## 1. Benchmark Results (`results_v3.json`)

| Experiment | Profile | Median (us) | Mean (us) | P95 (us) | S3 ASM Insts | S3 Blocks | `.text` (bytes) | Accuracy / Parity |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `mechanics_lab_2000steps` | `O0 PER_INSTRUCTION` | 768.0 | 771.4 | 778.1 | 2387 | 517 | 237,653 | `abs_error_x=4.04e-13`, `abs_error_energy=0.0` (PASS) |
| `mechanics_lab_2000steps` | `O1 PER_INSTRUCTION` | 702.1 | 703.0 | 705.9 | 1502 | 281 | 157,024 | `abs_error_x=4.04e-13`, `abs_error_energy=0.0` (PASS) |
| `mechanics_lab_2000steps` | `O1 EXACT_SEGMENT` | 695.8 | 700.3 | 712.4 | 1502 | 281 | 232,337 | `abs_error_x=4.04e-13`, `abs_error_energy=0.0` (PASS) |
| `materials_diffusion_101x500` | `O0 PER_INSTRUCTION` | 3253.2 | 3244.4 | 3356.3 | 2311 | 505 | 229,644 | `max_abs_error=1.47e-06`, `cfl_r=0.2` (PASS) |
| `materials_diffusion_101x500` | `O1 PER_INSTRUCTION` | 2742.4 | 2745.3 | 2784.4 | 1456 | 277 | 151,813 | `max_abs_error=1.47e-06`, `cfl_r=0.2` (PASS) |
| `materials_diffusion_101x500` | `O1 EXACT_SEGMENT` | 2628.6 | 2659.2 | 2724.9 | 1456 | 277 | 223,479 | `max_abs_error=1.47e-06`, `cfl_r=0.2` (PASS) |
| `bio_reaction_kinetics_2000steps` | `O0 PER_INSTRUCTION` | 756.8 | 764.1 | 775.0 | 2310 | 517 | 228,787 | `abs_error_a=2.66e-15`, `mass_err=0.0` (PASS) |
| `bio_reaction_kinetics_2000steps` | `O1 PER_INSTRUCTION` | 694.5 | 694.6 | 697.5 | 1425 | 281 | 148,228 | `abs_error_a=2.66e-15`, `mass_err=0.0` (PASS) |
| `bio_reaction_kinetics_2000steps` | `O1 EXACT_SEGMENT` | 620.7 | 638.8 | 653.3 | 1425 | 281 | 219,151 | `abs_error_a=2.66e-15`, `mass_err=0.0` (PASS) |
| `biomechanics_joint_1000steps` | `O0 PER_INSTRUCTION` | 391.1 | 392.0 | 396.0 | 2218 | 492 | 220,572 | `theta_final=0.1968029741` (PASS) |
| `biomechanics_joint_1000steps` | `O1 PER_INSTRUCTION` | 428.5 | 400.1 | 435.4 | 1423 | 280 | 148,109 | `theta_final=0.1968029741` (PASS) |
| `biomechanics_joint_1000steps` | `O1 EXACT_SEGMENT` | 346.5 | 358.9 | 433.3 | 1423 | 280 | 219,062 | `theta_final=0.1968029741` (PASS) |
| `fem_1d_bar_2elem` | `O0 PER_INSTRUCTION` | 3.0 | 3.2 | 3.5 | 2191 | 492 | 216,856 | `max_abs_error=0.0` (PASS) |
| `fem_1d_bar_2elem` | `O1 PER_INSTRUCTION` | 2.9 | 3.0 | 3.1 | 1351 | 268 | 140,403 | `max_abs_error=0.0` (PASS) |
| `fem_1d_bar_2elem` | `O1 EXACT_SEGMENT` | 3.4 | 3.5 | 4.2 | 1351 | 268 | 206,614 | `max_abs_error=0.0` (PASS) |

## 2. Confirmed Compiler Bottlenecks & Ergonomic Gaps

1. **High Dynamic Instruction Budget Pressure on Nested Loops:**
   `materials_diffusion_101x500` (`N=101`, `500` FTCS steps) exceeded `max_instructions=50_000_000` in `__s3mod_s3_materials_diffusion__diffuse_1d_ftcs` (at `while_condition_39, TLOAD`), requiring `max_instructions=500_000_000`. Even for a small `101 x 500` stencil (~`50,000` inner updates), bounds checks, slice indexing, and per-instruction/segment budget accounting consume >50M virtual budget units.
2. **Code Size vs. Runtime Trade-off (`O1`):**
   `O1` reduces S3 assembly instruction count by **35.8%–38.3%** and `.text` size by **~34%** under `PER_INSTRUCTION`. Switching to `EXACT_SEGMENT` lowers median wall-time on compute-heavy loops (`bio_reaction_kinetics`: `-10.6%` vs `O1 PER_INSTRUCTION`; `materials_diffusion`: `-4.1%`), at the cost of expanding `.text` back to `206–232 KB` due to segment boundary accounting.
3. **S3 Language & Type-Checker Gaps Observed While Building `s3_sci_core` and Experiments:**
   - **No scientific notation in float literals:** `1e-12` fails with `ParseError`; requires `0.000000000001`.
   - **No multi-line parenthesized imports:** `from mod import (a, b)` fails with `ParseError`.
   - **No implicit `tryte` -> `i64` literal coercion in comparisons:** `len(a) < 4` fails type checking; requires `to_i64(4)` or typed local `mut four: i64 = 4`.
   - **No `&mut [f64]` -> `&[f64]` slice borrow coercion:** passing a mutable slice into a read-only slice parameter (e.g., `vec_copy`) is rejected.
   - **Cross-module FFI symbol mangling:** `compile_sources` exports functions as `__s3mod_<module>__<fn_name>`.
