from __future__ import annotations

from tools.validate_control_route_snapshot import validate


CONTRACT = {
    "sequence": [
        {"id": "01", "file": "a.md", "authorization": None},
        {"id": "09", "file": "b.md", "authorization": "canonical_stage1_mutation_authorized"},
    ]
}


def _live() -> dict:
    return {
        "sequence": [
            {"id": "01", "file": "a.md", "authorization": None},
            {"id": "09", "file": "b.md", "authorization": "canonical_stage1_mutation_authorized"},
        ],
        "authorization_rule": "Never infer authorization. Re-fetch CURRENT.json immediately before gated stages/actions.",
        "failure_rule": "On a failed stage gate, remain in that stage while implementing/fixing the failing semantic slice.",
    }


def test_control_route_exact_match() -> None:
    report = validate(CONTRACT, _live())
    assert report["status"] == "MATCH"
    assert report["changes"] == []


def test_control_route_detects_reordered_stage() -> None:
    live = _live()
    live["sequence"] = list(reversed(live["sequence"]))
    report = validate(CONTRACT, live)
    assert report["status"] == "DRIFT_DETECTED"
    assert report["changes"]


def test_control_route_detects_authorization_mapping_change() -> None:
    live = _live()
    live["sequence"][1]["authorization"] = None
    report = validate(CONTRACT, live)
    assert report["status"] == "DRIFT_DETECTED"
    assert report["requires_control_contract_review"] is True


def test_control_route_detects_added_stage() -> None:
    live = _live()
    live["sequence"].append({"id": "10", "file": "c.md", "authorization": None})
    report = validate(CONTRACT, live)
    assert report["status"] == "DRIFT_DETECTED"
    assert report["observed_stage_count"] == 3
