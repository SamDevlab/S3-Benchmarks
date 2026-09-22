from __future__ import annotations

import json

from tools.budget_generalization import (
    MATERIAL_SHARE_THRESHOLD,
    VARIANTS,
    _balanced_order,
    _classify,
)
from tools.runtime_attribution import remove_instruction_budget_instrumentation


def test_budget_generalization_declares_six_variants_and_materiality_gate() -> None:
    assert VARIANTS == (
        "S3_O0_BASELINE",
        "S3_O0_NO_BUDGET",
        "S3_O1_BASELINE",
        "S3_O1_NO_BUDGET",
        "GCC_O2",
        "CLANG_O2",
    )
    assert MATERIAL_SHARE_THRESHOLD == 0.10


def test_balanced_schedule_rotates_every_variant_before_repeating() -> None:
    assert _balanced_order(0) == VARIANTS
    assert _balanced_order(1) == VARIANTS[1:] + VARIANTS[:1]
    flattened = [label for repetition in range(len(VARIANTS)) for label in _balanced_order(repetition)]
    assert len(flattened) == len(VARIANTS) ** 2
    assert all(flattened.count(label) == len(VARIANTS) for label in VARIANTS)


def test_budget_rewrite_derives_sites_and_rejects_partial_layout() -> None:
    site = (
        "    movabs r11, 10000000000\n"
        "    cmp qword ptr [rip + __s3_instruction_count], r11\n"
        "    jae .L__s3_failure_site_1\n"
        "    inc qword ptr [rip + __s3_instruction_count]\n"
    )
    rewritten, result = remove_instruction_budget_instrumentation(site + site.replace("_1", "_2"))
    assert rewritten == ""
    assert result.expected_sites == 2
    assert result.removed_sites == 2
    assert result.unexpected_mutations == 0


def test_generalization_classification_does_not_treat_missing_data_as_zero() -> None:
    workloads = [
        {"id": "hpc.prk.nstream", "causal_classification": "CONFIRMED_CAUSAL"},
        {"id": "realworld.jsmn", "causal_classification": "BLOCKED"},
        {"id": "scientific.xsbench.compatible_lookup.medium", "causal_classification": "CONFIRMED_CAUSAL"},
    ]
    assert _classify(workloads) == "SYSTEMIC_PARTIAL"
    assert json.loads(json.dumps(workloads))[1]["causal_classification"] == "BLOCKED"
