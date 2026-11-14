"""S3 V10: generic black-box GF(2) linear-map inference and fast-forward.

This module receives an opaque step(state)->state callable and a bit width.
It neither knows nor branches on cellular automaton rule names.  Discovering
linearity by finite oracle probes is probabilistic except when exhaustive.

Algorithmic baseline: standard GF(2) basis reconstruction + repeated squaring.
Not novel and NOT a full S3 compiler integration or mathematical proof of an
unknown black-box oracle's global linearity.
"""
from __future__ import annotations
from dataclasses import dataclass
import random
from typing import Callable

Oracle = Callable[[int], int]


class NotCertified(RuntimeError):
    """The observed oracle violated GF(2) linearity or its domain contract."""


def apply_columns(columns: tuple[int, ...], state: int) -> int:
    value = 0
    while state:
        lowbit = state & -state
        value ^= columns[lowbit.bit_length() - 1]
        state ^= lowbit
    return value


def compose_columns(lhs: tuple[int, ...], rhs: tuple[int, ...]) -> tuple[int, ...]:
    """Return columns of lhs ◦ rhs over GF(2)."""
    return tuple(apply_columns(lhs, column) for column in rhs)


@dataclass(frozen=True)
class GF2Candidate:
    width: int
    columns: tuple[int, ...]
    status: str
    oracle_calls: int
    exhaustive: bool
    checks: int

    def advance(self, state: int, generations: int) -> int:
        mask = (1 << self.width) - 1
        if state < 0 or state > mask or generations < 0:
            raise ValueError("state or generations outside nonnegative supported domain")
        columns = self.columns
        out = state
        steps = generations
        while steps:
            if steps & 1:
                out = apply_columns(columns, out)
            steps >>= 1
            if steps:
                columns = compose_columns(columns, columns)
        return out

    def advance_with_counts(self, state: int, generations: int) -> tuple[int, dict]:
        mask = (1 << self.width) - 1
        if state < 0 or state > mask or generations < 0:
            raise ValueError("invalid state/generations")
        columns = self.columns
        out = state
        e = generations
        squarings = applies = 0
        while e:
            if e & 1:
                out = apply_columns(columns, out)
                applies += 1
            e >>= 1
            if e:
                columns = compose_columns(columns, columns)
                squarings += 1
        return out, {
            "bit_length_N": generations.bit_length(),
            "popcount_N": generations.bit_count(),
            "matrix_compositions": squarings,
            "matrix_vector_applications": applies,
            "generation_loop_steps": 0,
        }


def infer_gf2_map(
    oracle: Oracle,
    width: int,
    *,
    probes: int = 96,
    seed: int = 1777,
    exhaustive_limit: int = 10,
) -> GF2Candidate:
    if not 1 <= width <= 64:
        raise ValueError("width must be 1..64")
    if probes < 0:
        raise ValueError("probes must be >=0")
    mask = (1 << width) - 1
    calls = 0
    rng = random.Random(seed)

    def query(s: int) -> int:
        nonlocal calls
        value = oracle(s)
        calls += 1
        if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= mask:
            raise NotCertified("out-of-domain oracle output")
        return value

    if query(0) != 0:
        raise NotCertified("GF(2) linear map requires f(0)=0")

    columns = tuple(query(1 << i) for i in range(width))
    # All candidate basis results are deduced from the black-box oracle.
    # Deliberately no hint for Rule 90/150 or any recurrence family.

    checks = 0
    if width <= exhaustive_limit:
        for x in range(1 << width):
            checks += 1
            if query(x) != apply_columns(columns, x):
                raise NotCertified(f"exhaustive linearity counterexample: x={x}")
        exhaustive = True
    else:
        # Non-random vectors targeted at obvious sparse/dense structures.
        vectors = [mask, mask >> 1, (mask + 1) // 3, mask ^ 1]
        for x in vectors:
            checks += 1
            if query(x) != apply_columns(columns, x):
                raise NotCertified(f"structured linearity counterexample: x={x}")
        for _ in range(probes):
            x, y = rng.getrandbits(width), rng.getrandbits(width)
            fx, fy, fxy = query(x), query(y), query(x ^ y)
            checks += 1
            if fxy != (fx ^ fy):
                raise NotCertified(f"BLR linearity test counterexample for x={x}, y={y}")
            if fx != apply_columns(columns, x):
                raise NotCertified(f"basis reconstruction counterexample x={x}")
        exhaustive = False

    return GF2Candidate(
        width=width, columns=columns,
        status="EXHAUSTIVE_ORACLE_EQUIVALENCE" if exhaustive else "PROVISIONAL_RANDOMIZED_LINEARITY",
        oracle_calls=calls, exhaustive=exhaustive, checks=checks,
    )
