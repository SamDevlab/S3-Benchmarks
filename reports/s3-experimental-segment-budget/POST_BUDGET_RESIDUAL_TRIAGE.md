# Post-Budget Residual Triage

## Observed

P2 was faster than P1 in every cell and crossed the strong-recovery threshold
in all six cells. Against the unsafe PNEG lower bound, RMSD P2 was 4.3-6.8%
faster; XSBench P2 was 2.2-3.9% slower; JSMN P2 was 7.9-9.5% slower.

The emitted P2 `.text` is 39.17% larger for RMSD, 53.35-53.57% larger for
XSBench, and 58.27-58.54% larger for JSMN. The implementation emits a fast
precharge/body and a separate exact scalar slow-path copy for every fast
segment. The plans contain 17, 27, and 298 fast segments respectively. Thus
slow-path duplication and per-segment guard structure are the strongest direct
structural residual candidates. Their contribution to the measured P2-vs-PNEG
runtime differences was not isolated; no microarchitectural cause is claimed.

## Evidence Not Established

This campaign did not measure dynamic loads/stores, stack traffic, spill/reload
counts, register pressure, branch-misprediction, bounds-check cost, or runtime
helper cost. It therefore does not establish H4/H5, helpers, or instruction
selection as the dominant residual. Static native-instruction counts and code
size are descriptive and are not dynamic execution counts.

## PR #190 Read-Only Correlation

PR #190 remains an unrelated open Draft experiment and was not changed or
activated. Its V2.1 report records compact-EA move/instruction reduction with
no load/store or stack reduction; scalar replacement removed one load and one
store; region-aware spill, rematerialization, and live-range splitting were
neutral in that attribution. These are not a direct match for P2's duplicated
exact slow path.

| mechanism | classification | relation to this residual |
|---|---|---|
| compact indexed memory | POSSIBLE_MATCH | may improve native address lowering, but the observed growth is the P2 exact slow-path copy; no causal overlap shown |
| scalar replacement | NO_MATCH | one load/store reduction in PR #190 evidence; P2 has no measured traffic attribution |
| region-aware spill | NO_MATCH | prior attribution neutral; no spill evidence in this campaign |
| rematerialization | NO_MATCH | prior attribution neutral; not the segment duplication mechanism |
| live-range split | NO_MATCH | prior attribution neutral; no live-range pressure measured here |
| register policy | NO_MATCH | PR #190 produced no production candidate; no register-residence evidence links it to P2 residual |

## One Next Step

The one selected continuation is `S3_EXPERIMENT_SEGMENT_BUDGET_HARDENING`:
test whether the existing exact slow path can be outlined/shared to reduce
`.text` expansion while preserving E0 and deterministic Assembly segment
boundaries. Do not combine it with bounds, allocation, helper, or instruction
selection experiments. No hardening or new architecture is implemented by
this report.
