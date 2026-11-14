# S3 V5 Ecosystem Forge — Cross-Subsystem Benchmark Suite

**Campaign:** `S3_V5_ECOSYSTEM_FORGE`  
**Timestamp (UTC):** `2026-11-14T10:07:34.234712+00:00`  
**Environment:** WSL2 Linux x86-64 (`Python 3.12.3`, `gcc 13.3.0`, `node v24.21.0`)

## Evaluated Repository Revisions
- `S3`: `9c1bec32c181710eec6e99c3056825d85b8412c6` (`exp/s3-v5-ecosystem-compiler`)
- `S3-Elite-Lab`: `5c9c5b661e73666544059d708a7e0a0fd69ed56e` (`feat/s3-v5-doom-wasm`)
- `S3-wt-compact-v18`: `de77b2cd6b3649be967f0f30a88aae59f69cfe24` (`exp/s3-v5-compact`)
- `S3-wt-s3cng`: `8e79f07825c7648a12310f90f48f9c59f8109264` (`exp/s3-v5-s3cng`)

## Reproduction
```bash
wsl bash -lc "cd /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks && python3 benchmarks/v5_ecosystem_forge/run_v5_suite.py"
```

## 1. Predictive Compute (`CRChain` Native SCEV Lowering vs Standard S3 `.so`)
Measured via `ctypes` over compiled `.so` artifacts (`warmups=3`, `samples=9`, `predictive_small_t_cutoff=4`):

| Kernel | `T` Steps | Calls / Sample | Exact Parity | Standard S3 `.so` Median (ms) | `CRChain` Native Median (ms) | Speedup |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| `sum_i2` | 10 | 200 | `true` | 0.1093 | 0.1205 | 0.91x |
| `sum_i2` | 100 | 200 | `true` | 0.1417 | 0.1208 | 1.17x |
| `sum_i2` | 1,000 | 200 | `true` | 0.4542 | 0.1179 | 3.85x |
| `sum_i2` | 10,000 | 20 | `true` | 0.3618 | 0.0134 | 27.00x |
| `sum_i2` | 100,000 | 5 | `true` | 0.8816 | 0.0039 | **226.05x** |
| `triangular_cubic` | 10 | 200 | `true` | 0.1076 | 0.1410 | 0.76x |
| `triangular_cubic` | 100 | 200 | `true` | 0.1516 | 0.1417 | 1.07x |
| `triangular_cubic` | 1,000 | 200 | `true` | 0.5561 | 0.1362 | 4.08x |
| `triangular_cubic` | 10,000 | 20 | `true` | 0.4540 | 0.0150 | 30.27x |
| `triangular_cubic` | 100,000 | 5 | `true` | 1.1100 | 0.0043 | **258.14x** |

*Negative cost-crossover finding:* At `T=10`, binomial/overflow-safe constant-time evaluation incurs `0.76x–0.91x` overhead compared to a tiny native loop, validating static/dynamic cutoff gating (`predictive_small_t_cutoff`).

## 2. x86-64 Scientific Kernels (`S3` vs `GCC -O3`)
### 2.1 SSE2 Vector Dot (`f64_vector_dot`)
| `n` | Reps | S3 Scalar (ms) | S3 SIMD (ms) | `GCC -O3` (ms) | SIMD vs Scalar | SIMD / GCC Ratio | Max Abs Diff vs GCC |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 256 | 1562 | 2.9965 | 0.2483 | 0.2927 | 12.07x | **0.85x** | 0.0 |
| 1,024 | 390 | 3.0114 | 0.2343 | 0.3148 | 12.85x | **0.74x** | 0.0 |
| 4,096 | 97 | 3.3387 | 0.3281 | 0.3340 | 10.18x | **0.98x** | 2.39e-12 |
| 16,384 | 24 | 3.3511 | 0.6017 | 0.3495 | 5.57x | 1.72x | 5.12e-13 |

### 2.2 Chunked 2D Poisson (`cg_solve_csr_jacobi_chunk`, `chunk_iter=50`)
| Grid | Unknowns | Iters (S3 / GCC) | S3 Exec (ms) | GCC `-O3` (ms) | Max Err vs GCC | Max Err vs True | Validity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `16x16` | 256 | 58 / 58 | 3.2311 | 0.1527 | 0.0 | 3.80e-14 | `VALID` |
| `24x24` | 576 | 88 / 88 | 9.9906 | 0.3964 | 0.0 | 5.88e-14 | `VALID` |
| `32x32` | 1,024 | 118 / 118 | 21.6893 | 0.9980 | 0.0 | 4.86e-14 | `VALID` |
| `48x48` | 2,304 | 176 / 176 | 68.7480 | 3.0252 | 0.0 | 6.39e-14 | `VALID` |

*Spill / Codegen Progress:* Under `O1_ra`, `total_asm_lines = 46,385`, `csr_matvec_f64` spills dropped `69 -> 3`, `cg_solve_csr` spills dropped `204 -> 32`, and `cg_solve_csr_jacobi` (`movq = 18`, `movsd = 53`, `fp_arith = 78`).

## 3. S3 Compact V19 (`V5-COMPACT-TURBO`, `warmups=1`, `repeats=3`)
| Corpus | Output Bytes | SHA-256 Identical | `wt_local_O0` Enc (MB/s) | `s3_v5_O1_default` Enc (MB/s) | Encode Speedup | `s3_v5_O1_default` Dec (MB/s) |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| `head_s3_compact_1mib` | 301,316 | `true` | 2.87 | 19.67 | **6.86x** | 140.38 |
| `high_byte_wrap_512kib` | 8,774 | `true` | 6.38 | 33.58 | **5.26x** | 221.33 |
| `repetitive_512kib` | 12,145 | `true` | 7.17 | 41.17 | **5.74x** | 239.71 |

## 4. DOOM / WASM (`S3-Elite-Lab`) & S3C-NG (`S3-wt-s3cng`)
- `S3-Elite-Lab`: `node --test-isolation=none --test tests/doom-m55-line-trace.test.mjs` -> **9 passed, 0 failed**.
  - `m48` (`37,977` B, `sha256=1486ee3fe76f521a...`, `evidence_sha_match=true`): `s3Wasm` mean `12.065 ms` vs `jsReference` `2.555 ms` (`4.722x`, `140,000` calls, `0` traps/fallbacks).
  - `m50` (`42,110` B, `sha256=4d468a0feb2ea683...`, `evidence_sha_match=true`): `m50Reduced` `8.1083 ms` (`50,000` compared plans, `0` traps/fallbacks).
  - `m55` (`10,828` B, `sha256=fafaeefe5666b320...`, `evidence_sha_match=true`): mean geometry `0.9809 ms` (S3 WASM) vs `0.2373 ms` (JS) across 512 Freedoom rays (`0` traps/fallbacks).
- `S3-wt-s3cng` (`8e79f078`): `tests/test_v7_differential_corpus.py` -> **12 passed, 0 failed**.
