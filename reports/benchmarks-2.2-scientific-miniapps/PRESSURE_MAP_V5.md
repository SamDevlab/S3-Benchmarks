# Pressure Map V5

STATUS=PHASE_B_CORRECTNESS_COMPLETE
CAUSAL_EXPERIMENT_READY=NO

Phase A established reproducible direct FFI observations across triad,
nstream, GEMM, and RMSD families. Phase B adds scientific correctness
coverage through deterministic RMSD profiles. Neither phase identifies a
unique compiler cause or justifies a promoted optimization.

PRESSURE=scientific indexed-vector and nested-loop representability
FAMILIES=RMSD_SINGLE,RMSD_BATCH,RMSD_MATRIX
EVIDENCE_STRENGTH=CORRECTNESS_AND_NATIVE_CANARY
CAUSALITY=NOT_ESTABLISHED
SCIENTIFIC_CORRECTNESS=PASS
NATIVE_SPEEDUP_CLAIM=NO
TIMING=NOT_RUN

PRESSURE=external scientific workload promotion requires provenance and adapter closure
FAMILIES=XSBench,miniBUDE,miniMD
EVIDENCE_STRENGTH=AUDIT_ONLY
CAUSALITY=NOT_APPLICABLE
PROMOTION=DEFERRED

NEXT_DISCRIMINATING_EXPERIMENT=qualify one deferred workload with immutable source, license, input contract, independent oracle, and matched native canary before timing
