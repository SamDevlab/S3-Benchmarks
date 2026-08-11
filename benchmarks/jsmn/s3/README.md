# S3 JSMN Implementation

- **Source Repository**: [`SamDevlab/S3`](https://github.com/SamDevlab/S3)
- **Branch**: `experiment/jsmn-s3-20260810`
- **Pinned Commit SHA**: `85541b782571c80d4857d013d1fb25b4997c1eb9`
- **Source File**: `examples/external/jsmn/jsmn_demo.s3`

## Kernel Constraints & Properties

```text
JSMN_S3_DROP_IN_API=NO
JSMN_S3_INCREMENTAL_PARSER=NO
JSMN_S3_RUNTIME_TOKEN_CAPACITY=NO
JSMN_S3_LARGE_INPUT=NO
JSMN_S3_C_ABI=NO
JSMN_S3_NATIVE_KERNEL=YES
JSMN_S3_O0_NATIVE=YES
JSMN_S3_O1_NATIVE=YES
RA_SEPARATE_SWITCH=UNAVAILABLE
```

The S3 implementation is a fixed-capacity, zero-allocation tokenization kernel designed for inputs up to 96 bytes (`tryte[96]`) and up to 32 tokens (`token_*[32]`).
It exhibits 100% behavioral parity with upstream `zserge/jsmn` default non-strict parsing contract.
