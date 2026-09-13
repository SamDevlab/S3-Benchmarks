from __future__ import annotations

import pytest

from tools.minimize_s3_failure import MinimizationError, minimize_lines


def test_minimizer_preserves_interesting_trigger() -> None:
    source = (
        "fn helper() -> i64:\n"
        "    return 1\n"
        "\n"
        "fn main() -> i64:\n"
        "    value: i64 = 10\n"
        "    # TRIGGER\n"
        "    return value\n"
    )

    def predicate(candidate: str) -> bool:
        return "TRIGGER" in candidate

    minimized, report = minimize_lines(source, predicate, max_runs=100)
    assert "TRIGGER" in minimized
    assert report["minimized_lines"] < report["original_lines"]
    assert report["status"] == "MINIMIZED"


def test_minimizer_rejects_non_interesting_original() -> None:
    with pytest.raises(MinimizationError):
        minimize_lines("fn main() -> i64:\n    return 1\n", lambda text: "TRIGGER" in text)


def test_minimizer_respects_run_budget() -> None:
    source = "a\nb\nc\nd\ne\n"
    _minimized, report = minimize_lines(source, lambda _text: True, max_runs=2)
    assert report["predicate_runs"] <= 2
