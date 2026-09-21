"""Render reviewable reports from one immutable native-v1 result envelope."""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
from statistics import median
from typing import Any

ROOT = Path(__file__).resolve().parent.parent


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("schema") != "s3.benchmark.native-measurement.v1":
        raise ValueError("unexpected native measurement schema")
    return value


def _measurement_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    rows: dict[tuple[str, str], dict[str, Any]] = {}
    for result in data["measurements"]:
        key = (result["workload"]["id"], result["workload"]["size_class"])
        row = rows.setdefault(key, {
            "id": key[0],
            "size": key[1],
            "family": key[0].split(".", 1)[0],
            "work_units": result["workload"]["work_units_per_sample"],
            "variants": {},
        })
        row["variants"][result["variant"]["id"]] = result
    return [rows[key] for key in sorted(rows)]


def _median_metric(rows: list[dict[str, Any]], metric: str) -> float:
    values = [float(row["variants"]["s3-o1"]["artifact_metrics"][metric]) for row in rows]
    return median(values)


def _artifact_index(data: dict[str, Any]) -> dict[str, Any]:
    artifacts = []
    for result in data["measurements"]:
        artifacts.append({
            "workload_id": result["workload"]["id"],
            "size_class": result["workload"]["size_class"],
            "variant": result["variant"]["id"],
            "source_sha256": result["artifact_metrics"]["source_sha256"],
            "source_bytes": result["artifact_metrics"]["source_bytes"],
            "assembly_sha256": result["artifact_metrics"]["assembly_sha256"],
            "executable_sha256": result["artifact_metrics"]["executable_sha256"],
            "assembly_path": result["build"]["assembly_path"],
            "executable_path": result["build"]["executable_path"],
        })
    return {
        "schema": "s3.benchmark.native-v1-artifact-index.v1",
        "provenance": data["provenance"],
        "environment": {
            "machine_fingerprint_sha256": data["environment"]["machine_fingerprint_sha256"],
            "hostname": data["environment"]["hostname"],
        },
        "artifacts": artifacts,
    }


