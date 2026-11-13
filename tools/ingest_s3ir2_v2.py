"""Ingest a Stage1 S3IR2 v2 stream without importing the S3 compiler package.

This is a benchmark/laboratory consumer only. It validates the frozen record
shape and structural references, reports the five-lane completeness mask, and
keeps semantic-conformance authority in SamDevlab/S3's v2 verifier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

HEADER = "S3IR2 2"
COMPLETE_MASK = 31
EXPECTED_FIELDS = {
    "F": 6,
    "B": 5,
    "V": 8,
    "M": 5,
    "I": 9,
    "O": 3,
    "R": 3,
    "C": 7,
    "A": 3,
    "T": 7,
    "Z": 1,
}
LANE_BITS = {
    "S1_typed_values_and_bindings": 1,
    "S2_instruction_def_use": 2,
    "S3_call_dataflow": 4,
    "S4_complete_terminators": 8,
    "S5_canonical_serialization": 16,
}


class S3IR2IngestError(ValueError):
    pass


def parse_stream(text: str) -> dict[str, Any]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines or lines[0] != HEADER:
        raise S3IR2IngestError("missing or invalid S3IR2 v2 header")

    records: list[dict[str, Any]] = []
    mask: int | None = None
    for line_number, line in enumerate(lines[1:], start=2):
        parts = line.split()
        tag = parts[0]
        if tag not in EXPECTED_FIELDS:
            raise S3IR2IngestError(f"line {line_number}: unknown tag {tag!r}")
        try:
            fields = [int(item) for item in parts[1:]]
        except ValueError as error:
            raise S3IR2IngestError(f"line {line_number}: non-integer field") from error
        if len(fields) != EXPECTED_FIELDS[tag]:
            raise S3IR2IngestError(
                f"line {line_number}: {tag} expects {EXPECTED_FIELDS[tag]} fields, got {len(fields)}"
            )
        if tag == "Z":
            if mask is not None:
                raise S3IR2IngestError("multiple Z completeness records")
            mask = fields[0]
        records.append({"tag": tag, "fields": fields, "line": line_number})
    if mask is None:
        raise S3IR2IngestError("missing Z completeness record")
    if mask < 0 or mask > COMPLETE_MASK:
        raise S3IR2IngestError(f"invalid completeness mask {mask}")
    return {"records": records, "mask": mask}


def validate_structure(parsed: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    functions: set[int] = set()
    blocks: set[tuple[int, int]] = set()
    values: set[int] = set()
    instructions: dict[int, tuple[int, int, int, int]] = {}
    operands: dict[int, list[tuple[int, int]]] = {}
    results: dict[int, list[tuple[int, int]]] = {}
    calls: dict[int, tuple[int, int]] = {}
    call_args: dict[int, list[tuple[int, int]]] = {}
    terminators: set[int] = set()

    for record in parsed["records"]:
        tag = record["tag"]
        f = record["fields"]
        if tag == "F":
            if f[0] in functions:
                errors.append(f"duplicate function id {f[0]}")
            functions.add(f[0])
        elif tag == "B":
            key = (f[0], f[1])
            if key in blocks:
                errors.append(f"duplicate block {f[0]}:{f[1]}")
            blocks.add(key)
            if f[0] not in functions:
                errors.append(f"block {f[0]}:{f[1]} references unknown function")
        elif tag == "V":
            if f[0] in values:
                errors.append(f"duplicate value id {f[0]}")
            values.add(f[0])
            if f[1] not in functions:
                errors.append(f"value {f[0]} references unknown function {f[1]}")
        elif tag == "M":
            if f[0] not in functions:
                errors.append(f"memory {f[1]} references unknown function {f[0]}")
        elif tag == "I":
            iid = f[0]
            if iid in instructions:
                errors.append(f"duplicate instruction id {iid}")
            instructions[iid] = (f[1], f[2], f[5], f[6])
            if (f[1], f[2]) not in blocks:
                errors.append(f"instruction {iid} references unknown block {f[1]}:{f[2]}")
        elif tag == "O":
            operands.setdefault(f[0], []).append((f[1], f[2]))
        elif tag == "R":
            results.setdefault(f[0], []).append((f[1], f[2]))
        elif tag == "C":
            calls[f[0]] = (f[5], f[6])
        elif tag == "A":
            call_args.setdefault(f[0], []).append((f[1], f[2]))
        elif tag == "T":
            if f[0] in terminators:
                errors.append(f"duplicate terminator instruction {f[0]}")
            terminators.add(f[0])

    for iid, (_owner, _block, expected_results, expected_operands) in instructions.items():
        got_o = operands.get(iid, [])
        got_r = results.get(iid, [])
        if len(got_o) != expected_operands:
            errors.append(f"instruction {iid} operand count mismatch")
        if len(got_r) != expected_results:
            errors.append(f"instruction {iid} result count mismatch")
        for _ordinal, value_id in got_o + got_r:
            if value_id not in values:
                errors.append(f"instruction {iid} references unknown value {value_id}")

    for iid, (expected_args, _expected_results) in calls.items():
        if iid not in instructions:
            errors.append(f"call references unknown instruction {iid}")
        got = call_args.get(iid, [])
        if len(got) != expected_args:
            errors.append(f"call {iid} argument count mismatch")
        for _ordinal, value_id in got:
            if value_id not in values:
                errors.append(f"call {iid} references unknown value {value_id}")

    return errors


def ingest(text: str, *, source_sha256: str | None = None) -> dict[str, Any]:
    parsed = parse_stream(text)
    errors = validate_structure(parsed)
    counts = {tag: 0 for tag in EXPECTED_FIELDS}
    for record in parsed["records"]:
        counts[record["tag"]] += 1
    mask = int(parsed["mask"])
    lanes = {
        name: ("PASS_DECLARED" if mask & bit else "BLOCKED")
        for name, bit in LANE_BITS.items()
    }
    complete = mask == COMPLETE_MASK
    return {
        "schema": "s3-benchmarks.bootstrap.s3ir2-v2-ingest.v1",
        "protocol": "S3IR2 v2",
        "stream_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "source_sha256": source_sha256,
        "completeness_mask": mask,
        "declared_complete": complete,
        "structural_status": "PASS" if not errors else "FAIL",
        "semantic_conformance_status": "NOT_EVALUATED_USE_S3_CONFORMANCE_GATE",
        "promotion_effect": "NONE_CONSUMER_ONLY",
        "lanes": lanes,
        "record_counts": counts,
        "errors": errors,
        "bootstrap_gate": "CANDIDATE_STREAM_READY_FOR_STRICT_CONFORMANCE" if complete and not errors else "BLOCKED",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stream", type=Path)
    parser.add_argument("--source-sha256")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report = ingest(
            args.stream.read_text(encoding="utf-8"),
            source_sha256=args.source_sha256,
        )
    except (OSError, S3IR2IngestError) as error:
        parser.exit(2, f"S3IR2_INGEST_ERROR={error}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STATUS={report['structural_status']}")
    print(f"MASK={report['completeness_mask']}")
    print(f"BOOTSTRAP_GATE={report['bootstrap_gate']}")
    return 0 if report["structural_status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
