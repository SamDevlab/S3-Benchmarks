"""Dynamic-width eight-neighbor 2D stencil source, no fixed-width specializer."""
from __future__ import annotations
import hashlib


def source():
    return """export fn dynamic_neighbor(xs: &[i64], width: i64, base: i64) -> i64:
    match (width >= 3):
        -1:
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
        else:
            mut twice_slow: i64 = width + width
            mut upper_slow: i64 = twice_slow + 2
            mut j1: i64 = base + 1
            mut j2: i64 = base + 2
            mut j3: i64 = base + width
            mut j4: i64 = j3 + 2
            mut j5: i64 = base + twice_slow
            mut j6: i64 = j5 + 1
            mut j7: i64 = base + upper_slow
            return xs[base] + xs[j7] + xs[j1] + xs[j2] + xs[j3] + xs[j4] + xs[j5] + xs[j6]

export fn dynamic_stencil(xs: &[i64], width: i64, height: i64) -> i64:
    match (width >= 3):
        -1:
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
        else:
            return 0

fn main() -> i64:
    return 0
"""


def sha256_hex():
    return hashlib.sha256(source().encode()).hexdigest()
