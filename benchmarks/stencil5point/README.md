# Stencil 2D 5-Point Verified Compute Benchmark

Pinned comparative record for the **S3 Verified Compute** 2D 5-point integer stencil (`stencil5point.s3`) against the independent C `-O2` reference (`scientific_stencil_reference.c`), using the paired alternating harness (`scientific_benchmark.c`) and the native C host ABI (`libs3compute_host.so`) compiled directly from the installed `s3-bootstrap` wheel.

## Pinned revisions

- **S3 PR / commit:** [`SamDevlab/S3#434`](https://github.com/SamDevlab/S3/pull/434) (`54c08c0aba4758304aac0519e4bc38d8e7d7f154`, based on `main` `88f0e85c511e4519b366e11e2015513297c0fd51`)
- **Decision / issue:** [`SamDevlab/S3#418`](https://github.com/SamDevlab/S3/issues/418) (`DIAGNOSTIC_CANDIDATE` for performance optimization)

## Reproduction command (Linux x86-64)

1. Install the pinned S3 wheel into a clean venv and build `libs3compute_host.so` + `stencil5point` V3 package from `site-packages/bootstrap/s3`.
2. Compile `examples/compute/scientific_benchmark.c` + `examples/compute/scientific_stencil_reference.c` with `gcc -O2` linked against `libs3compute_host.so`.
3. Run paired alternating samples (`s3-first` / `c-first`) with `memcmp` parity on warmup and every sample:

```bash
./scientific_benchmark ./stencil5point 64 40 20 5 1
./scientific_benchmark ./stencil5point 128 80 20 5 1
./scientific_benchmark ./stencil5point 256 160 20 5 1
```

## Recorded paired results (`2026-11-19`, WSL Ubuntu 24.04, GCC 13.3.0 `-O2`, Python 3.12.3)

Raw JSON: [results/2026-11-19-wsl-pinned-54c08c0a.json](results/2026-11-19-wsl-pinned-54c08c0a.json)

| Grid | Generations | Warmups / Paired Samples | Parity (`memcmp`) | S3 Wall Median (ns) | S3 `kernel_ns` Median (ns) | C `-O2` Wall Median (ns) | S3 Wall / C | S3 `kernel_ns` / C |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| `64×40` | 20 | 1 / 5 | PASS | 1,222,800 | 1,202,100 | 84,700 | 14.44× | 14.19× |
| `128×80` | 20 | 1 / 5 | PASS | 4,816,900 | 4,740,800 | 343,200 | 14.04× | 13.81× |
| `256×160` | 20 | 1 / 5 | PASS | 19,099,800 | 18,942,800 | 1,394,100 | 13.70× | 13.59× |

## Methodological scope

- `kernel_ns` in `bootstrap/s3/compute_host_api.inc` covers both the S3 kernel call and per-generation output-value domain validation.
- Static disassembly of `s3_stencil_value` (111 instructions, including 20 `dec r15` + `js` pairs = 40 instructions) supports an investigation hypothesis, but the exact runtime fraction attributable to instruction-budget accounting remains unisolated; performance optimization remains `DIAGNOSTIC_CANDIDATE` in `S3#418`.
