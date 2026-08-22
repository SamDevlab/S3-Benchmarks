"""Interleaved P1 stability runner with persistent sample-level evidence."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import statistics
import subprocess
import sys
import time
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from benchmarks.jsmn.harness.benchmark import run_native_executable_sample  # noqa: E402
from benchmarks.rc1.statistics import bootstrap_median_ci, classify_paired_delta, robust_stats  # noqa: E402
from tools.artifacts import git_head, require_provenance  # noqa: E402


EXPECTED_SHAS = {
    "H0": "85541b782571c80d4857d013d1fb25b4997c1eb9",
    "H1": "631b51e70562a33183ac14d0be5bbe2ddd140779",
    "H2": "5dd6844607ba3a2d5830ed836fb9026eed86d0fb",
    "H3": "2316300f7f6c119004009b713849cae1c101d1a5",
    "H4": "e23b092bec100cedc520841a7dd0f4488090b6a1",
    "H5": "9b39c7070d7bfa23d709c2128eb0b0bbef164177",
}
FIXTURES = (
    "tiny_04_arr",
    "tiny_03_pair",
    "tiny_02_empty_arr",
    "tiny_05_string",
    "tiny_06_bool_null",
    "tiny_01_empty_obj",
)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _render_c(text: str, iterations: int) -> str:
    values = ", ".join(str(value) for value in text.encode("ascii"))
    return f"""/* Immutable campaign C control. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include \"jsmn.h\"
#define MAX_TOKENS 32
static const char input_buffer[] = {{{values}}};
static const size_t input_len = {len(text.encode('ascii'))};
int main(int argc, char **argv) {{
    long loops = {iterations};
    for (int i = 1; i + 1 < argc; ++i) if (!strcmp(argv[i], \"--loop\")) loops = atol(argv[i + 1]);
    if (loops <= 0) loops = 1;
    int accum = 0;
    for (long i = 0; i < loops; ++i) {{
        jsmn_parser parser; jsmntok_t tokens[MAX_TOKENS]; jsmn_init(&parser);
        int result = jsmn_parse(&parser, input_buffer, input_len, tokens, MAX_TOKENS);
        int value = result >= 0 ? result : -result; accum += value; if (accum >= 200) accum -= 200;
    }}
    printf(\"program returned: %d\\n\", accum); return 0;
}}
"""


def _compile_controls(control_root: Path, fixture_root: Path, parses: int, *, reuse: bool) -> dict[str, Any]:
    manifest_path = control_root / "control-manifest.json"
    if reuse:
        if not manifest_path.is_file():
            raise RuntimeError(f"missing shared control manifest: {manifest_path}")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("parses_per_sample") != parses:
            raise RuntimeError("shared control parse count mismatch")
        for record in manifest["fixtures"]:
            for variant in record["variants"].values():
                if _sha256_file(Path(variant["binary"])) != variant["binary_sha256"]:
                    raise RuntimeError("shared control binary digest mismatch")
        return manifest
    control_root.mkdir(parents=True, exist_ok=False)
    compiler = shutil.which("gcc")
    if compiler is None:
        raise RuntimeError("gcc unavailable for shared control")
    fixtures: list[dict[str, Any]] = []
    for fixture_id in FIXTURES:
        text_path = fixture_root / f"{fixture_id}.json"
        text = text_path.read_text(encoding="utf-8")
        fixture_dir = control_root / fixture_id
        fixture_dir.mkdir()
        source_path = fixture_dir / "control.c"
        source_path.write_text(_render_c(text, parses), encoding="utf-8", newline="\n")
        variants: dict[str, Any] = {}
        for optimization in ("O0", "O2", "O3"):
            binary = fixture_dir / f"control-{optimization}"
            command = [compiler, f"-{optimization}", "-std=c99", "-I", str(BASE_DIR / "benchmarks/jsmn/upstream"), str(source_path), "-o", str(binary)]
            subprocess.run(command, check=True, capture_output=True, text=True)
            variants[optimization] = {
                "binary": str(binary.resolve()),
                "binary_sha256": _sha256_file(binary),
                "source_sha256": _sha256_file(source_path),
                "command": command,
            }
        fixtures.append({"fixture": fixture_id, "input_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "variants": variants})
    manifest = {
        "schema": "s3.rc1.shared-c-control.v1",
        "compiler": compiler,
        "compiler_version": subprocess.run([compiler, "--version"], check=True, capture_output=True, text=True).stdout.splitlines()[0],
        "parses_per_sample": parses,
        "fixtures": fixtures,
    }
    _json(manifest_path, manifest)
    return manifest


def _host_preflight(output: Path, samples: int = 8) -> dict[str, Any]:
    observations: list[dict[str, Any]] = []
    for index in range(samples):
        uptime = subprocess.run(["uptime"], capture_output=True, text=True, check=False).stdout.strip()
        free = subprocess.run(["free", "-m"], capture_output=True, text=True, check=False).stdout.strip()
        active = subprocess.run(["pgrep", "-af", "(runner|p1_stability|benchmarks)"], capture_output=True, text=True, check=False).stdout.splitlines()
        active = [line for line in active if str(os.getpid()) not in line]
        observations.append({"index": index + 1, "timestamp": datetime.now(timezone.utc).isoformat(), "uptime": uptime, "free_m": free, "active_benchmark_processes": active})
        if index + 1 < samples:
            time.sleep(5)
    stable_memory = len({item["free_m"] for item in observations}) > 0
    no_competitors = all(not item["active_benchmark_processes"] for item in observations)
    result = {"samples": observations, "host_ready": stable_memory and no_competitors, "taskset": shutil.which("taskset")}
    _json(output, result)
    return result


def _compile_checkpoint(checkpoint: str, root: Path, output: Path, control: str, parses: int, benchmark_sha: str, fixture_root: Path) -> dict[str, Any]:
    if output.exists():
        raise RuntimeError(f"refusing to reuse checkpoint artifact root: {output}")
    command = [
        sys.executable, str(BASE_DIR / "tools" / "compile_s3_checkpoint.py"),
        "--s3-root", str(root), "--s3-sha", EXPECTED_SHAS[checkpoint], "--benchmark-sha", benchmark_sha,
        "--checkpoint", checkpoint, "--output-dir", str(output), "--template", str(BASE_DIR / "benchmarks/jsmn/s3/jsmn_demo.s3"),
        "--parses", str(parses),
    ]
    for fixture_id in FIXTURES:
        command.extend(["--fixture", str((fixture_root / f"{fixture_id}.json").resolve())])
    environment = os.environ.copy()
    environment["S3_REPO"] = str(root.resolve())
    subprocess.run(command, cwd=str(BASE_DIR), env=environment, check=True, capture_output=True, text=True)
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    if manifest["provenance"]["s3_commit"] != EXPECTED_SHAS[checkpoint]:
        raise RuntimeError(f"compiled checkpoint provenance mismatch: {checkpoint}")
    return manifest


def _sample_row(*, run_id: str, block_id: str, sequence_index: int, checkpoint: str, variant: str, fixture: str, elapsed_ns: int, parses: int, role: str, affinity: str, measurement_index: int) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "block_id": block_id,
        "sequence_index": sequence_index,
        "measurement_index": measurement_index,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "timestamp_ns": time.time_ns(),
        "checkpoint": checkpoint,
        "variant": variant,
        "fixture": fixture,
        "raw_elapsed_ns": elapsed_ns,
        "parses": parses,
        "ns_per_parse": elapsed_ns / parses,
        "cpu_affinity": affinity,
        "control_candidate_role": role,
    }


def _execute(binary: Path, parses: int) -> tuple[int, int]:
    elapsed, ok, result = run_native_executable_sample(binary, parses)
    if not ok:
        raise RuntimeError(f"native execution failed: {binary}")
    return elapsed, result


def _schedule(checkpoints: list[str], block: int) -> list[tuple[str, str, str]]:
    if checkpoints == ["H4", "H5"]:
        base = [("C", "O2", "control"), ("H4", "O1", "candidate"), ("H5", "O1", "candidate"), ("H5", "O1", "candidate"), ("H4", "O1", "candidate"), ("C", "O2", "control")]
    else:
        base = [("C", "O2", "control"), ("H0", "O1", "candidate"), ("H3", "O1", "candidate"), ("H5", "O1", "candidate"), ("H2", "O1", "candidate"), ("H4", "O1", "candidate"), ("H1", "O1", "candidate"), ("C", "O2", "control")]
    shift = block % len(base)
    return base[shift:] + base[:shift]


def _paired_delta(rows: list[dict[str, Any]], left: str, right: str) -> dict[str, Any]:
    # Each checkpoint follows the same rotated schedule, so the stable pair is
    # the fixture-local measurement ordinal.  A global ordinal cannot be used:
    # H4 and H5 occupy different positions inside every interleaved block.
    by_key: dict[tuple[str, int], dict[str, float]] = {}
    for row in rows:
        if row["checkpoint"] not in {left, right} or row["variant"] != "O1":
            continue
        by_key.setdefault((row["fixture"], row["measurement_index"]), {})[row["checkpoint"]] = row["ns_per_parse"]
    deltas = [(value[right] / value[left] - 1.0) * 100.0 for value in by_key.values() if left in value and right in value]
    if not deltas:
        return {"count": 0, "median_percent": None, "ci95_percent": None, "classification": "INCONCLUSIVE"}
    ci = bootstrap_median_ci(deltas, seed=17)
    return {"count": len(deltas), "median_percent": statistics.median(deltas), "ci95_percent": ci, "classification": "PENDING_CONTROL_GATE"}


def run_campaign(args: argparse.Namespace) -> dict[str, Any]:
    checkpoints = args.checkpoints
    if checkpoints not in (["H4", "H5"], list(EXPECTED_SHAS)):
        raise SystemExit("checkpoints must be exactly H4 H5 or H0 H1 H2 H3 H4 H5")
    roots = {key: Path(value).resolve() for key, value in (item.split("=", 1) for item in args.s3_root)}
    if set(roots) != set(checkpoints):
        raise SystemExit("one --s3-root CHECKPOINT=PATH is required for each checkpoint")
    for checkpoint in checkpoints:
        require_provenance(s3_repo=roots[checkpoint], requested_s3_sha=EXPECTED_SHAS[checkpoint], benchmark_repo=BASE_DIR, requested_benchmark_sha=args.benchmark_sha)
    fixture_root = BASE_DIR / "benchmarks" / "jsmn" / "corpus" / "tiny"
    run_root = args.artifact_root.resolve()
    if run_root.exists():
        raise RuntimeError(f"refusing to reuse campaign root: {run_root}")
    run_root.mkdir(parents=True)
    preflight = _host_preflight(run_root / "host-preflight.json")
    if not preflight["host_ready"]:
        raise SystemExit("STOP_TIMING_UNSTABLE_HOST")
    control = _compile_controls(args.control_root.resolve(), fixture_root, args.parses, reuse=args.reuse_control)
    artifacts: dict[str, Any] = {}
    for checkpoint in checkpoints:
        artifacts[checkpoint] = _compile_checkpoint(checkpoint, roots[checkpoint], run_root / checkpoint, "O1", args.parses, args.benchmark_sha, fixture_root)
    binaries: dict[tuple[str, str, str], Path] = {}
    for record in control["fixtures"]:
        for optimization, variant in record["variants"].items():
            binaries[("C", record["fixture"], optimization)] = Path(variant["binary"])
    for checkpoint, manifest in artifacts.items():
        for record in manifest["records"]:
            for optimization, variant in record["variants"].items():
                binaries[(checkpoint, record["fixture"], optimization)] = Path(variant["executable"])
    correctness: list[dict[str, Any]] = []
    for fixture_id in FIXTURES:
        c_elapsed, c_result = _execute(binaries[("C", fixture_id, "O2")], args.parses)
        row = {"fixture": fixture_id, "control_result": c_result, "checkpoints": {}}
        for checkpoint in checkpoints:
            values = {}
            for optimization in ("O0", "O1"):
                elapsed, result = _execute(binaries[(checkpoint, fixture_id, optimization)], args.parses)
                values[optimization] = {"result": result, "elapsed_ns": elapsed}
                if result != c_result:
                    raise RuntimeError(f"correctness mismatch {checkpoint}/{fixture_id}/{optimization}: {result} != {c_result}")
            row["checkpoints"][checkpoint] = values
        correctness.append(row)
    rows: list[dict[str, Any]] = []
    measurement_counts: dict[tuple[str, str, str], int] = {}
    sequence_index = 0
    total_blocks = args.repetitions // 2 if checkpoints == ["H4", "H5"] else args.repetitions
    if args.repetitions % 2:
        raise SystemExit("repetitions must be even for ABBA block schedules")
    for fixture_id in FIXTURES:
        for warmup in range(args.warmups):
            for checkpoint, optimization, _role in _schedule(checkpoints, warmup):
                binary_key = ("C" if checkpoint == "C" else checkpoint, fixture_id, optimization)
                _execute(binaries[binary_key], args.parses)
        for block in range(total_blocks):
            for checkpoint, optimization, role in _schedule(checkpoints, block):
                sequence_index += 1
                key = ("C" if checkpoint == "C" else checkpoint, fixture_id, optimization)
                elapsed, _result = _execute(binaries[key], args.parses)
                count_key = (checkpoint, fixture_id, optimization)
                measurement_index = measurement_counts.get(count_key, 0)
                measurement_counts[count_key] = measurement_index + 1
                rows.append(_sample_row(run_id=args.run_id, block_id=f"block-{block:03d}", sequence_index=sequence_index, checkpoint=checkpoint, variant=optimization, fixture=fixture_id, elapsed_ns=elapsed, parses=args.parses, role=role, affinity=args.cpu_affinity, measurement_index=measurement_index))
    _json(run_root / "samples.json", rows)
    with (run_root / "samples.csv").open("w", newline="", encoding="utf-8") as stream:
        fields = list(rows[0])
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    grouped: dict[tuple[str, str, str], list[float]] = {}
    for row in rows:
        grouped.setdefault((row["checkpoint"], row["fixture"], row["variant"]), []).append(row["ns_per_parse"])
    summaries = [{"checkpoint": key[0], "fixture": key[1], "variant": key[2], **robust_stats(values)} for key, values in sorted(grouped.items())]
    controls_by_block: dict[str, list[float]] = {}
    for row in rows:
        if row["checkpoint"] == "C":
            controls_by_block.setdefault(row["block_id"], []).append(row["ns_per_parse"])
    block_controls = [statistics.median(values) for _block, values in sorted(controls_by_block.items())]
    control_drift = {
        "block_values_ns_per_parse": block_controls,
        "start_median": statistics.median(block_controls[: max(1, len(block_controls) // 3)]),
        "middle_median": statistics.median(block_controls[max(1, len(block_controls) // 3): max(2, 2 * len(block_controls) // 3)]),
        "end_median": statistics.median(block_controls[max(2, 2 * len(block_controls) // 3):]),
        "relative_range": max(block_controls) / min(block_controls) - 1.0,
    }
    control_drift["classification"] = "STABLE" if control_drift["relative_range"] <= 0.05 else "HIGH"
    paired = _paired_delta(rows, "H4", "H5") if set(("H4", "H5")) <= set(checkpoints) else None
    if paired is not None:
        paired["classification"] = classify_paired_delta(paired["median_percent"], paired["ci95_percent"], control_drift["classification"] == "STABLE")
    summary = {
        "schema": "s3.rc1.p1-v2.summary.v1",
        "run_id": args.run_id,
        "mode": "primary" if checkpoints == ["H4", "H5"] else "history",
        "provenance": {"benchmark_sha": args.benchmark_sha, "s3_shas": {key: EXPECTED_SHAS[key] for key in checkpoints}},
        "host_ready": preflight["host_ready"],
        "cpu_affinity": args.cpu_affinity,
        "sample_level_data_available": "YES",
        "correctness": "PASS",
        "control_drift": control_drift,
        "paired_h4_h5": paired,
        "summaries": summaries,
        "raw_samples": "samples.json",
        "control_manifest": str((args.control_root / "control-manifest.json").resolve()),
        "protocol": {"warmups": args.warmups, "repetitions": args.repetitions, "parses_per_sample": args.parses, "schedule": "interleaved rotating blocks; C H4 H5 H5 H4 C or rotating C H0 H3 H5 H2 H4 H1 C", "process_startup": "AMORTIZED_NOT_SUBTRACTED"},
    }
    _json(run_root / "summary.json", summary)
    _json(run_root / "correctness.json", correctness)
    _json(run_root / "protocol.json", summary["protocol"])
    print(json.dumps({"run_id": args.run_id, "status": "PASS", "control_drift": control_drift["classification"], "sample_level_data_available": "YES", "paired": paired}, sort_keys=True))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-root", action="append", required=True, metavar="CHECKPOINT=PATH")
    parser.add_argument("--checkpoints", nargs="+", required=True)
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--control-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--reuse-control", action="store_true")
    parser.add_argument("--warmups", type=int, default=5)
    parser.add_argument("--repetitions", type=int, default=30)
    parser.add_argument("--parses", type=int, default=10000)
    parser.add_argument("--cpu-affinity", default="taskset -c 0")
    args = parser.parse_args()
    run_campaign(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
