"""Pinned, correctness-first workload contracts for the RC1 campaign.

The contracts deliberately do not pretend that a contract probe is a native
performance result.  A workload becomes canonical only after its S3 input,
oracle, provenance, raw output, and timing boundary have all been exercised.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from typing import Any


COMPARISON_CLASSES = frozenset(
    {"S3_LONGITUDINAL", "S3_VS_C", "CURRENT_CAPABILITY", "STRUCTURAL_ONLY"}
)


@dataclass(frozen=True, slots=True)
class WorkloadContract:
    workload_id: str
    name: str
    comparison_class: str
    input_contract: str
    expected_output: str
    oracle: str
    timing_boundary: str
    capability_note: str

    def __post_init__(self) -> None:
        if self.comparison_class not in COMPARISON_CLASSES:
            raise ValueError(f"unsupported comparison class: {self.comparison_class}")
        if not self.workload_id.startswith("P"):
            raise ValueError(f"invalid workload id: {self.workload_id}")

    def canonical_payload(self) -> bytes:
        value = {
            "workload_id": self.workload_id,
            "name": self.name,
            "comparison_class": self.comparison_class,
            "input_contract": self.input_contract,
            "expected_output": self.expected_output,
            "oracle": self.oracle,
            "timing_boundary": self.timing_boundary,
            "capability_note": self.capability_note,
        }
        return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


WORKLOADS: tuple[WorkloadContract, ...] = (
    WorkloadContract("P2", "cold compiler latency", "S3_LONGITUDINAL", "pinned small/medium/multi-module projects", "artifact manifest and output digest", "exact output digest and artifact existence", "process wall time from compiler invocation to artifact close", "incremental project corpus is not yet part of the public S3 CLI"),
    WorkloadContract("P3", "incremental no-change build", "S3_LONGITUDINAL", "pinned project followed by byte-identical rebuild", "unchanged artifact and cache accounting", "artifact digest plus cache-event oracle", "initial build and no-change rebuild as separate timed regions", "incremental query/cache API is not exposed by the current RC1 harness"),
    WorkloadContract("P4", "direct leaf invalidation", "S3_LONGITUDINAL", "pinned multi-module project with one private leaf edit", "only permitted dependent artifacts change", "dependency graph and output digest oracle", "rebuild invocation after one controlled source edit", "dependency invalidation counters are not exposed by the current RC1 harness"),
    WorkloadContract("P5", "transitive interface invalidation", "S3_LONGITUDINAL", "pinned dependency graph with one public interface edit", "all transitive dependents rebuild", "negative cache-hit oracle plus artifact digest", "rebuild invocation after public interface edit", "workspace invalidation protocol requires a future S3 project runner"),
    WorkloadContract("P6", "generic specialization", "S3_LONGITUDINAL", "pinned generic-heavy source and instantiation list", "specialized output digest and specialization count", "semantic output and specialization manifest oracle", "compile and native execution as separate regions", "specialization reporting is not available in RC1"),
    WorkloadContract("P7", "native arithmetic control", "S3_VS_C", "paired S3/C integer kernels with pinned bytes", "exact result vector", "cross-language result-vector oracle", "native process execution excluding compilation", "a fair paired kernel corpus has not yet been promoted"),
    WorkloadContract("P8", "call stack and ABI", "S3_VS_C", "paired call/return kernels with pinned arguments", "exact return vector", "cross-language return-value oracle", "native process execution excluding compilation", "ABI corpus requires a separately reviewed source contract"),
    WorkloadContract("P9", "arrays structs and memory", "S3_VS_C", "paired bounded array/struct kernels with pinned bytes", "exact checksum and bounds behavior", "cross-language checksum oracle", "native process execution excluding compilation", "memory corpus requires a separately reviewed source contract"),
    WorkloadContract("P10", "async channels and select", "CURRENT_CAPABILITY", "bounded local task/channel trace", "ordered event trace and completion count", "deterministic event-trace oracle", "hosted runtime operation loop", "current benchmark harness has no isolated async runner"),
    WorkloadContract("P11", "HTTP/1 loopback", "CURRENT_CAPABILITY", "local loopback request/response trace", "status, response bytes, request count", "wire-level response oracle", "loopback client/server request latency", "loopback benchmark adapter is not yet part of this benchmark repository"),
    WorkloadContract("P12", "HTTP/2 protocol core", "CURRENT_CAPABILITY", "pinned frame/state transition sequence", "state trace and frame result digest", "protocol state oracle", "in-memory protocol transition loop", "HTTP/2 implementation capability is not exposed by the current RC1 harness"),
    WorkloadContract("P13", "package workspace resolver", "CURRENT_CAPABILITY", "deterministic local workspace graph", "resolved graph and package digest", "graph oracle with no network access", "cold and warm local resolution", "package resolver runner is not available in RC1"),
    WorkloadContract("P14", "formatter", "CURRENT_CAPABILITY", "pinned source corpus", "format(format(x)) equals format(x)", "idempotence and output-hash oracle", "formatter wall time over the pinned corpus", "formatter entry point is not available in the benchmark harness"),
    WorkloadContract("P15", "S3 test runner", "CURRENT_CAPABILITY", "pinned tiny and medium test manifests", "discovery and execution result manifest", "test-result manifest oracle", "framework overhead separated from test body", "current benchmark runner cannot invoke a canonical S3 test project"),
    WorkloadContract("P16", "FFI roundtrip", "S3_VS_C", "pinned tiny C/S3 call signatures", "exact return-value vector", "bidirectional return-value oracle", "native call loop excluding compilation", "FFI workload is not certified by the current benchmark harness"),
    WorkloadContract("P17", "documentation generation", "CURRENT_CAPABILITY", "pinned multi-module API corpus", "deterministic output hash", "output-hash oracle", "generation wall time", "documentation generator is not available in RC1"),
    WorkloadContract("P18", "real-world multi-module project", "S3_LONGITUDINAL", "pinned realistic multi-module S3 corpus", "native result and artifact manifest", "end-to-end result and hash oracle", "cold build and native execution as separate regions", "no realistic corpus has passed promotion gates in this campaign"),
)


def workload_map() -> dict[str, WorkloadContract]:
    result = {workload.workload_id: workload for workload in WORKLOADS}
    if len(result) != len(WORKLOADS):
        raise ValueError("duplicate workload id")
    return result


def run_contract_probe(workload: WorkloadContract) -> dict[str, Any]:
    """Run only the deterministic contract probe, never a timing claim."""

    payload = workload.canonical_payload()
    digest = sha256(payload).hexdigest()
    observed = json.loads(payload.decode("utf-8"))
    expected = workload.to_dict()
    passed = observed == expected
    return {
        "workload": workload.workload_id,
        "name": workload.name,
        "comparison_class": workload.comparison_class,
        "contract_probe": "PASS" if passed else "FAIL",
        "input_sha256": digest,
        "expected_output_defined": True,
        "correctness_oracle_defined": True,
        "inputs_pinned": True,
        "timing_boundary_documented": True,
        "performance_status": "DEFERRED_BY_CAPABILITY",
        "canonical_status": "EXPERIMENTAL_WORKLOAD",
        "native_timing": "NOT_RUN",
        "s3_vs_c_claim": "NO",
        "reason": workload.capability_note,
    }


def run_all_contract_probes() -> list[dict[str, Any]]:
    return [run_contract_probe(workload) for workload in WORKLOADS]

