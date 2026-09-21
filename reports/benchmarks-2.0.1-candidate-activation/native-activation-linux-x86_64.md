# Native Activation Evidence

- Host: `s3-vm`, Linux x86-64
- S3 candidate: `e07d0b5464bf472b2ca18993f3e196a234ff0fc5`
- Cases attempted: 32
- `NATIVE_PASS`: 32
- `NATIVE_FAIL`: 0
- `NATIVE_BLOCKED`: 0
- `NATIVE_EXECUTION`: `PASS`
- `NATIVE_OBSERVABLE`: `CANARY`
- Timing recorded: no
- Native speedup claim: no

The workload source still performs its calculation in `f64`. For native
qualification only, the adapter generates a separate entry-point wrapper that
returns the integer canary `1` exactly when the calculated result matches the
independent Python oracle value. This avoids requiring standalone native
decimal-f64 printing while preserving the workload operations.

The first native attempt, before this canary protocol was applied, is retained
as `native-activation-linux-x86_64-initial-blocked.json` and recorded 32
instances of the same decimal-f64 output limitation. It is historical
evidence, not the final qualification result.

Final raw JSON: `native-activation-linux-x86_64.json`.

- Final raw SHA-256: `978f02e152fffb1ddde36e666a1bc6f1c8b89249963b9700db49a20cc2d33d0d`
- Final raw size: 16076 bytes
- Initial blocked raw SHA-256: `3ee07223cdf66f2d2fe6085ecbb097a94569c75b7992d3fa54781e2c83bb49ae`
