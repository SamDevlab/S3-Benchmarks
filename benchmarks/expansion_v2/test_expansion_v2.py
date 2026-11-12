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


def test_p6_p7_compute_compact_schema_and_parity() -> None:
    p6_p7_path = Path(__file__).resolve().parent / "p6_p7_compute_compact.json"
    assert p6_p7_path.exists()
    data = json.loads(p6_p7_path.read_text(encoding="utf-8"))

    p6 = data["phase_p6_s3_compute"]
    assert p6["exact_instruction_budget_N_8x8_stencil"] == 3901
    assert p6["boundary_checks"]["N_minus_1"]["per_instruction_trapped"] is True
    assert p6["boundary_checks"]["N_minus_1"]["exact_segment_trapped"] is True
    assert p6["boundary_checks"]["N_exact"]["per_instruction_stdout"] == "program returned: 220"
    assert p6["boundary_checks"]["N_exact"]["exact_segment_stdout"] == "program returned: 220"

    p7 = data["phase_p7_s3_compact"]
    assert len(p7["corpora"]) == 5
    for _cname, c in p7["corpora"].items():
        variants = c["variants"]
        for variant in ("v18_control_o0_per_inst", "v18_p4_o1_exact_seg", "v19_prefilter_o1_exact_seg"):
            assert variants[variant]["roundtrip_sha256_match"] is True
            assert variants[variant]["payload_identical_to_v18"] is True
        assert variants["v18_p4_o1_exact_seg"]["encode_median_ns"] < variants["v18_control_o0_per_inst"]["encode_median_ns"]
        assert variants["v18_p4_o1_exact_seg"]["decode_median_ns"] < variants["v18_control_o0_per_inst"]["decode_median_ns"]


def test_p11_p13_studies_schema_and_ternary_advantage() -> None:
    p11_p13_path = Path(__file__).resolve().parent / "p11_p13_p15_studies.json"
    assert p11_p13_path.exists()
    data = json.loads(p11_p13_path.read_text(encoding="utf-8"))

    p11 = data["p11_elf_footprint"]
    assert p11["study"] == "P11_MINIMAL_ELF_AND_BINARY_FOOTPRINT"
    assert len(p11["entries"]) >= 16

    p13 = data["p13_balanced_ternary"]
    assert p13["study"] == "P13_BALANCED_TERNARY_VS_BINARY"
    assert p13["elements_n"] == 4096
    assert p13["physical_memory_reduction_ratio"] == 8.0
    assert p13["ternary_trit_representation"]["physical_x86_64_abi_slot_bytes"] == 1
    assert p13["binary_i64_representation"]["physical_x86_64_abi_slot_bytes"] == 8
    assert p13["ternary_trit_representation"]["s3_asm_instructions"] < p13["binary_i64_representation"]["s3_asm_instructions"]
    assert p13["speedup_ternary_vs_binary_i64"] > 1.0


