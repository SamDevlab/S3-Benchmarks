#!/usr/bin/env python3
"""Build, validate, and measure the isolated S3 pure/controlled V1 matrix."""
from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import math
import os
import platform
import re
import random
import shutil
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from fixture import SEED, SIZE_COUNTS, expected_outputs, fixture_values, workload_counts, write_expected, write_fixture

HERE = Path(__file__).resolve().parent
MANIFEST = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
WORKLOADS = [item["id"] for item in MANIFEST["workloads"]]
S3_MODES = {
    "PURE_EXPERIMENTAL": "pure-experimental",
    "PER_INSTRUCTION": "per-instruction",
    "EXACT_SEGMENT": "exact-segment",
    "LOOP_HYBRID": "loop-hybrid",
}
TOL_ABS = MANIFEST["fixture"]["correctness_tolerance"]["absolute"]
TOL_REL = MANIFEST["fixture"]["correctness_tolerance"]["relative"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def append_jsonl(path: Path, value: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
        stream.flush()


def version(command: list[str]) -> str:
    found = shutil.which(command[0])
    if found is None:
        return "unavailable"
    try:
        result = subprocess.run([found, *command[1:]], check=False, text=True, capture_output=True, timeout=10)
        text = (result.stdout or result.stderr).splitlines()
        return text[0].strip() if text else f"exit={result.returncode}"
    except (OSError, subprocess.TimeoutExpired) as error:
        return f"unavailable: {error}"


def timed_command(command: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> float:
    start = time.perf_counter_ns()
    completed = subprocess.run(command, cwd=cwd, env=env, check=False, text=True, capture_output=True, timeout=120)
    elapsed = (time.perf_counter_ns() - start) / 1e9
    if completed.returncode:
        raise RuntimeError(
            f"command failed ({completed.returncode}): {' '.join(command)}\n"
            f"stdout:\n{completed.stdout[-4000:]}\nstderr:\n{completed.stderr[-4000:]}"
        )
    return elapsed


def text_section(path: Path) -> int | None:
    objdump = shutil.which("objdump")
    if not objdump:
        return None
    result = subprocess.run([objdump, "-h", str(path)], check=True, text=True, capture_output=True)
    for line in result.stdout.splitlines():
        fields = line.split()
        if len(fields) >= 3 and fields[1] == ".text":
            return int(fields[2], 16)
    return None


def static_disassembly_counts(path: Path) -> dict[str, int] | None:
    objdump = shutil.which("objdump")
    if not objdump:
        return None
    result = subprocess.run([objdump, "-d", "--no-show-raw-insn", str(path)], check=True, text=True, capture_output=True)
    instruction_count = conditional_branches = call_count = memory_operand_count = 0
    for line in result.stdout.splitlines():
        match = re.match(r"^\s*[0-9a-fA-F]+:\s+([A-Za-z.][A-Za-z0-9_.]*)\b(.*)$", line)
        if not match:
            continue
        mnemonic, operands = match.group(1).lower(), match.group(2)
        instruction_count += 1
        if mnemonic.startswith("j") or mnemonic.startswith("loop"):
            conditional_branches += 1
        if mnemonic.startswith("call"):
            call_count += 1
        if "(" in operands or "[" in operands:
            memory_operand_count += 1
    return {"static_instruction_count": instruction_count,
            "static_branch_instruction_count": conditional_branches,
            "static_call_instruction_count": call_count,
            "static_memory_operand_instruction_count": memory_operand_count}


def check_elf_x86_64(path: Path) -> None:
    readelf = shutil.which("readelf")
    if not readelf:
        raise RuntimeError("readelf is required to verify ELF identity")
    result = subprocess.run([readelf, "-h", str(path)], check=True, text=True, capture_output=True)
    if "ELF64" not in result.stdout or "X86-64" not in result.stdout:
        raise RuntimeError(f"artifact is not ELF64 x86-64: {path}")


def command_output(command: list[str]) -> tuple[str, int]:
    completed = subprocess.run(command, check=False, text=True, capture_output=True, timeout=30)
    if completed.returncode:
        raise RuntimeError(f"metadata command failed: {' '.join(command)}: {completed.stderr[-2000:]}")
    return (completed.stdout or completed.stderr).strip(), completed.returncode


def host_metadata() -> dict[str, Any]:
    cpu_model = "unknown"
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.exists():
        for line in cpuinfo.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.lower().startswith("model name"):
                cpu_model = line.split(":", 1)[-1].strip()
                break
    governor_path = Path("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor")
    memory = {}
    meminfo = Path("/proc/meminfo")
    if meminfo.exists():
        for line in meminfo.read_text(encoding="ascii", errors="replace").splitlines():
            if ":" in line and line.split(":", 1)[0] in {"MemTotal", "MemAvailable", "SwapTotal"}:
                memory[line.split(":", 1)[0]] = line.split(":", 1)[1].strip()
    cpu_set = sorted(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else []
    disk = {}
    for mount in ("/", "/dev/shm"):
        try:
            usage = shutil.disk_usage(mount)
            disk[mount] = {"total_bytes": usage.total, "used_bytes": usage.used, "free_bytes": usage.free}
        except OSError:
            disk[mount] = None
    return {
        "platform": platform.platform(),
        "uname": list(platform.uname()),
        "machine": platform.machine(),
        "cpu_model": cpu_model,
        "logical_cpus": os.cpu_count(),
        "load_average": list(os.getloadavg()) if hasattr(os, "getloadavg") else None,
        "affinity_cpus": cpu_set,
        "frequency_governor": governor_path.read_text().strip() if governor_path.exists() else None,
        "memory": memory, "disk": disk,
        "tool_versions": {
            "gcc": version(["gcc", "--version"]), "clang": version(["clang", "--version"]),
            "rustc": version(["rustc", "--version"]), "zig": version(["zig", "version"]),
            "python": sys.version.splitlines()[0], "binutils_objdump": version(["objdump", "--version"]),
        },
        "kernel_runner_affinity": cpu_set,
    }


def git_value(repo: Path, revision: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), "rev-parse", revision], check=True, text=True, capture_output=True)
    return result.stdout.strip()


def validate_sources() -> dict[str, str]:
    hashes = {}
    for item in MANIFEST["workloads"]:
        path = HERE / item["source"]
        actual = sha256(path)
        if actual != item["sha256"]:
            raise RuntimeError(f"source hash mismatch for {path.name}: {actual} != {item['sha256']}")
        hashes[item["id"]] = actual
    return hashes


def run_process(command: list[str], *, timeout: float = 20.0) -> tuple[dict[str, Any], int]:
    preexec = None
    if platform.system() == "Linux":
        import resource

        def limits() -> None:
            resource.setrlimit(resource.RLIMIT_CPU, (12, 13))
            address = 1024 * 1024 * 1024
            resource.setrlimit(resource.RLIMIT_AS, (address, address))
            file_size = 64 * 1024 * 1024
            resource.setrlimit(resource.RLIMIT_FSIZE, (file_size, file_size))

        preexec = limits
    start = time.perf_counter_ns()
    result = subprocess.run(command, cwd=HERE, check=False, text=True, capture_output=True,
                            timeout=timeout, preexec_fn=preexec)
    wall_ns = time.perf_counter_ns() - start
    if result.returncode:
        raise RuntimeError(f"runner failed ({result.returncode}): {' '.join(command)}\n{result.stderr[-3000:]}\n{result.stdout[-1000:]}")
    try:
        parsed = json.loads(result.stdout.strip().splitlines()[-1])
    except (IndexError, json.JSONDecodeError) as error:
        raise RuntimeError(f"runner did not return JSON: {result.stdout[-2000:]}\n{result.stderr[-2000:]}") from error
    return parsed, wall_ns


def assert_parity(actual: list[float | int], expected: list[float | int], workload: str, implementation: str) -> None:
    if len(actual) != len(expected):
        raise RuntimeError(f"{implementation}/{workload}: output length {len(actual)} != {len(expected)}")
    for index, (got, want) in enumerate(zip(actual, expected)):
        if isinstance(want, int):
            if int(got) != want:
                raise RuntimeError(f"{implementation}/{workload}[{index}]: {got!r} != exact {want!r}")
        elif not math.isclose(float(got), float(want), rel_tol=TOL_REL, abs_tol=TOL_ABS):
            raise RuntimeError(f"{implementation}/{workload}[{index}]: {got!r} != {want!r} within tolerance")


def verify_s3_invalid_output(library: Path, workload: str, seed: int) -> int:
    """Probe a short output slice outside timing; Pure must retain checked FFI bounds."""
    f = fixture_values(seed)
    counts = workload_counts("small")
    n, points = counts["agent_energy_residual"], counts["point_cloud_summary"]
    dptr, iptr, i64 = ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64
    actual = (ctypes.c_double * len(f["actual"]))(*f["actual"])
    load = (ctypes.c_double * len(f["load"] ))(*f["load"])
    values = (ctypes.c_double * len(f["values"] ))(*f["values"])
    mask = (ctypes.c_int64 * len(f["valid_mask"] ))(*f["valid_mask"])
    coords = (ctypes.c_double * len(f["coordinates"] ))(*f["coordinates"])
    library_handle = ctypes.CDLL(str(library))
    fn = getattr(library_handle, workload)
    fn.restype = i64
    if workload == "agent_energy_residual":
        output = (ctypes.c_double * 3)(); fn.argtypes = [dptr, i64, dptr, i64, i64, dptr, i64]
        result = fn(actual, n, load, n, n, output, 2)
    elif workload == "agent_point_bounds":
        output = (ctypes.c_double * 6)(); fn.argtypes = [dptr, i64, i64, dptr, i64]
        result = fn(coords, points * 3, points, output, 5)
    elif workload == "agent_raster_threshold_count":
        output = (ctypes.c_int64 * 1)(); fn.argtypes = [dptr, i64, iptr, i64, i64, ctypes.c_double, iptr, i64]
        result = fn(values, n, mask, n, n, f["threshold"], output, 0)
    elif workload == "agent_raster_valid_mean":
        output = (ctypes.c_double * 1)(); fn.argtypes = [dptr, i64, iptr, i64, i64, dptr, i64]
        result = fn(values, n, mask, n, n, output, 0)
    elif workload == "energy_series_aggregation":
        output = (ctypes.c_double * 5)(); fn.argtypes = [dptr, i64, dptr, i64, ctypes.c_double, dptr, i64]
        result = fn(actual, n, load, n, f["capacity"], output, 4)
    elif workload == "point_cloud_summary":
        output = (ctypes.c_double * 10)(); fn.argtypes = [dptr, i64, i64, dptr, i64]
        result = fn(coords, points * 3, points, output, 9)
    else:
        raise ValueError(workload)
    if result != 2:
        raise RuntimeError(f"{library.name}/{workload}: short output returned {result}, expected status 2")
    return int(result)


def record_artifact(path: Path, artifact_id: str, language: str, profile: str,
                    flags: list[str], compile_s: float | None, link_s: float | None,
                    extra: dict[str, Any] | None = None) -> dict[str, Any]:
    check_elf_x86_64(path)
    row = {
        "artifact_id": artifact_id, "language": language, "profile": profile, "flags": flags,
        "path": path.name, "sha256": sha256(path), "binary_bytes": path.stat().st_size,
        "text_bytes": text_section(path), "compile_seconds": compile_s, "link_seconds": link_s,
    }
    if language == "S3":
        row["static_disassembly"] = static_disassembly_counts(path)
    if extra:
        row.update(extra)
    return row


def build_s3_artifact(repo: Path, workload: str, source_path: Path, mode_name: str,
                      budget_mode: str, optimization: str, build_dir: Path, cc: str,
                      compiler_commit: str) -> dict[str, Any]:
    sys.path.insert(0, str(repo))
    from bootstrap.s3.backends.x86_64 import NativeToolchain, generate_ffi_assembly
    from bootstrap.s3.pipeline import compile_source

    stem = f"s3-{mode_name.lower()}-{optimization.lower()}-{workload}"
    asm_path, obj_path, lib_path = (build_dir / f"{stem}.{suffix}" for suffix in ("s", "o", "so"))
    start = time.perf_counter_ns()
    compiled = compile_source(source_path.read_text(encoding="utf-8"), optimization)
    frontend_s = (time.perf_counter_ns() - start) / 1e9
    _, ordinary_assembly = compiled.require_ordinary_artifacts()
    start = time.perf_counter_ns()
    native_assembly = generate_ffi_assembly(ordinary_assembly, instruction_budget_mode=budget_mode)
    assembly_s = (time.perf_counter_ns() - start) / 1e9
    asm_path.write_text(native_assembly, encoding="utf-8", newline="\n")
    start = time.perf_counter_ns()
    subprocess.run([cc, "-x", "assembler", "-c", str(asm_path), "-o", str(obj_path)],
                   check=True, text=True, capture_output=True, timeout=120)
    assemble_s = (time.perf_counter_ns() - start) / 1e9
    start = time.perf_counter_ns()
    subprocess.run([cc, "-shared", "-nostdlib", "-Wl,--build-id=none", str(obj_path), "-o", str(lib_path)],
                   check=True, text=True, capture_output=True, timeout=120)
    link_s = (time.perf_counter_ns() - start) / 1e9
    artifact = record_artifact(lib_path, stem, "S3", f"{mode_name}/{optimization}",
        [f"compiler={compiler_commit}", f"optimization={optimization}", f"budget_mode={budget_mode}"],
        frontend_s + assembly_s + assemble_s, link_s,
        {"frontend_optimizer_seconds": frontend_s, "backend_assembly_seconds": assembly_s,
         "assembler_seconds": assemble_s, "assembly_sha256": sha256(asm_path),
         "object_sha256": sha256(obj_path), "source_sha256": sha256(source_path),
         "compiler_commit": compiler_commit, "budget_mode": budget_mode,
         "assembly_bytes": asm_path.stat().st_size})
    artifact["path"] = str(lib_path)
    return artifact


def build_external_artifact(language: str, profile: str, source: Path, build_dir: Path) -> dict[str, Any]:
    stem = f"{language.lower()}-{profile.lower().replace('-', '')}"
    obj, lib = build_dir / f"{stem}.o", build_dir / f"lib{stem}.so"
    compile_s = link_s = None
    flags: list[str]
    if language in {"GCC", "Clang"}:
        cc = shutil.which("gcc" if language == "GCC" else "clang")
        optimization = "-O0" if profile == "O0" else "-O2"
        flags = [optimization, "-fPIC", "-fno-fast-math", "-ffp-contract=off", "-std=c11"]
        compile_s = timed_command([cc, *flags, "-c", str(source), "-o", str(obj)])
        link_s = timed_command([cc, "-shared", "-Wl,--build-id=none", str(obj), "-lm", "-o", str(lib)])
    elif language == "Rust":
        optimization = "0" if profile == "opt-level-0" else "2"
        wrapper = HERE / "reference" / "rust_linker_wrapper.py"
        wrapper.chmod(wrapper.stat().st_mode | 0o111)
        link_record = build_dir / f"{stem}.link.json"
        env = os.environ.copy()
        env["S3_LINK_TIMING_FILE"] = str(link_record)
        env["CC"] = shutil.which("gcc")
        flags = ["--edition=2021", "--crate-type=cdylib", f"-Copt-level={optimization}",
                 f"-Clinker={wrapper}", "-Cpanic=abort"]
        start = time.perf_counter_ns()
        result = subprocess.run([shutil.which("rustc"), *flags, str(source), "-o", str(lib)],
                                check=False, text=True, capture_output=True, timeout=180, env=env)
        total_s = (time.perf_counter_ns() - start) / 1e9
        if result.returncode:
            raise RuntimeError(f"rustc failed: {result.stderr[-4000:]}")
        link_s = json.loads(link_record.read_text(encoding="utf-8"))["elapsed_ns"] / 1e9 if link_record.exists() else None
        compile_s = total_s - link_s if link_s is not None else None
        extra = {"rustc_total_seconds": total_s, "link_time_measured_by_wrapper": link_s is not None}
    elif language == "Zig":
        optimization = "Debug" if profile == "Debug" else "ReleaseFast"
        flags = ["build-obj", "-O", optimization, "-fPIC", f"-femit-bin={obj}"]
        local_cache, global_cache = build_dir / "zig-local-cache", build_dir / "zig-global-cache"
        local_cache.mkdir(exist_ok=True); global_cache.mkdir(exist_ok=True)
        zig_env = os.environ.copy()
        zig_env["ZIG_LOCAL_CACHE_DIR"] = str(local_cache)
        zig_env["ZIG_GLOBAL_CACHE_DIR"] = str(global_cache)
        zig_env["XDG_CACHE_HOME"] = str(global_cache)
        zig_env["TMPDIR"] = str(build_dir)
        compile_s = timed_command([shutil.which("zig"), *flags, str(source)], env=zig_env)
        link_s = timed_command([shutil.which("zig"), "build-lib", str(obj), "-dynamic", "-O", optimization,
                                f"-femit-bin={lib}"], env=zig_env)
    else:
        raise ValueError(language)
    artifact = record_artifact(lib, stem, language, profile, flags, compile_s, link_s,
                               {"source_sha256": sha256(source), "object_sha256": sha256(obj) if obj.exists() else None,
                                "object_bytes": obj.stat().st_size if obj.exists() else None,
                                **(extra if language == "Rust" else {})})
    artifact["path"] = str(lib)
    return artifact


def percentile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, max(0, math.ceil(fraction * len(ordered)) - 1))]


