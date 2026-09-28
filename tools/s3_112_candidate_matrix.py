"""Build and compare an explicit matrix of pinned S3 compiler variants."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import importlib.util
import json
import math
import platform
import random
import re
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.s3_19_executor import (
    BENCHMARK_SCRIPT,
    _checkout_source,
    _safe_source_identity,
)


ROOT = Path(__file__).resolve().parents[1]
SHA1 = re.compile(r"^[0-9a-f]{40}$")
VARIANT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.+-]{0,63}$")
WORKLOADS = {
    "engineering.point-cloud-summary.v1": "point_cloud_summary",
    "geospatial.raster-window-statistics.v1": "raster_window_statistics",
    "energy.pv-timeseries-aggregation.v1": "energy_series_aggregation",
}
OPTIMIZATIONS = {"O0", "O1"}
NATIVE_POLICIES = {"baseline", "compact-ea"}
BUDGET_MODES = {"per-instruction", "exact-segment", "loop-hybrid"}


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()


def _write_once(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(payload)


def _positive_int(value: object, label: str, *, minimum: int = 1) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label} must be an integer >= {minimum}")
    return value


def _validate_variant(value: object, label: str) -> dict[str, str]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    variant_id = value.get("id")
    revision = value.get("revision")
    optimization = value.get("optimization")
    native_policy = value.get("native_policy")
    budget_mode = value.get("instruction_budget_mode")
    if not isinstance(variant_id, str) or VARIANT_ID.fullmatch(variant_id) is None:
        raise ValueError(f"{label}.id is invalid")
    if not isinstance(revision, str) or SHA1.fullmatch(revision) is None:
        raise ValueError(f"{label}.revision must be a full lowercase Git SHA")
    if optimization not in OPTIMIZATIONS:
        raise ValueError(f"{label}.optimization is unsupported")
    if native_policy not in NATIVE_POLICIES:
        raise ValueError(f"{label}.native_policy is unsupported")
    if budget_mode not in BUDGET_MODES:
        raise ValueError(f"{label}.instruction_budget_mode is unsupported")
    return {
        "id": variant_id,
        "revision": revision,
        "optimization": optimization,
        "native_policy": native_policy,
        "instruction_budget_mode": budget_mode,
    }


def validate_spec(value: object) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != "s3.candidate-matrix.v1":
        raise ValueError("unsupported candidate matrix schema")
    experiment_id = value.get("experiment_id")
    source_url = value.get("source_url")
    if not isinstance(experiment_id, str) or not experiment_id.strip():
        raise ValueError("experiment_id is required")
    if not isinstance(source_url, str) or not source_url.strip():
        raise ValueError("source_url is required")
    source_identity = _safe_source_identity(source_url)

    control = _validate_variant(value.get("control"), "control")
    candidates_value = value.get("candidates")
    if not isinstance(candidates_value, list) or not candidates_value:
        raise ValueError("at least one candidate variant is required")
    candidates = [
        _validate_variant(item, f"candidates[{index}]")
        for index, item in enumerate(candidates_value)
    ]
    variants = [control, *candidates]
    ids = [item["id"] for item in variants]
    if len(set(ids)) != len(ids):
        raise ValueError("variant IDs must be unique")

    workloads_value = value.get("workloads")
    if not isinstance(workloads_value, list) or not workloads_value:
        raise ValueError("at least one workload is required")
    if any(not isinstance(item, str) or item not in WORKLOADS for item in workloads_value):
        raise ValueError("workload set contains an unsupported identity")
    if len(set(workloads_value)) != len(workloads_value):
        raise ValueError("workload IDs must be unique")

    protocol_value = value.get("protocol")
    if not isinstance(protocol_value, dict):
        raise ValueError("protocol is required")
    protocol = {
        "iterations_per_sample": _positive_int(protocol_value.get("iterations_per_sample"), "iterations_per_sample"),
        "warmups": _positive_int(protocol_value.get("warmups"), "warmups"),
        "samples": _positive_int(protocol_value.get("samples"), "samples", minimum=3),
        "bootstrap_resamples": _positive_int(protocol_value.get("bootstrap_resamples", 10_000), "bootstrap_resamples", minimum=100),
        "seed": _positive_int(protocol_value.get("seed", 11201), "seed", minimum=0),
    }
    return {
        "schema_version": "s3.candidate-matrix.v1",
        "experiment_id": experiment_id,
        "source_url": source_url,
        "source_identity": source_identity,
        "control": control,
        "candidates": candidates,
        "workloads": list(workloads_value),
        "protocol": protocol,
    }


def sample_order(labels: list[str], sample_index: int) -> list[str]:
    if not labels or len(set(labels)) != len(labels) or sample_index < 0:
        raise ValueError("sample order inputs are invalid")
    offset = sample_index % len(labels)
    order = labels[offset:] + labels[:offset]
    return list(reversed(order)) if sample_index % 2 else order


def _load_benchmark(checkout: Path, revision: str):
    path = checkout / BENCHMARK_SCRIPT
    if not path.is_file():
        raise FileNotFoundError(f"pinned S3 benchmark helper is missing: {path}")
    sys.path.insert(0, str(checkout))
    spec = importlib.util.spec_from_file_location(f"s3_matrix_benchmark_{revision}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load pinned S3 benchmark helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _worker_build(checkout: Path, variant: dict[str, str], workloads: list[str], output: Path) -> dict[str, Any]:
    checkout = checkout.resolve()
    output.mkdir(parents=True, exist_ok=True)
    benchmark = _load_benchmark(checkout, variant["revision"])
    manifest, references = benchmark._load_inputs()
    manifest_by_id = {item["workload_id"]: item for item in manifest["workloads"]}
    references_by_id = {item["workload_id"]: item for item in references["workloads"]}
    rows: dict[str, Any] = {}
    level = benchmark.OptimizationLevel(variant["optimization"])
    budget_mode = benchmark.InstructionBudgetMode(variant["instruction_budget_mode"])
    for workload_id in workloads:
        if workload_id not in manifest_by_id or workload_id not in references_by_id:
            raise ValueError(f"pinned source lacks workload inputs: {workload_id}")
        manifest_row = manifest_by_id[workload_id]
        reference = references_by_id[workload_id]
        if manifest_row["dataset_sha256"] != reference["dataset_sha256"]:
            raise ValueError(f"reference dataset identity mismatch: {workload_id}")
        if manifest_row["expected_output_sha256"] != reference["output_sha256"]:
            raise ValueError(f"reference output identity mismatch: {workload_id}")
        source_path = checkout / "benchmarks" / manifest_row["s3_source"]
        source_bytes = source_path.read_bytes()
        source = source_bytes.decode("utf-8")
        stem = hashlib.sha256(workload_id.encode("utf-8")).hexdigest()[:16]
        binary = output / f"{stem}.so"
        compiled = benchmark._compile_s3(
            source,
            binary,
            level,
            variant["native_policy"],
            budget_mode=budget_mode,
        )
        assembly = Path(compiled["assembly_path"])
        rows[workload_id] = {
            "source_sha256": _sha256(source_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")),
            "benchmark_helper_sha256": _sha256((checkout / BENCHMARK_SCRIPT).read_bytes()),
            "dataset_sha256": manifest_row["dataset_sha256"],
            "expected_output_sha256": manifest_row["expected_output_sha256"],
            "assembly": {"path": assembly.name, "bytes": assembly.stat().st_size, "sha256": _sha256(assembly.read_bytes())},
            "binary": {"path": binary.name, "bytes": binary.stat().st_size, "sha256": _sha256(binary.read_bytes())},
            "compiler": compiled["compiler"],
            "compiler_version": compiled["compiler_version"],
            "optimization": compiled["optimization"],
            "native_policy": compiled["native_policy"],
            "instruction_budget_mode": compiled["instruction_budget_mode"],
        }
    return {"variant": variant, "workloads": rows}


def _worker_main(args: argparse.Namespace) -> int:
    variant = json.loads(args.worker_variant_json)
    workloads = json.loads(args.worker_workloads_json)
    result = _worker_build(args.worker_checkout, variant, workloads, args.worker_output)
    _write_once(args.worker_result, _json_bytes(result))
    return 0


def _run_worker(
    checkout: Path, variant: dict[str, str], workloads: list[str], output: Path,
    result_path: Path, log_dir: Path, timeout_seconds: int,
) -> dict[str, Any]:
    command = [
        sys.executable, str(Path(__file__).resolve()),
        "--_worker-checkout", str(checkout),
        "--_worker-variant-json", json.dumps(variant, sort_keys=True),
        "--_worker-workloads-json", json.dumps(workloads),
        "--_worker-output", str(output),
        "--_worker-result", str(result_path),
    ]
    try:
        process = subprocess.run(command, capture_output=True, text=True, timeout=timeout_seconds)
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        _write_once(log_dir / f"{variant['id']}-build-stdout.txt", stdout.encode())
        _write_once(log_dir / f"{variant['id']}-build-stderr.txt", stderr.encode())
        raise TimeoutError(f"variant {variant['id']} build timed out after {timeout_seconds}s") from exc
    _write_once(log_dir / f"{variant['id']}-build-stdout.txt", process.stdout.encode())
    _write_once(log_dir / f"{variant['id']}-build-stderr.txt", process.stderr.encode())
    if process.returncode != 0:
        raise RuntimeError(f"variant {variant['id']} build worker failed with exit {process.returncode}")
    return json.loads(result_path.read_text(encoding="utf-8"))


def _inspect_binary(path: Path, symbol: str) -> dict[str, int]:
    size = subprocess.run(["size", "-A", str(path)], check=True, capture_output=True, text=True).stdout
    text_bytes = next(
        (int(parts[1]) for line in size.splitlines() if (parts := line.split()) and parts[0] == ".text"),
        0,
    )
    nm = subprocess.run(["nm", "-S", "--defined-only", str(path)], check=True, capture_output=True, text=True).stdout
    function_bytes = next(
        (int(parts[1], 16) for line in nm.splitlines() if (parts := line.split()) and len(parts) >= 4 and parts[-1] == symbol),
        0,
    )
    if text_bytes <= 0 or function_bytes <= 0:
        raise ValueError(f"could not inspect .text and symbol {symbol}")
    disassembly = subprocess.run(
        ["objdump", "-d", f"--disassemble={symbol}", str(path)],
        check=True, capture_output=True, text=True,
    ).stdout
    instructions: list[tuple[str, str]] = []
    for line in disassembly.splitlines():
        if ":\t" not in line:
            continue
        columns = line.split("\t")
        if len(columns) >= 3:
            fields = columns[2].strip().split(None, 1)
            if fields:
                instructions.append((fields[0].lower(), fields[1] if len(fields) > 1 else ""))
    if not instructions:
        raise ValueError(f"no disassembly instructions found for {symbol}")
    frame = 0
    for mnemonic, operands in instructions:
        match = re.search(r"\$0x([0-9a-f]+),%rsp", operands)
        if mnemonic == "sub" and match:
            frame = int(match.group(1), 16)
    return {
        "elf_file_bytes": path.stat().st_size,
        "text_section_bytes": text_bytes,
        "exported_function_bytes": function_bytes,
        "static_machine_instructions": len(instructions),
        "static_branches": sum(mnemonic.startswith("j") for mnemonic, _ in instructions),
        "static_calls": sum(mnemonic.startswith("call") for mnemonic, _ in instructions),
        "static_memory_references": sum("(" in operands for _, operands in instructions),
        "static_stack_references": sum("%rsp" in operands or "%rbp" in operands for _, operands in instructions),
        "stack_frame_bytes": frame,
    }


def _paired_summary(
    baseline: list[float], candidate: list[float], *, seed: int, resamples: int
) -> dict[str, Any]:
    if len(baseline) != len(candidate) or len(baseline) < 3:
        raise ValueError("paired comparison requires equal sample counts >= 3")
    ratios = [left / right for left, right in zip(baseline, candidate, strict=True)]
    rng = random.Random(seed)
    draws = sorted(statistics.median(rng.choices(ratios, k=len(ratios))) for _ in range(resamples))
    low, high = draws[int(0.025 * resamples)], draws[int(0.975 * resamples) - 1]
    if low > 1.05:
        classification = "MATERIAL_IMPROVEMENT"
    elif high < 0.95:
        classification = "MATERIAL_REGRESSION"
    elif low >= 0.95 and high <= 1.05:
        classification = "NO_MATERIAL_CHANGE_WITHIN_5_PERCENT"
    else:
        classification = "INCONCLUSIVE"
    return {
        "baseline_over_candidate_median_ratio": statistics.median(ratios),
        "paired_bootstrap_95_percentile_interval": [low, high],
        "resamples": resamples,
        "seed": seed,
        "material_change_threshold": 0.05,
        "classification": classification,
    }


def _disjoint_new_paths(work_root: Path, output_dir: Path) -> tuple[Path, Path]:
    work, output = work_root.resolve(), output_dir.resolve()
    if work.exists() or output.exists():
        raise FileExistsError("work root and evidence output must be new paths")
    if work == output or work in output.parents or output in work.parents:
        raise ValueError("work root and evidence output must be disjoint")
    return work, output


def execute_matrix_spec(
    *, spec_path: Path, work_root: Path, output_dir: Path, timeout_seconds: int = 900,
) -> dict[str, Any]:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("candidate matrix requires Linux x86-64")
    if timeout_seconds < 1:
        raise ValueError("timeout_seconds must be positive")
    spec_bytes = spec_path.read_bytes()
    spec = validate_spec(json.loads(spec_bytes))
    work_root, output_dir = _disjoint_new_paths(work_root, output_dir)
    lab_head = _git(ROOT, "rev-parse", "HEAD")
    lab_tree = _git(ROOT, "rev-parse", "HEAD^{tree}")
    if _git(ROOT, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("lab checkout must be clean before an evidence run")

    started_at = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    work_root.mkdir(parents=True)
    output_dir.mkdir(parents=True)
    variants = [spec["control"], *spec["candidates"]]
    builds: dict[str, dict[str, Any]] = {}
    checkouts: dict[str, Path] = {}
    try:
        for variant in variants:
            variant_work = work_root / variant["id"]
            checkout, tree = _checkout_source(spec["source_url"], variant["revision"], variant_work)
            checkouts[variant["id"]] = checkout
            artifact_dir = output_dir / "artifacts" / variant["id"]
            result_path = output_dir / "build-results" / f"{variant['id']}.json"
            result_path.parent.mkdir(parents=True, exist_ok=True)
            result = _run_worker(
                checkout, variant, spec["workloads"], artifact_dir, result_path,
                output_dir / "build-logs", timeout_seconds,
            )
            result["source_tree"] = tree
            builds[variant["id"]] = result

        control_id = spec["control"]["id"]
        benchmark = _load_benchmark(checkouts[control_id], spec["control"]["revision"])
        manifest, references = benchmark._load_inputs()
        reference_by_id = {row["workload_id"]: row for row in references["workloads"]}
        manifest_by_id = {row["workload_id"]: row for row in manifest["workloads"]}
        workload_results: dict[str, Any] = {}
        protocol = spec["protocol"]
        variant_ids = [row["id"] for row in variants]
        for workload_index, workload_id in enumerate(spec["workloads"]):
            ref = reference_by_id[workload_id]
            manifest_row = manifest_by_id[workload_id]
            calls: dict[str, Any] = {}
            output_buffers: dict[str, Any] = {}
            outputs: dict[str, list[float]] = {}
            output_digests: dict[str, str] = {}
            native_metrics: dict[str, dict[str, int]] = {}
            for variant in variants:
                variant_id = variant["id"]
                row = builds[variant_id]["workloads"][workload_id]
                control_row = builds[control_id]["workloads"][workload_id]
                for field in ("source_sha256", "benchmark_helper_sha256", "dataset_sha256", "expected_output_sha256"):
                    if row[field] != control_row[field]:
                        raise ValueError(f"{workload_id}: variants differ in shared input identity {field}")
                if row["source_sha256"] != _sha256(
                    (checkouts[control_id] / "benchmarks" / manifest_row["s3_source"]).read_bytes()
                    .replace(b"\r\n", b"\n").replace(b"\r", b"\n")
                ):
                    raise ValueError(f"{workload_id}: source hash does not match the control checkout")
                artifact = output_dir / "artifacts" / variant_id / row["binary"]["path"]
                binary_bytes = artifact.read_bytes()
                if len(binary_bytes) != row["binary"]["bytes"] or _sha256(binary_bytes) != row["binary"]["sha256"]:
                    raise ValueError(f"{workload_id}/{variant_id}: binary artifact hash mismatch")
                library = ctypes.CDLL(str(artifact))
                output = (ctypes.c_double * len(benchmark.OUTPUT_KEYS[workload_id]))()
                call = benchmark._make_call(library, ref, output)
                status = call()
                values = list(output)
                if status != 0:
                    raise RuntimeError(f"{workload_id}/{variant_id}: native status {status}")
                benchmark._check_output(values, ref["expected_output"], workload_id)
                digest = _sha256(benchmark._json_bytes([round(value, 10) for value in values]))
                calls[variant_id] = call
                output_buffers[variant_id] = output
                outputs[variant_id] = values
                output_digests[variant_id] = digest
                native_metrics[variant_id] = _inspect_binary(artifact, WORKLOADS[workload_id])
            if any(outputs[variant_id] != outputs[control_id] for variant_id in variant_ids[1:]):
                raise ValueError(f"{workload_id}: exact native outputs differ between variants")

            for _ in range(protocol["warmups"]):
                for variant_id in variant_ids:
                    if calls[variant_id]() != 0:
                        raise RuntimeError(f"{workload_id}/{variant_id}: warmup failed")
                    if list(output_buffers[variant_id]) != outputs[variant_id]:
                        raise ValueError(f"{workload_id}/{variant_id}: output changed during warmup")
            timings = {variant_id: [] for variant_id in variant_ids}
            orders = []
            for sample_index in range(protocol["samples"]):
                order = sample_order(variant_ids, sample_index)
                orders.append(order)
                for variant_id in order:
                    duration = benchmark._measure(calls[variant_id], protocol["iterations_per_sample"])
                    if not math.isfinite(duration) or duration <= 0:
                        raise ValueError(f"{workload_id}/{variant_id}: invalid timing sample")
                    timings[variant_id].append(duration)
            for variant_id in variant_ids:
                if calls[variant_id]() != 0 or list(output_buffers[variant_id]) != outputs[variant_id]:
                    raise ValueError(f"{workload_id}/{variant_id}: output changed after timing")
            timing_rows = {}
            for variant_id in variant_ids:
                samples = timings[variant_id]
                timing_rows[variant_id] = {
                    "raw_ns_per_call": samples,
                    "median_ns_per_call": statistics.median(samples),
                    "mean_ns_per_call": statistics.fmean(samples),
                    "sample_count": len(samples),
                }
            comparisons = {
                variant_id: _paired_summary(
                    timings[control_id], timings[variant_id],
                    seed=protocol["seed"] + workload_index * 101 + index,
                    resamples=protocol["bootstrap_resamples"],
                )
                for index, variant_id in enumerate(variant_ids[1:], start=1)
            }
            workload_results[workload_id] = {
                "input": {
                    "source_sha256": builds[control_id]["workloads"][workload_id]["source_sha256"],
                    "dataset_sha256": manifest_row["dataset_sha256"],
                    "expected_output_sha256": manifest_row["expected_output_sha256"],
                },
                "correctness": {
                    "reference": {variant_id: "PASS" for variant_id in variant_ids},
                    "exact_cross_variant_output_equal": True,
                    "output_sha256": output_digests,
                },
                "native_metrics": native_metrics,
                "timing": {
                    "class": "CHARACTERIZATION_ONLY",
                    "native_speedup_claim": False,
                    "protocol": protocol,
                    "sample_order": orders,
                    "variants": timing_rows,
                    "control_over_candidate": comparisons,
                },
            }
        elapsed = time.monotonic() - started
        result = {
            "schema_version": "s3.candidate-matrix-result.v1",
            "experiment_id": spec["experiment_id"],
            "status": "PASS",
            "classification": "INDEPENDENT_BUILD_CORRECTNESS_STRUCTURE_AND_PAIRED_TIMING_CHARACTERIZATION",
            "provenance": {
                "lab_head": lab_head,
                "lab_tree": lab_tree,
                "lab_worktree_clean": True,
                "spec_sha256": _sha256(spec_bytes),
                "source_repository": spec["source_identity"],
                "variants": {
                    variant["id"]: {
                        "revision": variant["revision"],
                        "tree": builds[variant["id"]]["source_tree"],
                        "configuration": variant,
                        "binary_artifacts": {
                            workload_id: builds[variant["id"]]["workloads"][workload_id]["binary"]
                            for workload_id in spec["workloads"]
                        },
                    }
                    for variant in variants
                },
                "target": "Linux x86-64",
            },
            "protocol": {
                **protocol,
                "timing_class": "CHARACTERIZATION_ONLY",
                "native_speedup_claim": False,
                "timed_region": "same-process scalar C ABI; compilation/setup excluded; ctypes dispatch included equally",
            },
            "workloads": workload_results,
            "elapsed_seconds": round(elapsed, 6),
        }
        payload = _json_bytes(result)
        _write_once(output_dir / "candidate-matrix-result.json", payload)
        return result
    except Exception as exc:
        failure = {
            "schema_version": "s3.candidate-matrix-result.v1",
            "experiment_id": spec["experiment_id"],
            "status": "FAIL",
            "error": f"{type(exc).__name__}: {exc}",
            "spec_sha256": _sha256(spec_bytes),
            "lab_head": lab_head,
            "started_at_utc": started_at,
            "elapsed_seconds": round(time.monotonic() - started, 6),
        }
        _write_once(output_dir / "candidate-matrix-failure.json", _json_bytes(failure))
        raise RuntimeError(f"candidate matrix failed; evidence preserved at {output_dir}: {failure['error']}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", type=Path)
    parser.add_argument("--work-root", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--timeout-seconds", type=int, default=900)
    parser.add_argument("--_worker-checkout", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--_worker-variant-json", help=argparse.SUPPRESS)
    parser.add_argument("--_worker-workloads-json", help=argparse.SUPPRESS)
    parser.add_argument("--_worker-output", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--_worker-result", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args._worker_checkout is not None:
        if not all((args._worker_variant_json, args._worker_workloads_json, args._worker_output, args._worker_result)):
            parser.error("incomplete internal build-worker arguments")
        return _worker_main(args)
    if args.spec is None or args.work_root is None or args.output_dir is None:
        parser.error("--spec, --work-root, and --output-dir are required")
    result = execute_matrix_spec(
        spec_path=args.spec,
        work_root=args.work_root,
        output_dir=args.output_dir,
        timeout_seconds=args.timeout_seconds,
    )
    print(f"CANDIDATE_MATRIX={result['status']} variants={len(result['provenance']['variants'])} workloads={len(result['workloads'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
