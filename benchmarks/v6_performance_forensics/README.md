# S3 V6 Performance Forensics Suite (`benchmarks/v6_performance_forensics/`)

## 1. Objective (P0 V4 vs V5 Audit)
This suite isolates and quantifies the cause of the apparent discrepancy between:
- **V4 Published Poisson 2D CSR (`S3-Benchmarks/benchmarks/v4_compiler_maturity/run_v4_suite.py`):** `32x32 = 1.5755 ms` (`1.90x` vs GCC), `48x48 = 5.2328 ms` (`1.90x` vs GCC) at `tol = 1e-10` (`109` and `162` iterations).
- **V5 Published Poisson 2D CSR (`S3-Benchmarks/benchmarks/v5_ecosystem_forge/run_v5_suite.py` -> `tools/numerics_v4_9_study.py`):** `32x32 = 21.6893 ms` (`21.73x` vs GCC), `48x48 = 68.7480 ms` (`22.73x` vs GCC) at `tol = 1e-12` (`118` and `176` iterations).

## 2. Official Classification
- **Primary Decision:** `METHODOLOGY_ARTIFACT_CONFIRMED`
- **Secondary Decision:** `NO_REPRODUCIBLE_REGRESSION` (the V5 compiler is **1.31x to 1.66x faster** than the V4 compiler across all grids `16x16..128x128` under normalized `KERNEL_ONLY` measurement).

## 3. Root Causes Quantified
1. **Timer Scope Asymmetry (`END_TO_END_S3` vs `KERNEL_ONLY_GCC`):**
   - `tools/numerics_v4_9_study.py` timed `gcc_fn(...)` strictly around the C solver call (`KERNEL_ONLY`) after pre-building the CSR matrix and `ctypes` arrays.
   - For S3, it read `s3_res["exec_s"]` from `tools/s3_science.py::_run_s3_kernel("poisson2d", ...)`, which started `time.perf_counter()` **before**:
     - Pure-Python nested-loop CSR matrix construction (`CSR_CONSTRUCTION_MS`: `1.3427 ms` on `48x48`),
     - Pure-Python RHS `b_l` generation (`INPUT_GENERATION_MS`: `2.9634 ms` on `48x48`),
     - `ctypes` array allocation and copying (`CTYPES_BUFFER_ALLOCATION_MS`: `4.6155 ms` on `48x48`),
     - Pure-Python post-solve `rows` dictionary list comprehension (`OUTPUT_MATERIALIZATION_MS`: `0.9949 ms` on `48x48`),
     - Pure-Python error reduction (`RESULT_VALIDATION_MS`: `0.5452 ms` on `48x48`).
   - Total non-kernel Python overhead inside `_run_s3_kernel` on `48x48`: **`10.4617 ms`** (`2.54x` larger than the `4.1167 ms` native S3 kernel execution itself).
2. **Cold Single-Sample DrvFS Execution vs Warm Multi-Sample Median:**
   - `benchmark_poisson2d_large_chunked` executed a single cold call (`0` warmups, `1` sample) immediately after loading the `.so` from `/mnt/c/.../science_cache/`, whereas `run_v4_suite.py` used `/tmp` (native Linux tmpfs) with warmups and multi-sample medians.
3. **Tolerance & Iteration Difference:**
   - V4 used `tol = 1e-10` (`tol2 = 1e-20`, `109` iters on `32x32`, `162` iters on `48x48`).
   - V5 used `tol = 1e-12` (`tol2 = 1e-24`, `118` iters on `32x32`, `176` iters on `48x48`, `+8.3%` to `+8.6%` more iterations).

## 4. 4-Cell A/B Matrix Summary (`results_forensics.json`)
| Grid | Cell | Compiler SHA | Harness | Tol | Iters | S3 Median (ms) | GCC Kernel (ms) | S3/GCC Ratio | Max Err vs GCC |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| `32x32` | `V4_COMPILER + V4_HARNESS` | `f33b5b3b` | `V4_HARNESS` | `1e-10` | 109 | `2.0640` | `0.9332` | `2.21x` | `0.0` |
| `32x32` | `V5_COMPILER + V4_HARNESS` | `9c1bec32` | `V4_HARNESS` | `1e-10` | 109 | **`1.0951`** | `0.9332` | **`1.17x`** | `0.0` |
| `32x32` | `V4_COMPILER + V5_HARNESS` | `f33b5b3b` | `V5_HARNESS` | `1e-12` | 118 | `6.0589` | `0.9019` | `6.72x` | `0.0` |
| `32x32` | `V5_COMPILER + V5_HARNESS` | `9c1bec32` | `V5_HARNESS` | `1e-12` | 118 | `6.2306` | `0.9019` | `6.91x` | `0.0` |
| `48x48` | `V4_COMPILER + V4_HARNESS` | `f33b5b3b` | `V4_HARNESS` | `1e-10` | 162 | `5.7626` | `2.8705` | `2.01x` | `0.0` |
| `48x48` | `V5_COMPILER + V4_HARNESS` | `9c1bec32` | `V4_HARNESS` | `1e-10` | 162 | **`3.6470`** | `2.8705` | **`1.27x`** | `0.0` |
| `48x48` | `V4_COMPILER + V5_HARNESS` | `f33b5b3b` | `V5_HARNESS` | `1e-12` | 176 | `16.3046` | `3.1046` | `5.25x` | `0.0` |
| `48x48` | `V5_COMPILER + V5_HARNESS` | `9c1bec32` | `V5_HARNESS` | `1e-12` | 176 | `14.5265` | `3.1046` | `4.68x` | `0.0` |

## 5. Reproduction
```bash
wsl bash -c "python3 /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks/benchmarks/v6_performance_forensics/run_v6_forensics.py"
pytest S3-Benchmarks/tests/test_v6_performance_forensics.py -v
```
