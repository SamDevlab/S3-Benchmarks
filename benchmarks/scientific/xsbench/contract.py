"""Faithful deterministic XSBench baseline lookup subset.

The subset keeps the baseline macroscopic lookup shape: material composition,
per-nuclide sorted energy grids, bounded binary search, interpolation, and
weighted reaction-channel accumulation. All storage is flat for the S3 ABI.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import re

from tools.ffi_direct_kernel_methodology import FFIPilot


WORKLOAD_ID = "scientific.xsbench.compatible_lookup"
SYMBOL = "xs_lookup_batch"
LOOKUPS_PER_CALL = 8
GRID_POINTS = 5
NUCLIDES = 3
MATERIALS = 2
MAX_NUCLIDES_PER_MATERIAL = 2
GRID_CHANNELS = 5
GRID_STRIDE = GRID_POINTS * GRID_CHANNELS
REACTION_WEIGHTS = (1.0, 3.0, 5.0, 7.0, 11.0)
QUERY_ENERGIES = (0.05, 0.22, 0.37, 0.49, 0.63, 0.78, 0.91, 0.14)
QUERY_ENERGY_TICKS = (5, 22, 37, 49, 63, 78, 91, 14)
QUERY_MATERIALS = (0, 1, 0, 1, 1, 0, 1, 0)
NUCLIDE_MAP = (0, 1, 1, 2)
GRID_ENERGY_TICKS = (0, 25, 50, 75, 100) * NUCLIDES
INDEX_METADATA = NUCLIDE_MAP + GRID_ENERGY_TICKS
GRID_BASE = 10


def _flat_data() -> tuple[float, ...]:
    values: list[float] = [3.0, 5.0, 2.0, 2.0, 2.0, 2.0, 0.6, 0.4, 0.25, 0.75]
    for nuclide in range(NUCLIDES):
        for point in range(GRID_POINTS):
            values.extend(
                (
                    float(1 + nuclide * 10 + point),
                    0.1 + nuclide * 10 + point * 0.1,
                    0.2 + nuclide * 10 + point * 0.1,
                    0.3 + nuclide * 10 + point * 0.1,
                    0.4 + nuclide * 10 + point * 0.1,
            )
            )
    return tuple(values)


DATA = _flat_data()


def _micro_xs(energy: float, nuclide: int) -> tuple[float, ...]:
    low = 0
    high = GRID_POINTS - 1
    while high - low > 1:
        middle = low + (high - low) // 2
        middle_energy = GRID_ENERGY_TICKS[nuclide * GRID_POINTS + middle] / 100.0
        if middle_energy > energy:
            high = middle
        else:
            low = middle
    low_base = GRID_BASE + nuclide * GRID_STRIDE + low * GRID_CHANNELS
    high_base = GRID_BASE + nuclide * GRID_STRIDE + high * GRID_CHANNELS
    low_energy = GRID_ENERGY_TICKS[nuclide * GRID_POINTS + low] / 100.0
    high_energy = GRID_ENERGY_TICKS[nuclide * GRID_POINTS + high] / 100.0
    factor = (high_energy - energy) / (high_energy - low_energy)
    return tuple(
        DATA[high_base + channel] - factor * (DATA[high_base + channel] - DATA[low_base + channel])
        for channel in range(GRID_CHANNELS)
    )


def oracle_lookup(energy: float, material: int) -> float:
    composition = ((0, 1), (1, 2))[material]
    concentrations = ((0.6, 0.4), (0.25, 0.75))[material]
    channels = [0.0] * 5
    for nuclide, concentration in zip(composition, concentrations):
        values = _micro_xs(energy, nuclide)
        for channel, value in enumerate(values):
            channels[channel] += concentration * value
    return sum(weight * value for weight, value in zip(REACTION_WEIGHTS, channels))


def oracle_result() -> float:
    return sum(oracle_lookup(energy, material) for energy, material in zip(QUERY_ENERGIES, QUERY_MATERIALS))


def s3_source(*, vector_mode: bool = False) -> str:
    source = """export fn xs_lookup_batch(data: &[f64], metadata: &[i64], energies: &[i64], materials: &[i64]) -> f64:
    mut lookup: i64 = 0
    mut checksum: f64 = 0.0
    while lookup < 8:
        mut energy_ticks: i64 = energies[lookup]
        mut energy: f64 = to_f64(energy_ticks) / 100.0
        mut material: i64 = materials[lookup]
        mut position: i64 = 0
        mut total_xs: f64 = 0.0
        mut elastic_xs: f64 = 0.0
        mut absorption_xs: f64 = 0.0
        mut fission_xs: f64 = 0.0
        mut nu_fission_xs: f64 = 0.0
        while position < 2:
            mut composition_index: i64 = material * 2 + position
            mut nuclide: i64 = metadata[composition_index]
            mut concentration_index: i64 = 6 + material * 2 + position
            mut concentration: f64 = data[concentration_index]
            mut low: i64 = 0
            mut high: i64 = 4
            mut grid_base: i64 = 10 + nuclide * 25
            while high - low > 1:
                mut middle: i64 = low + (high - low) / 2
                mut middle_index: i64 = 4 + nuclide * 5 + middle
                mut middle_energy_ticks: i64 = metadata[middle_index]
                match middle_energy_ticks <=> energy_ticks:
                    1:
                        high = middle

                    else:
                        low = middle
            mut low_index: i64 = grid_base + low * 5
            mut high_index: i64 = grid_base + high * 5
            mut low_energy_index: i64 = 4 + nuclide * 5 + low
            mut high_energy_index: i64 = 4 + nuclide * 5 + high
            mut low_energy_ticks: i64 = metadata[low_energy_index]
            mut high_energy_ticks: i64 = metadata[high_energy_index]
            mut low_energy: f64 = to_f64(low_energy_ticks) / 100.0
            mut high_energy: f64 = to_f64(high_energy_ticks) / 100.0
            mut factor: f64 = (high_energy - energy) / (high_energy - low_energy)
            mut high_total_index: i64 = high_index
            mut low_total_index: i64 = low_index
            mut high_elastic_index: i64 = high_index + 1
            mut low_elastic_index: i64 = low_index + 1
            mut high_absorption_index: i64 = high_index + 2
            mut low_absorption_index: i64 = low_index + 2
            mut high_fission_index: i64 = high_index + 3
            mut low_fission_index: i64 = low_index + 3
            mut high_nu_fission_index: i64 = high_index + 4
            mut low_nu_fission_index: i64 = low_index + 4
            total_xs = total_xs + concentration * (data[high_total_index] - factor * (data[high_total_index] - data[low_total_index]))
            elastic_xs = elastic_xs + concentration * (data[high_elastic_index] - factor * (data[high_elastic_index] - data[low_elastic_index]))
            absorption_xs = absorption_xs + concentration * (data[high_absorption_index] - factor * (data[high_absorption_index] - data[low_absorption_index]))
            fission_xs = fission_xs + concentration * (data[high_fission_index] - factor * (data[high_fission_index] - data[low_fission_index]))
            nu_fission_xs = nu_fission_xs + concentration * (data[high_nu_fission_index] - factor * (data[high_nu_fission_index] - data[low_nu_fission_index]))
            position = position + 1
        checksum = checksum + total_xs + 3.0 * elastic_xs + 5.0 * absorption_xs + 7.0 * fission_xs + 11.0 * nu_fission_xs
        lookup = lookup + 1
    return checksum

