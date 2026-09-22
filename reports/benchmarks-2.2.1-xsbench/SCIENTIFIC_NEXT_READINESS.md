# Scientific Next Readiness

## miniBUDE

```text
UPSTREAM=UoB-HPC/miniBUDE
SHA=570f66c1fd0c29b7f3ab6fa96fba87f4561aa44c
LICENSE=Apache-2.0
READINESS=READY_WITH_ADAPTERS
IMPLEMENTED=NO
TIMING=NOT_RUN
```

The audit identified the serial docking-energy kernel, flat/vector-like input
data, and implementations across serial, OpenMP, CUDA, HIP, SYCL and other
models. The core uses `sqrt` and float-valued paths and the complete project
has model-specific drivers and input-deck generation. A future S3 subset can
be audited around the serial kernel with explicit adapters, but the full
application is not ready for implementation in this PR.

## miniMD

```text
UPSTREAM=Mantevo/miniMD
SHA=2662065eb2b2264a673bda780a23d296f05a2c87
LICENSE=LGPL-3.0
READINESS=MAJOR_CAPABILITY_GAPS
IMPLEMENTED=NO
TIMING=NOT_RUN
```

The reference tree is a parallel C++ molecular-dynamics application with MPI
and OpenMP variants, spatial decomposition, mutable atom/neighbor data, and
sqrt/pow-heavy force and setup paths. A serial kernel subset might be a future
adapter target, but full miniMD readiness is not established by this audit.

```text
MINIBUDE_TIMING=NOT_RUN
MINIMD_IMPLEMENTED=NO
```
