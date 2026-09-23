#include <math.h>
#include <stdint.h>
double identity_f64(double value) { return value; }
double rmsd(const double *left, int64_t left_len, const double *right, int64_t right_len, int64_t pairs, int64_t coordinates) {
    (void)left_len; (void)right_len;
    double total = 0.0;
    for (int64_t pair = 0; pair < pairs; ++pair) {
        double ssd = 0.0;
        for (int64_t coordinate = 0; coordinate < coordinates; ++coordinate) {
            int64_t offset = pair * coordinates + coordinate;
            double delta = left[offset] - right[offset];
            ssd += delta * delta;
        }
        total += sqrt(ssd / (double)coordinates);
    }
    return total;
}
