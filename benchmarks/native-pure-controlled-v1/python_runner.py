#!/usr/bin/env python3
"""Interpreted comparison path; fixture loading and oracle checks stay untimed."""
from __future__ import annotations

import json
import struct
import sys
import time
from pathlib import Path

try:
    import resource
except ImportError:  # Windows is used for unit tests; campaign measurements run on Linux.
    resource = None

from fixture import COORDS, FORMAT, MAGIC, N, workload_counts


def main() -> int:
    if len(sys.argv) != 5:
        raise SystemExit("usage: python_runner.py WORKLOAD FIXTURE ITERATIONS SIZE")
    workload, fixture_path, iteration_text, size = sys.argv[1:]
    iterations = int(iteration_text)
    counts = workload_counts(size)
    count = counts[workload]
    point_count = counts["point_cloud_summary"]
    blob = Path(fixture_path).read_bytes()
    values = struct.unpack(FORMAT, blob)
    if values[0] != MAGIC or values[1] != N or len(blob) != struct.calcsize(FORMAT):
        raise SystemExit("fixture header/size mismatch")
    offset = 3
    actual = values[offset:offset + N]; offset += N
    load = values[offset:offset + N]; offset += N
    raster = values[offset:offset + N]; offset += N
    mask = values[offset:offset + N]; offset += N
    coordinates = values[offset:offset + COORDS]; offset += COORDS
    threshold, capacity = values[offset:offset + 2]
    out = [0.0] * 10
    iout = [0]

    if workload == "agent_energy_residual":
        def run() -> None:
            signed = absolute = maximum = 0.0
            for i in range(count):
                difference = actual[i] - load[i]
                magnitude = 0.0 - difference if difference < 0.0 else difference
                signed += difference; absolute += magnitude
                if magnitude > maximum: maximum = magnitude
            divisor = 0.0
            for _ in range(count): divisor += 1.0
            out[0] = signed; out[1] = maximum; out[2] = absolute / divisor
        output_count = 3
    elif workload == "agent_point_bounds":
        def run() -> None:
            min_x, min_y, min_z = coordinates[0], coordinates[1], coordinates[2]
            max_x, max_y, max_z = min_x, min_y, min_z
            for base in range(3, count * 3, 3):
                x, y, z = coordinates[base:base + 3]
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                if z < min_z: min_z = z
                if z > max_z: max_z = z
            out[:6] = [min_x, min_y, min_z, max_x, max_y, max_z]
        output_count = 6
    elif workload == "agent_raster_threshold_count":
        def run() -> None:
            found = 0
            for i in range(count):
                if mask[i] == 1 and raster[i] > threshold: found += 1
            iout[0] = found
        output_count = 1
    elif workload == "agent_raster_valid_mean":
        def run() -> None:
            total = 0.0; valid_count = 0
            for i in range(count):
                if mask[i] == 1:
                    total += raster[i]; valid_count += 1
            divisor = 0.0
            for _ in range(valid_count): divisor += 1.0
            out[0] = total / divisor
        output_count = 1
    elif workload == "energy_series_aggregation":
        def run() -> None:
            ac_energy = net_energy = absolute = 0.0
            peak = actual[0]
            for i in range(count):
                ac = actual[i]; demand = load[i]
                ac_energy += ac; net_energy = net_energy + ac - demand
                balance = ac - demand
                absolute += 0.0 - balance if balance < 0.0 else balance
                if ac > peak: peak = ac
            out[:5] = [ac_energy, peak, net_energy, ac_energy / (capacity * count), absolute / count]
        output_count = 5
    elif workload == "point_cloud_summary":
        def run() -> None:
            min_x, min_y, min_z = coordinates[0], coordinates[1], coordinates[2]
            max_x, max_y, max_z = min_x, min_y, min_z
            total_x = total_y = total_z = 0.0
            for point in range(point_count):
                base = point * 3
                x, y, z = coordinates[base], coordinates[base + 1], coordinates[base + 2]
                total_x += x; total_y += y; total_z += z
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if z < min_z: min_z = z
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                if z > max_z: max_z = z
            cx, cy, cz = total_x / float(point_count), total_y / float(point_count), total_z / float(point_count)
            radius = 0.0
            for point in range(point_count):
                base = point * 3
                dx, dy, dz = coordinates[base] - cx, coordinates[base + 1] - cy, coordinates[base + 2] - cz
                radius += dx * dx + dy * dy + dz * dz
            out[:] = [cx, cy, cz, min_x, min_y, min_z, max_x, max_y, max_z, (radius / point_count) ** 0.5]
        output_count = 10
    else:
        raise SystemExit(f"unknown workload: {workload}")

    run()  # correctness smoke outside the timed region
    start = time.perf_counter_ns()
    for _ in range(iterations): run()
    elapsed = time.perf_counter_ns() - start
    result = [iout[0]] if workload == "agent_raster_threshold_count" else list(out[:output_count])
    checksum = float(result[0]) if len(result) == 1 else sum(float(x) for x in result)
    print(json.dumps({
        "status": 0, "iterations": iterations, "elapsed_ns": elapsed,
        "ns_per_call": elapsed / iterations if iterations else 0.0, "checksum": checksum,
        "outputs": result, "maxrss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if resource else None,
    }, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
