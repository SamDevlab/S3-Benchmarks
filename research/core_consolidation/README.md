# S3 Core Consolidation — audit and local baseline

Date: **2026-11-15**. This is an evidence campaign,
not a compiler release. It never merges code or invokes
GitHub Actions.

## Source of truth

- Canonical Kanban: Relat-rio branch
  `feat/native-kanban-flow-v1-20261111`, PR #38;
  cards KB-0027…KB-0034.
- Native code candidate: S3 branch
  `exp/s3-v18-autoguard-loop-versioning` at
  `1a323a033c361d904aa6b9ce747364f7ee05255e`.
- Historical `main`: `9b39c7070d7bfa23d709c2128eb0b0bbef164177`.
  There are 663 commits in the candidate after main;
  the two are **not an equivalent native performance A/B**.
- Open PR snapshots were collected read-only using
  Windows `gh pr list`, in three `prs_*.json` files.

## Reproduction on the authorized Windows+WSL machine

Windows PowerShell (read-only GitHub queries; **no Actions**):

```powershell
gh pr list --repo SamDevlab/S3 --state open --limit 200 --json number,title,baseRefName,headRefName,isDraft,state,url,mergeStateStatus > prs_s3_open.json
gh pr list --repo SamDevlab/S3-Benchmarks --state open --limit 200 --json number,title,baseRefName,headRefName,isDraft,state,url,mergeStateStatus > prs_benchmarks_open.json
gh pr list --repo SamDevlab/Relat-rio --state open --limit 200 --json number,title,baseRefName,headRefName,isDraft,state,url,mergeStateStatus > prs_relatorio_open.json
```

The above are examples for a future new snapshot; **do not
overwrite the dated 2026-11-15 evidence files** without
changing their snapshot date/version.

The `git_refs_20261115.json` file was captured with Windows
Git because WSL Git cannot resolve Windows-absolute
`.git` pointers in these worktrees.

WSL:
```bash
python3 research/core_consolidation/collect_core.py
python3 research/core_consolidation/run_local_baseline.py
python3 research/core_consolidation/refresh_baseline.py
python3 research/core_consolidation/finalize_baseline.py
python3 -m pytest -q research/core_consolidation/test_core_consolidation.py
```

Run in the V18 S3-Benchmarks checkout with matching
sibling worktrees. The initial baseline commands were
executed locally and logs/JSON committed here. Re-running
the baseline overwrites dated logs and is a **new trial**;
archive or version the old evidence first.

## Recorded outcome

- Candidate: **246 selected tests passed**, two known
  inherited selectors explicitly deselected (separately
  run and failed as anticipated).
- Historical main: **61 tests passed**, different test
  matrix and code era.
- Artifact validators V15–V18: **21 passed**.
- Snapshot: **27 target PRs** from V11–V18 across
  three repositories, V12 parallel branches identified.
- No GitHub Actions job used, no claim of green CI.
- No GPU, Compact or DOOM change; no merge/deploy/default.

See `baseline_20261115.json`, `pr_stack_20261115.json`
and `DEPENDENCIES_20261115.md` for exact commands,
SHAs, test logs, PR URLs and conservative integration gates.
