"""V10 challenge suite created AFTER engine freeze commit ab0b252.

Cases remain opaque to blackbox_gf2.py.  This file alone defines oracles.
No part of these examples may be used to alter the frozen discovery engine
within this evaluation. An empirical acceptance is NOT a source proof.
"""
from dataclasses import dataclass
import random
from typing import Callable


@dataclass(frozen=True)
class Challenge:
    id: str
    width: int
    step: Callable[[int], int]
    expected_linear: bool
    family: str
    polynomial: int | None = None
    rare_trigger: int | None = None


def rotate(x: int, k: int, w: int) -> int:
    k %= w
    mask = (1 << w) - 1
    return ((x << k) | (x >> (w-k))) & mask if k else x & mask


def cyclic_step(offsets: tuple[int, ...], width: int):
    def step(x):
        value = 0
        for k in offsets:
            value ^= rotate(x, k, width)
        return value
    return step


def random_linear(width: int, seed: int):
    rng = random.Random(seed)
    cols = tuple(rng.getrandbits(width) for _ in range(width))

    def step(x):
        v = 0
        while x:
            b = x & -x
            v ^= cols[b.bit_length() - 1]
            x ^= b
        return v
    return step


def rule30_like(width: int):
    mask = (1 << width) - 1

    def step(x):
        left = rotate(x, 1, width)
        right = rotate(x, -1, width)
        return (left ^ (x | right)) & mask
    return step


def cases() -> list[Challenge]:
    # Not a training set: engine was already committed before this file.
    rule90_8 = (1, 7)
    rule90_24 = (1, 23)
    rule150_32 = (0, 1, 31)
    hybrid_24 = (0, 2, 7, 9, 23)
    rare_width = 24
    rng = random.Random(115781)
    rare = rng.getrandbits(rare_width)
    while rare in (0, (1 << rare_width) - 1) or rare.bit_count() < 3:
        rare = rng.getrandbits(rare_width)
    rare_base = cyclic_step((0, 1, 5), rare_width)

    def rare_nonlinear(x):
        return rare_base(x) ^ (1 if x == rare else 0)

    mask16 = (1 << 16) - 1
    return [
        Challenge("sealed_rule90_8", 8, cyclic_step(rule90_8, 8), True, "cyclic", sum(1<<a for a in rule90_8)),
        Challenge("sealed_rule90_24", 24, cyclic_step(rule90_24, 24), True, "cyclic", sum(1<<a for a in rule90_24)),
        Challenge("sealed_rule150_32", 32, cyclic_step(rule150_32, 32), True, "cyclic", sum(1<<a for a in rule150_32)),
        Challenge("sealed_hybrid_24", 24, cyclic_step(hybrid_24, 24), True, "cyclic", sum(1<<a for a in hybrid_24)),
        Challenge("sealed_dense_linear_16", 16, random_linear(16, 234278), True, "matrix"),
        Challenge("sealed_dense_linear_32", 32, random_linear(32, 920021), True, "matrix"),
        Challenge("sealed_affine_16", 16, lambda x: ((x ^ ((x << 1)&mask16)) ^ 7) & mask16, False, "affine"),
        Challenge("sealed_nonlinear_rule30_24", 24, rule30_like(24), False, "nonlinear"),
        Challenge("sealed_rare_trigger_24", rare_width, rare_nonlinear, False, "adversarial_rare", rare_trigger=rare),
    ]
