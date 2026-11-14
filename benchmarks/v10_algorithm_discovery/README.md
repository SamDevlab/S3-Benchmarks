# S3 V10 — Algorithm Discovery Challenge (experimental)

**Scope:** black-box discovery of general GF(2) linear transitions, blind
post-freeze holdouts, and GCC-native demonstration. **Not integrated with the
S3 compiler yet.** Compact and DOOM remain frozen.

## Protocol

1. The generic engine \`blackbox_gf2.py\` and its white-box tests were
   committed as \`ab0b252\` **before** the held-out oracles were created.
2. \`sealed_challenge.py\` defines six unseen linear examples plus three
   nonlinear negative controls; the engine only receives opaque callables.
3. \`run_sealed_challenge.py\` evaluates candidate equivalence and records
   a deliberately rare nonlinear counterexample.
4. \`native_compare.py\` generates actual GCC-compiled C from **inferred
   columns** and compares it to a matrix-iterative baseline and (for cyclic
   systems) an independent known polynomial method.
5. Source proof is absent; never deploy the probabilistic candidate as an
   exact compiler optimization.

## Reproduce on WSL

\`\`\`bash
cd /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks/benchmarks/v10_algorithm_discovery
python3 -m unittest discover -s . -p 'test_*.py' -v
python3 run_sealed_challenge.py
python3 native_compare.py
\`\`\`

## Outcomes

- 6/6 linear holdouts passed.
- 2/3 nonlinear controls rejected during discovery.
- 1 rare-trigger nonlinearity **falsely accepted**, discovered only
  during post-freeze independent evaluation; this is an explicit NO-GO.
- 6/6 inferred linear C backends compiled and passed tested native
  differential comparisons.
- 14 unit tests passed.
- Strong cyclic specialist GCC baseline outperformed generic inferred
  matrix powering in representative tests.
- No new asymptotic algorithm was discovered; existing known GF(2)
  linear algebra was automatically reused for unseen oracle families.

## Provenance and limitations

The Python engine makes O(W) basis oracle queries plus validation; small
widths can be exhaustively checked, larger widths receive probabilistic
BLR tests. Discovering linearity from arbitrary black-box queries is **not
a sound universal mathematical certificate**. Observed runtime speedup
excludes discovery, compiling, load, and verification costs. Machine
benchmarks cover one CPU/WSL session and five rounds; they are exploratory.

The next science gate is a sound source-aware S3 IR proof of linearity
and domain guards, then same-IR S3-native and GCC-native comparisons.
