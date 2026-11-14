#!/usr/bin/env python3
"""S3 V7 — Reproducible x86-64 Poisson 2D (32x32..192x192) & AVX2/FMA F64 Benchmark Suite.

Drives S3 compiled shared libraries and GCC -O3 / -O3 -march=native libraries inside a
single pure C11 -O3 CLOCK_MONOTONIC harness with:
  - Alternating paired trials (>=15 trials per grid after warmups)
  - Full statistics: median, IQR, min, max, ratio_vs_gcc
  - CPU model & live /proc/cpuinfo MHz logging per grid
  - Strict FP_REASSOCIATION_DEFAULT=FALSE (primary apples-to-apples baseline vs gcc -O3)
  - Explicit opt-in AVX2/FMA (allow_fp_reassociation=True vs gcc -O3 -mavx2 -mfma -ffast-math)
  - Backend compiler plan metrics (blocks, spills, hot_spills, insns)
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import statistics
import subprocess
import sys
import tempfile
import time
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
BENCH_ROOT = THIS_DIR.parents[1]
WORKSPACE_ROOT = BENCH_ROOT.parent
S3_ROOT = WORKSPACE_ROOT / "S3"
if str(S3_ROOT) not in sys.path:
    sys.path.insert(0, str(S3_ROOT))

from bootstrap.s3.backends.x86_64 import NativeToolchain, X8664Backend
from bootstrap.s3.backends.x86_64.allocation import analyze_allocation
from bootstrap.s3.backends.x86_64.backend import SCIENTIFIC_MAX_INSTRUCTIONS
from bootstrap.s3.backends.x86_64.simd_features import compile_simd_lib, detect_cpu_features
from bootstrap.s3.ffi import build_shared_library
from bootstrap.s3.pipeline import OptimizationLevel, compile_sources
from tools.numerics_oracle_v4_7 import GCC_CSR_JACOBI_C

VECTOR_S3_SRC = """
export fn bench_dot_f64(a: &[f64], b: &[f64], n: i64) -> f64:
    mut i: i64 = 0
    mut acc: f64 = 0.0
    while i < n:
        acc = acc + a[i] * b[i]
        i = i + 1
    return acc

export fn bench_axpy_f64(y: &mut [f64], alpha: f64, x: &[f64], n: i64) -> i64:
    mut i: i64 = 0
    while i < n:
        y[i] = y[i] + alpha * x[i]
        i = i + 1
    return 0

export fn bench_scale_f64(out: &mut [f64], alpha: f64, x: &[f64], n: i64) -> i64:
    mut i: i64 = 0
    while i < n:
        out[i] = alpha * x[i]
        i = i + 1
    return 0

export fn bench_triad_stencil(out: &mut [f64], a: &[f64], b: &[f64], alpha: f64, n: i64) -> i64:
    mut i: i64 = 0
    while i < n:
        out[i] = a[i] + alpha * b[i]
        i = i + 1
    return 0

fn main() -> i64:
    return 0
"""

VECTOR_GCC_C = r"""
#include <stdint.h>

double gcc_bench_dot_f64(const double *a, const double *b, int64_t n) {
    double acc = 0.0;
    for (int64_t i = 0; i < n; i++) {
        acc += a[i] * b[i];
    }
    return acc;
}

int64_t gcc_bench_axpy_f64(double *y, double alpha, const double *x, int64_t n) {
    for (int64_t i = 0; i < n; i++) {
        y[i] = y[i] + alpha * x[i];
    }
    return 0;
}

int64_t gcc_bench_scale_f64(double *out, double alpha, const double *x, int64_t n) {
    for (int64_t i = 0; i < n; i++) {
        out[i] = alpha * x[i];
    }
    return 0;
}

int64_t gcc_bench_triad_stencil(double *out, const double *a, const double *b, double alpha, int64_t n) {
    for (int64_t i = 0; i < n; i++) {
        out[i] = a[i] + alpha * b[i];
    }
    return 0;
}
"""

C_DRIVER_SRC = r"""
#define _POSIX_C_SOURCE 200809L
#include <dlfcn.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static double ns_now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec * 1e9 + (double)ts.tv_nsec;
}

