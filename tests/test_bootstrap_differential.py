from tools.run_bootstrap_differential import classify_observations, extract_observation


def _obs(code=0, out="", err="", status="COMPLETED"):
    import hashlib

    raw = out.encode()
    return {
        "status": status,
        "returncode": code,
        "stdout": out,
        "stderr": err,
        "stdout_sha256": hashlib.sha256(raw).hexdigest(),
    }


def test_missing_stage1_is_not_failure() -> None:
    assert classify_observations(_obs(out="42\n"), None) == "STAGE1_NOT_RUN"


def test_exact_stdout_parity_passes() -> None:
    assert classify_observations(_obs(out="42\n"), _obs(out="42\n")) == "PASS"


def test_output_difference_is_semantic_mismatch() -> None:
    assert classify_observations(_obs(out="42\n"), _obs(out="41\n")) == "SEMANTIC_MISMATCH"


def test_explicit_stage1_blocker_is_not_relabelled_as_pass() -> None:
    result = classify_observations(
        _obs(out="42\n"),
        _obs(code=2, err="S3_STAGE1_EMITTER_BLOCKED"),
        blocked_marker="S3_STAGE1_EMITTER_BLOCKED",
    )
    assert result == "STAGE1_BLOCKED"


def test_unrecognized_nonzero_stage1_is_failure_in_stdout_mode() -> None:
    assert classify_observations(_obs(), _obs(code=2, err="other")) == "STAGE1_FAIL"


def test_reference_failure_takes_precedence_in_stdout_mode() -> None:
    assert classify_observations(_obs(code=1), _obs()) == "REFERENCE_FAIL"


def test_hosted_return_line_can_match_native_exit_code() -> None:
    result = classify_observations(
        _obs(code=0, out="program returned: 37\n"),
        _obs(code=37),
        reference_mode="program-return-line",
        stage1_mode="exit-code",
    )
    assert result == "PASS"


def test_hosted_return_line_and_native_exit_code_mismatch_is_semantic() -> None:
    result = classify_observations(
        _obs(code=0, out="program returned: 37\n"),
        _obs(code=36),
        reference_mode="program-return-line",
        stage1_mode="exit-code",
    )
    assert result == "SEMANTIC_MISMATCH"


def test_blocker_marker_precedes_exit_code_observation() -> None:
    result = classify_observations(
        _obs(code=0, out="program returned: 2\n"),
        _obs(code=2, err="S3_STAGE1_EMITTER_BLOCKED"),
        blocked_marker="S3_STAGE1_EMITTER_BLOCKED",
        reference_mode="program-return-line",
        stage1_mode="exit-code",
    )
    assert result == "STAGE1_BLOCKED"


def test_program_return_line_requires_canonical_marker() -> None:
    valid, value = extract_observation(_obs(out="37\n"), "program-return-line")
    assert valid is False
    assert value is None
