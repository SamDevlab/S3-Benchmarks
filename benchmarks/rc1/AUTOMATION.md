# RC1 Automation

`python -m benchmarks.rc1.automation` is the bounded, non-interactive entry
point for scheduled RC1 checks. It creates a new run directory containing the
manifest, environment identity, correctness result, preflight samples, timing
artifacts, regression status, and machine-readable status.

## Modes

| Mode | Correctness | Preflight | Timing |
| --- | --- | --- | --- |
| `fast` | P1, P7, P8, P9 | no | no |
| `correctness-only` | P1, P7, P8, P9 | no | no |
| `preflight-only` | no | C control only | no |
| `nightly` | P1, P7, P8, P9 | yes | bounded, only when eligible |
| `weekly` | P1, P7, P8, P9 | yes | bounded, only when eligible |
| `performance` | P1, P7, P8, P9 | yes | explicit bounded campaign |

Correctness is never promoted to a performance result. The control preflight
uses five blocks with ten samples per block by default. Drift at or below 3%
is `STABLE`; drift above 3% and at or below 5% is `MARGINAL`; drift above 5%
or an obvious monotonic host trend is `UNSTABLE`. Only `STABLE` and `MARGINAL`
allow timing. An unstable environment is an infrastructure measurement result,
not a compiler regression.

The current RC1 is pinned to:

```text
S3_SHA=9b39c7070d7bfa23d709c2128eb0b0bbef164177
S3_TAG=v1.0.0-rc1
```

Every invocation requires exact S3 and benchmark repository HEADs. The RC1 tag
is peeled before comparison so an annotated tag object is never confused with
its commit target. The runner refuses to time when provenance or correctness is
not exact.

Examples:

```bash
python -m benchmarks.rc1.automation --mode fast \
  --s3-repo /path/to/S3 \
  --s3-sha 9b39c7070d7bfa23d709c2128eb0b0bbef164177 \
  --benchmark-sha "$(git rev-parse HEAD)"

python -m benchmarks.rc1.automation --mode preflight-only \
  --s3-repo /path/to/S3
```

`--ssh-host`, `--ssh-port`, and `--ssh-user` are accepted as transport
configuration for a pre-staged Linux executor. Credentials are never stored
in the repository. No scheduler, cron job, service, shutdown, or reboot is
registered by this repository; external scheduling invokes one bounded command
at a time.

Historical V1/V2 evidence remains under `reports/rc1-longitudinal-native-20260822`
and is not rewritten by automation runs. Only a run that has correctness,
provenance, eligible control drift, raw samples, and valid statistics is
eligible for `history/runs.jsonl`.
