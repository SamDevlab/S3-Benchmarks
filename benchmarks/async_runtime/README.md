# S3 Async Runtime Benchmark Preflight

This workload is the first executable candidate from the post-M1.80 benchmark corpus.

It currently provides **correctness verification only** for S3 M1.71-M1.76. It does **not** publish async performance numbers yet.

## Why correctness-only first?

The repository-wide rule remains:

> **CORRECTNESS BEFORE PERFORMANCE.**

S3 now has source-visible async/await, a deterministic hosted state-machine model, a bounded cooperative executor, and bounded channels. However, a fair performance comparison requires an equivalent native S3 workload plus a clearly defined external reference implementation. Timing the hosted Python model against Tokio or another native runtime would be methodologically invalid.

Therefore the current gate locks the semantics that a later native benchmark must preserve.

## Covered contracts

The gate verifies:

- deterministic `async fn` / `await` lowering and observable IR result;
- `Pending -> Ready` future progression;
- fail-closed lexical borrow across suspension;
- exactly-once owned-frame cleanup on cancellation;
- bounded executor batch completion;
- explicit wake after a suspended task;
- bounded-channel backpressure;
- message ownership transfer only after successful send;
- deterministic source-order `select` tie handling;
- closed-channel send failure without consuming message ownership.

## S3 baseline

The initial preflight is pinned conceptually to:

`SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`

CI checks out that exact S3 commit separately from the historical JSMN benchmark pin.

## Run

```bash
S3_CURRENT_REPO=/path/to/S3 python tools/async_runtime_runner.py --verify-only
```

Windows PowerShell:

```powershell
$env:S3_CURRENT_REPO = "C:\path\to\S3"
python tools/async_runtime_runner.py --verify-only
```

Default report:

`reports/async-runtime-correctness.json`

## Performance status

`DEFERRED_UNTIL_EQUIVALENT_NATIVE_WORKLOAD_EXISTS`

A later performance campaign may be promoted only after all of the following exist:

1. a native S3 async workload with equivalent observable semantics;
2. a pinned external reference implementation;
3. deterministic correctness fixtures;
4. differential equivalence before timing;
5. amortized process/runtime startup where applicable;
6. clearly separated hosted, structural, and native measurements.

Likely first performance kernels are bounded task completion and bounded channel ping-pong. Reactor/network/TLS benchmarks should follow only after their own local-fixture correctness gates exist.
