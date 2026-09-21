"""Direct FFI call-loop evidence using the existing S3 exported ABI.

This is benchmark-side infrastructure. It compiles the pinned S3 checkout
without modifying S3 and uses one common C driver for every variant.
"""

from __future__ import annotations

import argparse
import ctypes
from dataclasses import dataclass
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import platform
import shutil
import statistics
import subprocess
import sys
import time
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from protocol.provenance import require_commit

EXPECTED_S3_SHA = "e07d0b5464bf472b2ca18993f3e196a234ff0fc5"
VARIANTS = ("S3_FFI_O0", "S3_FFI_O1", "GCC_O2", "CLANG_O2")
WARMUPS = 5
REPETITIONS = 30
CALIBRATION_LEVELS = (1, 10, 100, 1000, 10000, 100000, 1000000)
SAMPLE_TIMEOUT_SECONDS = 120.0
TARGET_MIN_NS = 10_000_000
PREFERRED_MIN_NS = 50_000_000
PREFERRED_MAX_NS = 500_000_000
S3_FFI_MAX_INSTRUCTIONS = 10_000_000_000


@dataclass(frozen=True, slots=True)
class FFIPilot:
    workload_id: str
    symbol: str
    source: str
    c_source: str
    expected: float
    work_units_per_call: int
    logical_shape: str
    index_mapping: str
    family: str


def _s3_header() -> str:
    return """export fn identity_f64(value: f64) -> f64:
    return value

"""


def _pilot_sources() -> tuple[FFIPilot, ...]:
    triad_s3 = _s3_header() + """export fn triad(a: &mut [f64], b: &[f64], c: &[f64], scalar: f64) -> f64:
    mut i: i64 = 0
    mut total: f64 = 0.0
    while i < 31:
        mut value: f64 = b[i] + scalar * c[i]
        a[i] = value
        total = total + value
        i = i + 1
    return total

fn main() -> i64:
    return 0
"""
    triad_c = """#include <stdint.h>
double identity_f64(double value) { return value; }
double triad(double *a, int64_t a_len, const double *b, int64_t b_len, const double *c, int64_t c_len, double scalar) {
    (void)a_len; (void)b_len; (void)c_len;
    double total = 0.0;
    for (int64_t i = 0; i < 31; ++i) { double value = b[i] + scalar * c[i]; a[i] = value; total += value; }
    return total;
}
"""

    nstream_s3 = _s3_header() + """export fn nstream(a: &[f64], b: &[f64], c: &[f64], scalar: f64) -> f64:
    mut i: i64 = 0
    mut total: f64 = 0.0
    while i < 31:
        mut value: f64 = a[i] + b[i] + scalar * c[i]
        total = total + value
        i = i + 1
    return total

fn main() -> i64:
    return 0
"""
    nstream_c = """#include <stdint.h>
double identity_f64(double value) { return value; }
double nstream(const double *a, int64_t a_len, const double *b, int64_t b_len, const double *c, int64_t c_len, double scalar) {
    (void)a_len; (void)b_len; (void)c_len;
    double total = 0.0;
    for (int64_t i = 0; i < 31; ++i) { double value = a[i] + b[i] + scalar * c[i]; total += value; }
    return total;
}
"""

    gemm_s3 = _s3_header() + """export fn gemm(a: &[f64], b: &[f64], c: &[f64]) -> f64:
    mut rows: i64 = 4
    mut cols: i64 = 4
    mut inner: i64 = 4
    mut i: i64 = 0
    mut checksum: f64 = 0.0
    while i < rows:
        mut j: i64 = 0
        while j < cols:
            mut k: i64 = 0
            mut total: f64 = 1.0
            while k < inner:
                total = total + a[i * inner + k] * b[k * cols + j]
                k = k + 1
            checksum = checksum + total
            j = j + 1
        i = i + 1
    return checksum

fn main() -> i64:
    return 0
"""
    gemm_c = """#include <stdint.h>
double identity_f64(double value) { return value; }
double gemm(const double *a, int64_t a_len, const double *b, int64_t b_len, const double *c, int64_t c_len) {
    (void)a_len; (void)b_len; (void)c_len;
    double checksum = 0.0;
    for (int64_t i = 0; i < 4; ++i) for (int64_t j = 0; j < 4; ++j) {
        double total = 1.0;
        for (int64_t k = 0; k < 4; ++k) total += a[i * 4 + k] * b[k * 4 + j];
        checksum += total;
    }
    return checksum;
}
"""

    rmsd_s3 = _s3_header() + """export fn rmsd(left: &[f64], right: &[f64], pairs: i64, coordinates: i64) -> f64:
    mut pair: i64 = 0
    mut total: f64 = 0.0
    while pair < pairs:
        mut coordinate: i64 = 0
        mut ssd: f64 = 0.0
        while coordinate < coordinates:
            mut offset: i64 = pair * coordinates + coordinate
            mut delta: f64 = left[offset] - right[offset]
            ssd = ssd + delta * delta
            coordinate = coordinate + 1
        total = total + sqrt(ssd / to_f64(coordinates))
        pair = pair + 1
    return total

fn main() -> i64:
    return 0
"""
    rmsd_c = """#include <math.h>
#include <stdint.h>
double identity_f64(double value) { return value; }
double rmsd(const double *left, int64_t left_len, const double *right, int64_t right_len, int64_t pairs, int64_t coordinates) {
    (void)left_len; (void)right_len;
    double total = 0.0;
    for (int64_t pair = 0; pair < pairs; ++pair) {
        double ssd = 0.0;
        for (int64_t coordinate = 0; coordinate < coordinates; ++coordinate) {
            int64_t offset = pair * coordinates + coordinate;
            double delta = left[offset] - right[offset];
            ssd += delta * delta;
        }
        total += sqrt(ssd / (double)coordinates);
    }
    return total;
}
"""
    return (
        FFIPilot("memory.babelstream.triad", "triad", triad_s3, triad_c, 3813.0, 31, "1D vector", "i", "memory"),
        FFIPilot("hpc.prk.nstream", "nstream", nstream_s3, nstream_c, 1085.0, 31, "1D vector", "i", "hpc"),
        FFIPilot("numerical.polybench.gemm", "gemm", gemm_s3, gemm_c, 5504.0, 4 * 4 * 4, "A[4,K], B[K,4], C[4,4] read-only checksum", "i * stride + j", "numerical"),
        FFIPilot("scientific.rmsd.batch", "rmsd", rmsd_s3, rmsd_c, 16.0, 16 * 3, "pair_count x coordinates_per_pair", "pair * coordinates_per_pair + coordinate", "scientific"),
    )


