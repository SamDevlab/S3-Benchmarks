from __future__ import annotations

import json

from benchmarks.rc1.automation import (
    _append_history,
    _write_once,
    build_parser,
    classify_control_blocks,
    classify_regression,
    performance_allowed,
    SSHTransport,
)


def test_control_policy_has_stable_marginal_and_unstable_boundaries():
    stable = classify_control_blocks([100.0, 101.0, 100.5])
    marginal = classify_control_blocks([100.0, 104.0, 100.0])
    unstable = classify_control_blocks([100.0, 106.0, 100.0])

    assert stable["classification"] == "STABLE"
    assert stable["performance_eligible"] is True
    assert marginal["classification"] == "MARGINAL"
    assert marginal["performance_eligible"] is True
    assert unstable["classification"] == "UNSTABLE"
    assert unstable["performance_eligible"] is False


def test_performance_requires_correctness_and_preflight():
    stable = {"classification": "STABLE", "performance_eligible": True}
    unstable = {"classification": "UNSTABLE", "performance_eligible": False}

    assert performance_allowed(correctness_status="PASS", preflight=stable)
    assert not performance_allowed(correctness_status="FAIL", preflight=stable)
    assert not performance_allowed(correctness_status="PASS", preflight=unstable)
    assert not performance_allowed(correctness_status="PASS", preflight=None)


def test_regression_policy_is_fail_closed_without_comparable_samples():
    result = classify_regression(
        baseline_median=None,
        candidate_median=None,
        ci95=None,
        environment_status="STABLE",
        correctness_status="PASS",
    )
    assert result["status"] == "NONE"
    assert result["delta_percent"] is None


def test_correctness_failure_takes_precedence_over_environment():
    result = classify_regression(
        baseline_median=100.0,
        candidate_median=120.0,
        ci95=(10.0, 30.0),
        environment_status="UNSTABLE",
        correctness_status="FAIL",
    )
    assert result["status"] == "CORRECTNESS_FAILURE"


def test_run_evidence_is_write_once_and_history_is_append_only(tmp_path):
    evidence = tmp_path / "run" / "summary.json"
    _write_once(evidence, {"status": "PASS"})
    assert json.loads(evidence.read_text(encoding="utf-8"))["status"] == "PASS"

    history = tmp_path / "history" / "runs.jsonl"
    _append_history(history, {"run_id": "one"})
    _append_history(history, {"run_id": "two"})
    assert [json.loads(line)["run_id"] for line in history.read_text(encoding="utf-8").splitlines()] == ["one", "two"]


def test_cli_exposes_all_automation_modes():
    parser = build_parser()
    for mode in ("fast", "nightly", "weekly", "performance", "correctness-only", "preflight-only"):
        args = parser.parse_args(["--mode", mode])
        assert args.mode == mode


def test_ssh_transport_is_explicit_and_does_not_store_credentials():
    transport = SSHTransport("benchmark-host", port=2222, user="runner")
    assert transport.target == "runner@benchmark-host"
    assert transport.command(["python3", "-m", "benchmarks.rc1.automation"], cwd="/srv/bench") == [
        "ssh",
        "-p",
        "2222",
        "runner@benchmark-host",
        "cd -- /srv/bench && python3 -m benchmarks.rc1.automation",
    ]
