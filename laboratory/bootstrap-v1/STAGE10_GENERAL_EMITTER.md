# Stage10 General Emitter qualification (prepared, inactive)

The General Emitter must consume the qualified semantic path rather than reconstructing semantics from lexical shortcuts.

Prepared gate requirements:

```text
CANONICAL_SEMANTIC_INTEGRATION=PASS
S1=PASS
S2=PASS
S3=PASS
S4=PASS
S5=PASS
FOCUSED_CODEGEN_NATIVE_FIXTURES=PASS
GENERAL_EMITTER=PASS
CANONICAL_STAGE1_EMISSION=PASS
```

Required design principles are evidence fields as well:

- semantic records, not lexical shortcuts;
- no self-source-specific special cases;
- ABI/signature semantics preserved;
- unsupported semantic opcodes remain fail-closed.

Exact candidate/canonical/emitter/artifact identities must be preserved.

A Stage10 PASS does **not** authorize SELF_EMIT. The live control plane must be re-read before Stage11 and its independent `self_emit_authorized` bit must be true.