def stats(values: list[float], seed: int) -> dict[str, Any]:
    mean = statistics.fmean(values)
    stddev = statistics.pstdev(values)
    rng = random.Random(seed)
    boot = []
    for _ in range(5000):
        sample = [values[rng.randrange(len(values))] for _ in values]
        boot.append(statistics.median(sample))
    return {
        "n": len(values), "median_ns_per_call": statistics.median(values),
        "mean_ns_per_call": mean, "p95_ns_per_call": percentile(values, 0.95),
        "stddev_ns_per_call": stddev, "cv": stddev / mean if mean else 0.0,
        "median_bootstrap_95ci_ns_per_call": [percentile(boot, 0.025), percentile(boot, 0.975)],
    }


def paired_ratio(numer: list[float], denom: list[float], seed: int) -> dict[str, Any]:
    ratios = [a / b for a, b in zip(numer, denom)]
    rng = random.Random(seed)
    boot = []
    for _ in range(10000):
        sample = [ratios[rng.randrange(len(ratios))] for _ in ratios]
        boot.append(statistics.median(sample))
    return {
        "paired_rounds": len(ratios), "median_ratio": statistics.median(ratios),
        "mean_ratio": statistics.fmean(ratios), "bootstrap_95ci_median_ratio": [percentile(boot, 0.025), percentile(boot, 0.975)],
        "paired_ratios": ratios,
    }


