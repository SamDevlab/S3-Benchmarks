from __future__ import annotations

import shlex
import sys

from tools.check_bootstrap_determinism import check
from tools.measure_bootstrap_resource_envelope import measure


def _python_command(code: str) -> str:
    return f"{shlex.quote(sys.executable)} -c {shlex.quote(code)}"


def test_resource_measurement_is_characterization_only(tmp_path) -> None:
    report = measure(_python_command("print('ok')"), [], 10.0)
    assert report["returncode"] == 0
    assert report["classification"] == "CHARACTERIZATION_ONLY"
    assert report["performance_claim"] is False
    assert report["wall_seconds"] >= 0


def test_resource_measurement_records_artifact_size(tmp_path) -> None:
    artifact = tmp_path / "artifact.bin"
    code = f"from pathlib import Path; Path({str(artifact)!r}).write_bytes(b'abc')"
    report = measure(_python_command(code), [artifact], 10.0)
    assert report["artifacts"] == [
        {"path": str(artifact), "exists": True, "bytes": 3}
    ]


def test_stdout_determinism_passes_for_stable_command(tmp_path) -> None:
    source = tmp_path / "case.s3"
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    report = check(source, _python_command("print('stable')"), 3, 10.0)
    assert report["classification"] == "PASS"
    assert report["deterministic"] is True
    assert len(report["unique_digests"]) == 1
    assert report["semantic_correctness_claim"] is False


def test_artifact_determinism_uses_output_placeholder(tmp_path) -> None:
    source = tmp_path / "case.s3"
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    command = _python_command(
        "from pathlib import Path; Path(r'{output}').write_bytes(b'stable-artifact')"
    )
    report = check(source, command, 2, 10.0)
    assert report["artifact_mode"] is True
    assert report["classification"] == "PASS"
    assert len(report["unique_digests"]) == 1
