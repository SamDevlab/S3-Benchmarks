# Native Activation Evidence

- Host: `s3-vm`, Linux x86-64
- S3 candidate: `e07d0b5464bf472b2ca18993f3e196a234ff0fc5`
- Cases attempted: 32
- `NATIVE_PASS`: 0
- `NATIVE_FAIL`: 0
- `NATIVE_BLOCKED`: 32
- Timing recorded: no
- Native speedup claim: no

All cases stopped at the same standalone-runtime output boundary:

```text
NativeBackendError: native entry function 'main' cannot return f64 until the standalone runtime provides decimal float output
```

Classification: `TRUE_BACKEND_CAPABILITY_BLOCKER` at the native standalone
decimal-`f64` output protocol. This is not evidence of a source-language
correctness failure. The raw JSON transcript is preserved beside this report
as `native-activation-linux-x86_64.json`; its SHA-256 is
`3ee07223cdf66f2d2fe6085ecbb097a94569c75b7992d3fa54781e2c83bb49ae` and its
size is 11092 bytes.