typedef int64_t (*s3_cg_chunk_fn)(
    const int64_t *, int64_t, const int64_t *, int64_t,
    const double *, int64_t, const double *, int64_t, const double *, int64_t,
    double *, int64_t, double *, int64_t, double *, int64_t,
    double *, int64_t, double *, int64_t,
    int64_t, double, int64_t, double *, int64_t);

typedef int64_t (*gcc_cg_fn)(
    const int64_t *, const int64_t *, const double *, const double *, const double *,
    double *, double *, double *, double *, double *,
    int64_t, double, int64_t, double *);

typedef double (*s3_dot_fn)(const double *, int64_t, const double *, int64_t, int64_t);
typedef int64_t (*s3_axpy_fn)(double *, int64_t, double, const double *, int64_t, int64_t);
typedef int64_t (*s3_scale_fn)(double *, int64_t, double, const double *, int64_t, int64_t);
typedef int64_t (*s3_triad_fn)(double *, int64_t, const double *, int64_t, const double *, int64_t, double, int64_t);

typedef double (*c_dot_fn)(const double *, const double *, int64_t);
typedef int64_t (*c_axpy_fn)(double *, double, const double *, int64_t);
typedef int64_t (*c_scale_fn)(double *, double, const double *, int64_t);
typedef int64_t (*c_triad_fn)(double *, const double *, const double *, double, int64_t);

typedef void (*simd_axpy_asm_fn)(double, const double *, double *, int64_t);

static volatile double g_sink_f64 = 0.0;
static volatile int64_t g_sink_i64 = 0;

static void build_poisson2d(
    int64_t grid, int64_t **out_rp, int64_t **out_ci, double **out_vl,
    double **out_dg, double **out_b, double **out_xtrue, int64_t *out_nnz
) {
    int64_t n = grid * grid;
    int64_t cap = 5 * n;
    int64_t *rp = (int64_t *)malloc((size_t)(n + 1) * sizeof(int64_t));
    int64_t *ci = (int64_t *)malloc((size_t)cap * sizeof(int64_t));
    double *vl = (double *)malloc((size_t)cap * sizeof(double));
    double *dg = (double *)malloc((size_t)n * sizeof(double));
    double *b = (double *)malloc((size_t)n * sizeof(double));
    double *xt = (double *)malloc((size_t)n * sizeof(double));

    int64_t k = 0;
    rp[0] = 0;
    for (int64_t r = 0; r < grid; r++) {
        for (int64_t c = 0; c < grid; c++) {
            int64_t idx = r * grid + c;
            if (r > 0) { ci[k] = (r - 1) * grid + c; vl[k++] = -1.0; }
            if (c > 0) { ci[k] = r * grid + (c - 1); vl[k++] = -1.0; }
            ci[k] = idx; vl[k++] = 4.0;
            if (c + 1 < grid) { ci[k] = r * grid + (c + 1); vl[k++] = -1.0; }
            if (r + 1 < grid) { ci[k] = (r + 1) * grid + c; vl[k++] = -1.0; }
            rp[idx + 1] = k;
            dg[idx] = 4.0;
            xt[idx] = 1.0 + (double)idx / (double)(n > 1 ? n - 1 : 1);
        }
    }
    for (int64_t i = 0; i < n; i++) {
        double s = 0.0;
        for (int64_t j = rp[i]; j < rp[i + 1]; j++) {
            s += vl[j] * xt[ci[j]];
        }
        b[i] = s;
    }
    *out_rp = rp; *out_ci = ci; *out_vl = vl; *out_dg = dg;
    *out_b = b; *out_xtrue = xt; *out_nnz = k;
}

