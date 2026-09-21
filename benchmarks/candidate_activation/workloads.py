"""Deterministic S3 source generators and independent numerical oracles.

The generators deliberately use only the existing candidate's f64_vector,
scalar arithmetic, references, and while loops.  A generated program returns
an integer checksum so hosted and native adapters observe the same value.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable


@dataclass(frozen=True, slots=True)
class WorkloadCase:
    workload_id: str
    size: str
    source: str
    expected: float
    classification: str
    logical_shape: str
    physical_layout: str
    index_mapping: str


def cases() -> tuple[WorkloadCase, ...]:
    result: list[WorkloadCase] = []
    for size, n in (("tiny", 4), ("small", 7)):
        result.append(_case("hpc.prk.nstream", size, n, _nstream_source, _nstream_oracle, "1D vector", "flat f64_vector", "i"))
        result.append(_case("memory.babelstream.copy", size, n, _babel_copy_source, _babel_copy_oracle, "1D vector", "flat f64_vector", "i"))
        result.append(_case("memory.babelstream.scale", size, n, _babel_scale_source, _babel_scale_oracle, "1D vector", "flat f64_vector", "i"))
        result.append(_case("memory.babelstream.add", size, n, _babel_add_source, _babel_add_oracle, "1D vector", "flat f64_vector", "i"))
        result.append(_case("memory.babelstream.triad", size, n, _babel_triad_source, _babel_triad_oracle, "1D vector", "flat f64_vector", "i"))
        result.append(_case("memory.babelstream.dot", size, n, _babel_dot_source, _babel_dot_oracle, "1D vector", "flat f64_vector", "i"))
        result.append(_case("scientific.rmsd.batch", size, max(2, n // 2), _rmsd_batch_source, _rmsd_batch_oracle, "pair_count x coordinates_per_pair", "flat f64_vector", "pair * coordinates_per_pair + coordinate"))
        result.append(_case("scientific.rmsd.matrix", size, max(2, n // 2), _rmsd_matrix_source, _rmsd_matrix_oracle, "P x Q pair matrix", "flat f64_vector", "p * Q + q"))

    for size, rows, cols in (("tiny", 2, 3), ("small", 3, 4)):
        result.append(_case("hpc.prk.transpose", size, (rows, cols), _transpose_source, _transpose_oracle, f"{rows} x {cols}", "flat f64_vector", "row * cols + column"))
        result.append(_case("numerical.polybench.atax", size, (rows, cols), _atax_source, _atax_oracle, f"A[{rows},{cols}], x[{cols}], y[{cols}]", "flat f64_vector", "i * N + j"))
        result.append(_case("numerical.polybench.mvt", size, (rows, cols), _mvt_source, _mvt_oracle, f"A[{rows},{cols}], x1[{rows}], x2[{cols}]", "flat f64_vector", "i * N + j"))
        result.append(_case("numerical.polybench.gemm", size, (rows, cols, 2), _gemm_source, _gemm_oracle, f"A[{rows},K], B[K,{cols}], C[{rows},{cols}]", "flat f64_vector", "i * stride + j"))
        result.append(_case("language.plb2.matmul", size, (rows, cols, 2), _gemm_source, _gemm_oracle, f"A[{rows},K], B[K,{cols}], C[{rows},{cols}]", "flat f64_vector", "i * stride + j"))
        result.append(_case("numerical.polybench.2mm", size, (rows, cols, 2), _two_mm_source, _two_mm_oracle, f"A[{rows},K], B[K,{cols}], C[{cols},K], D[K,{cols}]", "flat f64_vector", "i * stride + j"))
        result.append(_case("numerical.polybench.jacobi_1d", size, cols + 2, _jacobi_source, _jacobi_oracle, f"two 1D vectors length {cols + 2}", "flat f64_vector", "i"))

    for size, pairs in (("tiny", (2, 3)), ("small", (3, 4))):
        result.append(_case("compiler.tsvc.initial-subset", size, pairs, _tsvc_source, _tsvc_oracle, "selected scalar loop corpus", "flat f64_vector", "i"))
    return tuple(result)


def _case(workload_id: str, size: str, shape, builder: Callable, oracle: Callable, logical_shape: str, physical_layout: str, index_mapping: str) -> WorkloadCase:
    source = builder(shape)
    return WorkloadCase(workload_id, size, source, float(oracle(shape)), "SUPPORTED_WITH_BENCHMARK_ADAPTER", logical_shape, physical_layout, index_mapping)


def _vector(name: str, values: list[float]) -> list[str]:
    lines = [f"    mut {name}: f64_vector = f64_vector_new({len(values)})"]
    for value in values:
        lines.append(f"    discard f64_vector_push(&mut {name}, {value!r})")
    return lines


def _zeros(name: str, length: int) -> list[str]:
    return _vector(name, [0.0] * length)


def _program(body: list[str], result: str, _expected: float) -> str:
    # Hosted execution observes the actual f64 checksum.  Native execution is
    # intentionally reported through its separate i64 canary contract.
    return "fn candidate_sqrt(value: f64) -> f64:\n    return sqrt(value)\n\nfn main() -> f64:\n" + "\n".join(body) + f"\n    return {result}\n"


def _nstream_source(n: int) -> str:
    body = _vector("a", [float(i + 1) for i in range(n)]) + _vector("b", [float(i + 2) for i in range(n)]) + _vector("c", [1.0] * n)
    body += ["    mut i: i64 = 0", "    mut total: f64 = 0.0", f"    while i < {n}:", "        mut av: f64 = f64_vector_get(&a, i)", "        mut bv: f64 = f64_vector_get(&b, i)", "        mut cv: f64 = f64_vector_get(&c, i)", "        mut value: f64 = av + bv + 2.0 * cv", "        discard f64_vector_set(&mut a, i, value)", "        total = total + value", "        i = i + 1"]
    return _program(body, "total", _nstream_oracle(n))


def _nstream_oracle(n: int) -> float:
    return sum((i + 1) + (i + 2) + 2 for i in range(n))


def _babel_source(n: int, operation: str) -> str:
    a = [float(i + 1) for i in range(n)]
    b = [float(2 * i + 1) for i in range(n)]
    c = [float(3 * i + 1) for i in range(n)]
    body: list[str] = []
    if operation in {"copy", "add", "dot", "triad"}:
        body += _vector("a", a)
    if operation in {"copy", "add", "scale", "dot", "triad"}:
        body += _vector("b", b)
    if operation in {"add", "dot", "triad", "scale"}:
        body += _vector("c", c)
    body += ["    mut i: i64 = 0", "    mut total: f64 = 0.0", f"    while i < {n}:"]
    if operation == "copy":
        body += ["        mut value: f64 = f64_vector_get(&a, i)"]
    elif operation == "scale":
        body += ["        mut value: f64 = 2.0 * f64_vector_get(&c, i)", "        discard f64_vector_set(&mut b, i, value)"]
    elif operation == "add":
        body += ["        mut value: f64 = f64_vector_get(&a, i) + f64_vector_get(&b, i)", "        discard f64_vector_set(&mut c, i, value)"]
    elif operation == "triad":
        body += ["        mut value: f64 = f64_vector_get(&b, i) + 2.0 * f64_vector_get(&c, i)", "        discard f64_vector_set(&mut a, i, value)"]
    else:
        body += ["        mut value: f64 = f64_vector_get(&a, i) * f64_vector_get(&b, i)"]
    body += ["        total = total + value", "        i = i + 1"]
    oracle = {"copy": _babel_copy_oracle, "scale": _babel_scale_oracle, "add": _babel_add_oracle, "triad": _babel_triad_oracle, "dot": _babel_dot_oracle}[operation]
    return _program(body, "total", oracle(n))


def _babel_copy_source(n: int) -> str: return _babel_source(n, "copy")
def _babel_scale_source(n: int) -> str: return _babel_source(n, "scale")
def _babel_add_source(n: int) -> str: return _babel_source(n, "add")
def _babel_triad_source(n: int) -> str: return _babel_source(n, "triad")
def _babel_dot_source(n: int) -> str: return _babel_source(n, "dot")
def _babel_copy_oracle(n: int) -> float: return sum(float(i + 1) for i in range(n))
def _babel_scale_oracle(n: int) -> float: return sum(2.0 * (3 * i + 1) for i in range(n))
def _babel_add_oracle(n: int) -> float: return sum((i + 1) + (2 * i + 1) for i in range(n))
def _babel_triad_oracle(n: int) -> float: return sum((2 * i + 1) + 2 * (3 * i + 1) for i in range(n))
def _babel_dot_oracle(n: int) -> float: return sum((i + 1) * (2 * i + 1) for i in range(n))


def _rmsd_batch_source(pair_count: int) -> str:
    n = 3
    body = _vector("left", [float(i + 1) for i in range(pair_count * n)]) + _vector("right", [float(i + 2) for i in range(pair_count * n)])
    body += ["    mut pair: i64 = 0", "    mut total: f64 = 0.0", f"    while pair < {pair_count}:", "        mut coordinate: i64 = 0", "        mut ssd: f64 = 0.0", f"        while coordinate < {n}:", f"            mut offset: i64 = pair * {n} + coordinate", "            mut delta: f64 = f64_vector_get(&left, offset) - f64_vector_get(&right, offset)", "            ssd = ssd + delta * delta", "            coordinate = coordinate + 1", f"        total = total + candidate_sqrt(ssd / {float(n)!r})", "        pair = pair + 1"]
    return _program(body, "total", _rmsd_batch_oracle(pair_count))


def _rmsd_batch_oracle(pair_count: int) -> float: return float(pair_count)


def _rmsd_matrix_source(dimension: int) -> str:
    n = 3
    count = dimension * dimension * n
    body = _vector("left", [1.0] * count) + _vector("right", [2.0] * count) + _zeros("result", dimension * dimension)
    body += ["    mut p: i64 = 0", "    mut checksum: f64 = 0.0", f"    while p < {dimension}:", "        mut q: i64 = 0", f"        while q < {dimension}:", "            mut coordinate: i64 = 0", "            mut ssd: f64 = 0.0", f"            while coordinate < {n}:", f"                mut left_offset: i64 = (p * to_i64({dimension}) + q) * to_i64({n}) + coordinate", f"                mut right_offset: i64 = (q * to_i64({dimension}) + p) * to_i64({n}) + coordinate", "                mut delta: f64 = f64_vector_get(&left, left_offset) - f64_vector_get(&right, right_offset)", "                ssd = ssd + delta * delta", "                coordinate = coordinate + 1", f"            mut value: f64 = candidate_sqrt(ssd / {float(n)!r})", f"            mut result_index: i64 = p * to_i64({dimension}) + q", "            discard f64_vector_set(&mut result, result_index, value)", "            checksum = checksum + value", "            q = q + 1", "        p = p + 1"]
    return _program(body, "checksum", _rmsd_matrix_oracle(dimension))


def _rmsd_matrix_oracle(dimension: int) -> float: return float(dimension * dimension)


def _matrix_values(rows: int, cols: int, offset: int = 0) -> list[float]:
    return [float(offset + r * cols + c + 1) for r in range(rows) for c in range(cols)]


def _transpose_source(shape: tuple[int, int]) -> str:
    rows, cols = shape
    body = _vector("input", _matrix_values(rows, cols)) + _zeros("output", rows * cols)
    body += ["    mut i: i64 = 0", f"    while i < {rows}:", "        mut j: i64 = 0", f"        while j < {cols}:", f"            mut source_index: i64 = i * to_i64({cols}) + j", f"            mut destination_index: i64 = j * to_i64({rows}) + i", "            mut value: f64 = f64_vector_get(&input, source_index)", "            discard f64_vector_set(&mut output, destination_index, value)", "            j = j + 1", "        i = i + 1", "    mut index: i64 = 0", "    mut checksum: f64 = 0.0", f"    while index < {rows * cols}:", "        mut value: f64 = f64_vector_get(&output, index)", "        checksum = checksum + (to_f64(index) + 1.0) * value", "        index = index + 1"]
    return _program(body, "checksum", _transpose_oracle(shape))


def _transpose_oracle(shape: tuple[int, int]) -> float:
    rows, cols = shape
    return sum((j * rows + i + 1) * (i * cols + j + 1) for i in range(rows) for j in range(cols))


def _atax_source(shape: tuple[int, int]) -> str:
    rows, cols = shape
    body = _vector("matrix", _matrix_values(rows, cols)) + _vector("x", [float(i + 1) for i in range(cols)]) + _zeros("tmp", rows) + _zeros("y", cols)
    body += ["    mut i: i64 = 0", f"    while i < {rows}:", "        mut j: i64 = 0", "        mut total: f64 = 0.0", f"        while j < {cols}:", f"            mut index: i64 = i * to_i64({cols}) + j", "            total = total + f64_vector_get(&matrix, index) * f64_vector_get(&x, j)", "            j = j + 1", "        discard f64_vector_set(&mut tmp, i, total)", "        i = i + 1", "    mut j: i64 = 0", f"    while j < {cols}:", "        mut i2: i64 = 0", "        mut total2: f64 = 0.0", "        while i2 < " + str(rows) + ":", f"            mut index2: i64 = i2 * to_i64({cols}) + j", "            total2 = total2 + f64_vector_get(&matrix, index2) * f64_vector_get(&tmp, i2)", "            i2 = i2 + 1", "        discard f64_vector_set(&mut y, j, total2)", "        j = j + 1", "    mut k: i64 = 0", "    mut checksum: f64 = 0.0", f"    while k < {cols}:", "        checksum = checksum + f64_vector_get(&y, k)", "        k = k + 1"]
    return _program(body, "checksum", _atax_oracle(shape))


def _atax_oracle(shape: tuple[int, int]) -> float:
    rows, cols = shape
    a = _matrix_values(rows, cols)
    x = [float(i + 1) for i in range(cols)]
    tmp = [sum(a[i * cols + j] * x[j] for j in range(cols)) for i in range(rows)]
    return sum(sum(a[i * cols + j] * tmp[i] for i in range(rows)) for j in range(cols))


def _mvt_source(shape: tuple[int, int]) -> str:
    rows, cols = shape
    body = _vector("matrix", _matrix_values(rows, cols)) + _vector("x1", [float(i + 1) for i in range(rows)]) + _vector("x2", [float(i + 2) for i in range(cols)]) + _vector("y1", [1.0] * rows) + _vector("y2", [1.0] * cols)
    body += ["    mut i: i64 = 0", f"    while i < {rows}:", "        mut j: i64 = 0", f"        while j < {cols}:", f"            mut index: i64 = i * to_i64({cols}) + j", "            mut value1: f64 = f64_vector_get(&y1, i) + f64_vector_get(&matrix, index) * f64_vector_get(&x2, j)", "            discard f64_vector_set(&mut y1, i, value1)", "            mut value2: f64 = f64_vector_get(&y2, j) + f64_vector_get(&matrix, index) * f64_vector_get(&x1, i)", "            discard f64_vector_set(&mut y2, j, value2)", "            j = j + 1", "        i = i + 1", "    mut checksum: f64 = 0.0", "    mut k: i64 = 0", f"    while k < {rows}:", "        checksum = checksum + f64_vector_get(&y1, k)", "        k = k + 1", "    k = 0", f"    while k < {cols}:", "        checksum = checksum + f64_vector_get(&y2, k)", "        k = k + 1"]
    return _program(body, "checksum", _mvt_oracle(shape))


def _mvt_oracle(shape: tuple[int, int]) -> float:
    rows, cols = shape
    a = _matrix_values(rows, cols)
    x1, x2 = [float(i + 1) for i in range(rows)], [float(i + 2) for i in range(cols)]
    y1, y2 = [1.0] * rows, [1.0] * cols
    for i in range(rows):
        for j in range(cols):
            y1[i] += a[i * cols + j] * x2[j]
            y2[j] += a[i * cols + j] * x1[i]
    return sum(y1) + sum(y2)


def _gemm_source(shape: tuple[int, int, int]) -> str:
    rows, cols, inner = shape
    body = _vector("a", _matrix_values(rows, inner)) + _vector("b", _matrix_values(inner, cols, 1)) + _vector("c", [1.0] * (rows * cols))
    body += ["    mut i: i64 = 0", f"    while i < {rows}:", "        mut j: i64 = 0", f"        while j < {cols}:", "            mut k: i64 = 0", "            mut total: f64 = 1.0", f"            while k < {inner}:", f"                mut a_index: i64 = i * to_i64({inner}) + k", f"                mut b_index: i64 = k * to_i64({cols}) + j", "                total = total + f64_vector_get(&a, a_index) * f64_vector_get(&b, b_index)", "                k = k + 1", f"            mut c_index: i64 = i * to_i64({cols}) + j", "            discard f64_vector_set(&mut c, c_index, total)", "            j = j + 1", "        i = i + 1", "    mut checksum: f64 = 0.0", "    mut index: i64 = 0", f"    while index < {rows * cols}:", "        checksum = checksum + f64_vector_get(&c, index)", "        index = index + 1"]
    return _program(body, "checksum", _gemm_oracle(shape))


def _gemm_oracle(shape: tuple[int, int, int]) -> float:
    rows, cols, inner = shape
    a, b = _matrix_values(rows, inner), _matrix_values(inner, cols, 1)
    return sum(1.0 + sum(a[i * inner + k] * b[k * cols + j] for k in range(inner)) for i in range(rows) for j in range(cols))


def _two_mm_source(shape: tuple[int, int, int]) -> str:
    rows, cols, inner = shape
    p = rows
    body = _vector("a", _matrix_values(rows, inner)) + _vector("b", _matrix_values(inner, cols, 1)) + _vector("c", _matrix_values(cols, inner, 2)) + _vector("d", _matrix_values(inner, cols, 3)) + _zeros("tmp", rows * cols) + _zeros("out", rows * cols)
    body += [
        "    mut i: i64 = 0",
        f"    while i < {rows}:",
        "        mut j: i64 = 0",
        f"        while j < {cols}:",
        "            mut k: i64 = 0",
        "            mut total: f64 = 0.0",
        f"            while k < {inner}:",
        f"                mut ai: i64 = i * to_i64({inner}) + k",
        f"                mut bk: i64 = k * to_i64({cols}) + j",
        "                total = total + f64_vector_get(&a, ai) * f64_vector_get(&b, bk)",
        "                k = k + 1",
        f"            mut tmp_index: i64 = i * to_i64({cols}) + j",
        "            discard f64_vector_set(&mut tmp, tmp_index, total)",
        "            j = j + 1",
        "        i = i + 1",
        "    i = 0",
        f"    while i < {p}:",
        "        mut j: i64 = 0",
        f"        while j < {cols}:",
        "            mut k: i64 = 0",
        "            mut total2: f64 = 0.0",
        f"            while k < {inner}:",
        f"                mut ci: i64 = i * to_i64({inner}) + k",
        f"                mut dj: i64 = k * to_i64({cols}) + j",
        "                total2 = total2 + f64_vector_get(&c, ci) * f64_vector_get(&d, dj)",
        "                k = k + 1",
        f"            mut out_index: i64 = i * to_i64({cols}) + j",
        "            mut value: f64 = f64_vector_get(&tmp, out_index) + total2",
        "            discard f64_vector_set(&mut out, out_index, value)",
        "            j = j + 1",
        "        i = i + 1",
        "    mut checksum: f64 = 0.0",
        "    mut index: i64 = 0",
        f"    while index < {rows * cols}:",
        "        checksum = checksum + f64_vector_get(&out, index)",
        "        index = index + 1",
    ]
    return _program(body, "checksum", _two_mm_oracle(shape))


def _two_mm_oracle(shape: tuple[int, int, int]) -> float:
    rows, cols, inner = shape
    a, b = _matrix_values(rows, inner), _matrix_values(inner, cols, 1)
    c, d = _matrix_values(cols, inner, 2), _matrix_values(inner, cols, 3)
    return sum(sum(a[i * inner + k] * b[k * cols + j] for k in range(inner)) + sum(c[i * inner + k] * d[k * cols + j] for k in range(inner)) for i in range(rows) for j in range(cols))


def _jacobi_source(n: int) -> str:
    body = _vector("a", [float(i + 1) for i in range(n)]) + _vector("b", [0.0] * n)
    body += ["    mut step: i64 = 0", "    while step < 2:", "        mut i: i64 = 1", f"        while i < {n - 1}:", "            mut value: f64 = (f64_vector_get(&a, i - 1) + f64_vector_get(&a, i) + f64_vector_get(&a, i + 1)) / 3.0", "            discard f64_vector_set(&mut b, i, value)", "            i = i + 1", "        mut swap: f64_vector = a", "        a = b", "        b = swap", "        step = step + 1", "    mut checksum: f64 = 0.0", "    mut index: i64 = 0", f"    while index < {n}:", "        checksum = checksum + f64_vector_get(&a, index)", "        index = index + 1"]
    return _program(body, "checksum", _jacobi_oracle(n))


def _jacobi_oracle(n: int) -> float:
    a, b = [float(i + 1) for i in range(n)], [0.0] * n
    for _ in range(2):
        for i in range(1, n - 1):
            b[i] = (a[i - 1] + a[i] + a[i + 1]) / 3.0
        a, b = b, a
    return sum(a)


def _tsvc_source(shape: tuple[int, int]) -> str:
    n, stride = shape
    body = _vector("a", [float(i + 1) for i in range(n)]) + _vector("b", [float(2 * i + 1) for i in range(n)])
    body += ["    mut i: i64 = 0", "    mut checksum: f64 = 0.0", f"    while i < {n}:", "        mut x: f64 = f64_vector_get(&a, i)", "        mut y: f64 = f64_vector_get(&b, i)", "        mut value: f64 = x + y", "        discard f64_vector_set(&mut a, i, value)", "        checksum = checksum + value * to_f64(i + 1)", f"        i = i + {stride}"]
    return _program(body, "checksum", _tsvc_oracle(shape))


def _tsvc_oracle(shape: tuple[int, int]) -> float:
    n, stride = shape
    a, b = [float(i + 1) for i in range(n)], [float(2 * i + 1) for i in range(n)]
    return sum((a[i] + b[i]) * (i + 1) for i in range(0, n, stride))


def expected_for(case: WorkloadCase) -> float:
    return case.expected
