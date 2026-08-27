"""Run the S3 Bootstrap Laboratory v1 evidence pipeline.

This orchestrator is deliberately read-only with respect to the S3 repository.
It composes the existing laboratory tools and writes reports only under the chosen
output directory. Missing optional stages remain unavailable; no promotion, merge,
compiler mutation, Stage2 creation, or performance claim is performed here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from tools.check_bootstrap_determinism import check as check_determinism
from tools.check_bootstrap_laboratory import validate as validate_snapshot
from tools.compare_bootstrap_stages import STAGES, compare as compare_stages
from tools.generate_bootstrap_fuzz_corpus import generate as generate_corpus
from tools.import_s3_bootstrap_evidence import import_checkout
from tools.measure_bootstrap_resource_envelope import measure as measure_resources
from tools.run_bootstrap_differential import run_campaign
from tools.summarize_bootstrap_semantic_coverage import summarize as summarize_coverage

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "laboratory" / "bootstrap-v1" / "contract.json"

HARD_DIFFERENTIAL_FAILURES = {
    "SEMANTIC_MISMATCH",
    "REFERENCE_FAIL",
    "REFERENCE_TIMEOUT",
    "STAGE1_FAIL",
    "STAGE1_TIMEOUT",
}


def _write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _has_hard_differential_failure(report: dict[str, Any]) -> bool:
    counts = report.get("counts", {})
    return any(name in counts and counts[name] for name in HARD_DIFFERENTIAL_FAILURES)


def run_lab(
    *,
    s3_repo: Path,
    benchmark_repo: Path,
    output_dir: Path,
    contract_path: Path = DEFAULT_CONTRACT,
    expected_s3_commit: str | None = None,
    expected_benchmark_commit: str | None = None,
    reference_command: str | None = None,
    stage1_command: str | None = None,
    reference_observation: str = "stdout",
    stage1_observation: str = "stdout",
    blocked_marker: str | None = "S3_STAGE1_EMITTER_BLOCKED",
    differential_timeout: float = 30.0,
    resource_command: str | None = None,
    resource_artifacts: list[Path] | None = None,
    resource_timeout: float = 120.0,
    determinism_source: Path | None = None,
    determinism_command: str | None = None,
    determinism_repeats: int = 3,
    determinism_timeout: float = 60.0,
    stage_artifacts: dict[str, Path | None] | None = None,
    stage_observations: dict[str, Path | None] | None = None,
) -> tuple[dict[str, Any], int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    contract = json.loads(contract_path.read_text(encoding="utf-8"))

    corpus_dir = output_dir / "corpus"
    manifest = generate_corpus(corpus_dir)
    manifest_path = corpus_dir / "manifest.json"

    snapshot = import_checkout(
        s3_repo,
        benchmark_repo,
        expected_s3_commit=expected_s3_commit,
        expected_benchmark_commit=expected_benchmark_commit,
    )
    snapshot_path = output_dir / "current-bootstrap.json"
    _write(snapshot_path, snapshot)

    validation = validate_snapshot(snapshot, contract)
    _write(output_dir / "snapshot-validation.json", validation)

    components: dict[str, Any] = {
        "corpus": {
            "status": "PASS",
            "case_count": manifest["case_count"],
            "path": str(manifest_path),
        },
        "snapshot": {
            "status": validation["status"],
            "path": str(snapshot_path),
        },
        "differential": {"status": "NOT_RUN"},
        "semantic_coverage": {"status": "NOT_RUN"},
        "resources": {"status": "NOT_RUN"},
        "determinism": {"status": "NOT_RUN"},
        "stage_equivalence": {"status": "NOT_AVAILABLE"},
    }
    hard_failure = validation["status"] != "PASS"

    if reference_command is not None:
        differential = run_campaign(
            manifest_path,
            reference_command=reference_command,
            stage1_command=stage1_command,
            blocked_marker=blocked_marker,
            timeout=differential_timeout,
            reference_mode=reference_observation,
            stage1_mode=stage1_observation,
        )
        differential_path = output_dir / "differential.json"
        _write(differential_path, differential)
        differential_hard_failure = _has_hard_differential_failure(differential)
        components["differential"] = {
            "status": "FAIL" if differential_hard_failure else "PASS",
            "path": str(differential_path),
            "counts": differential["counts"],
            "stage1_invoked": differential["stage1_invoked"],
        }
        hard_failure = hard_failure or differential_hard_failure

        coverage = summarize_coverage(snapshot, differential)
        coverage_path = output_dir / "semantic-coverage.json"
        _write(coverage_path, coverage)
        coverage_fail = bool(coverage["semantic_mismatches"])
        components["semantic_coverage"] = {
            "status": "FAIL" if coverage_fail else "PASS",
            "path": str(coverage_path),
            "case_parity_pass": coverage["case_parity_pass"],
            "case_count": coverage["case_count"],
            "semantic_mismatches": coverage["semantic_mismatches"],
        }
        hard_failure = hard_failure or coverage_fail

    if resource_command is not None:
        resource_report = measure_resources(
            resource_command,
            resource_artifacts or [],
            resource_timeout,
        )
        resource_path = output_dir / "resource-envelope.json"
        _write(resource_path, resource_report)
        components["resources"] = {
            "status": resource_report["classification"],
            "path": str(resource_path),
            "performance_claim": False,
        }
        # A requested resource command failure is evidence of command failure, but
        # characterization ineligibility must never be interpreted as performance FAIL.
        if resource_report["classification"] in {"COMMAND_FAILED", "TIMEOUT_CHARACTERIZATION"}:
            hard_failure = True

    if (determinism_source is None) != (determinism_command is None):
        raise ValueError("determinism_source and determinism_command must be supplied together")
    if determinism_source is not None and determinism_command is not None:
        determinism = check_determinism(
            determinism_source,
            determinism_command,
            determinism_repeats,
            determinism_timeout,
        )
        determinism_path = output_dir / "determinism.json"
        _write(determinism_path, determinism)
        components["determinism"] = {
            "status": determinism["classification"],
            "path": str(determinism_path),
            "semantic_correctness_claim": False,
        }
        if determinism["classification"] != "PASS":
            hard_failure = True

    artifacts = stage_artifacts or {stage: None for stage in STAGES}
    observations = stage_observations or {stage: None for stage in STAGES}
    equivalence = compare_stages(artifacts, observations)
    equivalence_path = output_dir / "stage-equivalence.json"
    _write(equivalence_path, equivalence)
    equivalence_state = equivalence["stage1_stage2_stage3_observable_equivalence"]
    components["stage_equivalence"] = {
        "status": equivalence_state,
        "path": str(equivalence_path),
        "stage2_stage3_byte_identity": equivalence["stage2_stage3_byte_identity"],
    }
    if equivalence_state == "FAIL":
        hard_failure = True

    summary = {
        "schema": "s3.bootstrap-laboratory-run.v1",
        "status": "FAIL" if hard_failure else "PASS",
        "components": components,
        "provenance": snapshot["provenance"],
        "bootstrap": snapshot["bootstrap"],
        "semantic_ir": snapshot["semantic_ir"],
        "promotion": {
            "performed": False,
            "self_hosting_claim": False,
            "performance_claim": False,
            "compiler_mutated": False,
        },
        "interpretation": (
            "PASS means the requested evidence pipeline completed without a hard contradiction. "
            "It does not mean Stage1 semantic closure, self-hosting, Stage2 creation, or performance qualification."
        ),
    }
    _write(output_dir / "summary.json", summary)
    return summary, 2 if hard_failure else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--benchmark-repo", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--expected-s3-commit")
    parser.add_argument("--expected-benchmark-commit")

    parser.add_argument("--reference-command")
    parser.add_argument("--stage1-command")
    parser.add_argument(
        "--reference-observation",
        choices=("stdout", "program-return-line", "exit-code"),
        default="stdout",
    )
    parser.add_argument(
        "--stage1-observation",
        choices=("stdout", "program-return-line", "exit-code"),
        default="stdout",
    )
    parser.add_argument("--blocked-marker", default="S3_STAGE1_EMITTER_BLOCKED")
    parser.add_argument("--differential-timeout", type=float, default=30.0)

    parser.add_argument("--resource-command")
    parser.add_argument("--resource-artifact", action="append", type=Path, default=[])
    parser.add_argument("--resource-timeout", type=float, default=120.0)

    parser.add_argument("--determinism-source", type=Path)
    parser.add_argument("--determinism-command")
    parser.add_argument("--determinism-repeats", type=int, default=3)
    parser.add_argument("--determinism-timeout", type=float, default=60.0)

    for stage in STAGES:
        parser.add_argument(f"--{stage}-artifact", type=Path)
        parser.add_argument(f"--{stage}-observation", type=Path)

    args = parser.parse_args(argv)
    if args.determinism_repeats < 2:
        parser.error("--determinism-repeats must be at least 2")

    stage_artifacts = {stage: getattr(args, f"{stage}_artifact") for stage in STAGES}
    stage_observations = {stage: getattr(args, f"{stage}_observation") for stage in STAGES}
    summary, exit_code = run_lab(
        s3_repo=args.s3_repo,
        benchmark_repo=args.benchmark_repo,
        output_dir=args.output_dir,
        contract_path=args.contract,
        expected_s3_commit=args.expected_s3_commit,
        expected_benchmark_commit=args.expected_benchmark_commit,
        reference_command=args.reference_command,
        stage1_command=args.stage1_command,
        reference_observation=args.reference_observation,
        stage1_observation=args.stage1_observation,
        blocked_marker=args.blocked_marker,
        differential_timeout=args.differential_timeout,
        resource_command=args.resource_command,
        resource_artifacts=args.resource_artifact,
        resource_timeout=args.resource_timeout,
        determinism_source=args.determinism_source,
        determinism_command=args.determinism_command,
        determinism_repeats=args.determinism_repeats,
        determinism_timeout=args.determinism_timeout,
        stage_artifacts=stage_artifacts,
        stage_observations=stage_observations,
    )
    print(f"OUTPUT_DIR={args.output_dir}")
    print(f"STATUS={summary['status']}")
    print(f"STAGE1={summary['bootstrap']['stage1']}")
    print(f"SELF_EMIT={summary['bootstrap']['stage1_self_emit']}")
    print(f"STAGE2={summary['bootstrap']['stage2']}")
    print(f"STAGE3={summary['bootstrap']['stage3']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
