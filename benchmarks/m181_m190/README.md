# M1.81-M1.90 Executable Campaign

This is a local, correctness-first campaign branch. It does not replace the
JSMN runner and it does not publish benchmark results.

## Execution contract

Every check compares an observable result with an independent deterministic
reference contract before timing. Set `S3_REPO` to the exact S3 campaign
checkout; the harness refuses the historical runner fallback. `S3_COMMIT` is
recorded as metadata and should be set to the exact candidate SHA.

```powershell
$env:S3_REPO = 'C:\path\to\S3-m181-m190-autonomous-20260819'
$env:S3_COMMIT = '25b8e53231917b4c0b4f4b676f8ea71b9a2802e9'
python -m benchmarks.m181_m190.correctness --json
python -m benchmarks.m181_m190.benchmark --smoke
```

The smoke runner uses `time.perf_counter_ns`, one warmup, and at most ten
repetitions. Its measurements are `CHARACTERIZATION_ONLY`: no pinned Rust,
Tokio, rustls, Cargo, or uv executable reference is vendored or assumed.

## Campaigns

| Campaign | Correctness observable | Timing state on this branch |
|---|---|---|
| async task | value, poll count, suspension/completion states | eligible for local characterization |
| await chain | final value and compiled async function count | eligible for local characterization |
| channels | FIFO order, count, checksum, and close state at capacities 1/8/64 | eligible for local characterization |
| executor | sorted values, one poll/task, empty task set | eligible for local characterization |
| process I/O | stdout, stderr, exit code | eligible for local characterization |
| HTTP loopback | status, body, body digest | eligible for local characterization |
| registry/cache | verified digest and first/second cache state | eligible for local characterization |
| reproducibility | repeated bundle SHA and size | eligible for local characterization |
| TLS | certificate-required and hostname-checked policy | structural only; no local cert fixture |
| Ed25519 | real provider-backed signature verdict | deferred when `cryptography` is absent |
| AArch64 | target identity and bounded structural artifact | structural only on Windows |

No result is comparative performance evidence until a matching reference
toolchain and an equivalent workload are pinned. Public network services are
never correctness fixtures.
