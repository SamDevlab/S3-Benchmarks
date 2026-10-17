#!/usr/bin/env python3
"""Pinned characterization of one S3 source across hosted and S3-TISA V3.

This records separate compile-only, hosted compile+execute, S3-to-TISA
compile/lower/execute, and already-lowered TISA-emulator execution samples.
Wall times are machine-local characterization, not portable speedup claims.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import statistics
import subprocess
import sys
import time
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "benchmarks" / "s3-tisa-v3" / "fixtures" / "arithmetic_add.s3"
CPU_V3_SHA = "326ac9a9082b9e6a542c52320a9b13ba61efe1a0"
COMPILER_SHA = "2eab8a43f07b7fc842c4036ea0fb0203a9d41d6c"
SHARED_CONTRACT_SHA = "01358CE2A836935E4E5AA1BF5FF40EF07660FCF61AD03000D402D9FE812159C9"
TISA_CONTRACT_SHA = "15C73B54E8BDF0CE8A0E32E236E894D4191486C9F388DE324A5699EFA1B0967C"
EXPECTED_RESULT = 42
MAX_REPETITIONS = 1_000


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_sha256(value: Any) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(data)


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True,
        encoding="utf-8", errors="replace", check=False,
    )
    if result.returncode:
        raise ValueError(f"git {' '.join(args)} failed for {root}: {result.stderr.strip()}")
    return result.stdout.strip()


def require_clean_pin(root: Path, expected_sha: str, label: str) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"{label} checkout does not exist: {root}")
    top = Path(_git(root, "rev-parse", "--show-toplevel")).resolve()
    if top != root:
        raise ValueError(f"{label} path must be the Git checkout root: {root}")
    head = _git(root, "rev-parse", "HEAD").lower()
    if head != expected_sha:
        raise ValueError(f"{label} pin mismatch: expected {expected_sha}, got {head}")
    if _git(root, "status", "--porcelain=v1", "--untracked-files=all"):
        raise ValueError(f"{label} checkout is dirty: {root}")
    return {"root": str(root), "commit": head, "clean": True}


def _percentile95(samples: list[int]) -> int:
    if not samples:
        raise ValueError("timing sample set must not be empty")
    return sorted(samples)[max(0, math.ceil(0.95 * len(samples)) - 1)]


def summarize_samples(samples: list[int], warmups: int) -> dict[str, Any]:
    if not samples or any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in samples):
        raise ValueError("timing samples must be a non-empty list of non-negative integer nanoseconds")
    return {
        "unit": "nanoseconds",
        "warmups": warmups,
        "repetitions": len(samples),
        "median": int(statistics.median(samples)),
        "p95_nearest_rank": _percentile95(samples),
        "min": min(samples),
        "max": max(samples),
        "samples": samples,
    }


def _measure(function, *, warmups: int, repetitions: int, expected: Any) -> tuple[dict[str, Any], Any]:
    for _ in range(warmups):
        result = function()
        if result != expected:
            raise ValueError(f"warmup result mismatch: expected {expected!r}, got {result!r}")
    samples: list[int] = []
    last: Any = None
    for _ in range(repetitions):
        start = time.perf_counter_ns()
        last = function()
        elapsed = time.perf_counter_ns() - start
        if last != expected:
            raise ValueError(f"measured result mismatch: expected {expected!r}, got {last!r}")
        samples.append(elapsed)
    return summarize_samples(samples, warmups), last


def _load_reference_compiler(root: Path):
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    sys.dont_write_bytecode = True
    root_text = str(root.resolve())
    if root_text not in sys.path:
        sys.path.insert(0, root_text)
    from bootstrap.s3.pipeline import compile_source, run_source

    module = sys.modules.get("bootstrap.s3.pipeline")
    module_file = getattr(module, "__file__", None)
    if module_file is None or not Path(module_file).resolve().is_relative_to(root.resolve()):
        raise ValueError("loaded hosted compiler API did not originate from the pinned compiler checkout")
    return compile_source, run_source


def run_benchmark(
    *, compiler_root: Path, cpu_root: Path, source_path: Path,
    warmups: int, repetitions: int,
) -> dict[str, Any]:
    if isinstance(warmups, bool) or not isinstance(warmups, int) or not 0 <= warmups <= 100:
        raise ValueError("warmups must be an integer in [0, 100]")
    if isinstance(repetitions, bool) or not isinstance(repetitions, int) or not 1 <= repetitions <= MAX_REPETITIONS:
        raise ValueError(f"repetitions must be an integer in [1, {MAX_REPETITIONS}]")

    compiler_identity = require_clean_pin(compiler_root, COMPILER_SHA, "compiler")
    cpu_identity = require_clean_pin(cpu_root, CPU_V3_SHA, "CPU V3")
    source_path = source_path.resolve()
    source_bytes = source_path.read_bytes()
    source = source_bytes.decode("utf-8", errors="strict")

    contract_paths = {
        "shared_lab": (cpu_root.resolve() / "contracts" / "s3-lab-contract.v1.json", SHARED_CONTRACT_SHA),
        "tisa_v1": (cpu_root.resolve() / "contracts" / "s3.tisa.v1.json", TISA_CONTRACT_SHA),
    }
    contract_hashes: dict[str, str] = {}
    for name, (path, expected) in contract_paths.items():
        digest = sha256_file(path)
        if digest != expected:
            raise ValueError(f"{name} contract hash mismatch: expected {expected}, got {digest}")
        contract_hashes[name] = digest

    cpu_source = str(cpu_root.resolve() / "src")
    sys.path.insert(0, cpu_source)
    from s3cpu.cpu import CPU, ExecutionStatus
    from s3cpu.target.pipeline import compile_and_run_source

    compile_source, run_source = _load_reference_compiler(compiler_root)

    # CompilationResult is not equality-stable across calls; validate outputs
    # explicitly while retaining a separate compile-only timing distribution.
    for _ in range(warmups):
        warm_compile = compile_source(source, "O0")
        warm_compile.require_ordinary_artifacts()
    compile_samples: list[int] = []
    compilation = None
    for _ in range(repetitions):
        start = time.perf_counter_ns()
        compilation = compile_source(source, "O0")
        elapsed = time.perf_counter_ns() - start
        compilation.require_ordinary_artifacts()
        compile_samples.append(elapsed)
    compile_timing = summarize_samples(compile_samples, warmups)

    hosted_timing, hosted_result = _measure(
        lambda: run_source(source, entry="main", optimization="O0"),
        warmups=warmups, repetitions=repetitions, expected=EXPECTED_RESULT,
    )

    def compile_target() -> tuple[Any, Any]:
        return compile_and_run_source(source, compiler_root)

    for _ in range(warmups):
        warm_lowered, warm_target_report = compile_target()
        if warm_target_report.target_status != "PASS" or warm_target_report.parity != "PASS":
            raise ValueError("warmup S3-to-TISA compilation did not pass hosted/emulator parity")
        if warm_target_report.hosted_result != EXPECTED_RESULT or warm_target_report.cpu_result != EXPECTED_RESULT:
            raise ValueError("warmup S3-to-TISA result mismatch")

    target_samples: list[int] = []
    lowered = None
    target_report = None
    for _ in range(repetitions):
        start = time.perf_counter_ns()
        lowered, target_report = compile_target()
        target_samples.append(time.perf_counter_ns() - start)
        if target_report.target_status != "PASS" or target_report.parity != "PASS":
            raise ValueError("S3-to-TISA compilation did not pass hosted/emulator parity")
        if target_report.hosted_result != EXPECTED_RESULT or target_report.cpu_result != EXPECTED_RESULT:
            raise ValueError("S3-to-TISA compile/run result mismatch")
    target_timing = summarize_samples(target_samples, warmups)
    assert lowered is not None and target_report is not None

    cpu = CPU()

    def run_emulator() -> tuple[str, int, int]:
        cpu.load_program(lowered.program)
        state = cpu.run(max_steps=10_000)
        if state.status is not ExecutionStatus.HALTED:
            raise ValueError(f"TISA emulator did not halt: {state.status.value} {state.fault}")
        result = state.registers[lowered.return_physical_register]
        return state.status.value, result, state.cycle_count

    for _ in range(warmups):
        status, result, cycles = run_emulator()
        if (status, result) != (ExecutionStatus.HALTED.value, EXPECTED_RESULT):
            raise ValueError("TISA emulator warmup did not produce the expected halted state")
    emulator_samples: list[int] = []
    emulator_result: tuple[str, int, int] | None = None
    for _ in range(repetitions):
        start = time.perf_counter_ns()
        emulator_result = run_emulator()
        emulator_samples.append(time.perf_counter_ns() - start)
        if emulator_result[:2] != (ExecutionStatus.HALTED.value, EXPECTED_RESULT):
            raise ValueError("TISA emulator result mismatch")
    emulator_timing = summarize_samples(emulator_samples, warmups)
    assert emulator_result is not None

    source_digest = sha256_bytes(source_bytes)
    if target_report.source_sha256.upper() != source_digest:
        raise ValueError("CPU target pipeline reported a different source hash")
    machine_digest = sha256_bytes(lowered.machine_code)
    if target_report.machine_code_sha256.upper() != machine_digest:
        raise ValueError("CPU target pipeline reported a different machine-code hash")
    if target_report.cpu_result != emulator_result[1] or target_report.cpu_attempt_count != emulator_result[2]:
        raise ValueError("independent repeated emulator state disagrees with target pipeline report")

    try:
        recorded_source_path = source_path.relative_to(ROOT).as_posix()
    except ValueError:
        recorded_source_path = str(source_path)

    report: dict[str, Any] = {
        "schema": "s3.v3.longitudinal-benchmark-report/v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "status": "PASS",
        "classification": "CHARACTERIZATION_ONLY_NO_SPEEDUP_CLAIM",
        "pins": {
            "compiler": compiler_identity,
            "cpu_v3": cpu_identity,
            "contracts_sha256": contract_hashes,
        },
        "workload": {
            "id": "s3.tryte-add-42.v1",
            "source_path": recorded_source_path,
            "source_sha256": source_digest,
            "expected_result": EXPECTED_RESULT,
            "optimization": "O0",
        },
        "environment": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "python": platform.python_version(),
            "timer": "time.perf_counter_ns",
        },
        "measurements": {
            "compiler_compile_only": compile_timing,
            "hosted_compile_and_execute": hosted_timing,
            "s3_to_tisa_compile_lower_and_emulator": target_timing,
            "tisa_emulator_only": emulator_timing,
        },
        "correctness": {
            "hosted_result": hosted_result,
            "cpu_target_status": target_report.target_status,
            "cpu_target_parity": target_report.parity,
            "cpu_emulator_result": target_report.cpu_result,
            "independent_repeated_emulator_result": emulator_result[1],
            "rtl": {"status": "NOT_MEASURED_BY_THIS_INCREMENT", "reason": "RTL qualification is recorded separately in S3-CPU evidence."},
            "wasm_wasi": {"status": "NOT_MEASURED_BY_THIS_INCREMENT", "reason": "WASI cross-target qualification is a separate lane."},
            "native": {"status": "NOT_RUN", "reason": "No native code path is included in this V3 TISA workload."},
        },
        "artifact": {
            "tisa_v1_sha256": machine_digest,
            "bytes": len(lowered.machine_code),
            "instruction_count": len(lowered.program.instructions),
            "emulator_attempts": emulator_result[2],
            "emulator_terminal_status": emulator_result[0],
        },
        "limitations": [
            "One deterministic arithmetic fixture; this is not a general workload suite.",
            "Wall time is local characterization and is sensitive to host load, Python/runtime versions, and filesystem state.",
            "Compile-plus-execute measurements intentionally include the named phases and must not be compared as execution-only timings.",
            "No native, WASM/WASI, or RTL runtime measurement is made by this report.",
        ],
    }
    report["report_sha256"] = canonical_sha256(report)
    return report


def write_report(path: Path, report: dict[str, Any]) -> None:
    destination = path.resolve()
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite benchmark evidence: {destination}")
    unsigned = dict(report)
    claimed_hash = unsigned.pop("report_sha256", None)
    if claimed_hash != canonical_sha256(unsigned):
        raise ValueError("benchmark report self-hash is invalid")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compiler-root", type=Path, required=True)
    parser.add_argument("--cpu-v3-root", type=Path, required=True)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--warmups", type=int, default=3)
    parser.add_argument("--repetitions", type=int, default=30)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report = run_benchmark(
            compiler_root=args.compiler_root, cpu_root=args.cpu_v3_root,
            source_path=args.source, warmups=args.warmups, repetitions=args.repetitions,
        )
        write_report(args.report, report)
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError) as error:
        print(f"benchmark rejected: {error}", file=sys.stderr)
        return 2
    print(json.dumps({
        "status": report["status"], "report": str(args.report.resolve()),
        "report_sha256": report["report_sha256"],
        "workload": report["workload"]["id"],
        "instruction_count": report["artifact"]["instruction_count"],
        "emulator_attempts": report["artifact"]["emulator_attempts"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
