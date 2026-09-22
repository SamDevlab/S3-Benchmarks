"""Benchmark-side static audit and diagnostic rewrite for S3 native assembly.

The rewrite is deliberately narrow: it removes only the exact four-line
instruction-budget accounting sequence emitted by the pinned S3 backend. It
does not change S3 source, compiler behavior, frame checks, bounds checks,
calls, ABI setup, or data layout.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Any


INSTRUCTION_LIMIT = 10_000_000_000
_SITE = r"\.L__s3_failure_site_[0-9]+"
_BUDGET_BLOCK = re.compile(
    rf"^    movabs r11, (?P<limit>[0-9]+)\n"
    rf"^    cmp qword ptr \[rip \+ __s3_instruction_count\], r11\n"
    rf"^    jae (?P<label>{_SITE})\n"
    rf"^    inc qword ptr \[rip \+ __s3_instruction_count\]\n",
    re.MULTILINE,
)


class DiagnosticRewriteError(ValueError):
    """Raised when the input assembly is not the expected exact layout."""


@dataclass(frozen=True)
class RewriteResult:
    input_sha256: str
    output_sha256: str
    expected_sites: int
    removed_sites: int
    unexpected_mutations: int

    def as_dict(self) -> dict[str, Any]:
        return {
            "input_assembly_sha": self.input_sha256,
            "output_assembly_sha": self.output_sha256,
            "expected_sites": self.expected_sites,
            "removed_sites": self.removed_sites,
            "unexpected_mutations": self.unexpected_mutations,
            "diagnostic_only": True,
            "production_artifact": False,
            "s3_source_changed": False,
        }


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _budget_matches(text: str) -> list[re.Match[str]]:
    return list(_BUDGET_BLOCK.finditer(text))


def _assert_exact_budget_layout(text: str) -> list[re.Match[str]]:
    matches = _budget_matches(text)
    if not matches:
        raise DiagnosticRewriteError("no complete instruction-budget sites found")

    for match in matches:
        if int(match.group("limit")) != INSTRUCTION_LIMIT:
            raise DiagnosticRewriteError("instruction-budget site has an unexpected limit")

    # Every hot-path reference must belong to a complete four-line site. This
    # rejects partial sites and future compiler layouts rather than guessing.
    marker_lines = [
        line
        for line in text.splitlines()
        if "__s3_instruction_count" in line
        and not line.lstrip().startswith("#")
        and not line.lstrip().startswith("__s3_instruction_count:")
    ]
    consumed_lines = 2 * len(matches)
    if len(marker_lines) != consumed_lines:
        raise DiagnosticRewriteError(
            "instruction-count references are not exclusively complete expected sites"
        )
    return matches


def remove_instruction_budget_instrumentation(text: str) -> tuple[str, RewriteResult]:
    """Remove only complete expected instruction-budget blocks.

    The output is formed by deleting matched blocks from the original text;
    therefore any non-deletion mutation is structurally impossible here and is
    still reported explicitly for the evidence contract.
    """

    matches = _assert_exact_budget_layout(text)
    chunks: list[str] = []
    cursor = 0
    for match in matches:
        chunks.append(text[cursor : match.start()])
        cursor = match.end()
    chunks.append(text[cursor:])
    output = "".join(chunks)
    result = RewriteResult(
        input_sha256=_sha256_text(text),
        output_sha256=_sha256_text(output),
        expected_sites=len(matches),
        removed_sites=len(matches),
        unexpected_mutations=0,
    )
    if result.removed_sites != result.expected_sites:
        raise DiagnosticRewriteError("removed site count does not match expected site count")
    return output, result


def _instruction_lines(lines: list[str]) -> list[str]:
    instructions: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", ".")) or stripped.endswith(":"):
            continue
        instructions.append(stripped)
    return instructions


def _mnemonic(instruction: str) -> str:
    return instruction.split(None, 1)[0].lower()


def audit_assembly(text: str, *, binary: Path | None = None) -> dict[str, Any]:
    """Return deterministic static counts with explicit approximation labels."""

    lines = text.splitlines()
    instructions = _instruction_lines(lines)
    budget_sites = _budget_matches(text)
    frame_sites = [
        line
        for line in lines
        if "cmp qword ptr [rip + __s3_frame_count]" in line
    ]
    global_reads = sum(
        "__s3_instruction_count" in line and ("cmp" in line or "mov" in line)
        for line in lines
    )
    global_writes = sum(
        "__s3_instruction_count" in line and ("inc" in line or "mov" in line)
        for line in lines
    )
    branches = {"jmp", "ja", "jae", "jb", "jbe", "jc", "je", "jg", "jge", "jl", "jle", "jne", "jnz", "jo", "js"}
    calls = sum(_mnemonic(item) == "call" for item in instructions)
    branch_count = sum(_mnemonic(item) in branches for item in instructions)
    memory_ops = sum("[" in item and "]" in item for item in instructions)
    stack_ops = sum(
        _mnemonic(item) in {"push", "pop"} or "rsp" in item or "[rbp" in item
        for item in instructions
    )
    static_budget_instructions = len(budget_sites) * 4
    frame_instructions = sum(
        "__s3_frame_count" in item for item in instructions
    )
    result: dict[str, Any] = {
        "total_assembly_lines": len(lines),
        "total_instructions": len(instructions),
        "s3_logical_instruction_sites": len(instructions) - static_budget_instructions - frame_instructions,
        "instruction_budget_check_sites": len(budget_sites),
        "frame_limit_check_sites": len(frame_sites),
        "global_counter_reads": global_reads,
        "global_counter_writes": global_writes,
        "call_count_static": calls,
        "branch_count_static": branch_count,
        "load_count_static_approx": memory_ops,
        "store_count_static_approx": sum(
            "[" in item and (item.startswith(("mov ", "inc ", "dec ", "stos")))
            for item in instructions
        ),
        "stack_ops_static_approx": stack_ops,
        "counts_are_static": True,
        "load_store_method": "memory-operand approximation; not dynamic counts",
        "text_size_bytes": None,
        "so_size_bytes": None,
        "binary_size_source": "unavailable_without_native_binary",
    }
    if binary is not None:
        result["so_size_bytes"] = binary.stat().st_size
        result["binary_size_source"] = str(binary)
    return result


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    rewrite = subparsers.add_parser("rewrite")
    rewrite.add_argument("--input", type=Path, required=True)
    rewrite.add_argument("--output", type=Path, required=True)
    rewrite.add_argument("--report", type=Path, required=True)

    audit = subparsers.add_parser("audit")
    audit.add_argument("--input", type=Path, required=True)
    audit.add_argument("--output", type=Path, required=True)
    audit.add_argument("--binary", type=Path)

    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8")
    if args.command == "rewrite":
        output, report = remove_instruction_budget_instrumentation(text)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8", newline="\n")
        _write_json(args.report, report.as_dict())
    else:
        _write_json(args.output, audit_assembly(text, binary=args.binary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
