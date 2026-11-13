"""Check deterministic bootstrap output for a command template.

Use {source} and optionally {output} placeholders in --command. If {output} is
present the generated artifact bytes are hashed; otherwise stdout bytes are hashed.
This is reproducibility evidence only and does not imply semantic correctness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shlex
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _argv(template: str, source: Path, output: Path) -> list[str]:
    return [
        item.replace("{source}", str(source)).replace("{output}", str(output))
        for item in shlex.split(template)
    ]


def check(source: Path, command: str, repeats: int, timeout: float) -> dict[str, Any]:
    uses_output = "{output}" in command
    runs: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="s3-bootstrap-determinism-") as temp:
        root = Path(temp)
        for index in range(repeats):
            output = root / f"artifact-{index}.bin"
            argv = _argv(command, source, output)
            started = time.perf_counter()
            try:
                result = subprocess.run(argv, capture_output=True, timeout=timeout, check=False)
            except subprocess.TimeoutExpired as error:
                runs.append(
                    {
                        "index": index,
                        "returncode": None,
                        "status": "TIMEOUT",
                        "wall_seconds": time.perf_counter() - started,
                        "digest": None,
                        "stderr": (error.stderr or b"").decode("utf-8", errors="replace"),
                    }
                )
                continue
            digest = None
            status = "COMPLETED"
            if result.returncode == 0:
                if uses_output:
                    if output.is_file():
                        digest = _sha256(output.read_bytes())
                    else:
                        status = "MISSING_ARTIFACT"
                else:
                    digest = _sha256(result.stdout)
            runs.append(
                {
                    "index": index,
                    "returncode": result.returncode,
                    "status": status,
                    "wall_seconds": time.perf_counter() - started,
                    "digest": digest,
                    "stdout_sha256": _sha256(result.stdout),
                    "stderr": result.stderr.decode("utf-8", errors="replace"),
                }
            )

    successful = [run for run in runs if run["returncode"] == 0 and run["digest"]]
    digests = {run["digest"] for run in successful}
    all_success = len(successful) == repeats
    deterministic = all_success and len(digests) == 1
    if deterministic:
        classification = "PASS"
    elif not all_success:
        classification = "INCOMPLETE_OR_FAILED"
    else:
        classification = "NONDETERMINISTIC"
    return {
        "schema": "s3.bootstrap-determinism.v1",
        "source": str(source),
        "source_sha256": _sha256(source.read_bytes()),
        "repeat_count": repeats,
        "artifact_mode": uses_output,
        "classification": classification,
        "deterministic": deterministic,
        "unique_digests": sorted(digests),
        "runs": runs,
        "semantic_correctness_claim": False,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--command", required=True)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.repeats < 2:
        parser.error("--repeats must be at least 2")
    report = check(args.source, args.command, args.repeats, args.timeout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OUTPUT={args.output}")
    print(f"CLASSIFICATION={report['classification']}")
    print(f"UNIQUE_DIGESTS={len(report['unique_digests'])}")
    return 0 if report["classification"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
