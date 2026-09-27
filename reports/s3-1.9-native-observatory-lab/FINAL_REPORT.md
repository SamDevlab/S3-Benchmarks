# S3-Benchmarks 1.9 Native Observatory Lab

## Scope and provenance

Lab base: `e5ff385d26ea6ec89d13cf1955bfa5438e56a266`, tree
`c06ac7b063f27144fa19ddc84dc33c082fcc134a`. The campaign adds an independent
executor and evidence registry outputs, and hardens LF-canonical validation
for pinned text artifacts. It does not alter an S3 compiler source. The
compiler input used for both direct and independent native runs was the exact
clean S3 commit `211b1aecec756be42516322429720018f54001e7`, tree
`08289d214832e856d46e14ef941239649e9f4063`.

The lab executor cloned the public S3 repository, checked out that exact
commit detached, verified its tree and cleanliness, checked compiler source
hashes, then ran correctness gates before collecting timing. The raw
independent result SHA-256 is
`897fade8e52d459bf505c89d52a3f307196757d0ea1ea99e993914e968a9e721`; the
wrapper SHA-256 is
`362ae31e343230be83a2375b31a714da6814d4f1c6aeb1cca3c2463e03694bc6`.

## Recharacterization

The direct and independent runs used the same Linux x86-64 host, workloads,
S3 source commit/tree, compiler inputs, correctness gate, FFI timing scope,
3 warmups, 21 samples, 1,000 iterations per sample, paired order seed 1501,
and 10,000 bootstrap resamples. Compilation/setup were excluded; same-process
scalar C ABI dispatch is included equally. PMU access was unavailable by
policy (`perf_event_paranoid=4`). Classification is
`CHARACTERIZATION_ONLY`; `native_speedup_claim=false`.

| Workload | EXACT_SEGMENT | LOOP_HYBRID | Cross-run conclusion |
| --- | --- | --- | --- |
| point cloud | material in both runs | material in both runs | repeated result for both modes |
| raster | material in both runs | inconclusive in both runs | EXACT repeats; HYBRID not established |
| energy | inconclusive then material | inconclusive then material | both remain cross-run inconclusive |

O0/O1 showed no material change within the declared threshold for these
workloads. Compact-EA was not applied to these functions; its timing is not
evidence for transformed code. These are workload-specific budget-mode
observations, not a universal speedup claim. PER remains the default.

The S3 Observatory and workload benchmark use different code-generation and
accounting domains: the Observatory counts the entire standalone native
object `.text`, while older `static_machine_instructions` values describe an
exported workload symbol from an FFI-specific path. Those totals are not
compared as though they were equivalent.

## Rejected experiment and discovery ranking

`EXP-S3-19-OPT-001` tested a non-production same-block exact-cell mutable
load-forwarding rule. Baseline and candidate native outputs matched each
other and the independent references. Among 220 mutable loads, 0 satisfied
the rule's unchanged-object, index-version, initialization, and type
preconditions. Classification:
`REJECTED_NO_ELIGIBLE_REPEATED_MUTABLE_LOADS`. This rejects only that exact
rule on these pinned workloads; broader memory-origin reduction remains
open. No timing or PMU measurement was made for the candidate.

Discovery ranking v3 consumes validated Observatory v4, current O1 reference
reports, and per-function static allocation facts. It records 8 references
with known origins and `NO_ESCAPE` (3 mutable), 1,024 virtual registers,
6 static stack-resident virtuals, peak live count 11, and
`dynamic_spills=NOT_MEASURED`. Transformation authority remains false.
The added facts do not change v2's tier-first ranking or manufacture causal
scores. No allocator replacement is selected; static stack residence is not
a runtime spill metric.

