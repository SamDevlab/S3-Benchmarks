# Reactor + Local Network Correctness Preflight

This workload verifies the S3 M1.73/M1.74 reactor and async-network contracts without requiring public internet access.

## Scope

The current preflight uses a deterministic local provider fixture, not public sockets or public DNS. It verifies:

- deterministic reactor readiness ordering;
- wake coalescing and cleanup after registration close;
- TCP-like connect with pending-resource identity preservation;
- pending then ready write/read progression;
- idempotent handle close and bounded active-handle accounting;
- UDP send/receive ordering through the S3 async-network surface;
- deterministic local DNS fixture resolution;
- cancellation cleanup for a pending owned resource;
- network handle resource-limit failure and cleanup.

M1.74 V1 exposes UDP operations but does not expose a separate public UDP-socket constructor. The fixture therefore bootstraps one generic network handle through the provider connect hook and then exercises only `udp_send` / `udp_receive`. That limitation is recorded rather than hidden.

## Baseline

`SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`

The runner refuses a different S3 HEAD.

## Run

```bash
S3_CURRENT_REPO=/path/to/S3 python tools/network_loopback_runner.py --verify-only
```

Default report:

`reports/network-loopback-correctness.json`

## Performance status

`DEFERRED_UNTIL_NATIVE_REACTOR_ADAPTER_IS_BENCHMARKABLE`

The deterministic hosted/provider model is a correctness oracle, not a valid throughput/latency comparator against Mio, Tokio, or libuv. Native timing should be promoted only after S3 has a native reactor/socket adapter with equivalent semantics.
