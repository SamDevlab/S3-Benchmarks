# MoneyPrinterTurbo-Inspired Provider Pipeline Preflight

This workload is a compact **integration correctness** benchmark shape inspired by the provider-registry/service-layer architecture in `harry0703/MoneyPrinterTurbo`.

It is **not** a port of MoneyPrinterTurbo, does not call real AI providers, and does not require API keys or public internet.

## Reference

Pinned reference:

`harry0703/MoneyPrinterTurbo@d4c0e45da4ac0889af77f7307f52f9d5d4f74942`

The useful idea copied at the architectural level is the separation between:

- stable provider metadata/identity;
- adapter selection;
- configuration loading;
- service execution.

No MoneyPrinterTurbo source code is vendored into this benchmark.

## Pipeline

The bounded workload is:

```text
config.json
    ↓
S3 CrossPlatformOSServices read
    ↓
provider registry lookup by stable ID
    ↓
model/default resolution
    ↓
S3 async DNS fixture
    ↓
S3 async network connect
    ↓
S3 async TLS handshake
    ↓
deterministic HTTP-like request envelope
    ↓
local fixture provider response
    ↓
response parse
    ↓
S3 CrossPlatformOSServices write
    ↓
deterministic result file
```

## S3 surfaces exercised

- M1.66 cross-platform OS services: bounded relative file read/write;
- M1.74 async network: deterministic DNS + pending-resource connect;
- M1.75 async TLS: nonblocking handshake/read/write and mandatory secure defaults;
- explicit cleanup of TLS session and network handle.

The lower-level package/cache/reproducibility gate remains separate in `benchmarks/package_repro`; this application workload does not invent a package-install step just to increase feature count.

## Correctness contracts

The gate checks:

- provider selection is by stable provider ID;
- registry order is deterministic;
- blank model configuration resolves to the provider default;
- explicit model configuration overrides the default;
- unknown providers fail before network activity starts;
- DNS stays local and deterministic;
- network connect progresses `Pending -> Ready` with exact resource ownership;
- TLS progresses `Pending -> Ready` and keeps certificate/hostname validation enabled;
- request and result bytes are deterministic across different JSON key insertion order;
- response parsing produces the expected deterministic result;
- output is written and read back through S3 OS services;
- `../` output escape is rejected;
- TLS and network resources are cleaned up even after a late output-path failure.

## Important limitation: JSON

S3 M1.71-M1.80 does not expose a general JSON runtime used by this workload. The first provider-pipeline gate therefore uses Python's JSON parser/serializer **inside the benchmark harness**.

The report marks this explicitly as:

`python_benchmark_harness_not_s3_runtime_feature`

Do not use this gate as evidence that S3 has a production JSON library.

## Run

```bash
S3_CURRENT_REPO=/path/to/S3 python tools/provider_pipeline_runner.py --verify-only
```

Default report:

`reports/provider-pipeline-correctness.json`

Required S3 baseline:

`SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`

The runner also verifies the pinned MoneyPrinterTurbo reference SHA in `references/upstreams-m171-m180.json`.

## Security / isolation

- public internet: **not required**;
- real AI provider calls: **none**;
- API keys/secrets: **none**;
- TLS certificate validation: **required**;
- TLS hostname validation: **required**;
- shell execution: **not used** in V1.

The process-invocation step from the original candidate plan remains optional and is intentionally omitted here because it adds no useful semantic coverage to the first provider pipeline.

## Performance status

`DEFERRED_UNTIL_EQUIVALENT_NATIVE_S3_APPLICATION_WORKLOAD_EXISTS`

This hosted integration preflight must not be timed against native MoneyPrinterTurbo/Python or native provider SDKs and presented as S3 application performance. A future performance campaign requires an equivalent native S3 application path first.
