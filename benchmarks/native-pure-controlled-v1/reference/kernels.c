#include <math.h>
#include <stdint.h>

int64_t agent_energy_residual(const double *actual, int64_t actual_n,
                              const double *load, int64_t load_n,
                              int64_t count, double *output, int64_t output_n) {
    if (count <= 0 || count > 364 || actual_n != count || load_n != count) return 1;
    if (output_n != 3) return 1;
    double signed_sum = 0.0, absolute_sum = 0.0, maximum_absolute = 0.0;
    for (int64_t i = 0; i < count; ++i) {
        const double difference = actual[i] - load[i];
        const double magnitude = difference < 0.0 ? 0.0 - difference : difference;
        signed_sum += difference;
        absolute_sum += magnitude;
        if (magnitude > maximum_absolute) maximum_absolute = magnitude;
    }
    double divisor = 0.0;
    for (int64_t i = 0; i < count; ++i) divisor += 1.0;
    output[0] = signed_sum;
    output[1] = maximum_absolute;
    output[2] = absolute_sum / divisor;
    return 0;
}

int64_t agent_point_bounds(const double *coordinates, int64_t coordinate_n,
                           int64_t point_count, double *output, int64_t output_n) {
    if (point_count <= 0 || point_count > 121 || coordinate_n != point_count * 3) return 1;
    if (output_n != 6) return 1;
    double min_x = coordinates[0], min_y = coordinates[1], min_z = coordinates[2];
    double max_x = min_x, max_y = min_y, max_z = min_z;
    for (int64_t base = 3; base < point_count * 3; base += 3) {
        const double x = coordinates[base], y = coordinates[base + 1], z = coordinates[base + 2];
        if (x < min_x) min_x = x;
        if (x > max_x) max_x = x;
        if (y < min_y) min_y = y;
        if (y > max_y) max_y = y;
        if (z < min_z) min_z = z;
        if (z > max_z) max_z = z;
    }
    output[0] = min_x; output[1] = min_y; output[2] = min_z;
    output[3] = max_x; output[4] = max_y; output[5] = max_z;
    return 0;
}

int64_t agent_raster_threshold_count(const double *values, int64_t value_n,
                                     const int64_t *valid_mask, int64_t mask_n,
                                     int64_t cell_count, double threshold,
                                     int64_t *output, int64_t output_n) {
    if (cell_count <= 0 || cell_count > 364 || value_n != cell_count || mask_n != cell_count) return 1;
    if (output_n != 1) return 1;
    int64_t count = 0;
    for (int64_t i = 0; i < cell_count; ++i)
        if (valid_mask[i] == 1 && values[i] > threshold) ++count;
    output[0] = count;
    return 0;
}

int64_t agent_raster_valid_mean(const double *values, int64_t value_n,
                                const int64_t *valid_mask, int64_t mask_n,
                                int64_t cell_count, double *output, int64_t output_n) {
    if (cell_count <= 0 || cell_count > 364 || value_n != cell_count || mask_n != cell_count) return 1;
    if (output_n != 1) return 1;
    double sum = 0.0;
    int64_t valid_count = 0;
    for (int64_t i = 0; i < cell_count; ++i) {
        if (valid_mask[i] == 1) { sum += values[i]; ++valid_count; }
    }
    if (valid_count == 0) return 1;
    double divisor = 0.0;
    for (int64_t i = 0; i < valid_count; ++i) divisor += 1.0;
    output[0] = sum / divisor;
    return 0;
}

int64_t energy_series_aggregation(const double *ac_power, int64_t ac_count,
                                  const double *load, int64_t load_count,
                                  double capacity_w, double *output, int64_t output_count) {
    if (ac_count <= 0 || ac_count > 364 || capacity_w <= 0.0) return 1;
    if (load_count != ac_count || output_count != 5) return 2;
    double ac_energy = 0.0, net_energy = 0.0, peak = ac_power[0], absolute_balance = 0.0;
    for (int64_t i = 0; i < ac_count; ++i) {
        const double ac = ac_power[i], demand = load[i];
        ac_energy += ac;
        net_energy = net_energy + ac - demand;
        const double balance = ac - demand;
        absolute_balance += balance < 0.0 ? 0.0 - balance : balance;
        if (ac > peak) peak = ac;
    }
    output[0] = ac_energy;
    output[1] = peak;
    output[2] = net_energy;
    output[3] = ac_energy / (capacity_w * (double)ac_count);
    output[4] = absolute_balance / (double)ac_count;
    return 0;
}

int64_t point_cloud_summary(const double *coordinates, int64_t coordinate_n,
                            int64_t point_count, double *output, int64_t output_n) {
    if (point_count <= 0 || point_count > 121) return 1;
    if (coordinate_n != point_count * 3 || output_n != 10) return 2;
    double min_x = coordinates[0], min_y = coordinates[1], min_z = coordinates[2];
    double max_x = min_x, max_y = min_y, max_z = min_z;
    double total_x = 0.0, total_y = 0.0, total_z = 0.0;
    for (int64_t point = 0; point < point_count; ++point) {
        const int64_t base = point * 3;
        const double x = coordinates[base], y = coordinates[base + 1], z = coordinates[base + 2];
        total_x += x; total_y += y; total_z += z;
        if (x < min_x) min_x = x; if (y < min_y) min_y = y; if (z < min_z) min_z = z;
        if (x > max_x) max_x = x; if (y > max_y) max_y = y; if (z > max_z) max_z = z;
    }
    const double center_x = total_x / (double)point_count;
    const double center_y = total_y / (double)point_count;
    const double center_z = total_z / (double)point_count;
    double squared_radius_sum = 0.0;
    for (int64_t point = 0; point < point_count; ++point) {
        const int64_t base = point * 3;
        const double dx = coordinates[base] - center_x;
        const double dy = coordinates[base + 1] - center_y;
        const double dz = coordinates[base + 2] - center_z;
        squared_radius_sum += dx * dx + dy * dy + dz * dz;
    }
    output[0] = center_x; output[1] = center_y; output[2] = center_z;
    output[3] = min_x; output[4] = min_y; output[5] = min_z;
    output[6] = max_x; output[7] = max_y; output[8] = max_z;
    output[9] = sqrt(squared_radius_sum / (double)point_count);
    return 0;
}