static int64_t run_s3_chunked(
    s3_cg_chunk_fn fn, const int64_t *rp, int64_t n_rp, const int64_t *ci, int64_t n_ci,
    const double *vl, const double *dg, const double *b,
    double *x, double *r, double *z, double *p, double *ap,
    int64_t n, double tol2, int64_t chunk_step, double *out_res2
) {
    memset(x, 0, (size_t)n * sizeof(double));
    double state[4] = {0.0, 0.0, 0.0, 0.0};
    int64_t iters = 0;
    while (iters < 5000 && state[3] < 0.5) {
        int64_t step = 5000 - iters;
        if (step > chunk_step) step = chunk_step;
        int64_t rc = fn(
            rp, n_rp, ci, n_ci, vl, n_ci, dg, n, b, n,
            x, n, r, n, z, n, p, n, ap, n,
            n, tol2, step, state, 4);
        if (rc < 0) return -rc - 1;
        iters += rc;
    }
    *out_res2 = state[2];
    return iters;
}

static double read_cpu_mhz(void) {
    FILE *f = fopen("/proc/cpuinfo", "r");
    if (!f) return 0.0;
    char buf[256];
    while (fgets(buf, sizeof(buf), f)) {
        double mhz = 0.0;
        if (sscanf(buf, "cpu MHz : %lf", &mhz) == 1) {
            fclose(f);
            return mhz;
        }
    }
    fclose(f);
    return 0.0;
}

