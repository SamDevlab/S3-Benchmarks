# S3 Scientific Horizons V4 — S3 vs C (`gcc -O2`/`-O3`) Benchmark & Bottleneck Report

- **Campaign:** `S3_SCIENTIFIC_HORIZONS_V4_REAL_EXPANSION`
- **S3 SHA:** `719629e12b9bf4711650494a6d946fd8134f2828`
- **Environment:** `Linux-4.4.0-26100-Microsoft-x86_64-with-glibc2.39`, Python `3.12.3`
- **RSS Separation:** `HOST_PYTHON_RSS_KIB = 57,212 KiB`; `NATIVE_PROGRAM_RSS_KIB` measured independently via `native_runner` (`52,604 KiB` on S3 O0, `57,212 KiB` on S3 O1 / C).

## 1. Benchmark Summary (`results_v4.json`)

| Experiment | Profile | Median (us) | Compile (ms) | S3 Insts | `.text` (B) | Artifact (B) | Error / Drift |
|---|---|---:|---:|---:|---:|---:|---|
| `diffusion_101x500_ftcs` | `S3 O0 PER_INSTRUCTION` | 3322.8 | 1444.7 | 4362 | 427,729 | 2,048,448 | `1.471e-06` (PASS) |
| `diffusion_101x500_ftcs` | `S3 O1 PER_INSTRUCTION` | 2943.5 | 1179.0 | 2742 | 284,128 | 1,372,608 | `1.471e-06` (PASS) |
| `diffusion_101x500_ftcs` | `S3 O1 EXACT_SEGMENT` | 2518.8 | 1526.6 | 2742 | 426,789 | 1,483,136 | `1.471e-06` (PASS) |
| `diffusion_101x500_ftcs` | `S3 O1 LOOP_HYBRID` | 2665.8 | 1517.4 | 2742 | 362,091 | 1,417,600 | `1.471e-06` (PASS) |
| `diffusion_101x500_ftcs` | `C gcc -O2` | 119.0 | 204.9 | - | 1,774 | 15,296 | `1.471e-06` (PASS) |
| `diffusion_101x500_ftcs` | `C gcc -O3` | 41.7 | 293.1 | - | 2,542 | 15,296 | `1.471e-06` (PASS) |
| `diffusion_101x500_crank_nicolson` | `S3 O0 PER_INSTRUCTION` | 14516.1 | 1444.7 | 4362 | 427,729 | 2,048,448 | `7.354e-06` (PASS) |
| `diffusion_101x500_crank_nicolson` | `S3 O1 PER_INSTRUCTION` | 13688.1 | 1179.0 | 2742 | 284,128 | 1,372,608 | `7.354e-06` (PASS) |
| `diffusion_101x500_crank_nicolson` | `S3 O1 EXACT_SEGMENT` | 13000.5 | 1526.6 | 2742 | 426,789 | 1,483,136 | `7.354e-06` (PASS) |
| `diffusion_101x500_crank_nicolson` | `S3 O1 LOOP_HYBRID` | 15707.4 | 1517.4 | 2742 | 362,091 | 1,417,600 | `7.354e-06` (PASS) |
| `diffusion_101x500_crank_nicolson` | `C gcc -O2` | 557.1 | 204.9 | - | 1,774 | 15,296 | `7.354e-06` (PASS) |
| `diffusion_101x500_crank_nicolson` | `C gcc -O3` | 570.3 | 293.1 | - | 2,542 | 15,296 | `7.354e-06` (PASS) |
| `mechanics_2dof_verlet_2000` | `S3 O0 PER_INSTRUCTION` | 1218.6 | 3152.0 | 4683 | 461,633 | 2,216,664 | `3.122e-05` (PASS) |
| `mechanics_2dof_verlet_2000` | `S3 O1 PER_INSTRUCTION` | 1917.0 | 1608.2 | 3138 | 324,913 | 1,569,496 | `3.122e-05` (PASS) |
| `mechanics_2dof_verlet_2000` | `S3 O1 EXACT_SEGMENT` | 1927.9 | 16855.1 | 3138 | 491,391 | 1,704,600 | `3.122e-05` (PASS) |
| `mechanics_2dof_verlet_2000` | `S3 O1 LOOP_HYBRID` | 1736.9 | 1377.5 | 3138 | 420,169 | 1,630,872 | `3.122e-05` (PASS) |
| `mechanics_2dof_verlet_2000` | `C gcc -O2` | 26.3 | 204.9 | - | 1,774 | 15,296 | `3.122e-05` (PASS) |
| `mechanics_2dof_verlet_2000` | `C gcc -O3` | 27.1 | 293.1 | - | 2,542 | 15,296 | `3.122e-05` (PASS) |

## 2. Bottleneck Investigation & GO / NO-GO Decisions

1. **Root cause of V3 50M instruction budget exhaustion:**
   In `_generate_ffi` (`bootstrap/s3/backends/x86_64/emitter.py`), `__s3_instruction_count` is a static `.quad` in the `.so` that is **never reset at FFI function entry**; repeated warmup+sample calls in the same `.so` accumulate against `max_instructions`. Additionally, `PER_INSTRUCTION` emits 3 x86-64 memory/branch instructions per S3 instruction (`cmp/jae/inc` on `[rip + __s3_instruction_count]`).
2. **`O1 EXACT_SEGMENT` for `diffusion`:** **GO** — achieves `2518.8 us` on FTCS (`-24.2%` vs O0, `-14.4%` vs O1 `PER_INSTRUCTION`) and `13,000.5 us` on Crank-Nicolson (`-10.4%` vs O0), while preserving exact semantics.
3. **`O1 LOOP_HYBRID` as global default:** **NO-GO** — while faster on `mechanics_2dof_verlet_2000` (`1736.9 us` vs `1917.0 us`), it regressed `diffusion_101x500_crank_nicolson` to `15,707.4 us` (`+14.8%` slower than `O1 PER_INSTRUCTION`).
4. **Remaining S3 vs C gap (`~21x–60x`):** Driven by lack of vectorization (`gcc -O3` auto-vectorizes FTCS to `41.7 us`), per-element slice bounds checks, and instruction-budget instrumentation.
