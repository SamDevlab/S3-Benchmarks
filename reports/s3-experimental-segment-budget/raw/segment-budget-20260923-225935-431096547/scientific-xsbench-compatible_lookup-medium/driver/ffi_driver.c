#define _GNU_SOURCE
#include <dlfcn.h>
#include <inttypes.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef double (*identity_fn)(double);
typedef double (*triad_fn)(double *, int64_t, const double *, int64_t, const double *, int64_t, double);
typedef double (*nstream_fn)(const double *, int64_t, const double *, int64_t, const double *, int64_t, double);
typedef double (*gemm_fn)(const double *, int64_t, const double *, int64_t, const double *, int64_t);
typedef double (*rmsd_fn)(const double *, int64_t, const double *, int64_t, int64_t, int64_t);
typedef double (*xsbench_fn)(const double *, int64_t, const int64_t *, int64_t);

static void fail(const char *message) { fprintf(stderr, "%s\n", message); exit(2); }
static double *alloc_doubles(size_t count) { double *p = calloc(count, sizeof(*p)); if (!p) fail("allocation failed"); return p; }
static int64_t parse_i64(const char *text) { char *end = NULL; long long value = strtoll(text, &end, 10); if (!text[0] || !end || *end) fail("invalid integer argument"); return (int64_t)value; }
static double parse_f64(const char *text) { char *end = NULL; double value = strtod(text, &end); if (!text[0] || !end || *end) fail("invalid float argument"); return value; }
static uint64_t now_ns(void) { struct timespec ts; if (clock_gettime(CLOCK_MONOTONIC_RAW, &ts) != 0) fail("clock_gettime failed"); return (uint64_t)ts.tv_sec * 1000000000ull + (uint64_t)ts.tv_nsec; }
static void *symbol(void *handle, const char *name) { dlerror(); void *value = dlsym(handle, name); const char *error = dlerror(); if (error) { fprintf(stderr, "dlsym: %s\n", error); exit(2); } return value; }
static int close_enough(double actual, double expected) { double scale = fmax(1.0, fabs(expected)); return isfinite(actual) && fabs(actual - expected) <= 1e-9 * scale; }
static void emit_result(const char *workload, const char *variant, int64_t k, uint64_t elapsed, double observable, double expected) {
    int pass = close_enough(observable, expected);
    printf("{\"status\":\"%s\",\"workload\":\"%s\",\"variant\":\"%s\",\"K\":%" PRId64 ",\"elapsed_ns\":%" PRIu64 ",\"observable\":%.17g,\"expected\":%.17g,\"returncode\":%d}\n", pass ? "PASS" : "FAIL", workload, variant, k, elapsed, observable, expected, pass ? 0 : 1);
}

