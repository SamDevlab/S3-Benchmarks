"""Schema and invariant tests for S3 V5.5 Psychohistory benchmark artifacts."""

from __future__ import annotations

import json
from pathlib import Path

_BENCH_DIR = Path(__file__).resolve().parents[1] / "benchmarks" / "v5_5_psychohistory"


def test_v5_5_benchmark_artifacts_present_and_valid() -> None:
    res_json = _BENCH_DIR / "results.json"
    res_csv = _BENCH_DIR / "results.csv"
    readme = _BENCH_DIR / "README.md"
    assert res_json.exists(), "Missing benchmarks/v5_5_psychohistory/results.json"
    assert res_csv.exists(), "Missing benchmarks/v5_5_psychohistory/results.csv"
    assert readme.exists(), "Missing benchmarks/v5_5_psychohistory/README.md"

    payload = json.loads(res_json.read_text(encoding="utf-8"))
    assert payload["campaign"] == "S3_V5_5_PSYCHOHISTORY_RESEARCH"

    disc = payload["discovery"]
    assert len(disc["speedup_rows"]) >= 6
    assert disc["negative_control"]["lowered"] is False
    assert disc["negative_control"]["status"] == "DISCOVERY_REJECTED_UNVERIFIED"
    for row in disc["speedup_rows"]:
        assert row["verification_status"] == "PROVED_EXACT"
        assert row["parity_exact"] is True

    scaling_rows = payload["scaling"]["scaling_rows"]
    ns_seen = {r["n_agents"] for r in scaling_rows}
    assert {100, 1_000, 10_000, 100_000, 1_000_000} <= ns_seen
    for row in scaling_rows:
        assert row["max_abs_err_vs_c11"] == 0.0
        assert row["s3_native_ms"] > 0.0
        assert row["c11_gcc_o3_ms"] > 0.0

    decisions = {u["decision"] for u in payload["prediction"]["unknown_routing"]}
    assert {
        "EXACT_FAST_FORWARD",
        "STATISTICAL_FORECAST",
        "MONTE_CARLO_SIMULATION",
        "CONVENTIONAL_SIMULATION",
        "INSUFFICIENT_EVIDENCE",
    } <= decisions

    hyps = {h["hypothesis_id"]: h for h in payload["hypotheses_and_compression"]["hypotheses"]}
    assert len(hyps) == 6
    for comp in payload["hypotheses_and_compression"]["checkpoint_compression"]:
        assert comp["sha256_verified"] is True
