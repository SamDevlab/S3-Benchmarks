# S3 V9 — Empirical Big-O Scaling Audit

**Classification: empirical observations, NOT mathematical proof of Big O.**

## Results

| Function | Backend | Hypothesis* | N range | Runtime growth | Effective p, all | Effective p, high | Caution |
|---|---|---|---|---:|---:|---:|---|
| fib_mod | A | O(N) | 100–1000000 (9 points) | 6590.99× | 0.975 | 1.045 | — |
| fib_mod | B | O(log N) | 100–1000000 (9 points) | 2.47× | 0.111 | 0.080 | SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| fib_mod | C | O(N) | 100–1000000 (9 points) | 8198.45× | 0.980 | 1.045 | — |
| fib_mod | D | O(log N) | 100–1000000 (9 points) | 2.34× | 0.105 | -0.007 | — |
| fib_mod | E | O(log N) | 100–1000000 (9 points) | 2.86× | 0.127 | 0.099 | SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| fib_mod | F | O(N) | 100–1000000 (9 points) | 8746.75× | 0.978 | 1.058 | — |
| fib_mod | G | O(log N) | 100–1000000 (9 points) | 1.74× | 0.073 | 0.038 | — |
| lcg_mod | A | O(N) | 100–1000000 (9 points) | 6862.60× | 0.963 | 1.090 | — |
| lcg_mod | B | O(log N) | 100–1000000 (9 points) | 1.02× | 0.003 | 0.062 | — |
| lcg_mod | C | O(N) | 100–1000000 (9 points) | 5961.63× | 0.974 | 0.955 | — |
| lcg_mod | D | O(log N) | 100–1000000 (9 points) | 2.80× | 0.107 | 0.034 | — |
| lcg_mod | E | O(log N) | 100–1000000 (9 points) | 2.49× | 0.105 | 0.013 | — |
| lcg_mod | F | O(N) | 100–1000000 (9 points) | 6605.00× | 0.971 | 0.954 | — |
| lcg_mod | G | O(log N) | 100–1000000 (9 points) | 2.06× | 0.090 | 0.041 | — |
| sum_quasi_parity | A | O(N) | 100–1000000 (9 points) | 15692.50× | 0.993 | 1.232 | — |
| sum_quasi_parity | B | O(1) | 100–1000000 (9 points) | 1.66× | 0.018 | 0.216 | SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| sum_quasi_parity | C | O(N) | 100–1000000 (9 points) | 7683.06× | 0.957 | 1.185 | — |
| sum_quasi_parity | D | O(1) | 100–1000000 (9 points) | 1.48× | 0.031 | 0.169 | VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| sum_quasi_parity | E | O(1) | 100–1000000 (9 points) | 0.77× | -0.034 | -0.020 | VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| sum_quasi_parity | F | O(N) | 100–1000000 (9 points) | 17178.60× | 1.036 | 1.182 | — |
| sum_quasi_parity | G | O(1) | 100–1000000 (9 points) | 0.97× | -0.011 | 0.133 | SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |

*Algorithmic hypotheses come from the known loop vs closed-form/matrix-exponentiation structure, NOT from time fitting. The A/C/F family uses an N-step loop; B/D/E/G use a closed form for polynomial/quasi-polynomial functions and logarithmic repeated squaring for modular LCG/Fibonacci.*

The observed p is a log-log slope (d log time / d log N), not a proof.
For finite n, constant call overhead, caches, loop setup and noise can dominate.

## Interpretation guide

- An O(N) loop typically tends toward p≈1 when the measured cost is dominated by the loop.
- A closed-form O(1) kernel tends toward p≈0 in a fixed-word model.
- O(log N) may also have p near 0 over limited inputs; distinguish via source-level structure and broader sweeps.
- O(N²) tends toward p≈2 only when n² work dominates, which is not established by this suite.
- For a numeric value N represented in L bits, O(log N)=O(L), O(N)=O(2^L); unbounded integer arithmetic has additional bit complexity.

## Caveats

- Big O CANNOT be inferred or formally proved from runtime measurements alone.
- All complexity hypotheses assume unit-cost fixed-width integer arithmetic and valid in-domain N.
- With finite i64 inputs, these are idealized algorithm families, not a literal N -> infinity claim.
- For arbitrary-precision inputs, bit complexity must also account for operand widths and multiplication.
- A measured effective exponent is not an asymptotic proof, especially with 3 data points.
- Constant-time or logarithmic kernels can be dominated by invocation overhead in this range.
- C handwritten formulas (D) can have different checked-overflow semantics from S3/GCC auto code (E).
- Only comparable inputs, correctness status, CPU, compiler flags and measurement scopes may be compared.
- Predictive fast-path O(1)/O(log N) estimates are CONDITIONAL; a guarded fallback can remain O(N).
- Global worst-case complexity across all valid inputs has NOT been established.

## Required follow-up to establish complexity

1. Derive recurrence or operation-count model from the IR and source.
2. Verify domain, checked overflow and fallback paths.
3. Count core operations dynamically and compare with theoretical bounds.
4. Measure new logarithmically spaced N values across a wider valid input domain.
5. For O(1) claims, ensure code does not fall back to a loop for some valid inputs.
6. Independently confirm equivalence for checked-i64 semantics.
7. Compare algorithmic complexity separately from compiler/backend constant factors.

## Sources

- /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks/benchmarks/v9_asymptotic/results_v9_dense_scaling.json — accepted 189; skipped 0
