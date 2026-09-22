from __future__ import annotations

import pytest

from tools.safe_budget_architecture import (
    UINT64_MAX,
    SafeBudgetRewriteError,
    countdown_boundary_contract,
    transform_global_countdown,
)


def _assembly(*, limit: int = 10_000_000_000, sites: int = 2) -> str:
    body = "".join(
        f"    movabs r11, {limit}\n"
        "    cmp qword ptr [rip + __s3_instruction_count], r11\n"
        f"    jae .L__s3_failure_site_{index}\n"
        "    inc qword ptr [rip + __s3_instruction_count]\n"
        "    nop\n"
        for index in range(sites)
    )
    return (
        ".section .text\nfn:\n"
        + body
        + "    ret\n"
        + ".section .bss\n"
        + "    .align 8\n__s3_frame_count:\n    .zero 8\n"
        + "    .align 8\n__s3_instruction_count:\n    .zero 8\n"
    )


def test_global_countdown_rewrites_all_sites_and_initializes_remaining() -> None:
    output, result = transform_global_countdown(_assembly())

    assert result.expected_sites == 2
    assert result.transformed_sites == 2
    assert result.unexpected_mutations == 0
    assert "sub qword ptr [rip + __s3_instruction_remaining], 1" in output
    assert output.count("sub qword ptr [rip + __s3_instruction_remaining], 1") == 2
    assert "jb .L__s3_failure_site_0" in output
    assert "__s3_instruction_remaining:\n    .quad 10000000000" in output
    assert "__s3_instruction_count" not in output


@pytest.mark.parametrize("limit", [0, 1, 0x7FFFFFFF, 0x80000000, UINT64_MAX])
def test_countdown_accepts_uint64_boundary_domain(limit: int) -> None:
    output, result = transform_global_countdown(_assembly(limit=limit, sites=1))
    assert result.configured_limit == limit
    assert f".quad {limit}" in output


def test_countdown_contract_makes_unsigned_underflow_explicit() -> None:
    contract = countdown_boundary_contract()
    assert contract["zero_budget"]["branch"] == "jb"
    assert contract["one_budget"]["branch"] == "execute"
    assert contract["uint64_max_budget"]["branch"] == "execute"


@pytest.mark.parametrize(
    "source",
    [
        _assembly().replace("    inc qword ptr", "    add qword ptr", 1),
        _assembly().replace("10000000000", "9999999999", 1),
        _assembly().replace("    jae .L__s3_failure_site_0\n", "", 1),
        _assembly().replace("__s3_instruction_count:\n    .zero 8\n", "", 1),
        _assembly() + "    mov rax, qword ptr [rip + __s3_instruction_count]\n",
    ],
)
def test_countdown_fails_closed_on_partial_or_unknown_layout(source: str) -> None:
    with pytest.raises(SafeBudgetRewriteError):
        transform_global_countdown(source)


def test_countdown_requires_expected_limit_when_supplied() -> None:
    with pytest.raises(SafeBudgetRewriteError):
        transform_global_countdown(_assembly(), expected_limit=42)
