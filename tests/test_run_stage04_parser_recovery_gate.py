from __future__ import annotations

from pathlib import Path

from tools.run_stage04_parser_recovery_gate import run


def _write(path: Path, *, attempt: str, sha: str, status: str, fp: str | None = None) -> None:
    lines = [
        f"PARSER_ATTEMPT_ID={attempt}",
        f"CANDIDATE_SOURCE_SHA256={sha}",
        f"PARSER_STATUS={status}",
    ]
    if fp is not None:
        lines.append(f"DIAGNOSTIC_FINGERPRINT={fp}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_bridge_reports_recovery_progress(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.txt"
    _write(first, attempt="a1", sha="a" * 64, status="BLOCKED_SYNTAX", fp="indent:10")
    _write(second, attempt="a2", sha="b" * 64, status="BLOCKED_STRUCTURAL", fp="duplicate:20")
    report = run([first, second], tmp_path / "out")
    assert report["status"] == "RECOVERY_PROGRESS"
    assert report["recovery"]["s1_projection"] == "NOT_EVALUATED_BY_PARSER_RECOVERY"


def test_bridge_blocks_bad_normalization(tmp_path: Path) -> None:
    bad = tmp_path / "bad.txt"
    bad.write_text("PARSER_ATTEMPT_ID=a1\nCANDIDATE_SOURCE_SHA256=bad\nPARSER_STATUS=PASS\n", encoding="utf-8")
    report = run([bad], tmp_path / "out")
    assert report["status"] == "BLOCKED_NORMALIZATION"
    assert report["recovery"] is None


def test_bridge_parser_pass_closes_only_parser_recovery(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.txt"
    _write(first, attempt="a1", sha="a" * 64, status="BLOCKED_SYNTAX", fp="indent:10")
    _write(second, attempt="a2", sha="b" * 64, status="PASS")
    report = run([first, second], tmp_path / "out")
    assert report["status"] == "PARSER_RECOVERED"
    recovery = report["recovery"]
    assert recovery["expr_parser_syntax_projection"] == "PASS"
    assert recovery["s1_projection"] == "NOT_EVALUATED_BY_PARSER_RECOVERY"
    assert recovery["s2_projection"] == "NOT_EVALUATED_BY_PARSER_RECOVERY"
