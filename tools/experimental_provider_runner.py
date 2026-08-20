#!/usr/bin/env python3
"""Non-normative external-provider runner for S3-Benchmarks experiments."""

from __future__ import annotations

import argparse
import json
import os
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPOSITORY_ROOT / "benchmarks" / "experimental_provider" / "manifest.json"
DEFAULT_PROVIDER = (
    REPOSITORY_ROOT
    / "benchmarks"
    / "experimental_provider"
    / "providers"
    / "reference_provider.py"
)
PROVIDER_ENV = "S3BENCH_EXPERIMENTAL_PROVIDER"
MAX_CAPTURE_BYTES = 1_048_576


class RunnerError(RuntimeError):
    pass


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run non-normative S3 external-provider experiments."
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--provider", type=Path)
    parser.add_argument("--benchmark", action="append")
    parser.add_argument("--include-disabled", action="store_true")
    parser.add_argument("--list", action="store_true")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--verify-only", action="store_true")
    mode.add_argument("--smoke", action="store_true")
    mode.add_argument("--full", action="store_true")
    parser.add_argument("--loops", type=int)
    parser.add_argument("--samples", type=int)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--output-json", type=Path)
    return parser


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RunnerError(f"could not read manifest: {error}") from error
    if document.get("manifest_version") != "0.1.0":
        raise RunnerError("unsupported experimental manifest version")
    if document.get("normative") is not False:
        raise RunnerError("experimental manifest must explicitly set normative=false")
    workloads = document.get("workloads")
    if not isinstance(workloads, list) or not workloads:
        raise RunnerError("manifest workloads must be a non-empty list")
    seen: set[str] = set()
    for workload in workloads:
        if not isinstance(workload, dict):
            raise RunnerError("workloads must be objects")
        benchmark_id = workload.get("benchmark_id")
        if not isinstance(benchmark_id, str) or not benchmark_id:
            raise RunnerError("benchmark_id must be a non-empty string")
        if benchmark_id in seen:
            raise RunnerError(f"duplicate benchmark_id: {benchmark_id}")
        seen.add(benchmark_id)
        expected = workload.get("expected_checksum")
        if not isinstance(expected, str) or not expected:
            raise RunnerError(f"{benchmark_id}: expected_checksum is required")
        input_data = workload.get("input")
        if not isinstance(input_data, dict):
            raise RunnerError(f"{benchmark_id}: input must be an object")
        if not isinstance(input_data.get("id"), str) or not input_data["id"]:
            raise RunnerError(f"{benchmark_id}: input.id is required")
        work_units = input_data.get("work_units_per_loop")
        if not isinstance(work_units, int) or work_units <= 0:
            raise RunnerError(f"{benchmark_id}: work_units_per_loop must be positive")
        default_loops = workload.get("default_loops")
        if not isinstance(default_loops, int) or default_loops <= 0:
            raise RunnerError(f"{benchmark_id}: default_loops must be positive")
    return document


def select_workloads(
    document: dict[str, Any],
    requested: list[str] | None,
    include_disabled: bool,
) -> list[dict[str, Any]]:
    wanted = set(requested or [])
    selected = []
    for workload in document["workloads"]:
        if wanted and workload["benchmark_id"] not in wanted:
            continue
        if not include_disabled and not workload.get("enabled_by_default", False):
            continue
        selected.append(workload)
    if wanted:
        found = {item["benchmark_id"] for item in selected}
        missing = wanted - found
        if missing and not include_disabled:
            raise RunnerError(
                "requested benchmark is disabled; pass --include-disabled: "
                + ", ".join(sorted(missing))
            )
        if missing:
            raise RunnerError("unknown benchmark(s): " + ", ".join(sorted(missing)))
    return selected


def resolve_provider(explicit: Path | None) -> Path:
    if explicit is not None:
        candidate = explicit
    elif os.environ.get(PROVIDER_ENV):
        candidate = Path(os.environ[PROVIDER_ENV])
    else:
        candidate = DEFAULT_PROVIDER
    candidate = candidate.expanduser().resolve()
    if not candidate.is_file():
        raise RunnerError(f"provider does not exist: {candidate}")
    return candidate


def provider_command(provider: Path) -> list[str]:
    if provider.suffix.lower() == ".py":
        return [sys.executable, os.fspath(provider)]
    return [os.fspath(provider)]


def parse_provider_output(stdout: str) -> tuple[str, int | None, str | None]:
    checksum_lines = [
        line.split("=", 1)[1].strip()
        for line in stdout.splitlines()
        if line.startswith("checksum=")
    ]
    if len(checksum_lines) != 1 or not checksum_lines[0]:
        raise RunnerError("provider must emit exactly one checksum=<value> line")
    kernel_ns = None
    provider_role = None
    for line in stdout.splitlines():
        if line.startswith("kernel_ns="):
            if kernel_ns is not None:
                raise RunnerError("provider emitted kernel_ns more than once")
            try:
                kernel_ns = int(line.split("=", 1)[1].strip())
            except ValueError as error:
                raise RunnerError("kernel_ns must be an integer") from error
            if kernel_ns < 0:
                raise RunnerError("kernel_ns must be non-negative")
        elif line.startswith("provider_role="):
            provider_role = line.split("=", 1)[1].strip() or None
    return checksum_lines[0], kernel_ns, provider_role


