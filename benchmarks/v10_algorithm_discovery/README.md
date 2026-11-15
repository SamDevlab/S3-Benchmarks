# S3 V10 — Algorithm Discovery Challenge (experimental)

**Scope:** the original V10 black-box discovery challenge used a frozen
GF(2) inference engine and GCC-native holdouts. V10.1–V10.3 subsequently
added a separate **restricted proof-gated S3-native experimental API**
in the sibling S3 repository; it is NOT an automatic compiler pass.
Compact and DOOM remain frozen.

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


## V10.3 — Dynamic-horizon certified S3-native vs GCC references

New controlled experiments use the **source-aware restricted S3 IR
certificate**, not the unsafe black-box probabilistic inference:

- \`run_dynamic_native_comparison.py\`: builds one S3-generated x86-64
  binary per width, then tests N={0,1,10,100,1000,10000,100000,1000000}
  in the same binary.
- \`native_gf2_dynamic_harness.c\`: independent C11/GCC native benchmark
  with four methods: direct N-step iteration; S3 dynamic GF(2) matrix
  repeated squaring; **GCC generic matrix repeated squaring with the same
  algorithmic strategy**; and a stronger known specialist cyclic GF(2)
  polynomial implementation.
- \`native_gf2_dynamic_results_v10_3.json\`: nine alternating rounds,
  64 differential state checks at every N, build and certificate
  latency and Python guarded API cost.
- \`test_dynamic_native_results.py\`: benchmark artifact consistency
  tests; performance ratios are observational, not correctness proofs.

Reproduce on Windows/WSL with sibling S3 repository present:

\`\`\`bash
cd /mnt/c/Users/samue/Desktop/gemini/S3-Benchmarks
python3 benchmarks/v10_algorithm_discovery/run_dynamic_native_comparison.py
python3 -m unittest discover \
    -s benchmarks/v10_algorithm_discovery -p 'test_*.py' -v
\`\`\`

At N=1,000,000 the single-host exploratory medians were:

| Width | S3 dynamic native | GCC same generic algorithm | GCC specialized cyclic algorithm |
|---|---:|---:|---:|
| W8 | 3.315 us | 1.227 us | 0.03537 us |
| W16 | 10.760 us | 3.900 us | 0.05488 us |

The matched generic GCC code was ~2.7x faster; the specialist was
~94–196x faster. This is an important **negative result for claims of
state-of-art performance**, not a failure of native correctness.
The protected Python API (~0.4–0.45 ms per call) is measured separately
because it revalidates the source-IR proof on every call. Cold build
and the mathematical certificate also have nonzero costs.

**GO:** restricted V10.3 dynamic-N S3-native experimental kernel.
**NO-GO:** automatic compiler promotion, production, universal proof
or a claim of new algorithmic asymptotics.

The V10 rare nonlinear black-box counterexample remains a mandatory
negative result; the V10.1/10.3 native path requires a source-derived
certificate and cannot be authorized solely by randomized linearity
testing.
