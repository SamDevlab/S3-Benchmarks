#include <math.h>
#include <stdint.h>

int64_t c_diffuse_1d_ftcs(
    double *cur, double *nxt, int64_t n,
    double alpha, double dt, double dx,
    double t_left, double t_right, int64_t steps
) {
    double r = alpha * dt / (dx * dx);
    if (r > 0.5) return 4;
    for (int64_t s = 0; s < steps; ++s) {
        nxt[0] = t_left;
        nxt[n - 1] = t_right;
        for (int64_t i = 1; i < n - 1; ++i) {
            nxt[i] = cur[i] + r * (cur[i - 1] - 2.0 * cur[i] + cur[i + 1]);
        }
        for (int64_t i = 0; i < n; ++i) {
            cur[i] = nxt[i];
        }
    }
    return 0;
}

int64_t c_diffuse_1d_crank_nicolson(
    double *cur, double *a, double *b, double *c, double *d,
    double *cp, double *dp, double *sol, int64_t n,
    double alpha, double dt, double dx,
    double t_left, double t_right, int64_t steps
) {
    double r = alpha * dt / (dx * dx);
    double half_r = 0.5 * r;
    int64_t interior = n - 2;
    for (int64_t k = 0; k < interior; ++k) {
        a[k] = -half_r;
        b[k] = 1.0 + r;
        c[k] = -half_r;
    }
    a[0] = 0.0;
    c[interior - 1] = 0.0;

    for (int64_t s = 0; s < steps; ++s) {
        for (int64_t idx = 0; idx < interior; ++idx) {
            int64_t g = idx + 1;
            double rhs = half_r * cur[g - 1] + (1.0 - r) * cur[g] + half_r * cur[g + 1];
            if (idx == 0) rhs += half_r * t_left;
            if (idx == interior - 1) rhs += half_r * t_right;
            d[idx] = rhs;
        }
        cp[0] = c[0] / b[0];
        dp[0] = d[0] / b[0];
        for (int64_t i = 1; i < interior; ++i) {
            double denom = b[i] - a[i] * cp[i - 1];
            cp[i] = c[i] / denom;
            dp[i] = (d[i] - a[i] * dp[i - 1]) / denom;
        }
        sol[interior - 1] = dp[interior - 1];
        for (int64_t j = interior - 2; j >= 0; --j) {
            sol[j] = dp[j] - cp[j] * sol[j + 1];
        }
        cur[0] = t_left;
        cur[n - 1] = t_right;
        for (int64_t w = 0; w < interior; ++w) {
            cur[w + 1] = sol[w];
        }
    }
    return 0;
}

int64_t c_mechanics_2dof_verlet(
    double x1_0, double v1_0, double x2_0, double v2_0,
    double m1, double m2, double k1, double k2, double k3,
    double dt, int64_t steps,
    double *out_x1, double *out_v1, double *out_x2, double *out_v2, double *out_e
) {
    double x1 = x1_0, v1 = v1_0, x2 = x2_0, v2 = v2_0;
    double half_dt2 = 0.5 * dt * dt;
    out_x1[0] = x1; out_v1[0] = v1; out_x2[0] = x2; out_v2[0] = v2;
    out_e[0] = 0.5*(m1*v1*v1 + m2*v2*v2) + 0.5*(k1*x1*x1 + k2*(x2-x1)*(x2-x1) + k3*x2*x2);
    for (int64_t i = 0; i < steps; ++i) {
        double a1_0 = (-(k1 + k2) * x1 + k2 * x2) / m1;
        double a2_0 = (k2 * x1 - (k2 + k3) * x2) / m2;
        double x1_n = x1 + v1 * dt + a1_0 * half_dt2;
        double x2_n = x2 + v2 * dt + a2_0 * half_dt2;
        double a1_1 = (-(k1 + k2) * x1_n + k2 * x2_n) / m1;
        double a2_1 = (k2 * x1_n - (k2 + k3) * x2_n) / m2;
        x1 = x1_n;
        v1 = v1 + 0.5 * (a1_0 + a1_1) * dt;
        x2 = x2_n;
        v2 = v2 + 0.5 * (a2_0 + a2_1) * dt;
        out_x1[i + 1] = x1; out_v1[i + 1] = v1; out_x2[i + 1] = x2; out_v2[i + 1] = v2;
        out_e[i + 1] = 0.5*(m1*v1*v1 + m2*v2*v2) + 0.5*(k1*x1*x1 + k2*(x2-x1)*(x2-x1) + k3*x2*x2);
    }
    return 0;
}
