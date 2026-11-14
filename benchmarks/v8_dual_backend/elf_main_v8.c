/* Standalone ELF harness for S3-to-C generated_optimized.elf (V8 Section 19-20).
 * Supports executing any exported corpus function via direct C call (no dlopen/dlsym)
 * and measuring direct-call vs dlsym FFI overhead.
 */
#define _POSIX_C_SOURCE 199309L
#include "generated_optimized.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static volatile int64_t g_sink = 0;

static double now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec * 1e9 + (double)ts.tv_nsec;
}

__attribute__((noinline))
static int64_t noop1_direct(int64_t x) {
    return x;
}

int main(int argc, char **argv) {
    if (argc >= 2 && strcmp(argv[1], "bench-direct") == 0) {
        int64_t T = argc > 2 ? strtoll(argv[2], NULL, 10) : 10000;
        long batch = argc > 3 ? atol(argv[3]) : 200000;
        int64_t xs[16];
        for (int i = 0; i < 16; ++i) xs[i] = T + i;

        int64_t acc = 0;
        for (long i = 0; i < batch; ++i) acc ^= noop1_direct(xs[i & 15]);
        double t0 = now_ns();
        for (long i = 0; i < batch; ++i) acc ^= noop1_direct(xs[i & 15]);
        double t1 = now_ns();
        double noop_ns = (t1 - t0) / (double)batch;

        for (long i = 0; i < batch; ++i) acc ^= sum_quasi_parity(xs[i & 15]);
        t0 = now_ns();
        for (long i = 0; i < batch; ++i) acc ^= sum_quasi_parity(xs[i & 15]);
        t1 = now_ns();
        double sqp_ns = (t1 - t0) / (double)batch;

        for (long i = 0; i < batch; ++i) acc ^= sum_i2(xs[i & 15]);
        t0 = now_ns();
        for (long i = 0; i < batch; ++i) acc ^= sum_i2(xs[i & 15]);
        t1 = now_ns();
        double si2_ns = (t1 - t0) / (double)batch;

        for (long i = 0; i < batch; ++i) acc ^= triangular_cubic(xs[i & 15], 13, -7);
        t0 = now_ns();
        for (long i = 0; i < batch; ++i) acc ^= triangular_cubic(xs[i & 15], 13, -7);
        t1 = now_ns();
        double tri_ns = (t1 - t0) / (double)batch;

        g_sink = acc;
        printf("{\"noop_direct_ns\": %.4f, \"sum_quasi_parity_direct_ns\": %.4f, \"sum_i2_direct_ns\": %.4f, \"triangular_cubic_direct_ns\": %.4f, \"sink\": %lld}\n",
               noop_ns, sqp_ns, si2_ns, tri_ns, (long long)g_sink);
        return 0;
    }
    if (argc >= 3 && strcmp(argv[1], "call") == 0) {
        const char *fn = argv[2];
        int64_t a1 = argc > 3 ? strtoll(argv[3], NULL, 10) : 0;
        int64_t a2 = argc > 4 ? strtoll(argv[4], NULL, 10) : 0;
        int64_t a3 = argc > 5 ? strtoll(argv[5], NULL, 10) : 0;
        int64_t out = 0;
        if (strcmp(fn, "sum_quasi_parity") == 0) out = sum_quasi_parity(a1);
        else if (strcmp(fn, "sum_i2") == 0) out = sum_i2(a1);
        else if (strcmp(fn, "triangular_cubic") == 0) out = triangular_cubic(a1, a2, a3);
        else if (strcmp(fn, "coupled_exchange") == 0) out = coupled_exchange(a1, a2, a3);
        else if (strcmp(fn, "lcg_mod") == 0) out = lcg_mod(a1, a2, a3);
        else if (strcmp(fn, "fib_mod") == 0) out = fib_mod(a1, a2);
        else return 2;
        printf("%lld\n", (long long)out);
        return 0;
    }
    /* Default smoke execution across all exported functions */
    int64_t v_sqp = sum_quasi_parity(10000);
    int64_t v_si2 = sum_i2(10000);
    int64_t v_tri = triangular_cubic(10000, 13, -7);
    int64_t v_ce = coupled_exchange(10000, 10, -3);
    int64_t v_lcg = lcg_mod(10000, 7, 1000000007);
    int64_t v_fib = fib_mod(10000, 1000000007);
    printf("{\"sum_quasi_parity\": %lld, \"sum_i2\": %lld, \"triangular_cubic\": %lld, \"coupled_exchange\": %lld, \"lcg_mod\": %lld, \"fib_mod\": %lld}\n",
           (long long)v_sqp, (long long)v_si2, (long long)v_tri, (long long)v_ce, (long long)v_lcg, (long long)v_fib);
    return 0;
}
