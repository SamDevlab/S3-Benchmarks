# S3 V4 Compiler Maturity & Scientific Benchmark Methodology

## 1. Execution Scope and Separation Guarantees

The V4 suite ([`run_v4_suite.py`](./run_v4_suite.py)) enforces strict isolation across **six non-overlapping execution categories** (`72` measured records across `7` sub-suites in [`results_v4.csv`](./results_v4.csv) and [`results_v4.json`](./results_v4.json)):

1. `S3_CONVENTIONAL_NATIVE`: S3 programs compiled with `predictive_exact=False` and `allow_fp_reassociation=False` to native x86-64 shared libraries (`X8664Backend.scientific(max_instructions=50_000_000, instruction_budget_mode="loop_hybrid")`), preserving exact conventional semantics and IEEE-754 floating-point evaluation order.
2. `S3_PREDICTIVE_NATIVE`: Opt-in S3 native predictive lowering (`predictive_exact=True`), opt-in AVX2/FMA reductions (`allow_fp_reassociation=True`), or the genuine S3-compiled GF(2)[x]/(x^W-1) native circulant shared library (`S3CompiledGF2Library`). Never enabled silently by default.
3. `S3_PREDICTIVE_PYTHON_WRAPPER`: Python-level predictive runtime wrappers (`predictive_execute`, Hashlife V3/V4 sparse glider acceleration, `predictive_scev`, `explain_compilation`), explicitly separated from native compiled S3 binaries so Python wrapper overhead is never conflated with native codegen.
4. `C11_CONVENTIONAL_GCC_O3`: Reference C11 iterative baselines and CSR Conjugate Gradient Jacobi (`gcc -O3 -std=c11 -shared -fPIC`) invoked directly via `ctypes`.
5. `C11_PREDICTIVE_GCC_O3`: Reference C11 predictive kernels (`s3_c11_gf2_circulant_fast_forward`), isolated from conventional GCC baselines and from S3-compiled GF(2) kernels.
6. `NEGATIVE_CONTROL`: Adversarial, cutoff, overflow, tamper-detection, and unsupported-domain checks verifying safe fallback/rejection (`runtime_small_t_bypass` at `T=10`, static `small_t_cutoff=100` skip, `fib(92)` signed `i64` trap preservation, SHA-256 certificate tamper rejection, GF(2) nonlinear Rule 30 / Rule 110 counterexample rejection, Hashlife V4 dense-chaotic prefilter handoff with `0` nodes created, and SCEV rejection of impure calls and exponential recurrences).

## 2. Safety & Compiler Policy Invariants

All runs verify and record the following campaign defaults inside `results_v4.json["environment"]`:

- `default_predictive_exact: false` — verified directly by compiling `_IR_V4_SRC` with default `CompilationCache().compile(..., OptimizationLevel.O1)` and asserting zero lowered functions.
- `default_fp_reassociation: false` — strict IEEE-754 `0.0` ULP error verified on `vec_scale_add` (`F64X4` AVX2) and `dot_product`, and exact iteration count + `0.0` solution delta against `gcc -O3` on 2D Poisson CSR (`32x32` through `128x128`).
- `scientific_max_instructions: 50_000_000` — enforced on native scientific FFI artifacts via `X8664Backend.scientific()` under `LOOP_HYBRID` budget checking.

## 3. Timing, Caching & Amortization Protocol

- **Cold vs. Warm Execution:** `_time_fn` captures the un-warmed first invocation (`cold_ms`) separately from post-warmup repeated calls (reporting `warm_median_ms` and interquartile range `warm_iqr_ms` across `2` to `21` repeats depending on runtime cost).
- **Compilation & Verification Caching (`compile_cache` suite):** Measures cold `O1` conventional compile, cold `O1` `predictive_exact=True` compile (lowering + independent translation-certificate verification + IR optimization + codegen), warm in-memory `CompilationCache.compile` hit latency, cold disk-backed `PredictiveVerificationCache` + `PredictiveLoweringCache` latency, warm in-memory lowering hit latency, and fresh-instance disk cache reload latency.
- **Amortization Break-Even:** For `lcg_mod` (`T=1,000` and `T=1,000,000`), break-even call count is computed honestly as `ceil((pred_cold_compile_ms - conv_compile_ms) / (conv_warm_median_ms - pred_warm_median_ms))`, preventing O(log T) runtime speedups from masking one-time compile/proof cost at small batch sizes.
- **Extrapolation Discipline:** Every S3 conventional 1D CA timing (`gf2_s3_conv_est_W*_T1M`) measures `10,000` native steps directly and scales by `100x` solely for comparison against `T=1,000,000`; `T=10^9` and `T=10^12` predictive executions are verified directly against independent O(log T) Python/C11 mathematical oracles.
- **Exact Parity Gate:** `main()` asserts `report["summary"]["all_exact_match"] == True` across all `72` records before exiting `0`.

