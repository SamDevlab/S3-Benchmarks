"""Consistency and schema verification tests for S3 Scientific Expansion V2 benchmarks."""

from __future__ import annotations

import json
from pathlib import Path


RESULTS_JSON = Path(__file__).resolve().parent / "results_v2.json"
RESULTS_MD = Path(__file__).resolve().parent / "RESULTS_V2.md"


def test_results_v2_artifacts_exist() -> None:
    assert RESULTS_JSON.exists(), "results_v2.json must be generated"
    assert RESULTS_MD.exists(), "RESULTS_V2.md must be generated"


def test_results_v2_schema_and_native_parity() -> None:
    payload = json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
    assert payload["campaign"] == "S3_SCIENTIFIC_EXPANSION_V2"
    assert payload["phase"] == "P1_CURRENT_NATIVE_BENCHMARKS"
    assert len(payload["s3_compiler_sha"]) >= 7
    assert len(payload["benchmarks_sha"]) >= 7

    env = payload["environment"]
    assert env["clang"] == "NOT_MEASURED"
    assert env["rustc"] == "NOT_MEASURED"
    assert env["zig"] == "NOT_MEASURED"

    workloads = payload["workloads"]
    assert {"jsmn", "rmsd", "stencil2d", "control_kernels"} <= set(workloads)

    # 1. JSMN corpora
    for cname in ("small", "medium", "large"):
        c_entry = workloads["jsmn"][cname]
        assert c_entry["input_bytes"] > 0
        assert c_entry["expected_tokens"] > 0
        for impl_key, impl_data in c_entry["implementations"].items():
            assert impl_data["classification"] == "CURRENT_NATIVE"
            assert impl_data["parity_pass"] is True, f"JSMN {cname} {impl_key} failed parity"
            assert impl_data["tokens"] == c_entry["expected_tokens"]
            assert impl_data["checksum"] == c_entry["expected_checksum"]
            assert impl_data["median_ns"] > 0

    # 2. RMSD scales + standalone ELF
    for scale in ("64", "256", "1024", "8192"):
        s_entry = workloads["rmsd"]["scales"][scale]
        assert s_entry["max_abs_error"] <= 1e-9
        for impl_key, impl_data in s_entry["implementations"].items():
            assert impl_data["classification"] == "CURRENT_NATIVE"
            assert impl_data["parity_pass"] is True
            assert impl_data["max_abs_error"] <= 1e-9
            assert impl_data["median_ns"] > 0

    elf = workloads["rmsd"]["standalone_similarity_distance_elf"]
    assert elf["classification"] == "CURRENT_NATIVE"
    assert elf["parity_pass"] is True
    assert elf["observed_checksum"] == 29356
    assert elf["text_bytes"] > 0
    assert elf["binary_bytes"] > elf["text_bytes"]

    # 3. Stencil 2D
    for grid in ("64x40", "128x80", "256x160"):
        g_entry = workloads["stencil2d"][grid]
        assert len(g_entry["expected_sha256"]) == 64
        for impl_key, impl_data in g_entry["implementations"].items():
            assert impl_data["classification"] == "CURRENT_NATIVE"
            assert impl_data["parity_pass"] is True
            assert impl_data["output_sha256"] == g_entry["expected_sha256"]
            assert impl_data["median_ns"] > 0
        # Verify EXACT_SEGMENT is faster than PER_INSTRUCTION on real 2D stencil
        per_ns = g_entry["implementations"]["s3_o1_per_instruction"]["median_ns"]
        exact_ns = g_entry["implementations"]["s3_o1_exact_segment"]["median_ns"]
        assert exact_ns < per_ns

    # 4. Control kernels
    for kname in ("GEMM_I64_32x32", "RULE110_CA_256x128", "FNV1A_HASH_4096x10"):
        k_entry = workloads["control_kernels"][kname]
        for impl_key, impl_data in k_entry["implementations"].items():
            assert impl_data["classification"] == "CURRENT_NATIVE"
            assert impl_data["parity_pass"] is True
            assert impl_data["checksum"] == k_entry["expected_checksum"]
            assert impl_data["median_ns"] > 0
