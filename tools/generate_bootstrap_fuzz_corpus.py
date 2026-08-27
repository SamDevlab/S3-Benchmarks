"""Generate a deterministic Stage1 bootstrap stress corpus.

The generator deliberately does not invoke S3. It creates small source fixtures
that target semantic surfaces currently relevant to self-hosting and writes a
manifest with exact hashes for later reference/Stage1 differential campaigns.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "laboratory" / "bootstrap-v1" / "generated-corpus"


@dataclass(frozen=True)
class Case:
    case_id: str
    category: str
    source: str
    required_surfaces: tuple[str, ...]
    current_stage1_expectation: str


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def cases() -> tuple[Case, ...]:
    return (
        Case(
            "wide_literal_positive",
            "wide_literals",
            "fn main() -> i64:\n    return 1000000000000\n",
            ("typed_values", "instruction_def_use"),
            "VALID_SOURCE_GENERAL_EMITTER_MAY_BLOCK",
        ),
        Case(
            "wide_literal_negative",
            "wide_literals",
            "fn main() -> i64:\n    return -1000000000000\n",
            ("typed_values", "instruction_def_use"),
            "VALID_SOURCE_GENERAL_EMITTER_MAY_BLOCK",
        ),
        Case(
            "parameter_ordinal_0",
            "parameters",
            "fn choose(a: i64, b: i64, c: i64, d: i64, e: i64, f: i64) -> i64:\n"
            "    return a\n\n"
            "fn main() -> i64:\n"
            "    return choose(11, 22, 33, 44, 55, 66)\n",
            ("typed_values", "instruction_def_use", "call_dataflow"),
            "REGISTER_PARAMETER_SUBSET_CANDIDATE",
        ),
        Case(
            "parameter_ordinal_5",
            "parameters",
            "fn choose(a: i64, b: i64, c: i64, d: i64, e: i64, f: i64) -> i64:\n"
            "    return f\n\n"
            "fn main() -> i64:\n"
            "    return choose(11, 22, 33, 44, 55, 66)\n",
            ("typed_values", "instruction_def_use", "call_dataflow"),
            "REGISTER_PARAMETER_SUBSET_CANDIDATE",
        ),
        Case(
            "parameter_ordinal_6",
            "parameters",
            "fn choose(a: i64, b: i64, c: i64, d: i64, e: i64, f: i64, g: i64) -> i64:\n"
            "    return g\n\n"
            "fn main() -> i64:\n"
            "    return choose(11, 22, 33, 44, 55, 66, 77)\n",
            ("typed_values", "instruction_def_use", "call_dataflow"),
            "VALID_SOURCE_EXPECT_STAGE1_FAIL_CLOSED_UNTIL_STACK_ARGUMENT_LOWERING",
        ),
        Case(
            "nested_calls",
            "calls",
            "fn double(value: i64) -> i64:\n"
            "    return value + value\n\n"
            "fn main() -> i64:\n"
            "    result: i64 = double(double(3))\n"
            "    return result\n",
            ("typed_values", "instruction_def_use", "call_dataflow"),
            "VALID_SOURCE_GENERAL_EMITTER_MAY_BLOCK",
        ),
        Case(
            "local_identity",
            "locals",
            "fn main() -> i64:\n"
            "    value: i64 = 41\n"
            "    result: i64 = value + 1\n"
            "    return result\n",
            ("typed_values", "instruction_def_use"),
            "VALID_SOURCE_GENERAL_EMITTER_MAY_BLOCK",
        ),
        Case(
            "call_result_reuse",
            "calls",
            "fn add(a: i64, b: i64) -> i64:\n"
            "    return a + b\n\n"
            "fn main() -> i64:\n"
            "    first: i64 = add(10, 20)\n"
            "    second: i64 = add(first, 12)\n"
            "    return second\n",
            ("typed_values", "instruction_def_use", "call_dataflow"),
            "VALID_SOURCE_GENERAL_EMITTER_MAY_BLOCK",
        ),
    )


def generate(output: Path) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, object]] = []
    for case in cases():
        path = output / f"{case.case_id}.s3"
        path.write_text(case.source, encoding="utf-8", newline="\n")
        records.append(
            {
                "case_id": case.case_id,
                "category": case.category,
                "path": path.name,
                "sha256": _sha256(case.source),
                "bytes": len(case.source.encode("utf-8")),
                "required_surfaces": list(case.required_surfaces),
                "current_stage1_expectation": case.current_stage1_expectation,
            }
        )

    manifest: dict[str, object] = {
        "schema": "s3.bootstrap-fuzz-corpus.v1",
        "deterministic": True,
        "compiler_invoked": False,
        "case_count": len(records),
        "categories": sorted({record["category"] for record in records}),
        "cases": records,
        "evidence_rule": (
            "Sources are corpus inputs only. A generated case is not PASS/FAIL evidence until run "
            "against an exact pinned reference/compiler artifact under an explicit differential contract."
        ),
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    manifest = generate(args.output)
    print(f"OUTPUT={args.output.resolve()}")
    print(f"CASES={manifest['case_count']}")
    print("COMPILER_INVOKED=False")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
