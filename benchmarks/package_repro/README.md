# S3 Package Resolver / Cache / Reproducibility Preflight

This workload promotes Candidate F from the post-M1.80 benchmark plan into an executable **correctness-only** gate.

It exercises the S3 package dependency resolver (M1.56), read-only content-addressed registry client (M1.79), and reproducible local toolchain bundler (M1.80).

## Rule

> **CORRECTNESS BEFORE PERFORMANCE.**

Cargo and uv are pinned external references for architecture and future workload design. This preflight does **not** execute them and does not claim S3 is faster or feature-equivalent.

## Covered contracts

### Dependency lock

- mapping-order independent lock output;
- stable lock SHA-256;
- deterministic topological order;
- identical multi-parent dependency identity accepted;
- conflicting reachable `(source, revision)` identity rejected;
- unreachable conflicting references do not influence the lock;
- root identity remains `source="."`, `revision=None`.

### Registry/cache

- exact content-addressed lock resolution;
- read-only registry surface;
- successful cache reuse after the source object disappears;
- SHA-256 verification on cache hits;
- deterministic installation path ordering;
- archive path traversal rejection;
- duplicate canonical path rejection;
- bounded member size enforcement;
- registry publishing remains unavailable.

### Reproducible toolchain bundle

- byte-identical output across input mapping order;
- stable bundle SHA-256;
- deterministic manifest file ordering;
- deterministic ZIP entry ordering;
- fixed ZIP timestamps and permissions;
- LICENSE inclusion;
- checksum verification;
- corruption rejection;
- Windows-machine/absolute-style path rejection;
- traversal and reserved-path rejection;
- remote release publishing remains unavailable.

## Provenance

Required S3 baseline:

`SamDevlab/S3@cd6804f72757d6936ca1ec6c20d5badf55d1aac4`

Pinned external references:

- `rust-lang/cargo@514c56dd7321eecbfdcf9b6479519cf4edfab906`
- `astral-sh/uv@5c170b8022c5565a1d4ada3406077d8fdf7f9088`

The runner refuses a different S3 HEAD and also fails if either pinned Cargo/uv reference in `references/upstreams-m171-m180.json` drifts from these SHAs.

Cargo and uv remain metadata/reference inputs only in this gate; they are not cloned, built, or executed.

## Run

```bash
S3_CURRENT_REPO=/path/to/S3 python tools/package_repro_runner.py --verify-only
```

Default report:

`reports/package-repro-correctness.json`

## Performance status

`DEFERRED_UNTIL_EQUIVALENT_NATIVE_RESOLVER_WORKLOAD_EXISTS`

A later timing campaign may compare bounded local dependency resolution/cache workloads only after:

1. equivalent workload definitions exist for S3 and the selected reference;
2. all inputs are local and immutable;
3. cold-cache and warm-cache phases are separated;
4. correctness and lock/content identity are proven before timing;
5. process startup and filesystem cache effects are reported honestly.

Live public registries are not required for correctness and must not be used to make reproducibility depend on network conditions.
