# S3 Laboratory Evidence Bridge

The S3 Laboratory consumes benchmark evidence; it does not replace benchmark runners and it does not manufacture benchmark results.

The division of responsibility is intentional:

```text
S3 implementation
      |
      v
S3-Benchmarks
(objective evidence)
      |
      v
S3 Laboratory
(versioned rubric + scorecard)
```

## Core rule

A laboratory score must be traceable to immutable evidence. If evidence is unavailable, the score for that metric is `null`/not measured rather than guessed.

Every scored metric should expose three independent dimensions:

- **score** — quality demonstrated by available evidence, 0..100 or `null`;
- **coverage** — how much of the intended capability has actually been exercised, 0..1;
- **confidence** — strength of evidence (`HIGH`, `MEDIUM`, `LOW`, `UNRATED`).

`DEFERRED_BY_ENVIRONMENT` should lower coverage/confidence where appropriate, but it is not automatically a zero quality score.

## Testing and benchmark policy

[`testing-policy-v1.md`](testing-policy-v1.md) and [`testing-policy-v1.json`](testing-policy-v1.json) define the laboratory's anti-cycle and staged-testing contract.

The policy explicitly separates:

- correctness/certification;
- performance benchmarking;
- test/harness execution cost.

A stable test that passes but takes a long time is not automatically a correctness regression. A watchdog timeout remains a truthful timeout result, but if bounded evidence shows the healthy workload normally exceeds that watchdog, the laboratory records a budget mismatch or stable-expensive-test classification instead of forcing production changes solely to make the test fit an arbitrary wall-clock margin.

Future implementation campaigns should proceed in stages: focused correctness, subsystem integration, targeted benchmark delta, cross-subsystem validation, and only then periodic full campaigns at explicit milestone/release checkpoints. Expensive full suites should not be reflexively rerun after every diagnostic or documentation-only change.

## Rubric

[`rubric-v1.json`](rubric-v1.json) defines the initial weighted axes:

- correctness;
- native/codegen;
- performance;
- runtime/async;
- network/TLS;
- packages/security;
- portability;
- reproducibility;
- real-world workloads.

Weights are policy, not benchmark measurements. Changing them requires a new rubric version so historical scorecards remain comparable.

## Scorecard contract

[`scorecard-v1.schema.json`](scorecard-v1.schema.json) defines the machine-readable scorecard envelope.

Each evidence reference should bind, when available:

- S3 commit SHA;
- S3-Benchmarks commit SHA;
- upstream commit or data/model digest;
- workload/schema id;
- result classification;
- result digest or immutable artifact identity.

A benchmark classified as `CHARACTERIZATION_ONLY` may contribute capability/coverage evidence but must not be converted into a native performance win.

Test/harness cost should be recorded separately from implementation quality. For example, `STABLE_EXPENSIVE_TEST` may become performance/test-cost debt while correctness remains supported by passing semantic assertions. A real correctness failure, however, can never be hidden by good timing numbers.

## Historical trend

The laboratory may store one scorecard per certified campaign/milestone, for example M1.80, M1.90, M2.00 and M2.10. Trend analysis should compare score, coverage and confidence separately.

This makes it possible to answer both:

- "Did S3 improve?"
- "Did we simply test more of it?"

without confusing broader coverage with better implementation quality.

For performance-relevant milestones, the laboratory should also preserve an immutable pre-change baseline and candidate SHA and compare only workloads materially affected by the implementation before deciding whether a broader benchmark rerun is justified.

## LLM readiness

The real-world corpus can feed an LLM-readiness view without pretending S3 already provides native inference. Suitable metrics include:

- local LLM client integration;
- JSON/SSE streaming;
- async backpressure/cancellation;
- filesystem/model-loading capability;
- large-buffer behavior;
- f32/f64/native compute coverage;
- SIMD/threading coverage;
- native inference correctness/performance when it eventually becomes eligible.

Until a true S3-native equivalent inference workload exists, `llama.cpp` remains reference/integration evidence and native LLM performance remains deferred.

## No automatic grade inflation

A laboratory consumer must not:

- convert `DEFERRED` to PASS;
- convert `CHARACTERIZATION_ONLY` to native comparative evidence;
- infer scores from missing benchmarks;
- drop failed correctness gates from the denominator silently;
- treat a stable expensive test as a compiler regression without production evidence;
- repeatedly rerun full certification solely to chase execution-time budgets;
- rewrite historical scorecards when the rubric changes.
