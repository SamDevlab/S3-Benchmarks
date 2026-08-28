from __future__ import annotations

from tools.compare_s3ir2_v2_campaigns import compare


def _campaign(
    *,
    native: str = "PASS",
    semantic: str = "PASS",
    deterministic: str = "PASS",
    stage: str = "PASS_EVIDENCE_SET",
) -> dict:
    return {
        "stages": {
            "07_SERIALIZATION_S5": {
                "status": stage,
                "cases": [
                    {
                        "case_id": "case_a",
                        "structural_status": "PASS",
                        "native_provenance_status": native,
                        "semantic_conformance_status": semantic,
                        "determinism_status": deterministic,
                    }
                ],
            }
        }
    }


def test_compare_detects_semantic_regression() -> None:
    report = compare(_campaign(), _campaign(semantic="FAIL", stage="SEMANTIC_CONFORMANCE_BLOCKED"))
    assert report["regression_gate"] == "FAIL"
    assert report["regression_count"] >= 2
    assert any(item["dimension"] == "semantic_conformance_status" for item in report["regressions"])


def test_compare_detects_native_provenance_regression() -> None:
    report = compare(_campaign(), _campaign(native="FAIL", stage="NATIVE_PROVENANCE_BLOCKED"))
    assert report["regression_gate"] == "FAIL"
    assert any(item["dimension"] == "native_provenance_status" for item in report["regressions"])


def test_compare_detects_determinism_regression() -> None:
    report = compare(_campaign(), _campaign(deterministic="FAIL", stage="DETERMINISM_BLOCKED"))
    assert report["regression_gate"] == "FAIL"
    assert any(item["dimension"] == "determinism_status" for item in report["regressions"])


def test_compare_reports_improvement_without_regression() -> None:
    report = compare(
        _campaign(semantic="FAIL", stage="SEMANTIC_CONFORMANCE_BLOCKED"),
        _campaign(),
    )
    assert report["regression_gate"] == "PASS"
    assert report["improvement_count"] >= 2
