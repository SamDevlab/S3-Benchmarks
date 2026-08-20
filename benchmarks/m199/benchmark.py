"""Correctness-first hosted characterization for M1.99 native self-moves."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import statistics
import subprocess
import sys
import textwrap
import time


_COMMIT_RE = re.compile(r"[0-9a-f]{40}")
WARMUPS = 5
REPETITIONS = 30
LOOPS = 25


def _git(root: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"git command failed for {root}: {' '.join(args)}") from error
    return result.stdout.strip()


def _git_head(root: Path, label: str) -> str:
    head = _git(root, "rev-parse", "--verify", "HEAD")
    if _COMMIT_RE.fullmatch(head) is None:
        raise SystemExit(f"{label} Git HEAD is not a full commit SHA")
    return head


def _require_pinned_head(root: Path, label: str, expected: str) -> str:
    if _COMMIT_RE.fullmatch(expected) is None:
        raise SystemExit(f"{label} evidence SHA must be a full commit SHA")
    actual = _git_head(root, label)
    if actual != expected:
        raise SystemExit(f"{label} HEAD mismatch: expected {expected}, got {actual}")
    return actual


def _s3_root() -> Path:
    value = os.environ.get("S3_REPO", "")
    if not value:
        raise SystemExit("S3_REPO must point to the tested S3 checkout")
    root = Path(value).resolve()
    if not (root / "bootstrap" / "s3").is_dir():
        raise SystemExit(f"S3_REPO is not an S3 checkout: {root}")
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    return root


def _fixture(*, include_self_moves: bool):
    from bootstrap.s3.assembly import parse_assembly

    moves = "    TMOV r0, r0\n" if include_self_moves else ""
    branch_move = "    TMOV r3, r3\n" if include_self_moves else ""
    source = textwrap.dedent(
        f"""\
        .function helper -> i64
            .param r0, i64
            .register r1, i64
        .label entry
            TADD r1, r0, r0
            TRET r1
        .end

        .function main -> i64
            .register r0, i64
            .register r1, i64
            .register r2, i64
            .register r3, i64
            .register r4, trit
            .memory m0, i64, 2, mutable
        .label entry
            TCONST r0, 7
        {moves}            TCONST r1, 0
            TSTORE m0, r1, r0
            TLOAD r2, m0, r1
            TCALL r3, helper, r2
            TCONST r4, -1
            TBR3 r4, negative, neutral, positive
        .label negative
        {branch_move}            TRET r3
        .label neutral
            TCONST r0, 0
            TRET r0
        .label positive
            TCONST r0, 1
            TRET r0
        .end
        """
    )
    return parse_assembly(source)


def _initialized_self_move():
    from bootstrap.s3.assembly import parse_assembly

    return parse_assembly(
        ".function main -> i64\n"
        "    .register r0, i64\n"
        ".label entry\n"
        "    TCONST r0, 7\n"
        "    TMOV r0, r0\n"
        "    TRET r0\n"
        ".end\n"
    )


def _uninitialized_self_move():
    from bootstrap.s3.assembly import parse_assembly

    return parse_assembly(
        ".function main -> i64\n"
        "    .register r0, i64\n"
        ".label entry\n"
        "    TMOV r0, r0\n"
        "    TCONST r0, 7\n"
        "    TRET r0\n"
        ".end\n"
    )


def _instruction_limit_boundary():
    return _initialized_self_move()


def _optimized(program):
    from bootstrap.s3.codegen_optimization import analyze_redundant_noop_moves

    return analyze_redundant_noop_moves(program)


def _execute(program, *, max_instructions: int = 100_000):
    from bootstrap.s3.emulator import Emulator

    return Emulator(max_frames=64, max_instructions=max_instructions).execute(program, entry="main")


def _native_text(program) -> str:
    from bootstrap.s3.backends.x86_64 import X8664Backend

    return X8664Backend().generate(program)


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _summary(samples: list[int]) -> dict[str, object]:
    quartiles = statistics.quantiles(samples, n=4, method="inclusive")
    return {
        "median_ns": statistics.median(samples),
        "min_ns": min(samples),
        "max_ns": max(samples),
        "q1_ns": quartiles[0],
        "q3_ns": quartiles[2],
        "iqr_ns": quartiles[2] - quartiles[0],
        "raw_samples_ns": samples,
    }


def _time_interleaved(off, on) -> dict[str, object]:
    for _ in range(WARMUPS):
        for program in (off, on):
            for _ in range(LOOPS):
                _execute(program)

    samples = {"off": [], "on": []}
    for repetition in range(REPETITIONS):
        order = (("off", off), ("on", on)) if repetition % 2 == 0 else (("on", on), ("off", off))
        for label, program in order:
            started = time.perf_counter_ns()
            for _ in range(LOOPS):
                _execute(program)
            samples[label].append(time.perf_counter_ns() - started)
    return {
        "warmups": WARMUPS,
        "repetitions": REPETITIONS,
        "loops_per_sample": LOOPS,
        "order": "deterministic alternating OFF/ON, ON/OFF",
        "off": _summary(samples["off"]),
        "on": _summary(samples["on"]),
    }


def _expect_failure(program, *, max_instructions: int | None = None, message: str) -> str:
    from bootstrap.s3.assembly_verifier import AssemblyVerifierError

    try:
        if max_instructions is None:
            _execute(program)
        else:
            _execute(program, max_instructions=max_instructions)
    except AssemblyVerifierError as error:
        observed = str(error)
        if message not in observed:
            raise SystemExit(f"unexpected failure: {observed}") from error
        return observed
    raise SystemExit(f"expected failure containing {message!r}")


def _correctness() -> tuple[dict[str, object], dict[str, object]]:
    from bootstrap.s3.assembly_verifier import AssemblyVerifier

    cases: list[dict[str, object]] = []
    workload = _fixture(include_self_moves=True)
    candidate, report = _optimized(workload)
    AssemblyVerifier().validate(workload, entry="main")
    AssemblyVerifier().validate(candidate, entry="main")
    off_result = _execute(workload)
    on_result = _execute(candidate)
    if off_result != on_result:
        raise SystemExit(f"workload mismatch: {off_result} != {on_result}")
    cases.append(
        {
            "case": "initialized_self_move_and_workload",
            "status": "PASS",
            "result_off": off_result,
            "result_on": on_result,
            "assembly_identity_preserved": candidate is workload,
            "input_instructions": report.input_instruction_count,
            "output_instructions": report.output_instruction_count,
            "candidate_self_moves": report.candidate_noop_moves,
        }
    )

    uninitialized = _uninitialized_self_move()
    candidate, report = _optimized(uninitialized)
    off_error = _expect_failure(uninitialized, message="uninitialized register r0")
    on_error = _expect_failure(candidate, message="uninitialized register r0")
    cases.append(
        {
            "case": "uninitialized_self_move",
            "status": "PASS",
            "failure_off": off_error,
            "failure_on": on_error,
            "assembly_identity_preserved": candidate is uninitialized,
            "input_instructions": report.input_instruction_count,
            "output_instructions": report.output_instruction_count,
        }
    )

    limited = _instruction_limit_boundary()
    candidate, report = _optimized(limited)
    off_error = _expect_failure(limited, max_instructions=2, message="instruction limit 2 exceeded")
    on_error = _expect_failure(candidate, max_instructions=2, message="instruction limit 2 exceeded")
    cases.append(
        {
            "case": "instruction_limit_boundary",
            "status": "PASS",
            "failure_off": off_error,
            "failure_on": on_error,
            "assembly_identity_preserved": candidate is limited,
            "input_instructions": report.input_instruction_count,
            "output_instructions": report.output_instruction_count,
        }
    )

    native = _native_text(_initialized_self_move())
    logical_sites = native.count("inc qword ptr [rip + __s3_instruction_count]")
    native_probe = {
        "sha256": _digest(native),
        "bytes": len(native.encode("utf-8")),
        "logical_instruction_sites": logical_sites,
        "physical_self_copy_elided": logical_sites == 3,
        "execution": "DEFERRED_BY_ENVIRONMENT",
    }
    if logical_sites != 3:
        raise SystemExit(f"unexpected native logical instruction count: {logical_sites}")
    return {"status": "PASS", "cases": cases}, native_probe


def _baseline_sha(s3_root: Path) -> tuple[str, str]:
    introducing = _git(
        s3_root,
        "log",
        "--format=%H",
        "--diff-filter=A",
        "--",
        "bootstrap/s3/codegen_optimization.py",
    ).splitlines()
    if len(introducing) != 1 or _COMMIT_RE.fullmatch(introducing[0]) is None:
        raise SystemExit("unable to identify a unique M1.99 optimizer introduction commit")
    optimization_sha = introducing[0]
    baseline = _git(s3_root, "rev-parse", "--verify", f"{optimization_sha}^")
    if _COMMIT_RE.fullmatch(baseline) is None:
        raise SystemExit("M1.99 baseline is not a full commit SHA")
    return baseline, optimization_sha


def main() -> int:
    s3_root = _s3_root()
    benchmark_root = Path(__file__).resolve().parents[2]
    source_sha = os.environ.get("S3_COMMIT", "")
    benchmark_sha = os.environ.get("BENCHMARK_REPO_COMMIT", "")
    resolved_source_sha = _require_pinned_head(s3_root, "S3_REPO", source_sha)
    resolved_benchmark_sha = _require_pinned_head(benchmark_root, "benchmark repository", benchmark_sha)
    baseline_sha, optimization_sha = _baseline_sha(s3_root)

    correctness, native_probe = _correctness()
    workload = _fixture(include_self_moves=True)
    candidate, _ = _optimized(workload)
    no_move_workload = _fixture(include_self_moves=False)
    no_move_candidate, _ = _optimized(no_move_workload)
    timing = {
        "with_self_moves": _time_interleaved(workload, candidate),
        "without_self_moves": _time_interleaved(no_move_workload, no_move_candidate),
    }

    native_available = (
        platform.system() == "Linux"
        and platform.machine().lower() in {"x86_64", "amd64"}
        and shutil.which("cc") is not None
    )
    payload = {
        "schema": "s3.m199.self-move.v2",
        "milestone": "M1.99",
        "name": "native-self-move-lowering-characterization",
        "baseline_s3_sha": baseline_sha,
        "candidate_s3_sha": resolved_source_sha,
        "benchmark_repo_sha": resolved_benchmark_sha,
        "m199_optimization_introduction_sha": optimization_sha,
        "platform": platform.platform(),
        "architecture": platform.machine(),
        "toolchain": {"python": sys.version.split()[0], "cc": shutil.which("cc")},
        "correctness_gate": correctness,
        "native_execution_available": native_available,
        "native_comparative_valid": False,
        "timing_class": "CHARACTERIZATION_ONLY",
        "native_speedup_claim": "NO",
        "control": {
            "same_parsed_assembly_program": True,
            "off": "original AssemblyProgram",
            "on": "eliminate_redundant_noop_moves(original)",
            "timing": "hosted Emulator",
            "native_x86_generation": "supplementary structural probe only",
            "native_speedup_claim": "none",
        },
        "native_probe": native_probe,
        "timing": timing,
        "provenance_check": "PASS",
        "status": "PASS_CHARACTERIZATION_ONLY",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
