# Opportunity Map V1

These are evidence-producing opportunities, not promises or implementation
tasks. Status reflects this campaign's checkpoint.

| ID | opportunity | category | evidence gain | dependency | status |
|---|---|---|---|---|---|
| O01 | complete instruction-budget G/H | causal runtime | direct attribution | Linux guest | NEXT |
| O02 | isolate frame budget after O01 | causal runtime | residual attribution | O01 residual >5x | DEFER |
| O03 | measure bounds-only diagnostic | causal runtime | safety cost split | O01/O02 | DEFER |
| O04 | measure initialization metadata | causal runtime | generated safety split | native build | DEFER |
| O05 | quantify index/address pressure | code structure | memory/index evidence | native disassembly | DEFER |
| O06 | compare stack traffic | code structure | static/dynamic relation | perf availability | DEFER |
| O07 | register-pressure differential | code structure | backend evidence | controlled emitter variant | DEFER |
| O08 | runtime helper attribution | runtime | call cost evidence | helper inventory | DEFER |
| O09 | multi-workload budget replication | causal runtime | holdout validity | O01 | DEFER |
| O10 | BEEBS readiness adapter | embedded | diversity | license/oracle audit | WATCH |
| O11 | CoreMark correctness pilot | embedded | compact control flow | adapter | WATCH |
| O12 | miniBUDE readiness pilot | scientific | irregular diversity | license/oracle | INVESTIGATE |
| O13 | miniMD readiness pilot | scientific | memory/numeric diversity | license/oracle | INVESTIGATE |
| O14 | GAPBS readiness adapter | graph | irregular memory | graph input contract | INVESTIGATE |
| O15 | JSMN native timing boundary | parsing | parsing diversity | native protocol | DEFER |
| O16 | YARPGen differential corpus | correctness | compiler robustness | safe harness | WATCH |
| O17 | CSmith differential corpus | correctness | randomized robustness | bounded runner | WATCH |
| O18 | reproducibility fingerprint schema | methodology | cross-host comparability | host matrix | DEFER |
| O19 | evidence registry for causal artifacts | infrastructure | provenance | schema design | NEXT |
| O20 | benchmark stack consolidation plan | governance | lower documentation debt | owner decision | DEFER |
| O21 | safe budget design review | runtime design | future bounded-mode options | O01 | DEFER |
| O22 | checked-vs-benchmark mode study | runtime design | safety/perf boundary | O01 | DEFER |
