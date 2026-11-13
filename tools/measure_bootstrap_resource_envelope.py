"""Measure a bootstrap command's resource envelope as characterization evidence.

This collector does not make performance claims. Wall time, CPU time, peak RSS,
and artifact sizes are recorded for capacity/scalability analysis only.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

try:
    import resource
except ImportError:  # pragma: no cover - Windows fallback
    resource = None


def _rss_bytes(raw: float) -> int:
    if sys.platform == "darwin":
        return int(raw)
    return int(raw * 1024)


def measure(command: str, artifacts: list[Path], timeout: float) -> dict[str, Any]:
    argv = shlex.split(command)
    before = resource.getrusage(resource.RUSAGE_CHILDREN) if resource else None
    started = time.perf_counter()
    try:
        result = subprocess.run(argv, capture_output=True, timeout=timeout, check=False)
        timed_out = False
    except subprocess.TimeoutExpired as error:
        elapsed = time.perf_counter() - started
        return {
            "schema": "s3.bootstrap-resource-envelope.v1",
            "classification": "TIMEOUT_CHARACTERIZATION",
            "command": argv,
            "returncode": None,
            "wall_seconds": elapsed,
            "user_cpu_seconds": None,
            "system_cpu_seconds": None,
            "peak_rss_bytes": None,
            "artifacts": [],
            "stdout": (error.stdout or b"").decode("utf-8", errors="replace"),
            "stderr": (error.stderr or b"").decode("utf-8", errors="replace"),
            "performance_claim": False,
        }
    elapsed = time.perf_counter() - started
    after = resource.getrusage(resource.RUSAGE_CHILDREN) if resource else None

    artifact_rows = []
    for path in artifacts:
        artifact_rows.append(
            {
                "path": str(path),
                "exists": path.is_file(),
                "bytes": path.stat().st_size if path.is_file() else None,
            }
        )

    user_cpu = None
    system_cpu = None
    peak_rss = None
    if before is not None and after is not None:
        user_cpu = max(0.0, after.ru_utime - before.ru_utime)
        system_cpu = max(0.0, after.ru_stime - before.ru_stime)
        peak_rss = _rss_bytes(after.ru_maxrss)

    return {
        "schema": "s3.bootstrap-resource-envelope.v1",
        "classification": "CHARACTERIZATION_ONLY" if result.returncode == 0 else "COMMAND_FAILED",
        "command": argv,
        "returncode": result.returncode,
        "wall_seconds": elapsed,
        "user_cpu_seconds": user_cpu,
        "system_cpu_seconds": system_cpu,
        "peak_rss_bytes": peak_rss,
        "artifacts": artifact_rows,
        "stdout": result.stdout.decode("utf-8", errors="replace"),
        "stderr": result.stderr.decode("utf-8", errors="replace"),
        "host": {"platform": sys.platform, "os_name": os.name},
        "performance_claim": False,
        "interpretation": "Resource envelope is capacity characterization, not comparative speed evidence.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--command", required=True)
    parser.add_argument("--artifact", action="append", type=Path, default=[])
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    report = measure(args.command, args.artifact, args.timeout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OUTPUT={args.output}")
    print(f"CLASSIFICATION={report['classification']}")
    print(f"WALL_SECONDS={report['wall_seconds']}")
    print(f"PEAK_RSS_BYTES={report['peak_rss_bytes']}")
    return 0 if report["returncode"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
