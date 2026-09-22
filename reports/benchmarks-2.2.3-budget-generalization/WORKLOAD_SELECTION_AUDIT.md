# Workload Selection Audit

CAMPAIGN=S3_BENCHMARKS_2_2_3_MULTI_WORKLOAD_BUDGET_CAUSAL_VALIDATION
BENCHMARK_BASE_HEAD=f2b4acb510b5f0e6a9e04287d3061194094d1417
S3_SHA=e07d0b5464bf472b2ca18993f3e196a234ff0fc5
S3_SOURCE_CHANGES_REQUIRED=NO

## Selection gate

The selection is based on already present benchmark implementations and
adapters, not on expected timing. The causal intervention is the existing
fail-closed instruction-budget assembly rewriter in
`tools/runtime_attribution.py`. No compiler, runtime, backend, ABI, or S3
source change is required.

| Workload | Class | Existing implementation | Native correctness | FFI / native path | Control | Oracle | Work unit | Required benchmark changes | S3 changes | License / provenance | Risk | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hpc.prk.nstream` | regular numerical | Existing `FFIPilot` in `tools/ffi_direct_kernel_methodology.py` with fixed 31-element vector kernel | Existing FFI pilot correctness gate; matched S3 and C implementations | Direct `dlopen`/`dlsym` driver with S3 O0/O1 and GCC/Clang O2 | C implementation in the same pilot, identical exported signature and work | Fixed scalar checksum in the pilot contract | One vector element update/checksum contribution; 31 per call | Generic causal runner can reuse the existing rewriter and FFI driver, but the preselection calibration did not reach the 100 ms fastest-control threshold before the frozen 10B instruction limit | No | PRK directory is pinned and its manifest records upstream ParRes provenance; this pilot already has an explicit benchmark-side C control | Low adapter risk; measurement-window risk is factual and preserved as a blocked attempt | FALLBACK |
| `scientific.rmsd.batch` | regular numerical | Existing `FFIPilot` source/control pair in `tools/ffi_direct_kernel_methodology.py`; tracked batch manifest remains `NOT_SUPPORTED_YET` for whole-program composition | Existing direct FFI pilot has matched S3/C result and independent expected checksum | Direct `dlopen`/`dlsym` driver with S3 O0/O1 and GCC/Clang O2; this experiment names the pilot path explicitly and does not claim tracked batch composition closure | Matched C implementation in the existing pilot | Fixed RMSD pilot checksum contract | One pair comparison across 16 coordinate triples; pilot repeats K calls | Generic causal runner applies the existing rewriter, derives sites, and adds paired sessions; no S3 changes | No | Scientific workload metadata pins `charnley.rmsd`; pilot source/control are already present | The tracked whole-program batch remains deferred; only the existing bounded FFI pilot is measured | SELECTED |
| `scientific.rmsd.single` | regular numerical | Tracked `benchmarks/scientific/rmsd/rmsd.s3` and Python oracle exist | Hosted correctness is present in the candidate matrix; no direct FFI export contract in the tracked source | Existing native measurement is adapter-generated PROCESS_E2E, not the tracked exported FFI kernel | No matched direct FFI control for the tracked source | Python RMSD oracle | One scalar coordinate comparison | Would require a new callable adapter or a materially different timing path | No S3 change allowed, but protocol compatibility work is non-trivial | RMSD manifest pins upstream reference | DEFERRED: less direct than NStream for this causal protocol | DEFERRED |
| `realworld.jsmn` | control-flow / parsing | Existing `benchmarks/jsmn` S3 implementation, corpus, upstream C runner, differential oracle, and native runner | Existing native S3 and C correctness path validates status, token boundaries, token count, and checksum | Existing native executable path; no FFI is required because the campaign permits native/FFI-compatible paths | Upstream `jsmn` C runner built with GCC/Clang | `reference_jsmn_oracle` plus `compare_results` in the existing harness | One complete JSON parse of a fixed corpus input; token/status/checksum remain observable | Small benchmark-side adapter: build S3 O0/O1 assembly, apply the existing rewriter to obtain no-budget variants, build GCC/Clang O2 controls, and run fresh processes with the existing differential oracle | No | `benchmarks/jsmn/upstream` and manifest provide the existing upstream material and corpus; verify recorded upstream pin before timing | Medium: the legacy runner is PROCESS_E2E and needs protocol normalization, but the semantic oracle and native path already exist | SELECTED |
| `scientific.xsbench.compatible_lookup.medium` | irregular scientific | Existing 2.2.2.1 positive-control artifact and raw evidence | 18/18 correctness and native diagnostic gates previously passed | Existing positive-control native measurement on recovered `s3-vm` | GCC O2 and Clang O2 artifacts from the prior campaign | Existing XSBench correctness contract | One XSBench lookup at the pinned medium workload and prior K | Compact confirmation only; reuse prior evidence unless host/provenance requires a bounded confirmation | No | Prior pinned XSBench provenance | Low: already confirmed, but current campaign must preserve its role as positive control rather than over-repeat it | SELECTED |

## Class decisions

REGULAR_WORKLOAD_SELECTION=scientific.rmsd.batch
SELECTION_REASON=existing direct FFI S3/C pilot, independent checksum, stable fixed work, and no S3 change; tracked whole-program batch composition remains explicitly deferred
CONTROL_FLOW_WORKLOAD=realworld.jsmn
CONTROL_FLOW_SELECTION_REASON=existing native executable, upstream C control, differential token oracle, and benchmark-side-only adapter path
IRREGULAR_WORKLOAD=scientific.xsbench.compatible_lookup.medium
NSTREAM_PRESELECTION=BLOCKED_NO_COMMON_MEASUREMENT_WINDOW
RMSD_BATCH_SELECTION=SELECTED_EXISTING_FFI_PILOT_TRACKED_BATCH_DEFERRED

## Protocol compatibility audit

The selected RMSD pilot can reuse the existing direct FFI driver and its
`CLOCK_MONOTONIC_RAW`, CPU-0, fresh-process, balanced-session machinery. The
selected JSMN path will use the same causal rewrite and fresh-process policy,
but its timing scope remains a matched native PROCESS_E2E parser invocation;
the report must not call it pure kernel time. The six variants remain S3 O0,
S3 O0 no-budget, S3 O1, S3 O1 no-budget, GCC O2, and Clang O2. Budget-site
counts must be derived from each generated assembly; XSBench counts are not
reused as expectations.

Before official timing, each selected workload requires all six correctness
variants, a per-workload K with the fastest control at or above 100 ms, five
external warmups, thirty balanced fresh-process repetitions, and two
independent sessions. Missing or failed samples remain failures and are never
encoded as zero.

## Environment and safety

The currently reachable native environment is the existing `s3-vm` guest,
Linux x86-64, with Python 3.14.4, GCC 15.2.0, Clang 21.1.8, and `/usr/bin/perf`
present. Host fingerprint and full toolchain details are captured in the raw
environment record before timing. The S3 checkout remains read-only at the
pinned SHA. PR #190 remains read-only. No power action is permitted.

WORKLOAD_SELECTION_GATE=PASS
