from __future__ import annotations

import pytest

from tools.runtime_attribution import (
    DiagnosticRewriteError,
    audit_assembly,
    remove_frame_budget_instrumentation,
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


def _frame_site(index: int, *, limit: int = 1024) -> str:
    return (
        f"fn{index}:\n"
        "    inc qword ptr [rip + __s3_frame_count]\n"
        f"    cmp qword ptr [rip + __s3_frame_count], {limit}\n"
        f"    jg .L__s3_failure_site_{index}\n"
        "    push rbp\n"
        "    mov rbp, rsp\n"
        "    nop\n"
        "    dec qword ptr [rip + __s3_frame_count]\n"
        "    leave\n"
        "    ret\n"
    )


def test_frame_rewriter_removes_exact_three_sites_and_preserves_prologue() -> None:
    source = "".join(_frame_site(index) for index in range(3))
    output, result = remove_frame_budget_instrumentation(source)

    assert output.count("inc qword ptr [rip + __s3_frame_count]") == 0
    assert output.count("cmp qword ptr [rip + __s3_frame_count]") == 0
    assert output.count("dec qword ptr [rip + __s3_frame_count]") == 0
    assert output.count("    push rbp\n") == 3
    assert output.count("jg .L__s3_failure_site_") == 0
    assert result.expected_sites == 3
    assert result.removed_sites == 3
    assert result.unexpected_mutations == 0


@pytest.mark.parametrize(
    "source",
    [
        _frame_site(0) + _frame_site(1),
        _frame_site(0).replace("    dec qword ptr [rip + __s3_frame_count]\n", "", 1)
        + _frame_site(1)
        + _frame_site(2),
        _frame_site(0, limit=2048) + _frame_site(1) + _frame_site(2),
        _frame_site(0).replace("    push rbp\n", "    push rbx\n", 1)
        + _frame_site(1)
        + _frame_site(2),
    ],
)
def test_frame_rewriter_fails_closed_on_partial_unknown_or_wrong_layout(source: str) -> None:
    with pytest.raises(DiagnosticRewriteError):
        remove_frame_budget_instrumentation(source)


def test_frame_rewriter_does_not_mutate_unmatched_failure_reporting() -> None:
    source = "".join(_frame_site(index) for index in range(3)) + (
        ".L__s3_failure_site_0:\n"
        "    mov rdi, qword ptr [rip + __s3_frame_count]\n"
        "    call __s3_fail_message\n"
    )
    output, result = remove_frame_budget_instrumentation(source)

    assert "mov rdi, qword ptr [rip + __s3_frame_count]" in output
    assert result.unexpected_mutations == 0
