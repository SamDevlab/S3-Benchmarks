# S3 V13 — Native Assembly & Physical GPU Placement

This is a **single-machine experimental study**. All generated S3
native programs compile from source/IR-certified S3 to x86-64 assembly.
The GCC C harness is independent; GCC only links the S3 assembly.

## Reproduce native x86 on Linux or WSL

Use sibling worktrees `V13-Native-GPU-Lab/S3` and
`V13-Native-GPU-Lab/S3-Benchmarks`.

```sh
python3 benchmarks/v13_native_gpu/native_ctz_v13.py --quick
python3 benchmarks/v13_native_gpu/native_ctz_v13.py
python3 benchmarks/v13_native_gpu/inline_ab_v13.py
python3 -m pytest -q benchmarks/v13_native_gpu/test_v13_artifacts.py
```

Requires Python, pytest, GCC and objdump. Native measurements have
9 rotating rounds, 64 independent C parity checks per case and four
horizons, including odd-width five-tap cases. Generated assembly
static counts are not PMU retired instruction measurements.

## Reproduce physical Windows Vulkan

Install Python 3.12, NumPy, wgpu, pytest and Zig on Windows in an
isolated environment. Require a supported physical Vulkan GPU. From
this repository, with adjacent S3 source:

```powershell
$env:PYTHONPATH="..\S3"
python benchmarks/v13_native_gpu/gpu_vs_native_c_v13.py s1
python benchmarks/v13_native_gpu/gpu_vs_native_c_v13.py s2
python benchmarks/v13_native_gpu/gpu_vs_native_c_v13.py s3
python benchmarks/v13_native_gpu/qualify_placement_v13.py
```

Each invocation compares **actual S3 WGSL kernels on physical AMD RX580**
against both an independent native Windows C DLL compiled with Zig
`cc -O3` and NumPy. The C function allocates ping-pong buffers,
copies input/output and performs its own loops. S3 GPU total includes
upload, resident dispatches, and final readback. Shader lowering and
native cold build are separate. WGPU uses explicit i64->i32 narrowing
only for bounded binary Conway cells.

The initial cold Zig build ran past a 150s child-process timeout but
produced a loadable native DLL. That output was verified through all
cell-parity tests and then reused. Cold C build duration is **unknown**
(`null`), not a success measurement. The DLL is intentionally excluded
from Git: compile locally when needed.

Recorded data contain 3 distinct process sessions on the **same host**,
each with seven timed rounds per shape. This is not independent
machine replication or production dispatch qualification.

## Observed decision

At 64x64/50 and 128x128/10,50, the GPU sometimes beats NumPy but
does **not** beat native C. The guarded S3 cost planner consumes the
real session records and returns `CPU/NO_CONSERVATIVE_GPU_GAIN`
for every task. No production GPU router or S3 defaults are changed.

**GO_EXPERIMENTAL:** V13 optional CTZ and inline rotations, hardware
comparison and fail-closed planner integration.

**NO-GO:** new mathematical algorithm, global compiler pass,
machine-code formal proof, blanket GPU acceleration claims or
merges/deployment from these exploratory results alone.
