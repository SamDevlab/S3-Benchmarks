"""Correctness-first local characterization for M1.99 native self-move removal."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import platform
import statistics
import sys
import time
import textwrap


def _s3_root() -> Path:
    value = os.environ.get("S3_REPO", "")
    if not value:
        raise RuntimeError("S3_REPO must point to the tested S3 checkout")
    root = Path(value).resolve()
    if not (root / "bootstrap" / "s3").is_dir():
        raise RuntimeError(f"S3_REPO is not an S3 checkout: {root}")
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


def _native_probe_fixture():
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


def _optimized(program):
    from bootstrap.s3.codegen_optimization import eliminate_redundant_noop_moves

    return eliminate_redundant_noop_moves(program)


def _native_text_with_optimization(program) -> str:
    from bootstrap.s3.backends.x86_64 import X8664Backend

    return X8664Backend().generate(program)


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _execute(program) -> int:
    from bootstrap.s3.emulator import Emulator

    return Emulator(max_frames=64, max_instructions=100_000).execute(program, entry="main")


def _time_variant(program, *, warmups: int, repetitions: int, loops: int) -> list[int]:
    for _ in range(warmups):
        for _ in range(loops):
            _execute(program)
    samples: list[int] = []
    for _ in range(repetitions):
        started = time.perf_counter_ns()
        for _ in range(loops):
            _execute(program)
        samples.append(time.perf_counter_ns() - started)
    return samples


def main() -> int:
    _s3_root()
    source_sha = os.environ.get("S3_COMMIT")
    benchmark_sha = os.environ.get("BENCHMARK_REPO_COMMIT")
    if not source_sha or not benchmark_sha:
        raise SystemExit("S3_COMMIT and BENCHMARK_REPO_COMMIT are required evidence inputs")
    warmups = 2
    repetitions = 7
    loops = 25
    correctness_cases = []
    timing = {}
    native_artifacts = {}
    for include_self_moves in (True, False):
        label = "with_self_moves" if include_self_moves else "without_self_moves"
        program = _fixture(include_self_moves=include_self_moves)
        optimized, report = _optimized(program)
        from bootstrap.s3.assembly_verifier import AssemblyVerifier

        AssemblyVerifier().validate(program, entry="main")
        AssemblyVerifier().validate(optimized, entry="main")
        before = _execute(program)
        after = _execute(optimized)
        if before != after:
            raise SystemExit(f"correctness mismatch for {label}: {before} != {after}")
        native_artifacts[label] = {
            "assembly_off_sha256": _digest(program.render()),
            "assembly_on_sha256": _digest(optimized.render()),
            "assembly_off_instructions": report.input_instruction_count,
            "assembly_on_instructions": report.output_instruction_count,
        }
        correctness_cases.append(
            {
                "case": label,
                "result_before": before,
                "result_after": after,
                "equivalent": before == after,
                "input_instructions": report.input_instruction_count,
                "output_instructions": report.output_instruction_count,
                "removed_self_moves": report.removed_noop_moves,
            }
        )
        off_samples = _time_variant(program, warmups=warmups, repetitions=repetitions, loops=loops)
        on_samples = _time_variant(optimized, warmups=warmups, repetitions=repetitions, loops=loops)
        timing[label] = {
            "loops_per_sample": loops,
            "off_ns": off_samples,
            "on_ns": on_samples,
            "off_median_ns": statistics.median(off_samples),
            "on_median_ns": statistics.median(on_samples),
        }
    native_probe = _native_probe_fixture()
    native_on = _native_text_with_optimization(native_probe)
    native_artifacts["native_probe"] = {
        "on_sha256": _digest(native_on),
        "on_bytes": len(native_on.encode("utf-8")),
        "off": "NOT_EMITTED; raw self-move is outside the backend emitter precondition",
        "execution": "DEFERRED_BY_ENVIRONMENT",
    }
    payload = {
        "schema": "s3.m199.self-move.v1",
        "status": "PASS_CHARACTERIZATION_ONLY",
        "s3_commit": source_sha,
        "benchmark_repo_commit": benchmark_sha,
        "environment": {
            "os": platform.platform(),
            "architecture": platform.machine(),
            "python": sys.version.split()[0],
            "native_execution": "DEFERRED_BY_ENVIRONMENT",
            "native_reason": "Linux x86-64 toolchain is unavailable on Windows host",
        },
        "protocol": {
            "warmups": warmups,
            "repetitions": repetitions,
            "loops_per_sample": loops,
            "timed_scope": "hosted Assembly emulator execution",
            "control": "same AssemblyProgram and x86-64 emitter with register allocation disabled; only eliminate_redundant_noop_moves toggled",
        },
        "correctness": {
            "status": "PASS",
            "all_cases_equivalent": all(item["equivalent"] for item in correctness_cases),
            "cases": correctness_cases,
        },
        "native_artifacts": native_artifacts,
        "timing": timing,
        "timing_class": "CHARACTERIZATION_ONLY",
        "claim": "Hosted emulator characterization only; no native speedup claim is made.",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
