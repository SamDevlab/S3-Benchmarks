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
    const size_t rows = 12, cols = 16, inner = 8;
    double *a = malloc(rows * inner * sizeof(*a));
    double *b = malloc(inner * cols * sizeof(*b));
    double *c = malloc(rows * cols * sizeof(*c));
    require_allocation(a); require_allocation(b); require_allocation(c);
    for (size_t i = 0; i < rows * inner; ++i) a[i] = (double)(i + 1);
    for (size_t i = 0; i < inner * cols; ++i) b[i] = (double)(i + 2);
    for (size_t i = 0; i < rows * cols; ++i) c[i] = 1.0;
    for (size_t repetition = 0; repetition < 1; ++repetition) {
        double checksum = 0.0;
        for (size_t i = 0; i < rows; ++i) for (size_t j = 0; j < cols; ++j) {
            double total = 1.0;
            for (size_t k = 0; k < inner; ++k) total += a[i * inner + k] * b[k * cols + j];
            c[i * cols + j] = total;
        }
        for (size_t i = 0; i < rows * cols; ++i) checksum += c[i];
        observable = checksum;
    }
    printf("program returned: %d\n", isfinite(observable) && fabs(observable - 5008704) <= 1e-9 ? 1 : 0);
    free(a); free(b); free(c);
    return 0;
}
