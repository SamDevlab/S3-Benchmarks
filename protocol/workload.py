"""Deterministic workload and variant contracts.

The model is deliberately data-oriented.  Workload manifests describe what is
being measured; adapters provide the implementation-specific execution.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import json
from pathlib import Path
from typing import Any


class WorkloadStatus(StrEnum):
    CANDIDATE = "CANDIDATE"
    UPSTREAM_PINNED = "UPSTREAM_PINNED"
    IMPLEMENTED = "IMPLEMENTED"
    CORRECTNESS_PASS = "CORRECTNESS_PASS"
    NATIVE_PASS = "NATIVE_PASS"
    MEASURED = "MEASURED"
    REPRODUCED = "REPRODUCED"
    EXTERNALIZED = "EXTERNALIZED"
    NOT_SUPPORTED_YET = "NOT_SUPPORTED_YET"


@dataclass(frozen=True, slots=True)
class BenchmarkWorkload:
    id: str
    family: str
    description: str
    upstream_reference: str | None
    upstream_sha: str | None
    work_unit: str
    input_sizes: tuple[str, ...]
    reference_variants: tuple[str, ...]
    s3_variants: tuple[str, ...]
    correctness_contract: dict[str, Any]
    build_recipe: dict[str, Any]
    run_recipe: dict[str, Any]
    measurement_protocol: dict[str, Any]
    capability_requirements: tuple[str, ...]
    status: WorkloadStatus

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "BenchmarkWorkload":
        required = {
            "id", "family", "description", "work_unit", "input_sizes",
            "reference_variants", "s3_variants", "correctness_contract",
            "build_recipe", "run_recipe", "measurement_protocol",
            "capability_requirements", "status",
        }
        missing = sorted(required.difference(raw))
        if missing:
            raise ValueError(f"workload missing required fields: {', '.join(missing)}")
        workload = cls(
            id=_text(raw["id"], "id"),
            family=_text(raw["family"], "family"),
            description=_text(raw["description"], "description"),
            upstream_reference=_optional_text(raw.get("upstream_reference")),
            upstream_sha=_optional_text(raw.get("upstream_sha")),
            work_unit=_text(raw["work_unit"], "work_unit"),
            input_sizes=_texts(raw["input_sizes"], "input_sizes"),
            reference_variants=_texts(raw["reference_variants"], "reference_variants"),
            s3_variants=_texts(raw["s3_variants"], "s3_variants"),
            correctness_contract=_mapping(raw["correctness_contract"], "correctness_contract"),
            build_recipe=_mapping(raw["build_recipe"], "build_recipe"),
            run_recipe=_mapping(raw["run_recipe"], "run_recipe"),
            measurement_protocol=_mapping(raw["measurement_protocol"], "measurement_protocol"),
            capability_requirements=_texts(raw["capability_requirements"], "capability_requirements"),
            status=WorkloadStatus(raw["status"]),
        )
        if not workload.id or "/" in workload.id or "\\" in workload.id:
            raise ValueError(f"invalid workload id: {workload.id!r}")
        if workload.status is WorkloadStatus.NOT_SUPPORTED_YET:
            for field in ("first_missing_capability", "evidence", "minimum_required_capability"):
                if not workload.correctness_contract.get(field):
                    raise ValueError(f"NOT_SUPPORTED_YET workload needs correctness_contract.{field}")
        return workload

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "family": self.family,
            "description": self.description,
            "upstream_reference": self.upstream_reference,
            "upstream_sha": self.upstream_sha,
            "work_unit": self.work_unit,
            "input_sizes": list(self.input_sizes),
            "reference_variants": list(self.reference_variants),
            "s3_variants": list(self.s3_variants),
            "correctness_contract": self.correctness_contract,
            "build_recipe": self.build_recipe,
            "run_recipe": self.run_recipe,
            "measurement_protocol": self.measurement_protocol,
            "capability_requirements": list(self.capability_requirements),
            "status": self.status.value,
        }


def load_workload(path: Path) -> BenchmarkWorkload:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"workload manifest must be an object: {path}")
    return BenchmarkWorkload.from_dict(raw)


def canonical_json(value: Any) -> str:
    """Serialize a protocol value independent of source object insertion order."""

    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def _text(value: Any, field: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    return value


def _optional_text(value: Any) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("optional text field must be a string or null")
    return value


def _texts(value: Any, field: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{field} must be a list of strings")
    return tuple(value)


def _mapping(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return value
