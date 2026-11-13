from __future__ import annotations

import argparse
import json
import os
import resource
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PROGRAMS = [
    ("conway", "examples/compute/conway.s3"),
    ("stencil5point", "examples/compute/stencil5point.s3"),
    ("s3_num_toolkit", "examples/expansion_v2/s3_num_toolkit.s3"),
    ("insertion_sort_search", "examples/language_maturity/insertion_sort_search.s3"),
    ("csv_integer_parser", "examples/language_maturity/csv_integer_parser.s3"),
    ("hex_encode", "examples/language_maturity/hex_encode.s3"),
]


def _text_bytes(path: Path) -> int:
    out = subprocess.check_output(["size", "-A", str(path)], text=True)
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0] == ".text":
            return int(parts[1])
    return 0


def _atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise


def _run_single_worker(
    name: str,
    rel: str,
    s3_root: Path,
    trials: int,
    warmups: int,
    cpu_limit_s: int,
    mem_limit_mb: int,
) -> dict:
    if cpu_limit_s > 0:
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit_s, cpu_limit_s))
    if mem_limit_mb > 0:
        limit_bytes = mem_limit_mb * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (limit_bytes, limit_bytes))

    sys.path.insert(0, str(s3_root))
    from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
    from bootstrap.s3.pipeline import OptimizationLevel, compile_source

    toolchain = NativeToolchain.detect()
    src_path = s3_root / rel
    source = src_path.read_text(encoding="utf-8")

    t_compile0 = time.perf_counter()
    _, ap = compile_source(source, OptimizationLevel.O1).require_ordinary_artifacts()
    compile_s = time.perf_counter() - t_compile0

    t_emit0 = time.perf_counter()
    asm = X8664Backend(register_allocation=True).generate(ap)
    emit_s = time.perf_counter() - t_emit0

    with tempfile.TemporaryDirectory() as td:
        exe = toolchain.build(asm, Path(td) / f"{name}.out")
        txt = _text_bytes(exe)

        stdout_ref = None
        rc_ref = None
        for _ in range(warmups):
            p = subprocess.run([str(exe)], capture_output=True, text=True, check=False, timeout=10)
            stdout_ref = p.stdout
            rc_ref = p.returncode

        times_ms = []
        for _ in range(trials):
            t1 = time.perf_counter()
            p = subprocess.run([str(exe)], capture_output=True, text=True, check=False, timeout=10)
            times_ms.append((time.perf_counter() - t1) * 1000.0)
            if p.stdout != stdout_ref or p.returncode != rc_ref:
                raise RuntimeError(f"Output mismatch on {name}: rc={p.returncode} vs {rc_ref}")

    return {
        "status": "ok",
        "path": rel,
        "text_bytes": txt,
        "compile_s": round(compile_s, 6),
        "emit_s": round(emit_s, 6),
        "median_ms": round(statistics.median(times_ms), 4),
        "returncode": rc_ref,
        "stdout_len": len(stdout_ref or ""),
        "stdout_head": (stdout_ref or "")[:120].strip(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3-root", type=Path, default=Path("/mnt/c/Users/samue/Desktop/gemini/S3"))
    parser.add_argument("--profile", type=str, default="s3_O1_regalloc")
    parser.add_argument("--trials", type=int, default=7)
    parser.add_argument("--warmups", type=int, default=2)
    parser.add_argument("--timeout-s", type=int, default=30)
    parser.add_argument("--cpu-limit-s", type=int, default=25)
    parser.add_argument("--mem-limit-mb", type=int, default=2048)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--worker-name", type=str, default=None)
    parser.add_argument("--worker-rel", type=str, default=None)
    args = parser.parse_args()

    if args.worker_name is not None:
        res = _run_single_worker(
            args.worker_name,
            args.worker_rel,
            args.s3_root,
            args.trials,
            args.warmups,
            args.cpu_limit_s,
            args.mem_limit_mb,
        )
        print(json.dumps(res), flush=True)
        return

    if args.out is None:
        parser.error("--out is required")

    results: dict[str, dict] = {}
    if args.resume and args.out.exists():
        loaded = json.loads(args.out.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            results = loaded

    total = len(PROGRAMS)
    for idx, (name, rel) in enumerate(PROGRAMS, start=1):
        if args.resume and name in results and results[name].get("status") == "ok":
            print(f"[{idx}/{total}] {name:22s} | profile={args.profile} | status=SKIPPED (cached)", flush=True)
            continue

        t0 = time.perf_counter()
        cmd = [
            sys.executable,
            __file__,
            "--s3-root",
            str(args.s3_root),
            "--trials",
            str(args.trials),
            "--warmups",
            str(args.warmups),
            "--cpu-limit-s",
            str(args.cpu_limit_s),
            "--mem-limit-mb",
            str(args.mem_limit_mb),
            "--worker-name",
            name,
            "--worker-rel",
            rel,
        ]
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=args.timeout_s,
                check=False,
            )
            elapsed = time.perf_counter() - t0
            if proc.returncode != 0:
                err_tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-3:]
                entry = {
                    "status": "error",
                    "path": rel,
                    "elapsed_s": round(elapsed, 4),
                    "returncode": proc.returncode,
                    "error": " | ".join(err_tail),
                }
                print(
                    f"[{idx}/{total}] {name:22s} | profile={args.profile} | elapsed={elapsed:.2f}s | status=ERROR (rc={proc.returncode})",
                    flush=True,
                )
            else:
                entry = json.loads(proc.stdout.strip().splitlines()[-1])
                entry["elapsed_s"] = round(elapsed, 4)
                print(
                    f"[{idx}/{total}] {name:22s} | profile={args.profile} | .text={entry['text_bytes']:6d}B | emit={entry['emit_s']:.3f}s | median={entry['median_ms']:.3f}ms | elapsed={elapsed:.2f}s | status=OK",
                    flush=True,
                )
        except subprocess.TimeoutExpired:
            elapsed = time.perf_counter() - t0
            entry = {
                "status": "timeout",
                "path": rel,
                "elapsed_s": round(elapsed, 4),
                "timeout_s": args.timeout_s,
            }
            print(
                f"[{idx}/{total}] {name:22s} | profile={args.profile} | elapsed={elapsed:.2f}s | status=TIMEOUT ({args.timeout_s}s)",
                flush=True,
            )

        results[name] = entry
        _atomic_write_json(args.out, results)


if __name__ == "__main__":
    main()
