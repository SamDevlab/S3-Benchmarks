# S3 Laboratory Testing Policy v1

This policy separates **correctness certification**, **benchmark evidence**, and **test execution cost** so the project does not enter a loop where every slow-but-healthy test becomes a new implementation blocker.

## Core principle

> A test is not a performance regression merely because it is slow, and a benchmark is not a correctness gate merely because it has a timeout.

The laboratory records what the evidence actually proves. It does not force healthy workloads into arbitrary wall-clock budgets.

## Independent evidence planes

The laboratory tracks three independent planes:

1. **Correctness/certification** — semantic failures, differential mismatches, invalid artifacts, reproducibility failures, unsafe behavior, and other explicit correctness contracts.
2. **Performance/benchmarking** — execution time, throughput, memory, code size, tokens/s, compilation cost, and other measured performance properties.
3. **Test/harness cost** — how expensive the verification workload itself is to execute.

A result in one plane must not be silently promoted into another.

Examples:

- a functional assertion failure is a correctness blocker;
- a stable test that passes in 450 seconds is a slow test, not automatically a correctness failure;
- a 300-second watchdog expiring on a workload whose healthy runtime is demonstrably above 300 seconds is evidence of a budget mismatch until evidence shows a hang or regression;
- a characterization benchmark does not become comparative native-performance evidence.

## Timeout interpretation

Timeouts remain truthful outcomes and must never be rewritten as `PASS`. Their interpretation, however, depends on evidence.

Allowed classifications include:

- `UNEXPECTED_TIMEOUT` — runtime should fit the declared budget; investigate;
- `HOST_SCHEDULING_VARIANCE` — host/runtime variance is evidenced;
- `STABLE_EXPENSIVE_TEST` — repeated isolated runs complete successfully but normal runtime is high;
- `AGGREGATE_GATE_BUDGET_TOO_SMALL` — the sum of valid bounded workloads exceeds an aggregate watchdog;
- `POSSIBLE_HANG` — bounded diagnostics cannot establish completion;
- `FUNCTIONAL_REGRESSION` — an actual semantic/assertion failure is observed.

The laboratory must preserve both the raw timeout result and its later classification.

## Do not optimize to satisfy an arbitrary watchdog

The project must not change compiler/runtime behavior merely to make an otherwise healthy test fit a historical timeout.

Performance work is justified when at least one of these is true:

- a benchmark identifies a material regression against a pinned baseline;
- a production workload has an explicit latency/throughput/resource objective;
- algorithmic evidence shows pathological scaling;
- the implementation milestone explicitly targets performance.

Test-only deduplication, fixture reuse, or harness improvements are allowed when they preserve observable coverage and do not hide mutable state or failures.

## Anti-cycle guard

When a gate times out:

1. preserve the original result;
2. classify the timeout with bounded diagnostics;
3. distinguish functional failure from stable execution cost;
4. change production only when production evidence warrants it;
5. do not repeatedly rerun a full certification suite while only investigating execution cost.

A new full certification run should follow a meaningful source/test-runner policy change or an explicit human decision. Diagnostic runs do not replace or erase prior certification evidence.

## Staged testing for future milestones

Future S3 implementation work should be evaluated in stages rather than repeatedly running every expensive test after every small change.

### Stage A — local correctness

Run the smallest deterministic tests that directly cover the changed code. Failures stop promotion.

### Stage B — subsystem integration

Run the relevant T1/T2-style subsystem checks and adjacent contracts. Expensive historical workloads may be deferred to the next appropriate stage when they are unrelated to the change.

### Stage C — targeted benchmark delta

Run benchmark workloads whose measured path is materially affected by the implementation. Compare against an immutable baseline when comparative validity exists; otherwise classify as `CHARACTERIZATION_ONLY`.

### Stage D — cross-subsystem validation

Run the relevant cross-layer/T3-style checks once the implementation is stable.

### Stage E — periodic full campaign

Run the full certification and broad benchmark snapshot at explicit milestone/release checkpoints, not as a reflex after every diagnostic or documentation change.

## Benchmark cadence

For a performance-relevant milestone, preserve:

```text
BASELINE_S3_SHA=<immutable pre-change source>
CANDIDATE_S3_SHA=<immutable candidate source>
BENCHMARK_SHA=<immutable harness source>
WORKLOAD_SCHEMA=<versioned workload contract>
```

Then execute in this order:

```text
correctness gate
-> targeted characterization/comparison
-> implementation analysis
-> focused change
-> targeted rerun
-> broader benchmark only when justified
```

This allows performance evolution to be analyzed in steps without turning the benchmark suite into a release-gate loop.

## Laboratory scoring implications

The scorecard should distinguish at least:

- correctness quality;
- performance quality;
- coverage;
- confidence;
- test/harness execution cost.

A `STABLE_EXPENSIVE_TEST` may be recorded as test-cost/performance debt without reducing correctness quality when its semantic assertions pass. Conversely, a real correctness failure cannot be hidden by good benchmark numbers.

Missing or deferred performance evidence remains unmeasured rather than guessed.

## Historical evidence

Historical raw transcripts, benchmark reports, scorecards, and timeout classifications are immutable evidence. New evidence may supersede a conclusion for a newer source SHA, but must not rewrite what happened in a prior run.
