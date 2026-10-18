#!/usr/bin/env python3
"""Validate and combine independent paired R2 measurement sessions."""
from __future__ import annotations

import argparse
import hashlib
import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any

from paired_codegen import paired_metrics


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pair_records(rows: list[dict[str, Any]]) -> dict[tuple[str, str, str, int], dict[str, Any]]:
    pairs: dict[tuple[str, str, str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("phase") != "measured":
            continue
        key = (row["profile"], row["workload"], row["size"], row["round"])
        pairs[key].append(row)

    result: dict[tuple[str, str, str, int], dict[str, Any]] = {}
    for key, observations in pairs.items():
        if len(observations) != 2:
            raise ValueError(f"{key}: expected exactly two measured observations")
        by_revision = {row["revision"]: row for row in observations}
        if set(by_revision) != {"BASELINE", "CANDIDATE"}:
            raise ValueError(f"{key}: expected one BASELINE and one CANDIDATE")
        before, after = by_revision["BASELINE"], by_revision["CANDIDATE"]
        for field in ("pair_id", "fixture_sha256", "source_sha256", "work_units_per_call"):
            if before.get(field) != after.get(field):
                raise ValueError(f"{key}: mismatched paired field {field}")
        expected_pair_id = "|".join((key[0], key[1], key[2], str(key[3])))
        if before["pair_id"] != expected_pair_id:
            raise ValueError(f"{key}: pair id does not match its workload cell")
        order = before.get("pair_order")
        if order not in (["BASELINE", "CANDIDATE"], ["CANDIDATE", "BASELINE"]):
            raise ValueError(f"{key}: invalid pair order")
        positions = {row["revision"]: row.get("position_in_pair") for row in observations}
        if positions != {revision: index for index, revision in enumerate(order)}:
            raise ValueError(f"{key}: pair position does not match recorded order")
        result[key] = by_revision
    return result


def _load_session(directory: Path) -> tuple[dict[str, Any], dict[tuple[str, str, str, int], dict[str, Any]]]:
    manifest_path = directory / "run-manifest.json"
    raw_path = directory / "raw_samples.jsonl"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    index = json.loads((directory / "evidence-index.json").read_text(encoding="utf-8"))
    for entry in index:
        path = directory / entry["path"]
        if not path.is_file() or entry["bytes"] != path.stat().st_size or entry["sha256"] != sha256(path):
            raise ValueError(f"{directory}: evidence index mismatch for {entry['path']}")

    raw_rows = [
        json.loads(line)
        for line in raw_path.read_text(encoding="utf-8").splitlines()
        if line
    ]
    warmup_rows = [
        json.loads(line)
        for line in (directory / "warmups.jsonl").read_text(encoding="utf-8").splitlines()
        if line
    ]
    expected = json.loads((directory / "expected-v1.json").read_text(encoding="utf-8"))
    invalid_probes = json.loads((directory / "invalid-probes.json").read_text(encoding="utf-8"))
    if any(row.get("result") != "PASS" or row.get("short_output_status") != 2 for row in invalid_probes):
        raise ValueError(f"{directory}: one or more invalid-output probes failed")
    build_rows = json.loads((directory / "builds.json").read_text(encoding="utf-8"))
    if {row["artifact_id"] for row in invalid_probes} != {row["artifact_id"] for row in build_rows}:
        raise ValueError(f"{directory}: invalid-output probes do not cover every build artifact")
    builds_by_id = {row["artifact_id"]: row for row in build_rows}
    for row in raw_rows:
        build = builds_by_id.get(row["artifact_id"])
        if build is None:
            raise ValueError(f"{directory}: sample references unknown artifact {row['artifact_id']}")
        if row["artifact_sha256"] != build["sha256"] or row["assembly_sha256"] != build["assembly_sha256"]:
            raise ValueError(f"{directory}: sample artifact hash mismatch for {row['artifact_id']}")
        expected_revision = "BASELINE" if row["revision"] == "BASELINE" else "CANDIDATE"
        if build["revision_label"] != expected_revision:
            raise ValueError(f"{directory}: revision label mismatch for {row['artifact_id']}")
        if row["profile"] != build["profile"].split("/", 1)[0] or row["workload"] != build["workload"]:
            raise ValueError(f"{directory}: workload/profile mismatch for {row['artifact_id']}")
        if row["fixture_sha256"] != manifest["fixture_sha256"]:
            raise ValueError(f"{directory}: sample fixture mismatch for {row['artifact_id']}")
        source_key = f"sources/{row['workload']}.s3"
        if row["source_sha256"] != manifest["source_hashes"].get(source_key):
            raise ValueError(f"{directory}: sample source mismatch for {row['artifact_id']}")
        if row["outputs"] != expected["outputs_by_size"][row["size"]][row["workload"]]:
            raise ValueError(f"{directory}: oracle mismatch for {row['artifact_id']}")
    for row in build_rows:
        revision_dir = "baseline" if row["revision_label"] == "BASELINE" else "candidate"
        assembly_path = directory / "assemblies" / revision_dir / (Path(row["path"]).stem + ".s")
        if not assembly_path.is_file() or sha256(assembly_path) != row["assembly_sha256"]:
            raise ValueError(f"{directory}: generated assembly hash mismatch for {row['artifact_id']}")
    pairs = pair_records(raw_rows)
    expected_pairs = manifest["measured_paired_rounds"] * len(manifest["profiles"]) * len(manifest["workloads"]) * len(manifest["input_sizes"])
    if len(pairs) != expected_pairs:
        raise ValueError(f"{directory}: expected {expected_pairs} complete pairs, found {len(pairs)}")
    expected_warmups = manifest["warmups"] * len(manifest["profiles"]) * len(manifest["workloads"]) * len(manifest["input_sizes"]) * 2
    if len(warmup_rows) != expected_warmups:
        raise ValueError(f"{directory}: expected {expected_warmups} warmup observations, found {len(warmup_rows)}")
    return manifest, pairs


def combine_sessions(directories: list[Path], seed: int) -> dict[str, Any]:
    if len(directories) < 2:
        raise ValueError("at least two independent sessions are required")
    loaded = [_load_session(directory) for directory in directories]
    manifests = [item[0] for item in loaded]
    identity_fields = (
        "baseline", "candidate", "workloads", "input_sizes", "profiles",
        "optimization", "iterations_per_sample_by_size", "source_hashes",
        "fixture_sha256", "expected_sha256", "kernel_runner_sha256",
    )
    reference = manifests[0]
    for index, manifest in enumerate(manifests[1:], start=1):
        for field in identity_fields:
            if manifest.get(field) != reference.get(field):
                raise ValueError(f"session {index}: mismatched run identity field {field}")

    build_identities: list[dict[tuple[str, str, str], tuple[str, str]]] = []
    for directory in directories:
        rows = json.loads((directory / "builds.json").read_text(encoding="utf-8"))
        identity = {}
        for row in rows:
            key = (row["revision_label"], row["profile"], row["workload"])
            identity[key] = (row["sha256"], row["assembly_sha256"])
        build_identities.append(identity)
    if any(value != build_identities[0] for value in build_identities[1:]):
        raise ValueError("compiler artifact or assembly hashes differ between sessions")

    cell_values: dict[tuple[str, str, str], dict[str, list[float]]] = defaultdict(
        lambda: {"BASELINE": [], "CANDIDATE": []}
    )
    for _, pairs in loaded:
        for (profile, workload, size, _round), observations in sorted(pairs.items()):
            cell = (profile, workload, size)
            for revision in ("BASELINE", "CANDIDATE"):
                cell_values[cell][revision].append(observations[revision]["ns_per_call"])

    cells: dict[str, Any] = {}
    for cell, observations in sorted(cell_values.items()):
        base = observations["BASELINE"]
        candidate = observations["CANDIDATE"]
        metrics = paired_metrics(
            base,
            candidate,
            seed=seed + sum(map(ord, "|".join(cell))),
        )
        key = "|".join(cell)
        cells[key] = {
            "baseline_median_ns_per_call": statistics.median(base),
            "candidate_median_ns_per_call": statistics.median(candidate),
            **metrics,
        }

    return {
        "schema": "s3-native-codegen-r2-combined-sessions/v1",
        "session_count": len(directories),
        "paired_rounds_per_cell": {
            "total": len(next(iter(cell_values.values()))["BASELINE"]),
            "per_session": [manifest["measured_paired_rounds"] for manifest in manifests],
        },
        "bootstrap_seed": seed,
        "run_identity": {
            key: reference[key]
            for key in identity_fields
        },
        "sessions": [
            {
                "path": directory.name,
                "run_manifest_sha256": sha256(directory / "run-manifest.json"),
                "raw_samples_sha256": sha256(directory / "raw_samples.jsonl"),
                "paired_runner_sha256": manifest.get("paired_runner_sha256"),
                "order_seed": manifest.get("order_seed"),
                "v1_inputs_archive_sha256": manifest.get("v1_inputs_archive_sha256"),
            }
            for directory, manifest in zip(directories, manifests, strict=True)
        ],
        "cells": cells,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", action="append", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--seed", type=int, default=20261018)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"refusing to overwrite existing output: {args.output}")
    result = combine_sessions([path.resolve() for path in args.session], args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"combined {result['session_count']} sessions; {len(result['cells'])} cells; {result['paired_rounds_per_cell']['total']} pairs/cell")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
