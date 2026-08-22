# RC1 Linux automation activation

The SSH transport was validated against the existing Linux VM. The connection
was non-interactive, stdout and stderr were captured, remote exit status was
observable, a bounded executor timeout returned 124, and no credentials were
persisted.

The RC1 S3 checkout was clean at
`9b39c7070d7bfa23d709c2128eb0b0bbef164177`. The Linux toolchain was available
with GCC/CC, x86-64, and KVM virtualization.

The activation stopped before `preflight-only`. The only available benchmark
checkout was at `6ae9e1f8bcff79557c02eb20c786e70d42eeda1d` and contained
untracked historical reports, while this campaign requires the exact final
automation HEAD `675593cd5d57c885c430484ba1c68061bc82d904`. Existing remote
checkouts were not changed or cleaned to manufacture a valid candidate.

Therefore no C control samples or RC1 timing smoke were run. Performance
eligibility is unknown and conservatively `NO`; no weekly run is authorized by
this activation. The local Windows semantics are now explicit:
`NOT_RUN_PLATFORM` is `CORRECTNESS_PARTIAL_BY_PLATFORM`, not a correctness
failure, regression, or automation failure, and returns exit 0 when it is the
only limitation.

Historical V1/V2 evidence, S3, RC1, T4, and all remote checkouts remain
unchanged. Scheduler registration, benchmark merge, T4, full suite, shutdown,
and reboot were not performed.
