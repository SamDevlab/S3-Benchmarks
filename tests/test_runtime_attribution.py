from __future__ import annotations

import pytest

from tools.runtime_attribution import (
    DiagnosticRewriteError,
    audit_assembly,
    remove_instruction_budget_instrumentation,
)


SITE = (
    "    movabs r11, 10000000000\n"
    "    cmp qword ptr [rip + __s3_instruction_count], r11\n"
    "    jae .L__s3_failure_site_7\n"
    "    inc qword ptr [rip + __s3_instruction_count]\n"
)


def test_rewriter_removes_only_complete_expected_site() -> None:
    source = "header:\n    mov rax, 1\n" + SITE + "    add rax, 2\n"
    output, result = remove_instruction_budget_instrumentation(source)

    assert output == "header:\n    mov rax, 1\n    add rax, 2\n"
    assert result.expected_sites == 1
    assert result.removed_sites == 1
    assert result.unexpected_mutations == 0


def test_rewriter_counts_all_sites_and_preserves_other_budget_symbols() -> None:
    source = SITE + "label:\n    mov rax, qword ptr [rip + __s3_instruction_count]\n"
    with pytest.raises(DiagnosticRewriteError, match="not exclusively complete"):
        remove_instruction_budget_instrumentation(source)


@pytest.mark.parametrize(
    "source",
    [
        SITE.replace("inc qword ptr", "add qword ptr", 1),
        SITE.replace("10000000000", "9999999999", 1),
        SITE.replace("jae .L__s3_failure_site_7\n", "", 1),
        SITE.replace("__s3_instruction_count", "__s3_other_counter", 1),
    ],
)
def test_rewriter_fails_closed_on_unknown_or_partial_layout(source: str) -> None:
    with pytest.raises(DiagnosticRewriteError):
        remove_instruction_budget_instrumentation(source)


def test_static_audit_separates_budget_sites_from_other_operations() -> None:
    source = (
        ".section .text\n"
        "fn:\n"
        "    inc qword ptr [rip + __s3_frame_count]\n"
        "    cmp qword ptr [rip + __s3_frame_count], 1024\n"
        "    jg .frame_fail\n"
        + SITE
        + "    call helper\n"
        "    mov rax, qword ptr [rbp - 8]\n"
    )
    audit = audit_assembly(source)
    assert audit["instruction_budget_check_sites"] == 1
    assert audit["frame_limit_check_sites"] == 1
    assert audit["call_count_static"] == 1
    assert audit["branch_count_static"] == 2
    assert audit["counts_are_static"] is True
    assert audit["so_size_bytes"] is None
