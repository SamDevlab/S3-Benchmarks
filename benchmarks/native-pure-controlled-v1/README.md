# S3 native pure vs controlled — V1

This is a new, isolated pre-V7 experiment. It does not reuse historical timing rows as observations and does not depend on V7, S3C-NG, or V8. The exact V6 compiler baseline is `2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c`; the optional benchmark-only Pure backend is a child commit with only an opt-in instruction-budget policy added.

## Workload and correctness contract

Six source fixtures already accepted by V6 are pinned under `sources/`. They cover arithmetic, data-dependent decisions, bounded array traversal, scientific reductions, geometry, and two composite applications. Every workload runs at three input sizes (32/128/364 items; geometric kernels use 16/64/121 points) over prefixes of the same deterministic runtime fixture. The timed-call count is scaled inversely for smaller inputs to keep total processed work roughly comparable, and is identical for all implementations at each workload/size. The fixture is generated once from a fixed seed and passed from a runtime binary file to every native implementation. The Python oracle validates every output before a timing row is accepted. Floating comparisons use absolute and relative tolerance `1e-10`; integer statuses/counts are exact. Invalid-input status probes are a separate untimed gate and are not included in performance rankings.

`reference/kernels.c`, `kernels.rs`, and `kernels.zig` are independent language ports of the same six valid-input algorithms with the same C ABI as the S3 exports. The repository's existing `native_reference_kernels.c` is retained as provenance; where its older ABI differs, the campaign wrappers use the pinned S3 source contract. Python is timed as an interpreted implementation and is never in a native S3/C/Rust/Zig timed region.

## What Pure means

`pure-experimental` removes only the dynamic instruction-budget counter/check from S3 x86-64 emission. It retains array bounds, overflow, initialization, and other generated checks. It is experimental and not security-equivalent to `PER_INSTRUCTION`; external process limits are still required for untrusted/non-terminating code. The controlled modes are `PER_INSTRUCTION`, `EXACT_SEGMENT`, and `LOOP_HYBRID`, not aliases for Pure. Default compilation remains controlled.

## Measurement

The C runner loads a shared library before starting `CLOCK_MONOTONIC_RAW`, performs a correctness call outside the timer, and times repeated calls over the same runtime fixture. The common indirect FFI call/dispatch is inside every native measurement and is not subtracted; this avoids claiming an unmeasured dispatch correction. It checks the final result after the timed region. The orchestration uses three warmups and fifteen measured samples per configuration, shuffled in balanced seeded rounds. Raw samples, including outliers, are retained. The process-startup/loader path, kernel time, compiler/frontend time, assembly time, object assembly time, link time, peak RSS, ELF size, and `.text` size are stored as separate fields. Python runtime is listed separately because its timer includes interpreter function and loop overhead. Zig cache/temp paths are passed only to the campaign child process and point into its `/dev/shm` build directory.

S3 O0/O1, C O0/O2, Rust opt-level 0/2, Zig Debug/ReleaseFast, and Python are distinct optimization contracts; they are not represented as equivalent optimizer levels. The guest is a 3-vCPU KVM VM, has no available frequency governor interface, and its root filesystem is full. All generated artifacts must therefore remain under `/dev/shm`; results are descriptive of this guest only and no bare-metal or causal hardware claim is made.

## Run

On Linux x86-64 with GCC, Rust, Zig, Python, and the pinned S3 compiler source available:

```sh
S3_REPO=/path/to/pinned-S3 python3 campaign.py --output /dev/shm/s3-native-pure-v1-results
```

The runner refuses to accept a result when a source hash, compile, status code, or output parity check fails. See `manifest.json` for the full pinned source hashes and protocol. Generated raw output belongs under the campaign's results directory and must not be folded into historical benchmark reports.

The sample size is bounded by S3's existing 100,000-instruction execution cap. A high-repetition pilot exhausted that cap in controlled O0 point-cloud processing; the final protocol uses a base of one call per process and scales to 8/2/1 calls for small/medium/full inputs. The failed pilot is a calibration limit, not a timing result.
