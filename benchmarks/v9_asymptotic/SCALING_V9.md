# S3 V9 — Empirical Big-O Scaling Audit

**Classification: empirical observations, NOT mathematical proof of Big O.**

## Results

| Function | Backend | Hypothesis* | N range | Runtime growth | Effective p, all | Effective p, high | Caution |
|---|---|---|---|---:|---:|---:|---|
| coupled_exchange | A | O(N) | 1000–1000000 (3 points) | 1015.08× | 1.002 | 1.002 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| coupled_exchange | B | O(1) | 1000–1000000 (3 points) | 1.08× | 0.008 | 0.008 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| coupled_exchange | C | O(N) | 1000–1000000 (3 points) | 988.91× | 0.999 | 0.999 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| coupled_exchange | D | O(1) | 1000–1000000 (3 points) | 1.03× | 0.004 | 0.004 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, TIMING_CLOSE_TO_NOISE_FLOOR, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| coupled_exchange | E | O(1) | 1000–1000000 (3 points) | 0.88× | -0.019 | -0.019 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| coupled_exchange | F | O(N) | 1000–1000000 (3 points) | 990.52× | 0.999 | 0.999 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| coupled_exchange | G | O(1) | 1000–1000000 (3 points) | 0.99× | -0.002 | -0.002 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| fib_mod | A | O(N) | 1000–1000000 (3 points) | 1024.79× | 1.004 | 1.004 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| fib_mod | B | O(log N) | 1000–1000000 (3 points) | 2.41× | 0.126 | 0.126 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| fib_mod | C | O(N) | 1000–1000000 (3 points) | 1013.17× | 1.002 | 1.002 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| fib_mod | D | O(log N) | 1000–1000000 (3 points) | 1.98× | 0.096 | 0.096 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| fib_mod | E | O(log N) | 1000–1000000 (3 points) | 2.35× | 0.121 | 0.121 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| fib_mod | F | O(N) | 1000–1000000 (3 points) | 1001.36× | 1.000 | 1.000 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| fib_mod | G | O(log N) | 1000–1000000 (3 points) | 2.15× | 0.108 | 0.108 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| lcg_mod | A | O(N) | 1000–1000000 (3 points) | 1028.41× | 1.004 | 1.004 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| lcg_mod | B | O(log N) | 1000–1000000 (3 points) | 1.69× | 0.075 | 0.075 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| lcg_mod | C | O(N) | 1000–1000000 (3 points) | 1021.74× | 1.004 | 1.004 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| lcg_mod | D | O(log N) | 1000–1000000 (3 points) | 1.71× | 0.077 | 0.077 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| lcg_mod | E | O(log N) | 1000–1000000 (3 points) | 1.80× | 0.085 | 0.085 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| lcg_mod | F | O(N) | 1000–1000000 (3 points) | 1027.11× | 1.004 | 1.004 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| lcg_mod | G | O(log N) | 1000–1000000 (3 points) | 1.77× | 0.083 | 0.083 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, SLOW_GROWTH_AMBIGUOUS_CONSTANT_VS_LOG |
| sum_i2 | A | O(N) | 1000–1000000 (3 points) | 995.17× | 0.999 | 0.999 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| sum_i2 | B | O(1) | 1000–1000000 (3 points) | 1.03× | 0.004 | 0.004 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| sum_i2 | C | O(N) | 1000–1000000 (3 points) | 1024.60× | 1.005 | 1.005 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| sum_i2 | D | O(1) | 1000–1000000 (3 points) | 1.00× | -0.000 | -0.000 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| sum_i2 | E | O(1) | 1000–1000000 (3 points) | 0.88× | -0.019 | -0.019 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| sum_i2 | F | O(N) | 1000–1000000 (3 points) | 982.39× | 0.997 | 0.997 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| sum_i2 | G | O(1) | 1000–1000000 (3 points) | 1.29× | 0.039 | 0.039 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| sum_quasi_parity | A | O(N) | 1000–1000000 (3 points) | 1012.01× | 1.002 | 1.002 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| sum_quasi_parity | B | O(1) | 1000–1000000 (3 points) | 1.01× | 0.001 | 0.001 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| sum_quasi_parity | C | O(N) | 1000–1000000 (3 points) | 987.73× | 0.999 | 0.999 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| sum_quasi_parity | D | O(1) | 1000–1000000 (3 points) | 1.20× | 0.025 | 0.025 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| sum_quasi_parity | E | O(1) | 1000–1000000 (3 points) | 0.87× | -0.019 | -0.019 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| sum_quasi_parity | F | O(N) | 1000–1000000 (3 points) | 998.48× | 1.000 | 1.000 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION |
| sum_quasi_parity | G | O(1) | 1000–1000000 (3 points) | 1.00× | -0.000 | -0.000 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE |
| triangular_cubic | A | O(N) | 1000–10000 (2 points) | 9.83× | 0.993 | 0.993 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, INPUT_RANGE_TOO_NARROW |
| triangular_cubic | B | O(1) | 1000–10000 (2 points) | 1.00× | 0.002 | 0.002 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, INPUT_RANGE_TOO_NARROW |
| triangular_cubic | C | O(N) | 1000–10000 (2 points) | 9.61× | 0.983 | 0.983 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, INPUT_RANGE_TOO_NARROW |
| triangular_cubic | D | O(1) | 1000–10000 (2 points) | 1.00× | -0.001 | -0.001 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE, INPUT_RANGE_TOO_NARROW |
| triangular_cubic | E | O(1) | 1000–10000 (2 points) | 0.95× | -0.021 | -0.021 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, VERY_SHORT_KERNEL_OVERHEAD_DOMINANCE_POSSIBLE, INPUT_RANGE_TOO_NARROW |
| triangular_cubic | F | O(N) | 1000–10000 (2 points) | 9.76× | 0.989 | 0.989 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, INPUT_RANGE_TOO_NARROW |
| triangular_cubic | G | O(1) | 1000–10000 (2 points) | 1.00× | -0.001 | -0.001 | SPARSE_SWEEP_NOT_SUITABLE_FOR_COMPLEXITY_DISCRIMINATION, INPUT_RANGE_TOO_NARROW |

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

## Required follow-up to establish complexity

1. Derive recurrence or operation-count model from the IR and source.
2. Verify domain, checked overflow and fallback paths.
3. Count core operations dynamically and compare with theoretical bounds.
4. Measure new logarithmically spaced N values across a wider valid input domain.
5. For O(1) claims, ensure code does not fall back to a loop for some valid inputs.
6. Independently confirm equivalence for checked-i64 semantics.
7. Compare algorithmic complexity separately from compiler/backend constant factors.

## Sources

- /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks/benchmarks/v8_dual_backend/results_v8_dual_backend.json — accepted 119; skipped 0
