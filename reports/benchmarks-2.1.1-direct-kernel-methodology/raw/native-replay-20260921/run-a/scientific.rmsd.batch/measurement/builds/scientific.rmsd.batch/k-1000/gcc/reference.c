#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

static volatile double observable;

static void require_allocation(const void *ptr) {
    if (ptr == NULL) {
        fputs("allocation failed\n", stderr);
        exit(2);
    }
}
int main(void) {
    const size_t pairs = 16, coordinates = 3;
    double *left = malloc(48 * sizeof(*left));
    double *right = malloc(48 * sizeof(*right));
    require_allocation(left); require_allocation(right);
    for (size_t i = 0; i < 48; ++i) { left[i] = (double)(i + 1); right[i] = (double)(i + 2); }
    for (size_t repetition = 0; repetition < 1000; ++repetition) {
        double total = 0.0;
        for (size_t pair = 0; pair < pairs; ++pair) {
            double ssd = 0.0;
            for (size_t coordinate = 0; coordinate < coordinates; ++coordinate) {
                size_t offset = pair * coordinates + coordinate;
                double delta = left[offset] - right[offset];
                ssd += delta * delta;
            }
            total += sqrt(ssd / (double)coordinates);
        }
        observable = total;
    }
    printf("program returned: %d\n", isfinite(observable) && fabs(observable - 16) <= 1e-9 ? 1 : 0);
    free(left); free(right);
    return 0;
}
