"""Faithful deterministic XSBench baseline lookup subset.

The subset keeps the baseline macroscopic lookup shape: material composition,
per-nuclide sorted energy grids, bounded binary search, interpolation, and
weighted reaction-channel accumulation. All storage is flat for the S3 ABI.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from tools.ffi_direct_kernel_methodology import FFIPilot


WORKLOAD_ID = "scientific.xsbench.compatible_lookup"
SYMBOL = "xs_lookup_batch"
LOOKUPS_PER_CALL = 8
GRID_POINTS = 5
NUCLIDES = 3
MATERIALS = 2
MAX_NUCLIDES_PER_MATERIAL = 2
GRID_BASE = 14
GRID_STRIDE = GRID_POINTS * 6
REACTION_WEIGHTS = (1.0, 3.0, 5.0, 7.0, 11.0)
QUERY_ENERGIES = (0.05, 0.22, 0.37, 0.49, 0.63, 0.78, 0.91, 0.14)
QUERY_MATERIALS = (0, 1, 0, 1, 1, 0, 1, 0)


def _flat_data() -> tuple[float, ...]:
    values: list[float] = [3.0, 5.0, 2.0, 2.0, 2.0, 2.0, 0.0, 1.0, 1.0, 2.0, 0.6, 0.4, 0.25, 0.75]
    for nuclide in range(NUCLIDES):
        for point in range(GRID_POINTS):
            energy = point / 4.0
            values.extend(
                (
                    energy,
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
        middle_energy = DATA[GRID_BASE + nuclide * GRID_STRIDE + middle * 6]
        if middle_energy > energy:
            high = middle
        else:
            low = middle
    low_base = GRID_BASE + nuclide * GRID_STRIDE + low * 6
    high_base = GRID_BASE + nuclide * GRID_STRIDE + high * 6
    factor = (DATA[high_base] - energy) / (DATA[high_base] - DATA[low_base])
    return tuple(
        DATA[high_base + channel] - factor * (DATA[high_base + channel] - DATA[low_base + channel])
        for channel in range(1, 6)
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


def s3_source() -> str:
    return """export fn xs_lookup_batch(data: &[f64], energies: &[f64], materials: &[f64]) -> f64:
    mut lookup: i64 = 0
    mut checksum: f64 = 0.0
    while lookup < 8:
        mut energy: f64 = energies[lookup]
        mut material: i64 = to_i64(materials[lookup])
        mut position: i64 = 0
        mut total_xs: f64 = 0.0
        mut elastic_xs: f64 = 0.0
        mut absorption_xs: f64 = 0.0
        mut fission_xs: f64 = 0.0
        mut nu_fission_xs: f64 = 0.0
        while position < 2:
            mut composition_index: i64 = 6 + material * 2 + position
            mut nuclide: i64 = to_i64(data[composition_index])
            mut concentration: f64 = data[10 + material * 2 + position]
            mut low: i64 = 0
            mut high: i64 = 4
            mut grid_base: i64 = 14 + nuclide * 30
            while high - low > 1:
                mut middle: i64 = low + (high - low) / 2
                mut middle_index: i64 = grid_base + middle * 6
                mut middle_energy: f64 = data[middle_index]
                match middle_energy > energy:
                    high = middle
                else:
                    low = middle
            mut low_index: i64 = grid_base + low * 6
            mut high_index: i64 = grid_base + high * 6
            mut factor: f64 = (data[high_index] - energy) / (data[high_index] - data[low_index])
            total_xs = total_xs + concentration * (data[high_index + 1] - factor * (data[high_index + 1] - data[low_index + 1]))
            elastic_xs = elastic_xs + concentration * (data[high_index + 2] - factor * (data[high_index + 2] - data[low_index + 2]))
            absorption_xs = absorption_xs + concentration * (data[high_index + 3] - factor * (data[high_index + 3] - data[low_index + 3]))
            fission_xs = fission_xs + concentration * (data[high_index + 4] - factor * (data[high_index + 4] - data[low_index + 4]))
            nu_fission_xs = nu_fission_xs + concentration * (data[high_index + 5] - factor * (data[high_index + 5] - data[low_index + 5]))
            position = position + 1
        checksum = checksum + total_xs + 3.0 * elastic_xs + 5.0 * absorption_xs + 7.0 * fission_xs + 11.0 * nu_fission_xs
        lookup = lookup + 1
    return checksum

fn main() -> i64:
    return 0
"""


def hosted_source() -> str:
    pushes = [f"    discard f64_vector_push(&mut data, {value!r})" for value in DATA]
    energy_pushes = [f"    discard f64_vector_push(&mut energies, {value!r})" for value in QUERY_ENERGIES]
    material_pushes = [f"    discard f64_vector_push(&mut materials, {float(value)!r})" for value in QUERY_MATERIALS]
    return s3_source().replace(
        "fn main() -> i64:\n    return 0\n",
        "fn main() -> f64:\n"
        "    mut data: f64_vector = f64_vector_new(104)\n"
        + "\n".join(pushes)
        + "\n    mut energies: f64_vector = f64_vector_new(8)\n"
        + "\n".join(energy_pushes)
        + "\n    mut materials: f64_vector = f64_vector_new(8)\n"
        + "\n".join(material_pushes)
        + "\n    return xs_lookup_batch(&data, &energies, &materials)\n",
    )


def c_source() -> str:
    data = ", ".join(repr(value) for value in DATA)
    energies = ", ".join(repr(value) for value in QUERY_ENERGIES)
    materials = ", ".join(repr(float(value)) for value in QUERY_MATERIALS)
    return f"""#include <stdint.h>
#include <stddef.h>
double {SYMBOL}(const double *data, int64_t data_len, const double *energies, int64_t energy_len, const double *materials, int64_t material_len) {{
    (void)data_len; (void)energy_len; (void)material_len;
    double checksum = 0.0;
    for (int64_t lookup = 0; lookup < 8; ++lookup) {{
        double energy = energies[lookup];
        int64_t material = (int64_t)materials[lookup];
        double channels[5] = {{0.0, 0.0, 0.0, 0.0, 0.0}};
        for (int64_t position = 0; position < 2; ++position) {{
            int64_t composition_index = 6 + material * 2 + position;
            int64_t nuclide = (int64_t)data[composition_index];
            double concentration = data[10 + material * 2 + position];
            int64_t low = 0, high = 4;
            int64_t grid_base = 14 + nuclide * 30;
            while (high - low > 1) {{
                int64_t middle = low + (high - low) / 2;
                if (data[grid_base + middle * 6] > energy) high = middle;
                else low = middle;
            }}
            int64_t low_index = grid_base + low * 6;
            int64_t high_index = grid_base + high * 6;
            double factor = (data[high_index] - energy) / (data[high_index] - data[low_index]);
            for (int channel = 0; channel < 5; ++channel) {{
                int64_t offset = channel + 1;
                channels[channel] += concentration * (data[high_index + offset] - factor * (data[high_index + offset] - data[low_index + offset]));
            }}
        }}
        checksum += channels[0] + 3.0 * channels[1] + 5.0 * channels[2] + 7.0 * channels[3] + 11.0 * channels[4];
    }}
    return checksum;
}}

static const double xsbench_fixture_data[] = {{{data}}};
static const double xsbench_fixture_energies[] = {{{energies}}};
static const double xsbench_fixture_materials[] = {{{materials}}};
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
