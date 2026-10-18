"""Reproducible runtime fixture and scalar oracle for native-pure-controlled-v1."""

from __future__ import annotations

import hashlib
import json
import math
import struct
from pathlib import Path

N = 364
COORDS = 363
MAGIC = b"S3NPV1\0\0"
SEED = 20261017
FORMAT = "<8sII364d364d364d364q363d2d"
SIZE_COUNTS = {"small": 32, "medium": 128, "full": 364}


def workload_counts(size: str) -> dict[str, int]:
    count = SIZE_COUNTS[size]
    points = {"small": 16, "medium": 64, "full": 121}[size]
    return {
        "agent_energy_residual": count,
        "agent_point_bounds": points,
        "agent_raster_threshold_count": count,
        "agent_raster_valid_mean": count,
        "energy_series_aggregation": count,
        "point_cloud_summary": points,
    }


def fixture_values(seed: int = SEED) -> dict[str, object]:
    s = seed % 997
    actual = [(((i * 37 + s * 11) % 2001) - 1000) / 32.0 for i in range(N)]
    load = [(((i * 29 + s * 7 + 311) % 1801) - 900) / 32.0 for i in range(N)]
    values = [(((i * 43 + s * 13 + 127) % 1201) - 600) / 64.0 for i in range(N)]
    valid_mask = [1 if (i * 17 + s * 5) % 7 != 0 else 0 for i in range(N)]
    coordinates = [
        ((((point * 19 + axis * 31 + s * 3) % 1009) - 504) / 16.0)
        for point in range(121)
        for axis in range(3)
    ]
    return {
        "seed": seed,
        "actual": actual,
        "load": load,
        "values": values,
        "valid_mask": valid_mask,
        "coordinates": coordinates,
        "threshold": 0.375,
        "capacity": 4900.0,
    }


def write_fixture(path: Path, seed: int = SEED) -> str:
    f = fixture_values(seed)
    packed = struct.pack(
        FORMAT,
        MAGIC,
        N,
        0,
        *f["actual"],
        *f["load"],
        *f["values"],
        *f["valid_mask"],
        *f["coordinates"],
        f["threshold"],
        f["capacity"],
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(packed)
    return hashlib.sha256(packed).hexdigest()


def expected_outputs(seed: int = SEED, size: str = "full") -> dict[str, list[float | int]]:
    f = fixture_values(seed)
    counts = workload_counts(size)
    n = counts["agent_energy_residual"]
    points = counts["point_cloud_summary"]
    actual, load = f["actual"], f["load"]
    values, masks = f["values"], f["valid_mask"]
    coords = f["coordinates"]

    differences = [actual[i] - load[i] for i in range(n)]
    magnitudes = [abs(value) for value in differences]
    residual = [sum(differences), max(magnitudes), sum(magnitudes) / float(n)]

    active_coords = coords[:points * 3]
    minimum = [min(active_coords[axis::3]) for axis in range(3)]
    maximum = [max(active_coords[axis::3]) for axis in range(3)]
    bounds = minimum + maximum

    threshold_count = sum(
        1 for value, valid in zip(values[:n], masks[:n]) if valid == 1 and value > f["threshold"]
    )
    valid_values = [value for value, valid in zip(values[:n], masks[:n]) if valid == 1]
    valid_mean = [sum(valid_values) / float(len(valid_values))]

    ac_energy = sum(actual[:n])
    balances = [actual[i] - load[i] for i in range(n)]
    energy = [
        ac_energy,
        max(actual[:n]),
        sum(balances),
        ac_energy / (f["capacity"] * n),
        sum(abs(value) for value in balances) / n,
    ]

    centers = [sum(active_coords[axis::3]) / float(points) for axis in range(3)]
    squared_radius_sum = 0.0
    for point in range(points):
        dx, dy, dz = (coords[point * 3 + axis] - centers[axis] for axis in range(3))
        squared_radius_sum += dx * dx + dy * dy + dz * dz
    cloud = centers + minimum + maximum + [math.sqrt(squared_radius_sum / float(points))]
    return {
        "agent_energy_residual": residual,
        "agent_point_bounds": bounds,
        "agent_raster_threshold_count": [threshold_count],
        "agent_raster_valid_mean": valid_mean,
        "energy_series_aggregation": energy,
        "point_cloud_summary": cloud,
    }


def write_expected(path: Path, seed: int = SEED) -> None:
    path.write_text(
        json.dumps({"seed": seed, "outputs_by_size": {size: expected_outputs(seed, size) for size in SIZE_COUNTS}}, indent=2) + "\n",
        encoding="utf-8",
    )
