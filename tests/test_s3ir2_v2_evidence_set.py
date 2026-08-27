from __future__ import annotations

import json
from pathlib import Path

from tools.ingest_s3ir2_v2_evidence_set import ingest_set


STREAM = """\
S3IR2 2
F 0 1 0 4 0 1
B 0 0 0 1 0
V 0 0 3 3 0 1 0 -1
I 0 0 0 0 23 0 1 -1 -1
O 0 0 0
T 0 1 -1 -1 -1 -1 0
Z 31
"""


def _files(tmp_path: Path) -> tuple[Path, Path, Path, Path]:
    source = tmp_path / "case.s3"
    stream = tmp_path / "case.s3ir2"
    conformance = tmp_path / "conformance.json"
    native = tmp_path / "native-provenance.json"
    source.write_text("fn main() -> i64:\n    return 1\n", encoding="utf-8")
    stream.write_text(STREAM, encoding="utf-8")
    conformance.write_text(json.dumps({"status": "PASS", "errors": []}) + "\n", encoding="utf-8")
    native.write_text(json.dumps({"status": "PASS", "errors": []}) + "\n", encoding="utf-8")
    return source, stream, conformance, native


def test_evidence_set_requires_repeat_determinism_for_gate(tmp_path: Path) -> None:
    source, stream, conformance, native = _files(tmp_path)
    output = tmp_path / "out"
    manifest = ingest_set(
        source=source,
        stream=stream,
        conformance=conformance,
        repeats=[],
        native_provenance=native,
        output=output,
    )
    assert manifest["structural_status"] == "PASS"
    assert manifest["semantic_conformance_status"] == "PASS"
    assert manifest["native_provenance_status"] == "PASS"
    assert manifest["determinism_status"] == "NOT_EVALUATED"
    assert manifest["qualification_gate"] == "BLOCKED"


def test_evidence_set_requires_native_provenance_for_gate(tmp_path: Path) -> None:
    source, stream, conformance, _native = _files(tmp_path)
    repeat = tmp_path / "repeat.s3ir2"
    repeat.write_text(STREAM, encoding="utf-8")
    manifest = ingest_set(
        source=source,
        stream=stream,
        conformance=conformance,
        repeats=[repeat],
        native_provenance=None,
        output=tmp_path / "out",
    )
    assert manifest["determinism_status"] == "PASS"
    assert manifest["native_provenance_status"] == "NOT_EVALUATED"
    assert manifest["qualification_gate"] == "BLOCKED"


def test_evidence_set_passes_lab_gate_with_all_proofs(tmp_path: Path) -> None:
    source, stream, conformance, native = _files(tmp_path)
    repeat2 = tmp_path / "repeat2.s3ir2"
    repeat3 = tmp_path / "repeat3.s3ir2"
    repeat2.write_text(STREAM, encoding="utf-8")
    repeat3.write_text(STREAM, encoding="utf-8")
    output = tmp_path / "out"
    manifest = ingest_set(
        source=source,
        stream=stream,
        conformance=conformance,
        repeats=[repeat2, repeat3],
        native_provenance=native,
        output=output,
    )
    assert manifest["structural_status"] == "PASS"
    assert manifest["semantic_conformance_status"] == "PASS"
    assert manifest["determinism_status"] == "PASS"
    assert manifest["native_provenance_status"] == "PASS"
    assert manifest["qualification_gate"] == "PASS"
    assert (output / "ingest.json").exists()
    assert (output / "determinism.json").exists()
    assert (output / "scorecard.json").exists()
    assert (output / "evidence-manifest.json").exists()
