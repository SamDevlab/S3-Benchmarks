# S3 M2.00 Linux Native Performance Campaign

## Purpose

Fill the performance evidence gap left by the Windows M2.00 progress snapshot using a Linux x86-64 VirtualBox guest with a real native C toolchain. This campaign measures performance; it does not reopen T4 certification and it does not reinterpret slow historical tests as compiler failures.

## Immutable comparison boundary

- Baseline S3: `a9e430551f2ee77aa2ef229daf9e967333e83e2c`
- Candidate S3: `a651e9b3551f218af1c27bb908e0692880afc4da`
- Benchmark harness code: `c13f159bb19f13cac9e83e523b6e392baae71738`
- Windows snapshot result: `8523aa53d0a9de095b9c20188d003bc062d8d6d7`
- Result branch: `benchmark/m200-linux-native-performance-20260821`

The executable benchmark checkout must stay pinned to `c13f159bb19f13cac9e83e523b6e392baae71738`. Reports may later be copied into the result branch above; the report-storage commit is not the benchmark harness SHA.

## Environment gate

Before timing, require:

- Linux x86-64 guest;
- `gcc` available;
- `as`, `ld`, and `size` available;
- Python 3.11-compatible environment;
- both S3 source worktrees clean and pinned exactly;
- no benchmark code changes;
- no unrelated load intentionally started during the campaign.

Record VM/host-visible CPU identity, vCPU count, RAM, kernel, Python, GCC/binutils versions and VirtualBox virtualization context. Do not claim bare-metal performance; label the environment as a VM.

## Correctness first

For both baseline and candidate, run `python tools/runner.py --verify-only` before any full timing. Performance from a correctness-failing candidate is invalid.

## JSMN native comparative

Run the existing full native benchmark unchanged for baseline and candidate on the same VM and toolchain. The harness already compares C GCC O0/O2/O3 with S3 O0/O1 and records native process timings, binary size and assembly metrics.

Required reports:

- `reports/lab-m200-linux-jsmn-baseline.json`
- `reports/lab-m200-linux-jsmn-baseline.md`
- `reports/lab-m200-linux-jsmn-candidate.json`
- `reports/lab-m200-linux-jsmn-candidate.md`

Do not alter warmups, repetitions, loop counts, fixtures or compiler flags between baseline and candidate.

## Comparison outputs

At minimum report:

- baseline/candidate S3 O0 median ns/parse;
- baseline/candidate S3 O1 median ns/parse;
- baseline/candidate S3 O1 vs C-GCC-O2 ratio;
- baseline/candidate S3 O1 vs S3 O0 ratio;
- S3 O1 baseline-to-candidate percentage delta;
- ELF file-size delta;
- `.text` size delta;
- fixture completion/blocking counts;
- correctness status for both pins.

Classify each metric as `IMPROVED`, `REGRESSED`, `UNCHANGED_WITHIN_NOISE`, or `UNMEASURED`. Do not infer significance from tiny differences without looking at the benchmark's recorded spread.

## Additional capability characterization

The M1.81-M1.90 smoke and M1.99 hosted characterization may be rerun on Linux for environment completeness, but they remain `CHARACTERIZATION_ONLY` unless a valid equivalent native comparative protocol exists. M1.99 must keep `native_speedup_claim=NO` under its current schema.

## Laboratory policy

Keep these evidence classes separate:

- correctness failure -> correctness issue;
- valid native performance delta -> performance evidence;
- stable expensive test -> test/harness cost;
- VM scheduling variance -> environment confidence issue;
- structural-only result -> capability coverage, not native performance;
- characterization-only timing -> not a speedup claim.

This campaign must not run T4, modify the S3 compiler, merge PR #184, or start M2.01.

## Publication

Generate a machine-readable summary and Markdown report:

- `reports/lab-m200-linux-performance-summary.json`
- `reports/lab-m200-linux-performance-summary.md`

Commit only reports/evidence to `benchmark/m200-linux-native-performance-20260821` after the run. Preserve the exact execution commands and immutable SHAs in the reports.
