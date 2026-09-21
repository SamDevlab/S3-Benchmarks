from tools.ffi_direct_kernel_methodology import (
    VARIANTS,
    _driver_source,
    _pilot_sources,
    _select_common_k,
    _expected,
)


def test_phase_a_declares_four_ffi_families_and_matching_symbols() -> None:
    pilots = _pilot_sources()
    assert [pilot.workload_id for pilot in pilots] == [
        "memory.babelstream.triad",
        "hpc.prk.nstream",
        "numerical.polybench.gemm",
        "scientific.rmsd.batch",
    ]
    assert [pilot.symbol for pilot in pilots] == ["triad", "nstream", "gemm", "rmsd"]
    assert all("export fn identity_f64" in pilot.source for pilot in pilots)
    assert all("double identity_f64" in pilot.c_source for pilot in pilots)


def test_phase_a_oracles_follow_runtime_call_contract() -> None:
    pilots = _pilot_sources()
    assert _expected(pilots[0], 1) == 3813.0
    assert _expected(pilots[1], 1) == 1085.0
    assert _expected(pilots[1], 10) == 1085.0 + 9 * 589.0
    assert _expected(pilots[2], 1) == 5008704.0
    assert _expected(pilots[3], 1) == 16.0


def test_phase_a_driver_is_shared_dlopen_runtime_k_and_monotonic_raw() -> None:
    source = _driver_source()
    assert "dlopen" in source
    assert "dlsym" in source
    assert "CLOCK_MONOTONIC_RAW" in source
    assert "for (int64_t i = 0; i < k; ++i)" in source
    assert "--workload" not in source


def test_phase_a_selects_one_common_runtime_k() -> None:
    calibration = {
        label: [
            {"K": 1, "status": "PASS", "elapsed_ns": 1_000_000},
            {"K": 100, "status": "PASS", "elapsed_ns": 70_000_000 if label == VARIANTS[0] else 90_000_000},
        ]
        for label in VARIANTS
    }
    selected, decision = _select_common_k(calibration)
    assert selected == 100
    assert decision["status"] == "PASS"