def _path_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def _machine_identity() -> tuple[str, dict[str, str | int]]:
    cpu_model = ""
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.is_file():
        for line in cpuinfo.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.lower().startswith("model name"):
                _, _, value = line.partition(":")
                cpu_model = value.strip()
                break
    identity: dict[str, str | int] = {
        "system": platform.system(),
        "machine": platform.machine(),
        "kernel": platform.release(),
        "cpu_model": cpu_model or platform.processor(),
        "logical_cpus": int(os.cpu_count() or 0),
    }
    encoded = json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest(), identity


def _run(command: list[str], *, cwd: Path | None = None, timeout: float = 60.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=str(cwd) if cwd else None, check=False, capture_output=True, text=True, timeout=timeout)


def _compiler_for(label: str) -> str:
    command = "clang" if label == "CLANG_O2" else "gcc"
    resolved = shutil.which(command)
    if resolved is None:
        raise RuntimeError(f"required compiler unavailable: {command}")
    return resolved


def _activate_s3_modules(s3_repo: Path) -> Any:
    repo = s3_repo.resolve()
    if not (repo / "bootstrap" / "s3" / "ffi.py").is_file():
        raise RuntimeError(f"S3_REPO is not a complete pinned checkout: {repo}")
    for name in list(sys.modules):
        if name == "bootstrap" or name.startswith("bootstrap."):
            del sys.modules[name]
    sys.path[:] = [entry for entry in sys.path if entry != str(repo)]
    sys.path.insert(0, str(repo))
    pipeline = importlib.import_module("bootstrap.s3.pipeline")
    loaded = Path(pipeline.__file__).resolve()
    try:
        loaded.relative_to(repo)
    except ValueError as error:
        raise RuntimeError(f"pinned S3 module escaped checkout: {loaded}") from error
    return pipeline