fn main() -> i64:
    return 0
"""
    if vector_mode:
        source = source.replace(
            "export fn xs_lookup_batch(data: &[f64], metadata: &[i64], energies: &[i64], materials: &[i64]) -> f64:",
            "fn xs_lookup_batch(data: &f64_vector, metadata: &i64_vector, energies: &i64_vector, materials: &i64_vector) -> f64:",
        )
        for name, getter in (("data", "f64_vector_get"), ("metadata", "i64_vector_get"), ("energies", "i64_vector_get"), ("materials", "i64_vector_get")):
            source = re.sub(rf"\b{name}\[([^]]+)\]", rf"{getter}({name}, \1)", source)
    return source


def hosted_source() -> str:
    pushes = [f"    discard f64_vector_push(&mut data, {value!r})" for value in DATA]
    metadata_pushes = [f"    discard i64_vector_push(&mut metadata, {value})" for value in INDEX_METADATA]
    energy_pushes = [f"    discard i64_vector_push(&mut energies, {value})" for value in QUERY_ENERGY_TICKS]
    material_pushes = [f"    discard i64_vector_push(&mut materials, {value})" for value in QUERY_MATERIALS]
    return s3_source(vector_mode=True).replace(
        "fn main() -> i64:\n    return 0\n",
        "fn main() -> f64:\n"
        "    mut data: f64_vector = f64_vector_new(85)\n"
        + "\n".join(pushes)
        + "\n    mut metadata: i64_vector = i64_vector_new(19)\n"
        + "\n".join(metadata_pushes)
        + "\n    mut energies: i64_vector = i64_vector_new(8)\n"
        + "\n".join(energy_pushes)
        + "\n    mut materials: i64_vector = i64_vector_new(8)\n"
        + "\n".join(material_pushes)
        + "\n    return xs_lookup_batch(&data, &metadata, &energies, &materials)\n",
    )


def c_source() -> str:
    data = ", ".join(repr(value) for value in DATA)
    metadata = ", ".join(str(value) for value in INDEX_METADATA)
    energies = ", ".join(str(value) for value in QUERY_ENERGY_TICKS)
    return f"""#include <stdint.h>
