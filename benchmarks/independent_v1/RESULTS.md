# S3 Independent Benchmarks V1.1 — Scientific Results Report

**Campaign**: `SAMDEV_UNIFIED_V3_1`  
**Workstream**: `FRENTE B — S3 BENCHMARKS`  
**Executor**: Google Antigravity (Gemini)  
**Branch**: `research/s3-independent-benchmarks-v1`  
**S3 SHA**: `7d625ee98364cad3d4034714e78783e7a7cdfd97` | **S3-Benchmarks SHA**: `51c4d7c34f30f3b7ec0484f6f6586b04f55e8ba6`  
**Date**: 2026-11-11  

---

## 1. Methodology & Mandatory Evidence Separation

In strict accordance with scientific rigor, every datum in this report is explicitly classified under the taxonomy below:
- `HISTORICAL_NATIVE`: Native compiled binaries executed and timed under the Linux x86-64 KVM 3-vCPU campaign (PR #33).
- `CURRENT_NATIVE`: Code executed natively by the host operating system (e.g. CPython 3.11 reference oracle).
- `CURRENT_IR_EMULATION`: S3 compiler bootstrap AST pipeline and Python IR instruction emulator. **No IR emulation measurement is ever presented as native compiled S3 performance.**
- `CORRECTNESS_ONLY`: Deterministic differential assertions, bit-exact checksums, and mathematical parity verifications.
- `STRUCTURAL_ONLY`: File byte counts, IR instruction counts, and assembly text section measurements.
- `INCONCLUSIVE`: Measurements with insufficient sample power, high variance, or unisolated noise.
- `NOT_MEASURED`: Native compiler toolchains absent from host environment (`TOOLCHAIN_UNAVAILABLE`).

---

## 2. Canonical Cross-Language Comparative Matrix (HISTORICAL_NATIVE Baseline)

*Workload: `agent_energy_residual` | Input size: `364` items | Baseline: GCC -O2 = 1.00x*
*Environment: Linux x86-64 KVM 3-vCPU isolation (PR #33) — Evidence Class: `HISTORICAL_NATIVE`*

| Language / Variant | Mode / Profile | Evidence Class | Median Time (ns) | ns / Item | Ratio vs GCC -O2 | Peak RSS (KiB) | Binary Size (bytes) | Text Section (bytes) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **C (GCC -O2)** | `gcc-o2` | `HISTORICAL_NATIVE` | 1,180 | 3.24 | **1.00x** | 21,688 | 15,696 | 1,962 |
| **C (Clang -O2)** | `clang-o2` | `HISTORICAL_NATIVE` | 1,130 | 3.10 | **0.96x** | 21,688 | 15,592 | 1,751 |
| **Rust (opt-level 2)** | `rust-optlevel2` | `HISTORICAL_NATIVE` | 1,090 | 2.99 | **0.92x** | 21,688 | 11,331,384 | 1,911 |
| **Zig (ReleaseFast)** | `zig-releasefast` | `HISTORICAL_NATIVE` | 870 | 2.39 | **0.74x** | 21,688 | 12,792 | 1,530 |
| **C (GCC -O0)** | `gcc-o0` | `HISTORICAL_NATIVE` | 3,840 | 10.55 | **3.25x** | 21,688 | 15,696 | 3,354 |
| **C (Clang -O0)** | `clang-o0` | `HISTORICAL_NATIVE` | 3,880 | 10.66 | **3.29x** | 21,688 | 15,592 | 3,195 |
| **Rust (opt-level 0)** | `rust-optlevel0` | `HISTORICAL_NATIVE` | 11,960 | 32.86 | **10.14x** | 21,688 | 11,765,072 | 257,386 |
| **Zig (Debug)** | `zig-debug` | `HISTORICAL_NATIVE` | 5,640 | 15.49 | **4.78x** | 21,688 | 2,564,432 | 694,826 |
| **S3 Pure Experimental (O1)** | `s3-pure_experimental-o1` | `HISTORICAL_NATIVE` | 39,040 | 107.25 | **33.08x** | 21,688 | 127,376 | 34,719 |
| **S3 Pure Experimental (O0)** | `s3-pure_experimental-o0` | `HISTORICAL_NATIVE` | 37,510 | 103.05 | **31.79x** | 21,688 | 127,376 | 34,723 |
| **S3 Controlled Per-Instruction (O1)** | `s3-per_instruction-o1` | `HISTORICAL_NATIVE` | 42,550 | 116.90 | **36.06x** | 21,688 | 209,424 | 46,619 |
| **S3 Controlled Per-Instruction (O0)** | `s3-per_instruction-o0` | `HISTORICAL_NATIVE` | 41,500 | 114.01 | **35.17x** | 21,688 | 209,424 | 46,675 |
| **S3 Controlled Exact-Segment (O1)** | `s3-exact_segment-o1` | `HISTORICAL_NATIVE` | 42,420 | 116.54 | **35.95x** | 21,688 | 225,680 | 68,715 |
| **S3 Controlled Loop-Hybrid (O1)** | `s3-loop_hybrid-o1` | `HISTORICAL_NATIVE` | 46,330 | 127.28 | **39.26x** | 21,688 | 217,480 | 57,653 |
| **Python (CPython 3.11)** | `python-cpython` | `HISTORICAL_NATIVE` | 82,139 | 225.66 | **69.61x** | 21,688 | 0 | 0 |

### Rigorous Findings from Historical Native Matrix
1. **Per-Instruction vs Pure Experimental on `agent_energy_residual`**: S3 Pure O1 achieves **39,040 ns**, while S3 Per-Instruction O1 achieves **42,550 ns**. The dynamic instruction-budget check adds **3,510 ns (+8.99%)** instrumentation overhead on this memory/reduction workload. It must **not** be conflated with the 3.21x penalty observed on pure instruction loop microbenchmarks.
2. **Status of `LOOP_HYBRID`**: In the historical matrix, `s3-loop_hybrid-o1` recorded **46,330 ns**, performing **slower** than `s3-per_instruction-o1` (42,550 ns). Therefore, recommending `LOOP_HYBRID` as a production default is unsupported by evidence.
3. **Code Footprint Overhead**: S3 Per-Instruction emits **209,424 bytes** (text section: 46,619 bytes), compared to **127,376 bytes** (text section: 34,719 bytes) for S3 Pure. Software budget instrumentation increases compiled `.text` code size by **+34.3% (+11.9 KB)** due to per-block decrement/jump trampolines.
4. **Native S3 vs C, Rust, Zig, Python**: S3 native execution is **2.10x faster than interpreted CPython 3.11** (39.0 µs vs 82.1 µs), but trails optimized native languages (GCC -O2: 1.18 µs, Clang -O2: 1.13 µs, Rust opt-level 2: 1.09 µs, Zig ReleaseFast: 0.87 µs) due to the absence of auto-vectorization (SIMD) and balanced-ternary conditional branch cascades.

---

## 3. Workload Verification & Live Host Measurements

### Workload A: JSMN (JSON Tokenizer & Balanced Ternary Parser)
- **Specification**: Balanced ternary tryte JSON state machine parser against `7` corpus fixtures.
- **Differential Correctness (`CORRECTNESS_ONLY`)**: `PASS (100% Token & Checksum Match)`.
- **Source Footprint (`STRUCTURAL_ONLY`)**: `24,125` bytes (`jsmn_demo.s3`).
- **Peak RSS**: `51,908` KiB.
- **Timing Note**: Python oracle runs under `CURRENT_NATIVE`; S3 timing reflects `CURRENT_IR_EMULATION` (instruction-by-instruction emulation in Python runtime, not native code).

| Fixture Name | Input Size (bytes) | Tokens Extracted | Python Oracle Median (ns) | S3 IR Emulation Median (ns) | Status / Checksum | Parity Gate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `tiny_obj` | 2 | 1 | 10,700 | 2,273,894,400 | `4` | `PASS` |
| `tiny_arr` | 2 | 1 | 7,500 | 2,634,920,600 | `5` | `PASS` |
| `tiny_pair` | 8 | 3 | 50,600 | 2,110,990,800 | `44` | `PASS` |
| `tiny_bool` | 12 | 3 | 10,300 | 2,254,890,900 | `54` | `PASS` |
| `gen_flat` | 27 | 5 | 16,400 | 2,503,900,800 | `176` | `PASS` |
| `gen_nested` | 26 | 5 | 22,900 | 2,330,310,000 | `165` | `PASS` |
| `gen_mixed` | 36 | 8 | 25,500 | 2,192,297,000 | `331` | `PASS` |

### Workload B: RMSD & Scientific Similarity Distance
- **Specification**: Vector scales 64, 256, 1024, 8192 computing Euclidean distance, RMSD, MAE, dot product, and cosine similarity.
- **Differential Correctness (`CORRECTNESS_ONLY`)**: `PASS`.
- **Negative Test (Perturbed Input Rejection)**: `PASS (Returned -1 as required)`.
- **Aggregate Expected Checksum**: `29356` | **S3 Emulated Checksum**: `29356`.
- **S3 IR Footprint (`STRUCTURAL_ONLY`)**: `1,348,604` bytes (1765 IR instructions, 1765 assembly instructions).
- **Peak RSS**: `52,512` KiB.

#### Multi-Scale Numerical Decomposition (`CORRECTNESS_ONLY`)

| Scale (N) | Squared Distance | Euclidean Distance | RMSD (0.49..0.51) | MAE (0.49..0.51) | Dot Product | Cosine (0.84..0.85) | Status Code | Parity Gate |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **64** | 16.0 | 4.0 | 0.5 | 0.5 | 40.0 | 0.8452 | `379` | `PASS` |
| **256** | 64.0 | 8.0 | 0.5 | 0.5 | 160.0 | 0.8452 | `955` | `PASS` |
| **1024** | 256.0 | 16.0 | 0.5 | 0.5 | 640.0 | 0.8452 | `3259` | `PASS` |
| **8192** | 2048.0 | 45.2548 | 0.5 | 0.5 | 5120.0 | 0.8452 | `24763` | `PASS` |

### Workload C: Geospatial Raster Window Statistics
- **Specification**: 8x8 raster grid (64 cells) with nodata mask, threshold filter (25.0), and valid horizontal-neighbor difference.
- **Scope Clarification**: This workload computes raster window statistics and valid-neighbor horizontal absolute differences; it is **NOT** the PDE 2D stencil solver from S3 Compute.
- **Differential Correctness (`CORRECTNESS_ONLY`)**: `PASS`.
- **Calculated Metrics Vector `[total, mean, min, max, threshold_count, gradient_mean]`**:
  `[3960.0, 68.2759, 24.0, 114.0, 55.0, 30.3043]`
- **S3 IR Footprint (`STRUCTURAL_ONLY`)**: `492,545` bytes (675 IR instructions, 675 assembly instructions).
- **Peak RSS**: `52,512` KiB.

---

## 4. Evidence Traceability & Artifact Index

- `benchmarks/independent_v1/results.json`: Canonical machine-readable metrics with full evidence classification tags.
- `benchmarks/independent_v1/BOTTLENECKS.md`: Corrected architectural bottleneck diagnosis with confidence grading.
- `benchmarks/independent_v1/test_benchmark_consistency.py`: Targeted unit tests verifying report consistency and taxonomy integrity.
- Historical PR #33 Baseline: `benchmarks/native-pure-controlled-v1/results/summary.json` (Commit `0430619`).