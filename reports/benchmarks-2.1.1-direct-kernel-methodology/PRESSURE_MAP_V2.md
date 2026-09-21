# Pressure Map V2

This report separates measurement confounders from S3 runtime bottlenecks.

| Pressure | Classification | Evidence |
| --- | --- | --- |
| Process startup/runtime initialization | HOSTED_PILOT_COMPLETE_NATIVE_KERNEL_DEFERRED | Linux x86-64 hosted K-scaling replay passed. |
| Static code/stack operation density | UNRESOLVED_NO_DIRECT_KERNEL_TIMER | The pinned S3 source exposes no callable kernel ABI or internal timer. |
| Measurement variability | UNRESOLVED_NO_REPEATED_TIMING_PROTOCOL | No Run A/B timing protocol was executed. |

The hosted pilot correctness gate passed independently for the generated K
levels. That is not a native performance result and does not authorize an S3
optimization campaign.
