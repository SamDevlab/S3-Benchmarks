# V14 — S3 native CPU, S3 Vulkan GPU, and generic x86 backend audit

**Experimental, NOT a production CPU/GPU routing endorsement.**

## Layout

`conway_s3_cpu.s3` is real S3 code for the full interior grid
update, exported to native x86-64 Linux FFI. The S3 GPU source is
`S3/examples/gpu_v3/conway_gpu.s3`, lowered to WGSL and run
on physical RX580 Windows/Vulkan.

`fixtures/*.bin` are deterministic random i32 binary Conway input
grids captured from the physical GPU run; corresponding
`*_gpu_output_sha256.txt` values were verified against both the
GPU result and independent NumPy Conway reference. All fixture data
are synthetic, with no user information.

`run_s3_native_cpu_v14.py` compiles the native S3 CPU engine with
the S3 compiler (GCC assembles/links its ELF assembly; no C Conway math).
`run_s3_physical_gpu_v14.py` runs the physical S3 GPU kernel and
writes matched-input/output artifacts. `run_general_native_v14.py`
and `general_native_v14.c` A/B-test 3 native S3 integer kernels
on the actual Linux x86-64 backend, with a C harness oracle.

## Reproduction (same physical host, DIFFERENT operating systems)

From S3-Benchmarks repository, which has sibling S3 worktree:

```powershell
# Windows 3.12 + numpy + wgpu, physical Vulkan RX580
$env:PYTHONPATH="..\S3"
python benchmarks/v14_core/run_s3_physical_gpu_v14.py
```

```sh
# Linux x86-64 or WSL, Python 3.12+, GCC
python3 benchmarks/v14_core/run_s3_native_cpu_v14.py
python3 benchmarks/v14_core/run_s3_native_cpu_v14.py --peephole
python3 benchmarks/v14_core/run_s3_native_cpu_v14.py --budget-mode exact-segment
python3 benchmarks/v14_core/run_s3_native_cpu_v14.py --budget-mode exact-segment --peephole
python3 benchmarks/v14_core/run_general_native_v14.py s1
python3 benchmarks/v14_core/run_general_native_v14.py s2
python3 benchmarks/v14_core/run_general_native_v14.py s3
python3 -m pytest -q benchmarks/v14_core/test_v14_artifacts.py
```

**Results from one physical machine**: 64x64/50 generations
CPU S3 7.734ms, GPU S3 8.174ms; 128x128/10 CPU S3 11.533ms,
GPU S3 5.279ms; 128x128/50 CPU S3 23.805ms,
GPU S3 7.060ms.

All three matched initial binary grids, fully verified every
output cell using an independent reference, and shared exact
final SHA-256 digests. Two warmups and seven benchmark rounds,
not multi-machine replication. CPU is ELF under WSL using i64,
GPU is Windows/Vulkan using explicitly narrowed i32 on binary
values; CPU makes one native FFI call per generation. Results
are NOT suitable for production selection or a blanket hardware
performance claim.

The general x86 peephole removes a few locally redundant
instructions and remains opt-in. Across three A/B sessions, some
native S3 integer loops improve while bit-counting regresses.
There is **NO universal win** and no default-codegen promotion.

Cold compilation is recorded separately where available.
No dynamic PMU counters were available. All benchmarks store
machine-readable JSON and are subject to the test validator.
