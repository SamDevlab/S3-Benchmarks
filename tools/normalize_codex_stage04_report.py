"""Normalize Codex Stage04 KEY=VALUE checkpoint text into gate JSON.

This parser is intentionally conservative. Unknown keys are preserved as
unmapped metadata, missing required keys remain missing/non-PASS, and no prose is
interpreted as evidence. It never infers PASS from surrounding text.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

KEY_RE = re.compile(r"^[A-Z0-9_]+$")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")

GATE_MAP = {
    "STAGE03_EVIDENCE_BACKFILL": "stage03_evidence_backfill",
    "EXPR_PARSER_SYNTAX": "expr_parser_syntax",
    "INTEGER_LITERAL_LOWERING": "integer_literal_lowering",
    "NEGATIVE_WIDE_LITERAL_LOWERING": "negative_wide_literal_lowering",
    "IDENTIFIER_LOOKUP": "identifier_lookup",
    "LEXICAL_SHADOWING": "lexical_shadowing",
    "UNARY_NEGATE": "unary_negate",
    "UNARY_INVERT": "unary_invert",
    "SUPPORTED_BINARY_OPERATORS": "supported_binary_operators",
    "BINARY_PRECEDENCE": "binary_precedence",
    "COMPARISON_LOWERING": "comparison_lowering",
    "LOCAL_INITIALIZATION": "local_initialization",
    "ASSIGNMENT_REASSIGNMENT": "assignment_reassignment",
    "INSTRUCTION_RESULT_IDS": "instruction_result_ids",
    "ORDERED_OPERAND_EDGES": "ordered_operand_edges",
    "SINGLE_RESULT_DEFINITION": "single_result_definition",
    "UNSUPPORTED_MULTIPLY_DIVIDE_REMAINDER": "unsupported_multiply_divide_remainder",
    "CANDIDATE_STAGE0_CHECK": "candidate_stage0_check",
    "FOCUSED_NATIVE_V2_CONFORMANCE": "focused_native_v2_conformance",
    "S1_TYPED_VALUES": "s1_typed_values",
    "S2_DEF_USE": "s2_def_use",
}

IDENTITY_ALIASES = {
    "CANDIDATE_GIT_SHA": "candidate_git_sha",
    "CANDIDATE_SHA": "candidate_git_sha",
    "HEAD_AFTER": "candidate_git_sha",
    "CANDIDATE_SOURCE_SHA256": "candidate_source_sha256",
    "CANDIDATE_BINARY_SHA256": "candidate_binary_sha256",
}


def parse_key_values(text: str) -> tuple[dict[str, str], list[str]]:
    values: dict[str, str] = {}
    duplicates: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if KEY_RE.fullmatch(key) is None:
            continue
        if key in values:
            duplicates.append(key)
        values[key] = value
    return values, duplicates


def _normalize_status(value: str) -> str:
    raw = value.strip().upper()
    aliases = {
        "YES": "PASS",
        "NO": "BLOCKED",
        "NOT RUN": "NOT_RUN",
        "NOT-RUN": "NOT_RUN",
        "NOT RECORDED": "NOT_RECORDED",
        "NOT REOBSERVED": "NOT_REOBSERVED",
        "FAIL-CLOSED": "FAIL_CLOSED",
        "N/A": "NOT_APPLICABLE",
        "NA": "NOT_APPLICABLE",
    }
    return aliases.get(raw, raw)


def normalize(text: str) -> dict[str, Any]:
    values, duplicates = parse_key_values(text)
    errors: list[str] = []
    gates: dict[str, str] = {}

    revision_raw = values.get("CONTROL_REVISION")
    revision: int | None = None
    if revision_raw is not None:
        try:
            revision = int(revision_raw)
        except ValueError:
            errors.append("CONTROL_REVISION is not an integer")

    for source_key, gate_key in GATE_MAP.items():
        if source_key in values:
            gates[gate_key] = _normalize_status(values[source_key])

    identity: dict[str, str | None] = {
        "candidate_git_sha": None,
        "candidate_source_sha256": None,
        "candidate_binary_sha256": None,
    }
    for source_key, target_key in IDENTITY_ALIASES.items():
        raw = values.get(source_key)
        if raw is None:
            continue
        current = identity.get(target_key)
        if current is not None and current != raw:
            errors.append(f"conflicting values for {target_key}")
        identity[target_key] = raw

    git_sha = identity["candidate_git_sha"]
    if git_sha is not None and HEX40.fullmatch(git_sha) is None:
        errors.append("candidate_git_sha is not 40 lowercase hex characters")
    source_sha = identity["candidate_source_sha256"]
    if source_sha is not None and HEX64.fullmatch(source_sha) is None:
        errors.append("candidate_source_sha256 is not 64 lowercase hex characters")
    binary_sha = identity["candidate_binary_sha256"]
    if binary_sha is not None and HEX64.fullmatch(binary_sha) is None:
        errors.append("candidate_binary_sha256 is not 64 lowercase hex characters")

    z_mask: int | None = None
    raw_z = values.get("Z_MASK")
    if raw_z is not None:
        if raw_z.startswith("<"):
            errors.append("Z_MASK must be the observed integer value, not a bound")
        else:
            try:
                z_mask = int(raw_z)
            except ValueError:
                errors.append("Z_MASK is not an integer")

    canonical_mutated = values.get("CANONICAL_SOURCE_MUTATED")
    if canonical_mutated is None:
        canonical_mutated_bool: bool | None = None
    elif canonical_mutated.upper() in {"NO", "FALSE"}:
        canonical_mutated_bool = False
    elif canonical_mutated.upper() in {"YES", "TRUE"}:
        canonical_mutated_bool = True
    else:
        canonical_mutated_bool = None
        errors.append("CANONICAL_SOURCE_MUTATED is not YES/NO")

    unmapped = {
        key: value
        for key, value in values.items()
        if key not in GATE_MAP
        and key not in IDENTITY_ALIASES
        and key not in {
            "CONTROL_REVISION",
            "Z_MASK",
            "CANONICAL_SOURCE_MUTATED",
            "FIRST_REAL_BLOCKER",
            "NEXT_STAGE",
        }
    }

    return {
        "schema": "s3.stage1.codex-stage-checkpoint.v2",
        "stage_id": "04_EXPRESSIONS_S1_S2",
        "control_revision": revision,
        **identity,
        "gates": gates,
        "invariants": {
            "canonical_source_mutated": canonical_mutated_bool,
            "self_emit_authorized": False,
            "stage2_authorized": False,
            "z_mask": z_mask,
        },
        "first_real_blocker": values.get("FIRST_REAL_BLOCKER") or None,
        "reported_next_stage": values.get("NEXT_STAGE") or None,
        "duplicate_keys": sorted(set(duplicates)),
        "unmapped_key_values": unmapped,
        "normalization_errors": errors,
        "normalization_status": "PASS" if not errors and not duplicates else "BLOCKED",
        "evidence_policy": "KEY_VALUE_ONLY_NO_PROSE_INFERENCE",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = normalize(args.report.read_text(encoding="utf-8"))
    except OSError as error:
        parser.exit(2, f"STAGE04_NORMALIZE_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"NORMALIZATION={report['normalization_status']}")
    print(f"CONTROL_REVISION={report['control_revision']}")
    print(f"GATES_OBSERVED={len(report['gates'])}")
    return 0 if report["normalization_status"] == "PASS" else 3


if __name__ == "__main__":
    raise SystemExit(main())
