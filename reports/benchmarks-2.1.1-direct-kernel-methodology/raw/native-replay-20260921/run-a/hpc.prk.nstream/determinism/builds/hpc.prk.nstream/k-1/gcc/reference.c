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
    const size_t n = 31;
    double *a = malloc(n * sizeof(*a));
    double *b = malloc(n * sizeof(*b));
    double *c = malloc(n * sizeof(*c));
    require_allocation(a); require_allocation(b); require_allocation(c);
    for (size_t i = 0; i < n; ++i) { a[i] = (double)(i + 1); b[i] = (double)(i + 2); c[i] = 1.0; }
    for (size_t repetition = 0; repetition < 1; ++repetition) {
        double total = 0.0;
        for (size_t i = 0; i < n; ++i) {
            double value = a[i] + b[i] + 2.0 * c[i];
            a[i] = value;
            total += value;
        }
        observable = total;
    }
    printf("program returned: %d\n", isfinite(observable) && fabs(observable - 1085) <= 1e-9 ? 1 : 0);
    free(a); free(b); free(c);
    return 0;
}
