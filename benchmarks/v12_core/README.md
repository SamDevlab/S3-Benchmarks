# S3 V12 — Verified IR Candidates, Native Arithmetic, Cost-Aware GPU

## Reproducible experiments

This campaign is an experimental move beyond V10–V11 GF(2).
The S3 repository implements:
- Source-aware structural proof of a restricted **checked-i64**
  same-sign progression, with exact overflow guards.
- Genuine S3 x86-64 generated native fast-forward code.
- Verified IR candidate registry that accepts GF(2) and i64 proof
  families and selects only when matched measured cost evidence
  justifies promotion; otherwise falls back to original IR.
- Physical CPU/GPU recommendation using real measurements,
  exact-workload matching and existing hard GPU safety qualification.

### I64 native S3 vs S3 iteration vs GCC -O3

\`run_i64_native_v12.py\` compiles the original S3 \`update\` and
certified closed-form S3 native dynamic-N routine, then calls the
independent C11 harness \`compare_i64_progression_v12.c\`.
Nine alternating rounds, 64 independently checked states per N.

Results in \`i64_progression_results_v12.json\`.

At N=1e6 (delta=+7):
- Original S3 N updates: 4.1291ms.
- Certified S3 native formula: 5.44ns raw C ABI.
- GCC C independent closed form: 0.81ns (very short/time-noise
  susceptible).
- Certificate proof ~0.271ms; specialized cold build plus smoke
  ~98.6ms; checked Python public call ~0.132ms.

This is **known O(N) to O(1) arithmetic progression**, not a new
mathematical algorithm. For N=0 the raw S3 original loop was
~4ns, while the specialized call was ~5.44ns, illustrating why
small inputs need cost-aware selection. Invalid signed-i64
endpoints are rejected rather than wrapped.

### Assembly profile

\`profile_native_codegen_v12.py\` compiles genuine certified
S3-native cyclic code and uses \`objdump\` to capture the
interesting S3 helper and GCC specialist assembly. Outputs:
- \`native_codegen_profile_v12.json\`
- \`native_codegen_disassembly_excerpt_v12.txt\`.

W32: S3 has ~104/148/185/151 static instructions in rotation,
GF(2) multiply/square and dynamic entry, versus ~133 static
instructions in the independently compiled GCC sparse specialist
entry (helpers inlined). This **does not isolate codegen quality**:
the C specialist uses a sparse set-bit algorithm and S3 uses dense
fixed-width loops, and static instructions are not dynamic counts.
No PMU hardware counters measured.

### Physical GPU exact-workload calibration

On Windows with physical AMD RX 580 Vulkan and the existing
\`S3/.venv_gpu\`, run \`gpu_calibration_v12.py\`.
It executes seven CPU NumPy and GPU S3->WGSL Conway 50-step
end-to-end runs for each grid, asserting full-cell parity each
time, within provisional safe GPU buffer limits, and feeds
**actual raw samples** to the new hard-gated CPU/GPU planner.

\`gpu_calibration_v12.json\`:
- 64x64: CPU 3.026ms / GPU 4.947ms => experimental CPU.
- 128x128: CPU 7.267ms / GPU 5.220ms => experimental GPU.

Selection is only for an exact match of source SHA, host,
device, precision, residency, dimensions and steps.
A faster GPU cannot bypass a device failure, unverified output,
unsupported precision, unsafe buffer or missing calibration.
No production dispatch changed.

### Reproduction

WSL/Linux:
\`\`\`bash
cd /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks
python3 benchmarks/v12_core/run_i64_native_v12.py
python3 benchmarks/v12_core/profile_native_codegen_v12.py
python3 -m unittest discover -s benchmarks/v12_core -p 'test_*.py' -v
\`\`\`

Windows physical GPU:
\`\`\`powershell
cd C:\Users\samue\Desktop\gemini\S3
& .\.venv_gpu\Scripts\python.exe ..\S3-Benchmarks\benchmarks\v12_core\gpu_calibration_v12.py
\`\`\`

## Scientific status

GO experimental: evidence-bound candidate registry across two
different IR proof families, checked-i64 source-native shortcut,
verified physical GPU data and architecture-aware disassembly.

NO-GO: full automatic production optimizer, universal algorithmic
invention, independent formal verification of x86 machine code,
generalizable GPU speedup or selected threshold for any other host.

This is one computer/session and samples were measured using local
toolchains; aggressive GCC optimization and timing resolution can
affect nanosecond comparisons. Research evidence should be
repeated independently before ranking runtimes across systems.

Compact/DOOM frozen; no auto-merge, deploy or Windows power actions.