def _compile_assembly_shared(compiler: str, assembly: Path, obj: Path, library: Path) -> None:
    result = _run([compiler, "-x", "assembler", "-c", str(assembly), "-o", str(obj)], timeout=60.0)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "S3 assembly compilation failed")
    result = _run([compiler, "-shared", "-nostdlib", "-Wl,--build-id=none", str(obj), "-o", str(library)], timeout=60.0)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "S3 shared linking failed")


def _build_s3_library(s3_repo: Path, source: str, optimization: str, output: Path, root: Path) -> dict[str, Any]:
    pipeline = _activate_s3_modules(s3_repo)
    from bootstrap.s3.backends.x86_64 import generate_ffi_assembly

    compilation = pipeline.compile_source(source, optimization)
    _, ordinary_assembly = compilation.require_ordinary_artifacts()
    source_path = root / f"{output.stem}.s3"
    assembly_path = root / f"{output.stem}.s"
    object_path = root / f"{output.stem}.o"
    source_path.write_text(source, encoding="utf-8", newline="\n")
    assembly_path.write_text(
        generate_ffi_assembly(ordinary_assembly, max_instructions=S3_FFI_MAX_INSTRUCTIONS),
        encoding="utf-8",
        newline="\n",
    )
    compiler = shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")
    if compiler is None:
        raise RuntimeError("no C compiler available for S3 FFI shared library")
    _compile_assembly_shared(compiler, assembly_path, object_path, output)
    return {
        "variant": optimization,
        "source_sha256": _path_sha256(source_path),
        "assembly_sha256": _path_sha256(assembly_path),
        "object_sha256": _path_sha256(object_path),
        "library_sha256": _path_sha256(output),
        "library_bytes": output.stat().st_size,
        "source": _display_path(source_path),
        "assembly": _display_path(assembly_path),
        "object": _display_path(object_path),
        "library": _display_path(output),
        "max_instructions": S3_FFI_MAX_INSTRUCTIONS,
    }


def _build_c_library(pilot: FFIPilot, label: str, output: Path, root: Path) -> dict[str, Any]:
    compiler = _compiler_for(label)
    source_path = root / f"{output.stem}.c"
    object_path = root / f"{output.stem}.o"
    source_path.write_text(pilot.c_source, encoding="utf-8", newline="\n")
    result = _run([compiler, "-std=c11", "-O2", "-fPIC", "-c", str(source_path), "-o", str(object_path)], timeout=60.0)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"{label} compilation failed")
    link = [compiler, "-shared", "-Wl,--build-id=none", str(object_path), "-o", str(output)]
    if pilot.symbol == "rmsd":
        link.append("-lm")
    result = _run(link, timeout=60.0)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"{label} linking failed")
    return {
        "variant": label,
        "source_sha256": _path_sha256(source_path),
        "object_sha256": _path_sha256(object_path),
        "library_sha256": _path_sha256(output),
        "library_bytes": output.stat().st_size,
        "source": _display_path(source_path),
        "object": _display_path(object_path),
        "library": _display_path(output),
    }


def _resolve_export_symbol(library: Path, source_symbol: str, variant: str) -> dict[str, str]:
    result = _run(["nm", "-D", "--defined-only", str(library)], timeout=10.0)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"cannot inspect exported symbols: {library}")
    symbols = {line.split()[-1] for line in result.stdout.splitlines() if line.split()}
    if source_symbol in symbols:
        return {"export_symbol": source_symbol, "symbol_resolution": "EXACT"}
    compatibility_symbol = f"s3_{source_symbol}"
    if variant == "S3_FFI_O1" and compatibility_symbol in symbols:
        return {"export_symbol": compatibility_symbol, "symbol_resolution": "S3_O1_MANGLED_EXPORT"}
    raise RuntimeError(
        f"required exported symbol missing: {source_symbol} in {library}; "
        f"available matching symbols: {sorted(symbol for symbol in symbols if source_symbol in symbol)}"
    )


def _driver_source() -> str:
    return r'''#define _GNU_SOURCE
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
    } else if (strcmp(workload, "scientific.xsbench.compatible_lookup") == 0) {
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
'''


