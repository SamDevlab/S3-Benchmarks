"""V14 corpus integrity and boundary checks for actual S3 CPU/GPU output."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def artifact(name):
    return json.loads((ROOT/name).read_text("utf-8"))


def test_same_initial_fixtures_and_final_gpu_native_s3_digest():
    native=artifact("results_native_s3_cpu_v14.json")
    gpu=artifact("results_s3_physical_gpu_v14.json")
    assert "WSL" in native["engine"]
    assert "Vulkan" in gpu["engine"]
    assert gpu["device"]["is_physical"] is True
    assert gpu["device"]["backend"]=="Vulkan"
    assert "AMD Radeon RX 580" in gpu["device"]["name"]
    assert native["ffi_boundary"].startswith("one exported S3 native call")
    assert gpu["sessions"]==1
    assert len(native["cases"])==len(gpu["cases"])==3
    for cpu,g in zip(native["cases"],gpu["cases"]):
        assert (cpu["width"],cpu["height"],cpu["steps"])==(
            g["width"],g["height"],g["steps"]
        )
        assert cpu["fixture_from_physical_gpu"] is True
        assert cpu["native_s3_parity"] is True
        assert cpu["gpu_digest_agrees"] is True
        assert cpu["source_input_sha256"]==g["initial_input_sha256"]
        assert cpu["final_output_sha256"]==g["final_output_sha256"]
        stem=f"conway_{cpu['width']}x{cpu['height']}_g{cpu['steps']}"
        binary=(ROOT/"fixtures"/(stem+"_input_i32le.bin")).read_bytes()
        digest=(ROOT/"fixtures"/(stem+"_gpu_output_sha256.txt")).read_text().strip()
        assert hashlib.sha256(binary).hexdigest()==cpu["source_input_sha256"]
        assert digest==cpu["final_output_sha256"]
        assert len(binary)==cpu["width"]*cpu["height"]*4
        assert len(cpu["all_samples_native_s3_cpu_ms"])==7
        assert len(g["samples"])==7
        assert cpu["median_native_s3_cpu_ms"]>0
        assert g["median_gpu_total_ms"]>0
        assert all(x["total_ms"]>0 for x in g["samples"])


def test_native_backend_ablation_retains_exact_outputs():
    files=(
        "results_native_s3_cpu_v14.json",
        "results_native_s3_cpu_v14_loop_hybrid_peephole.json",
        "results_native_s3_cpu_v14_exact_segment.json",
        "results_native_s3_cpu_v14_exact_segment_peephole.json",
    )
    corpora=[artifact(name) for name in files]
    for c in corpora:
        assert len(c["cases"])==3
        assert c["build"]["s3_generated_assembly_sha256"]
        for row in c["cases"]:
            assert row["native_s3_parity"]
            assert row["gpu_digest_agrees"]
            assert row["fixture_from_physical_gpu"]
    for i in range(3):
        ids={item["cases"][i]["final_output_sha256"] for item in corpora}
        assert len(ids)==1


def test_peephole_three_sessions_do_not_justify_global_promotion():
    corpora=[artifact("results_general_native_v14.json"),
            artifact("results_general_native_v14_s2.json"),
            artifact("results_general_native_v14_s3.json")]
    assert [a["session_id"] for a in corpora]==["s1","s2","s3"]
    for entry in corpora:
        assert entry["status"]=="EXPERIMENTAL_ONLY_NOT_PROMOTED"
        assert entry["asm_peephole_stats"]["dropped_fallthrough_jumps"]>0
        assert len(entry["bench"]["cases"])==5
        assert entry["bench"]["rounds"]==9
        assert all(
            row["parity"] and row["baseline_ns"]>0 and row["experimental_ns"]>0
            for row in entry["bench"]["cases"]
        )
    # At least one regression: the transform is not a universal optimization.
    assert any(
        row["speedup"]<1.0
        for entry in corpora for row in entry["bench"]["cases"]
    )


def test_no_cross_os_runtime_results_can_be_used_for_production_placement():
    cpu=artifact("results_native_s3_cpu_v14.json")
    gpu=artifact("results_s3_physical_gpu_v14.json")
    assert cpu["status"]=="EXPERIMENTAL_HOSTED_FFI_NOT_SAME_OS_AS_WINDOWS_GPU"
    assert gpu["production_dispatch_enabled"] is False
    assert cpu["build"]["s3_source_sha256"]
    assert gpu["gpu_source_hash"]
    # The two source programs implement the same bounded Conway rule;
    # matching test vectors alone are not a proof of general semantic equivalence.
    assert cpu["build"]["s3_source_sha256"]!=gpu["gpu_source_hash"]
