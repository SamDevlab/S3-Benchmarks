# S3 Evidence Lab 2.0 Capability Coverage

Registry digest: `b05c980a1275d4433de51f728f530d1a947f2198ee041191c5ac63c962d67cbf`

| Workload | Family | Status | Correctness | Native | Measured |
|---|---|---|---|---|---|
| `compiler.tsvc.initial` | compiler | NOT_SUPPORTED_YET | False | False | False |
| `hpc.prk.initial` | hpc | NOT_SUPPORTED_YET | False | False | False |
| `language.plb2.matmul` | language | NOT_SUPPORTED_YET | False | False | False |
| `memory.babelstream.initial` | memory | NOT_SUPPORTED_YET | False | False | False |
| `numerical.polybench.initial` | numerical | NOT_SUPPORTED_YET | False | False | False |
| `realworld.jsmn` | realworld | CORRECTNESS_PASS | True | False | False |
| `scientific.rmsd.batch` | scientific | NOT_SUPPORTED_YET | False | False | False |
| `scientific.rmsd.matrix` | scientific | NOT_SUPPORTED_YET | False | False | False |
| `scientific.rmsd.single` | scientific | CORRECTNESS_PASS | True | False | False |

## Missing capabilities

| Capability | Workload count | Workloads |
|---|---:|---|
| `bounded-array-workload-driver` | 1 | `memory.babelstream.initial` |
| `corpus-audit` | 1 | `compiler.tsvc.initial` |
| `multidimensional-data` | 3 | `language.plb2.matmul`, `numerical.polybench.initial`, `scientific.rmsd.matrix` |
| `parallel-execution` | 1 | `hpc.prk.initial` |
| `whole-program-batch-composition` | 1 | `scientific.rmsd.batch` |
