"""Pinned, lab-owned executor for S3 native workload evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_SCRIPT = Path("tools/s3_15_native_workload_benchmark.py")
WORKLOADS = (
    "engineering.point-cloud-summary.v1",
    "geospatial.raster-window-statistics.v1",
    "energy.pv-timeseries-aggregation.v1",
)
TIMING_VARIANTS = (
    "C_O1",
    "S3_O1_BASELINE",
    "S3_O1_COMPACT_EA",
    "S3_O1_EXACT_SEGMENT",
    "S3_O1_LOOP_HYBRID",
)
BINARY_VARIANTS = (
    "S3_O1_BASELINE",
    "S3_O1_COMPACT_EA",
    "S3_O1_EXACT_SEGMENT",
    "S3_O1_LOOP_HYBRID",
)
COMPILER_SOURCE_FILES = (
    "bootstrap/s3/optimizer.py",
    "bootstrap/s3/memory_effects.py",
    "bootstrap/s3/backends/x86_64/backend.py",
    "bootstrap/s3/backends/x86_64/emitter.py",
    "bootstrap/s3/codegen.py",
)
_SHA1 = re.compile(r"^[0-9a-f]{40}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _run(argv: list[str], *, cwd: Path, timeout: float = 120.0) -> str:
    completed = subprocess.run(
        argv,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(f"command failed ({completed.returncode}): {argv[0]}: {detail}")
    return completed.stdout.strip()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_source_identity(source_url: str) -> str:
    parsed = urlsplit(source_url)
    if not parsed.scheme:
        return "local-git-repository"
    if parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError("source URL must not embed credentials, query tokens, or fragments")
    host = parsed.hostname or ""
    if parsed.port is not None:
        host = f"{host}:{parsed.port}"
    return urlunsplit((parsed.scheme, host, parsed.path, "", ""))


def _relative_source_file(root: Path, value: str) -> Path:
    relative = PurePosixPath(value)
    if not value or relative.is_absolute() or ".." in relative.parts or "\\" in value:
        raise ValueError(f"compiler source path is not repository-relative: {value!r}")
    return root.joinpath(*relative.parts)


def _checkout_source(source_url: str, revision: str, work_root: Path) -> tuple[Path, str]:
    if not _SHA1.fullmatch(revision):
        raise ValueError("source revision must be a full lowercase 40-character Git SHA")
    work_root = work_root.resolve()
    if work_root.exists():
        raise FileExistsError(f"work root already exists; refusing to overwrite: {work_root}")
    work_root.mkdir(parents=True)
    checkout = work_root / "s3-source"
    _run(["git", "clone", "--quiet", "--no-checkout", source_url, str(checkout)], cwd=work_root)
    _run(["git", "checkout", "--quiet", "--detach", revision], cwd=checkout)
    actual_revision = _run(["git", "rev-parse", "HEAD"], cwd=checkout)
    if actual_revision != revision:
        raise ValueError(f"checked out {actual_revision}, expected pinned source {revision}")
    tree = _run(["git", "rev-parse", "HEAD^{tree}"], cwd=checkout)
    status = _run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=checkout)
    if status:
        raise ValueError("pinned source checkout is not clean")
    if not (checkout / BENCHMARK_SCRIPT).is_file():
        raise ValueError(f"pinned S3 source is missing {BENCHMARK_SCRIPT.as_posix()}")
    return checkout, tree


def _positive_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{label} must be finite and positive")
    return number


def _validate_benchmark_result(
    result: dict[str, Any],
    *,
    checkout: Path,
    revision: str,
    tree: str,
    iterations: int,
    warmups: int,
    samples: int,
) -> dict[str, object]:
    identity = result.get("source_revision")
    if (
        not isinstance(identity, dict)
        or identity.get("git_commit") != revision
        or identity.get("git_tree") != tree
        or identity.get("worktree_clean") is not True
        or identity.get("identity_source")
        not in {"explicit_source_checkout_provenance", "local_git_checkout"}
    ):
        raise ValueError("raw benchmark source identity does not match the verified pinned checkout")

    source_hashes = result.get("compiler_source_sha256")
    if not isinstance(source_hashes, dict) or set(source_hashes) != set(COMPILER_SOURCE_FILES):
        raise ValueError("raw benchmark compiler source hash set is incomplete or unexpected")
    verified_hashes: dict[str, str] = {}
    for relative in COMPILER_SOURCE_FILES:
        expected = source_hashes.get(relative)
        source_file = _relative_source_file(checkout, relative)
        if not source_file.is_file() or not isinstance(expected, str) or not _SHA256.fullmatch(expected):
            raise ValueError(f"raw benchmark source hash is invalid: {relative}")
        actual = _sha256(source_file)
        if actual != expected:
            raise ValueError(f"raw benchmark compiler source hash mismatch: {relative}")
        verified_hashes[relative] = actual

    protocol = result.get("protocol")
    if not isinstance(protocol, dict) or protocol.get("default_instruction_budget_mode") != "per-instruction":
        raise ValueError("raw benchmark does not preserve the per-instruction default")
    c_flags = protocol.get("c_flags")
    required_c_flags = {"-fno-fast-math", "-ffp-contract=off", "-fno-tree-vectorize"}
    if not isinstance(c_flags, list) or not required_c_flags.issubset(set(c_flags)):
        raise ValueError("raw benchmark does not preserve strict scalar C reference flags")

    workloads = result.get("workloads")
    if not isinstance(workloads, dict) or set(workloads) != set(WORKLOADS):
        raise ValueError("raw benchmark workload set is incomplete or unexpected")
    summaries: dict[str, object] = {}
    for workload_id in WORKLOADS:
        workload = workloads[workload_id]
        if not isinstance(workload, dict) or workload.get("correctness") != "PASS_ALL_BUILDS":
            raise ValueError(f"correctness did not pass for every build: {workload_id}")
        timings = workload.get("timings")
        if not isinstance(timings, dict) or not set(TIMING_VARIANTS).issubset(timings):
            raise ValueError(f"timing variant set is incomplete: {workload_id}")
        for variant in TIMING_VARIANTS:
            timing = timings[variant]
            if not isinstance(timing, dict) or timing.get("sample_count") != samples:
                raise ValueError(f"unexpected sample count for {workload_id}/{variant}")
            _positive_number(timing.get("median_ns_per_call"), f"{workload_id}/{variant} median")
            _positive_number(timing.get("minimum_ns_per_call"), f"{workload_id}/{variant} minimum")
            _positive_number(timing.get("maximum_ns_per_call"), f"{workload_id}/{variant} maximum")
        run_protocol = workload.get("timing_protocol")
        if not isinstance(run_protocol, dict) or (
            run_protocol.get("iterations_per_sample") != iterations
            or run_protocol.get("warmups") != warmups
            or run_protocol.get("samples") != samples
        ):
            raise ValueError(f"run protocol mismatch for {workload_id}")
        hashes = workload.get("native_candidate_output_sha256")
        if not isinstance(hashes, dict) or not set(TIMING_VARIANTS).issubset(hashes):
            raise ValueError(f"correctness output hashes are incomplete: {workload_id}")
        if any(not isinstance(hashes[name], str) or not _SHA256.fullmatch(hashes[name]) for name in TIMING_VARIANTS):
            raise ValueError(f"correctness output hash is invalid: {workload_id}")

        binaries = workload.get("binary_metrics")
        if not isinstance(binaries, dict) or not set(BINARY_VARIANTS).issubset(binaries):
            raise ValueError(f"binary metric set is incomplete: {workload_id}")
        for variant in BINARY_VARIANTS:
            metrics = binaries[variant]
            if not isinstance(metrics, dict):
                raise ValueError(f"binary metrics are malformed: {workload_id}/{variant}")
            for metric in ("text_section_bytes", "exported_function_bytes", "static_machine_instructions"):
                _positive_number(metrics.get(metric), f"{workload_id}/{variant}/{metric}")
        summaries[workload_id] = {
            "correctness": workload["correctness"],
            "samples": samples,
            "per_median_ns_per_call": timings["S3_O1_BASELINE"]["median_ns_per_call"],
            "exact_vs_per": workload.get("per_over_exact_segment_ratio"),
            "hybrid_vs_per": workload.get("per_over_loop_hybrid_ratio"),
            "compact_ea_applied": workload.get("compact_ea_applied"),
            "per_binary_metrics": binaries["S3_O1_BASELINE"],
            "per_output_sha256": hashes["S3_O1_BASELINE"],
        }
    return {"verified_compiler_source_sha256": verified_hashes, "workloads": summaries}


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def _native_artifact_inventory(output_dir: Path) -> list[dict[str, object]]:
    artifacts: list[dict[str, object]] = []
    for path in sorted(output_dir.iterdir(), key=lambda item: item.name):
        if path.suffix not in {".s", ".so"}:
            continue
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"native output is not a regular file: {path.name}")
        artifacts.append(
            {
                "path": path.name,
                "kind": "assembly" if path.suffix == ".s" else "shared_object",
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
            }
        )
    assembly_count = sum(item["kind"] == "assembly" for item in artifacts)
    binary_count = sum(item["kind"] == "shared_object" for item in artifacts)
    if assembly_count < 15 or binary_count < 16:
        raise ValueError("benchmark did not preserve the expected S3/C native artifact set")
    return artifacts


def execute(
    *,
    source_url: str,
    revision: str,
    work_root: Path,
    output_dir: Path,
    iterations: int = 1000,
    warmups: int = 3,
    samples: int = 21,
    timeout_seconds: int = 3600,
) -> dict[str, object]:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("S3 native workload executor requires Linux x86-64")
    if iterations < 1 or warmups < 1 or samples < 3 or timeout_seconds < 1:
        raise ValueError("iterations/warmups/timeout must be positive and samples must be >= 3")
    source_identity = _safe_source_identity(source_url)
    output_dir = output_dir.resolve()
    work_root = work_root.resolve()
    if output_dir == work_root or work_root in output_dir.parents or output_dir in work_root.parents:
        raise ValueError("work root and evidence output directory must be disjoint")
    if output_dir.exists():
        raise FileExistsError(f"output directory already exists; refusing to overwrite: {output_dir}")

    started_at = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    checkout, tree = _checkout_source(source_url, revision, work_root)
    lab_head = _run(["git", "rev-parse", "HEAD"], cwd=ROOT)
    lab_tree = _run(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT)
    lab_clean = not bool(_run(["git", "status", "--porcelain"], cwd=ROOT))
    output_dir.mkdir(parents=True)
    raw_path = output_dir / "native-workload-benchmark-v1.json"
    command = [
        sys.executable,
        str(checkout / BENCHMARK_SCRIPT),
        "--output-dir",
        str(output_dir),
        "--iterations",
        str(iterations),
        "--warmups",
        str(warmups),
        "--samples",
        str(samples),
        "--source-revision",
        revision,
        "--source-tree",
        tree,
        "--source-worktree-state",
        "clean",
    ]
    try:
        process = subprocess.run(
            command,
            cwd=checkout,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        stdout = process.stdout
        stderr = process.stderr
        return_code: int | None = process.returncode
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        stdout_value = exc.stdout or ""
        stderr_value = exc.stderr or ""
        stdout = stdout_value.decode(errors="replace") if isinstance(stdout_value, bytes) else stdout_value
        stderr = stderr_value.decode(errors="replace") if isinstance(stderr_value, bytes) else stderr_value
        return_code = None
        timed_out = True
    (output_dir / "executor-stdout.txt").write_text(stdout, encoding="utf-8", newline="\n")
    (output_dir / "executor-stderr.txt").write_text(stderr, encoding="utf-8", newline="\n")
    ended_at = datetime.now(timezone.utc).isoformat()
    elapsed = time.monotonic() - started
    validated: dict[str, object] | None = None
    error: str | None = None
    if timed_out:
        error = f"benchmark subprocess timed out after {timeout_seconds} seconds"
    elif return_code != 0:
        error = f"benchmark subprocess exited {return_code}"
    elif not raw_path.is_file():
        error = "benchmark subprocess succeeded without its required JSON result"
    else:
        try:
            raw_result = json.loads(raw_path.read_text(encoding="utf-8"))
            if not isinstance(raw_result, dict):
                raise ValueError("raw benchmark result must be a JSON object")
            validated = _validate_benchmark_result(
                raw_result,
                checkout=checkout,
                revision=revision,
                tree=tree,
                iterations=iterations,
                warmups=warmups,
                samples=samples,
            )
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            error = str(exc)

    artifact_inventory: list[dict[str, object]] = []
    if raw_path.is_file():
        try:
            artifact_inventory = _native_artifact_inventory(output_dir)
        except ValueError as exc:
            error = error or str(exc)
    report: dict[str, object] = {
        "schema_version": "1.0.0",
        "report_kind": "S3_BENCHMARKS_1_9_PINNED_NATIVE_EXECUTION",
        "status": "PASS" if error is None else "FAIL",
        "provenance": {
            "lab_head": lab_head,
            "lab_tree": lab_tree,
            "lab_worktree_clean": lab_clean,
            "executor_sha256": _sha256(Path(__file__)),
            "s3_repository": source_identity,
            "s3_commit": revision,
            "s3_tree": tree,
            "s3_worktree_clean": True,
            "raw_result_sha256": _sha256(raw_path) if raw_path.is_file() else None,
            "native_artifacts": artifact_inventory,
        },
        "host": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": sys.version.split()[0],
        },
        "protocol": {
            "iterations_per_sample": iterations,
            "warmups": warmups,
            "samples": samples,
            "timeout_seconds": timeout_seconds,
            "timed_execution": "S3 benchmark script; compile/setup excluded; same-process scalar C ABI and ctypes dispatch included",
            "timing_class": "CHARACTERIZATION_ONLY",
            "native_speedup_claim": False,
        },
        "execution": {
            "started_at_utc": started_at,
            "ended_at_utc": ended_at,
            "elapsed_seconds": round(elapsed, 6),
            "return_code": return_code,
            "timed_out": timed_out,
            "raw_result_path": raw_path.name if raw_path.is_file() else None,
            "validated": validated,
            "error": error,
        },
    }
    (output_dir / "executor-result-v1.json").write_bytes(_json_bytes(report))
    if error is not None:
        raise RuntimeError(f"native evidence run failed validation; artifacts preserved at {output_dir}: {error}")
    return report


def execute_matrix(
    *,
    source_url: str,
    revisions: list[str],
    work_root: Path,
    output_dir: Path,
    iterations: int = 1000,
    warmups: int = 3,
    samples: int = 21,
    timeout_seconds: int = 3600,
) -> dict[str, object]:
    """Run the qualified single-SHA protocol serially for exact revisions."""
    if not revisions:
        raise ValueError("at least one source revision is required")
    if any(not isinstance(revision, str) or not _SHA1.fullmatch(revision) for revision in revisions):
        raise ValueError("every source revision must be a full lowercase 40-character Git SHA")
    if len(set(revisions)) != len(revisions):
        raise ValueError("source revision list contains duplicates")
    source_identity = _safe_source_identity(source_url)

    output_dir = output_dir.resolve()
    work_root = work_root.resolve()
    if output_dir.exists() or work_root.exists():
        raise FileExistsError("matrix output and work roots must both be new directories")
    if output_dir == work_root or work_root in output_dir.parents or output_dir in work_root.parents:
        raise ValueError("matrix work root and output directory must be disjoint")

    output_dir.mkdir(parents=True)
    rows: list[dict[str, object]] = []
    for revision in sorted(revisions):
        try:
            report = execute(
                source_url=source_url,
                revision=revision,
                work_root=work_root / revision,
                output_dir=output_dir / revision,
                iterations=iterations,
                warmups=warmups,
                samples=samples,
                timeout_seconds=timeout_seconds,
            )
            rows.append({"source_revision": revision, "status": report["status"], "result": report})
        except Exception as exc:
            rows.append(
                {
                    "source_revision": revision,
                    "status": "FAIL",
                    "error": f"{type(exc).__name__}: {exc}",
                    "result_path": (
                        output_dir / revision / "executor-result-v1.json"
                    ).as_posix(),
                }
            )

    report: dict[str, object] = {
        "schema_version": "1.0.0",
        "report_kind": "S3_BENCHMARKS_MULTI_SHA_EXECUTION_MATRIX",
        "source_repository": source_identity,
        "revision_order": sorted(revisions),
        "execution_order": "serial_ascending_sha",
        "status": "PASS" if all(row["status"] == "PASS" for row in rows) else "FAIL",
        "runs": rows,
    }
    (output_dir / "multi-sha-result-v1.json").write_bytes(_json_bytes(report))
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-url", required=True, help="Git URL or local Git repository for the S3 source")
    revisions = parser.add_mutually_exclusive_group(required=True)
    revisions.add_argument("--source-revision", help="one exact full Git SHA")
    revisions.add_argument("--source-revisions", nargs="+", help="serial matrix of exact full Git SHAs")
    parser.add_argument("--work-root", type=Path, required=True, help="new directory for the detached S3 clone")
    parser.add_argument("--output-dir", type=Path, required=True, help="new directory for immutable run evidence")
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--warmups", type=int, default=3)
    parser.add_argument("--samples", type=int, default=21)
    parser.add_argument("--timeout-seconds", type=int, default=3600)
    args = parser.parse_args()
    if args.source_revisions:
        report = execute_matrix(
            source_url=args.s3_url,
            revisions=args.source_revisions,
            work_root=args.work_root,
            output_dir=args.output_dir,
            iterations=args.iterations,
            warmups=args.warmups,
            samples=args.samples,
            timeout_seconds=args.timeout_seconds,
        )
        print(f"S3_MULTI_SHA_EXECUTOR={report['status']} revisions={len(report['runs'])}")
        return 0 if report["status"] == "PASS" else 1

    report = execute(
        source_url=args.s3_url,
        revision=args.source_revision,
        work_root=args.work_root,
        output_dir=args.output_dir,
        iterations=args.iterations,
        warmups=args.warmups,
        samples=args.samples,
        timeout_seconds=args.timeout_seconds,
    )
    workloads = report["execution"]["validated"]["workloads"]
    print(f"S3_19_EXECUTOR={report['status']} s3_commit={args.source_revision} workloads={len(workloads)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
