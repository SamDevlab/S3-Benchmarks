# S3 Optimization Candidates

These are bounded hypotheses for later experiments, not implementation requests. No S3 source was changed by this campaign.

## Candidate 1

- `CANDIDATE`: direct kernel timing for one flat vector hot path
- `OBSERVATION`: all current rows are process-E2E; kernel cost cannot be separated from startup/runtime initialization.
- `AFFECTED_WORKLOADS`: BabelStream-compatible subset, PRK nstream, PolyBench vector paths
- `AFFECTED_FAMILIES`: `memory`, `hpc`, `numerical`
- `STRUCTURAL_EVIDENCE`: assembly metrics are available; dynamic counters are not.
- `PERFORMANCE_EVIDENCE`: multi-family process-E2E samples only.
- `CAUSALITY`: `UNKNOWN`
- `NEXT_DISCRIMINATING_EXPERIMENT`: add a setup-outside-loop kernel adapter for one non-mutating vector workload.
- `FALSIFIER`: direct kernel timing does not reproduce the E2E ordering or shows startup dominates.

## Candidate 2

- `CANDIDATE`: isolate vector access/helper and stack-operation density
- `OBSERVATION`: call-site and stack-operation counts are present across independent families.
- `AFFECTED_WORKLOADS`: vector, RMSD, transpose and PolyBench matrix rows
- `AFFECTED_FAMILIES`: `scientific`, `hpc`, `memory`, `numerical`
- `STRUCTURAL_EVIDENCE`: static call/stack/branch counts per work unit are recorded.
- `PERFORMANCE_EVIDENCE`: no direct causal timing or perf counters.
- `CAUSALITY`: `UNKNOWN`
- `NEXT_DISCRIMINATING_EXPERIMENT`: compare one S3 kernel against an equivalent flat-storage C kernel with matching work units.
- `FALSIFIER`: matched kernel timing shows no relationship to static stack/call density.

## Candidate 3

- `CANDIDATE`: reduce environmental variance before performance attribution
- `OBSERVATION`: process-E2E CV and p95 tails are material on a small virtualized host.
- `AFFECTED_WORKLOADS`: all measured points
- `AFFECTED_FAMILIES`: all measured families
- `STRUCTURAL_EVIDENCE`: fixed affinity is recorded; governor/turbo are unavailable.
- `PERFORMANCE_EVIDENCE`: raw samples, CV, MAD and p95 are preserved.
- `CAUSALITY`: `UNKNOWN`
- `NEXT_DISCRIMINATING_EXPERIMENT`: repeat a bounded same-machine direct-kernel run with documented host controls.
- `FALSIFIER`: variance remains unchanged under a controlled direct-kernel protocol.
