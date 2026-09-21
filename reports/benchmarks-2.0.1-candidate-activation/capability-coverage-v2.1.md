# Capability Coverage v2.1

This is a compatibility audit for the TSVC upstream corpus. It is not a
claim that the TSVC source has been implemented or vendored into S3-Benchmarks.

- Upstream pin: `badf9adb2974867ac0937718d85a44dec6dec95a`
- Source: `src/tsvc.c`
- Named loops audited: 138
- Representative loops audited in detail: 18
- TSVC source vendored: no
- Exact TSVC implementation in this campaign: no; the existing candidate
  adapters are independent S3 workloads selected from the same capability
  families.

The machine-readable classifications are in
`references/tsvc-loop-audit-v2.1.json`. `SUPPORTED_WITH_BENCHMARK_ADAPTER`
means the loop shape can be represented by an independent S3 workload adapter;
it does not mean that the upstream C source was copied or that a performance
result exists. `LAYOUT_ADAPTER_REQUIRED` and
`DATA_DEPENDENCE_ADAPTER_REQUIRED` identify shapes requiring additional
workload design before faithful activation.