#include <stddef.h>
double {SYMBOL}(const double *data, int64_t data_len, const int64_t *metadata, int64_t metadata_len, const int64_t *energies, int64_t energy_len, const int64_t *materials, int64_t material_len) {{
    (void)data_len; (void)metadata_len; (void)energy_len; (void)material_len;
    double checksum = 0.0;
    for (int64_t lookup = 0; lookup < 8; ++lookup) {{
        int64_t energy_ticks = energies[lookup];
        double energy = (double)energy_ticks / 100.0;
        int64_t material = materials[lookup];
        double channels[5] = {{0.0, 0.0, 0.0, 0.0, 0.0}};
        for (int64_t position = 0; position < 2; ++position) {{
            int64_t composition_index = material * 2 + position;
            int64_t nuclide = metadata[composition_index];
            double concentration = data[6 + material * 2 + position];
            int64_t low = 0, high = 4;
            int64_t grid_base = 10 + nuclide * 25;
            while (high - low > 1) {{
                int64_t middle = low + (high - low) / 2;
                if (metadata[4 + nuclide * 5 + middle] > energy_ticks) high = middle;
                else low = middle;
            }}
            int64_t low_index = grid_base + low * 5;
            int64_t high_index = grid_base + high * 5;
            double low_energy = (double)metadata[4 + nuclide * 5 + low] / 100.0;
            double high_energy = (double)metadata[4 + nuclide * 5 + high] / 100.0;
            double factor = (high_energy - energy) / (high_energy - low_energy);
            for (int channel = 0; channel < 5; ++channel) {{
                int64_t offset = channel;
                channels[channel] += concentration * (data[high_index + offset] - factor * (data[high_index + offset] - data[low_index + offset]));
            }}
        }}
        checksum += channels[0] + 3.0 * channels[1] + 5.0 * channels[2] + 7.0 * channels[3] + 11.0 * channels[4];
    }}
    return checksum;
}}

static const double xsbench_fixture_data[] = {{{data}}};
static const int64_t xsbench_fixture_energies[] = {{{energies}}};
static const int64_t xsbench_fixture_metadata[] = {{{metadata}}};
static const int64_t xsbench_fixture_materials[] = {{0, 1, 0, 1, 1, 0, 1, 0}};
"""


def pilot() -> FFIPilot:
    return FFIPilot(
        WORKLOAD_ID,
        SYMBOL,
        s3_source(),
        c_source().replace("const double *data", "const double *data", 1),
        oracle_result(),
        LOOKUPS_PER_CALL,
        "2 materials x 2 nuclides x 5-point grids x 5 reaction channels",
        "material * max_nuclides + position; nuclide * grid_stride + point",
        "scientific-irregular",
    )


@dataclass(frozen=True, slots=True)
class FixtureSummary:
    data_values: int
    lookup_count: int
    expected: float


def fixture_summary() -> FixtureSummary:
    return FixtureSummary(len(DATA), LOOKUPS_PER_CALL, oracle_result())
