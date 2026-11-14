#!/usr/bin/env python3
"""V7 Integration Matrix (Wave 19): Cross-Repo Verification via Disposable Git Worktree."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Any

BENCH_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = BENCH_ROOT.parent
S3_ROOT = WORKSPACE_ROOT / "S3"
ELITE_ROOT = WORKSPACE_ROOT / "S3-Elite-Lab"
COMPACT_ROOT = WORKSPACE_ROOT / "S3-wt-compact-v18"
S3CNG_ROOT = WORKSPACE_ROOT / "S3-wt-s3cng"
REPORTS_ROOT = WORKSPACE_ROOT / "Relat-rio"

if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))


def _check_defaults_and_invariants() -> dict[str, Any]:
    from bootstrap.s3 import OptimizationLevel, compile_source
    from bootstrap.s3.backends.x86_64 import X8664Backend

    sample = """
export fn sum_sq(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 0
    while i < n:
        acc = acc + i * i
        i = i + 1
    return acc

fn main() -> i64:
    return sum_sq(5)
"""
    comp_default = compile_source(sample, OptimizationLevel.O1)
    backend_default = X8664Backend()

    # Check S3C_NG_DEFAULT=FALSE in isolated python process against S3-wt-s3cng
    s3cng_out = subprocess.run(
        [
            sys.executable,
            "-c",
            (
                "import sys; sys.path.insert(0, %r); "
                "from bootstrap.s3.compiler_provider import DEFAULT_COMPILER, CompilerKind; "
                "assert DEFAULT_COMPILER is CompilerKind.PYTHON; "
                "print(DEFAULT_COMPILER.value)"
            )
            % str(S3CNG_ROOT),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    result = {
        "predictive_exact_default": bool(comp_default.predictive_lowered_functions),
        "experimental_hoist_constants_mode_default": backend_default.experimental_hoist_constants_mode,
        "s3c_ng_default_provider": s3cng_out.stdout.strip(),
        "passed": (
            comp_default.predictive_lowered_functions == ()
            and backend_default.experimental_hoist_constants_mode == "off"
            and s3cng_out.stdout.strip() == "python"
        ),
    }
    assert result["passed"]
    return result


def _run_disposable_worktree_s3_and_compact() -> dict[str, Any]:
    t0 = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="s3-v7-int-wt-") as tmp_str:
        tmp = Path(tmp_str)
        wt_s3 = tmp / "s3_wt"
        compact_cache = tmp / "compact_cache"
        compact_cache.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "-C", str(S3_ROOT), "worktree", "add", "--detach", str(wt_s3), "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        try:
            # 1. Verify predictive native ELF/FFI + Discovery V3 from isolated worktree HEAD
            s3_probe = """
import ctypes, tempfile
from pathlib import Path
from bootstrap.s3 import OptimizationLevel, compile_source
from bootstrap.s3.ffi import build_shared_library
from bootstrap.s3.ir_emulator import execute_ir
from bootstrap.s3.predictive_discovery import SequenceConfidenceClass, discover_sequence_structure

src = '''
export fn quasi_pair(n: i64) -> i64:
    mut i: i64 = 0
    mut acc: i64 = 0
    while i < n:
        acc = acc + ((i * i + 3 * i + 1) / 2)
        i = i + 1
    return acc
fn main() -> i64:
    return quasi_pair(20)
'''
c_pred = compile_source(src, OptimizationLevel.O1, predictive_exact=True)
assert 'quasi_pair' in c_pred.predictive_lowered_functions
with tempfile.TemporaryDirectory() as td:
    so = build_shared_library(src, Path(td) / 'q.so', optimization='O1', predictive_exact=True)
    lib = ctypes.CDLL(str(so))
    lib.quasi_pair.argtypes = [ctypes.c_int64]
    lib.quasi_pair.restype = ctypes.c_int64
    for t in (0, 5, 25, 100):
        assert lib.quasi_pair(t) == execute_ir(c_pred.ir, entry='quasi_pair', arguments=[t])

rep = discover_sequence_structure([10.0 + 4.0 * (0.6 ** k) for k in range(16)], sequence_name='matrix_relax', horizon=2)
assert rep.confidence_class == SequenceConfidenceClass.APPROXIMATE_FORECAST
assert not rep.source_aware_verified
print('WORKTREE_S3_OK')
"""
            env_wt = os.environ.copy()
            env_wt["PYTHONPATH"] = str(wt_s3)
            r_s3 = subprocess.run(
                [sys.executable, "-c", s3_probe],
                cwd=str(wt_s3),
                env=env_wt,
                check=True,
                capture_output=True,
                text=True,
            )
            assert "WORKTREE_S3_OK" in r_s3.stdout

            # 2. Verify S3 Compact V21 compiled against disposable S3 V7 worktree
            compact_probe = """
import hashlib, time
from s3_compact.native_engine import NativeS3Engine
payload = (b'S3-V7-INTEGRATION-MATRIX-ROUNDTRIP-DATA-' * 900)[:32768]
t0 = time.perf_counter()
eng = NativeS3Engine()
init_s = time.perf_counter() - t0
cid, comp = eng.encode_lz_extended(payload)
dec = eng.decode_lz_extended(cid, comp, len(payload))
assert dec == payload
assert hashlib.sha256(dec).hexdigest() == hashlib.sha256(payload).hexdigest()
print(f'COMPACT_V21_OK:{len(comp)}:{init_s:.4f}')
"""
            env_cmp = os.environ.copy()
            env_cmp["PYTHONPATH"] = str(COMPACT_ROOT)
            env_cmp["S3_COMPACT_COMPILER_ROOT"] = str(wt_s3)
            env_cmp["S3_COMPACT_USE_LOCAL_COMPILER"] = "0"
            env_cmp["S3_COMPACT_OPT_LEVEL"] = "O1"
            env_cmp["S3_COMPACT_BUDGET_MODE"] = "loop-hybrid"
            env_cmp["S3_COMPACT_SELECTIVE_HP"] = "1"
            env_cmp["S3_COMPACT_NATIVE_CACHE_DIR"] = str(compact_cache)
            r_cmp = subprocess.run(
                [sys.executable, "-c", compact_probe],
                cwd=str(COMPACT_ROOT),
                env=env_cmp,
                check=True,
                capture_output=True,
                text=True,
            )
            line = next(ln for ln in r_cmp.stdout.splitlines() if ln.startswith("COMPACT_V21_OK:"))
            _, comp_bytes_s, init_s_s = line.split(":")
        finally:
            subprocess.run(
                ["git", "-C", str(S3_ROOT), "worktree", "remove", "--force", str(wt_s3)],
                check=False,
                capture_output=True,
                text=True,
            )
            subprocess.run(
                ["git", "-C", str(S3_ROOT), "worktree", "prune"],
                check=False,
                capture_output=True,
                text=True,
            )

    wt_list = subprocess.run(
        ["git", "-C", str(S3_ROOT), "worktree", "list"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    assert "s3-v7-int-wt-" not in wt_list
    return {
        "passed": True,
        "elapsed_sec": round(time.perf_counter() - t0, 3),
        "compact_v21_32kib_compressed_bytes": int(comp_bytes_s),
        "compact_v21_cold_compile_sec": float(init_s_s),
        "disposable_worktree_cleaned": True,
    }


def _check_doom_m55() -> dict[str, Any]:
    ev_path = ELITE_ROOT / "docs" / "reports" / "evidence" / "v7" / "m55_benchmark.json"
    ev = json.loads(ev_path.read_text(encoding="utf-8"))
    assert str(ev.get("parity", "")).startswith("passed")
    assert ev["m55PerRound"]["traps"] == 0
    assert ev["m55PerRound"]["fallbacks"] == 0

    win_node = Path("/mnt/c/Program Files/nodejs/node.exe")
    node_exe = str(win_node) if win_node.is_file() else shutil.which("node")
    assert node_exe is not None, "node executable not found"
    if win_node.is_file():
        # Redirect stdio to a real Windows-backed file to avoid WSL pipe EISDIR in Node.exe.
        win_tmp_parent = Path("/mnt/c/Users/samue/AppData/Local/Temp")
        tmp_parent = win_tmp_parent if win_tmp_parent.is_dir() else ELITE_ROOT
        with tempfile.TemporaryDirectory(prefix="s3_doom_m55_", dir=str(tmp_parent)) as td:
            log_path = Path(td) / "doom_node_test.log"
            with log_path.open("wb") as log_f:
                res = subprocess.run(
                    [
                        node_exe,
                        "--test",
                        "tests/doom-m55-line-trace.test.mjs",
                        "tests/doom-v7-spatial-index.test.mjs",
                    ],
                    cwd=str(ELITE_ROOT),
                    stdin=subprocess.DEVNULL,
                    stdout=log_f,
                    stderr=subprocess.STDOUT,
                    check=False,
                )
            stdout_text = log_path.read_text(encoding="utf-8", errors="replace")
            if res.returncode != 0:
                raise RuntimeError(f"node --test failed ({res.returncode}):\n{stdout_text}")
    else:
        res = subprocess.run(
            [
                node_exe,
                "--test",
                "tests/doom-m55-line-trace.test.mjs",
                "tests/doom-v7-spatial-index.test.mjs",
            ],
            cwd=str(ELITE_ROOT),
            check=True,
            capture_output=True,
            text=True,
        )
        stdout_text = res.stdout
    return {
        "passed": res.returncode == 0 and "fail 0" in stdout_text,
        "evidence_path": "S3-Elite-Lab/docs/reports/evidence/v7/m55_benchmark.json",
        "broadphase_candidate_prep_ms": ev["candidatePreparationMsPerRound"],
        "s3_wasm_composed_ms": ev["composedTotalMeanMsPerRound"]["s3Wasm"],
        "node_test_output_lines": len(stdout_text.splitlines()),
    }


def _check_s3cng_v7_corpus() -> dict[str, Any]:
    probe = """
import sys
sys.path.insert(0, %r)
from tools import v7_differential_corpus as c
from bootstrap.s3.pipeline import compile_sources
from bootstrap.s3.ir_emulator import execute_ir

v7_ids = [
    'v7-quasi-poly-mod3-sum',
    'v7-gf2-rule90-xor-step',
    'v7-predictive-o1-closed-form-binomial',
    'v7-compute-stencil-fixed-row',
]
by_id = {case.case_id: case for case in c.ALL_CORPUS_CASES}
for cid in v7_ids:
    case = by_id[cid]
    comp = compile_sources(case.source_map(), entry_module=case.entry_module)
    val = execute_ir(comp.ir, entry=case.entry_function)
    assert val == case.expected_return, (cid, val, case.expected_return)
print('S3CNG_V7_CORPUS_OK:' + str(len(c.ALL_CORPUS_CASES)))
""" % str(S3CNG_ROOT)
    res = subprocess.run(
        [sys.executable, "-c", probe],
        cwd=str(S3CNG_ROOT),
        check=True,
        capture_output=True,
        text=True,
    )
    line = next(ln for ln in res.stdout.splitlines() if ln.startswith("S3CNG_V7_CORPUS_OK:"))
    total_cases = int(line.split(":")[1])
    return {
        "passed": True,
        "total_manifest_cases": total_cases,
        "v7_cases_verified": 4,
    }


def _check_benchmark_artifacts() -> dict[str, Any]:
    required = {
        "native_predictive": BENCH_ROOT / "benchmarks" / "v7_native_predictive" / "results_v7_native_predictive.json",
        "gcc_reproducibility": BENCH_ROOT / "benchmarks" / "v7_gcc_reproducibility" / "results_after.json",
        "compute_ca_gpu": BENCH_ROOT / "benchmarks" / "v7_compute_ca_gpu" / "results_v7_compute_ca_gpu.json",
        "unknown_dynamics": BENCH_ROOT / "benchmarks" / "v7_unknown_dynamics" / "results_v7_unknown_dynamics.json",
        "compiler_research": BENCH_ROOT / "benchmarks" / "v7_compiler_research" / "results_v7_compiler_research.json",
    }
    hashes: dict[str, str] = {}
    for key, path in required.items():
        data = path.read_bytes()
        json.loads(data.decode("utf-8"))
        hashes[key] = hashlib.sha256(data).hexdigest()[:16]
    return {"passed": True, "artifact_sha256_prefix16": hashes}


def main() -> int:
    t0 = time.perf_counter()
    results = {
        "campaign": "S3_V7_WAVE19_INTEGRATION_MATRIX",
        "defaults_and_invariants": _check_defaults_and_invariants(),
        "disposable_worktree_s3_and_compact_v21": _run_disposable_worktree_s3_and_compact(),
        "doom_m55_spatial_and_wasm": _check_doom_m55(),
        "s3c_ng_v7_corpus_parity": _check_s3cng_v7_corpus(),
        "benchmark_artifact_schemas": _check_benchmark_artifacts(),
    }
    results["all_checks_passed"] = all(
        section.get("passed") is True for key, section in results.items() if isinstance(section, dict)
    )
    results["total_elapsed_sec"] = round(time.perf_counter() - t0, 3)

    out_path = Path(__file__).resolve().with_name("results_v7_integration_matrix.json")
    out_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))
    return 0 if results["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
