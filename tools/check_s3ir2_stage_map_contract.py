"""Validate that the S3IR2 v2 stage map stays aligned with the deterministic corpus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tools.generate_bootstrap_fuzz_corpus import cases


FORBIDDEN_STAGE04_ARITHMETIC = (" * ", " / ", " % ")


def check(stage_map: dict) -> dict[str, object]:
    corpus = list(cases())
    ids = [case.case_id for case in corpus]
    errors: list[str] = []
    if len(ids) != len(set(ids)):
        errors.append("duplicate case_id in deterministic corpus")
    by_id = {case.case_id: case for case in corpus}

    stages = stage_map.get("stages")
    if not isinstance(stages, dict):
        return {"status": "FAIL", "errors": ["stage map lacks stages object"]}

    for stage_id, stage in stages.items():
        if not isinstance(stage, dict):
            errors.append(f"{stage_id}: stage must be object")
            continue
        required = stage.get("required_cases", [])
        if not isinstance(required, list):
            errors.append(f"{stage_id}: required_cases must be list")
            continue
        if len(required) != len(set(required)):
            errors.append(f"{stage_id}: duplicate required case")
        for case_id in required:
            if case_id not in by_id:
                errors.append(f"{stage_id}: unknown corpus case {case_id}")

    stage04 = stages.get("04_EXPRESSIONS_S1_S2", {})
    if isinstance(stage04, dict):
        for case_id in stage04.get("required_cases", []):
            case = by_id.get(case_id)
            if case is None:
                continue
            for token in FORBIDDEN_STAGE04_ARITHMETIC:
                if token in case.source:
                    errors.append(
                        f"04_EXPRESSIONS_S1_S2:{case_id}: forbidden arithmetic token {token.strip()}"
                    )

    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-stage-map-contract.v1",
        "status": "PASS" if not errors else "FAIL",
        "corpus_case_count": len(corpus),
        "mapped_stage_count": len(stages),
        "errors": errors,
        "promotion_effect": "NONE_STATIC_CONTRACT_ONLY",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage-map", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        stage_map = json.loads(args.stage_map.read_text(encoding="utf-8"))
        report = check(stage_map)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3IR2_STAGE_MAP_ERROR={error}\n")
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"STATUS={report['status']}")
    print(f"CORPUS_CASES={report['corpus_case_count']}")
    return 0 if report["status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
