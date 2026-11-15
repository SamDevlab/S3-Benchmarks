"""Cross-family semantic contracts on a B+A overlay, not production integration.

The two V12 PRs use separate registries with different eligibility
contracts. This test ensures coexistence without conflating their APIs,
using real S3 IR rather than names or synthetic descriptions.
"""
from __future__ import annotations

import pytest

from bootstrap.s3.pipeline import compile_source,OptimizationLevel
from bootstrap.s3.verified_strategy_registry import (
    discover_verified_candidates,select_verified_strategy,
    StrategyCostObservation,
)
from bootstrap.s3.verified_candidates_v12 import (
    register_verified_candidates,select_verified_candidate,
    CandidateProofError,
)
from bootstrap.s3.verified_i64_progression import certify_i64_progression_ir
from bootstrap.s3.verified_i64_native import compile_certified_i64_native


def ir(expression):
    source=(f"export fn transform(x: i64) -> i64:\n"
            f"    return {expression}\n"
            "fn main() -> i64:\n"
            "    return 0\n")
    return compile_source(
        source,optimization=OptimizationLevel.O0,predictive_exact=False,
    ).require_ordinary_artifacts()[0]


def test_checked_progression_registry_a_and_b_are_distinct_families():
    sample=ir("x + 7")
    a=discover_verified_candidates(sample,"transform")
    assert [x.name for x in a]==[
        "BASELINE_S3_IR","I64_CHECKED_PROGRESSION"
    ]
    b=register_verified_candidates(
        sample,"transform",enable_experimental=True
    )
    assert [x.strategy for x in b]==["UNMODIFIED"]
    assert all(not x.automatic_production_pass for x in a)
    assert all(x.proof_scope for x in b)


def test_identity_registry_b_is_not_claimed_as_progression_a():
    sample=ir("x * 1")
    a=discover_verified_candidates(sample,"transform")
    b=register_verified_candidates(
        sample,"transform",enable_experimental=True
    )
    assert [x.name for x in a]==["BASELINE_S3_IR"]
    assert [x.strategy for x in b]==[
        "UNMODIFIED","I64_PURE_IDENTITY"
    ]
    selected=select_verified_candidate(
        sample,"transform",enable_experimental=True
    )
    assert selected.generated_s3_source is not None
    assert selected.proven_machine_code is False


def test_b_optin_and_a_native_optin_are_independently_enforced():
    sample=ir("x + 7")
    with pytest.raises(CandidateProofError,match="EXPERIMENTAL_OPT_IN_REQUIRED"):
        register_verified_candidates(sample,"transform")
    cert=certify_i64_progression_ir(sample,"transform")
    with pytest.raises(Exception,match="EXPERIMENTAL_OPT_IN_REQUIRED"):
        compile_certified_i64_native(sample,cert)


def test_cost_registry_a_defaults_to_original_when_missing_measured_facts():
    sample=ir("x + 7")
    baseline,alternative=discover_verified_candidates(sample,"transform")
    # Incomplete measured information must not drive an optimization.
    decision=select_verified_strategy(
        sample,"transform",(baseline,alternative),{},expected_calls=100,
    )
    assert decision.selected=="BASELINE_S3_IR"
    assert decision.production_compiler_changed is False