int main(int argc, char **argv) {
    if (argc != 8) fail("usage: driver LIB WORKLOAD VARIANT SYMBOL K EXPECTED WARMUPS");
    const char *library_path = argv[1], *workload = argv[2], *variant = argv[3], *exported_symbol = argv[4];
    int64_t k = parse_i64(argv[5]), warmups = parse_i64(argv[7]);
    double expected = parse_f64(argv[6]);
    if (k < 1 || warmups < 0) fail("invalid K or warmups");
    void *handle = dlopen(library_path, RTLD_NOW | RTLD_LOCAL);
    if (!handle) { fprintf(stderr, "dlopen: %s\n", dlerror()); return 2; }
    double observable = 0.0;
    uint64_t begin = 0, end = 0;
    if (strcmp(workload, "identity_f64") == 0) {
        identity_fn fn = (identity_fn)symbol(handle, exported_symbol);
        for (int64_t w = 0; w < warmups; ++w) for (int64_t i = 0; i < k; ++i) observable = fn(1.25);
        begin = now_ns(); for (int64_t i = 0; i < k; ++i) observable = fn(1.25); end = now_ns();
    } else if (strcmp(workload, "memory.babelstream.triad") == 0 || strcmp(workload, "hpc.prk.nstream") == 0) {
        int triad = strcmp(workload, "memory.babelstream.triad") == 0;
        double *a = alloc_doubles(31), *b = alloc_doubles(31), *c = alloc_doubles(31);
        for (int64_t i = 0; i < 31; ++i) { a[i] = (double)(i + 1); b[i] = triad ? (double)(2 * i + 1) : (double)(i + 2); c[i] = triad ? (double)(3 * i + 1) : 1.0; }
        if (triad) {
            triad_fn fn = (triad_fn)symbol(handle, exported_symbol);
            for (int64_t w = 0; w < warmups; ++w) for (int64_t i = 0; i < k; ++i) observable = fn(a, 31, b, 31, c, 31, 2.0);
            for (int64_t i = 0; i < 31; ++i) { a[i] = (double)(i + 1); b[i] = (double)(2 * i + 1); c[i] = (double)(3 * i + 1); }
            begin = now_ns(); for (int64_t i = 0; i < k; ++i) observable = fn(a, 31, b, 31, c, 31, 2.0); end = now_ns();
        } else {
            nstream_fn fn = (nstream_fn)symbol(handle, exported_symbol);
            for (int64_t w = 0; w < warmups; ++w) for (int64_t i = 0; i < k; ++i) observable = fn(a, 31, b, 31, c, 31, 2.0);
            for (int64_t i = 0; i < 31; ++i) { a[i] = (double)(i + 1); b[i] = (double)(i + 2); c[i] = 1.0; }
            begin = now_ns(); for (int64_t i = 0; i < k; ++i) observable = fn(a, 31, b, 31, c, 31, 2.0); end = now_ns();
        }
        free(a); free(b); free(c);
    } else if (strcmp(workload, "numerical.polybench.gemm") == 0) {
        gemm_fn fn = (gemm_fn)symbol(handle, exported_symbol);
        const int64_t rows = 4, cols = 4, inner = 4;
        double *a = alloc_doubles(rows * inner), *b = alloc_doubles(inner * cols), *c = alloc_doubles(rows * cols);
        for (int64_t i = 0; i < rows * inner; ++i) a[i] = (double)(i + 1);
        for (int64_t i = 0; i < inner * cols; ++i) b[i] = (double)(i + 2);
        for (int64_t i = 0; i < rows * cols; ++i) c[i] = 1.0;
        for (int64_t w = 0; w < warmups; ++w) for (int64_t i = 0; i < k; ++i) observable = fn(a, rows * inner, b, inner * cols, c, rows * cols);
        begin = now_ns(); for (int64_t i = 0; i < k; ++i) observable = fn(a, rows * inner, b, inner * cols, c, rows * cols); end = now_ns();
        free(a); free(b); free(c);
    } else if (strcmp(workload, "scientific.rmsd.batch") == 0) {
        rmsd_fn fn = (rmsd_fn)symbol(handle, exported_symbol);
        const int64_t pairs = 16, coordinates = 3;
        double *left = alloc_doubles(pairs * coordinates), *right = alloc_doubles(pairs * coordinates);
        for (int64_t i = 0; i < pairs * coordinates; ++i) { left[i] = (double)(i + 1); right[i] = (double)(i + 2); }
        for (int64_t w = 0; w < warmups; ++w) for (int64_t i = 0; i < k; ++i) observable = fn(left, pairs * coordinates, right, pairs * coordinates, pairs, coordinates);
        begin = now_ns(); for (int64_t i = 0; i < k; ++i) observable = fn(left, pairs * coordinates, right, pairs * coordinates, pairs, coordinates); end = now_ns();
        free(left); free(right);
    } else if (strcmp(workload, "scientific.xsbench.compatible_lookup") == 0
            || strcmp(workload, "scientific.xsbench.compatible_lookup.tiny") == 0
            || strcmp(workload, "scientific.xsbench.compatible_lookup.small") == 0
            || strcmp(workload, "scientific.xsbench.compatible_lookup.medium") == 0) {
        xsbench_fn fn = (xsbench_fn)symbol(handle, exported_symbol);
        static const double data[] = {
            3.0, 5.0, 2.0, 2.0, 2.0, 2.0, 0.6, 0.4, 0.25, 0.75,
            1.0, 0.1, 0.2, 0.3, 0.4,
            2.0, 0.2, 0.3, 0.4, 0.5,
            3.0, 0.3, 0.4, 0.5, 0.6,
            4.0, 0.4, 0.5, 0.6, 0.7,
            5.0, 0.5, 0.6, 0.7, 0.8,
            11.0, 10.1, 10.2, 10.3, 10.4,
            12.0, 10.2, 10.3, 10.4, 10.5,
            13.0, 10.3, 10.4, 10.5, 10.6,
            14.0, 10.4, 10.5, 10.6, 10.7,
            15.0, 10.5, 10.6, 10.7, 10.8,
            21.0, 20.1, 20.2, 20.3, 20.4,
            22.0, 20.2, 20.3, 20.4, 20.5,
            23.0, 20.3, 20.4, 20.5, 20.6,
            24.0, 20.4, 20.5, 20.6, 20.7,
            25.0, 20.5, 20.6, 20.7, 20.8
        };
        static const int64_t metadata_tiny[] = {0, 1, 1, 2, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1};
        static const int64_t metadata_small[] = {0, 1, 1, 2, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 5, 22, 37, 49, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 4};
        static const int64_t metadata_medium[] = {0, 1, 1, 2, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 0, 25, 50, 75, 100, 5, 22, 37, 49, 63, 78, 91, 14, 0, 1, 0, 1, 1, 0, 1, 0, 8};
        const int64_t *metadata = metadata_medium;
        if (strcmp(workload, "scientific.xsbench.compatible_lookup.tiny") == 0) metadata = metadata_tiny;
        else if (strcmp(workload, "scientific.xsbench.compatible_lookup.small") == 0) metadata = metadata_small;
        for (int64_t w = 0; w < warmups; ++w) for (int64_t i = 0; i < k; ++i) observable = fn(data, (int64_t)(sizeof(data) / sizeof(data[0])), metadata, 36);
        begin = now_ns(); for (int64_t i = 0; i < k; ++i) observable = fn(data, (int64_t)(sizeof(data) / sizeof(data[0])), metadata, 36); end = now_ns();
    } else fail("unknown workload");
    dlclose(handle);
    emit_result(workload, variant, k, end - begin, observable, expected);
    return close_enough(observable, expected) ? 0 : 1;
}
