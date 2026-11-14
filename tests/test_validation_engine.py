from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "benchmarks" / "v4_gpu_and_cpu"))
from validation_engine import get_contract, reclassify_v4_3_results, validate_array


def test_validation_engine_exact_and_f32_rounding() -> None:
    ref = np.linspace(1.0, 10.0, 64, dtype=np.float32)
    act = ref.copy()
    r = validate_array(benchmark_id="B1", kernel="axpy", algorithm="axpy", actual=act, reference=ref, precision="f32")
    assert r["NUMERICAL_VALIDITY"] == "VALID"
    assert r["DATA_INTEGRITY"] == "PASS"
    assert r["PERFORMANCE_VALIDITY"] == "VALID"
    assert r["MISMATCH_COUNT"] == 0
    assert r["FIRST_MISMATCH_INDEX"] is None


def test_validation_engine_detects_nan_zero_and_isolated_spike() -> None:
    ref = np.ones(128, dtype=np.float32) * 5.0
    act = ref.copy()
    act[11] = 0.0
    act[23] = float("nan")
    r = validate_array(benchmark_id="B2", kernel="mm", algorithm="matmul", actual=act, reference=ref, precision="f32", k_dim=128)
    assert r["NUMERICAL_VALIDITY"] == "INVALID"
    assert r["PERFORMANCE_VALIDITY"] == "DIAGNOSTIC_ONLY"
    assert r["FIRST_MISMATCH_INDEX"] == 11
    assert "NON_FINITE_DETECTED" in r["DATA_INTEGRITY"]
    assert "UNEXPECTED_ZERO_CORRUPTION" in r["DATA_INTEGRITY"]


def test_validation_engine_detects_mod4_lane3_pattern_and_signed_zero() -> None:
    ref = np.zeros(16, dtype=np.float32)
    act = np.zeros(16, dtype=np.float32)
    act[3] = -0.0
    r0 = validate_array(
        benchmark_id="B3",
        kernel="k",
        algorithm="axpy",
        actual=act,
        reference=ref,
        precision="f32",
        check_signed_zero=True,
    )
    assert r0["DIAGNOSTICS"]["signed_zero_mismatches"] == 1
    assert r0["NUMERICAL_VALIDITY"] == "INVALID"

    ref2 = np.ones(32, dtype=np.float32)
    act2 = ref2.copy()
    act2[3::4] += 10.0
    r1 = validate_array(benchmark_id="B4", kernel="k", algorithm="axpy", actual=act2, reference=ref2, precision="f32")
    assert "SUSPECT_INDEX_STRIDE_MOD4_EQ_3" in r1["DATA_INTEGRITY"]


def test_not_validated_when_reference_is_none() -> None:
    r = validate_array(benchmark_id="B5", kernel="simpson", algorithm="quadrature", actual=[1.0, 2.0], reference=None, precision="f64")
    assert r["NUMERICAL_VALIDITY"] == "NOT_VALIDATED"
    assert r["PERFORMANCE_VALIDITY"] == "DIAGNOSTIC_ONLY"


def test_all_12_contracts_exist_and_v4_3_reclassification(tmp_path: Path) -> None:
    for alg in ("matmul", "axpy", "stencil", "dft", "fir", "fem", "cg", "quadrature", "ode", "monte_carlo", "particles", "image"):
        c = get_contract(alg, "f64" if alg in ("fem", "cg", "quadrature", "ode", "monte_carlo") else "f32")
        assert c.rationale
    src = Path(__file__).resolve().parents[1] / "benchmarks" / "v4_gpu_and_cpu" / "results_v4_3.json"
    dst = tmp_path / "reclass.json"
    out = reclassify_v4_3_results(src, dst)
    assert out["SUMMARY"]["INVALID"] >= 4
    v3_128 = [r for r in out["RECORDS"] if r["BENCHMARK_ID"] == "V4_3_GPU_MATMUL_V3_padded_fma_128"][0]
    assert v3_128["NUMERICAL_VALIDITY"] == "INVALID"
    assert v3_128["PERFORMANCE_VALIDITY"] == "DIAGNOSTIC_ONLY"

