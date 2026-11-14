# S3 V5.5 Psychohistory & Discovery Benchmark Suite

Generated cleanly on Linux (`WSL`, Python `3.12.3`, GCC `-O3 -march=native`) using `S3` `O1` native ELF shared libraries (`scientific` 50M budget).

## 1. Automatic Pattern Discovery (`O(T)` Default vs `O(1)` Discovered Lowered)

| Kernel | T | Default ms | Discovered Opt ms | Speedup | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| `sum_triangular` | 10 | 0.00110 | 0.00100 | 1.10x | `PROVED_EXACT` |
| `sum_triangular` | 100 | 0.00150 | 0.00110 | 1.36x | `PROVED_EXACT` |
| `sum_triangular` | 10000 | 0.06690 | 0.00110 | 60.82x | `PROVED_EXACT` |
| `sum_triangular` | 100000 | 0.74670 | 0.00110 | 678.82x | `PROVED_EXACT` |
| `coupled_exchange_sum` | 6 | 0.00140 | 0.00140 | 1.00x | `PROVED_EXACT` |
| `coupled_exchange_sum` | 100 | 0.00170 | 0.00150 | 1.13x | `PROVED_EXACT` |
| `coupled_exchange_sum` | 10000 | 0.03490 | 0.00150 | 23.27x | `PROVED_EXACT` |
| `coupled_exchange_sum` | 100000 | 0.33620 | 0.00150 | 224.13x | `PROVED_EXACT` |

## 2. Collective Dynamics Native Scaling (`N = 100 .. 1,000,000`)

| Model | N Agents | Steps | S3 Native ms | C11 GCC -O3 ms | S3/C11 Ratio | Python ms | S3 vs Python | Max Err vs C11 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `independent` | 100 | 20 | 0.331 | 0.116 | 2.86x | 1.923 | 5.8x | 0.0 |
| `independent` | 1000 | 20 | 0.577 | 0.282 | 2.04x | 20.394 | 35.3x | 0.0 |
| `independent` | 10000 | 20 | 4.073 | 1.217 | 3.35x | 188.713 | 46.3x | 0.0 |
| `independent` | 100000 | 20 | 40.769 | 11.393 | 3.58x | 1922.243 | 47.1x | 0.0 |
| `independent` | 1000000 | 6 | 123.063 | 33.368 | 3.69x | n/a | n/a | 0.0 |
| `curie_weiss` | 100 | 20 | 0.232 | 0.135 | 1.71x | 1.977 | 8.5x | 0.0 |
| `curie_weiss` | 1000 | 20 | 0.532 | 0.249 | 2.14x | 18.790 | 35.3x | 0.0 |
| `curie_weiss` | 10000 | 20 | 4.284 | 1.397 | 3.07x | 188.621 | 44.0x | 0.0 |
| `curie_weiss` | 100000 | 20 | 41.525 | 12.934 | 3.21x | 1906.033 | 45.9x | 0.0 |
| `curie_weiss` | 1000000 | 6 | 122.613 | 41.631 | 2.95x | n/a | n/a | 0.0 |
| `ring_k4` | 100 | 20 | 0.237 | 0.122 | 1.94x | 3.055 | 12.9x | 0.0 |
| `ring_k4` | 1000 | 20 | 1.118 | 0.244 | 4.58x | 29.799 | 26.6x | 0.0 |
| `ring_k4` | 10000 | 20 | 7.857 | 1.700 | 4.62x | 294.036 | 37.4x | 0.0 |
| `ring_k4` | 100000 | 20 | 78.626 | 17.907 | 4.39x | 3020.508 | 38.4x | 0.0 |
| `ring_k4` | 1000000 | 6 | 240.640 | 47.077 | 5.11x | n/a | n/a | 0.0 |

## 3. Falsifiable Hypotheses H1-H6 (Multi-Seed, N=100..100,000)

| Hypothesis | Status | Observed Summary |
| --- | --- | --- |
| `H1_LLN_INDEPENDENT_SCALING` | `CONFIRMED` | `{"ns": [100, 1000, 10000, 100000], "mean_within_stds": [0.09818561921032236, 0.030189934858813758, 0.010037821863151606, 0.00302032614491644], "alpha": 0.5014204815656012}` |
| `H2_SUBCRITICAL_MACRO_PREDICTABILITY` | `CONFIRMED` | `{"weak_stds": [0.11175742023586677, 0.03627740343188154, 0.01595364789307845, 0.0028725748125564368], "alpha": 0.5126791251999929, "kalman_rmse": 0.008860836147836882, "ar_rmse": 0.01376549427993818, "mean_field_rmse": 0.011207702072425782, "naive_rmse": 0.008908109709958175, "best_rmse_model": "kalman_state_space"}` |
| `H3_CRITICAL_AMPLIFICATION_NC` | `CONFIRMED` | `{"crit_total_stds": [0.45913949781340646, 0.09491996449867557, 0.04625007623015222, 0.03699984973604219], "weak_stds": [0.11175742023586677, 0.03627740343188154, 0.01595364789307845, 0.0028725748125564368], "alpha_critical": 0.35934791979179176, "amplification_ratio_at_max_n": 12.880378110366538}` |
| `H4_SHOCK_REGIME_LLN_BREAKDOWN_NC` | `CONFIRMED` | `{"shock_stds": [0.34311151406313195, 0.3311192980244954, 0.32879144387606885, 0.3300940406711026], "alpha_shock": 0.005345681039156226}` |
| `H5_CHAOS_HORIZON_COLLAPSE_NC` | `CONFIRMED` | `{"strategy_decision": "CONVENTIONAL_SIMULATION", "ar_rmse_h1": 0.2301636379211068, "ar_rmse_h5": 0.299164780285593, "quad_nmse": 1.7496137913732153e-17, "lin_nmse": 0.7031969511661278}` |
| `H6_TOPOLOGY_ORDERING_SENSITIVITY` | `CONFIRMED` | `{"mean_field_abs_m": 0.7798333333333334, "erdos_renyi_abs_m": 0.1965, "ring_k4_abs_m": 0.08516666666666667}` |

## 4. Blind Unknown Dynamics 5-Way Routing

| Series | Decision | Detected Regime | IR Proof Status |
| --- | --- | --- | --- |
| `ir_verified_affine` | `EXACT_FAST_FORWARD` | `formal_linear_or_crchain_ir` | `RECOGNIZED_IR_PROOF_ELIGIBLE` |
| `periodic_mod_7_no_ir` | `STATISTICAL_FORECAST` | `periodic_deterministic_period_7` | `NOT_APPLICABLE` |
| `logistic_chaos_r3.9` | `CONVENTIONAL_SIMULATION` | `nonlinear_chaotic_low_dim_map` | `NOT_APPLICABLE` |
| `weak_coupled_abm` | `STATISTICAL_FORECAST` | `stationary_or_smooth_collective_macro` | `NOT_APPLICABLE` |
| `critical_coupled_abm` | `STATISTICAL_FORECAST` | `stationary_or_smooth_collective_macro` | `NOT_APPLICABLE` |
| `shocked_regime_shift` | `MONTE_CARLO_SIMULATION` | `regime_switching_or_critical_shock_process` | `NOT_APPLICABLE` |
| `short_insufficient` | `INSUFFICIENT_EVIDENCE` | `insufficient_sample_length_or_nonfinite` | `NOT_APPLICABLE` |
