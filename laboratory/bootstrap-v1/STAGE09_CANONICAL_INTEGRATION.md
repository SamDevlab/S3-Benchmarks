# Stage09 canonical integration authorization firewall

Stage09 is forbidden unless the live control plane simultaneously says:

```text
active_stage=09_CANONICAL_INTEGRATION
canonical_stage1_mutation_authorized=true
```

and exact Stage08 canonical-input evidence is PASS.

The Benchmark-side tool `tools/check_stage09_authorization.py` never edits S3. It only returns `AUTHORIZED_HANDOFF` or `NOT_AUTHORIZED`.

Even when Stage09 is authorized:

- SELF_EMIT remains separately unauthorized unless its own later control bit is true;
- Stage2/Stage3/T4 remain separately unauthorized;
- S3IR2 v2 may not be redesigned as part of canonical integration;
- the expected integration is the smallest reviewable patch implementing already-qualified semantics.

A Stage09 authorization result is therefore a firewall decision, not a compiler mutation.
