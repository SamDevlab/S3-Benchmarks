"""Validate and compare independently pinned pre-V8 benchmark observations.

This tool reports measurement stages separately. It does not execute the S3
compiler or a workload, infer a speedup from an unqualified record, or mutate
historical evidence.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "protocol" / "pre-v8-experiment-groups-v1.json"
SCHEMA_PATH = ROOT / "protocol" / "pre-v8-longitudinal-result-v1.schema.json"
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
GROUPS = ("PURE PERFORMANCE", "CONTROLLED EFFICIENCY", "PROFILE DIFFERENTIAL")
LANGUAGES = ("S3", "C", "Rust", "Zig")
STAGES = ("correctness", "compilation", "execution", "binary_size")
STATUSES = ("PASS", "FAIL", "BLOCKED", "NOT_RUN")
S3_REPOSITORY = "https://github.com/SamDevlab/S3.git"


class ValidationError(ValueError):
    """A record violates the versioned longitudinal measurement contract."""


def _object(value: object, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{label} must be an object")
    return value


def _keys(value: dict[str, Any], required: set[str], label: str) -> None:
    missing = required - value.keys()
    extra = value.keys() - required
    if missing:
        raise ValidationError(f"{label} is missing: {', '.join(sorted(missing))}")
    if extra:
        raise ValidationError(f"{label} has unsupported fields: {', '.join(sorted(extra))}")


def _string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label} must be a non-empty string")
    return value


def _integer(value: object, label: str, minimum: int = 1) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValidationError(f"{label} must be an integer >= {minimum}")
    return value


def _digest(value: object, pattern: re.Pattern[str], label: str) -> str:
    if not isinstance(value, str) or pattern.fullmatch(value) is None:
        raise ValidationError(f"{label} must match the required lowercase hexadecimal digest format")
    return value


def validate_plan(plan: object) -> dict[str, Any]:
    plan = _object(plan, "experiment plan")
    if plan.get("schema_version") != "s3.pre-v8-experiment-groups.v1":
        raise ValidationError("unsupported experiment plan schema")
    if plan.get("status") != "PREPARATION_ONLY" or plan.get("ready_to_measure_v8") is not False:
        raise ValidationError("plan must remain preparation-only and not ready for V8 measurement")

    dependency = _object(plan.get("baseline_dependency"), "baseline_dependency")
    if dependency.get("repository") != S3_REPOSITORY:
        raise ValidationError("baseline_dependency must target the S3 compiler repository")
    if dependency.get("qualified_v7_commit") is not None:
        raise ValidationError("a V7 baseline must not be invented or selected before qualification")
    if dependency.get("accept_moving_refs") is not False:
        raise ValidationError("moving compiler references are forbidden")

    if plan.get("languages") != list(LANGUAGES):
        raise ValidationError("planned language matrix must contain S3, C, Rust, and Zig")
    if plan.get("comparison_stages") != list(STAGES):
        raise ValidationError("comparison stages must remain separate and complete")
    groups = plan.get("groups")
    if not isinstance(groups, list) or tuple(
        item.get("id") if isinstance(item, dict) else None for item in groups
    ) != GROUPS:
        raise ValidationError("the three future experiment groups are missing or out of order")
    for group in groups:
        if group.get("status") != "PLANNED_NOT_IMPLEMENTED":
            raise ValidationError(f"{group.get('id')} must remain planned, not implemented")
        if group.get("profiles") != [] or group.get("profile_implementation_claimed") is not False:
            raise ValidationError(f"{group.get('id')} must not claim execution profiles exist")
    return plan


def _status(stage: dict[str, Any], label: str) -> str:
    status = stage.get("status")
    if status not in STATUSES:
        raise ValidationError(f"{label}.status must be one of {', '.join(STATUSES)}")
    return status


def validate_record(record: object) -> dict[str, Any]:
    record = _object(record, "record")
    _keys(
        record,
        {
            "schema_version", "run_id", "campaign_group", "benchmark_repo_revision",
            "compiler", "implementation", "workload", "environment", "protocol", "stages",
        },
        "record",
    )
    if record["schema_version"] != "s3.pre-v8-longitudinal-result.v1":
        raise ValidationError("unsupported result schema")
    _string(record["run_id"], "run_id")
    if record["campaign_group"] not in GROUPS:
        raise ValidationError("campaign_group is not in the prepared V8 taxonomy")
    _digest(record["benchmark_repo_revision"], SHA1, "benchmark_repo_revision")

    compiler = _object(record["compiler"], "compiler")
    allowed_compiler_keys = {
        "language", "name", "version", "repository", "source_revision",
        "working_tree_clean", "executable_sha256",
    }
    if compiler.keys() - allowed_compiler_keys or {
        "language", "name", "version", "executable_sha256",
    } - compiler.keys():
        raise ValidationError("compiler identity fields are incomplete or unsupported")
    if compiler["language"] not in LANGUAGES:
        raise ValidationError("compiler.language must be S3, C, Rust, or Zig")
    _string(compiler["name"], "compiler.name")
    _string(compiler["version"], "compiler.version")
    _digest(compiler["executable_sha256"], SHA256, "compiler.executable_sha256")
    if compiler["language"] == "S3":
        if compiler.get("repository") != S3_REPOSITORY:
            raise ValidationError("S3 compiler repository must be the independent S3 source URL")
        _digest(compiler.get("source_revision"), SHA1, "S3 compiler.source_revision")
        if compiler.get("working_tree_clean") is not True:
            raise ValidationError("S3 compiler must be built from a clean, immutable checkout")
    elif compiler.get("source_revision") is not None:
        _digest(compiler["source_revision"], SHA1, "compiler.source_revision")

    implementation = _object(record["implementation"], "implementation")
    _keys(
        implementation,
        {"repository", "revision", "source_sha256", "build_recipe_sha256"},
        "implementation",
    )
    _string(implementation["repository"], "implementation.repository")
    _digest(implementation["revision"], SHA1, "implementation.revision")
    _digest(implementation["source_sha256"], SHA256, "implementation.source_sha256")
    _digest(implementation["build_recipe_sha256"], SHA256, "implementation.build_recipe_sha256")

    workload = _object(record["workload"], "workload")
    _keys(workload, {"id", "fixture_id", "dataset_sha256", "work_units"}, "workload")
    _string(workload["id"], "workload.id")
    _string(workload["fixture_id"], "workload.fixture_id")
    _digest(workload["dataset_sha256"], SHA256, "workload.dataset_sha256")
    _integer(workload["work_units"], "workload.work_units")

    environment = _object(record["environment"], "environment")
    _keys(environment, {"os", "architecture", "fingerprint_sha256"}, "environment")
    _string(environment["os"], "environment.os")
    _string(environment["architecture"], "environment.architecture")
    _digest(environment["fingerprint_sha256"], SHA256, "environment.fingerprint_sha256")

    protocol = _object(record["protocol"], "protocol")
    _keys(
        protocol,
        {"id", "sha256", "warmups", "samples", "iterations_per_sample", "ordering"},
        "protocol",
    )
    _string(protocol["id"], "protocol.id")
    _digest(protocol["sha256"], SHA256, "protocol.sha256")
    _integer(protocol["warmups"], "protocol.warmups", 0)
    _integer(protocol["samples"], "protocol.samples", 3)
    _integer(protocol["iterations_per_sample"], "protocol.iterations_per_sample")
    if protocol["ordering"] not in {"interleaved", "paired", "serial"}:
        raise ValidationError("protocol.ordering is unsupported")

    stages = _object(record["stages"], "stages")
    _keys(stages, set(STAGES), "stages")
    correctness = _object(stages["correctness"], "stages.correctness")
    _keys(correctness, {"status", "oracle", "output_sha256"}, "stages.correctness")
    correctness_status = _status(correctness, "stages.correctness")
    if correctness_status == "PASS":
        _string(correctness["oracle"], "stages.correctness.oracle")
        _digest(correctness["output_sha256"], SHA256, "stages.correctness.output_sha256")
    elif correctness["output_sha256"] is not None:
        raise ValidationError("non-passing correctness cannot publish a passing output digest")

    compilation = _object(stages["compilation"], "stages.compilation")
    _keys(compilation, {"status", "elapsed_ns", "exit_code"}, "stages.compilation")
    compilation_status = _status(compilation, "stages.compilation")
    if compilation_status == "PASS":
        _integer(compilation["elapsed_ns"], "stages.compilation.elapsed_ns")
        if compilation["exit_code"] != 0:
            raise ValidationError("passing compilation requires exit_code=0")
    elif compilation["elapsed_ns"] is not None:
        raise ValidationError("non-passing compilation cannot publish a compile duration")

    execution = _object(stages["execution"], "stages.execution")
    _keys(execution, {"status", "scope", "samples_ns"}, "stages.execution")
    execution_status = _status(execution, "stages.execution")
    if execution["scope"] not in {"process_e2e", "direct_kernel", "in_process_ffi"}:
        raise ValidationError("stages.execution.scope is unsupported")
    samples = execution["samples_ns"]
    if not isinstance(samples, list):
        raise ValidationError("stages.execution.samples_ns must be an array")
    if execution_status == "PASS":
        if correctness_status != "PASS" or compilation_status != "PASS":
            raise ValidationError("execution can pass only after correctness and compilation pass")
        if len(samples) != protocol["samples"]:
            raise ValidationError("execution sample count does not match the pinned protocol")
        for index, sample in enumerate(samples):
            _integer(sample, f"stages.execution.samples_ns[{index}]")
    elif samples:
        raise ValidationError("non-passing execution must not contain timing samples")

    binary_size = _object(stages["binary_size"], "stages.binary_size")
    _keys(binary_size, {"status", "bytes", "format"}, "stages.binary_size")
    binary_status = _status(binary_size, "stages.binary_size")
    if binary_status == "PASS":
        if compilation_status != "PASS":
            raise ValidationError("binary size can pass only after compilation passes")
        _integer(binary_size["bytes"], "stages.binary_size.bytes")
        if binary_size["format"] not in {"ELF", "PE", "Mach-O", "WASM", "OTHER"}:
            raise ValidationError("binary size format is unsupported")
    elif binary_size["bytes"] is not None:
        raise ValidationError("non-passing binary-size stage cannot publish a size")
    return record


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"cannot read JSON {path}: {exc}") from exc


def _protocol_identity(record: dict[str, Any]) -> tuple[Any, ...]:
    protocol = record["protocol"]
    return (
        protocol["id"], protocol["sha256"], protocol["warmups"], protocol["samples"],
        protocol["iterations_per_sample"], protocol["ordering"],
    )


def compare_records(records: list[dict[str, Any]], mode: str) -> dict[str, Any]:
    if mode not in {"revision", "language"}:
        raise ValidationError("comparison mode must be revision or language")
    if len(records) < 2:
        raise ValidationError("at least two records are required for comparison")
    for record in records:
        validate_record(record)

    first = records[0]
    invariants = (
        ("campaign_group", lambda r: r["campaign_group"]),
        ("workload", lambda r: (r["workload"]["id"], r["workload"]["fixture_id"],
                                 r["workload"]["dataset_sha256"], r["workload"]["work_units"])),
        ("environment", lambda r: r["environment"]["fingerprint_sha256"]),
        ("protocol", _protocol_identity),
        ("execution scope", lambda r: r["stages"]["execution"]["scope"]),
    )
    for label, identity in invariants:
        if any(identity(record) != identity(first) for record in records[1:]):
            raise ValidationError(f"records are not comparable: {label} differs")

    if mode == "revision":
        languages = {record["compiler"]["language"] for record in records}
        names = {record["compiler"]["name"] for record in records}
        source_hashes = {record["implementation"]["source_sha256"] for record in records}
        recipe_hashes = {record["implementation"]["build_recipe_sha256"] for record in records}
        revisions = {
            record["compiler"].get("source_revision") or record["compiler"]["version"]
            for record in records
        }
        if len(languages) != 1 or len(names) != 1:
            raise ValidationError("revision mode requires the same compiler language and name")
        if len(source_hashes) != 1 or len(recipe_hashes) != 1:
            raise ValidationError("revision mode requires identical workload source and build recipe")
        if len(revisions) != len(records):
            raise ValidationError("revision mode requires distinct immutable compiler revisions")
    else:
        languages = [record["compiler"]["language"] for record in records]
        if len(set(languages)) != len(records):
            raise ValidationError("language mode requires exactly one record per language")

    rows = []
    for record in records:
        stages = record["stages"]
        executable = stages["execution"]
        eligible = all(
            stages[stage]["status"] == "PASS"
            for stage in ("correctness", "compilation", "execution")
        )
        median_ns = statistics.median(executable["samples_ns"]) if eligible else None
        per_unit = (
            median_ns / (
                record["workload"]["work_units"]
                * record["protocol"]["iterations_per_sample"]
            )
            if median_ns is not None else None
        )
        rows.append({
            "language": record["compiler"]["language"],
            "compiler": record["compiler"]["name"],
            "compiler_version": record["compiler"]["version"],
            "compiler_revision": record["compiler"].get("source_revision"),
            "correctness": stages["correctness"]["status"],
            "compilation": {
                "status": stages["compilation"]["status"],
                "elapsed_ns": stages["compilation"]["elapsed_ns"],
            },
            "execution": {
                "status": executable["status"],
                "scope": executable["scope"],
                "median_ns_per_sample": median_ns,
                "median_ns_per_work_unit": per_unit,
                "eligible": eligible,
            },
            "binary_size": {
                "status": stages["binary_size"]["status"],
                "bytes": stages["binary_size"]["bytes"],
                "format": stages["binary_size"]["format"],
            },
        })
    return {
        "comparison_mode": mode,
        "classification": "DESCRIPTIVE_ONLY_NO_SPEEDUP_CLAIM",
        "workload_id": first["workload"]["id"],
        "fixture_id": first["workload"]["fixture_id"],
        "dataset_sha256": first["workload"]["dataset_sha256"],
        "environment_fingerprint_sha256": first["environment"]["fingerprint_sha256"],
        "protocol_sha256": first["protocol"]["sha256"],
        "rows": rows,
    }


def _check_plan() -> dict[str, Any]:
    plan = validate_plan(_load_json(PLAN_PATH))
    schema = _object(_load_json(SCHEMA_PATH), "JSON Schema")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValidationError("result schema draft is missing or unsupported")
    registry_path = ROOT / "reports" / "pre-v8-historical-evidence-index-v1.json"
    index = _object(_load_json(registry_path), "historical evidence index")
    if index.get("schema_version") != "s3.pre-v8-historical-evidence-index.v1":
        raise ValidationError("historical evidence index schema is unsupported")
    experiments = index.get("experiments")
    if not isinstance(experiments, list) or not experiments:
        raise ValidationError("historical evidence index must list sourced experiments")
    experiment_ids: set[str] = set()
    for item in experiments:
        row = _object(item, "experiment index entry")
        experiment_id = _string(row.get("id"), "experiment.id")
        if experiment_id in experiment_ids:
            raise ValidationError(f"duplicate historical experiment id: {experiment_id}")
        experiment_ids.add(experiment_id)
        _digest(row.get("source_revision"), SHA1, f"{row.get('id')}.source_revision")
        _string(row.get("integration_status"), f"{row.get('id')}.integration_status")
        compiler_revisions = row.get("compiler_revisions")
        if not isinstance(compiler_revisions, list):
            raise ValidationError(f"{row.get('id')}.compiler_revisions must be an array")
        for revision in compiler_revisions:
            _digest(revision, SHA1, f"{row.get('id')}.compiler_revisions[]")
        if not isinstance(row.get("sources"), list) or not row["sources"]:
            raise ValidationError(f"{row.get('id')} must retain source pointers")
        for source in row["sources"]:
            source_obj = _object(source, f"{row.get('id')}.source")
            url = _string(source_obj.get("url"), f"{row.get('id')}.source.url")
            if not url.startswith("https://github.com/SamDevlab/S3-Benchmarks/blob/"):
                raise ValidationError(f"{row.get('id')} source link must point to this repository")
            expected_blob = _digest(source_obj.get("blob_sha"), SHA1, f"{row.get('id')}.source.blob_sha")
            marker = "/blob/"
            if marker not in url:
                raise ValidationError(f"{row.get('id')} source URL must be an immutable GitHub blob link")
            pinned_revision, separator, source_path = url.split(marker, 1)[1].partition("/")
            if not separator or pinned_revision != row["source_revision"]:
                raise ValidationError(f"{row.get('id')} source URL commit does not match its indexed revision")
            try:
                actual_blob = subprocess.run(
                    ["git", "rev-parse", f"{pinned_revision}:{source_path}"],
                    cwd=ROOT,
                    check=True,
                    capture_output=True,
                    text=True,
                ).stdout.strip()
            except subprocess.CalledProcessError as exc:
                raise ValidationError(f"{row.get('id')} pinned source path is unavailable in Git") from exc
            if actual_blob != expected_blob:
                raise ValidationError(f"{row.get('id')} source blob hash does not match its pinned Git object")
    return {"plan": plan, "indexed_experiments": len(experiments)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check-plan", help="validate prepared groups and immutable evidence pointers")
    validate_parser = commands.add_parser("validate", help="validate one result record")
    validate_parser.add_argument("record", type=Path)
    compare_parser = commands.add_parser("compare", help="compare records without mixing metric stages")
    compare_parser.add_argument("--mode", choices=("revision", "language"), required=True)
    compare_parser.add_argument("records", nargs="+", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "check-plan":
            result = _check_plan()
            print(f"PRE_V8_PLAN=PASS indexed_experiments={result['indexed_experiments']} profile_groups=3 ready_to_measure_v8=NO")
        elif args.command == "validate":
            validate_record(_load_json(args.record))
            print("PRE_V8_RESULT=PASS")
        else:
            records = [_load_json(path) for path in args.records]
            result = compare_records(records, args.mode)
            print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    except ValidationError as exc:
        print(f"PRE_V8_VALIDATION=FAIL: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
