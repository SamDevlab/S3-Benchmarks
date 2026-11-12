# S3 Independent Benchmarks V1 — Scientific Results Report

**Campaign**: `SAMDEV_UNIFIED_V3`  
**Workstream**: `FRENTE B — S3 BENCHMARKS`  
**Executor**: Google Antigravity (Gemini)  
**Branch**: `research/s3-independent-benchmarks-v1`  
**Date**: 2026-11-11  

---

## 1. Executive Summary & Methodology

This report provides an independent, scientifically controlled benchmark evaluation of the S3 compiler system against:
1. **Reference languages**: C (GCC 12, Clang 16), Rust (rustc 1.75), Zig (0.11), and Python (CPython 3.11).
2. **Historical S3 compilation modes**: Controlled execution (`PER_INSTRUCTION`, `EXACT_SEGMENT`, `LOOP_HYBRID`) versus uninstrumented `PURE_EXPERIMENTAL` at optimization levels `O0` and `O1`.
3. **Three core computational workloads**:
   - **Workload A: JSMN** (Balanced ternary tryte JSON parser, token boundary extraction, checksum verification).
   - **Workload B: RMSD** (Scientific vector distance, Euclidean norm, Root-Mean-Square Deviation, dot product, cosine similarity over 64..8192 items).
   - **Workload C: STENCIL 2D** (Geospatial raster window statistics, valid mask reduction, horizontal neighbor gradients).

