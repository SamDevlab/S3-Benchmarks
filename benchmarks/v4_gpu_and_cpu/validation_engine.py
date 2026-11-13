"""Reusable numerical validation and corruption-detection engine for S3-Benchmarks."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import numpy as np


@dataclass(frozen=True)
class ToleranceContract:
    algorithm: str
    precision: str
    atol: float
    rtol: float
    rationale: str


def get_contract(algorithm: str, precision: str = "f32", *, k_dim: int = 1, steps: int = 1) -> ToleranceContract:
    alg = algorithm.lower()
    prec = precision.lower()
    if prec not in ("f32", "f64"):
        raise ValueError(f"Unsupported precision: {precision}")

    if alg == "matmul":
        if prec == "f32":
            # Binary32 eps ~ 1.19e-7; k accumulations allow O(k * eps) rounding + FMA difference
            atol = max(1e-4, k_dim * 1e-6)
            rtol = max(1e-4, k_dim * 5e-6)
            return ToleranceContract(alg, prec, atol, rtol, f"f32 MatMul with k={k_dim} accumulations + FMA")
        return ToleranceContract(alg, prec, 1e-11, 1e-11, "f64 MatMul accumulation contract")

    if alg == "axpy":
        return (
            ToleranceContract(alg, prec, 1e-6, 1e-6, "f32 single multiply-add per element")
            if prec == "f32"
            else ToleranceContract(alg, prec, 1e-13, 1e-13, "f64 single multiply-add per element")
        )

    if alg == "stencil":
        if prec == "f32":
            atol = 1e-3 if steps >= 50 else 1e-4
            rtol = 1e-3 if steps >= 50 else 1e-4
            return ToleranceContract(alg, prec, atol, rtol, f"f32 2D stencil over {steps} time steps")
        return ToleranceContract(alg, prec, 1e-11, 1e-11, "f64 stencil contract")

    if alg == "dft":
        return (
            ToleranceContract(alg, prec, 1e-3, 1e-4, "f32 DFT O(N) trig/accumulation error")
            if prec == "f32"
            else ToleranceContract(alg, prec, 1e-10, 1e-11, "f64 DFT contract")
        )

    if alg == "fir":
        return (
            ToleranceContract(alg, prec, 1e-4, 1e-4, "f32 FIR tap accumulation")
            if prec == "f32"
            else ToleranceContract(alg, prec, 1e-11, 1e-11, "f64 FIR contract")
        )

    if alg == "fem":
        return ToleranceContract(alg, prec, 1e-8, 1e-7, "1D FEM linear system & strain energy conditioning")

    if alg == "cg":
        return ToleranceContract(alg, prec, 1e-7, 1e-6, "Conjugate Gradient iterative residual tolerance")

    if alg == "quadrature":
        return ToleranceContract(alg, prec, 1e-8, 1e-8, "Simpson/Trapz quadrature convergence contract")

    if alg == "ode":
        return ToleranceContract(alg, prec, 1e-6, 1e-6, "ODE time integration truncation/conservation contract")

    if alg == "monte_carlo":
        return ToleranceContract(alg, prec, 0.05, 0.05, "Monte Carlo deterministic seed / statistical error bound")

    if alg == "particles":
        return (
            ToleranceContract(alg, prec, 1e-4, 1e-4, "f32 particle kinematics/restitution")
            if prec == "f32"
            else ToleranceContract(alg, prec, 1e-10, 1e-10, "f64 particle kinematics/restitution")
        )

    if alg == "image":
        return (
            ToleranceContract(alg, prec, 1e-4, 1e-4, "f32 image luminance/convolution")
            if prec == "f32"
            else ToleranceContract(alg, prec, 1e-11, 1e-11, "f64 image processing")
        )

    raise ValueError(f"Unknown algorithm contract: {algorithm}")


def _ulp_diff(a: np.ndarray, b: np.ndarray, precision: str) -> int:
    finite_mask = np.isfinite(a) & np.isfinite(b)
    if not np.any(finite_mask):
        return 0
    if precision == "f32":
        af = a[finite_mask].astype(np.float32, copy=False).view(np.int32).astype(np.int64)
        bf = b[finite_mask].astype(np.float32, copy=False).view(np.int32).astype(np.int64)
        af = np.where(af < 0, np.int64(0x80000000) - af, af)
        bf = np.where(bf < 0, np.int64(0x80000000) - bf, bf)
        return int(np.max(np.abs(af - bf)))
    af = a[finite_mask].astype(np.float64, copy=False).view(np.int64)
    bf = b[finite_mask].astype(np.float64, copy=False).view(np.int64)
    # Use Python big-int safe unsigned comparison for f64 ULPs
    diff = np.abs(af.astype(np.int64) - bf.astype(np.int64))
    return int(np.max(diff))


def validate_array(
    *,
    benchmark_id: str,
    kernel: str,
    algorithm: str,
    actual: Sequence[float] | np.ndarray,
    reference: Sequence[float] | np.ndarray | None,
    reference_name: str = "numpy_reference",
    precision: str = "f32",
    k_dim: int = 1,
    steps: int = 1,
    check_signed_zero: bool = False,
) -> dict[str, Any]:
    act = np.asarray(actual, dtype=np.float32 if precision == "f32" else np.float64).ravel()
    input_size = int(act.size)
    contract = get_contract(algorithm, precision, k_dim=k_dim, steps=steps)

    if reference is None:
        return {
            "BENCHMARK_ID": benchmark_id,
            "KERNEL": kernel,
            "REFERENCE": "NONE",
            "INPUT_SIZE": input_size,
            "PRECISION": precision,
            "ATOL": contract.atol,
            "RTOL": contract.rtol,
            "MAX_ABS_ERROR": None,
            "MAX_REL_ERROR": None,
            "RMS_ERROR": None,
            "MISMATCH_COUNT": None,
            "FIRST_MISMATCH_INDEX": None,
            "NUMERICAL_VALIDITY": "NOT_VALIDATED",
            "DATA_INTEGRITY": "NOT_VALIDATED",
            "PERFORMANCE_VALIDITY": "DIAGNOSTIC_ONLY",
            "DIAGNOSTICS": {"reason": "No reference array provided"},
        }

    ref = np.asarray(reference, dtype=np.float32 if precision == "f32" else np.float64).ravel()
    if act.shape != ref.shape:
        return {
            "BENCHMARK_ID": benchmark_id,
            "KERNEL": kernel,
            "REFERENCE": reference_name,
            "INPUT_SIZE": input_size,
            "PRECISION": precision,
            "ATOL": contract.atol,
            "RTOL": contract.rtol,
            "MAX_ABS_ERROR": float("inf"),
            "MAX_REL_ERROR": float("inf"),
            "RMS_ERROR": float("inf"),
            "MISMATCH_COUNT": max(act.size, ref.size),
            "FIRST_MISMATCH_INDEX": 0,
            "NUMERICAL_VALIDITY": "INVALID",
            "DATA_INTEGRITY": "CORRUPTION_SUSPECTED:SHAPE_MISMATCH",
            "PERFORMANCE_VALIDITY": "DIAGNOSTIC_ONLY",
            "DIAGNOSTICS": {"actual_size": int(act.size), "ref_size": int(ref.size)},
        }

    nan_count = int(np.sum(np.isnan(act)))
    inf_count = int(np.sum(np.isinf(act)))
    abs_err = np.abs(act.astype(np.float64) - ref.astype(np.float64))
    rel_denom = np.maximum(np.abs(ref.astype(np.float64)), 1e-12)
    rel_err = abs_err / rel_denom

    tol_per_elem = contract.atol + contract.rtol * np.abs(ref.astype(np.float64))
    mismatch_mask = (~np.isfinite(act)) | (abs_err > tol_per_elem)

    signed_zero_mismatches = 0
    if check_signed_zero:
        zero_both = (act == 0.0) & (ref == 0.0)
        sign_diff = np.signbit(act) != np.signbit(ref)
        sz_mask = zero_both & sign_diff
        signed_zero_mismatches = int(np.sum(sz_mask))
        mismatch_mask = mismatch_mask | sz_mask

    mismatch_indices = np.flatnonzero(mismatch_mask)
    mismatch_count = int(mismatch_indices.size)
    first_mismatch = int(mismatch_indices[0]) if mismatch_count > 0 else None

    finite_err = abs_err[np.isfinite(abs_err)]
    max_abs = float(np.max(finite_err)) if finite_err.size else float("inf")
    max_rel = float(np.max(rel_err[np.isfinite(rel_err)])) if np.any(np.isfinite(rel_err)) else float("inf")
    rms = float(np.sqrt(np.mean(finite_err ** 2))) if finite_err.size else float("inf")

    int_dtype = np.uint32 if precision == "f32" else np.uint64
    bit_mismatches = int(np.sum(act.view(int_dtype) != ref.view(int_dtype)))
    max_ulp = _ulp_diff(act, ref, precision)

    # Corruption classification
    integrity_flags: list[str] = []
    if nan_count > 0 or inf_count > 0:
        integrity_flags.append("NON_FINITE_DETECTED")
    unexpected_zero = (act == 0.0) & (np.abs(ref) > max(contract.atol * 100.0, 1e-3))
    if np.any(unexpected_zero):
        integrity_flags.append("UNEXPECTED_ZERO_CORRUPTION")
    if mismatch_count > 0:
        max_tol = float(np.max(tol_per_elem)) if tol_per_elem.size else contract.atol
        if 0 < mismatch_count <= max(8, int(0.05 * input_size)) and max_abs > max(100.0 * max_tol, 0.05):
            integrity_flags.append("ISOLATED_LARGE_SPIKE")
        mod4_3 = int(np.sum((mismatch_indices % 4) == 3))
        if mismatch_count >= 4 and mod4_3 >= int(0.75 * mismatch_count):
            integrity_flags.append("SUSPECT_INDEX_STRIDE_MOD4_EQ_3")
        if not integrity_flags:
            integrity_flags.append("TOLERANCE_EXCEEDED")

    numerical_valid = mismatch_count == 0 and nan_count == 0 and inf_count == 0
    data_integrity = "PASS" if not integrity_flags else f"CORRUPTION_SUSPECTED:{','.join(integrity_flags)}"
    perf_validity = "VALID" if numerical_valid and data_integrity == "PASS" else "DIAGNOSTIC_ONLY"

    return {
        "BENCHMARK_ID": benchmark_id,
        "KERNEL": kernel,
        "REFERENCE": reference_name,
        "INPUT_SIZE": input_size,
        "PRECISION": precision,
        "ATOL": contract.atol,
        "RTOL": contract.rtol,
        "MAX_ABS_ERROR": round(max_abs, 9) if np.isfinite(max_abs) else "inf",
        "MAX_REL_ERROR": round(max_rel, 9) if np.isfinite(max_rel) else "inf",
        "RMS_ERROR": round(rms, 9) if np.isfinite(rms) else "inf",
        "MISMATCH_COUNT": mismatch_count,
        "FIRST_MISMATCH_INDEX": first_mismatch,
        "NUMERICAL_VALIDITY": "VALID" if numerical_valid else "INVALID",
        "DATA_INTEGRITY": data_integrity,
        "PERFORMANCE_VALIDITY": perf_validity,
        "DIAGNOSTICS": {
            "nan_count": nan_count,
            "inf_count": inf_count,
            "signed_zero_mismatches": signed_zero_mismatches,
            "bit_mismatch_count": bit_mismatches,
            "max_ulp_diff": max_ulp,
            "contract_rationale": contract.rationale,
        },
    }


def reclassify_v4_3_results(src_path: Path, dst_path: Path) -> dict[str, Any]:
    raw = json.loads(src_path.read_text(encoding="utf-8"))
    records: list[dict[str, Any]] = []

    for bench_name, impls in raw.get("cpu", {}).get("compiler_comparison", {}).items():
        for impl_name in impls:
            records.append({
                "BENCHMARK_ID": f"V4_3_CPU_{bench_name}_{impl_name}",
                "KERNEL": f"{bench_name}:{impl_name}",
                "REFERENCE": "NONE_IN_V4_3_SUITE",
                "INPUT_SIZE": 2000 if "simpson" in bench_name else 12,
                "PRECISION": "f64",
                "ATOL": None,
                "RTOL": None,
                "MAX_ABS_ERROR": None,
                "MAX_REL_ERROR": None,
                "RMS_ERROR": None,
                "MISMATCH_COUNT": None,
                "FIRST_MISMATCH_INDEX": None,
                "NUMERICAL_VALIDITY": "NOT_VALIDATED",
                "DATA_INTEGRITY": "NOT_VALIDATED",
                "PERFORMANCE_VALIDITY": "DIAGNOSTIC_ONLY",
                "RECLASSIFICATION_NOTE": "V4.3 timed compiler comparison without per-run output comparison; reclassified to NOT_VALIDATED",
            })

    for lab_name in raw.get("cpu", {}).get("lab_benchmarks", {}):
        records.append({
            "BENCHMARK_ID": f"V4_3_LAB_{lab_name}",
            "KERNEL": lab_name,
            "REFERENCE": "NONE_IN_V4_3_SUITE",
            "INPUT_SIZE": None,
            "PRECISION": "f64",
            "ATOL": None,
            "RTOL": None,
            "MAX_ABS_ERROR": None,
            "MAX_REL_ERROR": None,
            "RMS_ERROR": None,
            "MISMATCH_COUNT": None,
            "FIRST_MISMATCH_INDEX": None,
            "NUMERICAL_VALIDITY": "NOT_VALIDATED",
            "DATA_INTEGRITY": "NOT_VALIDATED",
            "PERFORMANCE_VALIDITY": "DIAGNOSTIC_ONLY",
            "RECLASSIFICATION_NOTE": "V4.3 timed lab kernel without per-run output comparison; reclassified to NOT_VALIDATED",
        })

    for mm in raw.get("gpu", {}).get("matmul", []):
        n = int(mm["n"])
        contract = get_contract("matmul", "f32", k_dim=n)
        max_abs = float(mm["max_abs_error"])
        # Re-evaluate against strict MatMul f32 contract instead of V4.3's loose 1e-2 threshold
        strict_valid = max_abs <= max(contract.atol, contract.rtol * 10.0) and bool(mm.get("NUMERICALLY_VALID_RESULT"))
        records.append({
            "BENCHMARK_ID": f"V4_3_GPU_MATMUL_{mm['kernel']}_{n}",
            "KERNEL": mm["kernel"],
            "REFERENCE": "numpy_f32_matmul",
            "INPUT_SIZE": n * n,
            "PRECISION": "f32",
            "ATOL": contract.atol,
            "RTOL": contract.rtol,
            "MAX_ABS_ERROR": max_abs,
            "MAX_REL_ERROR": None,
            "RMS_ERROR": None,
            "MISMATCH_COUNT": None,
            "FIRST_MISMATCH_INDEX": None,
            "NUMERICAL_VALIDITY": "VALID" if strict_valid else "INVALID",
            "DATA_INTEGRITY": "PASS" if strict_valid else "CORRUPTION_OR_CONTRACT_VIOLATION",
            "PERFORMANCE_VALIDITY": "VALID" if strict_valid else "DIAGNOSTIC_ONLY",
            "HISTORICAL_V4_3_VALID_FLAG": mm.get("NUMERICALLY_VALID_RESULT"),
            "RECLASSIFICATION_NOTE": (
                "V4.3 MatMul V3 128x128 (max_abs=0.009526) was marked valid by loose <1e-2 rule; reclassified INVALID under MatMul contract"
                if mm["kernel"] == "V3_padded_fma" and n == 128
                else "Reclassified under V4.4 MatMul f32 contract"
            ),
        })

    for lab_name in raw.get("gpu", {}).get("gpu_labs", {}):
        records.append({
            "BENCHMARK_ID": f"V4_3_GPULAB_{lab_name}",
            "KERNEL": lab_name,
            "REFERENCE": "NONE_IN_V4_3_SUITE",
            "INPUT_SIZE": None,
            "PRECISION": "f32",
            "ATOL": None,
            "RTOL": None,
            "MAX_ABS_ERROR": None,
            "MAX_REL_ERROR": None,
            "RMS_ERROR": None,
            "MISMATCH_COUNT": None,
            "FIRST_MISMATCH_INDEX": None,
            "NUMERICAL_VALIDITY": "NOT_VALIDATED",
            "DATA_INTEGRITY": "NOT_VALIDATED",
            "PERFORMANCE_VALIDITY": "DIAGNOSTIC_ONLY",
            "RECLASSIFICATION_NOTE": "V4.3 timed GPU lab without per-run output comparison; reclassified to NOT_VALIDATED",
        })

    out = {
        "SOURCE_FILE": str(src_path.name),
        "RECLASSIFICATION_POLICY": "S3_V4_4_VALIDATION_ENGINE",
        "SUMMARY": {
            "TOTAL": len(records),
            "VALID": sum(1 for r in records if r["NUMERICAL_VALIDITY"] == "VALID"),
            "INVALID": sum(1 for r in records if r["NUMERICAL_VALIDITY"] == "INVALID"),
            "NOT_VALIDATED": sum(1 for r in records if r["NUMERICAL_VALIDITY"] == "NOT_VALIDATED"),
        },
        "RECORDS": records,
    }
    dst_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    return out
