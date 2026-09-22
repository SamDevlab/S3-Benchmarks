# External Frontier Radar

Initial watchlist. These are candidates for evidence diversity, not copied
code or current S3 support claims.

| project | verified repository/head | license | level | relevance | status |
|---|---|---|---:|---|---|
| Embench | requested alias not found | unknown | L2 | embedded/control-flow diversity | WATCH |
| BEEBS | embecosm/riscv-beebs @ 63847f95 | GPL-3.0 | L2 | small deterministic kernels | WATCH |
| CoreMark | eembc/coremark @ 1f483d5b | NOASSERTION | L1 | compact integer control flow | WATCH |
| CoreMark-Pro | eembc/coremark-pro @ 4832cc67 | NOASSERTION | L2 | broader embedded mix | WATCH |
| miniBUDE | scientific Monte Carlo | L3 | irregular scientific workload | INVESTIGATE |
| miniMD | molecular dynamics | L3 | memory/numeric workload | INVESTIGATE |
| XSBench | ANL-CESAR/XSBench @ ba08e522 | MIT | L3 | active irregular reference | PILOT_ACTIVE |
| LULESH | llnl/LULESH @ 3e01c40b | unspecified | L4 | larger scientific control/data flow | DEFER |
| HPCG | hpcg-benchmark/hpcg @ 114602d4 | BSD-3-Clause | L4 | locality and memory pressure | DEFER |
| NPB | requested alias not found | unknown | L4 | established portability corpus | DEFER |
| RAJAPerf | llnl/RAJAPerf @ 03295a10 | BSD-3-Clause | L4 | backend/memory comparisons | DEFER |
| GAPBS | sbeamer/gapbs @ 2972aeb2 | NOASSERTION | L3 | graph and irregular memory | INVESTIGATE |
| PBBS | parallel algorithms | L3 | algorithmic breadth | DEFER |
| YARPGen | requested alias not found | unknown | L3 | differential correctness methods | WATCH |
| LLVM test-suite | llvm/llvm-test-suite @ 4eee8855 | NOASSERTION | L5 | broad external validation | DEFER |
| CSmith | csmith-project/csmith @ 0cdc7103 | NOASSERTION | L3 | randomized differential testing | WATCH |

This radar is a planning artifact. Current heads were checked with GitHub API
and `git ls-remote` on 2026-09-22. A future pilot must verify license, current
head, oracle simplicity, and non-duplication before adoption. The requested
aliases for Embench, miniBUDE, miniMD, NPB, PBBS, and YARPGen were not found
under the guessed owners and remain unverified rather than being silently
replaced.
