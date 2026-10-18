#!/usr/bin/env python3
"""Paired, pinned BASE/CANDIDATE run for the Native Pure/Controlled R2 study."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

R2_DIR = Path(__file__).resolve().parent
V1_DIR = R2_DIR.parent / "native-pure-controlled-v1"
sys.path.insert(0, str(V1_DIR))
import campaign as v1  # noqa: E402
from fixture import SEED, SIZE_COUNTS, expected_outputs, workload_counts, write_expected, write_fixture  # noqa: E402

WORKLOADS = ("energy_series_aggregation", "agent_energy_residual")
SIZES = ("small", "medium", "full")
MODES = {
    "PURE_EXPERIMENTAL": v1.S3_MODES["PURE_EXPERIMENTAL"],
    "PER_INSTRUCTION": v1.S3_MODES["PER_INSTRUCTION"],
}
ALLOCATABLE = r"(?:rbx|r12|r13|r14|r15|rdi|rsi|rdx|rcx|r8|r9)"


def function_assembly_shape(assembly_path: Path, function_name: str) -> dict[str, Any]:
    lines = assembly_path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index(f"{function_name}:")
        end = next(
            i for i in range(start + 1, len(lines))
            if lines[i].startswith(f".size {function_name},")
        )
    except (ValueError, StopIteration) as error:
        raise ValueError(f"could not isolate native function {function_name!r}") from error
    body = lines[start:end]
    instruction_lines = [
        line for line in body if re.match(r"^\s+[a-z][a-z0-9]*(?:\s|$)", line)
    ]
    scratch_load = re.compile(r"^\s+mov \w+, qword ptr \[r10 \+ \w+ \* 8\]$")
    direct_load = re.compile(
        rf"^\s+mov {ALLOCATABLE}, qword ptr \[{ALLOCATABLE} \+ {ALLOCATABLE} \* 8\]$"
    )
    resident_base_load = re.compile(
        rf"^\s+mov {ALLOCATABLE}, qword ptr \[{ALLOCATABLE} \+ (?:{ALLOCATABLE}|rax) \* 8\]$"
    )
    scaled_load = re.compile(r"^\s+mov \w+, qword ptr \[[^\]]+\* 8\]$")
    load_lines = [line for line in body if scaled_load.match(line)]
    return {
        "static_assembly_instruction_lines": len(instruction_lines),
        "scaled_qword_loads": len(load_lines),
        "scratch_scaled_qword_loads": sum(bool(scratch_load.match(line)) for line in load_lines),
        "resident_register_scaled_qword_loads": sum(bool(direct_load.match(line)) for line in load_lines),
        "resident_base_scaled_qword_loads": sum(bool(resident_base_load.match(line)) for line in load_lines),
        "scaled_qword_load_examples": load_lines[:8],
    }


def tree_sha256(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
        digest.update(b"\0")
    return digest.hexdigest()


def orientation_schedule(samples: int, seed: int) -> list[bool]:
    """Return an exactly balanced BASE-first schedule (within one for odd n)."""
    if samples < 1:
        raise ValueError("samples must be positive")
    order = [True] * ((samples + 1) // 2) + [False] * (samples // 2)
    random.Random(seed).shuffle(order)
    return order


def artifact_identity(row: dict[str, Any]) -> tuple[str, str, str]:
    return row["revision_label"], row["profile"].split("/", 1)[0], row["workload"]


def paired_metrics(base: list[float], candidate: list[float], seed: int) -> dict[str, Any]:
    if len(base) != len(candidate) or not base:
        raise ValueError("paired BASE/CANDIDATE samples must have equal nonzero lengths")
    ratio = v1.paired_ratio(candidate, base, seed)
    differences = [new - old for old, new in zip(base, candidate, strict=True)]
    rng = random.Random(seed ^ 0xC0DE6E)
    boot = [
        statistics.median(differences[rng.randrange(len(differences))] for _ in differences)
        for _ in range(10000)
    ]
    return {
        **ratio,
        "median_delta_ns_per_call": statistics.median(differences),
        "bootstrap_95ci_median_delta_ns_per_call": [
            v1.percentile(boot, 0.025), v1.percentile(boot, 0.975)
        ],
    }


def git_revision(repo: Path, expression: str) -> str | None:
    if not (repo / ".git").exists():
        return None
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", expression], text=True
    ).strip()


def build_worker(args: argparse.Namespace) -> int:
    repo = Path(args.compiler_repo).resolve()
    if not repo.is_dir():
        raise SystemExit(f"compiler source directory does not exist: {repo}")
    head = git_revision(repo, "HEAD")
    if head is not None and head != args.compiler_revision:
        raise SystemExit(f"compiler HEAD mismatch: expected {args.compiler_revision}, got {head}")
    parent = git_revision(repo, "HEAD^")
    if parent is not None and parent != args.compiler_parent:
        raise SystemExit(f"compiler parent mismatch: expected {args.compiler_parent}, got {parent}")

    sys.path.insert(0, str(repo))
    from bootstrap.s3.assembly import AssemblyOpcode
    from bootstrap.s3.pipeline import compile_source

    cc = v1.shutil.which("gcc") or v1.shutil.which("cc")
    if not cc:
        raise SystemExit("GCC/cc is required to assemble pinned compiler output")
    build_dir = Path(args.build_dir).resolve()
    build_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for workload in WORKLOADS:
        source_row = next(item for item in v1.MANIFEST["workloads"] if item["id"] == workload)
        source_path = V1_DIR / source_row["source"]
        compiled = compile_source(source_path.read_text(encoding="utf-8"), "O1")
        _, assembly_program = compiled.require_ordinary_artifacts()
        tsload_sites = {
            function.name: sum(
                instruction.opcode is AssemblyOpcode.TSLOAD
                for instruction in function.instructions
            )
            for function in assembly_program.functions
        }
        for mode_name, mode_value in MODES.items():
            artifact = v1.build_s3_artifact(
                repo,
                workload,
                source_path,
                mode_name,
                mode_value,
                "O1",
                build_dir,
                cc,
                args.compiler_revision,
            )
            artifact["artifact_id"] = f"{args.label.lower()}-{artifact['artifact_id']}"
            artifact["revision_label"] = args.label
            artifact["workload"] = workload
            artifact["tsload_sites_by_function"] = tsload_sites
            artifact["native_function_shape"] = function_assembly_shape(
                Path(artifact["path"]).with_suffix(".s"), workload
            )
            rows.append(artifact)
    Path(args.artifacts_json).write_text(
        json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0


def perf_counter_status() -> dict[str, Any]:
    value = None
    setting = Path("/proc/sys/kernel/perf_event_paranoid")
    if setting.exists():
        try:
            value = int(setting.read_text(encoding="utf-8").strip())
        except ValueError:
            value = None
    perf = v1.shutil.which("perf")
    if not perf:
        return {"status": "UNAVAILABLE", "reason": "perf_not_installed", "perf_event_paranoid": value}
    result = subprocess.run(
        [perf, "stat", "-e", "cycles,instructions", "true"],
        text=True,
        capture_output=True,
        timeout=10,
        check=False,
    )
    return {
        "status": "AVAILABLE" if result.returncode == 0 else "UNAVAILABLE",
        "reason": "accessible" if result.returncode == 0 else "permission_or_event_denied",
        "perf_event_paranoid": value,
    }


def invoke_sample(
    runner: Path,
    taskset: str,
    cpu: int,
    artifact: dict[str, Any],
    workload: str,
    fixture_path: Path,
    iterations: int,
    size: str,
) -> tuple[dict[str, Any], int]:
    command = [
        taskset, "-c", str(cpu), str(runner), artifact["path"], workload,
        str(fixture_path), str(iterations), size,
    ]
    return v1.run_process(command)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-repo")
    parser.add_argument("--candidate-repo")
    parser.add_argument("--baseline-revision")
    parser.add_argument("--candidate-revision")
    parser.add_argument("--baseline-parent")
    parser.add_argument("--candidate-parent")
    parser.add_argument("--baseline-archive-sha256")
    parser.add_argument("--candidate-archive-sha256")
    parser.add_argument("--v1-inputs-archive-sha256")
    parser.add_argument("--output", default="/dev/shm/s3-native-r2-paired-results")
    parser.add_argument("--samples", type=int, default=41)
    parser.add_argument("--warmups", type=int, default=7)
    parser.add_argument("--iterations", type=int, default=1)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--order-seed", type=int)
    parser.add_argument("--_build-worker", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--label", choices=("BASELINE", "CANDIDATE"), help=argparse.SUPPRESS)
    parser.add_argument("--compiler-repo", help=argparse.SUPPRESS)
    parser.add_argument("--compiler-revision", help=argparse.SUPPRESS)
    parser.add_argument("--compiler-parent", help=argparse.SUPPRESS)
    parser.add_argument("--build-dir", help=argparse.SUPPRESS)
    parser.add_argument("--artifacts-json", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args._build_worker:
        return build_worker(args)
    required = (
        args.baseline_repo, args.candidate_repo, args.baseline_revision,
        args.candidate_revision, args.baseline_parent, args.candidate_parent,
        args.baseline_archive_sha256, args.candidate_archive_sha256,
        args.v1_inputs_archive_sha256,
    )
    if any(value is None for value in required):
        parser.error("both compiler revisions, parents, source directories, and archive hashes are required")
    if args.samples < 15 or args.warmups < 0 or args.iterations < 1:
        parser.error("samples must be >= 15, warmups non-negative, and iterations positive")
    if not args.output.startswith("/dev/shm/"):
        parser.error("generated benchmark artifacts must be written under /dev/shm")

    baseline_repo = Path(args.baseline_repo).resolve()
    candidate_repo = Path(args.candidate_repo).resolve()
    for repo, revision, parent in (
        (baseline_repo, args.baseline_revision, args.baseline_parent),
        (candidate_repo, args.candidate_revision, args.candidate_parent),
    ):
        if not repo.is_dir():
            raise SystemExit(f"compiler source directory does not exist: {repo}")
        head, actual_parent = git_revision(repo, "HEAD"), git_revision(repo, "HEAD^")
        if head is not None and (head != revision or actual_parent != parent):
            raise SystemExit(f"revision or parent mismatch for compiler source: {repo}")

    output = Path(args.output)
    if output.exists() and any(output.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty output directory: {output}")
    output.mkdir(parents=True, exist_ok=True)
    build_root = output / "build"
    build_root.mkdir()
    fixture_path = output / "runtime-fixture-v1.bin"
    fixture_sha = write_fixture(fixture_path, args.seed)
    expected_path = output / "expected-v1.json"
    write_expected(expected_path, args.seed)
    expected = {size: expected_outputs(args.seed, size) for size in SIZES}

    build_rows: list[dict[str, Any]] = []
    for label, repo, revision, parent in (
        ("BASELINE", baseline_repo, args.baseline_revision, args.baseline_parent),
        ("CANDIDATE", candidate_repo, args.candidate_revision, args.candidate_parent),
    ):
        artifacts_json = output / f"builds-{label.lower()}.json"
        command = [
            sys.executable, str(Path(__file__).resolve()), "--_build-worker",
            "--label", label, "--compiler-repo", str(repo),
            "--compiler-revision", revision, "--compiler-parent", parent,
            "--build-dir", str(build_root / label.lower()),
            "--artifacts-json", str(artifacts_json),
        ]
        subprocess.run(command, check=True, timeout=600)
        build_rows.extend(json.loads(artifacts_json.read_text(encoding="utf-8")))

    artifact_by_identity = {
        artifact_identity(row): row for row in build_rows
    }
    if len(artifact_by_identity) != len(build_rows):
        raise SystemExit("build artifacts do not have unique revision/profile/workload identities")

    runner_source = V1_DIR / "reference" / "kernel_runner.c"
    runner = build_root / "kernel_runner"
    cc = v1.shutil.which("gcc") or v1.shutil.which("cc")
    taskset = v1.shutil.which("taskset")
    if not cc or not taskset:
        raise SystemExit("GCC/cc and taskset are required by the pinned Linux measurement protocol")
    harness_seconds = v1.timed_command([cc, "-O2", "-std=c11", "-Wall", "-Wextra", str(runner_source), "-ldl", "-o", str(runner)])
    host = v1.host_metadata()
    cpu = 0 if 0 in host["affinity_cpus"] else min(host["affinity_cpus"])
    perf_status = perf_counter_status()

    variants = [
        (revision, mode, workload, size)
        for revision in ("BASELINE", "CANDIDATE")
        for mode in MODES
        for workload in WORKLOADS
        for size in SIZES
    ]
    def artifact_for(revision: str, mode: str, workload: str) -> dict[str, Any]:
        return artifact_by_identity[(revision, mode, workload)]

    # Correctness and the invalid-output gate run before any timed observations.
    for revision, mode, workload, size in variants:
        artifact = artifact_for(revision, mode, workload)
        result, _ = invoke_sample(runner, taskset, cpu, artifact, workload, fixture_path, 1, size)
        v1.assert_parity(result["outputs"], expected[size][workload], workload, f"{revision}/{mode}/{size}")
        if result["status"] != 0:
            raise RuntimeError(f"nonzero correctness-call status: {revision}/{mode}/{workload}/{size}")
    invalid_rows = []
    for row in build_rows:
        status = v1.verify_s3_invalid_output(Path(row["path"]), row["workload"], args.seed)
        if status != 2:
            raise RuntimeError(f"invalid-output probe failed for {row['artifact_id']}: status={status}")
        invalid_rows.append({"artifact_id": row["artifact_id"], "short_output_status": status, "result": "PASS"})

    iterations = {"small": args.iterations * 8, "medium": args.iterations * 2, "full": args.iterations}
    order_seed = args.seed if args.order_seed is None else args.order_seed
    rng = random.Random(order_seed ^ 0x52D2)
    orientation = {
        (mode, workload, size): orientation_schedule(args.samples, order_seed ^ sum(map(ord, f"{mode}|{workload}|{size}")))
        for mode in MODES for workload in WORKLOADS for size in SIZES
    }
    pairs = [(mode, workload, size) for mode in MODES for workload in WORKLOADS for size in SIZES]
    samples_path = output / "raw_samples.jsonl"
    warmups_path = output / "warmups.jsonl"
    with samples_path.open("w", encoding="utf-8", newline="\n") as measured_file, warmups_path.open("w", encoding="utf-8", newline="\n") as warmup_file:
        for phase, count, sink in (("warmup", args.warmups, warmup_file), ("measured", args.samples, measured_file)):
            for round_index in range(count):
                round_pairs = pairs.copy()
                rng.shuffle(round_pairs)
                for mode, workload, size in round_pairs:
                    key = (mode, workload, size)
                    baseline_first = (
                        orientation[key][round_index % args.samples]
                        if phase == "measured"
                        else bool(rng.getrandbits(1))
                    )
                    order = ("BASELINE", "CANDIDATE") if baseline_first else ("CANDIDATE", "BASELINE")
                    for position, revision in enumerate(order):
                        artifact = artifact_for(revision, mode, workload)
                        result, process_wall_ns = invoke_sample(
                            runner, taskset, cpu, artifact, workload, fixture_path,
                            iterations[size], size,
                        )
                        if result["status"] != 0:
                            raise RuntimeError(f"nonzero timing status: {revision}/{mode}/{workload}/{size}")
                        v1.assert_parity(result["outputs"], expected[size][workload], workload, f"{revision}/{mode}/{size}")
                        row = {
                            "phase": phase,
                            "round": round_index if phase == "measured" else None,
                            "pair_id": f"{mode}|{workload}|{size}|{round_index}",
                            "pair_order": order,
                            "position_in_pair": position,
                            "revision": revision,
                            "compiler_revision": args.baseline_revision if revision == "BASELINE" else args.candidate_revision,
                            "profile": mode,
                            "workload": workload,
                            "size": size,
                            "work_units_per_call": workload_counts(size)[workload],
                            "iterations": iterations[size],
                            "artifact_id": artifact["artifact_id"],
                            "artifact_sha256": artifact["sha256"],
                            "assembly_sha256": artifact["assembly_sha256"],
                            "source_sha256": artifact["source_sha256"],
                            "fixture_sha256": fixture_sha,
                            "elapsed_ns": result["elapsed_ns"],
                            "ns_per_call": result["ns_per_call"],
                            "ns_per_work_item": result["ns_per_call"] / workload_counts(size)[workload],
                            "checksum": result["checksum"],
                            "outputs": result["outputs"],
                            "maxrss_kib": result["maxrss_kib"],
                            "process_wall_ns": process_wall_ns,
                            "process_minus_kernel_ns": process_wall_ns - result["elapsed_ns"],
                        }
                        sink.write(json.dumps(row, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
                        sink.flush()
                if phase == "measured":
                    print(f"paired round {round_index + 1}/{args.samples}: {len(round_pairs)} cells", flush=True)

    raw = [json.loads(line) for line in samples_path.read_text(encoding="utf-8").splitlines() if line]
    groups: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
    for row in raw:
        groups.setdefault((row["revision"], row["profile"], row["workload"], row["size"]), []).append(row)
    runtime = {}
    for key, rows in groups.items():
        runtime["|".join(key)] = {
            **v1.stats([row["ns_per_call"] for row in rows], args.seed + sum(map(ord, "|".join(key)))),
            "median_ns_per_work_item": statistics.median(row["ns_per_work_item"] for row in rows),
            "median_maxrss_kib": statistics.median(row["maxrss_kib"] for row in rows),
            "artifact_sha256": rows[0]["artifact_sha256"],
            "assembly_sha256": rows[0]["assembly_sha256"],
        }
    comparisons = {}
    for mode in MODES:
        for workload in WORKLOADS:
            for size in SIZES:
                key = (mode, workload, size)
                base = {row["round"]: row["ns_per_call"] for row in raw if row["revision"] == "BASELINE" and (row["profile"], row["workload"], row["size"]) == key}
                candidate = {row["round"]: row["ns_per_call"] for row in raw if row["revision"] == "CANDIDATE" and (row["profile"], row["workload"], row["size"]) == key}
                if set(base) != set(range(args.samples)) or set(candidate) != set(range(args.samples)):
                    raise RuntimeError(f"unpaired sample set for {mode}/{workload}/{size}")
                paired = paired_metrics(
                    [base[index] for index in range(args.samples)],
                    [candidate[index] for index in range(args.samples)],
                    args.seed + sum(map(ord, f"{mode}|{workload}|{size}")),
                )
                comparisons["|".join(key)] = paired

    source_hashes = {str(path.relative_to(V1_DIR)): v1.sha256(path) for path in (V1_DIR / "sources").glob("*.s3")}
    v1_input_hashes = {
        str(path.relative_to(V1_DIR)): v1.sha256(path)
        for path in (
            V1_DIR / "campaign.py",
            V1_DIR / "fixture.py",
            V1_DIR / "manifest.json",
            V1_DIR / "reference" / "kernel_runner.c",
        )
    }
    manifest = {
        "schema": "s3-native-codegen-r2-paired/v1",
        "campaign": "S3_NATIVE_PERFORMANCE_R2_CODEGEN_ROOT_CAUSE_AND_OPTIMIZATION",
        "baseline": {
            "revision": args.baseline_revision,
            "parent": args.baseline_parent,
            "archive_sha256": args.baseline_archive_sha256,
            "source_tree_sha256": tree_sha256(baseline_repo),
        },
        "candidate": {
            "revision": args.candidate_revision,
            "parent": args.candidate_parent,
            "archive_sha256": args.candidate_archive_sha256,
            "source_tree_sha256": tree_sha256(candidate_repo),
        },
        "v1_inputs_archive_sha256": args.v1_inputs_archive_sha256,
        "v1_input_hashes": v1_input_hashes,
        "paired_runner_sha256": v1.sha256(Path(__file__).resolve()),
        "workloads": list(WORKLOADS),
        "input_sizes": list(SIZES),
        "profiles": list(MODES),
        "optimization": "O1",
        "warmups": args.warmups,
        "measured_paired_rounds": args.samples,
        "iterations_per_sample_by_size": iterations,
        "seed": args.seed,
        "order_seed": order_seed,
        "source_hashes": source_hashes,
        "fixture_sha256": fixture_sha,
        "expected_sha256": v1.sha256(expected_path),
        "kernel_runner_sha256": v1.sha256(runner),
        "kernel_runner_build_seconds": harness_seconds,
        "host": host,
        "pinning_cpu": cpu,
        "timer": "CLOCK_MONOTONIC_RAW; kernel loop only; process startup retained separately",
        "dynamic_pmu": perf_status,
        "measurement_scope": "paired BASE/CANDIDATE only; reuses V1 sources, fixture and C runner; no external-language matrix rerun",
        "no_production_or_default_changes": True,
    }
    (output / "run-manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    public_build_rows = []
    for row in build_rows:
        public_row = dict(row)
        public_row["path"] = Path(row["path"]).resolve().relative_to(output.resolve()).as_posix()
        public_build_rows.append(public_row)
    (output / "builds.json").write_text(json.dumps(public_build_rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (output / "invalid-probes.json").write_text(json.dumps(invalid_rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "result": "COMPLETE" if all(item["paired_rounds"] == args.samples for item in comparisons.values()) else "INCOMPLETE",
        "measured_pairs": sum(item["paired_rounds"] for item in comparisons.values()),
        "runtime": runtime,
        "candidate_over_baseline": comparisons,
        "artifact_builds": {row["artifact_id"]: row for row in public_build_rows},
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report = render_report(manifest, summary)
    (output / "report.md").write_text(report, encoding="utf-8")
    evidence = []
    for path in sorted(output.iterdir()):
        if path.is_file() and path.name != "evidence-index.json":
            evidence.append({"path": path.name, "bytes": path.stat().st_size, "sha256": v1.sha256(path)})
    (output / "evidence-index.json").write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"complete: {summary['measured_pairs']} paired observations; {len(build_rows)} immutable artifacts; output={output}")
    return 0


def render_report(manifest: dict[str, Any], summary: dict[str, Any]) -> str:
    lines = [
        "# Native S3 Codegen R2 — paired BASE/CANDIDATE experiment",
        "",
        f"- BASE: `{manifest['baseline']['revision']}` (parent `{manifest['baseline']['parent']}`)",
        f"- CANDIDATE: `{manifest['candidate']['revision']}` (parent `{manifest['candidate']['parent']}`)",
        f"- Host: {manifest['host']['cpu_model']}; {manifest['host']['platform']}; CPU affinity `{manifest['pinning_cpu']}`.",
        f"- Dynamic PMU counters: `{manifest['dynamic_pmu']['status']}` ({manifest['dynamic_pmu']['reason']}); no dynamic instruction counts are claimed.",
        f"- Fixture SHA-256 `{manifest['fixture_sha256']}`; {manifest['measured_paired_rounds']} paired rounds; V1 inputs and oracle reused.",
        "- A result below 1.000× means CANDIDATE was faster; interval crossing 1.000× does not establish a runtime gain.",
        "",
        "## Paired runtime (ns/call)",
        "",
        "| Workload | Size | Profile | BASE median | CANDIDATE median | Candidate/BASE | 95% paired bootstrap CI | BASE CV | Candidate CV |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for key, comparison in summary["candidate_over_baseline"].items():
        mode, workload, size = key.split("|")
        base = summary["runtime"][f"BASELINE|{mode}|{workload}|{size}"]
        candidate = summary["runtime"][f"CANDIDATE|{mode}|{workload}|{size}"]
        lo, hi = comparison["bootstrap_95ci_median_ratio"]
        lines.append(
            f"| `{workload}` | {size} | `{mode}` | {base['median_ns_per_call']:.2f} | "
            f"{candidate['median_ns_per_call']:.2f} | {comparison['median_ratio']:.3f}× | "
            f"[{lo:.3f}, {hi:.3f}]× | {base['cv']:.3f} | {candidate['cv']:.3f} |"
        )
    lines += [
        "",
        "## Static code, size and build observations",
        "",
        "Static instruction counts are disassembly counts, not dynamic counts. Compile measurements are one build per pinned artifact and descriptive, not a statistical build-time claim.",
        "",
        "| Artifact | Profile | IR TSLOAD sites by function | Function instructions | `r10` scratch / resident-base loads | Assembly bytes | Assembly SHA-256 | Static instructions | ELF bytes | `.text` bytes | Compile s | Link s |",
        "|---|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|",
    ]
    for artifact in summary["artifact_builds"].values():
        static = artifact.get("static_disassembly") or {}
        lines.append(
            f"| `{artifact['artifact_id']}` | {artifact['profile']} | "
            f"`{json.dumps(artifact['tsload_sites_by_function'], sort_keys=True)}` | "
            f"{artifact['native_function_shape']['static_assembly_instruction_lines']} | "
            f"{artifact['native_function_shape']['scratch_scaled_qword_loads']}/"
            f"{artifact['native_function_shape']['resident_base_scaled_qword_loads']} | "
            f"{artifact['assembly_bytes']} | `{artifact['assembly_sha256']}` | "
            f"{static.get('static_instruction_count', 'n/a')} | {artifact['binary_bytes']} | "
            f"{artifact['text_bytes'] if artifact['text_bytes'] is not None else 'n/a'} | "
            f"{artifact['compile_seconds']:.6f} | {artifact['link_seconds']:.6f} |"
        )
    lines += [
        "",
        "## Interpretation limits",
        "",
        "- The codegen change removes temporary-register copies for register-resident slice loads while retaining source-register initialization checks, the unsigned `index < length` check, and the bounds-failure path.",
        "- The semantic source, IR operations, slices, bounds behavior, fixture, FFI, and timed harness are unchanged between revisions.",
        "- V1 cross-language medians are historical context only; this experiment does not rerun or overwrite that matrix.",
        "- PMU denial means runtime cause attribution is supported by paired timing and static assembly evidence only, not dynamic instruction/cycle counters.",
        "- No claim is made about production profile/defaults or safety equivalence of `PURE_EXPERIMENTAL`.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
