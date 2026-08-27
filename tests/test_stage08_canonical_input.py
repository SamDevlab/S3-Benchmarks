from __future__ import annotations

import hashlib

from tools.validate_stage08_canonical_input import validate


CONTRACT = {
    "stage_id": "08_CANONICAL_SOURCE_INPUT",
    "required_pass_fields": [
        "canonical_source_as_input",
        "canonical_source_v2_conformance",
        "canonical_source_determinism",
        "native_provenance",
        "s1_typed_values",
        "s2_def_use",
        "s3_call_dataflow",
        "s4_complete_terminators",
        "s5_canonical_serialization",
    ],
    "next_stage_candidate": "09_CANONICAL_INTEGRATION",
    "authorization_after_pass": "RECHECK_LIVE_CONTROL_CANONICAL_STAGE1_MUTATION_AUTHORIZATION",
}


def _checkpoint(source: bytes) -> dict:
    return {
        "stage_id": "08_CANONICAL_SOURCE_INPUT",
        "candidate_git_sha": "a" * 40,
        "candidate_source_sha256": "b" * 64,
        "candidate_binary_sha256": "c" * 64,
        "canonical_source_sha256": hashlib.sha256(source).hexdigest(),
        "canonical_source_bytes": len(source),
        "stream_sha256": "d" * 64,
        "gates": {field: "PASS" for field in CONTRACT["required_pass_fields"]},
        "invariants": {"canonical_source_mutated": False, "z_mask": 31},
    }


def test_stage08_accepts_exact_canonical_source_binding() -> None:
    source = b"fn main() -> tryte:\n    return 0\n"
    report = validate(CONTRACT, _checkpoint(source), source)
    assert report["status"] == "PASS"
    assert report["canonical_mutation_authorized_by_this_tool"] is False
    assert report["next_stage_candidate"] == "09_CANONICAL_INTEGRATION"


def test_stage08_rejects_source_relabeling() -> None:
    source = b"fn main() -> tryte:\n    return 0\n"
    other = b"fn main() -> tryte:\n    return 1\n"
    report = validate(CONTRACT, _checkpoint(source), other)
    assert report["status"] == "BLOCKED"
    assert any("canonical_source_sha256" in error for error in report["errors"])


def test_stage08_rejects_mutated_canonical_flag() -> None:
    source = b"fn main() -> tryte:\n    return 0\n"
    checkpoint = _checkpoint(source)
    checkpoint["invariants"]["canonical_source_mutated"] = True
    report = validate(CONTRACT, checkpoint, source)
    assert report["status"] == "BLOCKED"
    assert any("canonical_source_mutated" in error for error in report["errors"])


def test_stage08_requires_z31() -> None:
    source = b"fn main() -> tryte:\n    return 0\n"
    checkpoint = _checkpoint(source)
    checkpoint["invariants"]["z_mask"] = 15
    report = validate(CONTRACT, checkpoint, source)
    assert report["status"] == "BLOCKED"
    assert any("z_mask" in error for error in report["errors"])


def test_stage08_blocks_missing_native_provenance() -> None:
    source = b"fn main() -> tryte:\n    return 0\n"
    checkpoint = _checkpoint(source)
    checkpoint["gates"]["native_provenance"] = "BLOCKED"
    report = validate(CONTRACT, checkpoint, source)
    assert report["status"] == "BLOCKED"
    assert "native_provenance" in report["blocked_fields"]