def test_live_native_stencil_reproduction() -> None:
    import subprocess
    import sys
    import tempfile

    s3_repo = Path(__file__).resolve().parents[3] / "S3"
    if not s3_repo.exists():
        return
    for p in (str(s3_repo), str(s3_repo / "bootstrap")):
        if p not in sys.path:
            sys.path.insert(0, p)

    from s3.backends.x86_64 import InstructionBudgetMode, NativeToolchain, X8664Backend
    from s3.optimizer import OptimizationLevel
    from s3.pipeline import compile_source
    from tests.test_x86_64_tsstore_register_preservation import SPLIT_INLINE_STENCIL_SOURCE

    src = SPLIT_INLINE_STENCIL_SOURCE

    comp_o0 = compile_source(src, optimization=OptimizationLevel.O0)
    comp_o1 = compile_source(src, optimization=OptimizationLevel.O1)
    _, asm_o0 = comp_o0.require_ordinary_artifacts()
    _, asm_o1 = comp_o1.require_ordinary_artifacts()

    inst_o0 = sum(len(b.instructions) for fn in asm_o0.functions for b in fn.blocks)
    inst_o1 = sum(len(b.instructions) for fn in asm_o1.functions for b in fn.blocks)
    blk_o0 = sum(len(fn.blocks) for fn in asm_o0.functions)
    blk_o1 = sum(len(fn.blocks) for fn in asm_o1.functions)

    assert (inst_o0, inst_o1) == (352, 202)
    assert (blk_o0, blk_o1) == (78, 38)

    import ctypes

    NativeToolchain.detect()
    w, h = 64, 40
    n = w * h
    init_grid = [(i * 17 + 31) % 257 for i in range(n)]
    outputs: dict[str, list[int]] = {}

    with tempfile.TemporaryDirectory(prefix="s3_repro_stencil_", dir="/tmp") as tmp:
        for label, asm, mode in [
            ("o0_per_inst", asm_o0, InstructionBudgetMode.PER_INSTRUCTION),
            ("o0_exact_seg", asm_o0, InstructionBudgetMode.EXACT_SEGMENT),
            ("o1_per_inst", asm_o1, InstructionBudgetMode.PER_INSTRUCTION),
            ("o1_exact_seg", asm_o1, InstructionBudgetMode.EXACT_SEGMENT),
        ]:
            s_path = Path(tmp) / f"stencil_{label}.s"
            so_path = Path(tmp) / f"stencil_{label}.so"
            asm_text = X8664Backend(
                max_instructions=50_000_000,
                register_allocation=True,
                instruction_budget_mode=mode,
            )._generate_ffi(asm)
            s_path.write_text(asm_text, encoding="utf-8")
            subprocess.run(
                ["gcc", "-shared", "-fPIC", "-O2", str(s_path), "-o", str(so_path)],
                check=True,
            )
            lib = ctypes.CDLL(str(so_path))
            fn = lib.stencil5point_step
            fn.argtypes = [
                ctypes.POINTER(ctypes.c_int64),
                ctypes.c_int64,
                ctypes.c_int64,
                ctypes.c_int64,
                ctypes.POINTER(ctypes.c_int64),
                ctypes.c_int64,
            ]
            fn.restype = ctypes.c_int64
            cur = (ctypes.c_int64 * n)(*init_grid)
            nxt = (ctypes.c_int64 * n)(*([0] * n))
            rc = fn(cur, n, w, h, nxt, n)
            assert rc == 0
            outputs[label] = list(nxt)

    ref = outputs["o0_per_inst"]
    assert any(x != 0 for x in ref)
    assert outputs["o0_exact_seg"] == ref
    assert outputs["o1_per_inst"] == ref
    assert outputs["o1_exact_seg"] == ref

    # Verify 10-generation SHA-256 oracle parity against results_v2.json and live GCC -O2
    import hashlib
    from benchmarks.expansion_v2.run_native_expansion_v2 import C_STENCIL5POINT_SOURCE

    payload = json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
    expected_sha256_64x40 = payload["workloads"]["stencil2d"]["64x40"]["expected_sha256"]
    init_64x40 = [(i * 37 + 19) % 512 for i in range(n)]

    with tempfile.TemporaryDirectory(prefix="s3_repro_c_vs_s3_", dir="/tmp") as tmp:
        c_path = Path(tmp) / "stencil_c.c"
        c_so = Path(tmp) / "stencil_c.so"
        c_path.write_text(C_STENCIL5POINT_SOURCE, encoding="utf-8")
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(c_path), "-o", str(c_so)], check=True)
        c_lib = ctypes.CDLL(str(c_so))
        c_fn = c_lib.stencil5point_step
        c_fn.argtypes = [
            ctypes.POINTER(ctypes.c_int64), ctypes.c_int64,
            ctypes.c_int64, ctypes.c_int64,
            ctypes.POINTER(ctypes.c_int64), ctypes.c_int64,
        ]
        c_fn.restype = ctypes.c_int64

        s3_path = Path(tmp) / "stencil_s3_o1_exact.s"
        s3_so = Path(tmp) / "stencil_s3_o1_exact.so"
        s3_asm_text = X8664Backend(
            max_instructions=50_000_000,
            register_allocation=True,
            instruction_budget_mode=InstructionBudgetMode.EXACT_SEGMENT,
        )._generate_ffi(asm_o1)
        s3_path.write_text(s3_asm_text, encoding="utf-8")
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s3_path), "-o", str(s3_so)], check=True)
        s3_lib = ctypes.CDLL(str(s3_so))
        s3_fn = s3_lib.stencil5point_step
        s3_fn.argtypes = c_fn.argtypes
        s3_fn.restype = ctypes.c_int64

        for fn in (c_fn, s3_fn):
            ba = (ctypes.c_int64 * n)(*init_64x40)
            bb = (ctypes.c_int64 * n)(*([0] * n))
            for _ in range(10):
                assert fn(ba, n, w, h, bb, n) == 0
                ba, bb = bb, ba
            digest = hashlib.sha256(",".join(map(str, list(ba))).encode("ascii")).hexdigest()
            assert digest == expected_sha256_64x40



