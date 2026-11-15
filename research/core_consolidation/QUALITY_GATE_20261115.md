# S3 Core — KB-0030 quality recovery and native SIMD validation

**Date:** 2026-11-15
**Campaign:** S3_CORE_QUALITY_V18_NO_LEGACY_DESELECTIONS_20261115
**Decision:** QUALITY_GATE_GO_LOCAL; **not a merge/deployment approval**.

## Root causes, corrections, regression contract

The previously deselected tests failed independently on the unmodified
V18 tree:

1. `tests/test_ffi_capability.py::test_shared_library_compiles_with_requested_optimization_and_syntax_mode`
   had an outdated `observed_compile_source` mock accepting only
   `mode`. The real FFI call forwards `predictive_exact`,
   `predictive_small_t_cutoff`, and `allow_fp_reassociation`.
   **Fix:** the mock now accepts and forwards all three exact
   keyword-only options and asserts their expected values. It
   deliberately does **not** use `**kwargs`, which would mask API drift.
2. `tests/test_native_x86_64.py::test_native_backend_emits_every_current_opcode`
   previously asserted that its source corpus emitted every enum
   opcode except three aggregate-reference operations. After the
   compiler gained backend-only vector and alias instructions, that
   assumption became invalid. A program source corpus cannot directly
   emit the generated vector ISA it is not designed to trigger.
   **Fix:** explicitly enumerate exactly **24** backend-generated
   vector/alias opcodes. Preserve the **25** normal source-emitted
   opcodes and **3** originally unqualified aggregate opcodes.
   The disjointness, exact enum-set equality and explicit 24-opcode
   list mean **new opcodes are not silently ignored**; extending the
   enum without updating the audit makes the test fail.

Changes are **only two test files**, **no production code**:
`tests/test_ffi_capability.py` and
`tests/test_native_x86_64.py`.
The reviewed patch is commit `356b323c` on the isolated branch
`fix/s3-core-inherited-tests-20261115`, based on V18
`1a323a03`.

## Results actually executed on WSL x86-64

| Local suite | Test cases | Exit | Deselect |
|---|---:|---:|---|
| V18 selected V10–V18 + foundation | **248** | **0** | **none** |
| Independent native SSE2/SIMD tests | **14** | **0** | **none** |
| Combined V18 + V12-A + same quality correction | **229** | **0** | **none** |

The combined-local test-only candidate `5340c39e` includes
V18 `1a323a03`, independent V12-A `a271bbfd` and the quality
correction. It is **not pushed** or merged; its only purpose is
semantic regression testing. The 229 included V11–V18,
both V12 families, core backend tests and independent V12
cross-family cases.

Tests were counted separately using `pytest --collect-only -q`
and actual suites had exit status 0. These are **three overlapping
corpora**, not 491 independent tests. The native SIMD suite
contains actual S3-to-x86 compilation and execution, including
SSE2 and automatic vectorization. This is **not** a physical
GPU RX 580 dispatch test or a certification of all vector ISA
variations on all CPUs.

## Versioning and rollout

- Source correction: S3 research branch
  `fix/s3-core-inherited-tests-20261115`,
  commit `356b323c3677f46fee69f1c535bb7f349b2fe35c`.
- Data and logs: S3-Benchmarks branch
  `research/s3-core-consolidation-20261115`;
  `quality_gate_20261115.json`,
  `post_quality_v18_v12a_20261115.json`,
  `quality_v18_*.log` and `post_quality_*.log`.
- No GitHub Actions runner or paid CI used.
  Commits use `[skip ci]`.
- The corrected test files are **not merged into the V18
  PR or main automatically**. Integration requires reviewing
  the stacked branch/dependencies and choosing a target.
- S3 GPU, Compact, DOOM and production unchanged.

## Kanban decision

**KB-0030 — DONE**: the two inherited fixtures were repaired in an
isolated branch, and the selected regression corpus passed with
**zero deselections**. The broader S3 default and release gates
remain separate. Keep experimental optimizations off by default.

Remaining normal planning: CPU/Big-O benchmark campaign
in Sprint 2, **not** an unplanned V19; first synchronize
the reviewed branches when an authorized integration window
is established.
