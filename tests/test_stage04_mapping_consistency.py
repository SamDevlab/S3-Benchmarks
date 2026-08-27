from __future__ import annotations

import json
from pathlib import Path

from tools.generate_bootstrap_fuzz_corpus import cases

ROOT = Path(__file__).resolve().parents[1]


def _load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_stage_map_references_only_existing_corpus_cases() -> None:
    corpus_ids = {case.case_id for case in cases()}
    stage_map = _load("laboratory/bootstrap-v1/s3ir2-v2-stage-map.json")
    referenced = {
        case_id
        for stage in stage_map["stages"].values()
        for case_id in stage["required_cases"]
    }
    assert referenced <= corpus_ids


def test_stage04_capability_matrix_references_only_existing_corpus_cases() -> None:
    corpus_ids = {case.case_id for case in cases()}
    matrix = _load("laboratory/bootstrap-v1/stage04-capability-matrix.json")
    referenced = {
        case_id
        for capability in matrix["capabilities"].values()
        for case_id in capability.get("fixtures", [])
    }
    assert referenced <= corpus_ids


def test_stage04_stage_map_requires_new_focused_expression_cases() -> None:
    stage_map = _load("laboratory/bootstrap-v1/s3ir2-v2-stage-map.json")
    required = set(stage_map["stages"]["04_EXPRESSIONS_S1_S2"]["required_cases"])
    assert "relational_precedence_v06" in required
    assert "mutable_reassignment_example" in required
    assert "wide_literal_negative" in required
