# S3 Autonomous Development V3 — Benchmark Methodology

**Script:** [run_suite.py](file:///c:/Users/samue/Desktop/gemini/S3-Benchmarks/benchmarks/autonomous_v3/run_suite.py)  
**Outputs:** [results.json](file:///c:/Users/samue/Desktop/gemini/S3-Benchmarks/benchmarks/autonomous_v3/results.json), [results.csv](file:///c:/Users/samue/Desktop/gemini/S3-Benchmarks/benchmarks/autonomous_v3/results.csv)  
**Baseline S3 Commit Measured:** `b813bfb6198e346ccabac340bb75df359fa7aa14`  
**Environment Measured:** `Linux-4.4.0-26100-Microsoft-x86_64-with-glibc2.39`, Python `3.12.3`, CPU features `{sse2: true, sse4_1: true, sse4_2: true, avx: true, avx2: true, fma: true}`, `SCIENTIFIC_MAX_INSTRUCTIONS = 50_000_000`.

---

## 1. Strict 6-Category Separation

Every measurement in `results.json` / `results.csv` (`84` total records, `all_exact_match = true`) is classified into one of six non-overlapping categories so that Python wrapper latency, GCC-compiled C11 helpers, S3-compiled x86-64 native code, and intentional fallbacks are never conflated:

1. `S3_CONVENTIONAL_NATIVE`: S3 source compiled via `compile_source(..., predictive_exact=False)` (the default) into native x86-64 `.so` via `NativeToolchain` or `X8664Backend.scientific(max_instructions=50_000_000)`.
2. `S3_PREDICTIVE_NATIVE`: S3 source compiled with explicit opt-in `predictive_exact=True` lowering certified recurrences into pure S3 IR `O(log T)` / `O(1)` CFGs (plus the opt-in `AVX2+FMA` runtime dot kernel compiled via `compile_simd_lib(prefer_avx2=True)`).
3. `S3_PREDICTIVE_PYTHON_WRAPPER`: Pure Python orchestration APIs (`predictive_execute`, `predictive_execute_ir`, `run_gf2_ca`, `run_hashlife_v2_finite_grid`, `run_hashlife_v3_finite_grid`, `PredictiveComputeToolkit`) reflecting end-to-end Python discovery, verification, certificate binding, and dispatch costs.
4. `C11_CONVENTIONAL_GCC_O3`: Reference C11 iterative baselines compiled with `gcc -O3 -std=c11 -shared -fPIC` (`v3_bench_ref.c` and `GCC_CSR_JACOBI_C`) and C11 iterative CA baselines (`native_lib.run_conventional_ca`). Note that `gcc -O3` preserves strict IEEE-754 F64 ordering (no `-ffast-math`).
5. `C11_PREDICTIVE_GCC_O3`: GCC-compiled C11 predictive kernels invoked via `ctypes` (fast-forwarded C11 closed-form `lcg_mod`, C11 `GF(2)[x]/(x^W-1)` circulant fast-forward `s3_c11_gf2_circulant_fast_forward`, and persistent resident C11 Brent workspace `S3CAWorkspace`).
6. `NEGATIVE_CONTROL`: Controlled safety, cutoff, and rejection probes where acceleration MUST NOT occur or MUST abort cleanly back to conventional semantics (`lcg_mod_T10` runtime selector gate `USE_CONVENTIONAL`, `static_small_T10_gate`, `fib92` i64 overflow trap parity, Hashlife V3 chaotic R-pentomino abort + C11 handoff, `ir_reject_{fp_loop,nonlinear_quad}`, `gf2_reject_rule{30,110}`, and `default_predictive_exact_off_isolation`).

---

## 2. Cold vs Warm Measurement Protocol

- **Cold timing (`cold_ms`)**: Measured on the first invocation inside `_time_fn` (`time.perf_counter_ns()`) prior to additional warmups (`warmups=0` or first warmup call before the timed loop). For `S3_PREDICTIVE_PYTHON_WRAPPER` GF(2) cases, an uncached `GF2LinearCACache()` is measured separately (`notes="cold_no_cache_ms=..."`).
- **Warm median & IQR (`warm_median_ms`, `warm_iqr_ms`)**: Measured after warmup (`warmups=1` or repeated invocations) using `statistics.median` and `(Q3 - Q1)` interquartile range across `repeats` samples (`7` for fast native/ctypes kernels, `3` for Poisson CG-Jacobi, `1-2` for multi-hundred-millisecond C11/HL runs).
- **Compile cold cost (`compile_cold_ms`)**: Recorded separately for S3 compilation + lowering + proof checking + shared-library emission (`207.675 ms` for conventional 6-function IR module, `4910.605 ms` with predictive lowering + independent translation validation, and `6535.579 ms` for `s3_sci_numerics_v5` scientific Poisson/CG bundle).

---

## 3. Suites Covered (`5` Computational + `1` Negative Control)

1. **`ir_native_lcg_mod` & `ir_native_multi`**:
   - Sweeps `lcg_mod` over horizons `T in {10, 10^3, 10^5, 10^6, 10^9, 10^12}`, plus `fib_mod`, `coupled2`, and `stride_sum` at `T=10^5` (parity against S3 & GCC `-O3`) and `T=10^12` (verified against `verify_translation_certificate` and `lcg_mod` C11 closed form).
2. **`gf2_circulant_ca`**:
   - Sweeps periodic Rule 90 at `W in {64, 256}` across `T in {10^3, 10^5, 10^12}` comparing C11 conventional loop (`T <= 10^5`), Python `GF2LinearCACache`, and C11 `run_gf2_circulant_fast_forward`, plus parity verification for Rules `{60, 102, 150}` at `W=256, T=10^12`.
3. **`hashlife_v3_and_brent`**:
   - Compares chaotic Conway `R-pentomino` (`64x64, T=500`) across C11 conventional, `HL_V2`, and `HL_V3` chaotic abort (`V2/V3 = 4.47x`, honest `NEGATIVE_CONTROL` since pure C11 remains `2.26x` faster than V3 abort warm), structured `128x128` tiled gliders (`T=4096`), and `16x16` glider `T=10^6` Python V1 Brent vs resident C11 `S3CAWorkspace` Brent (`0` warm reallocations).
4. **`poisson2d_native_scaling`**:
   - Solves 2D Poisson CSR Jacobi-preconditioned Conjugate Gradient across `32x32` (`N=1024`), `48x48` (`N=2304`), `64x64` (`N=4096`), `80x80` (`N=6400`), and `96x96` (`N=9216`) inside the unmodified `SCIENTIFIC_MAX_INSTRUCTIONS = 50_000_000` budget using adaptive chunking (`50` iters for `<=64x64`, `25` iters for `80x80`/`96x96`), verifying identical iteration counts (`siters == giters`) and `max_err < 1e-10` (`0.0` observed) against `GCC -O3`.
5. **`simd_avx2_fma`**:
   - Compares `dot_f64` (`N=16384`) under `C11 GCC -O3` (strict IEEE-754), `S3_CONVENTIONAL_NATIVE` (`allow_fp_reassociation=False`, `max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS`), and opt-in `S3_PREDICTIVE_NATIVE` (`AVX2+FMA`).
6. **`negative_controls`**:
   - Verifies strict rejection, selector cutoff enforcement, default `predictive_exact=False` isolation, and runtime signed-integer overflow trap parity (`fib(92)`).