int main(int argc, char **argv) {
    if (argc < 10) {
        fprintf(stderr, "usage: driver <s3_poi.so> <gcc_strict.so> <gcc_native.so> <s3_vec_strict.so> <s3_vec_avx2.so> <vec_gcc_strict.so> <vec_gcc_avx2.so> <simd_asm.so> <trials>\n");
        return 2;
    }
    void *h_s3p = dlopen(argv[1], RTLD_NOW);
    void *h_gs  = dlopen(argv[2], RTLD_NOW);
    void *h_gn  = dlopen(argv[3], RTLD_NOW);
    void *h_vs  = dlopen(argv[4], RTLD_NOW);
    void *h_va  = dlopen(argv[5], RTLD_NOW);
    void *h_vgs = dlopen(argv[6], RTLD_NOW);
    void *h_vga = dlopen(argv[7], RTLD_NOW);
    void *h_asm = dlopen(argv[8], RTLD_NOW);
    int trials = atoi(argv[9]);
    if (!h_s3p || !h_gs || !h_gn || !h_vs || !h_va || !h_vgs || !h_vga || !h_asm) {
        fprintf(stderr, "dlopen error: %s\n", dlerror());
        return 3;
    }

    s3_cg_chunk_fn s3_chunk = (s3_cg_chunk_fn)dlsym(h_s3p, "__s3mod_s3_sci_numerics_v5__cg_solve_csr_jacobi_chunk");
    gcc_cg_fn g_strict = (gcc_cg_fn)dlsym(h_gs, "gcc_cg_solve_csr_jacobi");
    gcc_cg_fn g_native = (gcc_cg_fn)dlsym(h_gn, "gcc_cg_solve_csr_jacobi");

    const int grids[] = {32, 48, 64, 96, 128, 160, 192};
    const int n_grids = 7;
    const double tols[] = {1e-10, 1e-12};

    for (int gi = 0; gi < n_grids; gi++) {
        int64_t g = grids[gi];
        int64_t n = g * g;
        int64_t nnz = 0;
        int64_t *rp = NULL, *ci = NULL;
        double *vl = NULL, *dg = NULL, *b = NULL, *xt = NULL;
        build_poisson2d(g, &rp, &ci, &vl, &dg, &b, &xt, &nnz);

        double *sx = (double *)malloc((size_t)n * sizeof(double));
        double *sr = (double *)malloc((size_t)n * sizeof(double));
        double *sz = (double *)malloc((size_t)n * sizeof(double));
        double *sp = (double *)malloc((size_t)n * sizeof(double));
        double *sap = (double *)malloc((size_t)n * sizeof(double));
        double *gx = (double *)malloc((size_t)n * sizeof(double));
        double *gr = (double *)malloc((size_t)n * sizeof(double));
        double *gz = (double *)malloc((size_t)n * sizeof(double));
        double *gp = (double *)malloc((size_t)n * sizeof(double));
        double *gap = (double *)malloc((size_t)n * sizeof(double));

        // Stay comfortably below 50,000,000 logical S3 instruction cap per chunk call
        int64_t chunk_step = 1200000LL / (5 * n);
        if (chunk_step < 2) chunk_step = 2;
        if (chunk_step > 100) chunk_step = 100;

        for (int ti = 0; ti < 2; ti++) {
            double tol = tols[ti];
            double tol2 = tol * tol;
            double s_res2 = 0.0, g_res2 = 0.0, gn_res2 = 0.0;
            int64_t sit = 0, git = 0, gnit = 0;

            // Warmups
            for (int w = 0; w < 2; w++) {
                sit = run_s3_chunked(s3_chunk, rp, n + 1, ci, nnz, vl, dg, b, sx, sr, sz, sp, sap, n, tol2, chunk_step, &s_res2);
                git = g_strict(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol, 5000, &g_res2);
                gnit = g_native(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol, 5000, &gn_res2);
            }
            if (sit < 0 || sit != git) {
                fprintf(stderr, "iteration/trap mismatch on %ldx%ld tol=%g: sit=%ld git=%ld\n",
                        (long)g, (long)g, tol, (long)sit, (long)git);
                return 4;
            }
            double max_err_gcc = 0.0, max_err_true = 0.0;
            for (int64_t i = 0; i < n; i++) {
                double eg = fabs(sx[i] - gx[i]);
                double et = fabs(sx[i] - xt[i]);
                if (eg > max_err_gcc) max_err_gcc = eg;
                if (et > max_err_true) max_err_true = et;
            }
            double mhz = read_cpu_mhz();
            printf("POISSON|%ldx%ld|%ld|%ld|%.0e|%ld|%ld|%ld|%ld|%.3e|%.3e|%.1f",
                   (long)g, (long)g, (long)n, (long)nnz, tol, (long)chunk_step,
                   (long)sit, (long)git, (long)gnit, max_err_gcc, max_err_true, mhz);

            // Alternating paired timing
            for (int tr = 0; tr < trials; tr++) {
                double t0, t1, ms_s, ms_gs, ms_gn;
                if ((tr & 1) == 0) {
                    t0 = ns_now();
                    sit = run_s3_chunked(s3_chunk, rp, n + 1, ci, nnz, vl, dg, b, sx, sr, sz, sp, sap, n, tol2, chunk_step, &s_res2);
                    t1 = ns_now();
                    ms_s = (t1 - t0) * 1e-6;
                    t0 = ns_now();
                    git = g_strict(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol, 5000, &g_res2);
                    t1 = ns_now();
                    ms_gs = (t1 - t0) * 1e-6;
                } else {
                    t0 = ns_now();
                    git = g_strict(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol, 5000, &g_res2);
                    t1 = ns_now();
                    ms_gs = (t1 - t0) * 1e-6;
                    t0 = ns_now();
                    sit = run_s3_chunked(s3_chunk, rp, n + 1, ci, nnz, vl, dg, b, sx, sr, sz, sp, sap, n, tol2, chunk_step, &s_res2);
                    t1 = ns_now();
                    ms_s = (t1 - t0) * 1e-6;
                }
                t0 = ns_now();
                gnit = g_native(rp, ci, vl, dg, b, gx, gr, gz, gp, gap, n, tol, 5000, &gn_res2);
                t1 = ns_now();
                ms_gn = (t1 - t0) * 1e-6;
                g_sink_f64 += sx[0] + gx[0] + s_res2 + g_res2 + gn_res2;
                g_sink_i64 += sit + git + gnit;
                printf("|%.6f,%.6f,%.6f", ms_s, ms_gs, ms_gn);
            }
            printf("\n");
        }
        free(rp); free(ci); free(vl); free(dg); free(b); free(xt);
        free(sx); free(sr); free(sz); free(sp); free(sap);
        free(gx); free(gr); free(gz); free(gp); free(gap);
    }

    // Vector/Stencil AVX2/F64 benchmarks
    s3_dot_fn   vs_dot   = (s3_dot_fn)dlsym(h_vs, "bench_dot_f64");
    s3_axpy_fn  vs_axpy  = (s3_axpy_fn)dlsym(h_vs, "bench_axpy_f64");
    s3_scale_fn vs_scale = (s3_scale_fn)dlsym(h_vs, "bench_scale_f64");
    s3_triad_fn vs_triad = (s3_triad_fn)dlsym(h_vs, "bench_triad_stencil");

    s3_dot_fn   va_dot   = (s3_dot_fn)dlsym(h_va, "bench_dot_f64");
    s3_axpy_fn  va_axpy  = (s3_axpy_fn)dlsym(h_va, "bench_axpy_f64");
    s3_scale_fn va_scale = (s3_scale_fn)dlsym(h_va, "bench_scale_f64");
    s3_triad_fn va_triad = (s3_triad_fn)dlsym(h_va, "bench_triad_stencil");

    c_dot_fn   vgs_dot   = (c_dot_fn)dlsym(h_vgs, "gcc_bench_dot_f64");
    c_axpy_fn  vgs_axpy  = (c_axpy_fn)dlsym(h_vgs, "gcc_bench_axpy_f64");
    c_scale_fn vgs_scale = (c_scale_fn)dlsym(h_vgs, "gcc_bench_scale_f64");
    c_triad_fn vgs_triad = (c_triad_fn)dlsym(h_vgs, "gcc_bench_triad_stencil");

    c_dot_fn   vga_dot   = (c_dot_fn)dlsym(h_vga, "gcc_bench_dot_f64");
    c_axpy_fn  vga_axpy  = (c_axpy_fn)dlsym(h_vga, "gcc_bench_axpy_f64");
    c_scale_fn vga_scale = (c_scale_fn)dlsym(h_vga, "gcc_bench_scale_f64");
    c_triad_fn vga_triad = (c_triad_fn)dlsym(h_vga, "gcc_bench_triad_stencil");

    c_dot_fn asm_dot = (c_dot_fn)dlsym(h_asm, "s3_simd_dot_f64");
    simd_axpy_asm_fn asm_axpy = (simd_axpy_asm_fn)dlsym(h_asm, "s3_simd_axpy_f64");

    const int64_t vec_ns[] = {4096, 65536};
    for (int vi = 0; vi < 2; vi++) {
        int64_t n = vec_ns[vi];
        double *a = (double *)malloc((size_t)n * sizeof(double));
        double *b = (double *)malloc((size_t)n * sizeof(double));
        double *y = (double *)malloc((size_t)n * sizeof(double));
        double *o = (double *)malloc((size_t)n * sizeof(double));
        for (int64_t i = 0; i < n; i++) {
            a[i] = 1.0 + (double)(i % 97) * 0.01;
            b[i] = 0.5 + (double)(i % 53) * 0.02;
            y[i] = 0.25;
            o[i] = 0.0;
        }
        int reps = (n <= 4096) ? 200 : 25;

        // 1. dot
        printf("VEC|dot_f64|%ld|%d", (long)n, reps);
        for (int tr = 0; tr < trials; tr++) {
            double t0, us_vs, us_va, us_gs, us_ga, us_asm, acc = 0.0;
            t0 = ns_now(); for (int r = 0; r < reps; r++) acc += vs_dot(a, n, b, n, n); us_vs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) acc += va_dot(a, n, b, n, n); us_va = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) acc += vgs_dot(a, b, n); us_gs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) acc += vga_dot(a, b, n); us_ga = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) acc += asm_dot(a, b, n); us_asm = (ns_now() - t0) / 1e3 / reps;
            g_sink_f64 += acc;
            printf("|%.6f,%.6f,%.6f,%.6f,%.6f", us_vs, us_va, us_gs, us_ga, us_asm);
        }
        printf("\n");

        // 2. axpy
        printf("VEC|axpy_f64|%ld|%d", (long)n, reps);
        for (int tr = 0; tr < trials; tr++) {
            double t0, us_vs, us_va, us_gs, us_ga, us_asm;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vs_axpy(y, n, 1.0001, a, n, n); us_vs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += va_axpy(y, n, 1.0001, a, n, n); us_va = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vgs_axpy(y, 1.0001, a, n); us_gs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vga_axpy(y, 1.0001, a, n); us_ga = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) asm_axpy(1.0001, a, y, n); us_asm = (ns_now() - t0) / 1e3 / reps;
            printf("|%.6f,%.6f,%.6f,%.6f,%.6f", us_vs, us_va, us_gs, us_ga, us_asm);
        }
        printf("\n");

        // 3. scale
        printf("VEC|scale_f64|%ld|%d", (long)n, reps);
        for (int tr = 0; tr < trials; tr++) {
            double t0, us_vs, us_va, us_gs, us_ga;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vs_scale(o, n, 2.5, a, n, n); us_vs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += va_scale(o, n, 2.5, a, n, n); us_va = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vgs_scale(o, 2.5, a, n); us_gs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vga_scale(o, 2.5, a, n); us_ga = (ns_now() - t0) / 1e3 / reps;
            printf("|%.6f,%.6f,%.6f,%.6f,0.0", us_vs, us_va, us_gs, us_ga);
        }
        printf("\n");

        // 4. triad
        printf("VEC|triad_f64|%ld|%d", (long)n, reps);
        for (int tr = 0; tr < trials; tr++) {
            double t0, us_vs, us_va, us_gs, us_ga;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vs_triad(o, n, a, n, b, n, 1.5, n); us_vs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += va_triad(o, n, a, n, b, n, 1.5, n); us_va = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vgs_triad(o, a, b, 1.5, n); us_gs = (ns_now() - t0) / 1e3 / reps;
            t0 = ns_now(); for (int r = 0; r < reps; r++) g_sink_i64 += vga_triad(o, a, b, 1.5, n); us_ga = (ns_now() - t0) / 1e3 / reps;
            printf("|%.6f,%.6f,%.6f,%.6f,0.0", us_vs, us_va, us_gs, us_ga);
        }
        printf("\n");

        free(a); free(b); free(y); free(o);
    }
    return 0;
}
"""


def _summary(vals: list[float]) -> dict[str, float]:
    s = sorted(vals)
    q1 = statistics.median(s[: len(s) // 2]) if len(s) >= 4 else s[0]
    q3 = statistics.median(s[(len(s) + 1) // 2 :]) if len(s) >= 4 else s[-1]
    return {
        "median": round(statistics.median(s), 6),
        "iqr": round(q3 - q1, 6),
        "min": round(s[0], 6),
        "max": round(s[-1], 6),
    }


def run_benchmark(*, tag: str, trials: int, out_path: Path) -> dict[str, Any]:
    NativeToolchain.detect()
    feats = detect_cpu_features()
    gcc_ver = subprocess.check_output(["gcc", "--version"], text=True).splitlines()[0]

    with tempfile.TemporaryDirectory(prefix="s3_v7_poi_avx2_") as td:
        td_path = Path(td)
        core_src = (S3_ROOT / "examples/horizons_v3/s3_sci_core.s3").read_text(encoding="utf-8")
        app_src = (S3_ROOT / "examples/horizons_v4/s3_sci_numerics_v5.s3").read_text(encoding="utf-8")

        t0 = time.perf_counter()
        comp = compile_sources(
            {"s3_sci_core.s3": core_src, "s3_sci_numerics_v5.s3": app_src},
            entry_module="s3_sci_numerics_v5",
            optimization=OptimizationLevel.O1,
            allow_fp_reassociation=False,
        )
        _, asm_prog = comp.require_ordinary_artifacts()
        backend = X8664Backend.scientific(max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS)
        hp_prog, hp10_map = backend._apply_hp_passes(asm_prog)
        asm_text = backend._generate_ffi(asm_prog)
        s3_compile_ms = round((time.perf_counter() - t0) * 1000.0, 2)

        fn_stats: dict[str, Any] = {}
        for fn in hp_prog.functions:
            for k in ("csr_matvec_f64", "cg_solve_csr_jacobi", "cg_solve_csr_jacobi_chunk", "vec_dot", "vec_axpy"):
                if fn.name.endswith(k):
                    plan = analyze_allocation(fn, ignore_proven_slice_lengths=True)
                    fn_stats[k] = {
                        "blocks": len(fn.blocks),
                        "vregs": len(fn.all_register_types),
                        "spills": len(plan.stack_resident_registers),
                        "hot_spills": plan.hot_loop_spills,
                        "hot_spill_score": plan.hot_spill_score,
                        "hp10": bool(hp10_map.get(fn.name, False)),
                    }

        s3_s = td_path / "s3_poi.s"
        s3_so = td_path / "libs3_poi.so"
        s3_s.write_text(asm_text, encoding="utf-8")
        subprocess.run(["gcc", "-shared", "-fPIC", "-O2", str(s3_s), "-o", str(s3_so)], check=True)

        gc_p = td_path / "gcc_poi.c"
        gc_strict_so = td_path / "libgcc_strict.so"
        gc_native_so = td_path / "libgcc_native.so"
        gc_p.write_text(GCC_CSR_JACOBI_C, encoding="utf-8")
        subprocess.run(["gcc", "-O3", "-shared", "-fPIC", str(gc_p), "-o", str(gc_strict_so)], check=True)
        subprocess.run(["gcc", "-O3", "-march=native", "-ffast-math", "-shared", "-fPIC", str(gc_p), "-o", str(gc_native_so)], check=True)

        vs_so = build_shared_library(
            VECTOR_S3_SRC,
            td_path / "libs3_vec_strict.so",
            optimization="O1",
            max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS,
            allow_fp_reassociation=False,
            instruction_budget_mode="loop-hybrid",
            selective_hp_cost_model=True,
        )
        va_so = build_shared_library(
            VECTOR_S3_SRC,
            td_path / "libs3_vec_avx2.so",
            optimization="O1",
            max_instructions=SCIENTIFIC_MAX_INSTRUCTIONS,
            allow_fp_reassociation=True,
            instruction_budget_mode="loop-hybrid",
            selective_hp_cost_model=True,
        )

        vg_p = td_path / "vec_gcc.c"
        vg_strict_so = td_path / "libvec_gcc_strict.so"
        vg_avx2_so = td_path / "libvec_gcc_avx2.so"
        vg_p.write_text(VECTOR_GCC_C, encoding="utf-8")
        subprocess.run(["gcc", "-O3", "-shared", "-fPIC", str(vg_p), "-o", str(vg_strict_so)], check=True)
        subprocess.run(["gcc", "-O3", "-mavx2", "-mfma", "-ffast-math", "-shared", "-fPIC", str(vg_p), "-o", str(vg_avx2_so)], check=True)

        asm_so, _, simd_isa = compile_simd_lib(td_path / "libsimd_asm.so", prefer_avx2=True)

        drv_c = td_path / "driver.c"
        drv_bin = td_path / "driver"
        drv_c.write_text(C_DRIVER_SRC, encoding="utf-8")
        subprocess.run(["gcc", "-O3", str(drv_c), "-o", str(drv_bin), "-ldl", "-lm"], check=True)

        out = subprocess.check_output(
            [
                str(drv_bin),
                str(s3_so),
                str(gc_strict_so),
                str(gc_native_so),
                str(vs_so),
                str(va_so),
                str(vg_strict_so),
                str(vg_avx2_so),
                str(asm_so),
                str(trials),
            ],
            text=True,
        )

    poisson_rows: list[dict[str, Any]] = []
    vec_rows: list[dict[str, Any]] = []
    for line in out.strip().splitlines():
        parts = line.split("|")
        if parts[0] == "POISSON":
            grid, n, nnz, tol, chunk, sit, git, gnit = parts[1:9]
            err_g, err_t, mhz = float(parts[9]), float(parts[10]), float(parts[11])
            s3_ts, gs_ts, gn_ts = [], [], []
            for blk in parts[12:]:
                a, b, c = (float(x) for x in blk.split(","))
                s3_ts.append(a)
                gs_ts.append(b)
                gn_ts.append(c)
            ss, gss, gns = _summary(s3_ts), _summary(gs_ts), _summary(gn_ts)
            poisson_rows.append({
                "grid": grid,
                "n_unknowns": int(n),
                "nnz": int(nnz),
                "tolerance": tol,
                "chunk_step": int(chunk),
                "s3_iters": int(sit),
                "gcc_strict_iters": int(git),
                "gcc_native_iters": int(gnit),
                "max_abs_err_vs_gcc": err_g,
                "max_abs_err_vs_true": err_t,
                "cpu_mhz_observed": mhz,
                "s3_ms": ss,
                "gcc_o3_strict_ms": gss,
                "gcc_o3_native_fastmath_ms": gns,
                "ratio_s3_over_gcc_strict": round(ss["median"] / gss["median"], 3),
                "ratio_s3_over_gcc_native": round(ss["median"] / gns["median"], 3),
            })
        elif parts[0] == "VEC":
            kernel, n, reps = parts[1], int(parts[2]), int(parts[3])
            vs_l, va_l, gs_l, ga_l, asm_l = [], [], [], [], []
            for blk in parts[4:]:
                a, b, c, d, e = (float(x) for x in blk.split(","))
                vs_l.append(a); va_l.append(b); gs_l.append(c); ga_l.append(d); asm_l.append(e)
            vec_rows.append({
                "kernel": kernel,
                "n": n,
                "reps": reps,
                "s3_strict_us": _summary(vs_l),
                "s3_avx2_reassoc_us": _summary(va_l),
                "gcc_o3_strict_us": _summary(gs_l),
                "gcc_o3_avx2_fma_fast_us": _summary(ga_l),
                "s3_simd_asm_us": _summary(asm_l) if any(x > 0 for x in asm_l) else None,
            })

    payload = {
        "benchmark": "S3_V7_POISSON_AND_AVX2_REPRODUCIBILITY",
        "tag": tag,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "platform": platform.platform(),
            "gcc": gcc_ver,
            "cpu_features": feats,
            "simd_features_selected_isa": simd_isa,
        },
        "trials_per_grid": trials,
        "s3_compile_ms": s3_compile_ms,
        "compiler_fn_stats": fn_stats,
        "poisson_2d_cg_jacobi": poisson_rows,
        "vector_f64_kernels": vec_rows,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="v7_run")
    ap.add_argument("--trials", type=int, default=15)
    ap.add_argument("--out", type=Path, default=THIS_DIR / "results_v7_poisson_avx2.json")
    args = ap.parse_args()
    res = run_benchmark(tag=args.tag, trials=args.trials, out_path=args.out)
    for row in res["poisson_2d_cg_jacobi"]:
        print(
            f"{row['grid']} tol={row['tolerance']}: "
            f"S3={row['s3_ms']['median']:.3f}ms (IQR={row['s3_ms']['iqr']:.3f}) vs "
            f"GCC-O3={row['gcc_o3_strict_ms']['median']:.3f}ms -> ratio={row['ratio_s3_over_gcc_strict']:.3f}x "
            f"(GCC-native={row['gcc_o3_native_fastmath_ms']['median']:.3f}ms, ratio={row['ratio_s3_over_gcc_native']:.3f}x)"
        )
    for vr in res["vector_f64_kernels"]:
        if vr["n"] == 65536:
            print(
                f"VEC {vr['kernel']} n={vr['n']}: S3_strict={vr['s3_strict_us']['median']:.2f}us "
                f"S3_avx2={vr['s3_avx2_reassoc_us']['median']:.2f}us "
                f"GCC_strict={vr['gcc_o3_strict_us']['median']:.2f}us "
                f"GCC_avx2={vr['gcc_o3_avx2_fma_fast_us']['median']:.2f}us"
            )


if __name__ == "__main__":
    main()
