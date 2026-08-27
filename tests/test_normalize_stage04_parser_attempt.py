from __future__ import annotations

from tools.normalize_stage04_parser_attempt import normalize


def test_normalize_parser_attempt_pass() -> None:
    report = normalize(
        "\n".join(
            [
                "PARSER_ATTEMPT_ID=attempt-7",
                f"CANDIDATE_SOURCE_SHA256={'a' * 64}",
                "PARSER_STATUS=BLOCKED_SYNTAX",
                "DIAGNOSTIC_CODE=PARSE_EXPECTED_MATCH_ARM",
                "DIAGNOSTIC_LINE=220",
                "DIAGNOSTIC_COLUMN=13",
                "DIAGNOSTIC_CLASS=duplicate_match_branch",
                "DIAGNOSTIC_FINGERPRINT=duplicate-match:220",
            ]
        )
    )
    assert report["normalization_status"] == "PASS"
    assert report["parser_status"] == "BLOCKED_SYNTAX"
    assert report["diagnostic_line"] == 220


def test_normalize_parser_attempt_rejects_bad_sha() -> None:
    report = normalize(
        "PARSER_ATTEMPT_ID=a1\n"
        "CANDIDATE_SOURCE_SHA256=abc\n"
        "PARSER_STATUS=PASS\n"
    )
    assert report["normalization_status"] == "BLOCKED"
    assert any("64 lowercase hex" in error for error in report["normalization_errors"])


def test_normalize_parser_attempt_rejects_duplicate_keys() -> None:
    report = normalize(
        "PARSER_ATTEMPT_ID=a1\n"
        "PARSER_ATTEMPT_ID=a2\n"
        f"CANDIDATE_SOURCE_SHA256={'b' * 64}\n"
        "PARSER_STATUS=PASS\n"
    )
    assert report["normalization_status"] == "BLOCKED"
    assert report["duplicate_keys"] == ["PARSER_ATTEMPT_ID"]


def test_normalize_parser_attempt_does_not_infer_from_prose() -> None:
    report = normalize(
        "Parser passou completamente agora.\n"
        "PARSER_ATTEMPT_ID=a1\n"
        f"CANDIDATE_SOURCE_SHA256={'c' * 64}\n"
    )
    assert report["normalization_status"] == "PASS"
    assert report["parser_status"] == "NOT_RUN"
