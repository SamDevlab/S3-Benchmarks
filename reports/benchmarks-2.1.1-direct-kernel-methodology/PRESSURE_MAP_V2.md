# Pressure Map V2

This report separates measurement confounders from S3 runtime bottlenecks.

| Pressure | Classification | Evidence |
| --- | --- | --- |
| Process startup/runtime initialization | PENDING_NATIVE_PILOT | Native K-scaling was not available on this host. |
| Static code/stack operation density | UNRESOLVED_NATIVE_DEFERRED | No comparable amortized/native kernel data yet. |
| Measurement variability | UNRESOLVED_NATIVE_DEFERRED | Run A/B requires a controlled Linux x86-64 host. |

The hosted pilot correctness gate passed independently for the generated K
levels. That is not a native performance result and does not authorize an S3
optimization campaign.
