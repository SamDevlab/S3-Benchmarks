"""Ingest a complete S3IR2 v2 evidence set into the Bootstrap Laboratory."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from tools.check_s3ir2_v2_determinism import check as check_determinism
from tools.classify_s3ir2_v2_failure import classify
from tools.ingest_s3ir2_v2 import ingest
from tools.render_s3ir2_v2_scorecard import build_scorecard


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def _bind_native_report(
    report: dict[str, Any],
    *,
    fixture_sha256: str,
    stream_sha256: str,
) -> dict[str, Any]:
    errors: list[str] = []
    if report.get("status") != "PASS":
        errors.append("native provenance validator status is not PASS")

    actual = report.get("actual_files")
    if not isinstance(actual, dict):
        errors.append("native provenance report lacks actual_files")
        actual = {}

    def actual_sha(label: str) -> str | None:
        item = actual.get(label)
        if not isinstance(item, dict):
            errors.append(f"native provenance lacks actual_files.{label}")
            return None
        value = item.get("sha256")
        if not isinstance(value, str):
            errors.append(f"native provenance lacks {label} sha256")
            return None
        return value

    candidate_source_sha = actual_sha("candidate_source")
    candidate_binary_sha = actual_sha("candidate_binary")
    fixture_sha = actual_sha("fixture_source")
    observed_stream_sha = actual_sha("stream")
    if fixture_sha is not None and fixture_sha != fixture_sha256:
        errors.append("native provenance fixture SHA does not match evidence-set source")
    if observed_stream_sha is not None and observed_stream_sha != stream_sha256:
        errors.append("native provenance stream SHA does not match evidence-set stream")

    candidate_git_sha = report.get("candidate_git_sha")
    if not isinstance(candidate_git_sha, str) or not candidate_git_sha:
        errors.append("native provenance lacks candidate_git_sha")

    return {
        "status": "PASS" if not errors else "FAIL",
        "candidate_git_sha": candidate_git_sha,
        "candidate_source_sha256": candidate_source_sha,
        "candidate_binary_sha256": candidate_binary_sha,
        "fixture_source_sha256": fixture_sha,
        "stream_sha256": observed_stream_sha,
        "control_revision": report.get("control_revision"),
        "errors": errors,
    }


def ingest_set(
    *,
    source: Path,
    stream: Path,
    conformance: Path,
    repeats: list[Path],
    native_provenance: Path | None,
    repeat_native_provenance: list[Path] | None = None,
    output: Path,
) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    repeat_native_provenance = list(repeat_native_provenance or [])
    source_sha = _sha(source)
    stream_sha = _sha(stream)
    stream_text = stream.read_text(encoding="utf-8")
    structural = ingest(stream_text, source_sha256=source_sha)
    conformance_data = _load_json(conformance)

    ingest_path = output / "ingest.json"
    ingest_path.write_text(
        json.dumps(structural, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    determinism_data: dict[str, object] | None = None
    determinism_path: Path | None = None
    if repeats:
        determinism_data = check_determinism([stream, *repeats])
        determinism_path = output / "determinism.json"
        determinism_path.write_text(
            json.dumps(determinism_data, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    primary_binding: dict[str, Any]
    if native_provenance is None:
        primary_binding = {
            "status": "NOT_EVALUATED",
            "errors": ["primary native provenance not supplied"],
        }
    else:
        primary_binding = _bind_native_report(
            _load_json(native_provenance),
            fixture_sha256=source_sha,
            stream_sha256=stream_sha,
        )

    repeat_bindings: list[dict[str, Any]] = []
    repeat_set_errors: list[str] = []
    if len(repeat_native_provenance) != len(repeats):
        if repeats or repeat_native_provenance:
            repeat_set_errors.append(
                "repeat stream count does not match repeat native-provenance count"
            )
    for index, repeat in enumerate(repeats):
        if index >= len(repeat_native_provenance):
            repeat_bindings.append({
                "status": "NOT_EVALUATED",
                "repeat_index": index,
                "errors": ["repeat native provenance missing"],
            })
            continue
        binding = _bind_native_report(
            _load_json(repeat_native_provenance[index]),
            fixture_sha256=source_sha,
            stream_sha256=_sha(repeat),
        )
        binding["repeat_index"] = index
        if primary_binding.get("status") == "PASS" and binding.get("status") == "PASS":
            for field in (
                "candidate_git_sha",
                "candidate_source_sha256",
                "candidate_binary_sha256",
                "fixture_source_sha256",
            ):
                if binding.get(field) != primary_binding.get(field):
                    binding["status"] = "FAIL"
                    binding.setdefault("errors", []).append(
                        f"repeat provenance {field} differs from primary run"
                    )
        repeat_bindings.append(binding)

    native_status = "PASS"
    if primary_binding.get("status") != "PASS":
        native_status = "BLOCKED"
    if repeat_set_errors:
        native_status = "BLOCKED"
    if any(binding.get("status") != "PASS" for binding in repeat_bindings):
        native_status = "BLOCKED"

    native_binding = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-native-binding.v1",
        "status": native_status,
        "primary": primary_binding,
        "repeats": repeat_bindings,
        "repeat_set_errors": repeat_set_errors,
        "same_candidate_required": True,
        "promotion_effect": "NONE_PROVENANCE_GATE_ONLY",
    }
    native_binding_path = output / "native-binding.json"
    native_binding_path.write_text(
        json.dumps(native_binding, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    scorecard = build_scorecard(
        structural,
        conformance=conformance_data,
        determinism=determinism_data,
        native_provenance={"status": native_status},
    )
    scorecard_path = output / "scorecard.json"
    scorecard_path.write_text(
        json.dumps(scorecard, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    triage_path: Path | None = None
    if str(conformance_data.get("status", "UNKNOWN")) != "PASS":
        triage = classify(conformance_data)
        triage_path = output / "triage.json"
        triage_path.write_text(
            json.dumps(triage, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    files: dict[str, object] = {
        "source": {"path": str(source), "sha256": source_sha},
        "stream": {"path": str(stream), "sha256": stream_sha},
        "conformance": {"path": str(conformance), "sha256": _sha(conformance)},
        "ingest": {"path": str(ingest_path), "sha256": _sha(ingest_path)},
        "native_binding": {"path": str(native_binding_path), "sha256": _sha(native_binding_path)},
        "scorecard": {"path": str(scorecard_path), "sha256": _sha(scorecard_path)},
    }
    if native_provenance is not None:
        files["native_provenance"] = {
            "path": str(native_provenance),
            "sha256": _sha(native_provenance),
        }
    if repeat_native_provenance:
        files["repeat_native_provenance"] = [
            {"path": str(path), "sha256": _sha(path)}
            for path in repeat_native_provenance
        ]
    if determinism_path is not None:
        files["determinism"] = {
            "path": str(determinism_path),
            "sha256": _sha(determinism_path),
        }
    if triage_path is not None:
        files["triage"] = {"path": str(triage_path), "sha256": _sha(triage_path)}

    manifest: dict[str, object] = {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-evidence-set.v1",
        "protocol": "S3IR2 v2",
        "files": files,
        "repeat_stream_count": len(repeats),
        "repeat_native_provenance_count": len(repeat_native_provenance),
        "structural_status": structural["structural_status"],
        "semantic_conformance_status": conformance_data.get("status", "UNKNOWN"),
        "determinism_status": (
            determinism_data.get("status", "UNKNOWN")
            if determinism_data is not None
            else "NOT_EVALUATED"
        ),
        "native_provenance_status": native_status,
        "qualification_gate": scorecard["qualification_gate"],
        "promotion_effect": "NONE_LABORATORY_EVIDENCE_ONLY",
    }
    manifest_path = output / "evidence-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--stream", type=Path, required=True)
    parser.add_argument("--conformance", type=Path, required=True)
    parser.add_argument("--repeat-stream", action="append", type=Path, default=[])
    parser.add_argument("--native-provenance", type=Path)
    parser.add_argument("--repeat-native-provenance", action="append", type=Path, default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = ingest_set(
            source=args.source,
            stream=args.stream,
            conformance=args.conformance,
            repeats=args.repeat_stream,
            native_provenance=args.native_provenance,
            repeat_native_provenance=args.repeat_native_provenance,
            output=args.output,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_EVIDENCE_SET_ERROR={error}\n")
    print(f"QUALIFICATION_GATE={manifest['qualification_gate']}")
    print(f"SEMANTIC_CONFORMANCE={manifest['semantic_conformance_status']}")
    print(f"DETERMINISM={manifest['determinism_status']}")
    print(f"NATIVE_PROVENANCE={manifest['native_provenance_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
