"""Minimize an S3 source while preserving an externally defined failure predicate.

The minimizer is deliberately compiler-agnostic. A predicate command is supplied
as a JSON argv array and receives the temporary candidate path through the
`{input}` placeholder. No shell is used. Invalid reductions simply fail the
predicate and are discarded.
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import tempfile
from pathlib import Path
from typing import Callable


class MinimizationError(ValueError):
    pass


def minimize_lines(
    source: str,
    predicate: Callable[[str], bool],
    *,
    max_runs: int = 200,
) -> tuple[str, dict[str, int | str]]:
    if max_runs < 1:
        raise MinimizationError("max_runs must be positive")
    runs = 1
    if not predicate(source):
        raise MinimizationError("original source does not satisfy failure predicate")

    lines = source.splitlines(keepends=True)
    if not lines:
        return source, {"status": "UNCHANGED", "predicate_runs": runs, "original_lines": 0, "minimized_lines": 0}

    original_count = len(lines)
    granularity = 2
    while len(lines) > 1 and runs < max_runs:
        chunk_size = max(1, math.ceil(len(lines) / granularity))
        reduced = False
        start = 0
        while start < len(lines) and runs < max_runs:
            candidate_lines = lines[:start] + lines[start + chunk_size :]
            start += chunk_size
            if not candidate_lines:
                continue
            candidate = "".join(candidate_lines)
            runs += 1
            if predicate(candidate):
                lines = candidate_lines
                granularity = max(2, granularity - 1)
                reduced = True
                break
        if reduced:
            continue
        if granularity >= len(lines):
            break
        granularity = min(len(lines), granularity * 2)

    minimized = "".join(lines)
    return minimized, {
        "status": "MINIMIZED" if len(lines) < original_count else "UNCHANGED",
        "predicate_runs": runs,
        "original_lines": original_count,
        "minimized_lines": len(lines),
    }


def _load_command(path: Path) -> list[str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or not value or not all(isinstance(item, str) for item in value):
        raise MinimizationError("predicate command JSON must be a non-empty string array")
    if not any("{input}" in item for item in value):
        raise MinimizationError("predicate command must contain {input} placeholder")
    return value


def _command_predicate(
    command: list[str],
    *,
    interesting_exit_code: int,
    timeout_seconds: float,
) -> Callable[[str], bool]:
    def predicate(candidate: str) -> bool:
        with tempfile.TemporaryDirectory(prefix="s3-min-") as directory:
            path = Path(directory) / "candidate.s3"
            path.write_text(candidate, encoding="utf-8", newline="\n")
            argv = [item.replace("{input}", str(path)) for item in command]
            try:
                completed = subprocess.run(
                    argv,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=timeout_seconds,
                    check=False,
                )
            except subprocess.TimeoutExpired:
                return False
            return completed.returncode == interesting_exit_code

    return predicate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--predicate-command-json", type=Path, required=True)
    parser.add_argument("--interesting-exit-code", type=int, default=0)
    parser.add_argument("--timeout-seconds", type=float, default=30.0)
    parser.add_argument("--max-runs", type=int, default=200)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    try:
        source = args.source.read_text(encoding="utf-8")
        command = _load_command(args.predicate_command_json)
        predicate = _command_predicate(
            command,
            interesting_exit_code=args.interesting_exit_code,
            timeout_seconds=args.timeout_seconds,
        )
        minimized, report = minimize_lines(source, predicate, max_runs=args.max_runs)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.exit(2, f"S3_MINIMIZE_ERROR={error}\n")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(minimized, encoding="utf-8", newline="\n")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"STATUS={report['status']}")
    print(f"ORIGINAL_LINES={report['original_lines']}")
    print(f"MINIMIZED_LINES={report['minimized_lines']}")
    print(f"PREDICATE_RUNS={report['predicate_runs']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
