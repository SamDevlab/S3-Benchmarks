"""Run a pinned bootstrap corpus against reference and optional Stage1 commands.

The runner compares an explicit observable value rather than assuming stdout is the
program semantics. Supported observation modes are:

- stdout: successful command stdout bytes;
- program-return-line: integer parsed from ``program returned: N``;
- exit-code: process return code, intended for an already-built/native program.

A missing Stage1 command is NOT_RUN, not failure. An explicit blocker marker takes
precedence over exit-code observation and is reported as STAGE1_BLOCKED.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import subprocess
import time
from pathlib import Path
from typing import Any

OBSERVATION_MODES = ("stdout", "program-return-line", "exit-code")
_RETURN_LINE = re.compile(r"(?:^|\n)program returned:\s*(-?\d+)\s*(?:\n|$)")


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


def _blocked(run: dict[str, Any], marker: str | None) -> bool:
    if not marker:
        return False
    combined = f"{run.get('stdout', '')}\n{run.get('stderr', '')}"
    return marker in combined


def extract_observation(run: dict[str, Any], mode: str) -> tuple[bool, str | None]:
    """Return (valid, canonical observable value).

    ``exit-code`` intentionally accepts non-zero values because it is designed for
    an already-built program whose process status *is* the observable result. For
    compiler/driver commands use ``stdout`` or ``program-return-line`` instead.
    """
    if mode not in OBSERVATION_MODES:
        raise ValueError(f"unsupported observation mode: {mode}")
    if run.get("status") != "COMPLETED":
        return False, None

    if mode == "exit-code":
        code = run.get("returncode")
        return (isinstance(code, int), str(code) if isinstance(code, int) else None)

    if run.get("returncode") != 0:
        return False, None

    stdout = str(run.get("stdout", ""))
    if mode == "stdout":
        return True, stdout

    match = _RETURN_LINE.search(stdout)
    if not match:
        return False, None
    return True, match.group(1)


def classify_observations(
    reference: dict[str, Any],
    stage1: dict[str, Any] | None,
    *,
    blocked_marker: str | None = None,
    reference_mode: str = "stdout",
    stage1_mode: str = "stdout",
) -> str:
    if reference.get("status") == "TIMEOUT":
        return "REFERENCE_TIMEOUT"
    reference_valid, reference_value = extract_observation(reference, reference_mode)
    if not reference_valid:
        return "REFERENCE_FAIL"

    if stage1 is None:
        return "STAGE1_NOT_RUN"
    if stage1.get("status") == "TIMEOUT":
        return "STAGE1_TIMEOUT"
    if _blocked(stage1, blocked_marker):
        return "STAGE1_BLOCKED"

    stage1_valid, stage1_value = extract_observation(stage1, stage1_mode)
    if not stage1_valid:
        return "STAGE1_FAIL"
    if stage1_value != reference_value:
        return "SEMANTIC_MISMATCH"
    return "PASS"


def run_campaign(
    manifest_path: Path,
    *,
    reference_command: str,
    stage1_command: str | None,
    blocked_marker: str | None,
    timeout: float,
    reference_mode: str = "stdout",
    stage1_mode: str = "stdout",
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
            reference,
            stage1,
            blocked_marker=blocked_marker,
            reference_mode=reference_mode,
            stage1_mode=stage1_mode,
        )
        counts[classification] = counts.get(classification, 0) + 1
        reference_valid, reference_value = extract_observation(reference, reference_mode)
        stage1_valid = False
        stage1_value = None
        if stage1 is not None and not _blocked(stage1, blocked_marker):
            stage1_valid, stage1_value = extract_observation(stage1, stage1_mode)
        records.append(
            {
                "case_id": case["case_id"],
                "category": case["category"],
                "required_surfaces": case.get("required_surfaces", []),
                "source_sha256": actual_sha,
                "classification": classification,
                "reference_observation": {
                    "mode": reference_mode,
                    "valid": reference_valid,
                    "value": reference_value,
                },
                "stage1_observation": None
                if stage1 is None
                else {
                    "mode": stage1_mode,
                    "valid": stage1_valid,
                    "value": stage1_value,
                },
                "reference": reference,
                "stage1": stage1,
            }
        )

    return {
        "schema": "s3.bootstrap-differential.v2",
        "manifest_sha256": _sha256_bytes(manifest_path.read_bytes()),
        "case_count": len(records),
        "stage1_invoked": stage1_command is not None,
        "observation_contract": {
            "reference": reference_mode,
            "stage1": stage1_mode,
        },
        "counts": dict(sorted(counts.items())),
        "cases": records,
        "promotion_policy": (
            "Only PASS means equality under the explicit observation contract for that case. "
            "STAGE1_BLOCKED is capability evidence, not correctness PASS. "
            "exit-code mode must only be used when process status is intentionally the program observable."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--reference-command", required=True)
    parser.add_argument("--stage1-command")
    parser.add_argument("--reference-observation", choices=OBSERVATION_MODES, default="stdout")
    parser.add_argument("--stage1-observation", choices=OBSERVATION_MODES, default="stdout")
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
        reference_mode=args.reference_observation,
        stage1_mode=args.stage1_observation,
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
