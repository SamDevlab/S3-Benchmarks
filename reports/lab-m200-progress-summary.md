# S3 M2.00 Progress Snapshot

## Provenance

| Item | Value |
| --- | --- |
| Baseline S3 | `a9e430551f2ee77aa2ef229daf9e967333e83e2c` |
| Candidate S3 | `a651e9b3551f218af1c27bb908e0692880afc4da` |
| Benchmark repository | `c13f159bb19f13cac9e83e523b6e392baae71738` |
| Result branch | `benchmark/m200-progress-snapshot-20260821` |

The baseline and candidate were tested through separate clean S3 worktrees.
The benchmark harness ran from a separate clean checkout pinned to the
benchmark SHA above. The S3 source was not changed.

## Environment

- OS: Windows 10 build `10.0.26200`, AMD64
- CPU: AMD Ryzen 5 3400G with Radeon Vega Graphics
- Logical CPUs: 8
- RAM: 15.95 GB
- Python: `3.11.9`
- Git: `2.55.0.windows.2`
- `gcc`, `clang`, and `cc`: unavailable
- Native execution: unavailable for the required Linux x86-64 comparison

Therefore `JSMN_NATIVE_COMPARATIVE=DEFERRED_BY_ENVIRONMENT`. This is a
coverage limitation, not a correctness failure.

## Gate Results

### JSMN

`tools/runner.py --verify-only` passed for both pins:

- baseline: differential correctness PASS, exit `0`;
- candidate: differential correctness PASS, exit `0`.

The native `--full` protocol was not run because the host cannot provide a
valid Linux x86-64 native comparison. No native performance result is claimed.

### M1.81-M1.90 compatibility

`python -m benchmarks.m181_m190.correctness --json` returned exit `0` with:

- `10` checks passed;
- `0` checks failed;
- `1` check deferred: provider-backed signature;
- status `PASS_WITH_DEFERRED`.

`python -m benchmarks.m181_m190.benchmark --smoke` returned exit `0` with
status `PASS_CHARACTERIZATION_ONLY`. It used one warmup and three measured
repetitions per executable check. The reference toolchain was unavailable, so
these timings are not comparative performance evidence.

### M1.99 characterization

`python -m benchmarks.m199.benchmark` returned exit `0` with:

- correctness gate: `PASS`;
- S3 candidate HEAD pin: `a651e9b3551f218af1c27bb908e0692880afc4da`;
- benchmark repository HEAD pin: `c13f159bb19f13cac9e83e523b6e392baae71738`;
- provenance check: `PASS`;
- native execution available: `false`;
- timing class: `CHARACTERIZATION_ONLY`;
- native speedup claim: `NO`.

The controlled comparison was the same parsed `AssemblyProgram` and workload:
OFF used the original program, ON used
`eliminate_redundant_noop_moves(original)`, and timing used the hosted
Emulator. Native x86 generation was only a supplementary structural probe.
The observed hosted medians were:

| Workload | OFF median | ON median |
| --- | ---: | ---: |
| With self-moves | 3,870,100 ns | 3,870,600 ns |
| Without self-moves | 3,540,850 ns | 3,524,450 ns |

These values describe hosted execution only and are not promoted to a native
speedup claim.

## Capability Dimensions

| Dimension | Status | Evidence boundary |
| --- | --- | --- |
| Correctness | `PASS_WITH_DEFERRED` | JSMN, M1.81-M1.90, and M1.99 contracts passed; signature deferred |
| Native/codegen | `PASS_STRUCTURAL_ONLY` | M1.99 structural probe passed; native execution deferred |
| Performance | `DEFERRED_BY_ENVIRONMENT` | No valid native baseline/candidate comparison |
| Runtime/async | `PASS` | Applicable M1.81-M1.90 runtime contracts passed |
| Network/TLS | `STRUCTURAL_ONLY` | HTTP and TLS policy contracts; no certificate handshake fixture |
| Packages/security | `PARTIAL` | Registry/cache contract only |
| Portability | `STRUCTURAL_ONLY` | AArch64 target structure passed; native execution deferred |
| Reproducibility | `PASS` | Reproducibility contract and Git pin checks passed |
| Real world | `UNMEASURED` | No promoted real-world benchmark equivalence harness |
| Test/harness cost | `UNMEASURED` | T4 and full-suite execution were explicitly excluded |

No objective scoring formula was available, so all dimension scores are
`null`. No `IMPROVED` or `REGRESSED` classification is assigned to native
performance metrics that were not measured under a comparable protocol.

## Final Record

```text
BASELINE_S3_SHA=a9e430551f2ee77aa2ef229daf9e967333e83e2c
CANDIDATE_S3_SHA=a651e9b3551f218af1c27bb908e0692880afc4da
BENCHMARK_SHA=c13f159bb19f13cac9e83e523b6e392baae71738
JSMN_CORRECTNESS_BASELINE=PASS
JSMN_CORRECTNESS_CANDIDATE=PASS
JSMN_NATIVE_COMPARATIVE=DEFERRED_BY_ENVIRONMENT
M181_M190_CORRECTNESS=PASS_WITH_DEFERRED
M181_M190_CHARACTERIZATION=PASS_CHARACTERIZATION_ONLY
M199_CORRECTNESS=PASS
M199_CHARACTERIZATION=PASS_CHARACTERIZATION_ONLY
PERFORMANCE_DIRECTION=DEFERRED_BY_ENVIRONMENT
CAPABILITY_DIRECTION=PASS_WITH_DEFERRED
S3_CHANGE=NO
T4_RUNS=0
MERGE=NO
M2.01_STARTED=NO
```

This snapshot is complete with explicit environment deferments. It does not
touch PR #184, execute T4, start M2.01, or make a native speedup claim.
