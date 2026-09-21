"""Hosted/native adapters for the bounded 2.0.1 candidate matrix."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import math
import os
from pathlib import Path
import re
import sys
from tempfile import TemporaryDirectory
from typing import Any

from protocol.provenance import require_commit

EXPECTED_S3_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"


@dataclass(frozen=True, slots=True)
class CandidateObservation:
    workload_id: str
    size: str
    status: str
    expected: int
    observed: int | float | None
    hosted: str
    native: str
    source_sha256: str
    logical_shape: str
    physical_layout: str
    index_mapping: str
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _load_s3():
    repo = Path(os.environ.get("S3_REPO", r"C:\Users\samue\Downloads\S3\S3-Benchmarks\scratch\s3-e07-checked-20260920")).resolve()
    require_commit(repo, os.environ.get("S3_COMMIT", EXPECTED_S3_SHA), label="S3 candidate")
    if str(repo) not in sys.path:
        sys.path.insert(0, str(repo))
    from bootstrap.s3.pipeline import compile_source, run_source
    return compile_source, run_source


def run_hosted(case, *, optimization: str = "O0") -> int | float:
    _compile_source, run_source = _load_s3()
    result = run_source(case.source, optimization=optimization)
    if isinstance(result, bool) or not isinstance(result, (int, float)):
        raise TypeError(f"S3 candidate returned non-numeric result: {result!r}")
    return result


def run_hosted_matrix(cases) -> list[CandidateObservation]:
    result: list[CandidateObservation] = []
    for case in cases:
        try:
            observed_o0 = run_hosted(case, optimization="O0")
            observed_o1 = run_hosted(case, optimization="O1")
            if not math.isclose(float(observed_o0), float(observed_o1), rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError(f"O0/O1 disagreement: {observed_o0} != {observed_o1}")
            if not math.isclose(float(observed_o0), float(case.expected), rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError(f"oracle mismatch: expected {case.expected}, observed {observed_o0}")
            result.append(CandidateObservation(case.workload_id, case.size, "CORRECTNESS_PASS", case.expected, observed_o0, "PASS", "NOT_RUN", hashlib.sha256(case.source.encode()).hexdigest(), case.logical_shape, case.physical_layout, case.index_mapping))
        except Exception as exc:
            result.append(CandidateObservation(case.workload_id, case.size, "TRUE_LANGUAGE_CAPABILITY_BLOCKER", case.expected, None, "FAIL", "NOT_RUN", hashlib.sha256(case.source.encode()).hexdigest(), case.logical_shape, case.physical_layout, case.index_mapping, f"{type(exc).__name__}: {exc}"))
    return result


def parse_native_result(stdout: str) -> int:
    match = re.fullmatch(r"program returned: (-?\d+)", stdout.strip())
    if match is None:
        raise ValueError(f"unexpected native canary output: {stdout!r}")
    return int(match.group(1))


def native_case(case, native_toolchain, backend_type) -> tuple[int, str]:
    compile_source, _run_source = _load_s3()
    with TemporaryDirectory(prefix="s3bench-native-") as directory:
        program = compile_source(case.source, optimization="O0").assembly
        text = backend_type(register_allocation=True).generate(program)
        executable = native_toolchain.build(text, Path(directory) / "candidate")
        completed = native_toolchain.run(executable)
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr or f"native exit {completed.returncode}")
        return parse_native_result(completed.stdout), "CANARY"