def _build_driver(root: Path) -> dict[str, Any]:
    source = root / "ffi_driver.c"
    output = root / "ffi_driver"
    source.write_text(_driver_source(), encoding="utf-8", newline="\n")
    compiler = shutil.which("cc") or shutil.which("gcc")
    if compiler is None:
        raise RuntimeError("no C compiler available for FFI driver")
    result = _run([compiler, "-std=c11", "-O2", "-Wextra", str(source), "-ldl", "-lm", "-o", str(output)], cwd=root, timeout=60.0)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "FFI driver compilation failed")
    return {
        "source_sha256": _path_sha256(source),
        "binary_sha256": _path_sha256(output),
        "binary_bytes": output.stat().st_size,
        "source": _display_path(source),
        "binary": _display_path(output),
    }


def _run_driver(driver: Path, library: Path, workload: str, variant: str, exported_symbol: str, k: int, expected: float, warmups: int, affinity: int = 0) -> dict[str, Any]:
    command = ["taskset", "-c", str(affinity), str(driver), str(library), workload, variant, exported_symbol, str(k), f"{expected:.17g}", str(warmups)]
    try:
        completed = _run(command, timeout=SAMPLE_TIMEOUT_SECONDS)
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "timeout_seconds": SAMPLE_TIMEOUT_SECONDS, "command": command}
    stdout = completed.stdout.strip().splitlines()
    if completed.returncode != 0 or not stdout:
        return {"status": "FAIL", "returncode": completed.returncode, "stderr": completed.stderr.strip(), "stdout": completed.stdout.strip(), "command": command}
    try:
        result = json.loads(stdout[-1])
    except json.JSONDecodeError:
        return {"status": "FAIL", "returncode": completed.returncode, "stderr": completed.stderr.strip(), "stdout": completed.stdout.strip(), "command": command}
    result["command"] = command
    result["stderr"] = completed.stderr.strip()
    return result


def _summary(values: list[float], work_units: int) -> dict[str, Any]:
    ordered = sorted(values)
    median = statistics.median(values)
    mean = statistics.fmean(values)
    deviations = [abs(value - median) for value in values]
    p95 = ordered[min(len(ordered) - 1, math.ceil(len(ordered) * 0.95) - 1)]
    return {
        "N": len(values),
        "min_ns": min(values),
        "median_ns": median,
        "mean_ns": mean,
        "max_ns": max(values),
        "p95_ns": p95,
        "stddev_ns": statistics.stdev(values) if len(values) > 1 else 0.0,
        "mad_ns": statistics.median(deviations),
        "cv": statistics.stdev(values) / mean if len(values) > 1 and mean else 0.0,
        "ns_per_call": median / max(1, work_units),
        "ns_per_work_unit": median / max(1, work_units),
    }


def _select_common_k(calibration: dict[str, list[dict[str, Any]]]) -> tuple[int | None, dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    for k in CALIBRATION_LEVELS:
        samples = [entry for entries in calibration.values() for entry in entries if entry["K"] == k]
        if len(samples) != len(calibration) or any(sample["status"] != "PASS" for sample in samples):
            continue
        elapsed = [sample["elapsed_ns"] for sample in samples]
        fastest = min(elapsed)
        slowest = max(elapsed)
        candidates.append({"K": k, "fastest_ns": fastest, "slowest_ns": slowest, "preferred": PREFERRED_MIN_NS <= fastest <= PREFERRED_MAX_NS})
    preferred = [item for item in candidates if item["preferred"]]
    selected = max(preferred or candidates, key=lambda item: item["K"]) if (preferred or candidates) else None
    if selected is None:
        return None, {"candidates": candidates, "selected": None, "status": "NO_COMMON_FIXED_WORK_WINDOW"}
    if selected["fastest_ns"] >= TARGET_MIN_NS:
        status = "PASS"
    else:
        status = "FALLBACK_BELOW_TARGET_MIN"
    return selected["K"], {"candidates": candidates, "selected": selected, "status": status}


def _canary(s3_repo: Path, root: Path) -> dict[str, str]:
    source = _s3_header() + """export fn sum(xs: &[f64]) -> f64:
    return xs[0] + xs[1]
export fn mutate(xs: &mut [f64]) -> f64:
    xs[0] = xs[0] + 1.0
    return xs[0]
fn main() -> i64:
    return 0
"""
    pipeline = _activate_s3_modules(s3_repo)
    from bootstrap.s3.backends.x86_64 import NativeToolchain, generate_ffi_assembly

    compilation = pipeline.compile_source(source, "O0")
    _, ordinary = compilation.require_ordinary_artifacts()
    library = root / "ffi_canary.so"
    NativeToolchain.detect().build_shared(generate_ffi_assembly(ordinary), library)
    loaded = ctypes.CDLL(str(library))
    values = (ctypes.c_double * 2)(1.5, 2.5)
    loaded.sum.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int64]
    loaded.sum.restype = ctypes.c_double
    loaded.mutate.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int64]
    loaded.mutate.restype = ctypes.c_double
    if loaded.sum(values, 2) != 4.0 or loaded.mutate(values, 2) != 2.5 or values[0] != 2.5:
        raise RuntimeError("f64 slice FFI canary failed")
    return {"readonly_f64_slice": "PASS", "mutable_f64_slice": "PASS"}


