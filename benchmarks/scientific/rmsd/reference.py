"""Small independent RMSD oracle used by the evidence lab."""

from __future__ import annotations

import math
from collections.abc import Sequence


def rmsd(left: Sequence[float], right: Sequence[float]) -> float:
    if len(left) != len(right):
        raise ValueError("length mismatch")
    if not left:
        raise ValueError("empty input")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)) / len(left))


def batch_rmsd(pairs: Sequence[tuple[Sequence[float], Sequence[float]]]) -> list[float]:
    return [rmsd(left, right) for left, right in pairs]
