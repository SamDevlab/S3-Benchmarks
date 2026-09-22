# Safe Instruction-Budget Design Space

This is a research inventory, not a production recommendation. Any future
design must preserve bounded execution, deterministic failure, and runaway
detection before it can be considered.

Candidates to measure independently:

- per-basic-block accounting;
- weighted-block accounting;
- loop-trip accounting;
- batched counter decrementing;
- register-resident accounting with spill-safe exit paths;
- function-level budget charging;
- periodic sampling with an explicit detection bound;
- checked, benchmark, and production execution modes;
- compile-time proven bounded regions.

Required future gates: correctness, bounded execution, runaway detection,
measured overhead, and multi-workload validation. None is implemented here.
