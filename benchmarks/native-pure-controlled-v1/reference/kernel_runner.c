#define _GNU_SOURCE
#include <dlfcn.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <time.h>

enum { N = 364, COORDS = 363 };
typedef struct {
    char magic[8];
    uint32_t n, reserved;
    double actual[N], load[N], values[N];
    int64_t valid_mask[N];
    double coordinates[COORDS];
    double threshold, capacity;
} Fixture;

typedef int64_t (*energy_residual_fn)(const double *, int64_t, const double *, int64_t,
                                      int64_t, double *, int64_t);
typedef int64_t (*point_bounds_fn)(const double *, int64_t, int64_t, double *, int64_t);
typedef int64_t (*threshold_count_fn)(const double *, int64_t, const int64_t *, int64_t,
                                      int64_t, double, int64_t *, int64_t);
typedef int64_t (*valid_mean_fn)(const double *, int64_t, const int64_t *, int64_t,
                                 int64_t, double *, int64_t);
typedef int64_t (*energy_series_fn)(const double *, int64_t, const double *, int64_t,
                                    double, double *, int64_t);
typedef int64_t (*point_cloud_fn)(const double *, int64_t, int64_t, double *, int64_t);

static uint64_t now_ns(void) {
    struct timespec ts;
    if (clock_gettime(CLOCK_MONOTONIC_RAW, &ts) != 0) { perror("clock_gettime"); exit(3); }
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + (uint64_t)ts.tv_nsec;
}

static void *load_symbol(void *handle, const char *symbol) {
    dlerror();
    void *value = dlsym(handle, symbol);
    const char *error = dlerror();
    if (error != NULL) { fprintf(stderr, "dlsym %s: %s\n", symbol, error); exit(4); }
    return value;
}

