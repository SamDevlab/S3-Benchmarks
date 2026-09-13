# P1 V2 sample-level summary

`SAMPLE_LEVEL_DATA_AVAILABLE=YES`

Both allowed H4/H5 attempts passed native correctness before timing and
produced 180 paired samples. Attempt 1 control drift was `72.1146%`; the one
bounded post-cooldown retry was `13.0953%`. Since both exceed the `5%` gate,
`CONTROL_DRIFT=HIGH` and the final P1 classification is
`INCONCLUSIVE_ENVIRONMENT`.

H4/M2.30 to H5/RC1 raw geomean delta: `+0.3703%`.

Paired median delta: `-0.0550%`; bootstrap CI95:
`[-0.4553%, +0.6191%]`; classification: `INCONCLUSIVE`.

RC1/C-O2 same-run geomean: `48.1984x`.
C-O3: `NOT_MEASURED_IN_P1_V2`.

The retry raw vectors are `raw/samples.json` and `raw/samples.csv`.
Attempt 1 is preserved under `raw/attempt-1/`.
