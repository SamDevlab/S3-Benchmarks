# Native S3 Codegen R2 — paired BASE/CANDIDATE experiment

- BASE: `87c0a5be070210f158313a4d272fbdd795536232` (parent `2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c`)
- CANDIDATE: `94ef25f2fca720931df0f7bb97ff0b26e0d4bab7` (parent `6e3881d6ff6066e6828d143e08adbf030542dd16`)
- Host: AMD Ryzen 5 3400G with Radeon Vega Graphics; Linux-7.0.0-31-generic-x86_64-with-glibc2.43; CPU affinity `0`.
- Dynamic PMU counters: `UNAVAILABLE` (permission_or_event_denied); no dynamic instruction counts are claimed.
- Fixture SHA-256 `870150e16732b81a733af584cb68b1ddddfb47fa06ee7f8a9d6248a99b099a8d`; 81 paired rounds; V1 inputs and oracle reused.
- A result below 1.000× means CANDIDATE was faster; interval crossing 1.000× does not establish a runtime gain.

## Paired runtime (ns/call)

| Workload | Size | Profile | BASE median | CANDIDATE median | Candidate/BASE | 95% paired bootstrap CI | BASE CV | Candidate CV |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `energy_series_aggregation` | small | `PURE_EXPERIMENTAL` | 2941.25 | 2660.00 | 0.901× | [0.879, 0.935]× | 1.219 | 0.505 |
| `energy_series_aggregation` | medium | `PURE_EXPERIMENTAL` | 11590.00 | 10165.00 | 0.913× | [0.872, 0.960]× | 0.712 | 0.393 |
| `energy_series_aggregation` | full | `PURE_EXPERIMENTAL` | 31140.00 | 27760.00 | 0.902× | [0.892, 0.934]× | 0.494 | 0.836 |
| `agent_energy_residual` | small | `PURE_EXPERIMENTAL` | 2660.00 | 2636.25 | 0.995× | [0.980, 1.036]× | 0.579 | 0.732 |
| `agent_energy_residual` | medium | `PURE_EXPERIMENTAL` | 9465.00 | 10010.00 | 1.005× | [0.974, 1.066]× | 0.516 | 0.686 |
| `agent_energy_residual` | full | `PURE_EXPERIMENTAL` | 25720.00 | 24380.00 | 0.960× | [0.942, 0.976]× | 0.564 | 0.509 |
| `energy_series_aggregation` | small | `PER_INSTRUCTION` | 3043.75 | 3008.75 | 1.013× | [1.002, 1.018]× | 0.315 | 0.666 |
| `energy_series_aggregation` | medium | `PER_INSTRUCTION` | 11570.00 | 11265.00 | 1.009× | [0.989, 1.014]× | 0.807 | 0.448 |
| `energy_series_aggregation` | full | `PER_INSTRUCTION` | 32250.00 | 31490.00 | 1.011× | [1.000, 1.014]× | 0.441 | 0.777 |
| `agent_energy_residual` | small | `PER_INSTRUCTION` | 2736.12 | 2353.75 | 0.931× | [0.909, 0.966]× | 0.601 | 0.654 |
| `agent_energy_residual` | medium | `PER_INSTRUCTION` | 8580.00 | 8300.00 | 0.982× | [0.955, 0.994]× | 1.538 | 1.792 |
| `agent_energy_residual` | full | `PER_INSTRUCTION` | 23290.00 | 23040.00 | 0.988× | [0.949, 1.013]× | 0.259 | 0.631 |

## Static code, size and build observations

Static instruction counts are disassembly counts, not dynamic counts. Compile measurements are one build per pinned artifact and descriptive, not a statistical build-time claim.

| Artifact | Profile | IR TSLOAD sites by function | Function instructions | Scratch/direct loads | Assembly bytes | Assembly SHA-256 | Static instructions | ELF bytes | `.text` bytes | Compile s | Link s |
|---|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| `baseline-s3-pure_experimental-o1-energy_series_aggregation` | PURE_EXPERIMENTAL/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2124 | 2/0 | 253745 | `a83a939ed5cebcae44f3e09326bfc73fa6a866fa257dbfc5c59d0da81a1b2f1e` | 5615 | 103112 | 27791 | 0.120064 | 0.009316 |
| `baseline-s3-per_instruction-o1-energy_series_aggregation` | PER_INSTRUCTION/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2754 | 2/0 | 368100 | `781fde32b69cd62b0cf3f590cbe9c5feee0fcfa90f66d0005ce18522e56e74df` | 7231 | 160584 | 36255 | 0.131147 | 0.008554 |
| `baseline-s3-pure_experimental-o1-agent_energy_residual` | PURE_EXPERIMENTAL/O1 | `{"agent_energy_residual": 2, "main": 0}` | 2774 | 2/0 | 321343 | `64c23d112a6b069dd67f0ed757a452d77977751c35051ba1e790f063dc1c9f38` | 6807 | 127376 | 34719 | 0.253519 | 0.011304 |
| `baseline-s3-per_instruction-o1-agent_energy_residual` | PER_INSTRUCTION/O1 | `{"agent_energy_residual": 2, "main": 0}` | 3682 | 2/0 | 481337 | `4b782059694c56b0b13e315b1be3b0c7170aff9770e69253c3f3899419f1b411` | 9079 | 209424 | 46619 | 0.245587 | 0.011222 |
| `candidate-s3-pure_experimental-o1-energy_series_aggregation` | PURE_EXPERIMENTAL/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2118 | 0/0 | 253643 | `d310e3f313a3d8dc8cc7d9c35b5601e2efe944c6b8d3464cc968459cf878739a` | 5609 | 103112 | 27773 | 0.118188 | 0.012489 |
| `candidate-s3-per_instruction-o1-energy_series_aggregation` | PER_INSTRUCTION/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2748 | 0/0 | 367998 | `df6cc7f415c9a2e5f07b83992d42ef7c0f17a39e303bb601915d9416fe2fb10f` | 7225 | 160584 | 36237 | 0.110490 | 0.008475 |
| `candidate-s3-pure_experimental-o1-agent_energy_residual` | PURE_EXPERIMENTAL/O1 | `{"agent_energy_residual": 2, "main": 0}` | 2768 | 0/0 | 321241 | `ab641a4939852199e6a12aaae0cedcc4af2689cc905a19ab15765bb9f0d866e2` | 6801 | 127376 | 34701 | 0.192470 | 0.008881 |
| `candidate-s3-per_instruction-o1-agent_energy_residual` | PER_INSTRUCTION/O1 | `{"agent_energy_residual": 2, "main": 0}` | 3676 | 0/0 | 481235 | `b0a29da225c1f462cb29499e1311e587b81e4e03005dcb6a11748094950d390c` | 9073 | 209424 | 46601 | 0.188244 | 0.007347 |

## Interpretation limits

- The codegen change removes temporary-register copies for register-resident slice loads while retaining source-register initialization checks, the unsigned `index < length` check, and the bounds-failure path.
- The semantic source, IR operations, slices, bounds behavior, fixture, FFI, and timed harness are unchanged between revisions.
- V1 cross-language medians are historical context only; this experiment does not rerun or overwrite that matrix.
- PMU denial means runtime cause attribution is supported by paired timing and static assembly evidence only, not dynamic instruction/cycle counters.
- No claim is made about production profile/defaults or safety equivalence of `PURE_EXPERIMENTAL`.
