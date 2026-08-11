"""
Environment detection tool for S3 benchmark suite.
Captures OS, CPU, Toolchains, Python version, and Git commits.
"""

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

def get_git_commit(repo_path: Path) -> str:
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return proc.stdout.strip()
    except Exception:
        return "UNKNOWN"

def get_tool_version(cmd: str) -> str:
    try:
        proc = subprocess.run(
            [cmd, "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        return proc.stdout.splitlines()[0].strip()
    except Exception:
        return "UNAVAILABLE"

def collect_environment_metadata(s3_repo_path: Path | None = None) -> dict[str, Any]:
    env = {
        "os": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "logical_cpus": os.cpu_count() or 1,
        "python_version": sys.version.split()[0],
        "gcc_version": get_tool_version("gcc"),
        "clang_version": get_tool_version("clang"),
        "as_version": get_tool_version("as"),
        "ld_version": get_tool_version("ld"),
    }

    # Benchmark repo commit
    benchmark_repo_path = Path(__file__).parent.parent
    env["benchmark_repo_commit"] = get_git_commit(benchmark_repo_path)

    # Upstream jsmn commit SHA
    upstream_readme = benchmark_repo_path / "benchmarks" / "jsmn" / "upstream" / "README.md"
    env["jsmn_upstream_commit"] = "25647e692c7906b96ffd2b05ca54c097948e879c"

    # S3 compiler commit
    if s3_repo_path and s3_repo_path.exists():
        env["s3_compiler_commit"] = get_git_commit(s3_repo_path)
    else:
        env["s3_compiler_commit"] = "85541b782571c80d4857d013d1fb25b4997c1eb9"

    return env

if __name__ == "__main__":
    import json
    print(json.dumps(collect_environment_metadata(), indent=2))
