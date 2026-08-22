# S3 RC1 longitudinal native benchmark

- RC1 source: `9b39c7070d7bfa23d709c2128eb0b0bbef164177`
- Benchmark analysis HEAD: `4ef8b605489e21f6affa2eb9fc244e54ae31004d`
- P1 correctness: **PASS**
- P1 longitudinal classification: **INCONCLUSIVE**
- C-O2 gap: **43.89x geomean**
- Native speedup claim: **NO**
- P2-P18: contract probes expanded the registry, but all remain experimental/deferred and are excluded from aggregate claims.

The evidence supports a large remaining native representation/code-generation gap, but not a causal claim for a single layer. H4-H5 runtime evolution is inconclusive because C-O2 control drift exceeded the declared threshold and paired raw samples were not persisted.
