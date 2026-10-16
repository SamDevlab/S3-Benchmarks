# Independent S3 Benchmark Lab — Pre-V8 Preparation

**Campaign:** `S3_BENCHMARKS_INDEPENDENT_PRE_V8_PREPARATION_V1`

**Repository:** `SamDevlab/S3-Benchmarks` only

**Evidence snapshot:** 2026-10-15

**S3 compiler baseline:** not selected; awaiting a qualified V7 HEAD pinned to a full commit SHA

**V8 profiles or compiler changes:** none

## Outcome

The lab now has a fail-closed result contract for longitudinal comparisons,
an explicit S3/C/Rust/Zig stage matrix, and a machine-readable plan for the
three requested future groups. It reuses the already-integrated exact-SHA
replay and candidate-matrix foundations. The groups remain
`PLANNED_NOT_IMPLEMENTED`; no execution profile is defined or claimed.

Historical evidence is indexed without copying or rewriting measurements in
[`pre-v8-historical-evidence-index-v1.json`](pre-v8-historical-evidence-index-v1.json).
Every entry points to its immutable report commit and Git blob. This matters
because the 2.x evidence is mostly in open stacked PRs, not in `main`: as of
the snapshot date PRs [#15](https://github.com/SamDevlab/S3-Benchmarks/pull/15)
through [#24](https://github.com/SamDevlab/S3-Benchmarks/pull/24) were open
Draft PRs. Their results are therefore marked **pending integration**, even
when a campaign report itself says a workload passed its local gates.

The integrated methodological base is in `main`: the 1.10 multi-SHA replay
checks exact source identities and output compatibility, while explicitly
disallowing cross-version timing deltas for serial, non-interleaved groups;
the 1.12 pinned candidate runner provides clean isolated checkouts, correctness,
artifact capture, and paired interleaved timing. Its three workload outputs
matched, but no eligible transform sites existed and every timing interval
included 1, so the result is inconclusive rather than a speedup.

## Experiment state

| State | Campaigns | Interpretation |
|---|---|---|
| Integrated | JSMN post-P8 report; S3 1.10 historical replay; S3 1.12 pinned candidate matrix | Usable as sourced history/methodology, with the per-report restrictions below. The old JSMN baseline is preserved but its performance evidence is explicitly invalidated. |
| Pending integration | 2.0 foundation (#15), 2.0.1 activation (#16), 2.1 native measurement (#17), 2.1.1–2.1.3 methodology/FFI (#18), scientific mini-apps (#19), XSBench qualification (#20), runtime attribution (#21), budget generalization (#22) | Their PRs were open Drafts. Do not treat them as integrated `main` capabilities or mix their data without protocol qualification. |
| Experimental / pending | 2.2.4 safe-budget P1 (#23); 2.2.5 exact-segment P2 (#24) | P1 passed safety but failed the declared material-recovery gate and was not promoted. P2 is strong benchmark-side experimental evidence, but its own report says production change is not ready and hardening remains. |
| Rejected or superseded evidence | Pre-P8 JSMN timing from the invalidated legacy report; initial XSBench FFI run with failed reproducibility; P1 as a material cross-workload improvement | Preserve in history; do not aggregate as qualified timing or reinterpret as a compiler production result. The later XSBench V2 closure is a distinct protocol and result. |

The complete PR-to-report/commit map and compiler pins are in the JSON index.
“Integrated” describes presence in repository `main`; “qualified” describes
only the named campaign's gates. They are not interchangeable.

## Historical workload findings

| Workload / evidence | Historical result | Boundary that must remain attached |
|---|---|---|
| RMSD | The 2.0 foundation had correctness for single-vector RMSD only. The 2.0.1 activation promoted batch and matrix adapters to correctness/native-canary coverage; its report records 32/32 native canary passes, not performance. The 2.2 scientific mini-app phase reports hosted and native correctness passes, with timing **not run**. The 2.1 process-E2E report includes medium batch (O0 530,528 ns; O1 595,714 ns; O1 CV 0.290), medium matrix (783,303 / 573,051 ns; CV 0.317), and medium single (536,676 / 507,532 ns; CV 0.465). | The 2.1 medians are process-E2E observations on one pinned compiler and one host with high variability; they are not a cross-language or cross-revision ranking. The mini-app result is correctness-only. |
| XSBench | Initial direct-FFI correctness passed 12/12, but reproducibility failed. The later 2.2.1 V2 closure reports a common 100ms work window, K=750,000, five warmups, 30 balanced/interleaved repetitions, and reproducibility pass. Run-E median ratios were S3 O1/GCC O2 105.20x and S3 O1/Clang O2 131.03x; the report explicitly makes **no speedup claim**. The 2.2.2 diagnostic reports about 2.31x (O0) and 2.11x (O1) baseline/no-budget median ratios on its selected workload. | These are different methods and questions: initial FFI fail is not pooled with V2; the later comparison is a qualified characterization, not a language-wide score; the no-budget diagnostic isolates a benchmark/compiler-runtime cost, not kernel-only work. Hardware PMU counters were unavailable. |
| JSMN | The legacy pre-P8 performance report says it is invalidated (no native S3 runner; GCC unavailable). The post-P8 report uses six tiny fixtures, an internal 10,000-parse loop, five warmups, 30 repetitions, with process startup included. S3 O1/GCC O2 geomean was 48.82x historically, 41.54x pre-P8, and 39.88x post-P8; post-P8 was a modest 3.508% absolute geomean reduction versus pre-P8. | The six-fixture corpus and process-E2E scope are narrow; the post-P8 result is characterization, not proof that P8 caused the change. Its external gap and static stack/load/store counts do not establish causal microarchitecture. |
| PolyBench | Five selected kernels (2mm, atax, gemm, Jacobi-1D, MVT) reached correctness/native-canary coverage in 2.0.1. In 2.1, O1/O0 medians varied by kernel: medium 2mm 0.977x, atax 0.902x, gemm 1.184x, and MVT 1.257x; the medium MVT O1 CV was 2.413. | A small subset and short process-level runs; CV makes simple O0/O1 ranking unreliable. PolyBench/C upstream version and dataset/compile-time options must be pinned before future cross-language runs. |
| PRK, BabelStream-compatible subset, PLB2, TSVC | Activation evidence established selected small/medium correctness and native-canary coverage. The mainline 1.10 work additionally supplies three unrelated engineering/geospatial/energy workload examples; exact-SHA compatibility passed, but serial version groups do not support timing deltas. | Do not infer full upstream workload compatibility from representative adapters. In 1.12 the candidate had no eligible sites, and timing remained inconclusive. |
| Exact instruction-budget studies | 2.2.3 reports diagnostic budget shares in the 51.78%–61.98% range for selected workloads. P1 recovered only small or negative fractions on its RMSD/XSBench/JSMN cells and failed the material gate. Experimental P2 reports 92.14%–104.56% “removable budget excess” recovered over the tested RMSD/XSBench/JSMN O0/O1 cells. | These are causal, benchmark-side budget diagnostics at specific pinned compiler/workload points—not a V8 profile, not a general application speedup, and not a production-ready S3 compiler change. P2 remains experimental/pending hardening. |

Exact source reports and commit pins are retained in the machine-readable
evidence index; historical report files have not been edited.

## Prepared comparison matrix

Each future cell is a distinct record identified by compiler/toolchain,
immutable revision, implementation revision and digest, workload fixture and
dataset digest, host fingerprint, protocol digest, and experiment group.
Results are reported in separate stage fields; a missing or failed stage is
never converted to zero or folded into another metric.

| Language | Compiler identity policy | Correctness | Compilation | Execution | Binary size |
|---|---|---|---|---|---|
| S3 | Full lowercase 40-character S3 commit, clean checkout, plus compiler executable digest | Independent oracle/output digest | Workload compile exit and elapsed ns | Raw samples, scope, normalized work units | Exact bytes and object format |
| C | Exact compiler version and executable digest; pinned workload source/build recipe | Same observable contract | Separate compile status/time | Same fixture and timing protocol | Exact bytes and object format |
| Rust | Exact compiler version and executable digest; pinned workload source/build recipe | Same observable contract | Separate compile status/time | Same fixture and timing protocol | Exact bytes and object format |
| Zig | Exact compiler version and executable digest; pinned workload source/build recipe | Same observable contract | Separate compile status/time | Same fixture and timing protocol | Exact bytes and object format |

`tools/pre_v8_longitudinal.py` enforces comparable workload, fixture, input,
host, protocol, and timing scope. Revision-mode comparisons additionally hold
the workload implementation and build recipe fixed. Language-mode output is
descriptive only and reports correctness, build time, execution, and size
separately; it does not turn them into a composite score or a speedup claim.

## Historical bottlenecks and experiment priority

1. **Measurement noise and inconsistent work duration.** 2.1's high CVs, the
   2.1.1 failed same-host slope replay, and the 2.1.2 inability to find a
   common fixed-work window show that work calibration and repeated sessions
   are first-order gating work, not reporting polish.
2. **Process/runtime overhead can dominate small kernels.** The JSMN
   process-level comparison and XSBench budget attribution expose large
   non-kernel/runtime costs, but require a scope-specific interpretation.
3. **Static size/counts are not causal execution evidence.** Assembly,
   `.text`, stack, and load/store observations help choose hypotheses, but
   counter access was unavailable in several runs and static counts do not
   prove hotness.
4. **Correctness adapter coverage is not full benchmark coverage.** RMSD,
   PolyBench, PRK and BabelStream subsets need explicit common inputs,
   algorithmic equivalence and upstream/version audit before expansion.
5. **Language and profile confounding.** A future matrix must pin the source
   implementation and compiler, and must not silently mix measurement scopes,
   flags, or profile modes.

Priority for the next safe campaign is therefore:

1. Wait for and record the qualified V7 full commit SHA; verify it exists and
   is clean/read-only in a detached source checkout. Do not use a moving branch
   or select a baseline before qualification completes.
2. Freeze one bounded, shared fixture/protocol cohort and qualify differential
   correctness for S3, C, Rust and Zig before performance collection.
3. Calibrate runtime so each language uses a common useful work window; retain
   raw samples and build multiple binaries/sessions where the protocol calls
   for it. Use interleaving/paired ordering for candidates and disclose scope.
4. Populate all four stage outcomes independently; keep execution evidence
   ineligible when correctness or build fails. Do not collapse binary size,
   build latency or execution time into a single score.
5. Only after profiles are implemented and separately specified, run the
   three planned groups. The present plan does not define or implement S3 Puro,
   S3 Controlado, or any V8 execution profile.

## Methodological sources and upstreams consulted

- Kalibera and Jones, [“Rigorous Benchmarking in Reasonable Time” (ISMM 2013)](https://kar.kent.ac.uk/33611/): repeat at relevant levels and account for uncertainty rather than treating one run as a stable effect.
- Kalibera and Jones, [“Quantifying Performance Changes with Effect Size Confidence Intervals”](https://arxiv.org/abs/2007.10899): quantify uncertainty in performance ratios and account for execution and compilation non-determinism. The prepared comparator deliberately reports descriptive medians only; it does not substitute for a paired confidence-interval analysis.
- Georges, Buytaert, and Eeckhout, [“Statistically Rigorous Java Performance Evaluation” (OOPSLA 2007)](https://dri.es/files/oopsla07-georges.pdf): useful general treatment of repeated measurements and analysis choices; JVM-specific findings are not transferred to S3.
- SPEC, [CPU 2017 Run and Reporting Rules](https://www.spec.org/cpu2017/Docs/runrules.html): disclose conditions, validate outputs, repeat runs, and use medians/slower-of-two under its own rules; used here as a methodological reference, not as a claim of SPEC compliance.
- [JSMN upstream](https://github.com/zserge/jsmn), [ANL-CESAR XSBench](https://github.com/ANL-CESAR/XSBench), [PolyBench/C 3.2](https://www.cs.colostate.edu/~pouchet/software/polybench/polybench.html), and [charnley/rmsd](https://github.com/charnley/rmsd): upstream workload context only. Their versions, licenses, ports, datasets, and algorithms still require the repository's own immutable pins and equivalence gates.

## Validation performed for this preparation

Validation results: all three new JSON documents parse; the plan check passed
for 16 evidence entries and verified each linked Git blob against its indexed
commit/path; the six new contract tests passed; Python compileall and
`git diff --check` passed. The full repository suite reported 57 passed, 1
skipped, and 2 failed: both failures are existing S3 1.10 replay-index tests
that stop on the same historical raw-file hash mismatch (expected
`550e7ca3…`, checked-in file `42998094…`). The failing source and evidence
paths were unchanged by this preparation. Excluding that existing test module,
the suite reported 57 passed and 1 skipped. No historical evidence was edited.

This host does not have the `jsonschema` package, so the JSON Schema document
was parsed and its contract was exercised through the custom validator tests,
not run through an external full JSON-Schema implementation. No S3 compiler or
workload was built or run. The current prep host is Windows and has Python,
but no `gcc`, `clang`, `rustc`, `cargo`, `zig`, or `cl` command available;
therefore no new cross-language benchmark was appropriate or reported.
