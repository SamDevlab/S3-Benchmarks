# S3 Scientific Expansion V2 — Current Native Linux x86-64 Benchmark Report

- **Campaign**: `S3_SCIENTIFIC_EXPANSION_V2`
- **S3 Compiler SHA**: `9f83a44dfdc75a039ca1f026423646c6c6800668` (includes P0 fix `fix/s3-native-ra-codegen-v1`)
- **S3-Benchmarks SHA**: `efbf71a99b34fbc6bb096879c1bf98041c927871`
- **Platform**: `Linux-4.4.0-26100-Microsoft-x86_64-with-glibc2.39` (`AMD Ryzen 5 3400G with Radeon Vega Graphics`)
- **Toolchains**: GCC `gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`, Python `3.12.3`
- **Unavailable Toolchains**: Clang=`NOT_MEASURED`, Rust=`NOT_MEASURED`, Zig=`NOT_MEASURED`
- **Sampling Protocol**: `warmups=3`, `samples=9` (all times in nanoseconds; `CURRENT_NATIVE` execution)

---

## 1. JSMN JSON Tokenization & Checksum (`CURRENT_NATIVE`)

| Corpus | Bytes | Tokens | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | S3 O1 EXACT MB/s |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `small` | 53 | 11 | 6,000 | 5,800 | 5,800 | 5,300 | 2,100 | 5,600 | **8.71** |
| `medium` | 324 | 61 | 25,300 | 22,500 | 23,000 | 19,800 | 2,500 | 32,300 | **13.43** |
| `large` | 1513 | 295 | 109,400 | 102,600 | 104,400 | 93,800 | 4,600 | 192,200 | **13.82** |

## 2. RMSD & Vector Similarity (`CURRENT_NATIVE`)

| Scale (N) | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | Max Abs Error |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **64** | 6,000 | 5,700 | 5,800 | 5,700 | 2,700 | 7,400 | `0.00e+00` |
| **256** | 14,800 | 15,700 | 15,300 | 14,700 | 2,600 | 26,700 | `0.00e+00` |
| **1024** | 53,600 | 53,900 | 54,100 | 52,200 | 3,200 | 113,000 | `0.00e+00` |
| **8192** | 424,800 | 400,700 | 412,000 | 402,100 | 9,000 | 938,800 | `0.00e+00` |

- **Standalone `similarity_distance.s3` ELF Binary (`CURRENT_NATIVE`)**: Median `4,960,600 ns` (`4.96 ms`), `.text` = `178,026 bytes`, ELF = `806,384 bytes`, checksum = `29356` (`PASS`).

## 3. Real Stencil 2D (`stencil5point_split_inline.s3`, 10 Generations, `CURRENT_NATIVE`)

| Grid | Cells | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | EXACT vs PER Speedup |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **64x40** | 2,560 | 1,434,500 | 1,409,700 | 1,225,900 | 1,384,500 | 53,900 | 9,810,900 | **1.15x** |
| **128x80** | 10,240 | 5,860,700 | 5,683,600 | 4,798,100 | 5,911,400 | 181,400 | 38,868,700 | **1.18x** |
| **256x160** | 40,960 | 23,270,700 | 23,334,500 | 19,312,200 | 23,823,800 | 664,200 | 178,338,300 | **1.21x** |

## 4. Complementary Control Kernels (`CURRENT_NATIVE`)

| Kernel | S3 O0 (ns) | S3 O1 PER_INST (ns) | S3 O1 EXACT_SEG (ns) | S3 O1 PURE_EXP (ns) | GCC -O2 (ns) | Python 3.12 (ns) | Checksum |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `GEMM_I64_32x32` | 1,302,500 | 1,018,800 | 1,076,600 | 986,300 | 22,300 | 3,951,700 | `-28` |
| `RULE110_CA_256x128` | 2,109,900 | 2,082,800 | 2,100,800 | 2,218,100 | 52,000 | 4,046,800 | `17522` |
| `FNV1A_HASH_4096x10` | 2,012,500 | 1,926,700 | 1,375,800 | 1,383,200 | 293,000 | 7,043,200 | `980717197` |
