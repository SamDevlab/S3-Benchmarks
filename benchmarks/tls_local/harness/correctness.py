"""Deterministic local TLS correctness gate for S3 M1.75.

The current S3 async TLS surface is provider-neutral. This fixture validates
the nonblocking state machine, secure configuration, failure cleanup, bounded
I/O, and close semantics without public internet or custom cryptography.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

from bootstrap.s3.async_core import PollKind
from bootstrap.s3.async_tls import (
    AsyncTlsClient,
    AsyncTlsConfig,
    AsyncTlsError,
    AsyncTlsErrorCode,
    AsyncTlsService,
    Failure,
    Ready,
    WantRead,
    WantWrite,
)


EXPECTED: dict[str, Any] = {
    "handshake": {
        "kinds": ["pending", "pending", "ready"],
        "states": ["suspended", "suspended", "completed"],
        "verify_certificate": True,
        "verify_hostname": True,
        "closed_before_client_close": 0,
        "closed_after_client_close": 1,
    },
    "secure_config": {
        "certificate_disable_rejected": True,
        "hostname_disable_rejected": True,
        "invalid_hostname_rejected": True,
    },
    "hostname_failure": {
        "kind": "failed",
        "error": "hostname",
        "connection_closed": 1,
    },
    "certificate_failure": {
        "kind": "failed",
        "error": "certificate",
        "connection_closed": 1,
    },
    "cancel_handshake": {
        "poll_kind": "pending",
        "cancel_ok": True,
        "connection_closed": 1,
    },
    "io": {
        "read_kinds": ["pending", "ready"],
        "read_data": "reply",
        "write_kinds": ["pending", "ready"],
        "write_count": 4,
        "oversize_error": "resource_limit",
        "close_idempotent": True,
        "provider_close_count": 1,
    },
}


class FixtureTlsProvider:
    def __init__(self, handshake_outcomes, *, read_outcomes=None, write_outcomes=None):
        self.handshake_outcomes = list(handshake_outcomes)
        self.read_outcomes = list(read_outcomes or [Ready(b"reply")])
        self.write_outcomes = list(write_outcomes or [])
        self.closed: list[object] = []

    def handshake(self, _connection, _hostname):
        if not self.handshake_outcomes:
            return Failure(
                AsyncTlsError(AsyncTlsErrorCode.IO, "handshake", "fixture exhausted")
            )
        return self.handshake_outcomes.pop(0)

    def read(self, _connection, _amount):
        if not self.read_outcomes:
            return Failure(AsyncTlsError(AsyncTlsErrorCode.IO, "read", "fixture exhausted"))
        return self.read_outcomes.pop(0)

    def write(self, _connection, data):
        if self.write_outcomes:
            return self.write_outcomes.pop(0)
        return Ready(len(data))

    def close(self, connection):
        self.closed.append(connection)


def _ready_client(provider: FixtureTlsProvider, *, max_read_write: int = 4) -> AsyncTlsClient:
    connection = object()
    future = AsyncTlsService(provider).handshake(
        connection,
        AsyncTlsConfig("fixture.local", max_read_write=max_read_write),
    )
    result = future.poll()
    if result.kind is not PollKind.READY or not isinstance(result.value, AsyncTlsClient):
        raise AssertionError(f"TLS fixture did not produce a client: {result!r}")
    return result.value


def _run_handshake_case() -> dict[str, Any]:
    provider = FixtureTlsProvider([WantRead(), WantWrite(), Ready(True)])
    connection = object()
    future = AsyncTlsService(provider).handshake(connection, AsyncTlsConfig("fixture.local"))
    polls = [future.poll(), future.poll(), future.poll()]
    client = polls[-1].value
    if not isinstance(client, AsyncTlsClient):
        raise AssertionError("TLS handshake did not yield AsyncTlsClient")
    closed_before = len(provider.closed)
    client.close()
    client.close()
    return {
        "kinds": [poll.kind.value for poll in polls],
        "states": [poll.state.value for poll in polls],
        "verify_certificate": client.config.verify_certificate,
        "verify_hostname": client.config.verify_hostname,
        "closed_before_client_close": closed_before,
        "closed_after_client_close": len(provider.closed),
    }


def _run_secure_config_case() -> dict[str, Any]:
    certificate_disable_rejected = False
    hostname_disable_rejected = False
    invalid_hostname_rejected = False
    try:
        AsyncTlsConfig("fixture.local", verify_certificate=False)
    except ValueError:
        certificate_disable_rejected = True
    try:
        AsyncTlsConfig("fixture.local", verify_hostname=False)
    except ValueError:
        hostname_disable_rejected = True
    try:
        AsyncTlsConfig("")
    except ValueError:
        invalid_hostname_rejected = True
    return {
        "certificate_disable_rejected": certificate_disable_rejected,
        "hostname_disable_rejected": hostname_disable_rejected,
        "invalid_hostname_rejected": invalid_hostname_rejected,
    }


def _run_failure_case(code: AsyncTlsErrorCode) -> dict[str, Any]:
    provider = FixtureTlsProvider(
        [Failure(AsyncTlsError(code, "handshake", f"fixture {code.value}"))]
    )
    connection = object()
    result = AsyncTlsService(provider).handshake(
        connection,
        AsyncTlsConfig("fixture.local"),
    ).poll()
    if result.error is None:
        raise AssertionError("TLS failure fixture unexpectedly succeeded")
    return {
        "kind": result.kind.value,
        "error": result.error.code.value,
        "connection_closed": len(provider.closed),
    }


def _run_cancel_case() -> dict[str, Any]:
    provider = FixtureTlsProvider([WantRead()])
    connection = object()
    future = AsyncTlsService(provider).handshake(
        connection,
        AsyncTlsConfig("fixture.local"),
    )
    poll = future.poll()
    cancelled = future.cancel()
    return {
        "poll_kind": poll.kind.value,
        "cancel_ok": cancelled.is_ok,
        "connection_closed": len(provider.closed),
    }


def _run_io_case() -> dict[str, Any]:
    provider = FixtureTlsProvider(
        [Ready(True)],
        read_outcomes=[WantRead(), Ready(b"reply")],
        write_outcomes=[WantWrite(), Ready(4)],
    )
    client = _ready_client(provider, max_read_write=4)

    read_future = client.read(4)
    read_first = read_future.poll()
    read_second = read_future.poll()

    write_future = client.write(b"ping")
    write_first = write_future.poll()
    write_second = write_future.poll()

    oversized = client.write(b"12345").poll()
    if oversized.error is None:
        raise AssertionError("oversized TLS write did not fail")

    first_close = client.close()
    second_close = client.close()
    return {
        "read_kinds": [read_first.kind.value, read_second.kind.value],
        "read_data": bytes(read_second.value or b"").decode("ascii"),
        "write_kinds": [write_first.kind.value, write_second.kind.value],
        "write_count": write_second.value,
        "oversize_error": oversized.error.code.value,
        "close_idempotent": first_close.is_ok and second_close.is_ok,
        "provider_close_count": len(provider.closed),
    }


def collect_results() -> dict[str, Any]:
    return {
        "handshake": _run_handshake_case(),
        "secure_config": _run_secure_config_case(),
        "hostname_failure": _run_failure_case(AsyncTlsErrorCode.HOSTNAME),
        "certificate_failure": _run_failure_case(AsyncTlsErrorCode.CERTIFICATE),
        "cancel_handshake": _run_cancel_case(),
        "io": _run_io_case(),
    }


def verify_behavioral_contract() -> tuple[bool, dict[str, Any]]:
    actual = collect_results()
    canonical = json.dumps(actual, sort_keys=True, separators=(",", ":"))
    report = {
        "schema": "s3.tls-local.correctness.v1",
        "fixture_scope": "local_provider_state_machine_no_public_internet_no_custom_crypto",
        "performance_results_valid": False,
        "performance_status": "DEFERRED_UNTIL_VETTED_NATIVE_TLS_PROVIDER_IS_BENCHMARKABLE",
        "certificate_verification_required": True,
        "hostname_verification_required": True,
        "expected": EXPECTED,
        "actual": actual,
        "actual_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "passed": actual == EXPECTED,
    }
    return report["passed"], report


if __name__ == "__main__":
    passed, report = verify_behavioral_contract()
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)
