"""Build and validate deterministic S3 1.8 cross-repository evidence snapshots."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "benchmarks/s3-1.8-compiler-science"
ARTIFACT_INDEX = LAB / "artifact-index.json"
PATTERN_CORPUS = LAB / "pattern-corpus.json"
RESULT_SCHEMA = LAB / "schemas/result-v1.schema.json"
MANIFEST_PATH = LAB / "manifest.json"
RESULTS_PATH = LAB / "results.json"
CROSS_VERSION_PATH = LAB / "cross-version-index.json"
CAMPAIGN_ID = "S3_1_8_MACHINE_INTELLIGENCE_VERIFIED_OPTIMIZATION_PORTABLE_COMPUTE_AND_COMPILER_SCIENCE_LAB"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _canonical_artifact_bytes(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def _sha(data: bytes) -> str:
    return hashlib.sha256(_canonical_artifact_bytes(data)).hexdigest()


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object at {path}")
    return value


def _safe_repo_path(value: object) -> Path:
    if not isinstance(value, str) or not value:
        raise ValueError("artifact path must be non-empty text")
    relative = PurePosixPath(value)
    if relative.is_absolute() or ".." in relative.parts or "\\" in value:
        raise ValueError(f"artifact path must be repository-relative: {value!r}")
    return ROOT.joinpath(*relative.parts)


def _input_artifacts() -> list[dict[str, object]]:
    index = _read_json(ARTIFACT_INDEX)
    if index.get("schema_version") != "1.0.0" or index.get("campaign_id") != CAMPAIGN_ID:
        raise ValueError("artifact index schema or campaign identity is invalid")
    artifacts = index.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise ValueError("artifact index must contain artifacts")
    seen: set[str] = set()
    output: list[dict[str, object]] = []
    for item in artifacts:
        if not isinstance(item, dict):
            raise ValueError("artifact entries must be objects")
        path_text = item.get("path")
        path = _safe_repo_path(path_text)
        if path_text in seen:
            raise ValueError(f"duplicate artifact path: {path_text}")
        seen.add(path_text)
        if not path.is_file():
            raise ValueError(f"required evidence artifact is missing: {path_text}")
        payload = _read_json(path)
        if payload.get("report_kind") != item.get("report_kind"):
            raise ValueError(f"report kind mismatch for {path_text}")
        if item.get("workload_id") not in path.name:
            raise ValueError(f"workload identity is not reflected in artifact path: {path_text}")
        provenance = payload.get("provenance", payload.get("input", {}))
        if not isinstance(provenance, dict):
            raise ValueError(f"artifact provenance is malformed: {path_text}")
        artifact_bytes = _canonical_artifact_bytes(path.read_bytes())
        output.append(
            {
                **item,
                "sha256": hashlib.sha256(artifact_bytes).hexdigest(),
                "bytes": len(artifact_bytes),
                "s3_head": provenance.get("git_head"),
                "source_sha256": provenance.get("source_sha256"),
                "git_worktree_dirty": provenance.get("git_worktree_dirty"),
            }
        )
    expected_head = index.get("repositories", {}).get("s3", {}).get("candidate_head")
    if not isinstance(expected_head, str) or not re.fullmatch(r"[0-9a-f]{40}", expected_head):
        raise ValueError("S3 candidate HEAD must be pinned in the artifact index")
    if any(item["s3_head"] != expected_head for item in output):
        mismatched = [str(item["path"]) for item in output if item["s3_head"] != expected_head]
        raise ValueError(f"evidence artifacts do not all match S3 candidate {expected_head}: {mismatched}")
    return sorted(output, key=lambda item: str(item["path"]))


def _historical_artifacts(index: dict[str, Any]) -> list[dict[str, object]]:
    records = index.get("historical_budget_evidence", [])
    output: list[dict[str, object]] = []
    for item in records:
        experiment_id = item.get("experiment_id")
        result_path = ROOT / "results" / f"{experiment_id}.json"
        if not result_path.is_file():
            if experiment_id == "S3-BENCH-2.2.4-P1":
                result_path = ROOT / "results/EXP-S3-17-LOWERING-001.json"
            else:
                raise ValueError(f"historical result is missing for {experiment_id}")
        result_bytes = _canonical_artifact_bytes(result_path.read_bytes())
        output.append(
            {
                "experiment_id": experiment_id,
                "path": result_path.relative_to(ROOT).as_posix(),
                "sha256": hashlib.sha256(result_bytes).hexdigest(),
                "bytes": len(result_bytes),
                "source": item["source"],
                "classification": item["classification"],
                "current_1_8_recharacterization": item["current_1_8_recharacterization"],
            }
        )
    return output


def build_manifest() -> dict[str, Any]:
    index = _read_json(ARTIFACT_INDEX)
    repositories = index["repositories"]
    return {
        "schema_version": "1.0.0",
        "campaign_id": CAMPAIGN_ID,
        "repositories": repositories,
        "input_files": [
            {"path": ARTIFACT_INDEX.relative_to(ROOT).as_posix(), "sha256": _sha(ARTIFACT_INDEX.read_bytes())},
            {"path": PATTERN_CORPUS.relative_to(ROOT).as_posix(), "sha256": _sha(PATTERN_CORPUS.read_bytes())},
            {"path": RESULT_SCHEMA.relative_to(ROOT).as_posix(), "sha256": _sha(RESULT_SCHEMA.read_bytes())},
        ],
        "evidence_artifacts": _input_artifacts(),
        "historical_artifacts": _historical_artifacts(index),
    }


def _load_report(path_text: str) -> dict[str, Any]:
    return _read_json(_safe_repo_path(path_text))


def _experiment_artifacts(manifest: dict[str, Any], kinds: set[str]) -> list[dict[str, str]]:
    return [
        {"path": str(item["path"]), "sha256": str(item["sha256"])}
        for item in manifest["evidence_artifacts"]
        if item["report_kind"] in kinds
    ]


def build_results(manifest: dict[str, Any]) -> dict[str, Any]:
    index = _read_json(ARTIFACT_INDEX)
    workload_ids = sorted({str(item["workload_id"]) for item in manifest["evidence_artifacts"]})

    reference_rows: list[dict[str, Any]] = []
    codegen_rows: list[dict[str, Any]] = []
    vector_rows: list[dict[str, Any]] = []
    allocator_rows: list[dict[str, Any]] = []
    for workload_id in workload_ids:
        entries = {
            str(item["report_kind"]): _load_report(str(item["path"]))
            for item in manifest["evidence_artifacts"]
            if item["workload_id"] == workload_id
        }
        references = next((value for value in entries.values() if value.get("report_kind") == "S3_REFERENCE_DATAFLOW_RESEARCH"), None)
        codegen = next((value for value in entries.values() if value.get("report_kind") == "S3_X86_64_CODEGEN_ATTRIBUTION_EXPERIMENTAL"), None)
        vector = next((value for value in entries.values() if value.get("report_kind") == "S3_VECTOR_LEGALITY_RESEARCH"), None)
        if not references or not codegen or not vector:
            raise ValueError(f"workload {workload_id} lacks the required three report families")
        if len({
            references["provenance"]["source_sha256"],
            codegen["input"]["source_sha256"],
            vector["provenance"]["source_sha256"],
        }) != 1:
            raise ValueError(f"source identity differs among reports for {workload_id}")

        ref_summary = references["summary"]
        all_refs = [fact for function in references["functions"] for fact in function["references"]]
        reference_rows.append(
            {
                "workload_id": workload_id,
                "source_sha256": references["provenance"]["source_sha256"],
                "function_count": ref_summary["function_count"],
                "complete_function_count": ref_summary["complete_function_count"],
                "reference_values": ref_summary["reference_values"],
                "known_origin_count": ref_summary["origin_status_counts"].get("KNOWN", 0),
                "escape_status_counts": ref_summary["escape_status_counts"],
                "read_uses": sum(fact["read_uses"] for fact in all_refs),
                "write_uses": sum(fact["write_uses"] for fact in all_refs),
                "unknown_uses": sum(fact["unknown_uses"] for fact in all_refs),
                "transformation_authorized": False,
            }
        )

        summary = codegen["summary"]
        native_count = summary["native_assembly_instruction_count"]
        attributed = summary["native_origin_attributed_instructions"]
        codegen_rows.append(
            {
                "workload_id": workload_id,
                "source_sha256": codegen["input"]["source_sha256"],
                "assembly_instruction_count": summary["assembly_instruction_count"],
                "generated_assembly_text_bytes": summary["generated_assembly_text_bytes"],
                "native_assembly_instruction_count": native_count,
                "origin_attributed_native_instructions": attributed,
                "origin_unknown_native_instructions": summary["native_origin_unknown_instructions"],
                "origin_attribution_fraction": round(attributed / native_count, 6) if native_count else None,
                "machine_text_bytes": summary["machine_text_bytes"],
                "native_speedup_claim": False,
                "compact_ea": codegen["optimization_explain"]["compact_ea"],
                "no_op_move_candidates": codegen["optimization_explain"]["redundant_noop_moves"]["candidate_noop_moves"],
            }
        )

        vector_summary = vector["summary"]
        vector_rows.append(
            {
                "workload_id": workload_id,
                "source_sha256": vector["provenance"]["source_sha256"],
                "loops_seen": vector_summary["loops_seen"],
                "vectorizable_loops": vector_summary["vectorizable_loops"],
                "not_vectorizable_loops": vector_summary["not_vectorizable_loops"],
                "unknown_loops": vector_summary["unknown_loops"],
                "transformation_authorized": False,
            }
        )

        expected_function = {
            "engineering.point-cloud-summary.v1": "point_cloud_summary",
            "geospatial.raster-window-statistics.v1": "raster_window_statistics",
            "energy.pv-timeseries-aggregation.v1": "energy_series_aggregation",
        }[workload_id]
        function = next(item for item in codegen["functions"] if item["name"] == expected_function)
        allocation = function["allocation"]
        allocator_rows.append(
            {
                "workload_id": workload_id,
                "function": expected_function,
                "virtual_register_count": allocation["virtual_register_count"],
                "peak_live_virtual_registers": allocation["peak_live_virtual_registers"],
                "stack_resident_virtual_register_count": allocation["stack_resident_virtual_register_count"],
                "static_frame_bytes": function["frame_bytes"],
                "same_physical_register_move_count": allocation["moves_assigned_same_physical_register"],
                "dynamic_spills": None,
                "budget_register_allocator_capacity_probe": allocation["budget_register_allocator_capacity_probe"],
            }
        )

    historical = _historical_artifacts(index)
    hist_refs = [
        {"path": item["path"], "sha256": item["sha256"]}
        for item in historical
    ]
    experiments = [
        {
            "experiment_id": "EXP-S3-18-REF-001",
            "research_question": "RQ1: can references be analyzed more precisely without weakening safety?",
            "maturity": "EXPERIMENTAL",
            "classification": "KNOWN_ORIGIN_AND_NO_ESCAPE_ON_8_OF_8_REFERENCE_VALUES; DIAGNOSTIC_ONLY",
            "protocol": {"kind": "STATIC_IR_ANALYSIS", "execution_performed": False, "transformation_authorized": False},
            "evidence_artifacts": _experiment_artifacts(manifest, {"S3_REFERENCE_DATAFLOW_RESEARCH"}),
            "observations": {"workloads": reference_rows, "limitations": ["interprocedural no-escape summaries absent", "facts do not authorize transformations"]},
        },
        {
            "experiment_id": "EXP-S3-18-CODEGEN-001",
            "research_question": "RQ2: how much emitted native assembly text can be tied to S3 Assembly operations?",
            "maturity": "PARTIAL",
            "classification": "ASSEMBLY_TO_GENERATED_TEXT_LINEAGE; BINARY_AND_RUNTIME_ATTRIBUTION_INCOMPLETE",
            "protocol": {"kind": "STATIC_X86_64_TEXT_ANALYSIS", "target": "linux-x86_64", "native_policy": "baseline", "instruction_budget_mode": "per-instruction", "execution_performed": False, "timing_measured": False},
            "evidence_artifacts": _experiment_artifacts(manifest, {"S3_X86_64_CODEGEN_ATTRIBUTION_EXPERIMENTAL"}),
            "observations": {"workloads": codegen_rows, "limitations": ["mapped ranges are emitted assembly text lines, not binary addresses", "generated runtime, prologue and unmodeled lines remain UNMAPPED", "machine .text bytes unavailable without assembled objects"]},
        },
        {
            "experiment_id": "EXP-S3-18-ALLOC-001",
            "research_question": "RQ4: how much static frame/register pressure is visible, and what is the r15 budget reservation trade-off?",
            "maturity": "PARTIAL",
            "classification": "STATIC_ALLOCATOR_CHARACTERIZATION_ONLY; NO_DYNAMIC_SPILL_OR_PERFORMANCE_CLAIM",
            "protocol": {"kind": "STATIC_REGISTER_ALLOCATION_REPORT", "budget_register": "r15", "counterfactual_is_executable": False, "execution_performed": False},
            "evidence_artifacts": _experiment_artifacts(manifest, {"S3_X86_64_CODEGEN_ATTRIBUTION_EXPERIMENTAL"}),
            "observations": {"workloads": allocator_rows, "limitations": ["stack-resident virtual values are not dynamic spills", "r15 availability probe is allocator-only and conflicts with current budget residency"]},
        },
        {
            "experiment_id": "EXP-S3-18-VEC-001",
            "research_question": "RQ5: which continuity-workload loops are legally vectorizable under strict semantics?",
            "maturity": "PARTIAL",
            "classification": "5_LOOPS_OBSERVED_0_VECTOR_BOUNDS_PROOFS_5_UNKNOWN; NO_SIMD_EMITTED",
            "protocol": {"kind": "STATIC_LOOP_FACT_REUSE", "strict_fp_preserved": True, "execution_performed": False, "transformation_authorized": False},
            "evidence_artifacts": _experiment_artifacts(manifest, {"S3_VECTOR_LEGALITY_RESEARCH"}),
            "observations": {"workloads": vector_rows, "limitations": ["natural loops exist but canonical induction and vector access proofs were not recognized", "general inter-iteration dependence is not modeled"]},
        },
        {
            "experiment_id": "EXP-S3-18-BUDGET-001",
            "research_question": "RQ6: does current PER materially change historical EXACT/HYBRID conclusions?",
            "maturity": "INCONCLUSIVE",
            "classification": "NOT_COMPARABLE_WITHOUT_MATCHED_1_8_ARTIFACT_AND_PROTOCOL",
            "protocol": {"kind": "HISTORICAL_EVIDENCE_RECONCILIATION", "new_benchmark_run": False, "default_changed": False},
            "evidence_artifacts": hist_refs,
            "observations": {"historical_reports": historical, "conclusion": "Historical exact-segment and budget experiments remain separately valid; no current 1.8 PER-vs-EXACT/HYBRID causal result is inferred."},
        },
        {
            "experiment_id": "EXP-S3-18-AGENT-001",
            "research_question": "RQ7: can agent-generated verbose programs be safely normalized?",
            "maturity": "NOT_STARTED",
            "classification": "OPEN_NO_LLM_AUTHORED_PAIRED_EQUIVALENCE_CORPUS",
            "protocol": {"kind": "CORPUS_AUDIT", "online_model_generation": False, "stylistic_scoring": False},
            "evidence_artifacts": [],
            "observations": {"checked_in_agent_kernel_authorship": "DETERMINISTIC_HUMAN_AUTHORED_QUALIFICATION_SAMPLES", "next_evidence_needed": "paired semantics-preserving verbose/normalized programs with hosted/native equivalence"},
        },
    ]
    research_questions = [
        {"id": "RQ1", "status": "PARTIAL", "evidence": "8/8 reference values across three kernels had known origins and NO_ESCAPE in this diagnostic; unknown calls still fail closed."},
        {"id": "RQ2", "status": "PARTIAL", "evidence": "34.6%-39.3% of parsed native assembly instructions mapped to Assembly-op spans; remaining lines are explicit UNMAPPED."},
        {"id": "RQ3", "status": "DEFERRED_WITH_EVIDENCE", "evidence": "No concrete optimization requiring a new Machine IR was qualified; Assembly-to-text provenance now covers a first observable layer."},
        {"id": "RQ4", "status": "PARTIAL", "evidence": "Static peak liveness/frame/stack-resident metrics were recorded; no dynamic spill or PMU evidence."},
        {"id": "RQ5", "status": "OPEN", "evidence": "5 natural loops, no recognized canonical induction/vector bounds proofs; all remain UNKNOWN."},
        {"id": "RQ6", "status": "INCONCLUSIVE", "evidence": "Existing 1.7 exact-segment records are not matched to a current 1.8 PER-vs-EXACT/HYBRID candidate/protocol."},
        {"id": "RQ7", "status": "OPEN", "evidence": "Checked-in agent-named kernels are human-authored examples; no LLM-generated paired normalization experiment."},
        {"id": "RQ8", "status": "PARTIAL", "evidence": "Reference/loop facts are IR-level and target-neutral, but no second-backend semantic execution probe was run."},
        {"id": "RQ9", "status": "PARTIAL", "evidence": "Existing deterministic seeded O0/O1 differential cases passed; no new broad fuzz campaign or failure discovery."},
        {"id": "RQ10", "status": "OPEN", "evidence": "Static unknown code regions are large, but static counters do not identify a runtime bottleneck."},
    ]
    hypotheses = [
        {"hypothesis_id": "HYP-S3-18-001", "research_question": "RQ1", "status": "PARTIAL", "experiment_ids": ["EXP-S3-18-REF-001"], "statement": "Reference origins and local use effects can be summarized more precisely for the modeled workload IR without authorizing transformations."},
        {"hypothesis_id": "HYP-S3-18-002", "research_question": "RQ2", "status": "PARTIAL", "experiment_ids": ["EXP-S3-18-CODEGEN-001"], "statement": "A deterministic emitter sidecar can relate some S3 Assembly operations to generated native assembly-text instruction ranges."},
        {"hypothesis_id": "HYP-S3-18-003", "research_question": "RQ3", "status": "INCONCLUSIVE", "experiment_ids": ["EXP-S3-18-CODEGEN-001"], "statement": "A new Machine IR is required for the next useful machine-level optimization."},
        {"hypothesis_id": "HYP-S3-18-004", "research_question": "RQ4", "status": "PARTIAL", "experiment_ids": ["EXP-S3-18-ALLOC-001"], "statement": "Reserving r15 has a measurable allocator-capacity effect on at least one continuity workload."},
        {"hypothesis_id": "HYP-S3-18-005", "research_question": "RQ5", "status": "PARTIAL", "experiment_ids": ["EXP-S3-18-VEC-001"], "statement": "The current loop facts are sufficient to prove vector legality for at least one continuity workload loop."},
        {"hypothesis_id": "HYP-S3-18-006", "research_question": "RQ6", "status": "INCONCLUSIVE", "experiment_ids": ["EXP-S3-18-BUDGET-001"], "statement": "Current PER materially changes the historical EXACT/HYBRID conclusion."},
        {"hypothesis_id": "HYP-S3-18-007", "research_question": "RQ7", "status": "OPEN", "experiment_ids": ["EXP-S3-18-AGENT-001"], "statement": "The compiler reliably normalizes verbose agent-authored programs while preserving behavior."},
        {"hypothesis_id": "HYP-S3-18-008", "research_question": "RQ8", "status": "PARTIAL", "experiment_ids": ["EXP-S3-18-REF-001", "EXP-S3-18-VEC-001"], "statement": "Reference and loop facts can be kept target-independent even when native attribution is x86-specific."},
        {"hypothesis_id": "HYP-S3-18-009", "research_question": "RQ9", "status": "PARTIAL", "experiment_ids": [], "statement": "Existing deterministic differential tests provide useful compiler correctness coverage, but do not replace a campaign-specific fuzz oracle."},
        {"hypothesis_id": "HYP-S3-18-010", "research_question": "RQ10", "status": "OPEN", "experiment_ids": ["EXP-S3-18-CODEGEN-001", "EXP-S3-18-ALLOC-001"], "statement": "Static codegen and allocator reports identify the dominant runtime bottleneck."},
    ]
    negative_results = [
        {"result_id": "NEG-S3-18-001", "experiment_id": "EXP-S3-18-CODEGEN-001", "observation": "Compact EA diagnostic applied zero sites in the three continuity workloads; effective emitted policy remained baseline.", "interpretation": "No lowering change or speedup is established."},
        {"result_id": "NEG-S3-18-002", "experiment_id": "EXP-S3-18-CODEGEN-001", "observation": "The redundant no-op move analysis found zero candidates in the measured Assembly programs.", "interpretation": "This corpus gives no target for a no-op-move elimination experiment."},
        {"result_id": "NEG-S3-18-003", "experiment_id": "EXP-S3-18-VEC-001", "observation": "Zero loops were proven vectorizable; all five observed loops remain UNKNOWN.", "interpretation": "No SIMD transformation is authorized by current evidence."},
        {"result_id": "NEG-S3-18-004", "experiment_id": "EXP-S3-18-CODEGEN-001", "observation": "Assembly-origin spans cover only 34.6%-39.3% of parsed native assembly-text instructions.", "interpretation": "Remaining instructions stay explicitly UNMAPPED; no complete machine-code genealogy claim."},
        {"result_id": "NEG-S3-18-005", "experiment_id": "EXP-S3-18-ALLOC-001", "observation": "The r15-free allocator comparison is a static counterfactual and was not emitted or executed.", "interpretation": "It cannot establish a runtime or production allocator benefit."},
        {"result_id": "NEG-S3-18-006", "experiment_id": "EXP-S3-18-BUDGET-001", "observation": "Historical exact-segment and budget evidence lacks a matched 1.8 artifact and protocol.", "interpretation": "The old PER/EXACT/HYBRID conclusion remains NOT_COMPARABLE, not overturned."},
    ]
    return {
        "schema_version": "1.0.0",
        "campaign_id": CAMPAIGN_ID,
        "provenance": {
            "s3_campaign_base": index["repositories"]["s3"]["campaign_base"],
            "s3_candidate_head": index["repositories"]["s3"]["candidate_head"],
            "bench_campaign_base": index["repositories"]["benchmarks"]["campaign_base"],
            "manifest_sha256": _sha(_render(manifest).encode("utf-8")),
        },
        "experiments": experiments,
        "hypotheses": hypotheses,
        "negative_results": negative_results,
        "research_questions": research_questions,
        "default_policy": {"instruction_budget": "PER_INSTRUCTION", "changed": False},
        "strict_fp_preserved": True,
        "runtime_performance_claims": False,
    }


def build_cross_version_index(manifest: dict[str, Any], results: dict[str, Any]) -> dict[str, Any]:
    old_path = ROOT / "results/EXP-S3-17-LOWERING-002.json"
    old = _read_json(old_path)
    historical_workloads: list[dict[str, Any]] = []
    for workload_id, record in sorted(old["workloads"].items()):
        static = record["static_metrics"]
        historical_workloads.append(
            {
                "workload_id": workload_id,
                "metric_family": "ELF_DISASSEMBLY_STATIC_COUNTS",
                "control_machine_instructions": static["control"]["static_machine_instructions"],
                "candidate_machine_instructions": static["candidate"]["static_machine_instructions"],
                "control_branches": static["control"]["static_branches"],
                "candidate_branches": static["candidate"]["static_branches"],
                "control_memory_operands": static["control"]["static_memory_operand_instructions"],
                "candidate_memory_operands": static["candidate"]["static_memory_operand_instructions"],
                "correctness": "PASS",
                "timing_classification": record["timing"]["paired_comparison"]["classification"],
            }
        )
    current = next(item for item in results["experiments"] if item["experiment_id"] == "EXP-S3-18-CODEGEN-001")
    return {
        "schema_version": "1.0.0",
        "campaign_id": CAMPAIGN_ID,
        "comparability_policy": "Only compare metrics with the same measurement unit, artifact scope, target, and extraction protocol; otherwise retain side-by-side records without delta.",
        "versions": [
            {
                "s3_line": "1.7",
                "s3_candidate_sha": old["s3_candidate_sha"],
                "benchmark_experiment_id": "EXP-S3-17-LOWERING-002",
                "benchmark_result_path": "results/EXP-S3-17-LOWERING-002.json",
                "benchmark_result_sha256": _sha(old_path.read_bytes()),
                "metric_family": "ELF_DISASSEMBLY_STATIC_COUNTS",
                "workloads": historical_workloads,
            },
            {
                "s3_line": "1.8-baseline",
                "s3_campaign_base": manifest["repositories"]["s3"]["campaign_base"],
                "experiment_id": "EXP-S3-18-CODEGEN-001",
                "metric_family": "GENERATED_ASSEMBLY_TEXT_AND_ASSEMBLY_TO_LINE_SPANS",
                "evidence_artifacts": current["evidence_artifacts"],
                "workloads": current["observations"]["workloads"],
            },
        ],
        "direct_delta_supported": False,
        "direct_delta_reason": "The 1.7 records count disassembled ELF instructions, while 1.8 records emitter text and Assembly-origin spans; no common object extraction protocol was run for both candidate lines.",
    }


def _render(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def build_snapshot() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    index = _read_json(ARTIFACT_INDEX)
    patterns = _read_json(PATTERN_CORPUS)
    if patterns.get("schema_version") != "1.0.0" or patterns.get("corpus_id") != "s3-1.8-compiler-patterns-v1":
        raise ValueError("compiler pattern corpus identity is invalid")
    manifest = build_manifest()
    results = build_results(manifest)
    cross_version = build_cross_version_index(manifest, results)
    _validate_result_shape(results)
    return manifest, results, cross_version


def _validate_result_shape(results: dict[str, Any]) -> None:
    if results.get("schema_version") != "1.0.0" or results.get("campaign_id") != CAMPAIGN_ID:
        raise ValueError("results schema or campaign identity is invalid")
    experiment_ids = [item.get("experiment_id") for item in results.get("experiments", [])]
    if len(experiment_ids) != len(set(experiment_ids)):
        raise ValueError("experiment IDs must be unique")
    if len(experiment_ids) < 5 or len(results.get("research_questions", [])) != 10:
        raise ValueError("campaign results must include at least five experiments and ten RQs")
    hypothesis_ids = [item.get("hypothesis_id") for item in results.get("hypotheses", [])]
    negative_ids = [item.get("result_id") for item in results.get("negative_results", [])]
    if len(hypothesis_ids) != 10 or len(hypothesis_ids) != len(set(hypothesis_ids)):
        raise ValueError("campaign must contain ten uniquely identified hypotheses")
    if len(negative_ids) != len(set(negative_ids)) or not negative_ids:
        raise ValueError("negative-result IDs must be non-empty and unique")
    hypothesis_statuses = {"OPEN", "SUPPORTED", "REFUTED", "PARTIAL", "INCONCLUSIVE"}
    rq_ids = {item.get("id") for item in results["research_questions"]}
    if rq_ids != {f"RQ{index}" for index in range(1, 11)}:
        raise ValueError("research question IDs must cover RQ1 through RQ10 exactly")
    if any(
        not re.fullmatch(r"HYP-S3-18-[0-9]{3}", str(item["hypothesis_id"]))
        or item["research_question"] not in rq_ids
        or item["status"] not in hypothesis_statuses
        or not item["statement"].strip()
        for item in results["hypotheses"]
    ):
        raise ValueError("hypothesis registry contains an invalid ID, RQ, status, or statement")
    if any(
        not re.fullmatch(r"NEG-S3-18-[0-9]{3}", str(item["result_id"]))
        or not item["observation"].strip()
        or not item["interpretation"].strip()
        for item in results["negative_results"]
    ):
        raise ValueError("negative-result registry contains an invalid ID or empty evidence")
    experiment_id_set = set(experiment_ids)
    if any(
        reference not in experiment_id_set
        for hypothesis in results["hypotheses"]
        for reference in hypothesis["experiment_ids"]
    ):
        raise ValueError("hypothesis references an unknown experiment")
    if any(item["experiment_id"] not in experiment_id_set for item in results["negative_results"]):
        raise ValueError("negative result references an unknown experiment")
    if results.get("default_policy") != {"instruction_budget": "PER_INSTRUCTION", "changed": False}:
        raise ValueError("PER_INSTRUCTION default must remain unchanged")
    if results.get("strict_fp_preserved") is not True or results.get("runtime_performance_claims") is not False:
        raise ValueError("strict-FP and no-runtime-claim guardrails are required")
    for experiment in results["experiments"]:
        if experiment["maturity"] not in {
            "QUALIFIED", "EXPERIMENTAL", "PROTOTYPE", "DESIGN", "PARTIAL",
            "DEFERRED_WITH_EVIDENCE", "REJECTED_WITH_EVIDENCE", "INCONCLUSIVE", "NOT_STARTED",
        }:
            raise ValueError(f"invalid maturity for {experiment['experiment_id']}")
        for artifact in experiment["evidence_artifacts"]:
            if not _SHA256.fullmatch(artifact["sha256"]):
                raise ValueError("experiment artifact SHA-256 is malformed")


def validate_snapshot() -> dict[str, object]:
    manifest, results, cross_version = build_snapshot()
    actual = {
        "manifest.json": manifest,
        "results.json": results,
        "cross-version-index.json": cross_version,
    }
    paths = {"manifest.json": MANIFEST_PATH, "results.json": RESULTS_PATH, "cross-version-index.json": CROSS_VERSION_PATH}
    for name, expected in actual.items():
        path = paths[name]
        if not path.is_file():
            raise ValueError(f"generated registry snapshot is missing: {path}")
        if path.read_text(encoding="utf-8") != _render(expected):
            raise ValueError(f"generated registry snapshot is stale: {path}")
    return {
        "artifact_count": len(manifest["evidence_artifacts"]),
        "experiment_count": len(results["experiments"]),
        "research_question_count": len(results["research_questions"]),
        "cross_version_delta_supported": cross_version["direct_delta_supported"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("snapshot", "validate"))
    args = parser.parse_args()
    if args.command == "snapshot":
        manifest, results, cross_version = build_snapshot()
        MANIFEST_PATH.write_text(_render(manifest), encoding="utf-8", newline="\n")
        RESULTS_PATH.write_text(_render(results), encoding="utf-8", newline="\n")
        CROSS_VERSION_PATH.write_text(_render(cross_version), encoding="utf-8", newline="\n")
        print(f"S3_18_SNAPSHOT=WRITTEN artifacts={len(manifest['evidence_artifacts'])} experiments={len(results['experiments'])}")
        return 0
    summary = validate_snapshot()
    print("S3_18_SNAPSHOT=VALID " + " ".join(f"{key}={value}" for key, value in summary.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
