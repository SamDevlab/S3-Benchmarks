# S3 AArch64 Structural Benchmark Preflight

This workload promotes the M1.77/M1.78 ARM64 candidate into an executable **structural correctness** gate.

It is **not** an ARM64 runtime benchmark and it does **not** claim that S3 currently matches LLVM code quality.

## Baselines

S3:

`SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`

Pinned external architecture/codegen reference:

`llvm/llvm-project@b562ef546e46face7172d174e1a5f5454c470eee`

The runner verifies both pins before producing evidence. LLVM is currently a **pinned review reference only**; the CI job does not build or execute that LLVM commit.

## What the current S3 gate can prove

The current M1.77/M1.78 implementation exposes bounded structural contracts for:

- Linux `linux-aarch64` target registration;
- macOS `macos-arm64` target registration;
- AAPCS64 integer/scalar argument locations `x0` through `x7`;
- scalar return in `x0`;
- stack argument locations after the first eight scalar arguments;
- deterministic `mov x0, #imm` + `ret` structural assembly;
- ELF64 little-endian AArch64 header identity (`e_machine = 183`);
- Mach-O 64-bit ARM64 executable header identity;
- explicit execution-certification deferment;
- fail-closed invalid structural inputs.

## What the current S3 gate cannot prove

These contracts remain explicitly **unmodeled** in the current V1 backend and therefore must not be inferred from a passing report:

- floating-point argument register classification;
- explicit 16-byte stack-alignment proof;
- aggregate argument classification;
- aggregate return / `sret` lowering;
- ELF sections and relocations;
- Mach-O load commands, sections and relocations;
- actual AArch64 machine-code encoding;
- native linking and execution.

Because of those gaps, the following remain invalid/deferred:

`COMPARATIVE_CODE_QUALITY_VALID=false`

`EXECUTION_BENCHMARK_VALID=false`

`LLVM_ORACLE_EXECUTION=DEFERRED_PINNED_REFERENCE_ONLY`

## Run

```bash
S3_CURRENT_REPO=/path/to/S3 python tools/aarch64_runner.py --verify-only
```

PowerShell:

```powershell
$env:S3_CURRENT_REPO = "C:\path\to\S3"
python tools/aarch64_runner.py --verify-only
```

Default report:

`reports/aarch64-structural.json`

## Future promotion criteria

A real S3-vs-LLVM AArch64 code-quality campaign requires, at minimum:

1. actual S3 AArch64 machine-code/object emission;
2. explicit ELF/Mach-O section and relocation semantics;
3. aggregate ABI and stack-alignment contracts;
4. equivalent source kernels compiled by both S3 and a reproducibly identified LLVM/Clang toolchain;
5. object disassembly or machine-code inspection;
6. correctness before instruction-count/code-size comparison;
7. real target hardware or a separately classified execution environment before runtime timing.

Until those exist, this workload is intentionally a structural conformance preflight rather than a performance benchmark.
