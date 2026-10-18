# Native S3 codegen R2 experiment

This companion experiment isolates the x86-64 slice-load lowering change without
rewriting or rerunning the V1 cross-language matrix.

## Design

- BASE is the immutable PR #333 compiler revision before this change; its parent
  is the pinned V6 baseline.
- Candidate ancestry is recorded exactly; the final candidate includes the
  initial resident-load lowering and its alias-safe follow-up. Do not rewrite
  or rebase the experiment commits.
- Each revision is built at O1 in `PURE_EXPERIMENTAL` and `PER_INSTRUCTION`.
- The six-workload V1 corpus is reused, but timing is limited to
  `energy_series_aggregation` and `agent_energy_residual`, at the existing
  small/medium/full sizes and fixture seed.
- Every BASE/CANDIDATE pair uses the same fixture, input size, profile and
  iteration count. Pair order is randomized and balanced over the sample window.
- `--order-seed` can vary ordering across repeat sessions without changing the
  fixture seed or source inputs.
- Correctness and short-output rejection run before timing. The timed region
  remains the V1 `CLOCK_MONOTONIC_RAW` kernel-only loop.
- The default run is 7 warmup pairs and 41 measured pairs for each of 12 cells
  (492 matched observations; 984 timed processes). Iterations remain 8/2/1 for
  small/medium/full to respect the existing instruction cap and V1 protocol.
- Compiler source archives, compiler commits/parents, V1 input archive and
  source-file hashes, the paired runner hash, fixture/artifact hashes, raw
  samples, build time, `.text`, ELF size and static disassembly counts are
  recorded. Static counts are not presented as dynamic counts.
- If PMU access is denied, the manifest records that state and the report makes
  no dynamic instruction/cycle claim.

## Reproduction

Run on the pinned Linux x86-64 VM with GCC, `taskset`, Python and the V1 runner
dependencies. Keep generated files under `/dev/shm`; the VM root disk may be
full. Prepare two source-only trees from immutable Git revisions:

```sh
BASE=87c0a5be070210f158313a4d272fbdd795536232
CANDIDATE=94ef25f2fca720931df0f7bb97ff0b26e0d4bab7
CANDIDATE_PARENT=6e3881d6ff6066e6828d143e08adbf030542dd16
V1_INPUTS_ARCHIVE_SHA=02851e164c4e9e8b1ff207b396227394d504caf77c45db1b6e816d28453f5191
S3_REPO=/path/to/S3
mkdir -p /dev/shm/s3-r2-source-base /dev/shm/s3-r2-source-candidate
git -C "$S3_REPO" archive --format=tar "$BASE" bootstrap/s3 | tar -xf - -C /dev/shm/s3-r2-source-base
git -C "$S3_REPO" archive --format=tar "$CANDIDATE" bootstrap/s3 | tar -xf - -C /dev/shm/s3-r2-source-candidate
BASE_ARCHIVE_SHA=$(git -C "$S3_REPO" archive --format=tar "$BASE" bootstrap/s3 | sha256sum | cut -d' ' -f1)
CANDIDATE_ARCHIVE_SHA=$(git -C "$S3_REPO" archive --format=tar "$CANDIDATE" bootstrap/s3 | sha256sum | cut -d' ' -f1)
python3 benchmarks/native-pure-controlled-r2/paired_codegen.py \
  --baseline-repo /dev/shm/s3-r2-source-base \
  --candidate-repo /dev/shm/s3-r2-source-candidate \
  --baseline-revision "$BASE" \
  --candidate-revision "$CANDIDATE" \
  --baseline-parent 2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c \
  --candidate-parent "$CANDIDATE_PARENT" \
  --baseline-archive-sha256 "$BASE_ARCHIVE_SHA" \
  --candidate-archive-sha256 "$CANDIDATE_ARCHIVE_SHA" \
  --v1-inputs-archive-sha256 "$V1_INPUTS_ARCHIVE_SHA" \
  --output /dev/shm/s3-native-r2-paired-results \
  --samples 81 --warmups 10 --iterations 1 --order-seed 20261018
```

To combine independent sessions without losing the pairing or accepting
artifact drift:

```sh
python3 benchmarks/native-pure-controlled-r2/combine_sessions.py \
  --session benchmarks/native-pure-controlled-r2/evidence/r2-alias-safe-20261018 \
  --session benchmarks/native-pure-controlled-r2/evidence/r2-alias-safe-replica-20261018 \
  --output /dev/shm/s3-r2-combined.json --seed 20261018
```

For archive transport between host and VM, compute each SHA-256 before and
after transfer and preserve both values with the run output. The script refuses
to overwrite a nonempty output directory. It does not modify compiler defaults,
push code, publish benchmark artifacts, or mutate PR history.

## Evidence

The V1 report and measurements remain authoritative for the original
cross-language comparison. R2 evidence belongs in this directory and must be
copied from the VM only after every paired cell and validation gate completes.
See [FINDINGS.md](FINDINGS.md) for the alias-safety result and combined paired
table. The session combiner verifies evidence-index hashes, raw pair
completeness/orientation, artifact and assembly hashes, and matching BASE /
CANDIDATE identities before it bootstraps across sessions.
