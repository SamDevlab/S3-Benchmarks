"""Generate focused Stage04 numeric-cast fixtures without invoking S3.

Positive fixtures use parameter inputs so hosted/candidate comparison is not
obscured by constant folding. The negative fixture is a fail-closed input only;
it is not eligible for strict hosted semantic conformance when Stage0 rejects it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "laboratory" / "bootstrap-v1" / "stage04-cast-fixtures"


@dataclass(frozen=True)
class CastCase:
    case_id: str
    source: str
    expected: str
    target_type: str
    strict_conformance_eligible: bool


def cases() -> tuple[CastCase, ...]:
    return (
        CastCase(
            "cast_tryte_to_i64",
            "fn cast(value: tryte) -> i64:\n    return to_i64(value)\n",
            "VALID_CONVERT",
            "i64",
            True,
        ),
        CastCase(
            "cast_i64_to_f64",
            "fn cast(value: i64) -> f64:\n    return to_f64(value)\n",
            "VALID_CONVERT",
            "f64",
            True,
        ),
        CastCase(
            "cast_i64_to_tryte",
            "fn cast(value: i64) -> tryte:\n    return to_tryte(value)\n",
            "VALID_CONVERT_CHECKED_RANGE",
            "tryte",
            True,
        ),
        CastCase(
            "cast_invalid_f64_to_tryte",
            "fn cast(value: f64) -> tryte:\n    return to_tryte(value)\n",
            "FAIL_CLOSED_HOST_REJECT_EXPECTED",
            "tryte",
            False,
        ),
    )


def generate(output: Path) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    for case in cases():
        payload = case.source.encode("utf-8")
        path = output / f"{case.case_id}.s3"
        path.write_text(case.source, encoding="utf-8", newline="\n")
        rows.append(
            {
                "case_id": case.case_id,
                "path": path.name,
                "sha256": hashlib.sha256(payload).hexdigest(),
                "bytes": len(payload),
                "expected": case.expected,
                "target_type": case.target_type,
                "strict_conformance_eligible": case.strict_conformance_eligible,
            }
        )
    manifest: dict[str, object] = {
        "schema": "s3-benchmarks.bootstrap.stage04-cast-fixtures.v1",
        "compiler_invoked": False,
        "oracle_strategy": "PARAMETER_INPUTS_AVOID_CONSTANT_FOLD_NO_GENERAL_CALL_DATAFLOW",
        "s3ir2_convert_shape": {
            "opcode": 10,
            "result_count": 1,
            "operand_count": 1,
            "aux_a": -1,
            "aux_b": -1,
            "ordered_operand_edges": 1,
            "result_edges": 1,
        },
        "cases": rows,
        "evidence_rule": "Generated fixtures are inputs only until exact candidate execution and, for eligible cases, strict S3 conformance are preserved.",
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    manifest = generate(args.output)
    print(f"OUTPUT={args.output.resolve()}")
    print(f"CASES={len(manifest['cases'])}")
    print("COMPILER_INVOKED=False")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
