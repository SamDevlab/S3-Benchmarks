# S3 Benchmark Handoff

## XSBench

The XSBench-compatible baseline lookup subset is functionally qualified on
the pinned S3 compiler and Linux x86-64 guest:

```text
HOSTED_CORRECTNESS=PASS
NATIVE_CORRECTNESS=PASS
FFI_CORRECTNESS=12/12 PASS
FULL_SUITE=52 passed, 1 skipped
S3_SOURCE_CHANGED=NO
```

The existing direct FFI timing completed with Run A and Run B and preserved
raw artifacts, but the prescribed reproducibility rule is open because at
least one control comparison exceeded 25 percent. It is therefore not a
performance qualification and does not justify a global S3 speed claim.

```text
XSBENCH_STATUS=CORRECTNESS_QUALIFIED_TIMING_OPEN
NEXT_PATH=MEASUREMENT_ENVIRONMENT_INVESTIGATION
READY_FOR_MERGE=NO
```

## Boundaries

No S3 compiler, runtime, backend, ABI, or FFI code was changed. No XSBench
source was vendored. No miniBUDE or miniMD implementation or timing was run.
No external PR, merge, tag, release, or shutdown was performed.
