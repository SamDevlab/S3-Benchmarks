"""Unguarded S3 dynamic-width 3x3 stencil: compiler must invent guard.

The source performs the original eight neighbor reads without any
width>=3 condition. The exact same code is the slow fallback.
"""
from __future__ import annotations
import hashlib


def source()->str:
    return """export fn auto_neighbor(xs: &[i64], width: i64, base: i64) -> i64:
    mut twice: i64 = width + width
    mut upper: i64 = twice + 2
    mut i1: i64 = base + 1
    mut i2: i64 = base + 2
    mut i3: i64 = base + width
    mut i4: i64 = i3 + 2
    mut i5: i64 = base + twice
    mut i6: i64 = i5 + 1
    mut i7: i64 = base + upper
    return xs[base] + xs[i7] + xs[i1] + xs[i2] + xs[i3] + xs[i4] + xs[i5] + xs[i6]

export fn auto_stencil(xs: &[i64], width: i64, height: i64) -> i64:
    mut y: i64 = 1
    mut total: i64 = 0
    mut limit_y: i64 = height - 1
    mut limit_x: i64 = width - 1
    while y < limit_y:
        mut x: i64 = 1
        while x < limit_x:
            mut yp: i64 = y - 1
            mut row: i64 = yp * width
            mut xp: i64 = x - 1
            mut base: i64 = row + xp
            mut twice: i64 = width + width
            mut upper: i64 = twice + 2
            mut i1: i64 = base + 1
            mut i2: i64 = base + 2
            mut i3: i64 = base + width
            mut i4: i64 = i3 + 2
            mut i5: i64 = base + twice
            mut i6: i64 = i5 + 1
            mut i7: i64 = base + upper
            total = total + xs[base] + xs[i7] + xs[i1] + xs[i2] + xs[i3] + xs[i4] + xs[i5] + xs[i6]
            x = x + 1
        y = y + 1
    return total

fn main() -> i64:
    return 0
"""


def sha256_hex()->str:
    return hashlib.sha256(source().encode("utf-8")).hexdigest()
