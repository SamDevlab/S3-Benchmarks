"""Render a Bootstrap Laboratory scorecard without collapsing evidence to one score.

The scorecard keeps bootstrap state, behavioral coverage, provenance confidence,
reproducibility and performance eligibility separate. It is presentation only and
cannot promote Stage1, Stage2, Stage3, self-hosting or performance.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _load_optional(path: Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"expected JSON object: {path}")
    return payload


def build_scorecard(
    snapshot: dict[str, Any],
    *,
    differential: dict[str, Any] | None = None,
    coverage: dict[str, Any] | None = None,
    resources: dict[str, Any] | None = None,
    determinism: dict[str, Any] | None = None,
    stage_equivalence: dict[str, Any] | None = None,
    host: dict[str, Any] | None = None,
) -> dict[str, Any]:
    provenance = snapshot.get("provenance", {})
    notes = snapshot.get("evidence_notes", {})
    supplemental = notes.get("supplemental_evidence", [])
    supplemental = supplemental if isinstance(supplemental, list) else []
    stale = [
        row
        for row in supplemental
        if isinstance(row, dict)
        and row.get("source_applicability") == "HISTORICAL_SOURCE_MISMATCH"
    ]
    unknown = [
        row
        for row in supplemental
        if isinstance(row, dict) and row.get("source_applicability") == "UNKNOWN"
    ]

    behavioral: dict[str, Any]
    if coverage is not None:
        behavioral = {
            "status": "MEASURED",
            "case_count": coverage.get("case_count"),
            "case_parity_pass": coverage.get("case_parity_pass"),
            "case_parity_ratio": coverage.get("case_parity_ratio"),
            "stage1_blocked_cases": coverage.get("stage1_blocked_cases"),
            "semantic_mismatches": coverage.get("semantic_mismatches"),
        }
    elif differential is not None:
        behavioral = {
            "status": "MEASURED_NO_COVERAGE_SUMMARY",
            "case_count": differential.get("case_count"),
            "counts": differential.get("counts", {}),
        }
    else:
        behavioral = {"status": "NOT_RUN"}

    determinism_dimension = (
        {
            "status": determinism.get("classification"),
            "deterministic": determinism.get("deterministic"),
            "semantic_correctness_claim": False,
        }
        if determinism is not None
        else {"status": "NOT_RUN"}
    )

    equivalence_dimension = (
        {
            "status": stage_equivalence.get(
                "stage1_stage2_stage3_observable_equivalence", "NOT_AVAILABLE"
            ),
            "stage2_stage3_byte_identity": stage_equivalence.get(
                "stage2_stage3_byte_identity"
            ),
        }
        if stage_equivalence is not None
        else {"status": "NOT_AVAILABLE"}
    )

    resource_dimension = (
        {
            "status": resources.get("classification"),
            "wall_seconds": resources.get("wall_seconds"),
            "peak_rss_bytes": resources.get("peak_rss_bytes"),
            "performance_claim": False,
        }
        if resources is not None
        else {"status": "NOT_RUN", "performance_claim": False}
    )

    host_dimension = (
        {
            "status": host.get("classification") or host.get("status"),
            "performance_eligible": host.get("performance_eligible"),
        }
        if host is not None
        else {"status": "NOT_MEASURED", "performance_eligible": False}
    )

    return {
        "schema": "s3.bootstrap-scorecard.v1",
        "single_numeric_score": None,
        "dimensions": {
            "bootstrap": snapshot.get("bootstrap", {}),
            "semantic_ir": snapshot.get("semantic_ir", {}),
            "behavioral_coverage": behavioral,
            "provenance_confidence": {
                "source_lock_valid": provenance.get("source_lock_valid", False),
                "benchmark_lock_valid": provenance.get("benchmark_lock_valid", False),
                "historical_source_mismatch_count": len(stale),
                "unknown_source_applicability_count": len(unknown),
                "host_oracle_used_as_stage1_evidence": notes.get(
                    "host_oracle_used_as_stage1_evidence", False
                ),
            },
            "reproducibility": determinism_dimension,
            "stage_equivalence": equivalence_dimension,
            "resource_characterization": resource_dimension,
            "host_eligibility": host_dimension,
            "performance_eligibility": snapshot.get("performance_eligibility", {}),
        },
        "promotion": {
            "performed": False,
            "self_hosting_claim": False,
            "performance_claim": False,
        },
        "interpretation": (
            "Dimensions are intentionally separate. Behavioral coverage, deterministic bytes, "
            "resource measurements, or historical evidence cannot substitute for authoritative "
            "semantic IR closure and bootstrap equivalence."
        ),
    }


def render_markdown(scorecard: dict[str, Any]) -> str:
    d = scorecard["dimensions"]
    bootstrap = d["bootstrap"]
    semantic = d["semantic_ir"]
    provenance = d["provenance_confidence"]
    behavioral = d["behavioral_coverage"]
    lines = [
        "# S3 Bootstrap Scorecard",
        "",
        "> No aggregate numeric score. Dimensions are intentionally independent.",
        "",
        "## Bootstrap",
        "",
        f"- Stage1: `{bootstrap.get('stage1')}`",
        f"- Self emit: `{bootstrap.get('stage1_self_emit')}`",
        f"- Stage2: `{bootstrap.get('stage2')}`",
        f"- Stage3: `{bootstrap.get('stage3')}`",
        f"- Full self hosting: `{bootstrap.get('full_self_hosting')}`",
        "",
        "## Semantic IR",
        "",
    ]
    for name, state in semantic.items():
        lines.append(f"- {name}: `{state}`")
    lines.extend(
        [
            "",
            "## Behavioral coverage",
            "",
            f"- Status: `{behavioral.get('status')}`",
        ]
    )
    if "case_count" in behavioral:
        lines.append(f"- Cases: `{behavioral.get('case_count')}`")
    if "case_parity_pass" in behavioral:
        lines.append(f"- Parity PASS: `{behavioral.get('case_parity_pass')}`")
    if "semantic_mismatches" in behavioral:
        lines.append(f"- Semantic mismatches: `{behavioral.get('semantic_mismatches')}`")
    lines.extend(
        [
            "",
            "## Provenance confidence",
            "",
            f"- Source lock: `{provenance.get('source_lock_valid')}`",
            f"- Benchmark lock: `{provenance.get('benchmark_lock_valid')}`",
            f"- Historical source mismatches: `{provenance.get('historical_source_mismatch_count')}`",
            f"- Unknown supplemental applicability: `{provenance.get('unknown_source_applicability_count')}`",
            "",
            "## Reproducibility / equivalence / performance",
            "",
            f"- Determinism: `{d['reproducibility'].get('status')}`",
            f"- Stage equivalence: `{d['stage_equivalence'].get('status')}`",
            f"- Resource characterization: `{d['resource_characterization'].get('status')}`",
            f"- Host eligibility: `{d['host_eligibility'].get('status')}`",
            f"- Performance valid: `{d['performance_eligibility'].get('performance_valid')}`",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--differential", type=Path)
    parser.add_argument("--coverage", type=Path)
    parser.add_argument("--resources", type=Path)
    parser.add_argument("--determinism", type=Path)
    parser.add_argument("--stage-equivalence", type=Path)
    parser.add_argument("--host", type=Path)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-markdown", type=Path)
    args = parser.parse_args(argv)

    snapshot = _load_optional(args.snapshot)
    assert snapshot is not None
    scorecard = build_scorecard(
        snapshot,
        differential=_load_optional(args.differential),
        coverage=_load_optional(args.coverage),
        resources=_load_optional(args.resources),
        determinism=_load_optional(args.determinism),
        stage_equivalence=_load_optional(args.stage_equivalence),
        host=_load_optional(args.host),
    )
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(scorecard, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    if args.output_markdown is not None:
        args.output_markdown.parent.mkdir(parents=True, exist_ok=True)
        args.output_markdown.write_text(
            render_markdown(scorecard), encoding="utf-8", newline="\n"
        )
    print(f"OUTPUT_JSON={args.output_json}")
    if args.output_markdown is not None:
        print(f"OUTPUT_MARKDOWN={args.output_markdown}")
    print("SINGLE_NUMERIC_SCORE=None")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
