from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools.s3_tisa_v3_benchmark import (
    canonical_sha256,
    require_clean_pin,
    summarize_samples,
    write_report,
)
from tools.s3_110_cross_version_index import _normalized_json_sha256


class LongitudinalBenchmarkTests(unittest.TestCase):
    def test_summary_reports_median_nearest_rank_p95_and_raw_samples(self) -> None:
        summary = summarize_samples([10, 20, 30, 40, 50], warmups=2)
        self.assertEqual(summary["median"], 30)
        self.assertEqual(summary["p95_nearest_rank"], 50)
        self.assertEqual(summary["samples"], [10, 20, 30, 40, 50])
        self.assertEqual(summary["repetitions"], 5)

    def test_summary_rejects_empty_negative_or_boolean_samples(self) -> None:
        for samples in ([], [-1], [True]):
            with self.subTest(samples=samples), self.assertRaises(ValueError):
                summarize_samples(samples, warmups=0)

    def test_canonical_report_hash_is_order_independent(self) -> None:
        first = {"schema": "test", "a": 1, "b": [2, 3]}
        second = {"b": [2, 3], "a": 1, "schema": "test"}
        self.assertEqual(canonical_sha256(first), canonical_sha256(second))

    def test_historical_json_hash_ignores_only_crlf_checkout_conversion(self) -> None:
        lf = b'{"result":42}\n'
        crlf = lf.replace(b"\n", b"\r\n")
        self.assertEqual(_normalized_json_sha256(lf), _normalized_json_sha256(crlf))
        self.assertNotEqual(_normalized_json_sha256(lf), _normalized_json_sha256(lf.replace(b"42", b"43")))

    def test_pinned_checkout_gate_rejects_wrong_revision_and_dirty_tree(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            with patch("tools.s3_tisa_v3_benchmark._git", side_effect=[str(root), "bad", ""]):
                with self.assertRaisesRegex(ValueError, "pin mismatch"):
                    require_clean_pin(root, "expected", "test")
            with patch("tools.s3_tisa_v3_benchmark._git", side_effect=[str(root), "expected", " M input"]):
                with self.assertRaisesRegex(ValueError, "dirty"):
                    require_clean_pin(root, "expected", "test")

    def test_report_writer_verifies_hash_and_refuses_overwrite(self) -> None:
        report = {"schema": "test", "value": 42}
        report["report_sha256"] = canonical_sha256(report)
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / "report.json"
            write_report(path, report)
            with self.assertRaises(FileExistsError):
                write_report(path, report)


if __name__ == "__main__":
    unittest.main()