int main(int argc, char **argv) {
    if (argc != 6) {
        fprintf(stderr, "usage: kernel_runner LIB WORKLOAD FIXTURE ITERATIONS SIZE\n");
        return 2;
    }
    char *end = NULL;
    const unsigned long long iterations = strtoull(argv[4], &end, 10);
    if (end == argv[4] || *end != '\0') return 2;
    int64_t data_count = 0, point_count = 0;
    if (strcmp(argv[5], "small") == 0) { data_count = 32; point_count = 16; }
    else if (strcmp(argv[5], "medium") == 0) { data_count = 128; point_count = 64; }
    else if (strcmp(argv[5], "full") == 0) { data_count = 364; point_count = 121; }
    else { fprintf(stderr, "unknown size: %s\n", argv[5]); return 2; }
    FILE *file = fopen(argv[3], "rb");
    if (file == NULL) { perror("fopen fixture"); return 2; }
    Fixture fixture;
    const size_t bytes = fread(&fixture, 1, sizeof(fixture), file);
    const int extra = fgetc(file);
    fclose(file);
    if (bytes != sizeof(fixture) || extra != EOF || memcmp(fixture.magic, "S3NPV1\0\0", 8) != 0 || fixture.n != N) {
        fprintf(stderr, "invalid fixture size/header: %zu\n", bytes); return 2;
    }

    void *handle = dlopen(argv[1], RTLD_NOW | RTLD_LOCAL);
    if (handle == NULL) { fprintf(stderr, "dlopen: %s\n", dlerror()); return 2; }
    const char *workload = argv[2];
    double dout[10] = {0};
    int64_t iout[1] = {0};
    int64_t status = -99;
    int output_count = 0;
    if (strcmp(workload, "agent_energy_residual") == 0) {
        energy_residual_fn fn = (energy_residual_fn)load_symbol(handle, workload);
        status = fn(fixture.actual, data_count, fixture.load, data_count, data_count, dout, 3); output_count = 3;
        if (status != 0) return 5;
        const uint64_t start = now_ns();
        for (unsigned long long i = 0; i < iterations; ++i) status = fn(fixture.actual, data_count, fixture.load, data_count, data_count, dout, 3);
        const uint64_t elapsed = now_ns() - start;
        if (status != 0) return 5;
        printf("{\"status\":%" PRId64 ",\"iterations\":%llu,\"elapsed_ns\":%" PRIu64 ",\"ns_per_call\":%.9f,\"checksum\":%.17g,\"outputs\":[", status, iterations, elapsed, iterations ? (double)elapsed / (double)iterations : 0.0, dout[0] + dout[1] + dout[2]);
        for (int i = 0; i < output_count; ++i) printf("%s%.17g", i ? "," : "", dout[i]);
    } else if (strcmp(workload, "agent_point_bounds") == 0) {
        point_bounds_fn fn = (point_bounds_fn)load_symbol(handle, workload);
        status = fn(fixture.coordinates, point_count * 3, point_count, dout, 6); output_count = 6;
        if (status != 0) return 5;
        const uint64_t start = now_ns();
        for (unsigned long long i = 0; i < iterations; ++i) status = fn(fixture.coordinates, point_count * 3, point_count, dout, 6);
        const uint64_t elapsed = now_ns() - start;
        if (status != 0) return 5;
        double checksum = 0.0; for (int i = 0; i < output_count; ++i) checksum += dout[i];
        printf("{\"status\":%" PRId64 ",\"iterations\":%llu,\"elapsed_ns\":%" PRIu64 ",\"ns_per_call\":%.9f,\"checksum\":%.17g,\"outputs\":[", status, iterations, elapsed, iterations ? (double)elapsed / (double)iterations : 0.0, checksum);
        for (int i = 0; i < output_count; ++i) printf("%s%.17g", i ? "," : "", dout[i]);
    } else if (strcmp(workload, "agent_raster_threshold_count") == 0) {
        threshold_count_fn fn = (threshold_count_fn)load_symbol(handle, workload);
        status = fn(fixture.values, data_count, fixture.valid_mask, data_count, data_count, fixture.threshold, iout, 1); output_count = 1;
        if (status != 0) return 5;
        const uint64_t start = now_ns();
        for (unsigned long long i = 0; i < iterations; ++i) status = fn(fixture.values, data_count, fixture.valid_mask, data_count, data_count, fixture.threshold, iout, 1);
        const uint64_t elapsed = now_ns() - start;
        if (status != 0) return 5;
        printf("{\"status\":%" PRId64 ",\"iterations\":%llu,\"elapsed_ns\":%" PRIu64 ",\"ns_per_call\":%.9f,\"checksum\":%" PRId64 ",\"outputs\":[%" PRId64, status, iterations, elapsed, iterations ? (double)elapsed / (double)iterations : 0.0, iout[0], iout[0]);
    } else if (strcmp(workload, "agent_raster_valid_mean") == 0) {
        valid_mean_fn fn = (valid_mean_fn)load_symbol(handle, workload);
        status = fn(fixture.values, data_count, fixture.valid_mask, data_count, data_count, dout, 1); output_count = 1;
        if (status != 0) return 5;
        const uint64_t start = now_ns();
        for (unsigned long long i = 0; i < iterations; ++i) status = fn(fixture.values, data_count, fixture.valid_mask, data_count, data_count, dout, 1);
        const uint64_t elapsed = now_ns() - start;
        if (status != 0) return 5;
        printf("{\"status\":%" PRId64 ",\"iterations\":%llu,\"elapsed_ns\":%" PRIu64 ",\"ns_per_call\":%.9f,\"checksum\":%.17g,\"outputs\":[%.17g", status, iterations, elapsed, iterations ? (double)elapsed / (double)iterations : 0.0, dout[0], dout[0]);
    } else if (strcmp(workload, "energy_series_aggregation") == 0) {
        energy_series_fn fn = (energy_series_fn)load_symbol(handle, workload);
        status = fn(fixture.actual, data_count, fixture.load, data_count, fixture.capacity, dout, 5); output_count = 5;
        if (status != 0) return 5;
        const uint64_t start = now_ns();
        for (unsigned long long i = 0; i < iterations; ++i) status = fn(fixture.actual, data_count, fixture.load, data_count, fixture.capacity, dout, 5);
        const uint64_t elapsed = now_ns() - start;
        if (status != 0) return 5;
        double checksum = 0.0; for (int i = 0; i < output_count; ++i) checksum += dout[i];
        printf("{\"status\":%" PRId64 ",\"iterations\":%llu,\"elapsed_ns\":%" PRIu64 ",\"ns_per_call\":%.9f,\"checksum\":%.17g,\"outputs\":[", status, iterations, elapsed, iterations ? (double)elapsed / (double)iterations : 0.0, checksum);
        for (int i = 0; i < output_count; ++i) printf("%s%.17g", i ? "," : "", dout[i]);
    } else if (strcmp(workload, "point_cloud_summary") == 0) {
        point_cloud_fn fn = (point_cloud_fn)load_symbol(handle, workload);
        status = fn(fixture.coordinates, point_count * 3, point_count, dout, 10); output_count = 10;
        if (status != 0) return 5;
        const uint64_t start = now_ns();
        for (unsigned long long i = 0; i < iterations; ++i) status = fn(fixture.coordinates, point_count * 3, point_count, dout, 10);
        const uint64_t elapsed = now_ns() - start;
        if (status != 0) return 5;
        double checksum = 0.0; for (int i = 0; i < output_count; ++i) checksum += dout[i];
        printf("{\"status\":%" PRId64 ",\"iterations\":%llu,\"elapsed_ns\":%" PRIu64 ",\"ns_per_call\":%.9f,\"checksum\":%.17g,\"outputs\":[", status, iterations, elapsed, iterations ? (double)elapsed / (double)iterations : 0.0, checksum);
        for (int i = 0; i < output_count; ++i) printf("%s%.17g", i ? "," : "", dout[i]);
    } else {
        fprintf(stderr, "unknown workload: %s\n", workload); return 2;
    }
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    printf("],\"maxrss_kib\":%ld}\n", usage.ru_maxrss);
    dlclose(handle);
    return 0;
}
