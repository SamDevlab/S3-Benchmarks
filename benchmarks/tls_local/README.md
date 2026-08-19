# Local TLS Correctness Preflight

This workload verifies the S3 M1.75 async TLS state-machine contract using a deterministic local provider fixture.

## Scope

The current preflight verifies:

- nonblocking `WantRead -> WantWrite -> Ready` handshake progression;
- certificate validation cannot be disabled;
- hostname validation cannot be disabled;
- invalid hostnames are rejected;
- hostname failure closes the owned pending connection;
- certificate failure closes the owned pending connection;
- cancellation closes the owned pending connection exactly once;
- bounded TLS read/write behavior;
- pending then ready TLS I/O progression;
- oversized writes fail with `RESOURCE_LIMIT` before provider I/O;
- client close is idempotent.

No public internet is used. No custom cryptography is implemented in this benchmark.

## Important certification boundary

This is a provider-state-machine correctness gate, not external-chain TLS certification. It does not claim that an OS trust store or production certificate chain was exercised. A later native benchmark must use the vetted TLS provider path and local trusted fixtures while keeping certificate and hostname validation enabled.

## Baseline

`SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`

The runner refuses a different S3 HEAD.

## Run

```bash
S3_CURRENT_REPO=/path/to/S3 python tools/tls_local_runner.py --verify-only
```

Default report:

`reports/tls-local-correctness.json`

## Performance status

`DEFERRED_UNTIL_VETTED_NATIVE_TLS_PROVIDER_IS_BENCHMARKABLE`

Timing the hosted provider-state-machine layer against rustls/OpenSSL/etc. would not be an equivalent benchmark. Native TLS timing starts only after the production provider and local trust fixture are both benchmarkable under the same observable contract.
