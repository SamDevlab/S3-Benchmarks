"""One-fixture, three-process native artifact determinism smoke."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
S3_REPO_DIR = Path().resolve()
sys.path.insert(0, str(BASE_DIR))

from tools.artifacts import (  # noqa: E402
    ArtifactError,
    RunIdentity,
    file_record,
    require_provenance,
)
from tools.assembly_analyzer import analyze_assembly_text  # noqa: E402


def _parse_native_result(output: str) -> int:
    match = re.search(r"program returned:\s*(-?\d+)", output)
    if match is None:
        raise ArtifactError(f"native smoke output had no result: {output!r}")
    return int(match.group(1))


def _run_native_once(executable: Path) -> int:
    completed = subprocess.run(
        [str(executable), "--loop", "1"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ArtifactError(
            f"native smoke execution failed with status {completed.returncode}: "
            f"{completed.stderr.strip()}"
        )
    return _parse_native_result(completed.stdout)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--s3-sha", required=True)
    parser.add_argument("--benchmark-sha", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument(
        "--fixture",
        type=Path,
        default=BASE_DIR / "benchmarks" / "jsmn" / "corpus" / "tiny" / "tiny_04_arr.json",
    )
    args = parser.parse_args()

    global S3_REPO_DIR
    S3_REPO_DIR = args.s3_repo.resolve()
    os.environ["S3_REPO"] = str(S3_REPO_DIR)
    if str(S3_REPO_DIR) not in sys.path:
        sys.path.insert(0, str(S3_REPO_DIR))

    from tools.runner import (  # noqa: PLC0415
        build_native_artifact,
        make_artifact_record,
        render_s3_loop_source,
        write_run_manifest,
    )
    from bootstrap.s3.backends.x86_64 import (  # noqa: PLC0415
        NativeToolchain,
        generate_native_assembly,
    )
    from bootstrap.s3.pipeline import compile_source  # noqa: PLC0415
    from benchmarks.jsmn.harness.correctness import (  # noqa: PLC0415
        compare_results,
        reference_jsmn_oracle,
        run_s3_jsmn,
    )

    provenance = require_provenance(
        s3_repo=S3_REPO_DIR,
        requested_s3_sha=args.s3_sha,
        benchmark_repo=BASE_DIR,
        requested_benchmark_sha=args.benchmark_sha,
    )
    run = RunIdentity.create(args.artifact_root, args.run_id)
    text = args.fixture.read_text(encoding="utf-8")
    fixture_id = args.fixture.stem
    fixture_dir = run.fixture_root(fixture_id)
    input_path = fixture_dir / "input.json"
    input_path.write_bytes(text.encode("utf-8"))

    template_path = BASE_DIR / "benchmarks" / "jsmn" / "s3" / "jsmn_demo.s3"
    template = template_path.read_text(encoding="utf-8")
    ref_status, ref_tokens = reference_jsmn_oracle(text.encode("ascii"))
    hosted = run_s3_jsmn(
        template,
        text,
        "O1",
        diagnostic_context={
            "fixture": fixture_id,
            "s3_sha": provenance["s3_commit"],
            "run_id": run.run_id,
        },
    )
    if not compare_results(ref_status, ref_tokens, hosted):
        raise ArtifactError(
            f"hosted correctness failed for {fixture_id}: "
            f"expected {ref_status}, got {hosted.status}"
        )

    source = render_s3_loop_source(template, text, 1)
    variant_dir = run.variant_root(fixture_id, "s3-o1")
    source_path = variant_dir / "source.s3"
    assembly_path = variant_dir / "program.s"
    source_path.write_text(source, encoding="utf-8", newline="\n")
    assembly = generate_native_assembly(
        compile_source(source, "O1").assembly,
        max_instructions=(1 << 62),
    )
    assembly_path.write_text(assembly, encoding="utf-8", newline="\n")

    toolchain = NativeToolchain.detect()
    executable_path = variant_dir / "program"
    object_path, commands = build_native_artifact(
        assembly_path,
        executable_path,
        toolchain.compiler,
    )
    native_status = _run_native_once(executable_path)
    if native_status != ref_status:
        raise ArtifactError(
            f"native correctness failed for {fixture_id}: "
            f"expected {ref_status}, got {native_status}"
        )

    metrics = analyze_assembly_text(assembly, "S3-O1", executable_path).__dict__
    metrics["elf_file_bytes"] = executable_path.stat().st_size
    metrics["text_bytes"] = metrics["text_section_bytes"]
    record = make_artifact_record(
        run,
        fixture_id=fixture_id,
        implementation="s3",
        optimization="O1",
        input_path=input_path,
        generated_source_path=source_path,
        assembly_path=assembly_path,
        object_path=object_path,
        executable_path=executable_path,
        commands=commands,
        metrics=metrics,
    )
    environment: dict[str, Any] = {
        **provenance,
        "python_version": sys.version.split()[0],
        "fixture_id": fixture_id,
        "optimization": "O1",
        "target": "native-x86-64",
    }
    write_run_manifest(
        run,
        provenance=provenance,
        environment=environment,
        argv=sys.argv,
        records=[record],
    )
    run.write_json_once(
        "smoke-result.json",
        {
            "run_id": run.run_id,
            "correctness": "PASS",
            "native_correctness": "PASS",
            "assembly": file_record(run, assembly_path),
            "executable": file_record(run, executable_path),
            "object": file_record(run, object_path),
            "metrics": metrics,
        },
    )
    print(json.dumps({"run_id": run.run_id, "assembly_sha256": record["assembly"]["sha256"], "executable_sha256": record["executable"]["sha256"], **metrics}, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ArtifactError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(2) from error
