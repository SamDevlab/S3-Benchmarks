"""Fail-closed benchmark-side prototype for exact global budget countdowns.

The pinned S3 compiler remains untouched.  This module rewrites only the
known x86-64 assembly shape emitted by that compiler and records enough
provenance to make an artifact diagnostic rather than production output.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re
from typing import Any


UINT64_MAX = (1 << 64) - 1
COUNT_SYMBOL = "__s3_instruction_count"
REMAINING_SYMBOL = "__s3_instruction_remaining"
_FAILURE_LABEL = r"\.L__s3_failure_site_[0-9]+"
_COUNTDOWN_SITE_WIDE = re.compile(
    rf"^    movabs r11, (?P<limit>[0-9]+)\n"
    rf"^    cmp qword ptr \[rip \+ {COUNT_SYMBOL}\], r11\n"
    rf"^    jae (?P<label>{_FAILURE_LABEL})\n"
    rf"^    inc qword ptr \[rip \+ {COUNT_SYMBOL}\]\n",
    re.MULTILINE,
)
_COUNTDOWN_SITE_IMMEDIATE = re.compile(
    rf"^    cmp qword ptr \[rip \+ {COUNT_SYMBOL}\], (?P<limit>[0-9]+)\n"
    rf"^    jae (?P<label>{_FAILURE_LABEL})\n"
    rf"^    inc qword ptr \[rip \+ {COUNT_SYMBOL}\]\n",
    re.MULTILINE,
)
_COUNT_STORAGE = re.compile(
    rf"(?m)^\s*{re.escape(COUNT_SYMBOL)}:\n"
    rf"^    \.zero 8\n"
)


class SafeBudgetRewriteError(ValueError):
    """Raised when the candidate cannot prove an exact transformation."""


@dataclass(frozen=True, slots=True)
class CountdownRewrite:
    input_sha256: str
    output_sha256: str
    configured_limit: int
    expected_sites: int
    transformed_sites: int
    unexpected_mutations: int
    storage_replaced: bool
    diagnostic_only: bool = True
    s3_source_changed: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {
            "input_sha256": self.input_sha256,
            "output_sha256": self.output_sha256,
            "configured_limit": self.configured_limit,
            "expected_sites": self.expected_sites,
            "transformed_sites": self.transformed_sites,
            "unexpected_mutations": self.unexpected_mutations,
            "storage_replaced": self.storage_replaced,
            "diagnostic_only": self.diagnostic_only,
            "production_artifact": False,
            "s3_source_changed": self.s3_source_changed,
        }


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _validate_limit(value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise SafeBudgetRewriteError("budget limit must be an integer")
    if value < 0 or value > UINT64_MAX:
        raise SafeBudgetRewriteError("budget limit is outside uint64")
    return value


def transform_global_countdown(text: str, *, expected_limit: int | None = None) -> tuple[str, CountdownRewrite]:
    """Rewrite all and only the pinned S3 instruction-budget sites.

    The existing `movabs/cmp/jae/inc` sequence is replaced with a single
    unsigned countdown (`sub/jb`).  A `.data` quad initializes the remaining
    budget once when the shared object is loaded, matching the current global
    process-persistent counter lifetime for a loaded artifact.
    """

    matches = [*(_COUNTDOWN_SITE_WIDE.finditer(text)), *(_COUNTDOWN_SITE_IMMEDIATE.finditer(text))]
    matches.sort(key=lambda match: match.start())
    if not matches:
        raise SafeBudgetRewriteError("no complete instruction-budget sites found")
    limits = {int(match.group("limit")) for match in matches}
    if len(limits) != 1:
        raise SafeBudgetRewriteError("instruction-budget sites disagree on limit")
    limit = _validate_limit(limits.pop())
    if expected_limit is not None and limit != _validate_limit(expected_limit):
        raise SafeBudgetRewriteError("instruction-budget limit does not match expectation")

    marker_lines = [
        line for line in text.splitlines()
        if COUNT_SYMBOL in line and not line.lstrip().startswith("#")
    ]
    expected_marker_lines = 2 * len(matches) + 1
    storage_matches = list(_COUNT_STORAGE.finditer(text))
    if len(marker_lines) != expected_marker_lines or len(storage_matches) != 1:
        raise SafeBudgetRewriteError("count references are not exclusively complete known sites")

    chunks: list[str] = []
    cursor = 0
    for match in matches:
        chunks.append(text[cursor:match.start()])
        label = match.group("label")
        chunks.append(
            f"    sub qword ptr [rip + {REMAINING_SYMBOL}], 1\n"
            f"    jb {label}\n"
        )
        cursor = match.end()
    chunks.append(text[cursor:])
    output = "".join(chunks)

    storage = storage_matches[0]
    replacement = (
        ".section .data\n"
        "    .align 8\n"
        f"{REMAINING_SYMBOL}:\n"
        f"    .quad {limit}\n"
    )
    output, storage_count = _COUNT_STORAGE.subn(replacement, output, count=1)
    if storage_count != 1:
        raise SafeBudgetRewriteError("instruction-count storage was not replaced exactly once")

    if _COUNTDOWN_SITE_WIDE.search(output) or _COUNTDOWN_SITE_IMMEDIATE.search(output):
        raise SafeBudgetRewriteError("original instruction-budget site remains")
    if COUNT_SYMBOL in output or output.count(REMAINING_SYMBOL) != len(matches) + 1:
        raise SafeBudgetRewriteError("unexpected counter references remain after rewrite")
    if output.count("    sub qword ptr [rip + __s3_instruction_remaining], 1\n") != len(matches):
        raise SafeBudgetRewriteError("countdown site count does not match expected site count")
    if output.count("    jb ") < len(matches):
        raise SafeBudgetRewriteError("countdown failure branches are incomplete")

    result = CountdownRewrite(
        input_sha256=_sha256(text),
        output_sha256=_sha256(output),
        configured_limit=limit,
        expected_sites=len(matches),
        transformed_sites=len(matches),
        unexpected_mutations=0,
        storage_replaced=True,
    )
    if result.transformed_sites != result.expected_sites:
        raise SafeBudgetRewriteError("transformed site count does not match expected site count")
    return output, result


def countdown_boundary_contract() -> dict[str, Any]:
    """Return the arithmetic proof inputs used by the safety report."""

    return {
        "comparison": "unsigned remaining-before-instruction",
        "zero_budget": {"remaining": 0, "sub_result": UINT64_MAX, "carry": 1, "branch": "jb"},
        "one_budget": {"remaining": 1, "sub_result": 0, "carry": 0, "branch": "execute"},
        "uint64_max_budget": {"remaining": UINT64_MAX, "sub_result": UINT64_MAX - 1, "carry": 0, "branch": "execute"},
        "max_domain": f"0..{UINT64_MAX}",
        "state_lifetime": "initialized once per loaded shared object; decremented across repeated calls",
    }
