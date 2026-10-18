# Native codegen R2 findings

## Root cause and correction

Each hot workload contains two S3 `TSLOAD` sites. The baseline x86-64 lowering copied the slice base and length into `r10`/`r11`, copied the index into `rax`, loaded through scratch registers, then copied the loaded value into its allocated destination. The first resident-register lowering removed all four copies, but allocation often made the destination the same physical register as the index (`mov rdx, [r14 + rdx * 8]`). In an 81-pair run that form regressed `energy_series_aggregation` in `PURE_EXPERIMENTAL` by 2.5%, 4.7%, and 5.2% at small, medium, and full sizes; all three paired intervals excluded 1.0. The failed hypothesis is retained in [its immutable evidence](evidence/r2-20261018/report.md).

The final lowering avoids destination/address aliasing: if the destination aliases the index, it copies the index to `rax`; if it aliases the base, it copies the base to `r10`. It then compares the same unsigned index against the same slice length and takes the same bounds-failure path before loading. Initialization checks, overflow checks, ABI behavior, source, IR, and instruction budgets are unchanged. This keeps three fewer static instructions per `TSLOAD` in the measured alias case, rather than four.

This is a code-generation finding, not a claim that slice checks or the workload algorithms are the primary source of S3's whole-program gap. Bounds and initialization checks are required semantics and remain present. The algorithm/source shape is identical between BASE and CANDIDATE. PMU access was denied (`perf_event_paranoid=4`), so no dynamic instruction or cycle counts are claimed; the alias attribution is supported by the generated assembly contrast and paired timings, not by a hardware-counter explanation.

## Replicated paired measurements

Two independent sessions used the same immutable compiler artifacts, V1 fixture and source hashes, 10 warmups, 81 balanced paired rounds each, and the V1 8/2/1 iterations per size. The combined summary contains 162 matched BASE/CANDIDATE pairs per cell. Ratios below 1.0 favor CANDIDATE; intervals are deterministic 10,000-resample paired bootstrap intervals over per-pair ratios.

| Profile | Workload | Size | BASE median ns/call | CANDIDATE median ns/call | Candidate/BASE | 95% paired CI | Pairs |
|---|---|---:|---:|---:|---:|---:|---:|
| PURE_EXPERIMENTAL | energy_series_aggregation | small | 3006.88 | 2808.12 | 0.919 | [0.896, 0.935] | 162 |
| PURE_EXPERIMENTAL | energy_series_aggregation | medium | 11472.50 | 10322.50 | 0.909 | [0.886, 0.922] | 162 |
| PURE_EXPERIMENTAL | energy_series_aggregation | full | 31350.00 | 28580.00 | 0.907 | [0.896, 0.917] | 162 |
| PURE_EXPERIMENTAL | agent_energy_residual | small | 2681.25 | 2657.50 | 0.992 | [0.982, 1.004] | 162 |
| PURE_EXPERIMENTAL | agent_energy_residual | medium | 9557.25 | 9985.00 | 1.022 | [0.995, 1.055] | 162 |
| PURE_EXPERIMENTAL | agent_energy_residual | full | 26115.00 | 27315.00 | 0.976 | [0.961, 1.014] | 162 |
| PER_INSTRUCTION | energy_series_aggregation | small | 3045.00 | 3019.38 | 1.008 | [0.991, 1.015] | 162 |
| PER_INSTRUCTION | energy_series_aggregation | medium | 11555.00 | 11330.00 | 1.003 | [0.986, 1.010] | 162 |
| PER_INSTRUCTION | energy_series_aggregation | full | 32170.00 | 31535.00 | 1.008 | [0.985, 1.012] | 162 |
| PER_INSTRUCTION | agent_energy_residual | small | 2540.00 | 2338.12 | 0.952 | [0.932, 0.972] | 162 |
| PER_INSTRUCTION | agent_energy_residual | medium | 8630.00 | 8395.00 | 0.977 | [0.956, 0.989] | 162 |
| PER_INSTRUCTION | agent_energy_residual | full | 23585.00 | 23005.00 | 0.983 | [0.964, 1.004] | 162 |

The primary result is repeatable: `energy_series_aggregation` under `PURE_EXPERIMENTAL` is 8.1–9.3% faster across all three sizes, with intervals excluding 1.0. `PER_INSTRUCTION` improves `agent_energy_residual` by 2–5% at small/medium; its full-size interval crosses 1.0. The remaining cells are neutral or uncertain; no universal speedup is claimed. Per-session raw data and build manifests are retained in [session A](evidence/r2-alias-safe-20261018/) and [session B](evidence/r2-alias-safe-replica-20261018/), with the reproducible aggregate at [combined summary](evidence/combined-20261018/summary.json).

## Static size and correctness

- Both workloads have two `TSLOAD` sites. The final form reduces each measured function by six static instructions and 102 assembly bytes. ELF sizes are unchanged; `.text` falls by 18 bytes: 27,791→27,773 bytes for `energy_series_aggregation` and 34,719→34,701 bytes for `agent_energy_residual`. Compile/link times are single-build observations, not statistical claims.
- All 24 revision/profile/workload/size executions matched the V1 oracle. All eight artifact short-output probes returned the expected status 2. A Linux x86-64 native out-of-bounds smoke test still reports `slice index 2 out of bounds`.
- The focused x86-64, slice, register-allocation and R2 aggregation tests pass. The original V1 cross-language matrix and its historical results remain unchanged.

## Next increment

Investigate the remaining instruction and memory-check overhead in reference/slice-heavy generated functions, but first extend the initialization proof with explicit alias/call safety tests. Keep it as a separate hypothesis; do not remove runtime checks without a complete proof. Revisit dynamic profiling only if PMU access becomes available without changing machine-wide settings.
