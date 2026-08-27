from __future__ import annotations

import json
import subprocess
from pathlib import Path

from tools.run_bootstrap_lab import run_lab


def _git_init(repo: Path) -> str:
    repo.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "lab@example.invalid"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "Bootstrap Lab"], check=True)
    marker = repo / ".lab-marker"
    marker.write_text("pinned\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(repo), "add", ".lab-marker"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-q", "-m", "fixture"], check=True)
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def _write_semantic_evidence(repo: Path) -> None:
    path = repo / "reports" / "selfhost" / "stage1" / "semantic-ir-requirements.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "schema": "s3.selfhost.stage1-semantic-ir-requirements.v1",
                "status": "BLOCKED_GENERAL_EMITTER_CAPABILITY_GAP",
                "stage1_self_emit": "BLOCKED_UNTIL_MISSING_LANES_EXIST_AND_VERIFY",
                "stage2": "NOT_STARTED",
                "stage3": "NOT_STARTED",
                "storage_evidence": {
                    "semantic_relationships": {
                        "typed_value_definitions": False,
                        "instruction_operand_value_ids": False,
                        "instruction_result_value_ids": False,
                        "call_argument_value_ids": False,
                        "call_result_value_ids": False,
                        "complete_terminator_values": False,
                        "canonical_serialized_ir": False,
                    }
                },
                "reference_typed_ir": {
                    "status": "MEASURED_HOST_IR_ORACLE_NOT_STAGE1_EVIDENCE"
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    subprocess.run(["git", "-C", str(repo), "add", str(path.relative_to(repo))], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-q", "-m", "evidence"], check=True)


def test_orchestrator_is_read_only_and_fail_closed(tmp_path) -> None:
    s3_repo = tmp_path / "S3"
    bench_repo = tmp_path / "S3-Benchmarks"
    _git_init(s3_repo)
    _write_semantic_evidence(s3_repo)
    s3_head = subprocess.check_output(["git", "-C", str(s3_repo), "rev-parse", "HEAD"], text=True).strip()
    bench_head = _git_init(bench_repo)
    before_status = subprocess.check_output(["git", "-C", str(s3_repo), "status", "--porcelain"], text=True)

    summary, exit_code = run_lab(
        s3_repo=s3_repo,
        benchmark_repo=bench_repo,
        output_dir=tmp_path / "out",
        expected_s3_commit=s3_head,
        expected_benchmark_commit=bench_head,
    )

    after_status = subprocess.check_output(["git", "-C", str(s3_repo), "status", "--porcelain"], text=True)
    assert before_status == after_status == ""
    assert exit_code == 0
    assert summary["status"] == "PASS"
    assert summary["bootstrap"]["stage1"] == "BLOCKED"
    assert summary["bootstrap"]["stage1_self_emit"] == "BLOCKED"
    assert summary["bootstrap"]["stage2"] == "NOT_STARTED"
    assert summary["components"]["differential"]["status"] == "NOT_RUN"
    assert summary["components"]["stage_equivalence"]["status"] == "NOT_AVAILABLE"
    assert summary["promotion"]["performed"] is False
    assert summary["promotion"]["compiler_mutated"] is False
    assert (tmp_path / "out" / "summary.json").is_file()
    assert (tmp_path / "out" / "corpus" / "manifest.json").is_file()