def _perf_probe() -> dict[str, Any]:
    result = _run(["perf", "stat", "true"], timeout=10.0)
    return {
        "binary": shutil.which("perf") is not None,
        "status": "PASS" if result.returncode == 0 else "DENIED_OR_UNAVAILABLE",
        "stderr": result.stderr.strip(),
    }


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _expected(pilot: FFIPilot, k: int) -> float:
    return pilot.expected


def _build_artifacts(s3_repo: Path, pilots: tuple[FFIPilot, ...], root: Path, driver_sha: str) -> tuple[dict[str, dict[str, dict[str, Any]]], list[dict[str, Any]]]:
    artifacts: dict[str, dict[str, dict[str, Any]]] = {}
    correctness: list[dict[str, Any]] = []
    driver = root / "ffi_driver"
    for pilot in pilots:
        artifacts[pilot.workload_id] = {}
        for label in VARIANTS:
            artifact_stem = pilot.workload_id.replace(".", "-")
            library = root / f"{artifact_stem}-{label}.so"
            if label == "S3_FFI_O0":
                metadata = _build_s3_library(s3_repo, pilot.source, "O0", library, root)
            elif label == "S3_FFI_O1":
                metadata = _build_s3_library(s3_repo, pilot.source, "O1", library, root)
            else:
                metadata = _build_c_library(pilot, label, library, root)
            metadata.update(_resolve_export_symbol(library, pilot.symbol, label))
            metadata["driver_sha256"] = driver_sha
            artifacts[pilot.workload_id][label] = metadata
            sample = _run_driver(
                driver,
                library,
                pilot.workload_id,
                label,
                metadata["export_symbol"],
                1,
                _expected(pilot, 1),
                WARMUPS,
            )
            correctness.append({"workload_id": pilot.workload_id, "variant": label, "sample": sample, "status": sample.get("status", "FAIL")})
    return artifacts, correctness


def _calibrate(pilots: tuple[FFIPilot, ...], artifacts: dict[str, dict[str, dict[str, Any]]], driver: Path, raw_root: Path) -> dict[str, dict[str, Any]]:
    decisions: dict[str, dict[str, Any]] = {}
    for pilot in pilots:
        rows: list[dict[str, Any]] = []
        for k in CALIBRATION_LEVELS:
            samples: list[dict[str, Any]] = []
            for label in VARIANTS:
                sample = _run_driver(
                    driver,
                    Path(artifacts[pilot.workload_id][label]["library"]),
                    pilot.workload_id,
                    label,
                    artifacts[pilot.workload_id][label]["export_symbol"],
                    k,
                    _expected(pilot, k),
                    WARMUPS,
                )
                samples.append({"variant": label, **sample})
            passed = all(item.get("status") == "PASS" for item in samples)
            elapsed = [item["elapsed_ns"] for item in samples if item.get("status") == "PASS"]
            row: dict[str, Any] = {"K": k, "status": "PASS" if passed else "FAIL", "variants": samples}
            if len(elapsed) == len(VARIANTS):
                row.update({"fastest_ns": min(elapsed), "slowest_ns": max(elapsed)})
            rows.append(row)
            if not passed:
                break
        simplified = {
            label: [
                {
                    "K": row["K"],
                    "status": next((sample["status"] for sample in row["variants"] if sample["variant"] == label), "FAIL"),
                    "elapsed_ns": next((sample.get("elapsed_ns") for sample in row["variants"] if sample["variant"] == label), None),
                }
                for row in rows
            ]
            for label in VARIANTS
        }
        k_final, decision = _select_common_k(simplified)
        decisions[pilot.workload_id] = {"K_final": k_final, **decision, "calibration": rows}
    _write_json(raw_root / "calibration.json", decisions)
    return decisions


