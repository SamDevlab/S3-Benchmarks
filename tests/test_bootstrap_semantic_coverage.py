from tools.summarize_bootstrap_semantic_coverage import summarize


def test_case_passes_do_not_promote_authoritative_surface() -> None:
    snapshot = {"semantic_ir": {"typed_values": "BLOCKED"}}
    differential = {
        "cases": [
            {
                "case_id": "a",
                "required_surfaces": ["typed_values"],
                "classification": "PASS",
            }
        ]
    }
    report = summarize(snapshot, differential)
    row = report["surfaces"]["typed_values"]
    assert row["authoritative_ir_state"] == "BLOCKED"
    assert row["parity_pass_cases"] == 1
    assert row["case_evidence_promotes_ir_surface"] is False


def test_blocked_and_mismatch_counts_remain_distinct() -> None:
    snapshot = {"semantic_ir": {}}
    differential = {
        "cases": [
            {
                "required_surfaces": ["call_dataflow"],
                "classification": "STAGE1_BLOCKED",
            },
            {
                "required_surfaces": ["call_dataflow"],
                "classification": "SEMANTIC_MISMATCH",
            },
        ]
    }
    report = summarize(snapshot, differential)
    assert report["stage1_blocked_cases"] == 1
    assert report["semantic_mismatches"] == 1
    assert report["surfaces"]["call_dataflow"]["applicable_cases"] == 2
