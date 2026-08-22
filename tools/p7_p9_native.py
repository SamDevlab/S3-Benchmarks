"""Correctness-first native timing runner for the focused P7-P9 workloads."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import statistics
import subprocess
import sys
import time
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from benchmarks.rc1.native_workloads import NATIVE_WORKLOADS  # noqa: E402
from benchmarks.rc1.statistics import robust_stats  # noqa: E402
from tools.artifacts import require_provenance  # noqa: E402
from tools.assembly_analyzer import analyze_assembly_text  # noqa: E402

CHECKPOINT_SHAS = {
    "H4": "e23b092bec100cedc520841a7dd0f4488090b6a1",
    "H5": "9b39c7070d7bfa23d709c2128eb0b0bbef164177",
}


def _json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _compile_c(workload: Any, root: Path) -> dict[str, Any]:
    compiler = shutil.which("gcc") or shutil.which("cc")
    if compiler is None:
        raise RuntimeError("gcc/cc unavailable for P7-P9 control")
    root.mkdir(parents=True, exist_ok=False)
    source = root / f"{workload.workload_id.lower()}.c"
    source.write_text(workload.c_source, encoding="utf-8", newline="\n")
    variants: dict[str, Any] = {}
    for optimization in ("O0", "O2", "O3"):
        binary = root / f"{workload.workload_id.lower()}-{optimization}"
        assembly = root / f"{workload.workload_id.lower()}-{optimization}.s"
        compile_command = [compiler, f"-{optimization}", "-std=c99", str(source), "-o", str(binary)]
        subprocess.run(compile_command, check=True, capture_output=True, text=True)
        assembly_command = [compiler, f"-{optimization}", "-std=c99", "-S", str(source), "-o", str(assembly)]
        subprocess.run(assembly_command, check=True, capture_output=True, text=True)
        variants[optimization] = {
            "binary": str(binary.resolve()),
            "binary_sha256": _sha256_file(binary),
            "assembly": str(assembly.resolve()),
            "assembly_sha256": _sha256_file(assembly),
            "metrics": analyze_assembly_text(assembly.read_text(encoding="utf-8"), f"C-{workload.workload_id}-{optimization}", binary).__dict__,
            "commands": [compile_command, assembly_command],
        }
    return {
        "workload_id": workload.workload_id,
        "compiler": compiler,
        "compiler_version": subprocess.run([compiler, "--version"], check=True, capture_output=True, text=True).stdout.splitlines()[0],
        "source": str(source.resolve()),
        "source_sha256": _sha256_file(source),
        "variants": variants,
    }


def _compile_s3(checkpoint: str, root: Path, artifact_root: Path, workload_id: str, benchmark_sha: str) -> dict[str, Any]:
    command = [
        sys.executable,
        str(BASE_DIR / "tools" / "compile_s3_native_workload.py"),
        "--s3-root", str(root),
        "--s3-sha", CHECKPOINT_SHAS[checkpoint],
        "--benchmark-sha", benchmark_sha,
        "--checkpoint", checkpoint,
        "--workload-id", workload_id,
        "--output-dir", str(artifact_root),
    ]
    environment = os.environ.copy()
    environment["S3_REPO"] = str(root.resolve())
    subprocess.run(command, cwd=str(BASE_DIR), env=environment, check=True, capture_output=True, text=True)
    return json.loads((artifact_root / "manifest.json").read_text(encoding="utf-8"))


def _run(binary: Path, loops: int, affinity: str) -> tuple[int, int]:
    prefix = affinity.split()
    command = prefix + [str(binary), "--loop", str(loops)]
    start = time.perf_counter_ns()
    process = subprocess.run(command, capture_output=True, text=True, check=False)
    elapsed = time.perf_counter_ns() - start
    if process.returncode != 0:
        raise RuntimeError(f"native workload failed: {binary}: {process.stderr.strip()}")
    match = re.search(r"program returned:\s*(-?\d+)", process.stdout)
    if match is None:
        raise RuntimeError(f"native workload produced no result: {binary}")
    return elapsed, int(match.group(1))


def _sample_row(*, run_id: str, workload: str, block: int, sequence: int, checkpoint: str, variant: str, elapsed: int, operations: int, result: int, affinity: str, role: str) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "workload": workload,
        "block_id": f"block-{block:03d}",
        "sequence_index": sequence,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "timestamp_ns": time.time_ns(),
        "checkpoint": checkpoint,
        "variant": variant,
        "raw_elapsed_ns": elapsed,
        "operations_per_run": operations,
        "ns_per_operation": elapsed / operations,
        "result": result,
        "cpu_affinity": affinity,
        "control_candidate_role": role,
    }


def _schedule(block: int) -> list[tuple[str, str, str]]:
    base = [("C", "O0", "control"), ("C", "O2", "control"), ("C", "O3", "control"), ("H4", "O0", "candidate"), ("H4", "O1", "candidate"), ("H5", "O0", "candidate"), ("H5", "O1", "candidate")]
    shift = block % len(base)
    return base[shift:] + base[:shift]


def _write_samples(path: Path, rows: list[dict[str, Any]]) -> None:
    _json(path.with_suffix(".json"), rows)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _paired_ratio(rows: list[dict[str, Any]], left: tuple[str, str], right: tuple[str, str]) -> list[float]:
    values: dict[tuple[str, int], dict[tuple[str, str], float]] = {}
    for row in rows:
        key = (row["workload"], row["block_id"])
        values.setdefault(key, {})[(row["checkpoint"], row["variant"])] = row["ns_per_operation"]
    return [(item[right] / item[left] - 1.0) * 100.0 for item in values.values() if left in item and right in item]


def run_campaign(args: argparse.Namespace) -> dict[str, Any]:
    roots = {key: Path(value).resolve() for key, value in (item.split("=", 1) for item in args.s3_root)}
    if set(roots) != set(CHECKPOINT_SHAS):
        raise SystemExit("P7-P9 requires H4 and H5 S3 roots")
    for checkpoint, root in roots.items():
        require_provenance(s3_repo=root, requested_s3_sha=CHECKPOINT_SHAS[checkpoint], benchmark_repo=BASE_DIR, requested_benchmark_sha=args.benchmark_sha)
    artifact_root = args.artifact_root.resolve()
    report_root = args.report_root.resolve()
    if artifact_root.exists() or report_root.exists():
        raise RuntimeError("refusing to reuse P7-P9 campaign roots")
    artifact_root.mkdir(parents=True)
    report_root.mkdir(parents=True)
    all_summaries: list[dict[str, Any]] = []
    for workload in NATIVE_WORKLOADS:
        control = _compile_c(workload, artifact_root / "control" / workload.workload_id)
        s3_manifests = {checkpoint: _compile_s3(checkpoint, root, artifact_root / checkpoint / workload.workload_id, workload.workload_id, args.benchmark_sha) for checkpoint, root in roots.items()}
        binaries: dict[tuple[str, str], Path] = {("C", opt): Path(record["binary"]) for opt, record in control["variants"].items()}
        for checkpoint, manifest in s3_manifests.items():
            for optimization, record in manifest["records"].items():
                binaries[(checkpoint, optimization)] = Path(record["executable"])
        correctness: dict[str, Any] = {"control_result": None, "variants": {}, "status": "PASS"}
        _, c_result = _run(binaries[("C", "O2")], 1, args.cpu_affinity)
        correctness["control_result"] = c_result
        for key, binary in sorted(binaries.items()):
            _, result = _run(binary, 1, args.cpu_affinity)
            correctness["variants"][f"{key[0]}-{key[1]}"] = result
            if result != c_result:
                correctness["status"] = "FAIL"
                raise RuntimeError(f"{workload.workload_id} correctness mismatch {key}: {result} != {c_result}")
        rows: list[dict[str, Any]] = []
        for warmup in range(args.warmups):
            for checkpoint, variant, _role in _schedule(warmup):
                _run(binaries[(checkpoint, variant)], workload.operations_per_run, args.cpu_affinity)
        sequence = 0
        for block in range(args.repetitions):
            for checkpoint, variant, role in _schedule(block):
                sequence += 1
                elapsed, result = _run(binaries[(checkpoint, variant)], workload.operations_per_run, args.cpu_affinity)
                rows.append(_sample_row(run_id=args.run_id, workload=workload.workload_id, block=block, sequence=sequence, checkpoint=checkpoint, variant=variant, elapsed=elapsed, operations=workload.operations_per_run, result=result, affinity=args.cpu_affinity, role=role))
        raw_csv = report_root / workload.workload_id / "raw" / "samples.csv"
        _write_samples(raw_csv, rows)
        grouped: dict[tuple[str, str], list[float]] = {}
        for row in rows:
            grouped.setdefault((row["checkpoint"], row["variant"]), []).append(row["ns_per_operation"])
        summaries = [{"checkpoint": key[0], "variant": key[1], **robust_stats(values)} for key, values in sorted(grouped.items())]
        controls = [row["ns_per_operation"] for row in rows if row["checkpoint"] == "C" and row["variant"] == "O2"]
        control_stats = robust_stats(controls)
        control_range = max(controls) / min(controls) - 1.0
        control_stable = control_range <= 0.05
        paired = {
            "rc1_vs_m230_percent": _paired_ratio(rows, ("H4", "O1"), ("H5", "O1")),
            "rc1_vs_c_o2_percent": _paired_ratio(rows, ("C", "O2"), ("H5", "O1")),
        }
        structural = {checkpoint: {opt: manifest["records"][opt]["metrics"] for opt in ("O0", "O1")} for checkpoint, manifest in s3_manifests.items()}
        c_structural = {opt: control["variants"][opt]["metrics"] for opt in ("O0", "O2", "O3")}
        status = "PROMOTED" if correctness["status"] == "PASS" and control_stable and len(rows) == args.repetitions * 7 and all(len(values) == args.repetitions for values in grouped.values()) else "EXPERIMENTAL"
        summary = {
            "schema": "s3.rc1.p7-p9.native-summary.v1",
            "run_id": args.run_id,
            "workload": workload.workload_id,
            "name": workload.name,
            "status": status,
            "correctness": correctness,
            "inputs_pinned": True,
            "oracle_defined": True,
            "sample_level_data_available": "YES",
            "repeatable": control_stable,
            "control_stable": control_stable,
            "control_drift_percent": control_range * 100.0,
            "control_stats": control_stats,
            "summaries": summaries,
            "paired": paired,
            "structural": {"s3": structural, "c": c_structural},
            "provenance": {"benchmark_sha": args.benchmark_sha, "s3_shas": CHECKPOINT_SHAS},
            "raw_samples": "raw/samples.json",
            "protocol": {"warmups": args.warmups, "repetitions": args.repetitions, "operations_per_run": workload.operations_per_run, "schedule": "rotating C-O0 C-O2 C-O3 H4-O0 H4-O1 H5-O0 H5-O1", "timing": "native process execution excluding compilation", "cpu_affinity": args.cpu_affinity},
            "perf": "DEFERRED_BY_ENVIRONMENT",
        }
        _json(report_root / workload.workload_id / "summary.json", summary)
        (report_root / workload.workload_id / "summary.md").write_text("# " + workload.workload_id + " native workload\n\n" + json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        all_summaries.append(summary)
    result = {"schema": "s3.rc1.p7-p9.native-result.v1", "run_id": args.run_id, "status": "PASS", "workloads": all_summaries, "provenance": {"benchmark_sha": args.benchmark_sha, "s3_shas": CHECKPOINT_SHAS}}
    _json(report_root / "summary.json", result)
    _json(report_root / "protocol.json", {"workloads": [item["workload"] for item in all_summaries], "correctness_before_timing": True, "sample_level_data_available": "YES", "native_speedup_claim": "NO"})
    print(json.dumps({"status": "PASS", "workloads": [item["workload"] + ":" + item["status"] for item in all_summaries]}, sort_keys=True))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-root", action="append", required=True, metavar="CHECKPOINT=PATH")
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--report-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--warmups", type=int, default=5)
    parser.add_argument("--repetitions", type=int, default=30)
    parser.add_argument("--cpu-affinity", default="taskset -c 0")
    args = parser.parse_args()
    run_campaign(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