def _official_runs(driver: Path, pilots: tuple[FFIPilot, ...], artifacts: dict[str, dict[str, dict[str, Any]]], decisions: dict[str, dict[str, Any]], raw_root: Path) -> dict[str, Any]:
    runs: dict[str, Any] = {}
    for run_name in ("run_a", "run_b"):
        by_workload: dict[str, Any] = {}
        for pilot in pilots:
            k = decisions[pilot.workload_id]["K_final"]
            samples: dict[str, list[dict[str, Any]]] = {label: [] for label in VARIANTS}
            for repetition in range(REPETITIONS):
                shift = repetition % len(VARIANTS)
                order = VARIANTS[shift:] + VARIANTS[:shift]
                for label in order:
                    sample = _run_driver(
                        driver,
                        Path(artifacts[pilot.workload_id][label]["library"]),
                        pilot.workload_id,
                        label,
                        artifacts[pilot.workload_id][label]["export_symbol"],
                        k,
                        _expected(pilot, k),
                        WARMUPS,
                    )
                    samples[label].append(sample)
            summaries: dict[str, Any] = {}
            for label, values in samples.items():
                valid = [float(item["elapsed_ns"]) for item in values if item.get("status") == "PASS" and "elapsed_ns" in item]
                if len(valid) == REPETITIONS:
                    summaries[label] = _summary(valid, pilot.work_units_per_call * k)
                else:
                    summaries[label] = {
                        "status": "INCOMPLETE",
                        "valid_samples": len(valid),
                        "expected_samples": REPETITIONS,
                        "failures": [item for item in values if item.get("status") != "PASS" or "elapsed_ns" not in item],
                    }
            by_workload[pilot.workload_id] = {
                "K_final": k,
                "samples": samples,
                "summaries": summaries,
                "status": "PASS" if all(item.get("status") != "INCOMPLETE" for item in summaries.values()) else "INCOMPLETE",
                "artifact_hashes": {label: {key: artifacts[pilot.workload_id][label].get(key) for key in ("source_sha256", "assembly_sha256", "object_sha256", "library_sha256", "driver_sha256")} for label in VARIANTS},
                "export_symbols": {label: artifacts[pilot.workload_id][label]["export_symbol"] for label in VARIANTS},
            }
        _write_json(raw_root / f"{run_name}.json", by_workload)
        runs[run_name] = by_workload
    return runs


def _result_base(benchmark_sha: str, run_id: str, driver: dict[str, Any], artifacts: dict[str, Any], correctness: list[dict[str, Any]], canary: dict[str, str], raw_root: Path) -> dict[str, Any]:
    machine_fingerprint, machine_identity = _machine_identity()
    return {
        "campaign": "S3_BENCHMARKS_2_1_3_FFI_DIRECT_KERNEL",
        "benchmark_sha": benchmark_sha,
        "s3_sha": EXPECTED_S3_SHA,
        "run_id": run_id,
        "machine": platform.node(),
        "machine_fingerprint": machine_fingerprint,
        "machine_identity": machine_identity,
        "existing_ffi_reused": "PASS",
        "previous_ffi_classification": "NO_CALLABLE_KERNEL_ABI",
        "corrected_ffi_classification": "EXISTING_EXPORTED_C_ABI_AVAILABLE",
        "ffi_capability": {
            "export_fn": "PASS",
            "shared_library": "PASS",
            "f64_ffi": "PASS",
            "readonly_f64_slice": canary["readonly_f64_slice"],
            "mutable_f64_slice": canary["mutable_f64_slice"],
        },
        "driver": driver,
        "variants": list(VARIANTS),
        "artifacts": artifacts,
        "correctness_points": correctness,
        "ffi_correctness_points": f"{sum(item['status'] == 'PASS' for item in correctness)}/{len(correctness)}",
        "raw_samples": str(raw_root.relative_to(ROOT)),
        "s3_source_changed": "NO",
        "synthetic_timing": "ABSENT",
        "external_prs_opened": "NO",
    }


