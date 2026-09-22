#include <stdint.h>
#include <stddef.h>
double xs_lookup_batch(const double *data, int64_t data_len, const int64_t *metadata, int64_t metadata_len) {
    (void)data_len; (void)metadata_len;
    double checksum = 0.0;
    int64_t lookup_limit = metadata[35];
    for (int64_t lookup = 0; lookup < lookup_limit; ++lookup) {
        int64_t energy_ticks = metadata[19 + lookup];
        double energy = (double)energy_ticks / 100.0;
        int64_t material = metadata[27 + lookup];
        double channels[5] = {0.0, 0.0, 0.0, 0.0, 0.0};
        for (int64_t position = 0; position < 2; ++position) {
            int64_t composition_index = material * 2 + position;
            int64_t nuclide = metadata[composition_index];
            double concentration = data[6 + material * 2 + position];
            int64_t low = 0, high = 4;
            int64_t grid_base = 10 + nuclide * 25;
            while (high - low > 1) {
                int64_t middle = low + (high - low) / 2;
                if (metadata[4 + nuclide * 5 + middle] > energy_ticks) high = middle;
                else low = middle;
            }
            int64_t low_index = grid_base + low * 5;
            int64_t high_index = grid_base + high * 5;
            double low_energy = (double)metadata[4 + nuclide * 5 + low] / 100.0;
            double high_energy = (double)metadata[4 + nuclide * 5 + high] / 100.0;
            double factor = (high_energy - energy) / (high_energy - low_energy);
            for (int channel = 0; channel < 5; ++channel) {
                int64_t offset = channel;
                channels[channel] += concentration * (data[high_index + offset] - factor * (data[high_index + offset] - data[low_index + offset]));
            }
        }
        checksum += channels[0] + 3.0 * channels[1] + 5.0 * channels[2] + 7.0 * channels[3] + 11.0 * channels[4];
    }
    return checksum;
}

static const double xsbench_fixture_data[] = {3.0, 5.0, 2.0, 2.0, 2.0, 2.0, 0.6, 0.4, 0.25, 0.75, 1.0, 0.1, 0.2, 0.3, 0.4, 2.0, 0.2, 0.30000000000000004, 0.4, 0.5, 3.0, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 4.0, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 5.0, 0.5, 0.6000000000000001, 0.7, 0.8, 11.0, 10.1, 10.2, 10.3, 10.4, 12.0, 10.2, 10.299999999999999, 10.4, 10.5, 13.0, 10.299999999999999, 10.399999999999999, 10.5, 10.6, 14.0, 10.4, 10.5, 10.600000000000001, 10.700000000000001, 15.0, 10.5, 10.6, 10.700000000000001, 10.8, 21.0, 20.1, 20.2, 20.3, 20.4, 22.0, 20.200000000000003, 20.3, 20.400000000000002, 20.5, 23.0, 20.3, 20.4, 20.5, 20.599999999999998, 24.0, 20.400000000000002, 20.5, 20.6, 20.7, 25.0, 20.5, 20.599999999999998, 20.7, 20.799999999999997};
static const int64_t xsbench_fixture_metadata[] = {0, 1, 1, 2, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1};
