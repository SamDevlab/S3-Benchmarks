# XSBench Capability Matrix

| Capability | Classification | Evidence |
|---|---|---|
| f64 arithmetic | REUSE_DIRECTLY | hosted and native fixture results |
| i64 arithmetic/counts | REUSE_DIRECTLY | metadata and lookup accounting |
| loops and conditionals | REUSE_DIRECTLY | source contract and hosted matrix |
| nested lookup control | REUSE_DIRECTLY | TINY/SMALL/MEDIUM correctness |
| flat indexed data | ADAPT_EXISTING_CONTRACT | explicit metadata/data layout |
| binary search | ADAPT_EXISTING_CONTRACT | upstream search invariant retained |
| interpolation | REUSE_DIRECTLY | independent oracle parity |
| borrowed/read-only slices | REUSE_EXISTING_FFI | common driver |
| exported f64 kernel | REUSE_EXISTING_FFI | 12/12 FFI correctness points |
| struct representation | ADAPT_EXISTING_CONTRACT | parallel flat arrays |
| S3 compiler/backend blocker | NONE | no S3 source change |

```text
TRUE_LANGUAGE_BLOCKERS=NONE
TRUE_RUNTIME_BLOCKERS=NONE
TRUE_BACKEND_BLOCKERS=NONE
S3_SOURCE_CHANGED=NO
```
