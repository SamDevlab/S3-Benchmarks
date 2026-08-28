# Prepared bootstrap route beyond the live Codex stage

The live S3 control plane remains authoritative. At the time this document was prepared it was observed at revision 5 / `04_EXPRESSIONS_S1_S2`.

Everything below Stage04 is preparation only until the live control branch selects the corresponding stage.

## Prepared sequence

```text
04 expressions / S1-S2      ACTIVE IN CONTROL PLANE
  ↓
05 calls + arrays / S3      PREPARED_NOT_ACTIVE
  ↓
06 control flow / S4        PREPARED_NOT_ACTIVE
  ↓
07 serialization / S5       PREPARED_NOT_ACTIVE
  ↓
08 canonical source INPUT   PREPARED_NOT_ACTIVE
  ↓
09 canonical integration    AUTHORIZATION FIREWALL ONLY
  ↓
10 General Emitter          PREPARED EVIDENCE GATE
  ↓
11 SELF_EMIT / Stage2 /
   Stage3 / T4              PER-ACTION FIREWALLS ONLY
```

## Stage06

Prepared S4 coverage requires explicit RETURN/JUMP/BRANCH3 semantics, negative/zero/positive target order and 100% terminator coverage for qualified blocks. `Z 31` is rejected during Stage06.

## Stage07

Prepared S5 coverage requires all `F/B/V/M/I/O/R/C/A/T/Z` record families, strict conformance and at least three independently proven native repeats with byte-identical streams. Stage07 requires exact `Z 31`.

## Stage08

The canonical Stage1 source is input only. `validate_stage08_canonical_input.py` recomputes the supplied canonical source SHA256/bytes and rejects source relabeling. Passing Stage08 does not authorize canonical mutation.

## Stage09

`check_stage09_authorization.py` is a firewall. It requires Stage08 PASS plus live `active_stage=09_CANONICAL_INTEGRATION` and `canonical_stage1_mutation_authorized=true`. The tool itself never mutates S3 and does not authorize SELF_EMIT.

## Stage10

The prepared General Emitter gate requires semantic-record consumption, no self-source special cases, ABI preservation, fail-closed unsupported opcodes, focused native codegen, General Emitter PASS and canonical Stage1 emission PASS. Stage10 PASS still does not authorize SELF_EMIT.

## Stage11

`check_stage11_action_authorization.py` evaluates exactly one action at a time:

- SELF_EMIT requires its own live authorization plus S1-S5/General Emitter/canonical emission PASS;
- Stage2 requires its own authorization plus real SELF_EMIT PASS;
- Stage3 requires its own authorization plus real Stage2 PASS;
- T4 requires its own authorization plus SELF_EMIT, Stage2, Stage3 and required equivalence PASS.

No later authorization is inferred from an earlier one.

## Route drift

`control-route-contract.json` records the observed Stage01-11 order and authorization mapping. `validate_control_route_snapshot.py` compares a later live `STAGE_SEQUENCE.json` snapshot against it. Any ordering/file/authorization change becomes `DRIFT_DETECTED` and requires review before reusing these prepared gates.

## Safety boundary

This entire prepared route has:

```text
S3_MUTATION=NO
PR268_MUTATION=NO
CANONICAL_STAGE1_MUTATION=NO
SELF_EMIT_EXECUTION=NO
STAGE2_CREATION=NO
STAGE3_CREATION=NO
T4_EXECUTION=NO
PROMOTION=NO
```

It is evidence/control infrastructure only.
