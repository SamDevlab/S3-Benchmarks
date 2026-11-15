# S3 Core — V12 PR #409 vs PR #410 semantic coexistence

**Campaign:** S3_CORE_V12_SEMANTIC_COHABITATION_20261115
**Date:** 2026-11-15
**Decision:** GO_EXPERIMENTAL_COMPATIBLE_SUBSET; NO MERGE / NO DEFAULT ENABLE
**Control:** local Windows Git worktrees + WSL Linux native pytest,
no GitHub Actions, no production changes.

## Problem

Two Draft PRs originate from the same V11 branch:
- **S3 #409** `exp/s3-v12-verified-candidate-registry`,
  commit `a271bbfdf8f9a4d2f1c1cff5fcb27fd973e0cfa0`;
- **S3 #410** `exp/s3-v12-core-native`,
  commit `02f0a3f76b138b5495362fe9161058cdee00f3f7`.

The #409 PR changes **nine files**, and #410 **eight**.
The PR diffs have **zero overlapping paths**. No shared file paths
does **not** establish binary or semantic compatibility.

S3 V13–V18 descend from the **#410** branch. To avoid
losing the #409 research or accidentally incorporating
unverified code into production, the #409 change was
applied read-only to disposable local integration worktrees.

## Exactly what was tested

Two isolated research branches built with Windows Git:
1. `research/s3-v12-combined-local-review-20261115`, base
   `02f0a3f7` (V12 #410), add all nine files from #409
   via `git cherry-pick --no-commit a271bbf`.
   Local test-only commit `3555bc01`.
2. `research/s3-v18-plus-v12a-local-review-20261115`,
   base `1a323a03` (V18), add exactly the same nine
   files via the same procedure.
   Local test-only commit `92973e3f`.

**The test-only branches remain LOCAL, not pushed or merged.**
None of the source PRs was altered. Both staged applications
were conflict-free, checked with `git diff --cached --check`,
then committed with `[skip ci]` locally to leave clean worktrees.

On the WSL Linux x86-64 host, the test sets include:
- Four original #409 test modules: empirical GPU route
  (*synthetic cost policy, not physical RX580 validation*),
  i64 proof, native exact progression, registry verification;
- Three original #410 test modules: GF2 sparse codegen,
  GPU cost dispatch and IR-bound verified candidate registry;
- V11 auto-algorithm selection and optimizer regression;
- Four independent cross-family tests in
  `test_v12_cross_family.py`: IR-derived checked progression
  belongs to A but is rejected by B; exact i64 identity
  belongs to B but is not falsely claimed by A; independent
  opt-in controls; incomplete cost evidence fails closed;
- On the V18 overlay, additional tests V13–V18 verify the
  later native compiler changes still run with A present.

| Isolated build | Collected test cases | Actual pytest exit | Outcome |
|---|---:|---:|---|
| V12 #410 + #409 | **93** | **0** | PASS |
| V18 + #409 | **159** | **0** | PASS |
| Combined | **252 executions** (some tests repeated) | 0/0 | PASS |

`pytest -q` in these repositories deliberately omits a
numeric summary; counts were derived with `pytest --collect-only -q`
for the **same test selectors** and cross-checked with the
actual suite exit codes. Raw logs and immutable PR SHA
data are present in `v12_coexistence_20261115.json`
and `v12_overlay_local_refs_20261115.json`.

## Semantic result, not cosmetic PR compatibility

The two candidate APIs are *different*, not aliases:
- #409 `discover_verified_candidates()` certifies an
  exact checked signed-i64 progression such as `x + 7`;
  its `StrategyCostObservation` requires provenance,
  seven or more paired measurements, parity, and
  amortized cost; absent evidence selects original IR.
  `compile_certified_i64_native()` requires explicit
  experimental opt-in and independently validates native
  exact arithmetic and overflow.
- #410 `register_verified_candidates()` admits a restricted
  `I64_PURE_IDENTITY` (e.g. `x * 1`, `x / 1`) and
  GF2 exact families, **not** the unchecked `x+7`
  rewrite. Its own experimental opt-in is separate.

Critically, the #409 registry documents that it is a
**research API, not wired to the production compiler**.
The cross tests verify separation and fail-closed behavior,
but this campaign does **not** modify the S3 optimizer to
automatically select either new candidate family.

The two branches can **coexist experimentally** in the
tested source trees. There is no evidence of name collision
or regression in the tested subset. This does not establish:
- all program states or compiler permutations;
- physical GPU throughput or dispatch safety;
- the correctness of integrating both into default routing;
- verified cost selection from production/real measured traces;
- approval for a multi-PR merge into `main`.

## Integration decision / next gate

**Recommend preserving #409 as an independent
opt-in research component**, while the stacked compiler
line continues to identify #410 as its V12 ancestor.

Do **not** merge #409 or #410 automatically; first
review V11 and older dependencies, choose an explicit
combined integration branch, and run a complete local
suite including the two known inherited failures once
their fixtures are repaired.

The direct next task in KB-0029 is to assess V11→V13
release dependencies and verify the candidate baseline
on the agreed target integration branch. KB-0030
remains READY for repair of the two inherited tests.

## Raw evidence

- `v12_fork_20261115.json`: original PR file sets
- `v12_coexistence_20261115.json`: exact test selectors,
  exit codes, duration and collected counts
- `v12_overlay_local_refs_20261115.json`: local test-only
  branch identities and applied paths
- `b_plus_a_original_v12.log`, `v18_plus_a_regression.log`:
  actual pytest run output
- `*_collect.log`: independent collection counts
- `test_v12_cross_family.py`: distinct semantic invariants
- `run_v12_coexistence.py` and
  `finalize_v12_coexistence.py`: reusable local harness.
