"""Automation-safe correctness and performance orchestration for RC1.

The runner keeps correctness and performance as separate gates.  A correctness
run may proceed on a noisy host; native timing is started only after the small
immutable C control preflight has classified the host as stable or marginal.
Every invocation owns a fresh run directory and writes raw observations before
deriving summaries, so a scheduled invocation can be inspected without relying
on process output or mutable aggregate reports.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shlex
import shutil
import statistics
import subprocess
import sys
import time
import uuid
from typing import Any, Iterable

BASE_DIR = Path(__file__).resolve().parents[2]
RC1_SHA = "9b39c7070d7bfa23d709c2128eb0b0bbef164177"
RC1_TAG = "v1.0.0-rc1"
STABLE_THRESHOLD_PERCENT = 3.0
MARGINAL_THRESHOLD_PERCENT = 5.0
MIN_EFFECT_PERCENT = 3.0

EXIT_OK = 0
EXIT_CORRECTNESS = 20
EXIT_REGRESSION = 21
EXIT_INFRASTRUCTURE = 22
EXIT_PROVENANCE = 23
EXIT_ENVIRONMENT = 24

MODES = frozenset({"fast", "nightly", "weekly", "performance", "correctness-only", "preflight-only"})

CONTROL_SOURCE = r"""#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    long iterations = 50000;
    if (argc == 3 && argv[1][0] == '-' && argv[1][1] == 'i') {
        iterations = atol(argv[2]);
    }
    if (iterations < 1) iterations = 1;
    uint64_t value = 0x9e3779b97f4a7c15ULL;
    for (long i = 0; i < iterations; ++i) {
        value ^= value << 7;
        value ^= value >> 9;
        value += (uint64_t)i * 0x100000001b3ULL;
    }
    printf("%llu\n", (unsigned long long)value);
    return 0;
}
"""


class AutomationError(RuntimeError):
    """A fail-closed automation error with a stable process exit code."""

    def __init__(self, message: str, exit_code: int = EXIT_INFRASTRUCTURE) -> None:
        super().__init__(message)
        self.exit_code = exit_code


class ProvenanceError(AutomationError):
    def __init__(self, message: str) -> None:
        super().__init__(message, EXIT_PROVENANCE)


@dataclass(frozen=True, slots=True)
class CommandResult:
    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str
    elapsed_ns: int


@dataclass(frozen=True, slots=True)
class RunContext:
    run_id: str
    root: Path
    started: str
    benchmark_sha: str
    s3_sha: str


@dataclass(frozen=True, slots=True)
class SSHTransport:
    """Safe command-line description for an externally staged Linux host."""

    host: str
    port: int = 22
    user: str | None = None

    @property
    def target(self) -> str:
        return f"{self.user}@{self.host}" if self.user else self.host

    def command(self, argv: Iterable[str], *, cwd: str | None = None) -> list[str]:
        remote = shlex.join(list(argv))
        if cwd:
            remote = f"cd -- {shlex.quote(cwd)} && {remote}"
        return ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10", "-p", str(self.port), self.target, remote]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    if not path.is_file():
        raise AutomationError(f"missing required file: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def _write_once(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
    except FileExistsError as error:
        raise AutomationError(f"refusing to overwrite run evidence: {path}") from error


def _write_text_once(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(value)
    except FileExistsError as error:
        raise AutomationError(f"refusing to overwrite run evidence: {path}") from error


def _generated_run_id() -> str:
    return datetime.now(timezone.utc).strftime("run-%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex[:12]


def _git(repo: Path, *args: str) -> str:
    try:
        result = subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True)
    except (OSError, subprocess.CalledProcessError) as error:
        raise ProvenanceError(f"unable to resolve Git state for {repo}: {' '.join(args)}") from error
    value = result.stdout.strip()
    if not value:
        raise ProvenanceError(f"Git returned an empty value for {repo}: {' '.join(args)}")
    return value


def resolve_provenance(*, s3_repo: Path, requested_s3_sha: str, benchmark_repo: Path, requested_benchmark_sha: str, require_rc1_tag: bool = True) -> dict[str, str]:
    """Require exact repository HEADs and an immutable RC1 tag target."""

    actual_s3 = _git(s3_repo, "rev-parse", "--verify", "HEAD")
    actual_benchmark = _git(benchmark_repo, "rev-parse", "--verify", "HEAD")
    if actual_s3 != requested_s3_sha:
        raise ProvenanceError(f"S3 HEAD mismatch: expected {requested_s3_sha}, got {actual_s3}")
    if actual_benchmark != requested_benchmark_sha:
        raise ProvenanceError(f"benchmark HEAD mismatch: expected {requested_benchmark_sha}, got {actual_benchmark}")
    tag_target = _git(s3_repo, "rev-parse", "--verify", f"refs/tags/{RC1_TAG}^{{}}")
    if require_rc1_tag and tag_target != RC1_SHA:
        raise ProvenanceError(f"STOP_RC1_TAG_MUTATED: {RC1_TAG} targets {tag_target}, expected {RC1_SHA}")
    return {
        "benchmark_sha": actual_benchmark,
        "s3_sha": actual_s3,
        "s3_tag": RC1_TAG,
        "s3_tag_target": tag_target,
    }


def _safe_command_output(command: list[str]) -> str:
    if shutil.which(command[0]) is None:
        return "UNAVAILABLE"
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.stdout.strip() or result.stderr.strip() or "UNAVAILABLE"


def _memory_available() -> int | None:
    meminfo = Path("/proc/meminfo")
    if meminfo.is_file():
        for line in meminfo.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("MemAvailable:"):
                try:
                    return int(line.split()[1]) * 1024
                except (IndexError, ValueError):
                    return None
    return None


def _cpu_model() -> str:
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.is_file():
        for line in cpuinfo.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.lower().startswith(("model name", "hardware", "processor")) and ":" in line:
                return line.split(":", 1)[1].strip()
    return platform.processor() or "UNAVAILABLE"


def _virtualization() -> str:
    value = _safe_command_output(["systemd-detect-virt"])
    if value != "UNAVAILABLE":
        return value.splitlines()[0].strip()
    return "UNAVAILABLE"


def collect_environment() -> dict[str, Any]:
    """Collect only non-secret, stable machine properties."""

    environment = {
        "schema": "s3.rc1.automation.environment.v1",
        "os": platform.system(),
        "kernel": platform.release(),
        "architecture": platform.machine(),
        "cpu_model": _cpu_model(),
        "logical_cpus": os.cpu_count() or 1,
        "python_version": platform.python_version(),
        "gcc_version": _safe_command_output(["gcc", "--version"]).splitlines()[0],
        "clang_version": _safe_command_output(["clang", "--version"]).splitlines()[0],
        "linker_version": _safe_command_output(["ld", "--version"]).splitlines()[0],
        "virtualization": _virtualization(),
        "affinity_policy": "caller-specified",
    }
    stable = {key: environment[key] for key in environment if key != "schema"}
    environment["environment_hash"] = _sha256_bytes(_canonical_json(stable))
    environment["host_id"] = "host-" + _sha256_bytes(_canonical_json({"os": environment["os"], "kernel": environment["kernel"], "architecture": environment["architecture"], "cpu_model": environment["cpu_model"], "logical_cpus": environment["logical_cpus"], "virtualization": environment["virtualization"]}))[:16]
    return environment


def collect_environment_diagnostics() -> dict[str, Any]:
    """Capture read-only diagnostics when timing eligibility is rejected."""

    return {
        "uname": _safe_command_output(["uname", "-a"]),
        "uptime": _safe_command_output(["uptime"]),
        "load_average": list(os.getloadavg()) if hasattr(os, "getloadavg") else None,
        "available_memory_bytes": _memory_available(),
        "cpu_model": _cpu_model(),
        "logical_cpus": os.cpu_count() or 1,
        "virtualization": _virtualization(),
        "top_processes": _safe_command_output(["ps", "-eo", "pid,pcpu,pmem,comm", "--sort=-pcpu"]).splitlines()[:12],
        "benchmark_processes": _safe_command_output(["pgrep", "-af", "(automation|p1_stability|p7_p9_native|runner)"]).splitlines(),
    }


def _affinity_prefix(value: str) -> list[str]:
    return shlex.split(value) if value.strip() else []


def _run(command: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None, timeout: float | None = None) -> CommandResult:
    started = time.perf_counter_ns()
    try:
        completed = subprocess.run(command, cwd=str(cwd) if cwd else None, env=env, capture_output=True, text=True, check=False, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        elapsed = time.perf_counter_ns() - started
        return CommandResult(tuple(command), 124, error.stdout or "", error.stderr or "TIMEOUT", elapsed)
    return CommandResult(tuple(command), completed.returncode, completed.stdout, completed.stderr, time.perf_counter_ns() - started)


def classify_control_blocks(medians: Iterable[float]) -> dict[str, Any]:
    """Classify block medians using the declared 3%/5% policy."""

    values = [float(value) for value in medians]
    if not values or min(values) <= 0:
        return {"classification": "UNSTABLE", "control_drift_percent": None, "monotonic_trend": False, "performance_eligible": False}
    relative_range = (max(values) / min(values) - 1.0) * 100.0
    monotonic = len(values) >= 3 and ((values[0] < values[-1] and values[1] < values[-1]) or (values[0] > values[-1] and values[1] > values[-1]))
    if relative_range <= STABLE_THRESHOLD_PERCENT and not monotonic:
        classification = "STABLE"
    elif relative_range <= MARGINAL_THRESHOLD_PERCENT and not monotonic:
        classification = "MARGINAL"
    else:
        classification = "UNSTABLE"
    return {"classification": classification, "control_drift_percent": relative_range, "monotonic_trend": monotonic, "performance_eligible": classification in {"STABLE", "MARGINAL"}}


def _control_preflight_run(root: Path, *, run_id: str, blocks: int, samples_per_block: int, iterations: int, warmups: int, affinity: str, compiler: str | None = None) -> dict[str, Any]:
    root.mkdir(parents=True, exist_ok=False)
    compiler_path = compiler or shutil.which("gcc") or shutil.which("cc")
    if compiler_path is None:
        diagnostics = collect_environment_diagnostics()
        result = {"schema": "s3.rc1.automation.preflight.v1", "status": "UNAVAILABLE", "classification": "UNSTABLE", "performance_eligible": False, "reason": "C_COMPILER_UNAVAILABLE", "diagnostics": diagnostics, "samples": [], "blocks": []}
        _write_once(root / "preflight.json", result)
        return result
    source = root / "control.c"
    binary = root / "control"
    _write_text_once(source, CONTROL_SOURCE)
    flags = [compiler_path, "-O2", "-std=c99", str(source), "-o", str(binary)]
    compiled = _run(flags)
    if compiled.returncode != 0:
        result = {"schema": "s3.rc1.automation.preflight.v1", "status": "FAIL", "classification": "UNSTABLE", "performance_eligible": False, "reason": "CONTROL_COMPILE_FAILED", "compile": {"command": flags, "returncode": compiled.returncode, "stdout": compiled.stdout, "stderr": compiled.stderr}, "samples": [], "blocks": []}
        _write_once(root / "preflight.json", result)
        return result
    binary_sha = _sha256_file(binary)
    prefix = _affinity_prefix(affinity)
    warmup_command = prefix + [str(binary), "-i", str(iterations)]
    for _ in range(warmups):
        if _sha256_file(binary) != binary_sha:
            raise AutomationError("CONTROL_BINARY_MUTATED")
        warmup_result = subprocess.run(warmup_command, capture_output=True, text=True, check=False)
        if warmup_result.returncode != 0:
            raise AutomationError(f"control warmup failed: {warmup_result.stderr.strip()}")
    observations: list[dict[str, Any]] = []
    block_values: list[list[float]] = []
    sequence = 0
    for block in range(blocks):
        values: list[float] = []
        for sample in range(samples_per_block):
            sequence += 1
            if _sha256_file(binary) != binary_sha:
                raise AutomationError("CONTROL_BINARY_MUTATED")
            command = prefix + [str(binary), "-i", str(iterations)]
            started = time.perf_counter_ns()
            completed = subprocess.run(command, capture_output=True, text=True, check=False)
            elapsed_ns = time.perf_counter_ns() - started
            if completed.returncode != 0:
                raise AutomationError(f"control execution failed: {completed.stderr.strip()}")
            ns_per_operation = elapsed_ns / iterations
            values.append(ns_per_operation)
            observations.append({
                "schema": "s3.benchmark.sample.v1",
                "run_id": run_id,
                "timestamp_utc": _now(),
                "mode": "preflight",
                "workload": "C_CONTROL",
                "subcase": "control",
                "candidate": "C-O2",
                "candidate_sha": binary_sha,
                "variant": "O2",
                "control_role": "control",
                "block_id": block,
                "sequence_index": sequence,
                "warmup": False,
                "operations": iterations,
                "elapsed_ns": elapsed_ns,
                "ns_per_operation": ns_per_operation,
                "host_id": None,
                "environment_hash": None,
                "cpu_affinity": affinity,
                "artifact_hash": binary_sha,
                "load_average": list(os.getloadavg()) if hasattr(os, "getloadavg") else None,
                "available_memory_bytes": _memory_available(),
            })
        block_values.append(values)
    medians = [statistics.median(values) for values in block_values if values]
    classification = classify_control_blocks(medians)
    environment = collect_environment()
    for row in observations:
        row["host_id"] = environment["host_id"]
        row["environment_hash"] = environment["environment_hash"]
    result = {
        "schema": "s3.rc1.automation.preflight.v1",
        "status": "PASS",
        "classification": classification["classification"],
        "performance_eligible": classification["performance_eligible"],
        "control_drift_percent": classification["control_drift_percent"],
        "block_medians_ns_per_operation": medians,
        "monotonic_trend": classification["monotonic_trend"],
        "thresholds_percent": {"stable": STABLE_THRESHOLD_PERCENT, "marginal": MARGINAL_THRESHOLD_PERCENT, "unstable_above": MARGINAL_THRESHOLD_PERCENT},
        "control_source_sha256": _sha256_file(source),
        "control_binary_sha256": binary_sha,
        "compiler": compiler_path,
        "compiler_flags": flags[1:],
        "cpu_affinity": affinity,
        "samples": observations,
        "blocks": [{"block_id": index, "median_ns_per_operation": median, "count": len(values)} for index, (median, values) in enumerate(zip(medians, block_values))],
        "environment": environment,
    }
    _write_once(root / "preflight.json", result)
    _write_once(root / "samples.json", observations)
    return result


def _parse_roots(values: Iterable[str], s3_repo: Path | None) -> dict[str, Path]:
    roots: dict[str, Path] = {}
    for value in values:
        if "=" not in value:
            raise AutomationError(f"S3 root must use CHECKPOINT=PATH: {value}")
        key, raw = value.split("=", 1)
        if key not in {"H4", "H5"}:
            raise AutomationError(f"unsupported S3 checkpoint: {key}")
        roots[key] = Path(raw).resolve()
    if s3_repo is not None:
        roots.setdefault("H5", s3_repo.resolve())
    return roots


def _command_record(result: CommandResult, output_dir: Path, name: str) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_text_once(output_dir / f"{name}.stdout.txt", result.stdout)
    _write_text_once(output_dir / f"{name}.stderr.txt", result.stderr)
    return {"command": list(result.command), "returncode": result.returncode, "elapsed_ns": result.elapsed_ns, "stdout": f"{name}.stdout.txt", "stderr": f"{name}.stderr.txt"}


def _gate_status(record: dict[str, Any], evidence_dir: Path) -> str:
    if record["returncode"] == 0:
        return "PASS"
    stderr_path = evidence_dir / record["stderr"]
    try:
        stderr = stderr_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        stderr = ""
    if "gcc/cc unavailable" in stderr or "NativePlatformError" in stderr:
        return "NOT_RUN_PLATFORM"
    return "FAIL"


def _correctness_gate(context: RunContext, args: argparse.Namespace, roots: dict[str, Path]) -> dict[str, Any]:
    h5 = roots.get("H5")
    if h5 is None:
        return {"status": "NOT_RUN", "reason": "H5_S3_ROOT_REQUIRED", "p1": {"status": "NOT_RUN"}, "p7_p8_p9": {"status": "NOT_RUN"}}
    env = os.environ.copy()
    env["S3_REPO"] = str(h5)
    p1_command = [sys.executable, str(BASE_DIR / "tools" / "runner.py"), "--verify-only", "--s3-sha", context.s3_sha, "--benchmark-sha", context.benchmark_sha, "--artifact-root", str(context.root / "artifacts" / "p1"), "--run-id", f"{context.run_id}-p1"]
    p1 = _run(p1_command, cwd=BASE_DIR, env=env)
    p1_record = _command_record(p1, context.root / "correctness", "p1")
    p1_record["status"] = "PASS" if p1.returncode == 0 else "FAIL"
    p1_record["tests"] = "P1 differential correctness"
    p7_command = [sys.executable, str(BASE_DIR / "tools" / "p7_p9_native.py"), "--s3-root", f"H5={h5}", "--checkpoints", "H5", "--correctness-only", "--benchmark-sha", context.benchmark_sha, "--artifact-root", str(context.root / "artifacts" / "p7-p9"), "--report-root", str(context.root / "correctness" / "p7-p9"), "--run-id", f"{context.run_id}-p7-p9"]
    p7 = _run(p7_command, cwd=BASE_DIR, env=env)
    p7_record = _command_record(p7, context.root / "correctness", "p7-p9")
    p7_record["status"] = _gate_status(p7_record, context.root / "correctness")
    p7_record["tests"] = ["P7", "P8", "P9"]
    if p1.returncode != 0:
        status = "FAIL"
    elif p7_record["status"] == "NOT_RUN_PLATFORM":
        status = "NOT_RUN_PLATFORM"
    else:
        status = "PASS" if p7.returncode == 0 else "FAIL"
    return {"schema": "s3.rc1.automation.correctness.v1", "status": status, "p1": p1_record, "p7_p8_p9": p7_record, "timing_started": False}


def _timing_gate(context: RunContext, args: argparse.Namespace, roots: dict[str, Path], preflight: dict[str, Any]) -> dict[str, Any]:
    if not preflight.get("performance_eligible", False):
        return {"status": "BLOCKED_BY_ENVIRONMENT_PREFLIGHT", "executed": False, "reason": "CONTROL_DRIFT_ABOVE_5_PERCENT_OR_UNAVAILABLE"}
    if set(roots) != {"H4", "H5"}:
        return {"status": "NOT_RUN", "executed": False, "reason": "H4_AND_H5_S3_ROOTS_REQUIRED"}
    environment = os.environ.copy()
    environment["S3_REPO"] = str(roots["H5"])
    p1_command = [sys.executable, str(BASE_DIR / "tools" / "p1_stability.py"), "--s3-root", f"H4={roots['H4']}", "--s3-root", f"H5={roots['H5']}", "--checkpoints", "H4", "H5", "--benchmark-sha", context.benchmark_sha, "--artifact-root", str(context.root / "timing" / "p1"), "--control-root", str(context.root / "timing" / "control"), "--run-id", f"{context.run_id}-p1-timing", "--warmups", "1", "--repetitions", str(args.timing_repetitions), "--parses", str(args.timing_parses)]
    p1 = _run(p1_command, cwd=BASE_DIR, env=environment, timeout=args.timing_timeout)
    records = {"p1": _command_record(p1, context.root / "timing", "p1")}
    p7_command = [sys.executable, str(BASE_DIR / "tools" / "p7_p9_native.py"), "--s3-root", f"H4={roots['H4']}", "--s3-root", f"H5={roots['H5']}", "--benchmark-sha", context.benchmark_sha, "--artifact-root", str(context.root / "timing" / "p7-p9-artifacts"), "--report-root", str(context.root / "timing" / "p7-p9"), "--run-id", f"{context.run_id}-p7-p9-timing", "--warmups", "1", "--repetitions", str(args.timing_repetitions)]
    p7 = _run(p7_command, cwd=BASE_DIR, env=environment, timeout=args.timing_timeout)
    records["p7_p8_p9"] = _command_record(p7, context.root / "timing", "p7-p9")
    status = "PASS" if p1.returncode == 0 and p7.returncode == 0 else "FAIL"
    return {"status": status, "executed": True, "control_drift_percent": preflight.get("control_drift_percent"), "commands": records, "promotion": "ELIGIBLE" if status == "PASS" else "NOT_PROMOTED"}


def performance_allowed(*, correctness_status: str, preflight: dict[str, Any] | None) -> bool:
    """Return whether timing may start after both mandatory gates."""

    return correctness_status == "PASS" and bool(preflight and preflight.get("performance_eligible", False))


def classify_correctness_aggregate(status: str) -> str:
    """Keep platform capability deferment distinct from correctness failure."""

    if status == "PASS":
        return "PASS"
    if status == "NOT_RUN_PLATFORM":
        return "CORRECTNESS_PARTIAL_BY_PLATFORM"
    if status == "NOT_RUN":
        return "NOT_RUN"
    return "FAIL"


def classify_regression(*, baseline_median: float | None, candidate_median: float | None, ci95: tuple[float, float] | None, environment_status: str, correctness_status: str) -> dict[str, Any]:
    """Apply the declared effect and CI policy without inventing missing data."""

    if correctness_status == "NOT_RUN":
        return {"status": "NONE", "delta_percent": None, "reason": "CORRECTNESS_NOT_REQUESTED"}
    if correctness_status == "NOT_RUN_PLATFORM":
        return {"status": "NOT_RUN_ENVIRONMENT", "delta_percent": None}
    if correctness_status != "PASS":
        return {"status": "CORRECTNESS_FAILURE", "delta_percent": None}
    if baseline_median is None or candidate_median is None or ci95 is None:
        return {"status": "NONE", "delta_percent": None, "reason": "NO_COMPARABLE_PAIRED_TIMING"}
    if environment_status not in {"STABLE", "MARGINAL"}:
        return {"status": "INCONCLUSIVE_ENVIRONMENT", "delta_percent": None}
    delta = (candidate_median / baseline_median - 1.0) * 100.0
    low, high = ci95
    confirmed = delta >= MIN_EFFECT_PERCENT and low > 0.0
    return {"status": "CONFIRMED" if confirmed else "NONE", "delta_percent": delta, "ci95_percent": [low, high], "regression_confirmed": confirmed}


def _append_history(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")


def _run_remote_automation(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    if not args.remote_benchmark_root or not args.remote_s3_repo:
        raise AutomationError("SSH mode requires --remote-benchmark-root and --remote-s3-repo")
    transport = SSHTransport(args.ssh_host, args.ssh_port, args.ssh_user)
    benchmark_sha = args.benchmark_sha or _git(BASE_DIR, "rev-parse", "--verify", "HEAD")
    s3_sha = args.s3_sha or RC1_SHA
    run_id = args.run_id or _generated_run_id()
    remote_output = args.remote_output_dir or f"/tmp/s3-rc1-automation-{run_id}"
    remote_args = [
        "python3",
        "-m",
        "benchmarks.rc1.automation",
        "--mode",
        args.mode,
        "--s3-repo",
        args.remote_s3_repo,
        "--s3-sha",
        s3_sha,
        "--benchmark-sha",
        benchmark_sha,
        "--run-id",
        run_id,
        "--output-dir",
        remote_output,
        "--history-file",
        f"{remote_output}/history.jsonl",
        "--cpu-affinity",
        args.cpu_affinity,
        "--preflight-blocks",
        str(args.preflight_blocks),
        "--preflight-samples",
        str(args.preflight_samples),
        "--preflight-warmups",
        str(args.preflight_warmups),
        "--preflight-iterations",
        str(args.preflight_iterations),
        "--timing-repetitions",
        str(args.timing_repetitions),
        "--timing-parses",
        str(args.timing_parses),
        "--timing-timeout",
        str(args.timing_timeout),
    ]
    for value in args.remote_s3_root:
        remote_args.extend(["--s3-root", value])
    remote = _run(transport.command(remote_args, cwd=args.remote_benchmark_root), timeout=args.ssh_timeout)
    print(remote.stdout, end="")
    if remote.stderr:
        print(remote.stderr, file=sys.stderr, end="")
    local_root = args.output_dir.resolve() / run_id
    local_root.parent.mkdir(parents=True, exist_ok=True)
    copy = _run(["scp", "-P", str(args.ssh_port), "-r", f"{transport.target}:{remote_output}/{run_id}", str(local_root.parent)])
    if copy.returncode != 0:
        raise AutomationError(f"unable to archive remote automation evidence: {copy.stderr.strip()}")
    status = {"status": "PASS" if remote.returncode == 0 else "FAIL", "remote_returncode": remote.returncode, "run_id": run_id, "transport": {"host": args.ssh_host, "port": args.ssh_port, "user": args.ssh_user}, "evidence_dir": str(local_root)}
    _write_once(local_root / "remote-status.json", status)
    return remote.returncode, status


def _machine_status(context: RunContext, mode: str, correctness: dict[str, Any], preflight: dict[str, Any] | None, timing: dict[str, Any] | None, regression: dict[str, Any]) -> dict[str, Any]:
    environment_status = (preflight or {}).get("classification", "NOT_RUN")
    return {
        "run_id": context.run_id,
        "mode": mode,
        "correctness_status": correctness.get("status", "NOT_RUN"),
        "correctness_aggregate_status": classify_correctness_aggregate(correctness.get("status", "NOT_RUN")),
        "environment_status": environment_status,
        "performance_eligible": (preflight or {}).get("performance_eligible", False),
        "performance_executed": (timing or {}).get("executed", False),
        "p1": correctness.get("p1", {}).get("status", "NOT_RUN"),
        "p7": correctness.get("p7_p8_p9", {}).get("status", "NOT_RUN"),
        "p8": correctness.get("p7_p8_p9", {}).get("status", "NOT_RUN"),
        "p9": correctness.get("p7_p8_p9", {}).get("status", "NOT_RUN"),
        "regression_status": regression.get("status", "NONE"),
        "improvement_status": "NOT_RUN",
        "report_dir": str(context.root),
    }


def run_automation(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    mode = args.mode
    if mode not in MODES:
        raise AutomationError(f"unsupported automation mode: {mode}")
    if args.ssh_host:
        return _run_remote_automation(args)
    benchmark_sha = args.benchmark_sha or _git(BASE_DIR, "rev-parse", "--verify", "HEAD")
    s3_repo = args.s3_repo.resolve() if args.s3_repo else None
    s3_sha = args.s3_sha or (RC1_SHA if s3_repo is None else _git(s3_repo, "rev-parse", "--verify", "HEAD"))
    roots = _parse_roots(args.s3_root, s3_repo)
    if not roots:
        raise AutomationError("an S3 root is required via --s3-repo or --s3-root CHECKPOINT=PATH")
    primary_root = roots.get("H5") or next(iter(roots.values()))
    provenance = resolve_provenance(s3_repo=primary_root, requested_s3_sha=s3_sha, benchmark_repo=BASE_DIR, requested_benchmark_sha=benchmark_sha, require_rc1_tag=(s3_sha == RC1_SHA))
    run_id = args.run_id or _generated_run_id()
    output_dir = args.output_dir.resolve()
    run_root = output_dir / run_id
    if run_root.exists():
        raise AutomationError(f"run id already exists: {run_id}")
    run_root.mkdir(parents=True)
    context = RunContext(run_id, run_root, _now(), benchmark_sha, s3_sha)
    environment = collect_environment()
    _write_once(run_root / "environment.json", environment)
    transport = SSHTransport(args.ssh_host, args.ssh_port, args.ssh_user) if args.ssh_host else None
    _write_once(run_root / "manifest.json", {"schema": "s3.rc1.automation.manifest.v1", "run_id": run_id, "mode": mode, "benchmark_sha": benchmark_sha, "s3_sha": s3_sha, "s3_tree": _git(primary_root, "rev-parse", "HEAD^{tree}"), "s3_tag": RC1_TAG if s3_sha == RC1_SHA else None, "start_time": context.started, "host_id": environment["host_id"], "environment_hash": environment["environment_hash"], "transport": {"kind": "ssh", "host": transport.host, "port": transport.port, "user": transport.user} if transport else {"kind": "local"}, "status": "RUNNING"})
    correctness = {"status": "NOT_RUN"}
    preflight: dict[str, Any] | None = None
    timing: dict[str, Any] | None = None
    if mode != "preflight-only":
        correctness = _correctness_gate(context, args, roots)
        correctness["aggregate_status"] = classify_correctness_aggregate(correctness.get("status", "NOT_RUN"))
        _write_once(run_root / "correctness.json", correctness)
    if mode in {"preflight-only", "nightly", "weekly", "performance"}:
        preflight = _control_preflight_run(run_root / "preflight", run_id=run_id, blocks=args.preflight_blocks, samples_per_block=args.preflight_samples, iterations=args.preflight_iterations, warmups=args.preflight_warmups, affinity=args.cpu_affinity)
    if mode in {"nightly", "weekly", "performance"} and performance_allowed(correctness_status=correctness.get("status", "NOT_RUN"), preflight=preflight):
        timing = _timing_gate(context, args, roots, preflight or {})
        _write_once(run_root / "timing.json", timing)
    elif mode in {"nightly", "weekly", "performance"}:
        timing = {"status": "BLOCKED_BY_GATE", "executed": False, "reason": "CORRECTNESS_OR_PREFLIGHT_GATE_NOT_PASSED"}
        _write_once(run_root / "timing.json", timing)
    if mode in {"fast", "correctness-only", "preflight-only"}:
        timing = {"status": "NOT_RUN_BY_MODE", "executed": False}
    environment_status = (preflight or {}).get("classification", "NOT_RUN")
    regression = classify_regression(baseline_median=None, candidate_median=None, ci95=None, environment_status=environment_status, correctness_status=correctness.get("status", "NOT_RUN"))
    _write_once(run_root / "regressions.json", regression)
    _write_text_once(run_root / "regressions.md", "# RC1 automation regression status\n\n" + json.dumps(regression, indent=2, sort_keys=True) + "\n")
    if timing and timing.get("executed") and timing.get("status") == "PASS":
        _append_history(args.history_file.resolve(), {"schema": "s3.rc1.automation.history.v1", "run_id": run_id, "timestamp_utc": _now(), "environment_hash": environment["environment_hash"], "s3_sha": s3_sha, "benchmark_sha": benchmark_sha, "mode": mode, "status": "PASS", "control_drift_percent": timing.get("control_drift_percent")})
    summary = {"schema": "s3.rc1.automation.summary.v1", "run_id": run_id, "mode": mode, "provenance": provenance, "environment": environment, "correctness": correctness, "preflight": preflight, "timing": timing, "regression": regression, "finished": _now()}
    _write_once(run_root / "summary.json", summary)
    machine = _machine_status(context, mode, correctness, preflight, timing, regression)
    status_code = EXIT_OK
    if correctness.get("status") == "FAIL":
        status_code = EXIT_CORRECTNESS
    elif correctness.get("status") == "NOT_RUN_PLATFORM":
        status_code = EXIT_OK
    elif regression.get("status") == "CONFIRMED":
        status_code = EXIT_REGRESSION
    elif preflight is not None and not preflight.get("performance_eligible", False) and mode in {"preflight-only", "nightly", "weekly", "performance"}:
        status_code = EXIT_ENVIRONMENT
    elif timing and timing.get("status") == "FAIL":
        status_code = EXIT_INFRASTRUCTURE
    machine["exit"] = status_code
    _write_once(run_root / "machine-status.json", machine)
    for key, value in machine.items():
        print(f"{key.upper()}={value}")
    return status_code, summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Environment-gated RC1 correctness and benchmark automation")
    parser.add_argument("--mode", choices=sorted(MODES), required=True)
    parser.add_argument("--s3-sha", default=None)
    parser.add_argument("--benchmark-sha", default=None)
    parser.add_argument("--s3-repo", type=Path, default=None)
    parser.add_argument("--s3-root", action="append", default=[], metavar="CHECKPOINT=PATH")
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--output-dir", type=Path, default=BASE_DIR / "reports" / "automation")
    parser.add_argument("--history-file", type=Path, default=BASE_DIR / "history" / "runs.jsonl")
    parser.add_argument("--ssh-host", default=None)
    parser.add_argument("--ssh-port", type=int, default=22)
    parser.add_argument("--ssh-user", default=None)
    parser.add_argument("--remote-benchmark-root", default=None)
    parser.add_argument("--remote-s3-repo", default=None)
    parser.add_argument("--remote-s3-root", action="append", default=[], metavar="CHECKPOINT=PATH")
    parser.add_argument("--remote-output-dir", default=None)
    parser.add_argument("--ssh-timeout", type=float, default=900.0)
    parser.add_argument("--cpu-affinity", default="")
    parser.add_argument("--preflight-blocks", type=int, default=5)
    parser.add_argument("--preflight-samples", type=int, default=10)
    parser.add_argument("--preflight-warmups", type=int, default=1)
    parser.add_argument("--preflight-iterations", type=int, default=50000)
    parser.add_argument("--timing-repetitions", type=int, default=2)
    parser.add_argument("--timing-parses", type=int, default=200)
    parser.add_argument("--timing-timeout", type=float, default=900.0)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.ssh_host:
        print(f"SSH_EXECUTOR_CONFIGURED=YES host={args.ssh_host} port={args.ssh_port} user={args.ssh_user or 'default'}")
    try:
        status, _summary = run_automation(args)
        return status
    except ProvenanceError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return error.exit_code
    except AutomationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return error.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