def render_report(summary: dict[str, Any], output: Path) -> None:
    runtime = summary["runtime"]
    ratios = summary["ratios"]
    builds = list(summary["artifact_builds"].values())
    runtime_rss_medians = [float(row["median_maxrss_kib"]) for row in runtime.values()]
    runtime_cvs = [float(row["cv"]) for row in runtime.values()]
    metadata = json.loads((output / "run-manifest.json").read_text(encoding="utf-8"))
    lines = [
        "# Native S3 Pure vs Controlled — measurement report",
        "",
        f"- Campaign: `{MANIFEST['campaign']}`",
        f"- Result: **{summary['result']}**; `{summary['workloads_qualified']}` workloads, `{summary['measured_cell_count']}` measured cells.",
        f"- V6 baseline: `{metadata['baseline_compiler_commit']}`; experimental profile commit: `{metadata['experimental_pure_compiler_commit']}` (direct child).",
        f"- Host: {metadata['host']['cpu_model']}, {metadata['host']['platform']}; CPU affinity {metadata['pinning_cpu']}; governor {metadata['host']['frequency_governor'] or 'unavailable'}.",
        f"- Fixture SHA-256: `{metadata['fixture_sha256']}`; generated source bundle SHA-256: `{metadata.get('compiler_archive_sha256') or 'not supplied'}`.",
        f"- Sampling: {metadata['warmups']} warmups + {metadata['measured_samples']} rounds; input sizes {', '.join(metadata['input_sizes'])}; raw outliers retained.",
        "- The native timer covers repeated indirect FFI calls only. Dispatch overhead is included, not subtracted. Python is timed separately as interpreted code.",
        "- The full root filesystem forced all generated artifacts/caches into `/dev/shm`. These are KVM-guest descriptive measurements, not bare-metal claims.",
        "",
        "## Kernel runtime",
        "",
        "Times are nanoseconds per call; optimization levels are tool-specific and not asserted equivalent. p95 is the empirical nearest-rank estimate from 15 samples. CV is population standard deviation / mean.",
        "",
        "| Workload | Input | Implementation | Median ns/call | p95 ns/call | CV | Median RSS KiB |",
        "|---|---:|---|---:|---:|---:|---:|",
    ]
    for workload in WORKLOADS:
        if not any(key.startswith(workload + "|") for key in runtime):
            continue
        for size in metadata["input_sizes"]:
            choices = [
                ("S3 Pure O1", "S3", "PURE_EXPERIMENTAL", "O1"),
                ("S3 Per-instruction O1", "S3", "PER_INSTRUCTION", "O1"),
                ("S3 Exact-segment O1", "S3", "EXACT_SEGMENT", "O1"),
                ("S3 Loop-hybrid O1", "S3", "LOOP_HYBRID", "O1"),
                ("GCC O2", "GCC", "O2", "O2"), ("Clang O2", "Clang", "O2", "O2"),
                ("Rust opt-level 2", "Rust", "opt-level-2", "opt-level-2"),
                ("Zig ReleaseFast", "Zig", "ReleaseFast", "ReleaseFast"),
                ("Python interpreted", "Python", "CPython", "interpreted"),
            ]
            for label, language, profile, optimization in choices:
                key = "|".join((workload, size, language, profile, optimization))
                stat = runtime.get(key)
                if stat:
                    lines.append(f"| `{workload}` | {size} | {label} | {stat['median_ns_per_call']:.2f} | {stat['p95_ns_per_call']:.2f} | {stat['cv']:.3f} | {stat['median_maxrss_kib']:.0f} |")
    lines += ["", "## Process initialization and peak memory", "", "Initialization is measured in separate zero-iteration launches after one untimed correctness call; it includes spawn, loader/interpreter and fixture decoding. It is not subtracted from the kernel timer.", "", "| Workload | Input | Implementation | Median wall ns | p95 wall ns |", "|---|---:|---|---:|---:|"]
    for key, value in summary.get("process_initialization", {}).items():
        workload, size, language, profile, optimization = key.split("|")
        lines.append(f"| `{workload}` | {size} | {language} `{profile}/{optimization}` | {value['median_wall_ns']:.0f} | {value['p95_wall_ns']:.0f} |")
    lines += ["", "## Cost of the S3 control mechanism", "", "Paired ratio is `controlled / pure` for the same workload, size, round, compiler commit and optimization. Values above 1 mean slower than Pure; 1.00× is parity.", "", "| Workload | Input | Controlled mode | Median paired ratio | 95% bootstrap CI |", "|---|---:|---|---:|---:|"]
    for key, value in ratios["control_overhead"].items():
        workload, size, mode = key.split("|")
        lo, hi = value["bootstrap_95ci_median_ratio"]
        lines.append(f"| `{workload}` | {size} | `{mode}` | {value['median_ratio']:.3f}× | [{lo:.3f}, {hi:.3f}]× |")
    lines += ["", "## S3 Pure vs other implementations", "", "Paired ratio is `S3 Pure O1 / other implementation` within each shuffled sample round. Python remains an interpreted comparison and is not included in any native ranking.", "", "| Workload | Input | Comparator | Median ratio | 95% bootstrap CI |", "|---|---:|---|---:|---:|"]
    for key, value in ratios["pure_vs_external"].items():
        workload, size, language, profile = key.split("|")
        lo, hi = value["bootstrap_95ci_median_ratio"]
        lines.append(f"| `{workload}` | {size} | {language} `{profile}` | {value['median_ratio']:.3f}× | [{lo:.3f}, {hi:.3f}]× |")
    lines += ["", "## Build time, ELF size, and static S3 code shape", "", "Compile and link are separate wall-clock observations. S3 compile time includes frontend/optimizer, backend assembly generation and assembler; link time is separate. Rust code-generation time is the rustc total minus the measured linker proxy wall time. Static instruction counts are disassembly counts, not dynamic instruction counts.", "", "| Artifact | Profile | Compile s | Link s | ELF bytes | `.text` bytes | Static insns* | SHA-256 |", "|---|---|---:|---:|---:|---:|---:|---|"]
    for build in builds:
        count = (build.get("static_disassembly") or {}).get("static_instruction_count")
        lines.append(f"| `{build['artifact_id']}` | {build['profile']} | {build['compile_seconds'] if build['compile_seconds'] is not None else 'n/a'} | {build['link_seconds'] if build['link_seconds'] is not None else 'n/a'} | {build['binary_bytes']} | {build['text_bytes'] if build['text_bytes'] is not None else 'n/a'} | {count if count is not None else 'n/a'} | `{build['sha256']}` |")
    if ratios["control_overhead"]:
        key, value = max(ratios["control_overhead"].items(), key=lambda pair: pair[1]["median_ratio"])
        lines += ["", f"Observed maximum control ratio: `{key}` at **{value['median_ratio']:.3f}×** (paired 95% bootstrap CI [{value['bootstrap_95ci_median_ratio'][0]:.3f}, {value['bootstrap_95ci_median_ratio'][1]:.3f}]×). This is a corpus observation, not a universal overhead claim."]
    native_ratios = {key: value for key, value in ratios["pure_vs_external"].items() if key.rsplit("|", 1)[-1] != "CPython"}
    if native_ratios:
        key, value = max(native_ratios.items(), key=lambda pair: pair[1]["median_ratio"])
        lines.append(f"Largest observed Pure/native residual: `{key}` at **{value['median_ratio']:.3f}×**. This identifies a follow-up candidate, not its cause.")
    builds_by_id = {build["artifact_id"]: build for build in builds}
    text_deltas = []
    for build in builds:
        if build["language"] == "S3" and build["profile"] == "PURE_EXPERIMENTAL/O1":
            workload = build["artifact_id"].rsplit("-", 1)[-1]
            controlled = builds_by_id.get(f"s3-per_instruction-o1-{workload}")
            if controlled and build.get("text_bytes") is not None and controlled.get("text_bytes") is not None:
                text_deltas.append((workload, controlled["text_bytes"] - build["text_bytes"]))
    if text_deltas:
        workload, delta = max(text_deltas, key=lambda item: item[1])
        lines.append(f"Largest O1 PER_INSTRUCTION minus Pure `.text` delta: `{workload}`, **{delta:+d} bytes** (static section size only).")
    lines.append("Calibration note: high-repetition controlled O0 `point_cloud_summary` exhausted the existing 100,000 logical-instruction budget when many calls accumulated in one process. The final protocol uses a base of one call (8/2/1 calls for small/medium/full per process), preserving the cap and approximately normalizing input work; this failed calibration is not a performance result.")
    max_cv = max(runtime_cvs, default=0.0)
    lines += ["", "## Interpretation and limits", "", "- The paired control-cost ratios are measured at all three input sizes, over six workloads, and use the same pinned compiler commit and optimization level within each S3 pair.", f"- Runtime-cell CV reached {max_cv:.3f}; the 15-sample, short-batch results are descriptive. Ratios whose paired confidence intervals include 1.00× do not resolve a difference in this run.", "- Process peak RSS includes the process and loader baseline, not just the kernel. Identical RSS medians are nondiscriminating and do not support a claim of equal kernel memory use.", "- `.text` size and static disassembly explain generated-code growth only. They do not prove dynamic instruction counts, CPU bottlenecks, vectorization behavior, or causality.", "- FFI dispatch is included equally through one C harness and is intentionally not subtracted. `process_initialization_wall_ns` includes process spawn, dynamic loader/interpreter, fixture loading and a correctness call; it is not a pure OS process-creation metric.", "- S3 Pure removes only dynamic instruction-budget accounting. Untimed invalid-output probes require status 2 across all S3 profiles; valid data parity is required for every measured sample.", "- No parser workload was accepted in this pinned V6-native subset, so parsing is explicitly unavailable rather than replaced with a simplified algorithm.", "- See `run-manifest.json`, `builds.jsonl`, `raw_samples.jsonl`, `startup_samples.jsonl`, `invalid_cases.jsonl`, `runtime-fixture-v1.bin`, and `expected-v1.json` for reproducible raw evidence.", ""]
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-repo", default=os.environ.get("S3_REPO"), help="clean pinned experimental compiler worktree")
    parser.add_argument("--s3-commit", default=MANIFEST["experimental_pure_compiler_commit"])
    parser.add_argument("--s3-parent", default=MANIFEST["experimental_parent_commit"])
    parser.add_argument("--compiler-archive", help="git-archive tar used to stage the compiler source tree")
    parser.add_argument("--compiler-archive-sha256", help="expected SHA-256 of --compiler-archive")
    parser.add_argument("--output", default="/dev/shm/s3-native-pure-controlled-v1-results")
    parser.add_argument("--reuse-builds-from", help="reuse hash-verified ELF builds from an earlier campaign output")
    parser.add_argument("--samples", type=int, default=15)
    parser.add_argument("--warmups", type=int, default=3)
    parser.add_argument("--iterations", type=int, default=1)
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--only-workload", choices=WORKLOADS, action="append")
    parser.add_argument("--only-language", choices=["S3", "GCC", "Clang", "Rust", "Zig", "Python"], action="append")
    parser.add_argument("--only-size", choices=sorted(SIZE_COUNTS), action="append")
    args = parser.parse_args()
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise SystemExit("campaign requires Linux x86-64")
    if args.samples < 1 or args.warmups < 0 or args.iterations < 0:
        raise SystemExit("samples must be positive; warmups/iterations non-negative")
    repo = Path(args.s3_repo).resolve() if args.s3_repo else None
    if repo is None or not repo.is_dir():
        raise SystemExit("set --s3-repo or S3_REPO to the pinned S3 compiler worktree")
    has_git = (repo / ".git").exists()
    compiler_commit, compiler_parent = args.s3_commit, args.s3_parent
    if has_git:
        if git_value(repo, "HEAD") != compiler_commit or git_value(repo, "HEAD^") != compiler_parent:
            raise SystemExit("S3 worktree commits do not match the explicit compiler/parent pins")
    elif compiler_commit != MANIFEST["experimental_pure_compiler_commit"] or compiler_parent != MANIFEST["experimental_parent_commit"]:
        raise SystemExit("source archives must use the explicit manifest compiler/parent pins")
    compiler_archive_sha = None
    if args.compiler_archive:
        archive_path = Path(args.compiler_archive).resolve()
        compiler_archive_sha = sha256(archive_path)
        if args.compiler_archive_sha256 and compiler_archive_sha.lower() != args.compiler_archive_sha256.lower():
            raise SystemExit("compiler source archive SHA-256 does not match the supplied identity")
    elif args.compiler_archive_sha256:
        raise SystemExit("--compiler-archive-sha256 requires --compiler-archive")

    output = Path(args.output).resolve()
    if not str(output).startswith("/dev/shm/"):
        raise SystemExit("generated campaign data must remain in /dev/shm (the VM root volume is full)")
    if output.exists() and any(output.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty output directory: {output}")
    output.mkdir(parents=True, exist_ok=True)
    build_dir = output / "build"
    build_dir.mkdir()
    raw_path, build_path, startup_path = output / "raw_samples.jsonl", output / "builds.jsonl", output / "startup_samples.jsonl"
    (output / "raw").mkdir()
    workloads = args.only_workload or WORKLOADS
    sizes = args.only_size or list(SIZE_COUNTS)
    iterations_by_size = {"small": args.iterations * 8, "medium": args.iterations * 2, "full": args.iterations}
    selected_languages = set(args.only_language or ["S3", "GCC", "Clang", "Rust", "Zig", "Python"])
    source_hashes = validate_sources()
    fixture_path = output / "runtime-fixture-v1.bin"
    fixture_sha = write_fixture(fixture_path, args.seed)
    expected_path = output / "expected-v1.json"
    write_expected(expected_path, args.seed)
    expected = {size: expected_outputs(args.seed, size) for size in sizes}
    host = host_metadata()
    cpu = 0 if 0 in host["affinity_cpus"] else min(host["affinity_cpus"])
    taskset = shutil.which("taskset")
    if not taskset:
        raise SystemExit("taskset is required for the pinned measurement protocol")
    cc = shutil.which("gcc") or shutil.which("cc")
    if not cc:
        raise SystemExit("GCC/cc is required for the S3 assembly linker and C harness")
    (output / "raw" / "kernel_runner.c").write_bytes((HERE / "reference" / "kernel_runner.c").read_bytes())
    runner = build_dir / "kernel_runner"
    harness_compile_s = timed_command([cc, "-O2", "-std=c11", "-Wall", "-Wextra", str(HERE / "reference" / "kernel_runner.c"), "-ldl", "-o", str(runner)])
    # The no-op fixture and its expected result are both content-addressed in the run manifest.

    artifact_by_lang_profile: dict[tuple[str, str], dict[str, Any]] = {}
    artifact_by_id: dict[str, dict[str, Any]] = {}
    build_rows: list[dict[str, Any]] = []
    build_file = build_path.open("w", encoding="utf-8", newline="\n")

    def save_build(row: dict[str, Any]) -> None:
        build_file.write(json.dumps(row, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
        build_file.flush()
        build_rows.append(row)
        artifact_by_id[row["artifact_id"]] = row

    if args.reuse_builds_from:
        reuse_root = Path(args.reuse_builds_from).resolve()
        prior_builds = reuse_root / "builds.jsonl"
        if not prior_builds.is_file():
            raise SystemExit("--reuse-builds-from must name a completed build manifest")
        prior_rows = [json.loads(line) for line in prior_builds.read_text(encoding="utf-8").splitlines() if line]
        expected_ids = {
            f"s3-{mode.lower()}-{optimization.lower()}-{workload}"
            for workload in workloads for mode in S3_MODES for optimization in ("O0", "O1")
        } if "S3" in selected_languages else set()
        for language, profiles in (("GCC", ("O0", "O2")), ("Clang", ("O0", "O2")),
                                   ("Rust", ("opt-level-0", "opt-level-2")), ("Zig", ("Debug", "ReleaseFast"))):
            if language in selected_languages:
                expected_ids.update(f"{language.lower()}-{profile.lower().replace('-', '')}" for profile in profiles)
        by_id = {row["artifact_id"]: row for row in prior_rows}
        if not expected_ids.issubset(by_id):
            raise SystemExit(f"reuse build manifest missing artifacts: {sorted(expected_ids - set(by_id))}")
        for artifact_id in sorted(expected_ids):
            row = dict(by_id[artifact_id])
            old_path = Path(row["path"])
            if not old_path.is_file() or sha256(old_path) != row["sha256"]:
                raise SystemExit(f"reusable artifact failed path/hash validation: {old_path}")
            if row["language"] == "S3" and row.get("compiler_commit") != compiler_commit:
                raise SystemExit(f"reusable artifact has a different compiler pin: {artifact_id}")
            if row["language"] == "S3":
                workload = next(item for item in MANIFEST["workloads"] if item["id"] == row.get("artifact_id", "").rsplit("-", 1)[-1])
                if row.get("source_sha256") != workload["sha256"]:
                    raise SystemExit(f"reusable S3 artifact source identity mismatch: {artifact_id}")
            else:
                source_by_language = {"GCC": "kernels.c", "Clang": "kernels.c", "Rust": "kernels.rs", "Zig": "kernels.zig"}
                if row.get("source_sha256") != sha256(HERE / "reference" / source_by_language[row["language"]]):
                    raise SystemExit(f"reusable reference source identity mismatch: {artifact_id}")
            new_path = build_dir / old_path.name
            shutil.copy2(old_path, new_path)
            if sha256(new_path) != row["sha256"]:
                raise SystemExit(f"copied artifact hash mismatch: {artifact_id}")
            row["path"] = str(new_path)
            save_build(row)
            if row["language"] != "S3":
                artifact_by_lang_profile[(row["language"], row["profile"])] = row

    if not args.reuse_builds_from and "GCC" in selected_languages:
        for profile in ("O0", "O2"):
            art = build_external_artifact("GCC", profile, HERE / "reference" / "kernels.c", build_dir)
            artifact_by_lang_profile[("GCC", profile)] = art; save_build(art)
    if not args.reuse_builds_from and "Clang" in selected_languages:
        if not shutil.which("clang"):
            raise SystemExit("Clang selected but clang is not available")
        for profile in ("O0", "O2"):
            art = build_external_artifact("Clang", profile, HERE / "reference" / "kernels.c", build_dir)
            artifact_by_lang_profile[("Clang", profile)] = art; save_build(art)
    if not args.reuse_builds_from and "Rust" in selected_languages:
        for profile in ("opt-level-0", "opt-level-2"):
            art = build_external_artifact("Rust", profile, HERE / "reference" / "kernels.rs", build_dir)
            artifact_by_lang_profile[("Rust", profile)] = art; save_build(art)
    if not args.reuse_builds_from and "Zig" in selected_languages:
        for profile in ("Debug", "ReleaseFast"):
            art = build_external_artifact("Zig", profile, HERE / "reference" / "kernels.zig", build_dir)
            artifact_by_lang_profile[("Zig", profile)] = art; save_build(art)

    variants: list[dict[str, Any]] = []
    if "S3" in selected_languages:
        for workload in workloads:
            item = next(x for x in MANIFEST["workloads"] if x["id"] == workload)
            source_path = HERE / item["source"]
            for mode_name, mode_value in S3_MODES.items():
                for optimization in ("O0", "O1"):
                    artifact_id = f"s3-{mode_name.lower()}-{optimization.lower()}-{workload}"
                    if args.reuse_builds_from:
                        artifact = artifact_by_id[artifact_id]
                    else:
                        artifact = build_s3_artifact(repo, workload, source_path, mode_name, mode_value, optimization, build_dir, cc, compiler_commit)
                        save_build(artifact)
                    for size in sizes:
                        variants.append({"workload": workload, "language": "S3", "profile": mode_name,
                                         "optimization": optimization, "size": size, "artifact": artifact})
    for language, profiles in (("GCC", ("O0", "O2")), ("Clang", ("O0", "O2")),
                               ("Rust", ("opt-level-0", "opt-level-2")), ("Zig", ("Debug", "ReleaseFast"))):
        if language not in selected_languages:
            continue
        for workload in workloads:
            for profile in profiles:
                for size in sizes:
                    variants.append({"workload": workload, "language": language, "profile": profile,
                                     "optimization": profile, "size": size, "artifact": artifact_by_lang_profile[(language, profile)]})
    if "Python" in selected_languages:
        py_artifact = {"artifact_id": f"CPython-{platform.python_version()}", "language": "Python",
                       "profile": "CPython", "flags": ["interpreted", sys.version.splitlines()[0]],
                       "path": str(HERE / "python_runner.py"), "sha256": sha256(HERE / "python_runner.py"),
                       "binary_bytes": None, "text_bytes": None, "compile_seconds": None, "link_seconds": None,
                       "source_sha256": sha256(HERE / "python_runner.py")}
        for workload in workloads:
            for size in sizes:
                variants.append({"workload": workload, "language": "Python", "profile": "CPython",
                                 "optimization": "interpreted", "size": size, "artifact": py_artifact})
    build_file.close()

    # Verify every language's output before any ranking or timing is accepted.
    commands: dict[str, list[str]] = {}
    for variant in variants:
        workload, language, profile, size = variant["workload"], variant["language"], variant["profile"], variant["size"]
        if language == "Python":
            command = [sys.executable, str(HERE / "python_runner.py"), workload, str(fixture_path), "1", size]
        else:
            command = [taskset, "-c", str(cpu), str(runner), str(variant["artifact"]["path"]), workload, str(fixture_path), "1", size]
        commands[variant["artifact"]["artifact_id"] + ":" + workload + ":" + size] = command
        result, _ = run_process(command)
        assert_parity(result["outputs"], expected[size][workload], workload, f"{language}/{profile}/{size}")
        if result["status"] != 0:
            raise RuntimeError(f"nonzero status from {language}/{profile}/{workload}")

    run_metadata = {
        "schema": "s3-native-pure-controlled-run/v1", "campaign": MANIFEST["campaign"],
        "baseline_compiler_commit": MANIFEST["baseline_compiler_commit"],
        "experimental_pure_compiler_commit": compiler_commit,
        "experimental_parent_commit": compiler_parent,
        "compiler_git_metadata_present": has_git,
        "compiler_archive_sha256": compiler_archive_sha,
        "reused_builds_from": str(Path(args.reuse_builds_from).resolve()) if args.reuse_builds_from else None,
        "v7_dependency": "NONE", "fixed_point_dependency": "NONE", "host": host,
        "fixture_sha256": fixture_sha, "expected_sha256": sha256(expected_path),
        "source_hashes": source_hashes, "workloads": workloads, "input_sizes": sizes,
        "languages": sorted(selected_languages), "warmups": args.warmups,
        "measured_samples": args.samples, "base_iterations_per_full_input": args.iterations,
        "iterations_per_sample_by_size": {size: iterations_by_size[size] for size in sizes},
        "invalid_input_probe": "short output slices must return S3 status 2; probes run outside performance timing",
        "timer_native": "CLOCK_MONOTONIC_RAW", "timer_python": "perf_counter_ns",
        "pinning_cpu": cpu, "external_process_limits": {"cpu_seconds_soft_hard": [12, 13], "address_space_bytes": 1073741824},
        "kernel_runner_sha256": sha256(runner), "kernel_runner_build_seconds": harness_compile_s,
        "started_utc_epoch_ns": time.time_ns(),
    }
    (output / "run-manifest.json").write_text(json.dumps(run_metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    invalid_path = output / "invalid_cases.jsonl"
    with invalid_path.open("w", encoding="utf-8", newline="\n") as stream:
        for variant in variants:
            if variant["language"] != "S3":
                continue
            status = verify_s3_invalid_output(Path(variant["artifact"]["path"]), variant["workload"], args.seed)
            probe = {"workload": variant["workload"], "profile": variant["profile"],
                     "optimization": variant["optimization"], "artifact_sha256": variant["artifact"]["sha256"],
                     "short_output_status": status, "result": "PASS"}
            stream.write(json.dumps(probe, sort_keys=True, separators=(",", ":")) + "\n"); stream.flush()

    # Explicit process initialization rows: zero timed iterations after loading the DSO and fixture.
    startup_file = startup_path.open("w", encoding="utf-8", newline="\n")
    for variant in variants:
        for repeat in range(3):
            workload, language, size = variant["workload"], variant["language"], variant["size"]
            if language == "Python":
                command = [sys.executable, str(HERE / "python_runner.py"), workload, str(fixture_path), "0", size]
            else:
                command = [taskset, "-c", str(cpu), str(runner), str(variant["artifact"]["path"]), workload, str(fixture_path), "0", size]
            _, wall_ns = run_process(command)
            row = {"workload": workload, "language": language, "profile": variant["profile"],
                   "optimization": variant["optimization"], "artifact_sha256": variant["artifact"]["sha256"],
                   "size": size,
                   "repeat": repeat, "process_initialization_wall_ns": wall_ns,
                   "definition": "process spawn + interpreter/loader + fixture load + one correctness invocation; not pure OS spawn"}
            startup_file.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"); startup_file.flush()
    startup_file.close()
    startup_rows = [json.loads(line) for line in startup_path.read_text(encoding="utf-8").splitlines() if line]
    startup_summary: dict[str, Any] = {}
    startup_groups: dict[str, list[int]] = {}
    for row in startup_rows:
        key = "|".join((row["workload"], row["size"], row["language"], row["profile"], row["optimization"]))
        startup_groups.setdefault(key, []).append(row["process_initialization_wall_ns"])
    for key, values in startup_groups.items():
        startup_summary[key] = {"n": len(values), "median_wall_ns": statistics.median(values),
                                "p95_wall_ns": percentile(values, 0.95)}

    samples_file = raw_path.open("w", encoding="utf-8", newline="\n")
    rng = random.Random(args.seed ^ 0x51A3)
    for phase, count in (("warmup", args.warmups), ("measured", args.samples)):
        for round_index in range(count):
            order = list(variants)
            rng.shuffle(order)
            for sequence, variant in enumerate(order):
                workload, language, size = variant["workload"], variant["language"], variant["size"]
                sample_iterations = iterations_by_size[size]
                if language == "Python":
                    command = [sys.executable, str(HERE / "python_runner.py"), workload, str(fixture_path), str(sample_iterations), size]
                else:
                    command = [taskset, "-c", str(cpu), str(runner), str(variant["artifact"]["path"]), workload,
                               str(fixture_path), str(sample_iterations), size]
                result, process_wall_ns = run_process(command)
                if result["status"] != 0:
                    raise RuntimeError(f"nonzero return status during timing: {variant}")
                assert_parity(result["outputs"], expected[size][workload], workload, f"{language}/{variant['profile']}/{size}")
                row = {
                    "phase": phase, "round": round_index if phase == "measured" else None,
                    "warmup_index": round_index if phase == "warmup" else None,
                    "sequence": sequence, "workload": workload, "size": size,
                    "work_units_per_call": workload_counts(size)[workload],
                    "language": language, "profile": variant["profile"], "optimization": variant["optimization"],
                    "artifact_id": variant["artifact"]["artifact_id"], "artifact_sha256": variant["artifact"]["sha256"],
                    "source_sha256": variant["artifact"].get("source_sha256"), "fixture_sha256": fixture_sha,
                    "iterations": sample_iterations, "elapsed_ns": result["elapsed_ns"],
                    "ns_per_call": result["ns_per_call"], "ns_per_work_item": result["ns_per_call"] / workload_counts(size)[workload],
                    "outputs": result["outputs"], "checksum": result["checksum"],
                    "maxrss_kib": result["maxrss_kib"], "process_wall_ns": process_wall_ns,
                    "process_minus_kernel_ns": process_wall_ns - result["elapsed_ns"],
                }
                samples_file.write(json.dumps(row, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n")
                samples_file.flush()
            if phase == "measured":
                print(f"measured round {round_index + 1}/{args.samples}: {len(order)} randomized cells", flush=True)
    samples_file.close()

    raw_rows = [json.loads(line) for line in raw_path.read_text(encoding="utf-8").splitlines() if line]
    measured = [row for row in raw_rows if row["phase"] == "measured"]
    series: dict[tuple[str, str, str, str, str], list[dict[str, Any]]] = {}
    for row in measured:
        key = (row["workload"], row["size"], row["language"], row["profile"], row["optimization"])
        series.setdefault(key, []).append(row)
    runtime_summary = {}
    for key, rows in series.items():
        workload, size, language, profile, optimization = key
        runtime_summary["|".join(key)] = {
            **stats([row["ns_per_call"] for row in rows], args.seed + sum(map(ord, "|".join(key)))),
            "ns_per_work_item_median": statistics.median(row["ns_per_work_item"] for row in rows),
            "median_maxrss_kib": statistics.median(row["maxrss_kib"] for row in rows),
            "artifact_sha256": rows[0]["artifact_sha256"], "source_sha256": rows[0]["source_sha256"],
        }
    paired = {"control_overhead": {}, "pure_vs_external": {}}
    if "S3" in selected_languages:
        for workload in workloads:
          for size in sizes:
            lookup = {(r["language"], r["profile"], r["optimization"]): {} for r in measured if r["workload"] == workload and r["size"] == size}
            for row in measured:
                if row["workload"] == workload and row["size"] == size:
                    lookup[(row["language"], row["profile"], row["optimization"])][row["round"]] = row["ns_per_call"]
            pure_key = ("S3", "PURE_EXPERIMENTAL", "O1")
            if pure_key in lookup:
                pure_vals = [lookup[pure_key][i] for i in range(args.samples)]
                for mode in ("PER_INSTRUCTION", "EXACT_SEGMENT", "LOOP_HYBRID"):
                    key = ("S3", mode, "O1")
                    if key in lookup:
                        paired["control_overhead"][f"{workload}|{size}|{mode}"] = paired_ratio(
                            [lookup[key][i] for i in range(args.samples)], pure_vals,
                            args.seed + sum(map(ord, workload + mode)))
                for lang, prof in (("GCC", "O2"), ("Clang", "O2"), ("Rust", "opt-level-2"), ("Zig", "ReleaseFast"), ("Python", "CPython")):
                    key = (lang, prof, prof)
                    if key not in lookup:
                        key = (lang, prof, "interpreted")
                    if key in lookup:
                        paired["pure_vs_external"][f"{workload}|{size}|{lang}|{prof}"] = paired_ratio(
                            pure_vals, [lookup[key][i] for i in range(args.samples)],
                            args.seed + sum(map(ord, workload + lang + prof)))

    build_by_id = {row["artifact_id"]: row for row in build_rows}
    summary = {
        "schema": "s3-native-pure-controlled-summary/v1", "campaign": MANIFEST["campaign"],
        "run_manifest_sha256": sha256(output / "run-manifest.json"),
        "build_count": len(build_rows), "variant_count": len(variants),
        "workloads_qualified": len(workloads), "runtime_samples_per_cell": args.samples,
        "warmups_per_cell": args.warmups, "input_sizes": sizes, "measured_cell_count": len(measured),
        "checksum_parity": "PASS: all preflight and timed rows matched the pinned scalar oracle",
        "invalid_case_count": sum(1 for v in variants if v["language"] == "S3"),
        "invalid_cases": ("PASS: every S3 profile returned checked status 2 for a short output slice; excluded from timings"
                          if any(v["language"] == "S3" for v in variants) else "NOT_RUN: S3 was not selected"),
        "runtime": runtime_summary, "process_initialization": startup_summary, "ratios": paired,
        "artifact_builds": {row["artifact_id"]: row for row in build_rows},
        "limitations": ["KVM guest results only; no bare-metal extrapolation", "Python results are interpreted and reported separately", "optimization levels are not equivalent across compilers", "no parsing workload was available in the six pinned V6-native fixture subset", "process initialization wall time includes spawn, loader/interpreter, fixture decoding and one validation invocation"],
        "result": "COMPLETE" if len(workloads) == len(WORKLOADS) and selected_languages == {"S3", "GCC", "Clang", "Rust", "Zig", "Python"} and set(sizes) == set(SIZE_COUNTS) else "PARTIAL",
    }
    expected_measured = len(variants) * args.samples
    if len(measured) != expected_measured:
        raise RuntimeError(f"raw sample count mismatch: {len(measured)} != {expected_measured}")
    for build in build_rows:
        artifact_path = Path(build["path"])
        if not artifact_path.is_file() or sha256(artifact_path) != build["sha256"]:
            raise RuntimeError(f"built artifact hash/path validation failed: {artifact_path}")
    (output / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    decoded_summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    if decoded_summary["measured_cell_count"] != expected_measured:
        raise RuntimeError("summary JSON post-write count validation failed")
    render_report(summary, output)
    evidence_files = ["run-manifest.json", "builds.jsonl", "raw_samples.jsonl", "startup_samples.jsonl",
                      "invalid_cases.jsonl", "runtime-fixture-v1.bin", "expected-v1.json", "summary.json", "report.md"]
    evidence_index = {"schema": "s3-native-pure-controlled-evidence-index/v1", "files": {}}
    for name in evidence_files:
        path = output / name
        evidence_index["files"][name] = {"sha256": sha256(path), "bytes": path.stat().st_size}
    index_path = output / "evidence-index.json"
    index_path.write_text(json.dumps(evidence_index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    verified_index = json.loads(index_path.read_text(encoding="utf-8"))
    for name, record in verified_index["files"].items():
        if sha256(output / name) != record["sha256"]:
            raise RuntimeError(f"evidence file hash validation failed: {name}")
    print(f"RESULT={summary['result']} workloads={len(workloads)} variants={len(variants)} measured_cells={len(measured)} fixture_sha256={fixture_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
