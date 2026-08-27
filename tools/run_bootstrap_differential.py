"""Run a pinned bootstrap corpus against reference and optional Stage1 commands.

The runner compares observable stdout and exit status. A missing Stage1 command is
reported as NOT_RUN, not failure. Non-zero Stage1 runs can be classified BLOCKED
only when an explicit blocker marker is observed; they are never silently treated
as unsupported/pass.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shlex
import subprocess
import time
from pathlib import Path
from typing import Any


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _render_command(template: str, source: Path) -> list[str]:
    return [part.replace("{source}", str(source)) for part in shlex.split(template)]


def _run(template: str, source: Path, timeout: float) -> dict[str, Any]:
    command = _render_command(template, source)
    started = time.perf_counter()
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        elapsed = time.perf_counter() - started
        stdout = error.stdout or b""
        stderr = error.stderr or b""
        return {
            "command": command,
            "status": "TIMEOUT",
            "returncode": None,
            "wall_seconds": elapsed,
            "stdout_sha256": _sha256_bytes(stdout),
            "stderr_sha256": _sha256_bytes(stderr),
            "stdout": stdout.decode("utf-8", errors="replace"),
            "stderr": stderr.decode("utf-8", errors="replace"),
        }
    elapsed = time.perf_counter() - started
    return {
        "command": command,
        "status": "COMPLETED",
        "returncode": result.returncode,
        "wall_seconds": elapsed,
        "stdout_sha256": _sha256_bytes(result.stdout),
        "stderr_sha256": _sha256_bytes(result.stderr),
        "stdout": result.stdout.decode("utf-8", errors="replace"),
        "stderr": result.stderr.decode("utf-8", errors="replace"),
    }


def classify_observations(
    reference: dict[str, Any],
    stage1: dict[str, Any] | None,
    *,
    blocked_marker: str | None = None,
) -> str:
    if reference.get("status") == "TIMEOUT":
        return "REFERENCE_TIMEOUT"
    if reference.get("returncode") != 0:
        return "REFERENCE_FAIL"
    if stage1 is None:
        return "STAGE1_NOT_RUN"
    if stage1.get("status") == "TIMEOUT":
        return "STAGE1_TIMEOUT"
    if stage1.get("returncode") != 0:
        combined = f"{stage1.get('stdout', '')}\n{stage1.get('stderr', '')}"
        if blocked_marker and blocked_marker in combined:
            return "STAGE1_BLOCKED"
        return "STAGE1_FAIL"
    if stage1.get("stdout_sha256") != reference.get("stdout_sha256"):
        return "SEMANTIC_MISMATCH"
    return "PASS"


def run_campaign(
    manifest_path: Path,
    *,
    reference_command: str,
    stage1_command: str | None,
    blocked_marker: str | None,
    timeout: float,
) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    base = manifest_path.parent
    records: list[dict[str, Any]] = []
    counts: dict[str, int] = {}

    for case in manifest.get("cases", []):
        source = base / case["path"]
        source_bytes = source.read_bytes()
        actual_sha = _sha256_bytes(source_bytes)
        if actual_sha != case["sha256"]:
            raise ValueError(f"source hash mismatch for {case['case_id']}")
        reference = _run(reference_command, source, timeout)
        stage1 = _run(stage1_command, source, timeout) if stage1_command else None
        classification = classify_observations(
            reference, stage1, blocked_marker=blocked_marker
        )
        counts[classification] = counts.get(classification, 0) + 1
        records.append(
            {
                "case_id": case["case_id"],
                "category": case["category"],
                "required_surfaces": case.get("required_surfaces", []),
                "source_sha256": actual_sha,
                "classification": classification,
                "reference": reference,
                "stage1": stage1,
            }
        )

    return {
        "schema": "s3.bootstrap-differential.v1",
        "manifest_sha256": _sha256_bytes(manifest_path.read_bytes()),
        "case_count": len(records),
        "stage1_invoked": stage1_command is not None,
        "counts": dict(sorted(counts.items())),
        "cases": records,
        "promotion_policy": (
            "Only PASS means observable reference/Stage1 parity for that case. "
            "STAGE1_BLOCKED is capability evidence, not correctness PASS."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--reference-command", required=True)
    parser.add_argument("--stage1-command")
    parser.add_argument("--blocked-marker", default="S3_STAGE1_EMITTER_BLOCKED")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    report = run_campaign(
        args.manifest,
        reference_command=args.reference_command,
        stage1_command=args.stage1_command,
        blocked_marker=args.blocked_marker,
        timeout=args.timeout,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OUTPUT={args.output}")
    print(f"CASES={report['case_count']}")
    print(f"COUNTS={json.dumps(report['counts'], sort_keys=True)}")
    hard_failures = {
        "SEMANTIC_MISMATCH",
        "REFERENCE_FAIL",
        "REFERENCE_TIMEOUT",
        "STAGE1_FAIL",
        "STAGE1_TIMEOUT",
    }
    return 2 if any(key in report["counts"] for key in hard_failures) else 0


if __name__ == "__main__":
    raise SystemExit(main())
