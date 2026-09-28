# S3 1.11 Independent Candidate Replay

## Provenance

```text
S3_CONTROL_SHA=832b1cc04fe1f6174e482eb3a245e08af3d53211
S3_CONTROL_TREE=dc1138890655169088f9371ce32a9050cfc3af8d
BENCH_EXECUTOR_SHA=b3ecb9b2269b583cba0706fd7ed13956a9641512
BENCH_EXECUTOR_TREE=06316635dfc1830d3ec3955803acb0d168b77a7e
TARGET=Linux x86-64
TIMING_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
HARDWARE_COUNTERS=UNAVAILABLE_BY_POLICY_NOT_PROBED_AGAIN
```

The Bench tools validated the pinned S3 source checkout, experiment identity,
native artifact filename/length/SHA-256, workload reference, and output
digests. They then independently replayed both baseline and candidate
artifacts. These were compiled artifacts from the S3 experiment; the replay
does not claim an independent recompilation of the research transformation.

## Candidate correctness replay

All three workload candidates passed reference checks and exact baseline /
candidate output-digest equality:

| Experiment | Replay result SHA-256 | Result |
| --- | --- | --- |
| `EXP-S3-111-VALUE-COST-001` | `54d8924147879b452753197794cccfdae6c5877e3160d4f94c111ffbd60a5dd3` | PASS 3/3 |
| `EXP-S3-111-VALUE-COST-002` | `95d335ea9b08d2b82435c4c2814afedd7d73896a1e97d90bee5243cbb3adc134` | PASS 3/3 |
| `EXP-S3-111-VALUE-COST-002` confirmatory artifact set | `8c4af641ef68fa5d3e117d9706901ce7e7ce90f8f5a3e436c0a7c8fc19a6f9d5` | PASS 3/3 |

The separate point-cloud timing report uses the same baseline native artifact
SHA-256 `fc640b39ef8c97304a45800bd48a7b5a779c046858f41988b6b87fff142bbd07`
and candidate SHA-256
`5557cc8de4c9d065ade26a11449bc8961a2059d10a4266809a63938b4194a714`.
Both produced the same expected output SHA-256
`6bdc5b40a566f1b9487ff18c96ceb2a7ab53c740c666b4f8bf10de84bee6dc07`.

## Interleaved point-cloud timing

The independent timing report is
`evidence/candidate-replay/EXP-S3-111-VALUE-COST-002-point-timing.json`,
SHA-256 `45517665fac2ccd9b7612ef921708c84c80416f8c629ca7c1044ae37630d70cb`.
Protocol: three warmups, 21 samples, 1,000 calls per sample, alternating
baseline/candidate order, paired bootstrap with 10,000 resamples.

```text
BASELINE_MEDIAN_NS_PER_CALL=17929.709
CANDIDATE_MEDIAN_NS_PER_CALL=16834.066
BASELINE_OVER_CANDIDATE_RATIO=1.0904381539626733
PAIRED_BOOTSTRAP_95_PERCENTILE_INTERVAL=[1.0617131092877699,1.1800766672510001]
CLASSIFICATION=MATERIAL_IMPROVEMENT
TIMING_CLASS=CHARACTERIZATION_ONLY
NATIVE_SPEEDUP_CLAIM=NO
```

This independently reproduces a material point-cloud timing signal for the
exact same binary artifacts as two recent S3 paired runs. An earlier S3 run
of the experiment was below the 5% threshold; it remains in the historical
record. One workload-specific timing result does not establish a cause or
generalize to energy/raster. The transformed candidate also increases static
memory references, stack references, peak live values and stack-resident
virtuals, so the S3 conservative Pareto/pressure gate continues to reject it.
No promotion is authorized by this characterization.

Tool provenance:

```text
TIMING_TOOL_SHA256=761550a64532ed3d471b1a76a90d3decc5ada38bdc094defbe40f71f397fe448
REPLAY_TOOL_SHA256=b163828224d67bc7404726f165804dc846fd8d0d9fe26119598e25d568d79116
```

```text
INDEPENDENT_CANDIDATE_CORRECTNESS_REPLAY=PASS (3/3)
INDEPENDENT_CANDIDATE_TIMING_REPLICATION=PARTIAL (point-cloud only)
PRODUCTION_DEFAULT_CHANGED=NO
RELEASE_OR_TAG_CREATED=NO
```

## Independent hot-fallthrough replay

`EXP-S3-111-HOT-FALLTHROUGH-001` was independently replayed by the Bench lab
using the exact S3-produced baseline and candidate shared objects. The replay
validated both outputs against the pinned energy workload reference, confirmed
exact baseline/candidate output equality, and independently re-extracted the
native structure.

```text
REPLAY_REPORT=evidence/EXP-S3-111-HOT-FALLTHROUGH-REPLAY-001.json
REPLAY_REPORT_SHA256=053c3dd3d0f2ad92ed6af6a2511885c5b4f83f4b3b66765f2d968ec102df4076
BASELINE_ARTIFACT_SHA256=6b4b944c54cc5ee6bf05b40f2c44e870626f8856fdb8169884a9634f44c0b2e8
CANDIDATE_ARTIFACT_SHA256=46c04d2fe7029429c7ced601fd98b6bca7d4eb85a53e627c8bd84b7858fe8a7f
OUTPUTS_EXACTLY_EQUAL=YES
INDEPENDENT_NATIVE_METRICS=MATCH
TIMING=NOT_MEASURED_IN_LAB_REPLAY
NATIVE_SPEEDUP_CLAIM=NO
```

The independent extractor confirmed the S3 report's structural delta: one
fewer static branch and machine instruction, and two fewer `.text` bytes;
memory references, stack references, frame size, and ELF size were unchanged.
The separate S3 21-pair timing characterization did not cross the ±5%
materiality threshold. This replay validates correctness and metric
reproducibility only; it is not a timing replication or promotion signal.