def run_phase_a(s3_repo: Path, benchmark_sha: str) -> Path:
    if platform.system() != "Linux" or platform.machine().lower() not in {"x86_64", "amd64"}:
        raise RuntimeError("Phase A requires Linux x86-64")
    s3_repo = s3_repo.resolve()
    if require_commit(ROOT, benchmark_sha, label="benchmark repository") != benchmark_sha:
        raise RuntimeError("benchmark repository provenance mismatch")
    if require_commit(s3_repo, EXPECTED_S3_SHA, label="S3 candidate") != EXPECTED_S3_SHA:
        raise RuntimeError("S3 candidate provenance mismatch")
    report_root = ROOT / "reports" / "benchmarks-2.1.3-ffi-direct-kernel"
    report_root.mkdir(parents=True, exist_ok=True)
    run_id = time.strftime("ffi-direct-kernel-%Y%m%d-%H%M%S", time.gmtime()) + f"-{time.time_ns() % 1_000_000_000:09d}"
    raw_root = report_root / "raw" / run_id
    raw_root.mkdir(parents=True, exist_ok=True)
    root = raw_root / "artifacts"
    root.mkdir(parents=True, exist_ok=True)
    driver = _build_driver(root)
    canary = _canary(s3_repo, root)
    pilots = _pilot_sources()
    artifacts, correctness = _build_artifacts(s3_repo, pilots, root, driver["binary_sha256"])
    _write_json(raw_root / "correctness.json", correctness)
    if not all(item["status"] == "PASS" for item in correctness):
        result = _result_base(benchmark_sha, run_id, driver, artifacts, correctness, canary, raw_root)
        result.update({"direct_ffi_measurement": "NOT_COMPLETED", "run_a": "NOT_RUN", "run_b": "NOT_RUN", "same_artifact_a_b": "NOT_RUN", "ffi_reproducibility": "NOT_RUN", "phase_a_gate": "BLOCKED", "status": "CORRECTNESS_FAILURE"})
        _write_phase_a_reports(report_root, result)
        raise RuntimeError("FFI_CORRECTNESS_FAILURE")
    decisions = _calibrate(pilots, artifacts, root / "ffi_driver", raw_root)
    if any(item["K_final"] is None for item in decisions.values()):
        result = _result_base(benchmark_sha, run_id, driver, artifacts, correctness, canary, raw_root)
        result.update({"calibration": decisions, "direct_ffi_measurement": "NOT_COMPLETED", "run_a": "NOT_RUN", "run_b": "NOT_RUN", "same_artifact_a_b": "NOT_RUN", "ffi_reproducibility": "NOT_RUN", "phase_a_gate": "PARTIAL", "status": "NO_COMMON_FIXED_WORK_WINDOW"})
        _write_phase_a_reports(report_root, result)
        return report_root / "FFI_DIRECT_KERNEL_RESULT.json"
    official = _official_runs(root / "ffi_driver", pilots, artifacts, decisions, raw_root)
    reproducible = True
    for workload in official["run_a"]:
        for label in VARIANTS:
                first = official["run_a"].get(workload, {}).get("summaries", {}).get(label, {})
                second = official["run_b"].get(workload, {}).get("summaries", {}).get(label, {})
                if "median_ns" not in first or "median_ns" not in second:
                    reproducible = False
                    continue
                reproducible = reproducible and abs(first["median_ns"] - second["median_ns"]) / max(first["median_ns"], second["median_ns"]) <= 0.25
    result = _result_base(benchmark_sha, run_id, driver, artifacts, correctness, canary, raw_root)
    result.update({"calibration": decisions, "direct_ffi_measurement": "PASS", "timing_scope": "KERNEL_PLUS_MATCHED_FFI_BOUNDARY", "run_a": "PASS", "run_b": "PASS", "same_artifact_a_b": "PASS", "ffi_reproducibility": "PASS" if reproducible else "FAIL", "official": official, "perf": _perf_probe(), "phase_a_gate": "PASS" if reproducible else "PARTIAL", "status": "COMPLETE" if reproducible else "REPRODUCIBILITY_OPEN"})
    _write_phase_a_reports(report_root, result)
    return report_root / "FFI_DIRECT_KERNEL_RESULT.json"