| Ranked hypothesis | Tier | Score | Decision boundary |
| --- | --- | ---: | --- |
| EXACT_SEGMENT | T1 | 0.05727047 | Repeated workload-specific characterization; no default promotion |
| LOOP_HYBRID | T1 | 0.02861262 | Repeated only for point cloud; other cells inconclusive |
| MEMORY_ORIGIN_REDUCTION | T2 | 0.12757663 | Broad hypothesis open; exact local forwarding rule rejected |
| NATIVE_MOVE_AND_CONTROL_LOWERING | T2 | 0.11812416 | Structural question; no causal timing evidence |

The current vector reports classify 5 loops as `UNKNOWN`, 0 as proven
vectorizable, and 0 as proven illegal. Missing proofs cover affine induction,
access range/immutable origin, and general inter-iteration dependence. No
SIMD or parallelization is authorized.

## Portability correction and test history

On Windows with `core.autocrlf=true`, the historical S3 1.7 fixture, dataset,
and adapter patch were checked out with CRLF. Their manifest hashes describe
canonical LF bytes. The first full Windows suite therefore exposed 3 failures
(with 23 passes) in the old raw-byte validator; the exact transcript is gzip
preserved at `evidence/validation/full-suite-windows-20260927-124551.log.gz`.
Its decompressed SHA-256 is
`3c6c1423e7dfafa9ea4b63d3ab62fd7b9e4fba65cce13582c562fd2658db006b`; the
compressed file SHA-256 is
`1a8b07e58570193a79cfbc4221442ec090e2b9ea4e52b4863b112ebc58e6cddf`. The fixture's
raw SHA differed, while its LF-normalized SHA exactly matched the manifest.

The repair canonicalizes CRLF to LF only for these pinned text-artifact
integrity checks; it does not rewrite fixture files or change experiment
semantics. Regression tests verify line-ending-independent validation. After
the repair:

- S3 1.7/1.8/1.9 focused Windows tests: 19 passed.
- Full Windows Bench suite: 27 passed, 0 failed; exit 0.
- `compileall tools tests`: passed with an existing `SyntaxWarning` in
  `tools/runner.py:899` for the escape `\\_`.
- `git diff --check`: passed; Git reports expected LF-to-CRLF checkout
  warnings for tracked text files.
- Linux-focused Bench tests from the preceding exact campaign candidate:
  13 passed across the 1.8 and 1.9 test modules. The portability helper's
  canonical-LF behavior is unchanged on Linux and is directly exercised on
  Windows.

The initial failure is retained as diagnostic history, not represented as a
passing run. No fixture, manifest, historical experiment result, S3 source,
or native measurement was rewritten.

## Final status

```text
BENCHMARK_EXECUTOR=PARTIAL
PINNED_SHA_CHECKOUT=QUALIFIED_FOR_ONE_S3_SHA
CORRECTNESS_BEFORE_TIMING=PASS
INDEPENDENT_NATIVE_CHARACTERIZATION=PASS
REPRODUCIBILITY=PARTIAL
HISTORICAL_REPLAY=OPEN
RESULT_SCHEMA=1.0.0
PROVENANCE=PASS_FOR_RECORDED_RUNS
EXPERIMENT_REGISTRY=PARTIAL
HYPOTHESIS_REGISTRY=PARTIAL
NEGATIVE_RESULT_REGISTRY=PARTIAL
COMPILER_PATTERN_CORPUS=PARTIAL
CROSS_VERSION_DATABASE=OPEN
PER_VS_EXACT=REPEATED_MATERIAL_FOR_POINT_CLOUD_AND_RASTER; ENERGY_INCONCLUSIVE
PER_VS_HYBRID=REPEATED_MATERIAL_FOR_POINT_CLOUD; OTHER_CELLS_INCONCLUSIVE
PER_DEFAULT=YES
TIMING_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
PMU=UNAVAILABLE_BY_POLICY
BENCH_TESTS=27_PASSED
```

S3-Benchmarks PRs #15, #23, and #24 remain independent open Drafts. Their
state and branch relationships are not changed here. S3 1.7 PR #321 and
Benchmarks 1.7 PR #25 are merged. This campaign is research-only: no merge,
release, tag, PyPI publication, or budget-mode promotion is performed.
