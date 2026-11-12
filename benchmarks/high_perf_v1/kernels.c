#include <stdint.h>
#include <math.h>

#ifdef WITH_CHECKS
#define CHECK_BOUNDS(idx, len) do { if ((uint64_t)(idx) >= (uint64_t)(len)) return -1; } while (0)
#else
#define CHECK_BOUNDS(idx, len) do { (void)(idx); (void)(len); } while (0)
#endif

int64_t dot_i64(const int64_t *a, int64_t a_len, const int64_t *b, int64_t b_len, int64_t n) {
    int64_t acc = 0;
    for (int64_t i = 0; i < n; ++i) {
        CHECK_BOUNDS(i, a_len);
        CHECK_BOUNDS(i, b_len);
        acc += a[i] * b[i];
    }
    return acc;
}

int64_t axpy_f64(double a, const double *x, int64_t x_len, double *y, int64_t y_len, int64_t n) {
    for (int64_t i = 0; i < n; ++i) {
        CHECK_BOUNDS(i, x_len);
        CHECK_BOUNDS(i, y_len);
        y[i] = a * x[i] + y[i];
    }
    return 0;
}

int64_t stencil_1d_f64(const double *u_in, int64_t u_len, double *buf_a, int64_t a_len, double *buf_b, int64_t b_len, int64_t n, int64_t steps, double alpha) {
    for (int64_t i = 0; i < n; ++i) {
        CHECK_BOUNDS(i, u_len);
        CHECK_BOUNDS(i, a_len);
        CHECK_BOUNDS(i, b_len);
        buf_a[i] = u_in[i];
        buf_b[i] = u_in[i];
    }
    for (int64_t s = 0; s < steps; ++s) {
        for (int64_t i = 1; i < n - 1; ++i) {
            CHECK_BOUNDS(i - 1, a_len);
            CHECK_BOUNDS(i, a_len);
            CHECK_BOUNDS(i + 1, a_len);
            CHECK_BOUNDS(i, b_len);
            buf_b[i] = buf_a[i] + alpha * (buf_a[i - 1] - 2.0 * buf_a[i] + buf_a[i + 1]);
        }
        for (int64_t i = 1; i < n - 1; ++i) {
            CHECK_BOUNDS(i, b_len);
            CHECK_BOUNDS(i, a_len);
            buf_a[i] = buf_b[i];
        }
    }
    return 0;
}

int64_t stencil_2d_f64(double *a, int64_t a_len, double *b, int64_t b_len, int64_t rows, int64_t cols, int64_t steps, double alpha) {
    for (int64_t s = 0; s < steps; ++s) {
        for (int64_t r = 1; r < rows - 1; ++r) {
            for (int64_t c = 1; c < cols - 1; ++c) {
                int64_t idx = r * cols + c;
                CHECK_BOUNDS(idx, a_len);
                CHECK_BOUNDS(idx - 1, a_len);
                CHECK_BOUNDS(idx + 1, a_len);
                CHECK_BOUNDS(idx - cols, a_len);
                CHECK_BOUNDS(idx + cols, a_len);
                CHECK_BOUNDS(idx, b_len);
                b[idx] = a[idx] + alpha * (a[idx - 1] + a[idx + 1] + a[idx - cols] + a[idx + cols] - 4.0 * a[idx]);
            }
        }
        for (int64_t r = 1; r < rows - 1; ++r) {
            for (int64_t c = 1; c < cols - 1; ++c) {
                int64_t idx = r * cols + c;
                CHECK_BOUNDS(idx, b_len);
                CHECK_BOUNDS(idx, a_len);
                a[idx] = b[idx];
            }
        }
    }
    return 0;
}

int64_t matmul_f64(const double *a, int64_t a_len, const double *b, int64_t b_len, double *c, int64_t c_len, int64_t n) {
    for (int64_t i = 0; i < n; ++i) {
        for (int64_t j = 0; j < n; ++j) {
            double acc = 0.0;
            for (int64_t k = 0; k < n; ++k) {
                CHECK_BOUNDS(i * n + k, a_len);
                CHECK_BOUNDS(k * n + j, b_len);
                acc += a[i * n + k] * b[k * n + j];
            }
            CHECK_BOUNDS(i * n + j, c_len);
            c[i * n + j] = acc;
        }
    }
    return 0;
}

int64_t thomas_f64(const double *a, int64_t a_len, const double *b, int64_t b_len, const double *c, int64_t c_len, const double *d, int64_t d_len, double *cp, int64_t cp_len, double *dp, int64_t dp_len, double *x, int64_t x_len, int64_t n) {
    CHECK_BOUNDS(0, c_len); CHECK_BOUNDS(0, b_len); CHECK_BOUNDS(0, cp_len);
    CHECK_BOUNDS(0, d_len); CHECK_BOUNDS(0, dp_len);
    cp[0] = c[0] / b[0];
    dp[0] = d[0] / b[0];
    for (int64_t i = 1; i < n; ++i) {
        CHECK_BOUNDS(i, b_len); CHECK_BOUNDS(i, a_len); CHECK_BOUNDS(i - 1, cp_len);
        CHECK_BOUNDS(i, c_len); CHECK_BOUNDS(i, cp_len);
        CHECK_BOUNDS(i, d_len); CHECK_BOUNDS(i - 1, dp_len); CHECK_BOUNDS(i, dp_len);
        double denom = b[i] - a[i] * cp[i - 1];
        cp[i] = c[i] / denom;
        dp[i] = (d[i] - a[i] * dp[i - 1]) / denom;
    }
    CHECK_BOUNDS(n - 1, dp_len); CHECK_BOUNDS(n - 1, x_len);
    x[n - 1] = dp[n - 1];
    for (int64_t i = n - 2; i >= 0; --i) {
        CHECK_BOUNDS(i, dp_len); CHECK_BOUNDS(i, cp_len); CHECK_BOUNDS(i + 1, x_len); CHECK_BOUNDS(i, x_len);
        x[i] = dp[i] - cp[i] * x[i + 1];
    }
    return 0;
}

double rk4_osc_f64(double x0, double v0, double k, double dt, int64_t steps) {
    double x = x0;
    double v = v0;
    for (int64_t i = 0; i < steps; ++i) {
        double k1x = v;
        double k1v = -k * x;
        double k2x = v + 0.5 * dt * k1v;
        double k2v = -k * (x + 0.5 * dt * k1x);
        double k3x = v + 0.5 * dt * k2v;
        double k3v = -k * (x + 0.5 * dt * k2x);
        double k4x = v + dt * k3v;
        double k4v = -k * (x + dt * k3x);
        x += (dt / 6.0) * (k1x + 2.0 * k2x + 2.0 * k3x + k4x);
        v += (dt / 6.0) * (k1v + 2.0 * k2v + 2.0 * k3v + k4v);
    }
    return x;
}

double verlet_osc_f64(double x0, double v0, double k, double dt, int64_t steps) {
    double x = x0;
    double v = v0;
    double a = -k * x;
    for (int64_t i = 0; i < steps; ++i) {
        double x_next = x + v * dt + 0.5 * a * dt * dt;
        double a_next = -k * x_next;
        v += 0.5 * (a + a_next) * dt;
        x = x_next;
        a = a_next;
    }
    return x;
}