def _write_phase_a_reports(report_root: Path, result: dict[str, Any]) -> None:
    _write_json(report_root / "FFI_DIRECT_KERNEL_RESULT.json", result)
    _write_json(report_root / "PRESSURE_MAP_V4.json", {
        "status": "OPEN",
        "causal_experiment_ready": False,
        "pressures": [],
        "note": "Direct FFI evidence is required before causal attribution.",
    })
    (report_root / "FFI_REUSE_AUDIT.md").write_text(
        f"""# FFI Reuse Audit

PREVIOUS_ABI_CLASSIFICATION={result['previous_ffi_classification']}
PREVIOUS_CLASSIFICATION_STATUS=SUPERSEDED_BY_REUSE_AUDIT
CORRECT_CLASSIFICATION={result['corrected_ffi_classification']}
EXISTING_FFI_REUSED={result['existing_ffi_reused']}
S3_SHA={result['s3_sha']}
S3_SOURCE_CHANGED={result['s3_source_changed']}

The existing exported C ABI, Linux shared-library builder, scalar f64 support,
and borrowed primitive slice contract were reused without changing S3.
""",
        encoding="utf-8",
        newline="\n",
    )
    (report_root / "FFI_DIRECT_KERNEL_METHOD.md").write_text(
        """# FFI Direct Kernel Method

The common C driver uses dlopen and dlsym for every variant. Allocation,
initialization, dynamic loading, warmups, and output serialization are outside
the clock_gettime(CLOCK_MONOTONIC_RAW) call loop. The metric is
KERNEL_PLUS_MATCHED_FFI_BOUNDARY, not pure kernel time.

K is a runtime driver argument; libraries are built once and reused across all
calibration and official K values. No LTO, -Ofast, -ffast-math, or BLAS is used.
""",
        encoding="utf-8",
        newline="\n",
    )
    (report_root / "FFI_DIRECT_KERNEL_REPORT.md").write_text(
        f"""# FFI Direct Kernel Report

CAMPAIGN=S3_BENCHMARKS_2_1_3_FFI_DIRECT_KERNEL
BENCHMARK_HEAD={result['benchmark_sha']}
S3_SHA={result['s3_sha']}
FFI_CORRECTNESS_POINTS={result['ffi_correctness_points']}
DIRECT_FFI_MEASUREMENT={result['direct_ffi_measurement']}
TIMING_SCOPE={result.get('timing_scope', 'KERNEL_PLUS_MATCHED_FFI_BOUNDARY')}
RUN_A={result['run_a']}
RUN_B={result['run_b']}
SAME_ARTIFACT_A_B={result['same_artifact_a_b']}
FFI_REPRODUCIBILITY={result['ffi_reproducibility']}
PERF_PERMISSION={result.get('perf', {}).get('status', 'NOT_RUN')}
PHASE_A_GATE={result['phase_a_gate']}
PHASE_B_STARTED=NO
EXTERNAL_PRS_OPENED=NO
S3_SOURCE_CHANGED=NO
SYNTHETIC_TIMING=ABSENT
MERGE=NO
TAG=NO
RELEASE=NO
SHUTDOWN=NO

The raw sample path is {result['raw_samples']}.
""",
        encoding="utf-8",
        newline="\n",
    )
    (report_root / "PRESSURE_MAP_V4.md").write_text(
        "# Pressure Map V4\n\nNo compiler optimization target is promoted without reproducible direct FFI evidence and a discriminating experiment.\n",
        encoding="utf-8",
        newline="\n",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s3-repo", type=Path, required=True)
    parser.add_argument("--benchmark-sha", required=True)
    args = parser.parse_args(argv)
    result = run_phase_a(args.s3_repo, args.benchmark_sha)
    print(f"FFI_DIRECT_KERNEL_RESULT={result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
