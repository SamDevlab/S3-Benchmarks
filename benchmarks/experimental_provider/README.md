# Experimental External Provider Bridge

This directory reserves a **non-normative** benchmark path for external compute
providers without changing the S3 language benchmark baselines.

The goal is to measure integration boundaries first: process/FFI overhead,
deterministic correctness, provider throughput, and eventually CPU/GPU engines.
It is intentionally separate from the JSMN benchmark and from release gates.

## Safety and scope

The committed workloads use only public deterministic vectors and synthetic
inputs. This repository does not ship wallet scanning, private-key recovery,
target-address search, or a Bitcoin puzzle solver.

The disabled `secp256k1` entry exists only to reserve the provider protocol for
a public known vector. It is opt-in and excluded from default runs.

## Provider contract

Set `S3BENCH_EXPERIMENTAL_PROVIDER` to an executable or Python file, or pass
`--provider PATH`. The runner invokes it without a shell:

```text
provider --benchmark-id ID --input-id INPUT --loops N
```

A successful provider must exit with status 0 and emit exactly one:

```text
checksum=<deterministic value>
```

It may also emit:

```text
kernel_ns=<non-negative integer>
provider_role=<free-form label>
```

If `kernel_ns` is present, throughput uses the provider-reported kernel region;
otherwise it uses the complete process invocation.

## Commands

The bundled provider is a protocol fixture, not a performance reference:

```bash
python tools/experimental_provider_runner.py --list
python tools/experimental_provider_runner.py --verify-only
python tools/experimental_provider_runner.py --smoke
```

Use an external provider:

```bash
S3BENCH_EXPERIMENTAL_PROVIDER=/path/to/provider \
python tools/experimental_provider_runner.py --full
```

Run the disabled public secp256k1 integration vector explicitly:

```bash
python tools/experimental_provider_runner.py \
  --benchmark experimental.crypto.secp256k1.public-vector.v1 \
  --include-disabled \
  --verify-only
```

## Future S3 integration

A future S3-side benchmark can keep this same protocol while changing the
provider implementation to:

```text
S3 program -> S3 FFI -> C/Rust provider -> CPU/GPU engine
```

That lets the benchmark report provider throughput separately from S3-to-FFI
overhead and avoids making any cryptographic engine a dependency of S3 itself.