def render(input_path: Path, output_dir: Path) -> None:
    data = _load(input_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = _measurement_rows(data)
    families = sorted({row["family"] for row in rows})
    measured_ids = sorted({row["id"] for row in rows})
    skip_runtime = data["corpus"]["skipped"]["runtime"]
    measurement_protocol = data["measurement_policy"]
    environment = data["environment"]
    perf = data["perf"]

    (input_path.parent / "artifact-index.json").write_text(
        json.dumps(_artifact_index(data), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    pressure_map = {
        "schema": "s3.benchmark.pressure-map.v1",
        "provenance": data["provenance"],
        "measurement_run": input_path.parent.name,
        "evidence_limits": [
            "All timings are PROCESS_E2E and include process launch, runtime initialization, workload, and one final canary.",
            "No direct KERNEL timing was collected; setup/work separation for kernel attribution is therefore unavailable.",
            "perf counters were unavailable by host permission, so dynamic cycles, instructions, branches, and cache misses are unavailable.",
            "No GCC/Clang reference binaries were included in this first S3-only native baseline.",
        ],
        "pressures": [
            {
                "pressure": "PROCESS_E2E_STARTUP_AND_RUNTIME_INITIALIZATION",
                "evidence_strength": "MULTI_FAMILY",
                "affected_families": families,
                "affected_workloads": len(rows),
                "causality": "UNKNOWN",
                "observed": "Every sample is a native process boundary measurement.",
                "next_experiment": "Add a direct kernel-mode adapter with setup outside the timed region and compare it with the same E2E row.",
            },
            {
                "pressure": "STATIC_CODE_AND_STACK_OPERATION_DENSITY",
                "evidence_strength": "MULTI_FAMILY",
                "affected_families": families,
                "affected_workloads": len(rows),
                "causality": "UNKNOWN",
                "observed": "Assembly instruction, branch, call-site, and stack-operation counts are available and scale with generated workload shape.",
                "next_experiment": "Pair one direct kernel sample with assembly counters and a flat C reference before attributing cost to a compiler mechanism.",
            },
            {
                "pressure": "MEASUREMENT_VARIABILITY",
                "evidence_strength": "MULTI_FAMILY",
                "affected_families": families,
                "affected_workloads": len(rows),
                "causality": "UNKNOWN",
                "observed": "Raw samples and CV/p95 are retained; several small process-E2E rows have broad tails.",
                "next_experiment": "Repeat one fixed machine run with direct kernel timing and the same affinity before changing compiler code.",
            },
            {
                "pressure": "MEMORY_BANDWIDTH_CACHE_LOCALITY_DYNAMIC_COUNTERS",
                "evidence_strength": "UNAVAILABLE",
                "affected_families": [],
                "affected_workloads": 0,
                "causality": "UNKNOWN",
                "observed": "No valid perf counters and no direct kernel timing.",
                "next_experiment": "Resolve measurement-only perf permission or use a supported counter collection host; do not alter system policy in this campaign.",
            },
        ],
    }
    (output_dir / "PRESSURE_MAP.json").write_text(json.dumps(pressure_map, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    pressure_md = """# Native Measurement Pressure Map\n\n"""
    pressure_md += f"Run `{input_path.parent.name}` on machine `{environment['machine_fingerprint_sha256']}`.\n\n"
    pressure_md += "The map is characterization evidence, not a compiler optimization decision. All timing rows are `PROCESS_E2E`; `KERNEL_TIME=NOT_AVAILABLE`.\n\n"
    pressure_md += "| Pressure | Evidence | Families | Workload points | Causality |\n|---|---|---:|---:|---|\n"
    for pressure in pressure_map["pressures"]:
        pressure_md += f"| {pressure['pressure']} | {pressure['evidence_strength']} | {len(pressure['affected_families'])} | {pressure['affected_workloads']} | {pressure['causality']} |\n"
    pressure_md += "\n## Interpretation limits\n\n"
    pressure_md += "- E2E startup/runtime cost is observed by construction, but it is not separated from useful work.\n"
    pressure_md += "- Static assembly counters are descriptive and do not establish dynamic causality.\n"
    pressure_md += "- `perf` was unavailable by host permission; cycles, instructions, branches, cache references/misses and IPC are not reported.\n"
    pressure_md += "- There is no official BabelStream claim: these are the named compatible kernel subset.\n"
    (output_dir / "PRESSURE_MAP.md").write_text(pressure_md, encoding="utf-8")

    candidates_md = """# S3 Optimization Candidates\n\nThese are bounded hypotheses for later experiments, not implementation requests. No S3 source was changed by this campaign.\n\n## Candidate 1\n\n- `CANDIDATE`: direct kernel timing for one flat vector hot path\n- `OBSERVATION`: all current rows are process-E2E; kernel cost cannot be separated from startup/runtime initialization.\n- `AFFECTED_WORKLOADS`: BabelStream-compatible subset, PRK nstream, PolyBench vector paths\n- `AFFECTED_FAMILIES`: `memory`, `hpc`, `numerical`\n- `STRUCTURAL_EVIDENCE`: assembly metrics are available; dynamic counters are not.\n- `PERFORMANCE_EVIDENCE`: multi-family process-E2E samples only.\n- `CAUSALITY`: `UNKNOWN`\n- `NEXT_DISCRIMINATING_EXPERIMENT`: add a setup-outside-loop kernel adapter for one non-mutating vector workload.\n- `FALSIFIER`: direct kernel timing does not reproduce the E2E ordering or shows startup dominates.\n\n## Candidate 2\n\n- `CANDIDATE`: isolate vector access/helper and stack-operation density\n- `OBSERVATION`: call-site and stack-operation counts are present across independent families.\n- `AFFECTED_WORKLOADS`: vector, RMSD, transpose and PolyBench matrix rows\n- `AFFECTED_FAMILIES`: `scientific`, `hpc`, `memory`, `numerical`\n- `STRUCTURAL_EVIDENCE`: static call/stack/branch counts per work unit are recorded.\n- `PERFORMANCE_EVIDENCE`: no direct causal timing or perf counters.\n- `CAUSALITY`: `UNKNOWN`\n- `NEXT_DISCRIMINATING_EXPERIMENT`: compare one S3 kernel against an equivalent flat-storage C kernel with matching work units.\n- `FALSIFIER`: matched kernel timing shows no relationship to static stack/call density.\n\n## Candidate 3\n\n- `CANDIDATE`: reduce environmental variance before performance attribution\n- `OBSERVATION`: process-E2E CV and p95 tails are material on a small virtualized host.\n- `AFFECTED_WORKLOADS`: all measured points\n- `AFFECTED_FAMILIES`: all measured families\n- `STRUCTURAL_EVIDENCE`: fixed affinity is recorded; governor/turbo are unavailable.\n- `PERFORMANCE_EVIDENCE`: raw samples, CV, MAD and p95 are preserved.\n- `CAUSALITY`: `UNKNOWN`\n- `NEXT_DISCRIMINATING_EXPERIMENT`: repeat a bounded same-machine direct-kernel run with documented host controls.\n- `FALSIFIER`: variance remains unchanged under a controlled direct-kernel protocol.\n"""
    (output_dir / "S3_OPTIMIZATION_CANDIDATES.md").write_text(candidates_md, encoding="utf-8")

    table = "| Workload | Size | Work units | O0 median ns | O1 median ns | O1/O0 | O1 ns/work | O1 CV |\n|---|---|---:|---:|---:|---:|---:|---:|\n"
    for row in rows:
        o0 = row["variants"]["s3-o0"]["statistics"]
        o1 = row["variants"]["s3-o1"]["statistics"]
        ratio = o1["median"] / o0["median"]
        table += f"| `{row['id']}` | `{row['size']}` | {row['work_units']} | {o0['median']:.0f} | {o1['median']:.0f} | {ratio:.3f} | {o1['median'] / row['work_units']:.1f} | {o1['cv']:.3f} |\n"

    final_md = f"""# S3 Benchmarks 2.1 Native Measurement\n\n## Status\n\n- `CAMPAIGN`: `S3_BENCHMARKS_2_1_NATIVE_MEASUREMENT`\n- `FUNCTIONAL_HEAD`: `{data['provenance']['benchmark_commit']}`\n- `S3_SHA`: `{data['provenance']['s3_commit']}`\n- `MEASUREMENT_RUN`: `{input_path.parent.name}`\n- `MEASURED_SIZE_POINTS`: `{len(rows)}`\n- `MEASURED_VARIANT_SERIES`: `{len(data['measurements'])}`\n- `NATIVE_QUALIFICATION`: `30/31 planned points`; one medium point was excluded before timing.\n\n## Eligibility and skips\n\nThe measured corpus reused the 2.0.1 source/oracle generators. Each point first passed hosted O0/O1 oracle checks and a separate native canary gate. `numerical.polybench.jacobi_1d medium` passed hosted execution but failed the exact native canary in both O0 and O1 (`program returned: 0`), so it was recorded as `NATIVE_NOT_QUALIFIED` and not timed. The canary was not relaxed.\n\nSkipped by policy: JSMN legacy adapter was not migrated to protocol v2; TSVC remains capability-shape evidence only; PRK stencil and dgemm were not activated.\n\n## Measurement protocol\n\n- timing scope: `PROCESS_E2E`\n- separate measurement executable from the correctness phase\n- one useful workload per process sample (`ITERATIONS_PER_SAMPLE=1`)\n- one integer anti-DCE canary after the workload\n- setup occurs before the workload in each process\n- warmups: `{measurement_protocol['warmups']}`; repetitions: `{measurement_protocol['repetitions']}`\n- variants are interleaved deterministically O0/O1\n- raw samples, median, mean, p95, stddev, MAD and CV are retained\n- no `-ffast-math` or `-Ofast`\n- no Python oracle or correctness comparison is in the timed process path\n\n`KERNEL_TIME=NOT_AVAILABLE`: the current generated programs do not expose a safe setup-outside-loop kernel entry point, so no E2E subtraction or inferred kernel number is reported. The 200--1000 ms calibration target was not reached for these short process-E2E workloads and is marked as such.\n\n## Host and provenance\n\n- machine fingerprint: `{environment['machine_fingerprint_sha256']}`\n- CPU: `{environment['cpu_model']}`\n- RAM: `{environment['ram']}`\n- kernel: `{environment['kernel']}`\n- architecture: `{environment['architecture']}`\n- affinity: `{environment['cpu_affinity']}`\n- SMT: `{environment['smt_status']}`\n- governor: `{environment['cpu_governor']}`\n- turbo: `{environment['turbo_state']}`\n- environment noisy: `{environment['environment_noisy']}`\n- perf: `{perf['available']}` (`{perf['permission']}`)\n\nS3 and benchmark repository identities were checked fail-closed before compilation:\n\n```text\nS3_SHA={data['provenance']['s3_commit']}\nBENCHMARK_REPO_SHA={data['provenance']['benchmark_commit']}\n```\n\n## Results\n\nThe table below is a per-workload characterization. It is not an aggregate score and is not a claim of native kernel speedup.\n\n{table}\n\n## Structural evidence\n\nAssembly analysis reused `tools/assembly_analyzer.py`. It records instruction, call-site, load/store, branch, conditional-branch, stack-operation, binary-size and `.text` metrics for each S3 O0/O1 artifact. Runtime-helper counts, dynamic bounds checks, dynamic stack traffic, cycles, instructions, cache counters and IPC are unavailable under this protocol.\n\n## Pressure decision\n\n`PRESSURE_MAP.md` and `PRESSURE_MAP.json` record three multi-family hypotheses with `CAUSALITY=UNKNOWN`: process startup/runtime initialization, static code/stack-operation density, and measurement variability. Since direct kernel evidence and dynamic counters are unavailable, the campaign selects **PATH C: improve benchmark methodology first**. No S3 optimization should be started from this data.\n\n## Reproducibility\n\n- raw result envelope: `{input_path.as_posix()}`\n- raw transcript: `scratch/native-measurement-20260921-02.txt`\n- artifact index: `{input_path.parent.as_posix()}/artifact-index.json`\n- same-machine reproduction: `NOT_RUN`\n- build determinism: `NOT_MEASURED`\n- full suite: inherited 2.0.1 evidence `18 passed, 1 skipped`; the final branch gate is recorded separately after the functional-head full suite.\n\n## Decision\n\n```text\nNEXT_PATH=PATH_C\nNEXT_CAMPAIGN=direct-kernel-and-flat-reference-methodology\nS3_SOURCE_CHANGED=NO\nEXTERNAL_PRS_OPENED=NO\nREADY_FOR_MERGE=NO\n```\n"""
    (output_dir / "FINAL_REPORT.md").write_text(final_md, encoding="utf-8")

    handoff = f"""# S3 Handoff\n\n## Measurement conclusion\n\nThe first native baseline is valid as controlled PROCESS_E2E characterization on Linux x86-64. It does not identify a dominant compiler/runtime cause.\n\n- pinned S3: `{data['provenance']['s3_commit']}`\n- benchmark head: `{data['provenance']['benchmark_commit']}`\n- measured points: `{len(rows)}` across `{len(families)}` families\n- raw samples: `PASS`\n- perf counters: `UNAVAILABLE`\n- kernel timing: `NOT_AVAILABLE`\n\n## Next experiment\n\nImplement only a benchmark-side direct-kernel adapter for one representative flat vector workload, with setup outside the timed region and the same work-unit contract. Compare it against this E2E row and a flat C reference. Do not modify S3 until that experiment establishes a correlated pressure with a falsifiable mechanism.\n\n## Readiness\n\n```text\nPRK_EXTERNALIZATION_READY=NO\nPLB2_EXTERNALIZATION_READY=NO\nLANGARENA_EXTERNALIZATION_READY=NO\nPROGRAMMING_LANGUAGE_BENCHMARKS_READY=NO\nS3_OPTIMIZATION_CAMPAIGN_READY=NO\n```\n"""
    (output_dir / "S3_HANDOFF.md").write_text(handoff, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "reports" / "benchmarks-2.1-native-measurement")
    args = parser.parse_args()
    render(args.input, args.output_dir)
    print(f"REPORT_DIR={args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
