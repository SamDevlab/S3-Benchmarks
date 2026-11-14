#include <dlfcn.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>

typedef int64_t (*s3_diff_fn)(
    double*, int64_t, double*, int64_t, double*, int64_t, double*, int64_t,
    double*, int64_t, double*, int64_t, double*, int64_t, double*, int64_t,
    double*, int64_t, double*, int64_t,
    int64_t, double, double, double, double, double, int64_t, int64_t
);

typedef int64_t (*c_ftcs_fn)(double*, double*, int64_t, double, double, double, double, double, int64_t);

int main(int argc, char **argv) {
    if (argc < 4) return 2;
    const char *kind = argv[1];
    const char *so_path = argv[2];
    const char *sym = argv[3];

    void *h = dlopen(so_path, RTLD_NOW);
    if (!h) { fprintf(stderr, "dlopen: %s\n", dlerror()); return 3; }

    int64_t n = 101, steps = 500;
    double alpha = 0.05, dt = 0.0004, dx = 1.0 / (n - 1);
    double cur[101], nxt[101], a[101], b[101], c[101], d[101], cp[101], dp[101], sol[101], cser[501];
    for (int64_t i = 0; i < n; ++i) cur[i] = sin(M_PI * i * dx);

    if (strcmp(kind, "s3_diff") == 0) {
        s3_diff_fn fn = (s3_diff_fn)dlsym(h, sym);
        if (!fn) return 4;
        fn(cur, n, nxt, n, a, n, b, n, c, n, d, n, cp, n, dp, n, sol, n, cser, steps + 1,
           n, alpha, dt, dx, 0.0, 0.0, steps, 1);
    } else if (strcmp(kind, "c_ftcs") == 0) {
        c_ftcs_fn fn = (c_ftcs_fn)dlsym(h, sym);
        if (!fn) return 4;
        fn(cur, nxt, n, alpha, dt, dx, 0.0, 0.0, steps);
    }
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    printf("%ld\n", ru.ru_maxrss);
    dlclose(h);
    return 0;
}
