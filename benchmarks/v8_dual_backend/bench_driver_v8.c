/* S3 V8 native micro-benchmark driver.
 *
 * - No Python in the timed region; CLOCK_MONOTONIC (clock_gettime) timestamps
 *   only bracket whole batches of calls.
 * - Target function is resolved with dlsym() and called through a function
 *   pointer (no inlining / no constant folding across the .so boundary).
 * - Inputs vary at run time (base + (i & 15)) and are read from a runtime
 *   filled array; every result is folded into a volatile sink.
 * - Modes: bench, verify, clock.
 *
 *   bench_driver_v8 bench  <so> <fn> <argc_mode> <T> <batch> <nbatches> [a2 [a3]]
 *   bench_driver_v8 verify <so> <fn> <argc_mode> <T> [a2 [a3]]
 *   bench_driver_v8 clock
 */
#define _POSIX_C_SOURCE 199309L
#include <dlfcn.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static volatile int64_t g_sink = 0;
static int64_t g_inputs[16];

static double now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec * 1e9 + (double)ts.tv_nsec;
}

static int cmp_d(const void *a, const void *b) {
    double x = *(const double *)a, y = *(const double *)b;
    return (x > y) - (x < y);
}

static int64_t call(void *sym, int mode, int64_t n, int64_t a2, int64_t a3) {
    if (mode == 1) return ((int64_t(*)(int64_t))sym)(n);
    if (mode == 2) return ((int64_t(*)(int64_t, int64_t))sym)(n, a2);
    return ((int64_t(*)(int64_t, int64_t, int64_t))sym)(n, a2, a3);
}

int main(int argc, char **argv) {
    if (argc >= 2 && strcmp(argv[1], "clock") == 0) {
        struct timespec res;
        clock_getres(CLOCK_MONOTONIC, &res);
        enum { N = 200000 };
        static double d[N];
        double prev = now_ns();
        for (int i = 0; i < N; ++i) {
            double t = now_ns();
            d[i] = t - prev;
            prev = t;
        }
        qsort(d, N, sizeof(double), cmp_d);
        double min_pos = 0.0;
        for (int i = 0; i < N; ++i)
            if (d[i] > 0.0) { min_pos = d[i]; break; }
        printf("{\"clock_getres_ns\": %.3f, \"back_to_back_median_ns\": %.3f, \"back_to_back_p99_ns\": %.3f, \"min_positive_delta_ns\": %.3f}\n",
               (double)res.tv_sec * 1e9 + (double)res.tv_nsec, d[N / 2], d[(N * 99) / 100], min_pos);
        return 0;
    }
    if (argc < 6) {
        fprintf(stderr, "usage error\n");
        return 2;
    }
    int verify = strcmp(argv[1], "verify") == 0;
    const char *so_path = argv[2];
    const char *fn_name = argv[3];
    int mode = atoi(argv[4]);
    int64_t T = strtoll(argv[5], NULL, 10);
    long batch = 0, nbatches = 0;
    int ai = 6;
    if (!verify) {
        if (argc < 8) { fprintf(stderr, "usage error\n"); return 2; }
        batch = atol(argv[6]);
        nbatches = atol(argv[7]);
        ai = 8;
    }
    int64_t a2 = argc > ai ? strtoll(argv[ai], NULL, 10) : 0;
    int64_t a3 = argc > ai + 1 ? strtoll(argv[ai + 1], NULL, 10) : 0;
    for (int i = 0; i < 16; ++i) g_inputs[i] = T + i;

    void *h = dlopen(so_path, RTLD_NOW);
    if (!h) { fprintf(stderr, "dlopen: %s\n", dlerror()); return 3; }
    void *sym = dlsym(h, fn_name);
    if (!sym) { fprintf(stderr, "dlsym: %s\n", dlerror()); return 4; }

    if (verify) {
        uint64_t sum = 0, x = 0;
        int64_t first = 0;
        for (int i = 0; i < 64; ++i) {
            int64_t r = call(sym, mode, g_inputs[i & 15], a2, a3);
            if (i == 0) first = r;
            sum += (uint64_t)r;
            x ^= (uint64_t)r * 0x9E3779B97F4A7C15ULL + (uint64_t)i;
        }
        printf("{\"first\": %lld, \"sum\": %llu, \"mix\": %llu}\n", (long long)first,
               (unsigned long long)sum, (unsigned long long)x);
        return 0;
    }

    /* warm-up */
    int64_t acc = 0;
    for (long i = 0; i < batch; ++i) acc ^= call(sym, mode, g_inputs[i & 15], a2, a3);
    g_sink = acc;

    printf("{\"per_call_ns\": [");
    for (long b = 0; b < nbatches; ++b) {
        acc = 0;
        double t0 = now_ns();
        for (long i = 0; i < batch; ++i) acc ^= call(sym, mode, g_inputs[i & 15], a2, a3);
        double t1 = now_ns();
        g_sink = acc;
        printf("%s%.4f", b ? ", " : "", (t1 - t0) / (double)batch);
    }
    printf("], \"batch\": %ld, \"sink\": %lld}\n", batch, (long long)g_sink);
    dlclose(h);
    return 0;
}