### Environmental Isolation Contract
- **Live Host Evaluation (Windows AMD64, Python 3.11.9)**: Executes S3 bootstrap compiler pipeline, IR serialization, instruction emulation, and Python reference oracles. Measures high-resolution wall time (`perf_counter_ns`), CPU process time (`process_time_ns`), and OS process working set (`K32GetProcessMemoryInfo`). Native toolchains are verified absent locally (`NOT_AVAILABLE_ON_HOST`) and are not synthetic or fabricated.
- **Canonical Cross-Language Matrix (Linux x86-64 KVM, PR #33)**: Reconciled directly from 4,590 KVM-controlled samples in `SamDevlab/S3-Benchmarks` PR #33 (`codex/s3-native-pure-controlled-benchmark-v1`). Provides absolute hardware baseline for compiled native code.

---

## 2. Cross-Language Comparative Matrix (Canonical Native Baseline)

*Workload: `agent_energy_residual` | Input size: `364` items | Baseline: GCC -O2 = 1.00x*

| Language / Variant | Mode / Profile | Median Time (ns) | ns / Item | Overhead vs GCC -O2 | Peak RSS (KiB) | Binary Size (bytes) | Text Section (bytes) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **C (GCC -O2)** | `gcc-o2` | 1,180 | 3.24 | **1.00x** | 21,688 | 15,696 | 1,962 |
| **C (Clang -O2)** | `clang-o2` | 1,130 | 3.10 | **0.96x** | 21,688 | 15,592 | 1,751 |
| **Rust (opt-level 2)** | `rust-optlevel2` | 1,090 | 2.99 | **0.92x** | 21,688 | 11,331,384 | 1,911 |
| **Zig (ReleaseFast)** | `zig-releasefast` | 870 | 2.39 | **0.74x** | 21,688 | 12,792 | 1,530 |
| **C (GCC -O0)** | `gcc-o0` | 3,840 | 10.55 | **3.25x** | 21,688 | 15,696 | 3,354 |
| **C (Clang -O0)** | `clang-o0` | 3,880 | 10.66 | **3.29x** | 21,688 | 15,592 | 3,195 |
| **Rust (opt-level 0)** | `rust-optlevel0` | 11,960 | 32.86 | **10.14x** | 21,688 | 11,765,072 | 257,386 |
| **Zig (Debug)** | `zig-debug` | 5,640 | 15.49 | **4.78x** | 21,688 | 2,564,432 | 694,826 |
| **S3 Pure Experimental (O1)** | `s3-pure_experimental-o1` | 39,040 | 107.25 | **33.08x** | 21,688 | 127,376 | 34,719 |
| **S3 Pure Experimental (O0)** | `s3-pure_experimental-o0` | 37,510 | 103.05 | **31.79x** | 21,688 | 127,376 | 34,723 |
| **S3 Controlled Per-Instruction (O1)** | `s3-per_instruction-o1` | 42,550 | 116.90 | **36.06x** | 21,688 | 209,424 | 46,619 |
| **S3 Controlled Per-Instruction (O0)** | `s3-per_instruction-o0` | 41,500 | 114.01 | **35.17x** | 21,688 | 209,424 | 46,675 |
| **S3 Controlled Exact-Segment (O1)** | `s3-exact_segment-o1` | 42,420 | 116.54 | **35.95x** | 21,688 | 225,680 | 68,715 |
| **S3 Controlled Loop-Hybrid (O1)** | `s3-loop_hybrid-o1` | 46,330 | 127.28 | **39.26x** | 21,688 | 217,480 | 57,653 |
| **Python (CPython 3.11)** | `python-cpython` | 82,139 | 225.66 | **69.61x** | 21,688 | 0 | 0 |

### Key Observations from Cross-Language Matrix
1. **Pure Experimental vs Controlled**: On `agent_energy_residual` (364 items), S3 Pure O1 achieves **39,040 ns** (107.25 ns/item), while S3 Per-Instruction O1 requires **42,550 ns** (116.90 ns/item). The dynamic instruction-budget check adds **3,510 ns (+9.0%)** instrumentation overhead on this workload, scaling up to **3.21x** on instruction-dense loop microbenchmarks.
2. **Binary Footprint Overhead**: S3 Per-Instruction emits **209,424 bytes** (text section: 46,619 bytes), compared to **127,376 bytes** (text section: 34,719 bytes) for S3 Pure. Software budget instrumentation increases compiled `.text` code size by **+34.3% (+11.9 KB)** due to per-block decrement/jump trampolines.
3. **Native S3 vs C, Rust, Zig, Python**: S3 native execution is **2.10x faster than interpreted CPython 3.11** (39.0 µs vs 82.1 µs), but trails optimized native languages (GCC -O2: 1.18 µs, Clang -O2: 1.13 µs, Rust opt-level 2: 1.09 µs, Zig ReleaseFast: 0.87 µs) due to the absence of auto-vectorization (SIMD) and balanced-ternary conditional branch cascades.

---

## 3. Workload Verification & Live Host Measurements

### Workload A: JSMN (JSON Tokenizer & Balanced Ternary Parser)
- **Specification**: Balanced ternary tryte JSON parser against `7` corpus fixtures.
- **Differential Correctness**: `PASS (100% Token & Checksum Match)`.
- **Source Footprint**: `24,125` bytes (`jsmn_demo.s3`).
- **Peak RSS**: `50,752` KiB.

| Fixture Name | Input Size (bytes) | Tokens Extracted | Python Median (ns) | S3 Pipeline Median (ns) | Status / Checksum | Parity Gate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `tiny_obj` | 2 | 1 | 9,100 | 1,670,079,400 | `4` | `PASS` |
| `tiny_arr` | 2 | 1 | 7,600 | 1,704,583,800 | `5` | `PASS` |
| `tiny_pair` | 8 | 3 | 13,700 | 1,816,192,500 | `44` | `PASS` |
| `tiny_bool` | 12 | 3 | 11,900 | 1,968,259,300 | `54` | `PASS` |
| `gen_flat` | 27 | 5 | 15,600 | 1,931,009,500 | `176` | `PASS` |
| `gen_nested` | 26 | 5 | 16,300 | 1,820,020,000 | `165` | `PASS` |
| `gen_mixed` | 36 | 8 | 23,700 | 2,007,003,700 | `331` | `PASS` |

### Workload B: RMSD & Scientific Similarity Distance
- **Specification**: Vector sizes 64, 256, 1024, 8192 items computing Euclidean distance, RMSD, MAE, dot product, and cosine similarity.
- **Differential Correctness**: `PASS`.
- **Expected Mathematical Checksum**: `29356`.
- **S3 Result Checksum**: `29356`.
- **S3 IR Footprint**: `1,348,604` bytes (1765 IR instructions, 1765 assembly instructions).
- **S3 Compilation Duration**: `457.78` ms.
- **Peak RSS**: `50,752` KiB.

### Workload C: STENCIL 2D (Raster Window Statistics)
- **Specification**: 8x8 raster grid (64 cells) with nodata mask, threshold filter (25.0), and horizontal valid-neighbor gradient.
- **Differential Correctness**: `PASS`.
- **Calculated Metrics Vector `[total, mean, min, max, threshold_count, gradient_mean]`**:
  `[3960.0, 68.2759, 24.0, 114.0, 55.0, 30.3043]`
- **S3 IR Footprint**: `492,545` bytes (675 IR instructions, 675 assembly instructions).
- **Peak RSS**: `50,752` KiB.

---

## 4. Methodological Compliance & Evidence Index

- `benchmarks/independent_v1/results.json`: Canonical machine-readable metrics and raw samples.
- `benchmarks/independent_v1/BOTTLENECKS.md`: Full architectural diagnosis of top 5 S3 performance bottlenecks.
- PR #33 Canonical Evidence: `benchmarks/native-pure-controlled-v1/results/summary.json` (SHA-256 verified).