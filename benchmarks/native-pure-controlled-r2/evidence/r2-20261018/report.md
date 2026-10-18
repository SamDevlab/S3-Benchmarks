# Native S3 Codegen R2 — paired BASE/CANDIDATE experiment

- BASE: `87c0a5be070210f158313a4d272fbdd795536232` (parent `2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c`)
- CANDIDATE: `6e3881d6ff6066e6828d143e08adbf030542dd16` (parent `87c0a5be070210f158313a4d272fbdd795536232`)
- Host: AMD Ryzen 5 3400G with Radeon Vega Graphics; Linux-7.0.0-31-generic-x86_64-with-glibc2.43; CPU affinity `0`.
- Dynamic PMU counters: `UNAVAILABLE` (permission_or_event_denied); no dynamic instruction counts are claimed.
- Fixture SHA-256 `870150e16732b81a733af584cb68b1ddddfb47fa06ee7f8a9d6248a99b099a8d`; 81 paired rounds; V1 inputs and oracle reused.
- A result below 1.000× means CANDIDATE was faster; interval crossing 1.000× does not establish a runtime gain.

## Paired runtime (ns/call)

| Workload | Size | Profile | BASE median | CANDIDATE median | Candidate/BASE | 95% paired bootstrap CI | BASE CV | Candidate CV |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `energy_series_aggregation` | small | `PURE_EXPERIMENTAL` | 2976.25 | 3018.75 | 1.025× | [1.013, 1.044]× | 0.301 | 0.632 |
| `energy_series_aggregation` | medium | `PURE_EXPERIMENTAL` | 11075.00 | 11620.00 | 1.047× | [1.039, 1.065]× | 0.516 | 0.419 |
| `energy_series_aggregation` | full | `PURE_EXPERIMENTAL` | 30790.00 | 32330.00 | 1.052× | [1.020, 1.068]× | 0.290 | 0.464 |
| `agent_energy_residual` | small | `PURE_EXPERIMENTAL` | 2651.25 | 2622.50 | 1.000× | [0.985, 1.015]× | 0.562 | 0.134 |
| `agent_energy_residual` | medium | `PURE_EXPERIMENTAL` | 9345.00 | 9409.50 | 0.998× | [0.991, 1.016]× | 0.429 | 0.522 |
| `agent_energy_residual` | full | `PURE_EXPERIMENTAL` | 25670.00 | 25440.00 | 0.984× | [0.971, 1.004]× | 0.388 | 0.345 |
| `energy_series_aggregation` | small | `PER_INSTRUCTION` | 2983.75 | 2962.50 | 0.993× | [0.990, 0.999]× | 0.309 | 0.660 |
| `energy_series_aggregation` | medium | `PER_INSTRUCTION` | 11334.50 | 11225.00 | 0.992× | [0.988, 0.996]× | 0.138 | 0.444 |
| `energy_series_aggregation` | full | `PER_INSTRUCTION` | 31540.00 | 31290.00 | 0.992× | [0.986, 0.995]× | 0.396 | 0.513 |
| `agent_energy_residual` | small | `PER_INSTRUCTION` | 2370.00 | 2483.75 | 1.024× | [1.011, 1.073]× | 0.446 | 0.605 |
| `agent_energy_residual` | medium | `PER_INSTRUCTION` | 8415.00 | 8815.00 | 1.008× | [0.985, 1.051]× | 0.437 | 0.671 |
| `agent_energy_residual` | full | `PER_INSTRUCTION` | 22950.00 | 23480.00 | 1.007× | [0.974, 1.043]× | 0.488 | 0.443 |

## Static code, size and build observations

Static instruction counts are disassembly counts, not dynamic counts. Compile measurements are one build per pinned artifact and descriptive, not a statistical build-time claim.

| Artifact | Profile | IR TSLOAD sites by function | Function instructions | Scratch/direct loads | Assembly bytes | Assembly SHA-256 | Static instructions | ELF bytes | `.text` bytes | Compile s | Link s |
|---|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| `baseline-s3-pure_experimental-o1-energy_series_aggregation` | PURE_EXPERIMENTAL/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2124 | 2/0 | 253745 | `a83a939ed5cebcae44f3e09326bfc73fa6a866fa257dbfc5c59d0da81a1b2f1e` | 5615 | 103112 | 27791 | 0.087077 | 0.007459 |
| `baseline-s3-per_instruction-o1-energy_series_aggregation` | PER_INSTRUCTION/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2754 | 2/0 | 368100 | `781fde32b69cd62b0cf3f590cbe9c5feee0fcfa90f66d0005ce18522e56e74df` | 7231 | 160584 | 36255 | 0.101618 | 0.008237 |
| `baseline-s3-pure_experimental-o1-agent_energy_residual` | PURE_EXPERIMENTAL/O1 | `{"agent_energy_residual": 2, "main": 0}` | 2774 | 2/0 | 321343 | `64c23d112a6b069dd67f0ed757a452d77977751c35051ba1e790f063dc1c9f38` | 6807 | 127376 | 34719 | 0.151439 | 0.006690 |
| `baseline-s3-per_instruction-o1-agent_energy_residual` | PER_INSTRUCTION/O1 | `{"agent_energy_residual": 2, "main": 0}` | 3682 | 2/0 | 481337 | `4b782059694c56b0b13e315b1be3b0c7170aff9770e69253c3f3899419f1b411` | 9079 | 209424 | 46619 | 0.148473 | 0.007953 |
| `candidate-s3-pure_experimental-o1-energy_series_aggregation` | PURE_EXPERIMENTAL/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2116 | 0/2 | 253609 | `6a759561a9e66e267bd3f6f79fab32c8519998ca0bc97cddcfddaf7ea84b9c11` | 5607 | 103112 | 27767 | 0.082831 | 0.007908 |
| `candidate-s3-per_instruction-o1-energy_series_aggregation` | PER_INSTRUCTION/O1 | `{"absolute_f64": 0, "energy_series_aggregation": 2, "main": 0}` | 2746 | 0/2 | 367964 | `c4f687e43b5f982fd59ffb9f1ca9e25a4c6f28f06ecfd22d9dc96616fd1decdc` | 7223 | 160584 | 36231 | 0.093080 | 0.006620 |
| `candidate-s3-pure_experimental-o1-agent_energy_residual` | PURE_EXPERIMENTAL/O1 | `{"agent_energy_residual": 2, "main": 0}` | 2766 | 0/2 | 321207 | `14c316bd34c7db340b289fbb6a4bad71e74e5666ef4938c8a6660f2f51d3dab7` | 6799 | 127376 | 34695 | 0.150723 | 0.006922 |
| `candidate-s3-per_instruction-o1-agent_energy_residual` | PER_INSTRUCTION/O1 | `{"agent_energy_residual": 2, "main": 0}` | 3674 | 0/2 | 481201 | `440def67de2c73b6ad8484599328755fdb1a98f778b3ca05859ed78ff3a152ad` | 9071 | 209424 | 46595 | 0.145425 | 0.007290 |

## Interpretation limits

- The codegen change removes temporary-register copies for register-resident slice loads while retaining source-register initialization checks, the unsigned `index < length` check, and the bounds-failure path.
- The semantic source, IR operations, slices, bounds behavior, fixture, FFI, and timed harness are unchanged between revisions.
- V1 cross-language medians are historical context only; this experiment does not rerun or overwrite that matrix.
- PMU denial means runtime cause attribution is supported by paired timing and static assembly evidence only, not dynamic instruction/cycle counters.
- No claim is made about production profile/defaults or safety equivalence of `PURE_EXPERIMENTAL`.