def invoke(
    provider: Path,
    workload: dict[str, Any],
    loops: int,
    timeout: float,
) -> dict[str, Any]:
    args = [
        *provider_command(provider),
        "--benchmark-id",
        workload["benchmark_id"],
        "--input-id",
        workload["input"]["id"],
        "--loops",
        str(loops),
    ]
    started = time.perf_counter_ns()
    try:
        completed = subprocess.run(
            args,
            cwd=REPOSITORY_ROOT,
            capture_output=True,
            text=True,
            shell=False,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        raise RunnerError(f"{workload['benchmark_id']}: provider timed out") from error
    process_ns = time.perf_counter_ns() - started
    stdout_bytes = completed.stdout.encode("utf-8", errors="replace")
    stderr_bytes = completed.stderr.encode("utf-8", errors="replace")
    if len(stdout_bytes) > MAX_CAPTURE_BYTES or len(stderr_bytes) > MAX_CAPTURE_BYTES:
        raise RunnerError(f"{workload['benchmark_id']}: provider output exceeded limit")
    if completed.returncode != 0:
        details = completed.stderr.strip() or completed.stdout.strip()
        raise RunnerError(
            f"{workload['benchmark_id']}: provider exited {completed.returncode}: {details}"
        )
    checksum, kernel_ns, provider_role = parse_provider_output(completed.stdout)
    expected = workload["expected_checksum"]
    if checksum != expected:
        raise RunnerError(
            f"{workload['benchmark_id']}: checksum mismatch: expected {expected}, got {checksum}"
        )
    work_units = workload["input"]["work_units_per_loop"] * loops
    timing_ns = kernel_ns if kernel_ns is not None else process_ns
    throughput = None
    if timing_ns > 0:
        throughput = work_units / (timing_ns / 1_000_000_000)
    return {
        "checksum": checksum,
        "kernel_ns": kernel_ns,
        "process_ns": process_ns,
        "provider_role": provider_role,
        "work_units": work_units,
        "throughput_per_second": throughput,
    }


def summarize(samples: list[dict[str, Any]]) -> dict[str, Any]:
    process = [sample["process_ns"] for sample in samples]
    kernel = [sample["kernel_ns"] for sample in samples if sample["kernel_ns"] is not None]
    throughput = [
        sample["throughput_per_second"]
        for sample in samples
        if sample["throughput_per_second"] is not None
    ]
    result: dict[str, Any] = {
        "sample_count": len(samples),
        "process_median_ns": statistics.median(process),
        "process_min_ns": min(process),
        "process_max_ns": max(process),
        "kernel_median_ns": statistics.median(kernel) if len(kernel) == len(samples) else None,
        "throughput_median_per_second": statistics.median(throughput) if throughput else None,
    }
    return result


def run_workload(
    provider: Path,
    workload: dict[str, Any],
    *,
    mode: str,
    loops_override: int | None,
    samples_override: int | None,
    timeout: float,
) -> dict[str, Any]:
    if mode == "verify":
        loops, warmups, sample_count = 1, 0, 1
    elif mode == "smoke":
        loops = min(workload["default_loops"], 100)
        warmups, sample_count = 1, 3
    else:
        loops = workload["default_loops"]
        warmups, sample_count = 3, 10

    if loops_override is not None:
        if loops_override <= 0:
            raise RunnerError("--loops must be positive")
        loops = loops_override
    if samples_override is not None:
        if samples_override <= 0:
            raise RunnerError("--samples must be positive")
        sample_count = samples_override

    for _ in range(warmups):
        invoke(provider, workload, loops, timeout)
    samples = [invoke(provider, workload, loops, timeout) for _ in range(sample_count)]
    return {
        "benchmark_id": workload["benchmark_id"],
        "category": workload["category"],
        "input_id": workload["input"]["id"],
        "enabled_by_default": workload.get("enabled_by_default", False),
        "loops_per_sample": loops,
        "expected_checksum": workload["expected_checksum"],
        "summary": summarize(samples),
        "samples": samples,
    }


def main(argv: list[str] | None = None) -> int:
    args = create_parser().parse_args(argv)
    if args.timeout <= 0:
        raise SystemExit("--timeout must be positive")
    try:
        document = load_manifest(args.manifest.resolve())
        selected = select_workloads(document, args.benchmark, args.include_disabled)
        if args.list:
            print(
                json.dumps(
                    [
                        {
                            "benchmark_id": item["benchmark_id"],
                            "category": item["category"],
                            "enabled_by_default": item.get("enabled_by_default", False),
                        }
                        for item in document["workloads"]
                    ],
                    indent=2,
                    sort_keys=True,
                )
            )
            return 0
        if not selected:
            raise RunnerError("no workloads selected")

        provider = resolve_provider(args.provider)
        mode = "verify" if args.verify_only else "smoke" if args.smoke else "full"
        results = [
            run_workload(
                provider,
                workload,
                mode=mode,
                loops_override=args.loops,
                samples_override=args.samples,
                timeout=args.timeout,
            )
            for workload in selected
        ]
        output = {
            "protocol_version": "0.1.0",
            "normative": False,
            "provider": os.fspath(provider),
            "provider_source": (
                "explicit"
                if args.provider is not None
                else "environment"
                if os.environ.get(PROVIDER_ENV)
                else "bundled-protocol-fixture"
            ),
            "mode": mode,
            "results": results,
        }
        payload = json.dumps(output, indent=2, sort_keys=True, allow_nan=False) + "\n"
        if args.output_json:
            args.output_json.parent.mkdir(parents=True, exist_ok=True)
            args.output_json.write_text(payload, encoding="utf-8", newline="\n")
        print(payload, end="")
        return 0
    except RunnerError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
