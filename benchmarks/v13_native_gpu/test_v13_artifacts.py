"""V13 recorded empirical data integrity; never assert speedup as a CI contract."""
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def load(name):
    return json.loads((HERE/name).read_text("utf-8"))

def test_native_ctz_real_s3_and_gcc_controls():
    data=load("results_native_v13.json")
    assert data["cpu_pmu_available"] is False
    assert data["measurements_include_compilation"] is False
    assert data["rounds"]==9
    assert len(data["cases"])==7
    assert sum(len(c["samples"]) for c in data["cases"])==28
    for case in data["cases"]:
        assert len(case["certificate_sha256"])==64
        assert "s3_v13" in case["assembly"]
        assert case["assembly"]["s3_v13"]["hot_symbols"]
        for sample in case["samples"]:
            assert sample["parity"] is True
            for value in sample["median_ns"].values():
                assert value>0

def test_inline_is_separate_optional_ab():
    data=load("results_inline_ab_v13.json")
    assert data["status"]=="EXPERIMENTAL_NO_AUTO_PROMOTION"
    assert len(data["cases"])==4
    for case in data["cases"]:
        assert len(case["samples"])==3
        assert case["assembly"]["v13_inline"]["hot_instructions_including_helpers"]>0
        for row in case["samples"]:
            assert row["parity"] is True
            assert row["ctz_ns"]>0 and row["inline_ns"]>0

def test_physical_gpu_vs_native_windows_c_parity_and_safety():
    data=load("results_gpu_vs_native_c_v13.json")
    assert data["status"]=="EXPLORATORY_ONE_HOST_SESSION_NOT_DISPATCH_QUALIFIED"
    assert data["device"]["name"]=="AMD Radeon RX 580 2048SP"
    assert data["device"]["is_physical"] is True
    assert data["device"]["backend"]=="Vulkan"
    assert data["sessions"]==1
    assert data["rounds_per_case"]==7
    assert data["automatic_production_gpu_dispatch"] is False
    assert data["windows_cpu_native_c_comparison"] is True
    assert data["gpu_to_s3_native_cpu_comparison"] is False
    assert len(data["cases"])==3
    for case in data["cases"]:
        assert case["physical_gpu_parity"] is True
        assert case["native_c_parity"] is True
        assert case["buffer_bytes"]<=131072
        assert case["gpu_total_ms"]>0
        assert case["native_c_total_ms"]>0
        assert len(case["all_samples_ms"]["gpu_total"])==7
        assert len(case["all_samples_ms"]["native_c_total"])==7

def test_native_compiler_cold_timing_not_fabricated():
    data=load("results_gpu_vs_native_c_v13.json")
    if data["native_c_dll_reused_after_cold_compilation_timeout"]:
        assert data["c_compile_cold_ms"] is None

def test_all_three_physical_sessions_and_cost_policy_choose_cpu():
    baseline=load("results_gpu_vs_native_c_v13.json")
    sessions=[baseline,load("results_gpu_vs_native_c_v13_s2.json"),
              load("results_gpu_vs_native_c_v13_s3.json")]
    for session in sessions:
        assert session["device"]==baseline["device"]
        assert session["sessions"]==1
        assert session["rounds_per_case"]==7
        assert len(session["cases"])==3
        for c in session["cases"]:
            assert c["physical_gpu_parity"] and c["native_c_parity"]
            assert c["gpu_total_ms"]>c["native_c_total_ms"]
    decision=load("results_placement_v13.json")
    assert decision["same_host_distinct_process_sessions"]==3
    assert decision["independent_machines"]==1
    assert decision["automatic_production_dispatch"] is False
    assert len(decision["cases"])==3
    for case in decision["cases"]:
        assert case["decision"]=="CPU"
        assert case["reason"]=="NO_CONSERVATIVE_GPU_GAIN"
        assert case["accepted_sessions"]==3
        assert all(value>1 for value in case["session_ratios_gpu_over_native_c"])
