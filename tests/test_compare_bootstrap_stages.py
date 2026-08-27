from tools.compare_bootstrap_stages import compare


def test_missing_stage2_stage3_remain_not_available(tmp_path) -> None:
    stage1 = tmp_path / "stage1.bin"
    stage1.write_bytes(b"stage1")
    report = compare(
        {"stage1": stage1, "stage2": None, "stage3": None},
        {"stage1": None, "stage2": None, "stage3": None},
    )
    assert report["stage1_stage2_stage3_observable_equivalence"] == "NOT_AVAILABLE"
    assert report["stage2_stage3_byte_identity"] is None
    assert report["full_self_hosting_claim"] is False


def test_stage2_stage3_byte_identity_is_separate_from_observable_equivalence(tmp_path) -> None:
    artifacts = {}
    observations = {}
    for stage, payload in (("stage1", b"bootstrap"), ("stage2", b"fixed"), ("stage3", b"fixed")):
        artifact = tmp_path / f"{stage}.bin"
        artifact.write_bytes(payload)
        artifacts[stage] = artifact
        observation = tmp_path / f"{stage}.obs"
        observation.write_bytes(b"same-result")
        observations[stage] = observation
    report = compare(artifacts, observations)
    assert report["stage2_stage3_byte_identity"] is True
    assert report["stage1_stage2_stage3_observable_equivalence"] == "PASS"


def test_observable_mismatch_is_failure_even_if_stage2_stage3_bytes_match(tmp_path) -> None:
    artifacts = {}
    observations = {}
    for stage in ("stage1", "stage2", "stage3"):
        artifact = tmp_path / f"{stage}.bin"
        artifact.write_bytes(b"same-artifact")
        artifacts[stage] = artifact
        observation = tmp_path / f"{stage}.obs"
        observation.write_bytes(stage.encode())
        observations[stage] = observation
    report = compare(artifacts, observations)
    assert report["stage2_stage3_byte_identity"] is True
    assert report["stage1_stage2_stage3_observable_equivalence"] == "FAIL"
