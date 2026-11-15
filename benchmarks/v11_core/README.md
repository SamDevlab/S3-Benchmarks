# S3 V11 — Core Algorithm Selection + Real GPU

**Experimental; no production defaults changed.**

## Real delivered experiments

- \`run_auto_native_v11.py\`: generates **two genuine S3 x86-64
  kernels from the same original S3 source and structural IR
  certificate**. An exact detector recognizes whether each bit-basis
  output column is a cyclic rotation of column zero. When true,
  \`algorithm="auto"\` selects proven GF(2) cyclic-polynomial
  powering; \`algorithm="generic"\` preserves the V10.3 matrix code.
- \`compare_s3_native_auto.c\`: independent GCC harness comparing
  the two real S3 native symbols against a known cyclic polynomial
  reference, with 64 differential states for each N and nine
  alternating timing rounds.
- \`gpu_physical_v11.py\`: actual Windows physical RX580/Vulkan
  S3->WGSL AXPY test, safe GPU buffers, f32 correctness and
  end-to-end GPU vs NumPy transfer-bound timing.
- \`gpu_resident_conway_v11.py\`: 50 Conway generations computed
  by S3->WGSL on the same physical GPU with resident ping-pong
  buffers; independent 7-round NumPy reference and full-cell parity.
- \`test_v11_core_results.py\`: validates outputs/provenance and
  prevents accidentally classifying opt-in experiments as
  universal production features.

## Reproduce

WSL/Linux native compilation and C harness:

\`\`\`bash
cd /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks
python3 benchmarks/v11_core/run_auto_native_v11.py
python3 -m unittest discover -s benchmarks/v11_core -p 'test_*.py' -v
\`\`\`

**Windows GPU** with the existing S3 GPU virtual environment:

\`\`\`powershell
cd C:\Users\samue\Desktop\gemini\S3
& .\.venv_gpu\Scripts\python.exe ..\S3-Benchmarks\benchmarks\v11_core\gpu_physical_v11.py
& .\.venv_gpu\Scripts\python.exe ..\S3-Benchmarks\benchmarks\v11_core\gpu_resident_conway_v11.py
\`\`\`

The native benchmark data should be used **only after checking that
the JSON indicates IR certificate verification, all differential
checks passing, and actual S3 native assembly**.

## Representative results (single computer, exploratory)

At runtime N=1,000,000, S3 automatically selected cyclic-polynomial
S3 code was respectively ~1.29x / ~1.91x / ~3.48x faster than S3
generic matrix code for widths W=8/16/32. **However, independently
written specialist C/GCC was still much faster** (~86–178x).

Physical RX580 AXPY with copy/readback was dramatically slower
than NumPy for N<=16384; existing GPU cost qualification recommends
CPU. For **50 resident Conway generations**, GPU was slower at
64x64 (8.949 vs 3.452ms) but faster at 128x128 (7.687 vs 12.485ms),
with exact cell parity. This is only one workload and hardware;
no general GPU cutoff is asserted.

The V11 experiment therefore offers a meaningful architectural
next step: cost/proof-driven compiler strategy choice plus cautious
CPU/GPU placement. It **does not** prove a novel algorithm, enable
a global S3 optimization pass or establish production-safe GPU
autodispatch. Compact/DOOM frozen; Windows remains on.
