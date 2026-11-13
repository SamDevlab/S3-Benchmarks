# Stage11 SELF_EMIT / Stage2 / Stage3 / T4 authorization firewalls

Stage11 contains four independent control-plane decisions. Passing one action never authorizes the next.

## SELF_EMIT

Requires live `self_emit_authorized=true` and proven S1-S5 + General Emitter + canonical Stage1 emission.

The self-emission proof must use the canonical/current Stage1 compiler path and must not delegate the core compile to Stage0/host shortcuts that would invalidate self-hosting evidence.

## Stage2

Requires live `stage2_authorized=true` plus a real successful SELF_EMIT artifact.

## Stage3

Requires live `stage3_authorized=true` plus a real Stage2 compiler artifact.

## T4

Requires live `t4_authorized=true` plus SELF_EMIT, Stage2, Stage3 and required Stage2/Stage3 equivalence all PASS.

`tools/check_stage11_action_authorization.py` evaluates exactly one requested action against one live control snapshot and prior evidence. It never executes SELF_EMIT, creates Stage2/Stage3, or runs T4.

This permits deliberate pauses between bootstrap milestones so evidence can be reviewed and the control route changed without implicit promotion.
