# M1.81-M1.90 Executable Campaign

This is a correctness-first benchmark campaign for the merged S3 M1.81-M1.90 line. It does not replace the JSMN runner and it does not publish comparative benchmark claims by itself.

## Immutable corpus

- canonical merged S3 baseline: `a9e430551f2ee77aa2ef229daf9e967333e83e2c`
- reviewed/tested PR #183 head: `8742010f7c7a7956733dd35fabb6a6ef731d0b0b`
- historical benchmark campaign commit: `fbf53a0eb8cf39ed0245438b6b47dfde63658b20`
- external references: [`../../references/upstreams-m181-m190.json`](../../references/upstreams-m181-m190.json)
- machine-readable workload corpus: [`corpus.json`](corpus.json)
- promotion plan: [`../../candidates/m181-m190/README.md`](../../candidates/m181-m190/README.md)

The historical benchmark evidence is preserved, but the merged S3 `BENCHMARK_APPLICABILITY.md` records that post-review source hardening requires focused correctness/smoke reruns before previous characterization is attributed to the newer source line. Therefore the canonical merge is a **new measurement baseline**, not an alias for the historical run.

## Execution contract

Every check compares an observable result with an independent deterministic reference contract before timing. Set `S3_REPO` to a checkout of the exact canonical merge and record the same SHA in `S3_COMMIT`.

```powershell
$env:S3_REPO = 'C:\path\to\S3-m181-m190-merged'
$env:S3_COMMIT = 'a9e430551f2ee77aa2ef229daf9e967333e83e2c'
python -m benchmarks.m181_m190.correctness --json
python -m benchmarks.m181_m190.benchmark --smoke
```

Before results are published for this baseline, the runner should additionally enforce the checkout HEAD against the corpus SHA rather than relying only on metadata.

The smoke runner uses `time.perf_counter_ns`, one warmup, and at most ten repetitions. Measurements remain `CHARACTERIZATION_ONLY` until an equivalent workload and pinned executable reference toolchain exist.

## Current harness coverage

| Harness check | Observable | Corpus action |
|---|---|---|
| `async_task` | value, poll count, suspension/completion states | repin + rerun |
| `await_chain` | final value and compiled async function count | expand Future/generic/module cases |
| `channels` | FIFO/count/checksum/close at capacities 1/8/64 | repin + rerun |
| `executor` | values, poll count, empty task set | add final M1.83 concurrency regressions |
| `process_io` | stdout/stderr/exit | add timeout/overflow kill+reap and filesystem cases |
| `http_loopback` | status/body/digest | add global deadline and ASCII-boundary hardening cases |
| `registry_cache` | verified digest/cache state | add canonical-origin and corruption cases |
| `reproducibility` | repeated bundle SHA/size | upgrade to final M1.90 RC matrix verification |
| `tls_policy` | certificate-required + hostname-check policy | add real local trusted/untrusted/hostname fixtures |
| `signature` | provider-backed Ed25519 verdict | run where `cryptography` is present; otherwise DEFERRED |
| `aarch64_structure` | Linux AArch64 target + structural artifact | expand typed AAPCS64 and add macOS ARM64 corpus |

## Evidence rules

- Public network services are never correctness fixtures.
- Missing optional crypto provider is `DEFERRED`, not PASS.
- Structural ARM64 evidence is not native execution evidence.
- Historical characterization is never silently repinned to a newer S3 commit.
- No comparative performance result is valid before differential/equivalence correctness passes on both S3 and the pinned reference implementation.
