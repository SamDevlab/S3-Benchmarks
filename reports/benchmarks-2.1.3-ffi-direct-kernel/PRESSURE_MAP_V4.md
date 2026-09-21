# Pressure Map V4

STATUS=READY_FOR_PHASE_B
CAUSAL_EXPERIMENT_READY=NO

The direct FFI protocol is now reproducible across four independent workload
families, but these observations do not by themselves identify a compiler
cause. No optimization target is promoted without a separate discriminating
experiment.

PRESSURE=high S3 call-loop cost relative to matched C references
FAMILIES=TRIAD,NSTREAM,GEMM,RMSD_BATCH
EVIDENCE_STRENGTH=MULTI_FAMILY
CAUSALITY=CORRELATED
DIRECT_FFI_EVIDENCE=PASS
STRUCTURAL_EVIDENCE=matched ABI and frozen artifact hashes
PERF_EVIDENCE=UNAVAILABLE_BY_POLICY
FALSIFIER=repeat on a controlled host with supported counters and an isolated boundary control

PRESSURE=S3_FFI_O1 lower call-loop cost than S3_FFI_O0 in all four families
FAMILIES=TRIAD,NSTREAM,GEMM,RMSD_BATCH
EVIDENCE_STRENGTH=MULTI_FAMILY
CAUSALITY=CORRELATED
DIRECT_FFI_EVIDENCE=PASS
STRUCTURAL_EVIDENCE=O0/O1 artifacts are distinct and provenance-pinned
PERF_EVIDENCE=UNAVAILABLE_BY_POLICY
FALSIFIER=an independently rebuilt pair that removes the same gap without changing the ABI or workload

NEXT_DISCRIMINATING_EXPERIMENT=measure a matched identity boundary and supported native counters on a controlled host
